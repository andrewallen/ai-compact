← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Plugins](../README.md) · **my-voice**

# my-voice plugin

A portable wrapper for the canonical [my-voice skill](../../skills/my-voice/SKILL.md), targeting the published [Agent Plugins 1.0.0 specification](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md). The maintained [manifest](plugin.json) declares its name, author and purpose. No MCP server or client extension is needed.

## Build and check

From the repository root, using Python 3.9 or later with no third-party dependencies:

```sh
python3 kit/implementation/plugins/build_my_voice.py
python3 kit/implementation/plugins/build_my_voice.py --check
```

The build writes `my-voice.zip` beside this document. It contains:

```text
my-voice/
├── plugin.json
└── skills/
    └── my-voice/
        ├── SKILL.md
        ├── authored-register.md
        ├── documentation-register.md
        └── examples.md
```

Extract the archive and supply its `my-voice/` directory to a client that supports Agent Plugins 1.0.0 and skills. The source directory beside this document is a build input, not a complete plugin. ZIP is a convenient transport chosen here; the standard defines the extracted directory and does not prescribe an installer or archive format.

The build uses the four files in `implementation/skills/my-voice/` and packages regular files, with no links back into the checkout. Edit those sources and rebuild. Do not maintain a second copy in this wrapper. The check verifies the exact archive file set and compares its contents with the current source after the conversion below. It is a freshness check, not a general schema validator or behavioural evaluation.

## Portable conversion and operating context

The canonical skill retains `disable-model-invocation: false` for existing client deployments. That field is outside the [Agent Skills frontmatter specification](https://agentskills.io/specification), so the portable build omits that single field. The skill body and three companion files are preserved byte for byte. The builder stops if the expected field or source file set changes, requiring a review of the packaging assumptions.

The skill's execution-only boundary and ownership checks remain in its description and body. Invocation controls belong to the host; removing a client-specific field does not establish how a different host will discover or invoke the skill.

Supply the core constitution or a condensed chat/execution contract through the host's instruction surface as described by the [deployment map](../../platforms/deployment-map.md). The plugin distributes execution craft and does not install standing instructions. Policy paths mentioned in the skill establish provenance; they do not imply access to this repository.

The manifest omits the optional package version in keeping with the repository's Git-based version policy. Its required schema identifier declares format compatibility, not a content revision. No licence grant or marketplace registration is added by packaging.

## Verification boundary

Packaging does not establish installation, discovery or writing quality in any host. The [validation and repair record](../../../../governance/evidence/2026-09-voice-plugin-validation.md) records bounded text checks and their limits. [Claude](../../platforms/claude/configuration-baseline.md) retains an earlier source revision; the standalone [Codex](../../platforms/codex/configuration-baseline.md) installation was removed at Andrew's request. A host-specific adapter or marketplace entry needs its own verified deployment route.
