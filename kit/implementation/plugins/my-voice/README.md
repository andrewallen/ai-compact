← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Plugins](../README.md) · **my-voice**

# my-voice plugin

A portable wrapper for the canonical [my-voice skill](../../skills/my-voice/SKILL.md), targeting [Agent Plugins 1.0.0](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md). The [manifest](plugin.json) owns package identity and metadata. The [marketplace catalogue](../../../../.claude-plugin/marketplace.json) exposes it to Claude, GitHub Copilot and Codex.

The ordinary repository URL is the marketplace address: `https://github.com/andrewallen/ai-compact`. Its catalogue follows the generated package at the root of `codex/plugin-marketplace`. There is one maintained skill source; no client-specific craft copies, MCP servers, hooks or automatic account installation are added.

## Install and update

These are setup instructions, not a claim that the package is installed in any account. Supply the operating context described below and check for an older standalone copy before installing. The current saved-state observations remain in the [Claude](../../platforms/claude/configuration-baseline.md) and [Codex](../../platforms/codex/configuration-baseline.md) baselines.

### Claude Code

```text
/plugin marketplace add andrewallen/ai-compact
/plugin install my-voice@ai-compact
```

In `/plugin`, select **Marketplaces → ai-compact → Enable auto-update**. Third-party marketplaces have automatic updates disabled by default. Claude Code checks after startup; a refreshed plugin becomes active after `/reload-plugins` or on the next launch. For a manual refresh, use `/plugin marketplace update ai-compact`, then `/plugin update my-voice@ai-compact`.

The generated `.claude-plugin/plugin.json` supplies Claude's compatibility entry point. Its metadata is derived from the portable manifest. See [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) and [automatic updates](https://code.claude.com/docs/en/discover-plugins#configure-auto-updates).

### Claude Desktop and Cowork

Open **Customize → Plugins → Personal plugins → + → Add marketplace → Add from a repository**, add `https://github.com/andrewallen/ai-compact`, then install my-voice. In Cowork, open the Cowork tab before Customize.

[Personal marketplace documentation](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) confirms repository installation but does not specify its automatic update cadence. Verify refresh and the installed version in the actual client. Claude's separate [organisation sync](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization) requires a private/internal marketplace repository and a merged PR with a version bump for automatic sync. This public repository's publication workflow does not establish that managed route.

### GitHub Copilot CLI

```sh
copilot plugin marketplace add andrewallen/ai-compact
copilot plugin install my-voice@ai-compact
```

For automatic updates, merge the following marketplace entry into the user's Copilot settings, preserving existing entries:

```json
{
  "extraKnownMarketplaces": {
    "ai-compact": {
      "source": {"source": "github", "repo": "andrewallen/ai-compact"},
      "autoUpdate": true
    }
  }
}
```

The [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) documents this opt-in for interactive and `-p` sessions. It is honoured from user or managed settings; repository settings cannot enable it. Global update controls and managed policy can still prevent it. SDK/server sessions do not use this automatic route. For an explicit refresh:

```sh
copilot plugin marketplace update ai-compact
copilot plugin update my-voice
```

### GitHub Copilot in VS Code

Add `andrewallen/ai-compact` to `chat.plugins.marketplaces`, preserving other entries. Find my-voice in the Agent Plugins view and install it. With `extensions.autoUpdate` enabled, VS Code checks every 24 hours; **Extensions: Check for Extension Updates** requests an earlier check. See [VS Code plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins).

### Codex

```sh
codex plugin marketplace add andrewallen/ai-compact
codex plugin add my-voice@ai-compact
```

For an explicit refresh, update the marketplace snapshot and refresh the installed plugin:

```sh
codex plugin marketplace upgrade ai-compact
codex plugin add my-voice@ai-compact
```

Start a new task after refreshing. Current [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins) supports the portable root manifest and the Claude-compatible catalogue. The local CLI exposes the commands above; an unattended personal update cadence has not been established. OpenAI's separate [workspace marketplace import](https://learn.chatgpt.com/docs/enterprise/plugin-management) has daily automatic sync, subject to workspace administration. A native Codex catalogue is unnecessary for this single shared entry.

## Publication from GitHub

The [workflow](../../../../.github/workflows/my-voice-marketplace.yml) runs validation on pull requests, pushes to `main` and manual dispatch. Only a successful run from this repository's `main` may publish. It uses the repository's built-in Actions token with write permission restricted to the publishing job; no separate personal token is required.

