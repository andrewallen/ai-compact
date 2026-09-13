#!/usr/bin/env python3
"""Distribute reviewed contract bodies; never derive policy from the constitution."""

import argparse
import os
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent
INFO_START = "<!-- generated-contract-info:start -->"
INFO_END = "<!-- generated-contract-info:end -->"
CHAT_BUDGET = 5000  # Repository budget, not a verified current product limit.
GROUPS = (
    ("chat-contract.md", "<!-- paste-ready:start -->", "<!-- paste-ready:end -->",
     ("claude/personal-preferences.md", "chatgpt/custom-instructions.md",
      "gemini/saved-instructions.md")),
    ("execution-contract.md", "<!-- derived-minimal-contract:start -->",
     "<!-- derived-minimal-contract:end -->",
     ("codex/README.md", "claude/code/README.md", "copilot-cli/README.md",
      "hermes/README.md")),
)


def region(text, start, end, label):
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"{label}: expected exactly one pair of {start} / {end}")
    left = text.index(start) + len(start)
    right = text.index(end)
    if left >= right:
        raise ValueError(f"{label}: reversed or empty marker region")
    return left, right


def replace_region(text, start, end, body, label):
    left, right = region(text, start, end, label)
    return text[:left] + "\n" + body + "\n" + text[right:]


def read(path):
    # Preserve wrappers exactly, including newline bytes.
    return path.read_bytes().decode("utf-8")


def planned_updates():
    updates = []
    for source_name, start, end, targets in GROUPS:
        source = BASE / source_name
        text = read(source)
        left, right = region(text, start, end, source_name)
        body = text[left:right].strip()
        if not body:
            raise ValueError(f"{source_name}: empty contract")
        versions = re.findall(r"^Version: (.+)$", text, re.MULTILINE)
        if len(versions) != 1 or not versions[0].strip():
            raise ValueError(f"{source_name}: expected one source version")
        if source_name == "chat-contract.md" and len(body) > CHAT_BUDGET:
            raise ValueError(f"{source_name}: {len(body)} characters exceed the "
                             f"{CHAT_BUDGET}-character repository budget")
        for target_name in targets:
            target = BASE / target_name
            if target.is_symlink() or target.resolve().parent != target.parent.resolve():
                raise ValueError(f"{target_name}: expected a regular local target")
            if not target.resolve().is_relative_to(BASE.resolve()):
                raise ValueError(f"{target_name}: target escapes platform directory")
            before = read(target)
            body_left, body_right = region(before, start, end, target_name)
            info_left, info_right = region(before, INFO_START, INFO_END, target_name)
            if not (info_right < body_left or body_right < info_left):
                raise ValueError(f"{target_name}: overlapping managed regions")
            relative_source = Path(os.path.relpath(source, target.parent)).as_posix()
            info = (f"Generated from [{source_name}]({relative_source}), source version "
                    f"`{versions[0]}`. Edit that source, not this copy. "
                    f"Paste-ready body: {len(body):,} characters; markers and metadata excluded.")
            after = replace_region(before, start, end, body, target_name)
            after = replace_region(after, INFO_START, INFO_END, info, target_name)
            updates.append((target, before, after))
    return updates


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Report drift without writing")
    mode.add_argument("--write", action="store_true", help="Refresh only managed regions")
    args = parser.parse_args()
    try:
        # Validate every source and target before any write.
        updates = planned_updates()
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Contract sync error: {exc}", file=sys.stderr)
        return 2
    stale = [(path, before, after) for path, before, after in updates if before != after]
    if args.check:
        for path, _, _ in stale:
            print(f"DRIFT {path.relative_to(BASE)}")
        if not stale:
            print(f"All {len(updates)} generated contract copies are current.")
        return 1 if stale else 0
    try:
        for path, before, after in stale:
            if read(path) != before:
                raise ValueError(f"{path.relative_to(BASE)} changed during generation; rerun")
            path.write_bytes(after.encode("utf-8"))
            print(f"UPDATED {path.relative_to(BASE)}")
    except (OSError, ValueError) as exc:
        print(f"Contract sync stopped: {exc}. Earlier reported updates may have been written.",
              file=sys.stderr)
        return 2
    print(f"Updated {len(stale)} of {len(updates)} copies; product wrappers preserved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
