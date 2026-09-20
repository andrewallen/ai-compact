#!/usr/bin/env python3
"""Build a portable voice plugin, or a complete versioned marketplace release."""

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from zipfile import BadZipFile, ZIP_DEFLATED, ZipFile, ZipInfo

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
SOURCE = BASE.parent / "skills" / "my-voice"
OUTPUT = BASE / "my-voice" / "my-voice.zip"
FILES = ("SKILL.md", "authored-register.md", "documentation-register.md", "examples.md")
REPOSITORY = "https://github.com/andrewallen/ai-compact"
BRANCH = "codex/plugin-marketplace"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def regular_bytes(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Expected a regular source file: {path}")
    return path.read_bytes()


def validate_catalog():
    catalog = json.loads(regular_bytes(ROOT / ".claude-plugin" / "marketplace.json"))
    if catalog.get("name") != "ai-compact" or not catalog.get("owner", {}).get("name"):
        raise ValueError("Unexpected marketplace identity")
    entries = catalog.get("plugins", [])
    if len(entries) != 1 or entries[0].get("name") != "my-voice":
        raise ValueError("Marketplace must expose only my-voice")
    expected = {"source": "url", "url": REPOSITORY + ".git", "ref": BRANCH}
    if entries[0].get("source") != expected or "version" in entries[0]:
        raise ValueError("Marketplace must follow the release branch without a version pin")
    return catalog


def package_files(version=None):
    manifest = regular_bytes(BASE / "my-voice" / "plugin.json")
    metadata = json.loads(manifest)
    if metadata.get("name") != "my-voice" or metadata.get("$schema") != SCHEMA:
        raise ValueError("Manifest must identify my-voice and Agent Plugins 1.0.0")
    allowed = {"$schema", "name", "description", "author", "homepage", "repository", "license", "keywords"}
    if set(metadata) - allowed:
        raise ValueError("Unexpected source manifest field; review portable packaging")
    for field in allowed - {"author", "keywords"}:
        if field in metadata and not isinstance(metadata[field], str):
            raise ValueError(f"Manifest {field} must be a string")
    author = metadata.get("author")
    if not isinstance(author, dict) or not author.get("name") or (
        set(author) - {"name", "email", "url"}
    ) or not all(isinstance(value, str) for value in author.values()):
        raise ValueError("Manifest author must contain a name and string metadata")
    keywords = metadata.get("keywords", [])
    if not isinstance(keywords, list) or not all(isinstance(value, str) for value in keywords):
        raise ValueError("Manifest keywords must be a list of strings")
    if version is not None:
        if not re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", version):
            raise ValueError("Release version must have three non-negative numeric parts")
        metadata["version"] = version
    actual = {path.name for path in SOURCE.iterdir() if path.name != ".DS_Store"}
    if actual != set(FILES):
        raise ValueError("Voice source file set changed; review the package file list")
    claude = {key: value for key, value in metadata.items() if key != "$schema"}
    contents = {
        "my-voice/plugin.json": json_bytes(metadata),
        "my-voice/.claude-plugin/plugin.json": json_bytes(claude),
        "my-voice/LICENSE": regular_bytes(ROOT / "LICENSE"),
        "my-voice/README.md": (
            "# my-voice\n\n"
            "Andrew Allen's writing craft for owned personal output and authorised factual documentation.\n\n"
            f"[Source and installation guide]({REPOSITORY}/blob/main/kit/implementation/plugins/my-voice/README.md).\n\n"
            "This generated package contains one skill and its three companion files. "
            "The portable copy omits the client-specific disable-model-invocation frontmatter field; "
            "the skill body and companion files are unchanged.\n\n"
            "Supply the core constitution or the supported condensed contract separately through the host's "
            "instruction surface. The plugin supplies execution craft, not standing instructions.\n\n"
            "Original material is by Andrew Allen, distributed under [CC BY 4.0](LICENSE). "
            "Except for attribution required by the licence, no permission is granted to use Andrew Allen's "
            "name, identity or personal information, or to imply endorsement.\n"
        ).encode(),
    }
    for name in FILES:
        path = SOURCE / name
        data = regular_bytes(path)
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


def zip_bytes(contents):
    # Fixed ordering, timestamps and permissions make unchanged builds reproducible.
    buffer = io.BytesIO()
    with ZipFile(buffer, "w", compression=ZIP_DEFLATED) as archive:
        for name, data in sorted(contents.items()):
            info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, data)
    return buffer.getvalue()


def fingerprint(contents):
    return hashlib.sha256(json_bytes({
        name: hashlib.sha256(data).hexdigest() for name, data in sorted(contents.items())
    })).hexdigest()


def release_files(version, revision):
    validate_catalog()
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Source revision must be a full Git commit SHA")
    package = {name.removeprefix("my-voice/"): data for name, data in package_files(version).items()}
    package["release.json"] = json_bytes({
        "name": "my-voice",
        "version": version,
        "source_repository": REPOSITORY,
        "source_revision": revision,
        "payload_sha256": fingerprint(package_files()),
        "files": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(package.items())},
    })
    archive = zip_bytes({f"my-voice/{name}": data for name, data in package.items()})
    return {**package, "my-voice.zip": archive}


def check_tree(directory, expected):
    paths = list(directory.rglob("*"))
    if any(path.is_symlink() for path in paths) or directory.is_symlink():
        raise ValueError("Release must not contain symlinks")
    actual = {path.relative_to(directory).as_posix() for path in paths if path.is_file()}
    if actual != set(expected):
        raise ValueError("Release file set differs from the package")
    for name, data in expected.items():
        if (directory / name).read_bytes() != data:
            raise ValueError(f"Release is stale: {name}")


def write_tree(directory, contents):
    if directory.is_symlink():
        raise ValueError("Release output must not follow a symlink")
    if directory.exists() and any(directory.iterdir()):
        raise ValueError("Release output must be a new or empty directory")
    directory.mkdir(parents=True, exist_ok=True)
    for name, data in contents.items():
        path = directory / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check existing output against source without writing")
    parser.add_argument("--release-dir", type=Path, help="Write a complete release to a new/empty directory")
    parser.add_argument("--version", help="Numeric release version, required with --release-dir")
    parser.add_argument("--source-revision", help="Full source commit SHA, required with --release-dir")
    args = parser.parse_args()
    try:
        validate_catalog()
        if args.release_dir:
            if not args.version or not args.source_revision:
                raise ValueError("A release needs --version and --source-revision")
            contents = release_files(args.version, args.source_revision)
            if args.check:
                check_tree(args.release_dir, contents)
                print(f"Verified release {args.version}: {args.release_dir}")
            else:
                write_tree(args.release_dir, contents)
                print(f"Built release {args.version}: {args.release_dir}")
        elif args.version or args.source_revision:
            raise ValueError("Release metadata requires --release-dir")
        elif args.check:
            contents = package_files()
            with ZipFile(OUTPUT) as archive:
                if sorted(archive.namelist()) != sorted(contents):
                    raise ValueError("Archive file set differs from the package")
                for name, data in contents.items():
                    if archive.read(name) != data:
                        raise ValueError(f"Archive is stale: {name}")
            print(f"Verified {len(contents)} packaged files against source: {OUTPUT}")
        else:
            OUTPUT.write_bytes(zip_bytes(package_files()))
            print(f"Built {OUTPUT}")
    except (OSError, ValueError, BadZipFile) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
