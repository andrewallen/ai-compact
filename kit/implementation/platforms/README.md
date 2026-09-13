← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Platforms** · [Governance](../../../governance/README.md)

# Platforms

Product-specific guidance for deploying the operating contract and configuring selected capabilities. Instruction bodies derive from the constitution; capability choices come from the [skills catalogue](../skills/README.md). Platform guides own the supported controls and distinguish adopted targets from verified deployment.

The [September alignment review](../../../governance/evidence/2026-09-constitution-alignment.md) records the source rewrite and static review. The later [Claude deployment record](../../../governance/evidence/2026-09-claude-deployment.md) verifies saved chat instructions, the Cowork addendum and the enabled my-voice v2 package. Other product references remain intended configuration guidance unless supported by their own deployment evidence.

## File Types

- **Preferences / custom instructions** — condensed operating contracts pasted into a tool's always-on settings.
- **Mode configs** — capability-specific settings for surfaces that need them, such as Cowork.
- **Templates** — starting points for project instructions.
- **Configuration references** — guidance for agent and CLI tools that should carry a minimal derived contract or read the constitution files directly when deeper operating context is needed.
- **Configuration baselines** — delivery of adopted capability choices, saved settings and verification limits. [Claude](claude/configuration-baseline.md) retains earlier verified observations; [Codex](codex/configuration-baseline.md) records an unverified live target. These are not runtime instructions.

## Folder Structure

```
kit/implementation/platforms/
├── README.md
├── deployment-map.md
├── chat-contract.md
├── execution-contract.md
├── contract-maintenance.md
├── sync_contracts.py
├── model-guidance.md
├── claude/
│   ├── README.md
│   ├── configuration-baseline.md
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
│   ├── README.md
│   └── configuration-baseline.md
├── copilot-cli/
│   └── README.md
├── hermes/
│   └── README.md
├── grok/
│   └── README.md
└── opencode/
    └── README.md
```

## Surface Inventory

| Surface | File | Deploys to | Purpose |
|---|---|---|---|
| All products | [deployment map](deployment-map.md) | Reference | Maps kit components to every supported product and mode. |
| Shared chat | [chat contract](chat-contract.md) | Authored derivation | Canonical body for the three generated chat adapters. |
| Maintenance | [contract maintenance](contract-maintenance.md) and [distribution script](sync_contracts.py) | Maintenance only | Coverage map, loading combinations and deterministic distribution. |
| Defined tasks | [execution contract](execution-contract.md) | Source derivation | Shared bounded-execution contract and task handover fields. |
| Multiple models | [model guidance](model-guidance.md) | Reference | Dated vendor observations, host distinctions and proposed steering. |
| Grok | [configuration guide](grok/README.md) | Reference | Applying the shared contract through the actual host. |
| OpenCode and Go | [configuration guide](opencode/README.md) | Reference | Instruction composition, model access and verification boundaries. |
| Claude | [Configuration baseline](claude/configuration-baseline.md) | Reference | Target capability controls, last verified settings and deployment alignment. |
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
| Codex | [configuration baseline](codex/configuration-baseline.md) | Reference | Target native and optional capability configuration; live state unverified. |
| Copilot CLI | [configuration guide](copilot-cli/README.md) | Reference | GitHub-native agent usage with kit references. |
| Hermes | [configuration guide](hermes/README.md) | Reference | Persistent-agent usage with kit references and open persona/redaction decisions. |

## Configuration Principles

Configurable chat surfaces should have enough standing instruction to work when no files are attached. Those settings should also defer clearly to the constitution files when they are present.

Agent and CLI surfaces should carry a minimal derived contract and read the source files directly when deeper operating context is needed. At this time, the repo does not recommend creating new `CLAUDE.md` or `AGENTS.md` deployment files for those surfaces. The root files with those names govern this repo only.

Shared derivations carry the constitutional voice boundary, a compact writing standard and durable vocabulary constraints. Detailed craft remains in the voice skill. Product wrappers add deployment guidance; generated bodies are edited only through their shared sources. [Contract maintenance](contract-maintenance.md) defines coverage, loading combinations and the check/write commands. Cowork is an addendum supplied alongside a base contract, not a third standalone derivation.

## Adding a New Product

1. Decide whether the product is a configurable chat surface or an agent/CLI reference surface.
2. Create a folder under `kit/implementation/platforms/`.
3. Reference the appropriate shared derivation. If a detached copy is needed, add its marked body and metadata regions and register the destination in `sync_contracts.py`; do not author another copy independently.
4. Put product-specific configuration and genuine additional safeguards in the wrapper or addendum. Document the required base context.
5. Update this index, the root overview and deployment map, then run the distribution check.

Version: 2026.09.13 @ 1.10
