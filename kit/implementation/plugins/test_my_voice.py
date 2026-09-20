"""Regression checks for package preservation and Git publication transitions."""

import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

import build_my_voice as build
from publish_my_voice import git, publish, remote_ref


class VoiceReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="my-voice-test-")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.repo = self.directory / "source"
        self.repo.mkdir()
        self.base = self.repo / "kit/implementation/plugins"
        self.source = self.repo / "kit/implementation/skills/my-voice"
        shutil.copytree(build.SOURCE, self.source)
        (self.base / "my-voice").mkdir(parents=True)
        shutil.copyfile(build.BASE / "my-voice/plugin.json", self.base / "my-voice/plugin.json")
        shutil.copyfile(build.ROOT / "LICENSE", self.repo / "LICENSE")
        (self.repo / ".claude-plugin").mkdir()
        shutil.copyfile(build.ROOT / ".claude-plugin/marketplace.json", self.repo / ".claude-plugin/marketplace.json")
        patches = patch.multiple(build, ROOT=self.repo, BASE=self.base, SOURCE=self.source)
        patches.start()
        self.addCleanup(patches.stop)
        git(self.repo, "init", "--initial-branch=main")
        git(self.repo, "config", "user.name", "Release test")
        git(self.repo, "config", "user.email", "release-test@example.invalid")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-m", "Initial test source")
        self.remote = self.directory / "remote.git"
        subprocess.run(["git", "init", "--bare", str(self.remote)], check=True, capture_output=True)
        git(self.repo, "remote", "add", "origin", str(self.remote))
        git(self.repo, "push", "origin", "main")
        self.number = 0

    def commit(self, path, text):
        (self.repo / path).write_text(text)
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-m", "Update test source")
        git(self.repo, "push", "origin", "main")

    def release(self, version="0.1.1"):
        self.number += 1
        directory = self.directory / f"release-{self.number}"
        revision = git(self.repo, "rev-parse", "HEAD")
        build.write_tree(directory, build.release_files(version, revision))
        return directory

    def test_exact_skill_preservation_and_manifest_agreement(self):
        directory = self.release()
        original = (self.source / "SKILL.md").read_bytes()
        portable = directory / "skills/my-voice/SKILL.md"
        self.assertEqual(portable.read_bytes(), original.replace(b"disable-model-invocation: false\n", b"", 1))
        for name in build.FILES[1:]:
            self.assertEqual((directory / "skills/my-voice" / name).read_bytes(), (self.source / name).read_bytes())
        root = json.loads((directory / "plugin.json").read_bytes())
        claude = json.loads((directory / ".claude-plugin/plugin.json").read_bytes())
        self.assertEqual(claude, {key: value for key, value in root.items() if key != "$schema"})
        self.assertEqual(root["version"], "0.1.1")
        with ZipFile(directory / "my-voice.zip") as archive:
            expected = {"my-voice/" + path.relative_to(directory).as_posix() for path in directory.rglob("*") if path.is_file() and path.name != "my-voice.zip"}
            self.assertEqual(set(archive.namelist()), expected)
            for name in expected:
                self.assertEqual(archive.read(name), (directory / name.removeprefix("my-voice/")).read_bytes())

    def test_reproducible_files_and_zip(self):
        revision = git(self.repo, "rev-parse", "HEAD")
        first = build.release_files("0.1.1", revision)
        self.assertEqual(first, build.release_files("0.1.1", revision))
        second = build.release_files("0.1.2", revision)
        self.assertNotEqual(first["my-voice.zip"], second["my-voice.zip"])
        self.assertEqual(json.loads(first["release.json"])["payload_sha256"], json.loads(second["release.json"])["payload_sha256"])

    def test_rejects_unreviewed_source_files_and_symlinks(self):
        extra = self.source / "unreviewed.md"
        extra.write_text("Unexpected content")
        with self.assertRaises(ValueError):
            build.package_files()
        extra.unlink()
        companion = self.source / "examples.md"
        companion.unlink()
        companion.symlink_to(self.repo / "LICENSE")
        with self.assertRaises(ValueError):
            build.package_files()

    def test_rejects_invocation_metadata_drift(self):
        skill = self.source / "SKILL.md"
        skill.write_bytes(skill.read_bytes().replace(b"disable-model-invocation: false", b"disable-model-invocation: true"))
        with self.assertRaises(ValueError):
            build.package_files()

    def test_rejects_invalid_manifest_types(self):
        path = self.base / "my-voice/plugin.json"
        original = json.loads(path.read_bytes())
        for key, value in (("description", []), ("author", "Author"), ("keywords", [42])):
            path.write_bytes(build.json_bytes({**original, key: value}))
            with self.assertRaises(ValueError):
                build.package_files()

    def test_release_check_rejects_extra_files_and_symlinks(self):
        directory = self.release()
        expected = build.release_files("0.1.1", git(self.repo, "rev-parse", "HEAD"))
        extra = directory / "unexpected.txt"
        extra.write_text("Unexpected content")
        with self.assertRaises(ValueError):
            build.check_tree(directory, expected)
        extra.unlink()
        extra.symlink_to(directory / "LICENSE")
        with self.assertRaises(ValueError):
            build.check_tree(directory, expected)

    def test_rejects_invalid_release_identity_and_catalog_pin(self):
        for version in ("1", "01.2.3", "1.2.3/evil", "-1.2.3"):
            with self.assertRaises(ValueError):
                build.release_files(version, "a" * 40)
        with self.assertRaises(ValueError):
            build.release_files("0.1.1", "main")
        catalog = self.repo / ".claude-plugin/marketplace.json"
        data = json.loads(catalog.read_bytes())
        data["plugins"][0]["version"] = "0.1.1"
        catalog.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            build.validate_catalog()

    def test_refuses_overwrite_and_symlink_output(self):
        directory = self.release()
        with self.assertRaises(ValueError):
            build.write_tree(directory, {"README.md": b"overwrite"})
        link = self.directory / "linked"
        link.symlink_to(directory, target_is_directory=True)
        with self.assertRaises(ValueError):
            build.write_tree(link, {"README.md": b"overwrite"})

    def test_first_publication_and_changed_payload_advance_branch_and_tags(self):
        head = git(self.repo, "rev-parse", "HEAD")
        index = (self.repo / ".git/index").read_bytes()
        first = publish(self.repo, self.release())
        self.assertEqual(remote_ref(self.repo, "refs/tags/my-voice-v0.1.1"), first)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), head)
        self.assertEqual((self.repo / ".git/index").read_bytes(), index)
        path = "kit/implementation/skills/my-voice/examples.md"
        self.commit(path, (self.repo / path).read_text() + "\nTest release change.\n")
        second = publish(self.repo, self.release("0.1.2"))
        self.assertEqual(git(self.repo, "rev-parse", second + "^"), first)
        self.assertEqual(remote_ref(self.repo, "refs/heads/" + build.BRANCH), second)
        self.assertEqual(remote_ref(self.repo, "refs/tags/my-voice-v0.1.2"), second)
        self.assertEqual(remote_ref(self.repo, "refs/tags/my-voice-v0.1.1"), first)
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_rerun_and_documentation_only_commit_do_not_republish(self):
        first = publish(self.repo, self.release())
        self.assertEqual(publish(self.repo, self.release()), first)
        self.commit("notes.md", "Documentation only\n")
        self.assertEqual(publish(self.repo, self.release("0.1.2")), first)
        self.assertIsNone(remote_ref(self.repo, "refs/tags/my-voice-v0.1.2"))

    def test_obsolete_source_cannot_publish(self):
        release = self.release()
        old = git(self.repo, "rev-parse", "HEAD")
        self.commit("notes.md", "Newer main\n")
        git(self.repo, "checkout", "--detach", old)
        self.assertIsNone(publish(self.repo, release))
        self.assertIsNone(remote_ref(self.repo, "refs/heads/" + build.BRANCH))

    def test_dirty_source_or_tampered_release_cannot_publish(self):
        directory = self.release()
        manifest = directory / "plugin.json"
        manifest.write_bytes(manifest.read_bytes() + b" ")
        with self.assertRaises(ValueError):
            publish(self.repo, directory)
        directory = self.release()
        (self.repo / "LICENSE").write_text("Dirty source")
        with self.assertRaises(ValueError):
            publish(self.repo, directory)
        self.assertIsNone(remote_ref(self.repo, "refs/heads/" + build.BRANCH))

    def test_changed_payload_requires_new_version_and_tags_are_immutable(self):
        first = publish(self.repo, self.release())
        path = "kit/implementation/skills/my-voice/examples.md"
        self.commit(path, (self.repo / path).read_text() + "\nChanged test payload.\n")
        with self.assertRaises(ValueError):
            publish(self.repo, self.release())
        git(self.repo, "push", "origin", "HEAD:refs/tags/my-voice-v0.1.2")
        with self.assertRaises(ValueError):
            publish(self.repo, self.release("0.1.2"))
        self.assertEqual(remote_ref(self.repo, "refs/heads/" + build.BRANCH), first)


if __name__ == "__main__":
    unittest.main()
