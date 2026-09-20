#!/usr/bin/env python3
"""Publish verified generated files without checking out or force-pushing a branch."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

from build_my_voice import BRANCH, check_tree, release_files


def git(repo, *args, data=None, env=None):
    result = subprocess.run(
        ["git", "-C", str(repo), *args], input=data, capture_output=True, check=True, env=env
    )
    return result.stdout.decode().strip()


def remote_ref(repo, ref):
    result = git(repo, "ls-remote", "origin", ref)
    return result.split()[0] if result else None


def publish(repo, directory):
    record = json.loads((directory / "release.json").read_bytes())
    version, revision = record["version"], record["source_revision"]
    check_tree(directory, release_files(version, revision))
    if git(repo, "rev-parse", "HEAD") != revision:
        raise ValueError("Release provenance differs from the source checkout")
    if git(repo, "status", "--porcelain", "--untracked-files=no"):
        raise ValueError("Publication requires a clean source checkout")
    # A rerun of an older workflow must never replace a newer main revision.
    if remote_ref(repo, "refs/heads/main") != revision:
        print("Skipped: source revision is no longer the current main commit")
        return None
    branch_ref = f"refs/heads/{BRANCH}"
    previous = remote_ref(repo, branch_ref)
    if previous:
        git(repo, "fetch", "--no-tags", "origin", branch_ref)
        previous = git(repo, "rev-parse", "FETCH_HEAD")
        old = json.loads(git(repo, "show", f"{previous}:release.json"))
        if old["payload_sha256"] == record["payload_sha256"]:
            print(f"Unchanged payload; retaining {old['version']} at {previous}")
            return previous
        if tuple(map(int, version.split("."))) <= tuple(map(int, old["version"].split("."))):
            raise ValueError("A changed payload requires a higher release version")
    tag_ref = f"refs/tags/my-voice-v{version}"
    if remote_ref(repo, tag_ref):
        raise ValueError(f"Immutable release tag already exists: {tag_ref}")

    # Use a private index and Git objects; leave the source tree, index and HEAD alone.
    with tempfile.TemporaryDirectory(prefix="my-voice-index-") as temporary:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(temporary) / "index"))
        git(repo, "read-tree", "--empty", env=env)
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                name = path.relative_to(directory).as_posix()
                blob = git(repo, "hash-object", "-w", "--stdin", data=path.read_bytes())
                git(repo, "update-index", "--add", "--cacheinfo", "100644", blob, name, env=env)
        tree = git(repo, "write-tree", env=env)
    parents = ["-p", previous] if previous else []
    commit = git(repo, "commit-tree", tree, *parents, "-m", f"Publish my-voice {version} from {revision}")
    if remote_ref(repo, "refs/heads/main") != revision:
        print("Skipped: main changed while the release was prepared")
        return None
    # Neither ref is forced. A competing publisher or tag collision rejects the whole push.
    git(repo, "push", "--atomic", "origin", f"{commit}:{branch_ref}", f"{commit}:{tag_ref}")
    print(f"Published my-voice {version}: {commit}")
    return commit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--release-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        publish(args.source_repo, args.release_dir)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        # Command output may contain private remote credentials; retain only the failing command's status.
        parser.exit(1, f"Publication failed: {exc}\n")


if __name__ == "__main__":
    main()
