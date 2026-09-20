#!/usr/bin/env python3
"""Package the canonical voice skill as an Agent Plugins directory in a ZIP."""

import argparse
import io
import json
from pathlib import Path
import sys
from zipfile import BadZipFile, ZIP_DEFLATED, ZipFile, ZipInfo

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / "skills" / "my-voice"
OUTPUT = BASE / "my-voice" / "my-voice.zip"
FILES = ("SKILL.md", "authored-register.md", "documentation-register.md", "examples.md")


def package_files():
    manifest = (BASE / "my-voice" / "plugin.json").read_bytes()
    metadata = json.loads(manifest)
    if metadata.get("name") != "my-voice" or metadata.get("$schema") != (
        "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    ):
        raise ValueError("Manifest must identify my-voice and Agent Plugins 1.0.0")
    actual = {path.name for path in SOURCE.iterdir() if path.name != ".DS_Store"}
    if actual != set(FILES):
        raise ValueError("Voice source file set changed; review the package file list")
    contents = {"my-voice/plugin.json": manifest}
    for name in FILES:
        path = SOURCE / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Expected a regular source file: {path}")
        data = path.read_bytes()
        if name == "SKILL.md":
            # Remove only the known client-specific field, never rewrite the body.
            parts = data.split(b"---\n", 2)
            if len(parts) != 3 or parts[0]:
                raise ValueError("Expected YAML frontmatter with LF delimiters")
            field = b"disable-model-invocation: false\n"
            lines = parts[1].splitlines(keepends=True)
            if lines.count(field) != 1:
                raise ValueError("Invocation metadata changed; review portable conversion")
            lines.remove(field)
            data = b"---\n" + b"".join(lines) + b"---\n" + parts[2]
        contents[f"my-voice/skills/my-voice/{name}"] = data
    return contents


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check the existing ZIP against source without writing")
    args = parser.parse_args()
    try:
        contents = package_files()
        if args.check:
            with ZipFile(OUTPUT) as archive:
                if sorted(archive.namelist()) != sorted(contents):
                    raise ValueError("Archive file set differs from the package")
                for name, data in contents.items():
                    if archive.read(name) != data:
                        raise ValueError(f"Archive is stale: {name}")
            print(f"Verified {len(contents)} packaged files against source: {OUTPUT}")
        else:
            # Fixed timestamps and permissions make unchanged builds reproducible.
            buffer = io.BytesIO()
            with ZipFile(buffer, "w", compression=ZIP_DEFLATED) as archive:
                for name, data in contents.items():
                    info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                    info.create_system = 3
                    info.external_attr = 0o100644 << 16
                    info.compress_type = ZIP_DEFLATED
                    archive.writestr(info, data)
            OUTPUT.write_bytes(buffer.getvalue())
            print(f"Built {OUTPUT}")
    except (OSError, ValueError, BadZipFile) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