Every main push is checked, avoiding missed releases when a later documentation commit supersedes a queued build. The [publisher](../publish_my_voice.py) compares the generated payload with the latest release and skips identical content. Relevant skill, metadata, licence or builder-output changes produce a release. Package versions are `0.1.<workflow run number>`; gaps are expected and do not indicate missed releases. Rerunning unchanged content retains the existing version.

Publication atomically advances `codex/plugin-marketplace` and creates `my-voice-v<version>`. Branch history is retained and tags are never overwritten. An obsolete run cannot publish after a newer main revision is visible. GitHub branch/tag rules must permit these generated refs. Hosts follow the branch through the catalogue's Git URL source; each host still controls refresh and activation.

The source catalogue deliberately omits a plugin version, so it cannot pin hosts to a stale release. Both manifests in the published package carry the same generated version. The generated package's `release.json` records the exact source commit, payload fingerprint and file hashes. It also carries a reproducible ZIP, available from the branch or an immutable version tag.

For rollback, revert the relevant source change through the normal review process and publish it as a newer version. For a fixed historical installation, select the corresponding release tag using the host's supported Git-source controls. Do not move an existing tag or reset the distribution branch. If a run fails, inspect Actions and run the workflow again from the current `main`; publication failures leave the previous release available. A first publication must succeed before the marketplace entry can be installed.

## Build and check

From the repository root, using Python 3.9 or later with no third-party dependencies:

```sh
python3 kit/implementation/plugins/build_my_voice.py
python3 kit/implementation/plugins/build_my_voice.py --check
```

The local build writes an unversioned `my-voice.zip` beside this document. It contains:

```text
my-voice/
├── plugin.json
├── .claude-plugin/plugin.json
├── LICENSE
├── README.md
└── skills/
    └── my-voice/
        ├── SKILL.md
        ├── authored-register.md
        ├── documentation-register.md
        └── examples.md
```

Extract the archive for local inspection or a manual upload. The source directory beside this document remains a build input. The distribution branch contains the complete plugin. ZIP is a transport choice; the standard defines the extracted directory and does not prescribe an installer.

The build uses the four canonical files and packages regular files without links back into the checkout. For a complete local release, choose a new or empty directory and supply a version and full source SHA:

```sh
python3 kit/implementation/plugins/build_my_voice.py \
  --release-dir /tmp/my-voice-release \
  --version 0.1.1 --source-revision "$(git rev-parse HEAD)"
python3 kit/implementation/plugins/build_my_voice.py --check \
  --release-dir /tmp/my-voice-release \
  --version 0.1.1 --source-revision "$(git rev-parse HEAD)"
python3 -m unittest discover -s kit/implementation/plugins -p 'test_*.py' -v
```

The check compares the exact file set and contents. Regression tests exercise source preservation, reproducibility and release transitions using temporary local Git repositories. They do not require credentials or modify host installations. Publication additionally requires a clean checkout and verifies the source revision against remote `main`.

## Portable conversion and operating context

The canonical skill retains `disable-model-invocation: false` for existing client deployments. That field is outside the [Agent Skills frontmatter specification](https://agentskills.io/specification), so the portable build omits that single field. The skill body and three companion files are preserved byte for byte. The builder stops if the expected field or source file set changes, requiring a review of the packaging assumptions.

The skill's execution-only boundary and ownership checks remain in its description and body. Invocation controls belong to the host; removing a client-specific field does not establish how a different host will discover or invoke the skill.

Supply the core constitution or a condensed chat/execution contract through the host's instruction surface as described by the [deployment map](../../platforms/deployment-map.md). The plugin distributes execution craft and does not install standing instructions. Policy paths mentioned in the skill establish provenance; they do not imply access to this repository.

The maintained manifest remains unversioned. The publisher generates package versions solely for host update detection, as recorded in [ADR-013](../../../../governance/decisions/adr-013-generated-plugin-marketplace.md). Its schema identifier declares format compatibility. Packaging carries the repository's existing CC BY 4.0 licence and attribution; it introduces no new licence grant or endorsement.

## Verification boundary

Packaging and publication do not establish account installation, discovery or writing quality. The [marketplace record](../../../../governance/evidence/2026-09-voice-marketplace.md) records build, release and host checks. The earlier [voice validation](../../../../governance/evidence/2026-09-voice-plugin-validation.md) records bounded text probes. Claude's existing skill installation retains an earlier source revision, and the standalone Codex installation remains removed unless a separate deployment is requested.
