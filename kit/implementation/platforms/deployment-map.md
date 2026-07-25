← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Platforms](README.md) · **Deployment map**

# Deployment Map

How AI Compact deploys to each product and surface. Update this when products change their configuration model. The constitution files do not change for platform reasons.

## Architecture Overview

The kit is a versioned source of truth for identity, calibration, operating behaviour and output craft across Claude Chat, Claude Cowork, Claude Code, ChatGPT, Gemini, Codex, Copilot CLI and Hermes.

## Kit Components

| Component | What it carries | Where it deploys |
|---|---|---|
| Constitution files | Identity, calibration, operating contract, professional overlay. Model-agnostic markdown. | Attached to conversations/projects, read from the filesystem by local agents, or attached and pasted directly where filesystem access is not available. |
| Platform prompts | Condensed operating contracts tailored to a product's standing-instruction field. | Claude preferences, ChatGPT custom instructions, Instructions for Gemini. |
| Mode configs | Safety and workflow rules for capability-specific modes. | Claude Cowork global instructions. |
| Skills | Standard SKILL.md methodology and output craft. | Supplied separately when a task needs the skill; not embedded in platform configuration. |
| Configuration references | Guidance for tools that should read the kit directly. | Claude Code, Codex, Copilot CLI, Hermes. |

## Surface Tiers

| Tier | Surfaces | Configuration model |
|---|---|---|
| Configurable chat | Claude Chat, Claude Cowork, ChatGPT, Gemini | Always-on condensed contract plus optional full constitution files. |
| Agent and CLI | Claude Code, Codex, Copilot CLI, Hermes | Carry a minimal derived contract and read the constitution files from this repo for deeper work. |
| Source of truth | This repo | Canonical files and documentation. |

## Claude

### Chat

[Claude personal preferences](claude/personal-preferences.md) is pasted into Claude's profile settings. It applies across Claude chat surfaces and carries the condensed operating contract: mode detection, expansion function, voice principles and sensitivity flagging.

For sustained chat work, use the [chat project template](claude/chat/template-chat-project.md) as project instructions and load the constitution files into the project:

- `kit/constitution/00-bootstrap.md`
- `kit/constitution/01-calibration.md`
- `kit/constitution/02-operating-contract.md`
- `kit/constitution/03-professional-overlay.md` only when relevant

### Cowork

[Cowork global instructions](claude/cowork/global-instructions.md) is pasted into Cowork global instructions. It governs filesystem safety, connector caution, planning discipline and persistent instruction changes. Cowork defaults toward execution because it is an agentic workbench, but the expansion function still applies.

The [Cowork project template](claude/cowork/template-cowork-project.md) is the project-level starting point.

### Code

Claude Code covers web, desktop, mobile and CLI.

Current recommendation: do not create new project or global `CLAUDE.md` files as the general configuration method. Instead, use the minimal derived contract in the platform README, or work from a checkout of this repo and have Claude Code read the constitution files directly for deeper work.

The root `CLAUDE.md` and `AGENTS.md` in this repo are working instructions for maintaining the kit itself. They are not the current deployment pattern for other projects.

Project-level `CLAUDE.md` templates are not part of this deployment model.

## ChatGPT

ChatGPT is the generalist surface with product-managed ambient memory.

Configuration:

- Paste [custom-instructions.md](chatgpt/custom-instructions.md) into ChatGPT custom instructions.
- Use ChatGPT Projects for sustained work.
- Upload the constitution files to projects or conversations when depth is needed.
- Keep voice reference material separate from platform configuration; the platform prompt carries only the neutral-partner / Andrew-output boundary.

## Gemini

Gemini is the Google-adjacent generalist surface.

Configuration:

- Enable Instructions for Gemini if available.
- Paste [saved-instructions.md](gemini/saved-instructions.md).
- Attach or paste constitution files when depth is needed.
- Keep voice reference material separate from platform configuration; the standing instruction carries only the neutral-partner / Andrew-output boundary.

## Codex

Codex is the local engineering, repo, browser and audit harness.

Configuration reference:

- Point Codex at this repo.
- Use the minimal derived contract in the platform README, or have it read the constitution files for deeper working context.
- Do not populate a global `AGENTS.md` as part of this deployment pattern; the root `AGENTS.md` governs this repository only.

## Copilot CLI

Copilot CLI is the GitHub-native coding surface.

Configuration reference:

- Run from a checkout that can read this repo, or provide explicit file paths.
- Use the minimal derived contract in the platform README, or have the agent read the constitution files when deeper operating context is needed.
- Do not create an `AGENTS.md` deployment file for this configuration.

## Hermes

Hermes is the persistent personal-agent, memory, messaging and automation surface.

Configuration reference:

- Point Hermes at this repo where possible.
- Use the minimal derived contract in the platform README, or have it read the constitution files for deeper operating context.
- Keep Hermes-specific memory, redaction, messaging and cron policy in Hermes configuration, not in this repo.

## Capability by Surface

| Capability | Claude Chat/Cowork | ChatGPT | Gemini | Agent/CLI surfaces |
|---|---|---|---|---|
| Standing condensed contract | Claude preferences / Cowork global instructions | Custom instructions | Instructions for Gemini | Tool-specific where supported |
| Full constitution files | Project knowledge, upload, filesystem | Project files or attachments | Attach or paste | Read from repo checkout |
| Professional overlay | Load only when relevant | Attach only when relevant | Attach only when relevant | Read only when relevant |
| Voice boundary | Neutral partner voice for thinking; Andrew's voice only for output on his behalf | Same | Same | Same |
| Ambient memory and history | Product-managed through account settings | Enabled, periodically reviewed; Temporary Chat when isolation is needed | Memory and activity retained per product settings | Tool-specific |
| Deliberate persistent changes | Explicit approval for tool-mediated changes | Explicit approval for user-visible artefacts | Explicit approval for user-visible artefacts | Explicit approval for files, instructions, store entries and equivalent artefacts |
| External actions | Cowork connector controls apply | Product-specific | Product-specific | Tool-specific |

## Principles

- **Constitution files are the source of truth.** Platform prompts are derived and condensed.
- **Standalone prompts work without attachments.** Chat surfaces need enough instruction to behave well when no constitution files are loaded.
- **Constitution files take precedence when present.** Platform prompts must state this clearly.
- **Platform files do not depend on the constitution being loaded.** They work as minimal derived contracts, while deferring when the full constitution files are present.
- **Voice material stays outside platform configuration.** Platform files carry only the neutral-partner / Andrew-output boundary; execution voice material is supplied separately.
- **Standard skill format only.** Skills remain SKILL.md folders. The repo does not create alternate formats.
- **Deliberate persistent changes require approval.** This includes project instructions, saved instructions, global agent files, knowledge-store entries, explicit user-visible memory entries, SOUL.md-class files and equivalent standing context.
- **Ambient product memory is settings-governed.** Platform adapters document whether it is enabled, how it is reviewed and how to start an isolated conversation. Standing prompts do not claim control over automatic retention or inference.
- **Root maintenance files are not deployment files.** `CLAUDE.md` and `AGENTS.md` govern this repository only; platform guidance does not treat them as the general configuration pattern.
- **Security settings are tool-side.** Credentials, trusted roots, redaction and dependency health belong in the products that hold them and must never be copied into this repository.

Version: 2026.07.25 @ 3.0
