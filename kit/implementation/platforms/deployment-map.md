← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Platforms](README.md) · **Deployment map**

# Deployment Map

How AI Compact deploys to each product and surface. Update this when products change their configuration model. The constitution files do not change for platform reasons.

## Architecture Overview

The kit is a versioned source of truth for identity, calibration, operating behaviour and output craft across Claude Chat, Claude Cowork, Claude Code, ChatGPT, Gemini, Codex, Copilot CLI, Hermes, Grok and OpenCode/Go.

## Kit Components

| Component | What it carries | Where it deploys |
|---|---|---|
| Constitution files | Identity, calibration, operating contract, professional overlay. Model-agnostic markdown. | Attached to conversations/projects, read from the filesystem by local agents, or attached and pasted directly where filesystem access is not available. |
| Platform prompts | Generated shared chat body with product-specific deployment wrappers. | Claude preferences, ChatGPT custom instructions, Instructions for Gemini. |
| Mode configs | Safety and workflow rules for capability-specific modes. | Claude Cowork global instructions. |
| Skills | Standard SKILL.md methodology and output craft. | Installed or supplied separately; enabled availability and on-demand loading depend on the client. Detailed craft is not embedded in standing platform prompts. |
| Plugins and native capabilities | Vendor distribution packages can include skills, tools/apps, hooks, agents and supporting resources; native internals may be opaque. | The skills catalogue owns selections and upstream links; platform baselines own delivery and observed state. A listed source is not an installed capability. |
| Configuration references | Guidance for tools that should receive a shared derivation or read the kit directly. | Claude Code, Codex, Copilot CLI, Hermes, Grok, OpenCode/Go. |

## Shared contract and model references

The [September constitution review](../../../governance/evidence/2026-09-constitution-alignment.md) records the source update, static review and explicit exclusion of behavioural runs. Model and host are separate: Fable 5.1 and GPT-6 Astra are primary thinking-partner targets; the execution derivation also supports bounded work on those models, Grok or Go-accessed models. This documents intended deployment, not installed state.

| Reference | Purpose |
|---|---|
| [Chat contract](chat-contract.md) | Canonical chat body generated into Claude, ChatGPT and Gemini files. |
| [Contract maintenance](contract-maintenance.md) | Source ownership, coverage, composition and distribution commands. |
| [Execution contract](execution-contract.md) | Condensed task contract generated into Codex, Claude Code, Copilot CLI and Hermes guides. |
| [Model guidance](model-guidance.md) | Separates model-specific observations from shared policy and host configuration. |
| [Grok](grok/README.md) | Execution guidance for the actual Grok host. |
| [OpenCode and Go](opencode/README.md) | Version-sensitive composition and provider-forwarding considerations. |

These additions stay in implementation. They create no new authority layer or installed configuration.

## Configuration records

The [Claude configuration baseline](claude/configuration-baseline.md) and [Codex configuration baseline](codex/configuration-baseline.md) translate the adopted capability target into product controls. Claude retains earlier verified settings; Codex live configuration is unverified. Adoption of the target is separate from applying or verifying it.

The [initial Claude configuration verification](../../../governance/evidence/2026-09-claude-configuration.md) records the earlier deployment gaps; the later [instruction deployment](../../../governance/evidence/2026-09-claude-deployment.md) verifies saved chat instructions, the Cowork addendum and the enabled my-voice v2 package against source. Source files define intended content; enabled switches describe availability; neither alone proves runtime loading or successful use. The provider catalogue simplification made no live changes.

## Skills, plugins and native capabilities

The [skills catalogue](../skills/README.md) owns useful outcomes, provider selections and upstream links. Platform guides own supported configuration; baselines and dated governance evidence own observed settings and results. Earlier capability and package registers remain historical research. None of these references is loaded as standing skill instructions.

Retain the host provider's useful native capabilities and select its own published additions. Use Anthropic offerings in Claude and OpenAI offerings in Codex; do not cross-import provider packages to match installations. Independently authored third-party skills can be considered for both later. The authored voice skill is unchanged by this selection batch.

On means enabled and available; Off means disabled or undeployed. In Claude, the whole plugin is the control unit: enabling it makes all its skills available, while disabling it removes it from chat selection. There is no task-only state or per-skill switch inside a plugin. Assess the full bundle and keep the selected set enabled. Verify other harness controls independently. Use managed provider distribution; do not manually upload provider copies to work around an unavailable route.

Prepare the exact live delta against the target: client/mode, package revision where inspectable, supported route, dependencies, affected controls and restoration. Check shared tool dependencies before disabling anything. Verify saved state, fresh-session availability, a relevant output and unwanted activation; distinguish exposure, loading and successful use. Native runtime internals may be unknown. Use a matched comparison only when value or interference is uncertain, following the [review method](../skills/review-method.md).

