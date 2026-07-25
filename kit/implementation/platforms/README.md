← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Platforms** · [Governance](../../../governance/README.md)

# Platforms

Product-specific configurations and references that deploy the operating contract to individual AI tools. Platform files are deployments of the constitution files, not independent sources of truth.

## File Types

- **Preferences / custom instructions** — condensed operating contracts pasted into a tool's always-on settings.
- **Mode configs** — capability-specific settings for surfaces that need them, such as Cowork.
- **Templates** — starting points for project instructions.
- **Configuration references** — guidance for agent and CLI tools that should carry a minimal derived contract or read the constitution files directly when deeper operating context is needed.

## Folder Structure

```
kit/implementation/platforms/
├── README.md
├── deployment-map.md
├── claude/
│   ├── personal-preferences.md
│   ├── chat/template-chat-project.md
│   ├── cowork/global-instructions.md
│   ├── cowork/template-cowork-project.md
│   └── code/
│       └── README.md
├── chatgpt/
│   ├── README.md
│   └── custom-instructions.md
├── gemini/
│   ├── README.md
│   └── saved-instructions.md
├── codex/
│   └── README.md
├── copilot-cli/
│   └── README.md
└── hermes/
    └── README.md
```

## Surface Inventory

| Surface | File | Deploys to | Purpose |
|---|---|---|---|
| All products | [deployment map](deployment-map.md) | Reference | Maps kit components to every supported product and mode. |
| Claude | [Claude index](claude/README.md) | Reference | Routes Chat, Cowork and Code configuration. |
| Claude Chat | [personal preferences](claude/personal-preferences.md) | Claude settings | Condensed operating contract for every Claude chat. |
| Claude Chat projects | [project template](claude/chat/template-chat-project.md) | Project instructions | Starting point for scoped chat projects. |
| Claude Cowork | [global instructions](claude/cowork/global-instructions.md) | Cowork global instructions | Filesystem safety, connector caution, planning discipline. |
| Claude Cowork projects | [project template](claude/cowork/template-cowork-project.md) | Project instructions | Starting point for Cowork projects. |
| Claude Code | [configuration guide](claude/code/README.md) | Reference | Current configuration guidance for Code surfaces and CLI. |
| ChatGPT | [custom instructions](chatgpt/custom-instructions.md) | ChatGPT custom instructions | Standalone condensed contract. |
| ChatGPT | [configuration guide](chatgpt/README.md) | Reference | Setup, memory posture, project usage. |
| Gemini | [Instructions for Gemini](gemini/saved-instructions.md) | Gemini standing instructions | Standalone condensed contract. |
| Gemini | [configuration guide](gemini/README.md) | Reference | Setup, memory/activity posture, context usage. |
| Codex | [configuration guide](codex/README.md) | Reference | How to use the constitution files without deploying AGENTS.md. |
| Copilot CLI | [configuration guide](copilot-cli/README.md) | Reference | GitHub-native agent usage with kit references. |
| Hermes | [configuration guide](hermes/README.md) | Reference | Persistent-agent usage with kit references and open persona/redaction decisions. |

## Configuration Principles

Configurable chat surfaces should have enough standing instruction to work when no files are attached. Those settings should also defer clearly to the constitution files when they are present.

Agent and CLI surfaces should carry a minimal derived contract and read the source files directly when deeper operating context is needed. At this time, the repo does not recommend creating new `CLAUDE.md` or `AGENTS.md` deployment files for those surfaces. The root files with those names govern this repo only.

Platform files carry only the minimal voice boundary from the constitution files: the assistant uses its own neutral analytical voice when thinking with Andrew, and Andrew's voice is reserved for output produced on his behalf. The platform layer does not instruct tools to load voice material; that material is supplied separately when needed.

## Adding a New Product

1. Decide whether the product is a configurable chat surface or an agent/CLI reference surface.
2. Create a folder under `kit/implementation/platforms/`.
3. For configurable chat surfaces, add a standalone condensed contract plus a README.
4. For agent/CLI surfaces, add a README that carries the minimal derived contract and points to the constitution files for deeper work.
5. Update the root README and `kit/implementation/platforms/deployment-map.md`.

Version: 2026.07.13 @ 1.5