Existing contract loading combinations remain canonical. Package selection does not authorise connector writes, memory changes or publication. The [implementation plan](../skills/implementation-plan.md) separates completed repository guidance from the pending live deployment; vendor-managed runtime rollback limits remain explicit.

## Surface Tiers

| Tier | Surfaces | Configuration model |
|---|---|---|
| Configurable chat | Claude Chat, ChatGPT, Gemini | Generated chat contract plus optional full constitution files. |
| Cowork | Claude Cowork | Supplied core or chat contract, plus the Cowork addendum. |
| Agent and CLI | Claude Code, Codex, Copilot CLI, Hermes, OpenCode | Carry a minimal derived contract and read the constitution files from this repo for deeper work. |
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

Supply the core constitution or the [chat-contract body](chat-contract.md), plus the [Cowork addendum](claude/cowork/global-instructions.md) in the applicable instruction surface. Confirm that the base is actually available; do not assume profile preferences flow into Cowork. The addendum retains plan confirmation, no overwrites, exact-file deletion approval, folder boundaries and connector previews. Shared mode, voice and approval policy comes from the base.

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
- Keep voice reference material separate from platform configuration; the shared body carries the voice boundary and compact writing standards.

## Gemini

Gemini is the Google-adjacent generalist surface.

Configuration:

- Enable Instructions for Gemini if available.
- Paste [saved-instructions.md](gemini/saved-instructions.md).
- Attach or paste constitution files when depth is needed.
- Keep voice reference material separate from platform configuration; the shared body carries the voice boundary and compact writing standards.

## Codex

Codex is a primary thinking and output harness alongside Claude, with engineering, repo, browser and audit capabilities.

Configuration reference:

- Point Codex at this repo.
- Apply the [capability baseline](codex/configuration-baseline.md) through actual host controls; the target is adopted and live harmonisation remains pending.
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

## Grok and OpenCode Go

[Grok guidance](grok/README.md) applies the shared contract through the actual app, API or agent host. [OpenCode guidance](opencode/README.md) covers version-sensitive instruction composition and Go model access. Supply a task handover with decisions, rationale, exact targets and authority. Neither route creates a new constitution, installs configuration, or establishes that native model controls pass through a gateway. Verify the actual host before deployment.

## Capability by Surface

| Capability | Claude Chat/Cowork | ChatGPT | Gemini | Agent/CLI surfaces |
|---|---|---|---|---|
| Standing condensed contract | Generated chat body; Cowork requires supplied base plus addendum | Custom instructions | Instructions for Gemini | Tool-specific where supported |
| Full constitution files | Project knowledge, upload, filesystem | Project files or attachments | Attach or paste | Read from repo checkout |
| Professional overlay | Load only when relevant | Attach only when relevant | Attach only when relevant | Read only when relevant |
| Voice boundary | Neutral partner voice for thinking; Andrew's voice only for output on his behalf | Same | Same | Same |
| Ambient memory and history | Product-managed through account settings | Enabled, periodically reviewed; Temporary Chat when isolation is needed | Memory and activity retained per product settings | Tool-specific |
| Deliberate persistent changes | Explicit approval for tool-mediated changes | Explicit approval for persistent artefacts, including hidden records | Explicit approval for persistent artefacts, including hidden records | Explicit approval for files, instructions, store entries and equivalent artefacts |
| External actions | Cowork connector controls apply | Product-specific | Product-specific | Tool-specific |

## Principles

- **Constitution files are the source of truth.** Platform prompts are derived and condensed.
- **Standalone prompts work without attachments.** Chat surfaces need enough instruction to behave well when no constitution files are loaded.
- **Constitution files declare internal precedence when present.** Platform prompts state this within the host’s instruction hierarchy; file labels cannot elevate message authority or override host controls.
- **Shared derivations work without full constitution files.** Chat and execution bodies supply standalone baselines and defer when the full constitution is present. Addenda and project templates require the base context specified in their loading instructions; maintenance references are not runtime contracts.
- **Voice material stays outside platform configuration.** Shared bodies carry voice boundaries and compact standards; execution craft is supplied separately.
- **Standard skill format only.** Skills remain SKILL.md folders. The repo does not create alternate formats.
- **Deliberate persistent changes require approval.** This includes project instructions, saved instructions, global agent files, knowledge-store entries, explicit user-visible memory entries, SOUL.md-class files and equivalent standing context.
- **Ambient product memory is settings-governed.** Platform adapters document whether it is enabled, how it is reviewed and how to start an isolated conversation. Standing prompts do not claim control over automatic retention or inference.
- **Root maintenance files are not deployment files.** `CLAUDE.md` and `AGENTS.md` govern this repository only; platform guidance does not treat them as the general configuration pattern.
- **Security settings are tool-side.** Credentials, exact trusted roots and account-specific security state belong in the products that hold them and must never be copied into this repository. Platform baselines may record portable settings policy and verification limits without importing those private values.

Version: 2026.09.13 @ 3.7
