# AI Compact

The constitution and operating terms for every AI that works with me.

AI Compact is a public, versioned collection of plain-markdown instructions, role charters, platform adapters and behavioural tests. It governs how AI thinks with me in conversation and establishes the authority, boundaries and evidence standards for agents that act on my behalf.

The repository contains both a reusable framework and my real personal implementation. The framework can be adopted independently; the kit shows how the pattern works across products and interaction modes.

## Status

**Stable baseline.** The architecture and initial model-guidance migration were completed in July 2026. There is no active repository migration. Future changes are driven by observed behaviour, new products and deliberately adopted capabilities.

## How it works

In an exploratory conversation, the operating contract asks the model to widen the frame, challenge material assumptions and leave the conclusion with me. When I own a position and request an output, the `my-voice` skill can render it in my voice. When an agent can use tools or change persistent state, the same constitution supplies its standing boundaries; a role charter adds the judgement policy for that particular job.

## Start here

| If you want to… | Start with |
|---|---|
| Understand the reusable pattern | [Framework](framework/README.md) and its [five-layer model](framework/layer-model.md) |
| Understand this personal implementation | [Personal kit](kit/README.md) |
| Deploy the kit to an AI product | [Platform deployment map](kit/implementation/platforms/deployment-map.md) |
| See how the whole system fits together | [Current architecture](governance/current-architecture.md) |
| Understand why the structure exists | [Architecture decisions](governance/decisions/README.md) |
| See what established the public baseline | [Baseline evidence](governance/evidence/2026-07-baseline.md) |
| Test a behavioural change | [Evaluation harness](kit/evals/README.md) |
| Maintain this repository | [AGENTS.md](AGENTS.md) and its [CLAUDE.md bridge](CLAUDE.md) |
| Contribute or report a problem | [Contributing](CONTRIBUTING.md) and [security reporting](SECURITY.md) |

## Three repository domains

| Domain | Purpose | Personal content? |
|---|---|---|
| [Framework](framework/README.md) | The generic, reusable specification: layer model, principles and adoption guide. | No. It must remain anonymised and independently publishable. |
| [Kit](kit/README.md) | The personal instance: philosophy, constitution, roles, implementation components and active evals. | Yes. This is the deployable working system. |
| [Governance](governance/README.md) | Current architecture, adopted decisions, diagrams and baseline evidence. | Where required to explain this implementation and its evolution. |

Repository-maintenance files remain at the root because they govern work across all three domains. Memory remains outside the repository because it is state, not system.

## Five-layer model

The framework and kit use five layers, ordered by authority and inverse rate of change:

| Layer | This implementation | Runtime posture |
|---|---|---|
| 1 — Philosophy | [`kit/philosophy/`](kit/philosophy/README.md) | Background only; never loaded during ordinary work. |
| 2 — Constitution | [`kit/constitution/`](kit/constitution/README.md) | Core files load for full operating context. |
| 3 — Role charters | [`kit/roles/`](kit/roles/README.md) | Load only when a role is active. |
| 4 — Implementation | [`kit/implementation/`](kit/implementation/README.md) | Platform adapters, skills and prompts deploy or execute as needed. |
| 5 — Memory | Outside this repository | The knowledge store, platform memory and conversation history. |

[Evals](kit/evals/README.md) verify behaviour across the personal layers. [Governance](governance/README.md) records why the system is shaped this way. Neither is a sixth runtime layer.

The constitution remains the behavioural source of truth. Platform-specific instructions are condensed derivations: they must work alone and defer to the full constitution when it is present.

## System boundary

The kit is the portable part of a larger personal AI system. The external knowledge store manages personal knowledge; platform memory supplies ambient continuity; tooling provides reach. The repository governs the seams without absorbing the state itself.

![Current system architecture](governance/diagrams/architecture-overview.svg)

See [Current architecture](governance/current-architecture.md) for the canonical description and [Framework: layer model](framework/layer-model.md) for the generic pattern.

## Repository structure

```text
<repository-root>/
├── README.md
├── AGENTS.md · CLAUDE.md               repository-maintenance instructions
├── framework/                          generic, anonymised specification
│   ├── layer-model.md
│   └── adoption-guide.md
├── kit/                                personal implementation
│   ├── philosophy/                     layer 1 — axioms
│   ├── constitution/                   layer 2 — operating source of truth
│   ├── roles/                          layer 3 — conditional role charters
│   ├── implementation/                 layer 4 — deployment and execution
│   │   ├── platforms/
│   │   ├── skills/
│   │   └── prompts/
│   └── evals/                          active behavioural regression probes
└── governance/                         architecture, decisions and evidence
    ├── current-architecture.md
    ├── design-decisions.md
    ├── decisions/
    ├── diagrams/
    └── evidence/
```

## Deploying the kit

The [deployment map](kit/implementation/platforms/deployment-map.md) is the source of truth across products and modes. The shortest routes are:

- **Claude Chat:** [personal preferences](kit/implementation/platforms/claude/personal-preferences.md) plus the [chat project template](kit/implementation/platforms/claude/chat/template-chat-project.md).
- **Claude Cowork:** [global instructions](kit/implementation/platforms/claude/cowork/global-instructions.md) plus the [Cowork project template](kit/implementation/platforms/claude/cowork/template-cowork-project.md).
- **ChatGPT:** [configuration guide](kit/implementation/platforms/chatgpt/README.md) and [custom instructions](kit/implementation/platforms/chatgpt/custom-instructions.md).
- **Gemini:** [configuration guide](kit/implementation/platforms/gemini/README.md) and [Instructions for Gemini](kit/implementation/platforms/gemini/saved-instructions.md).
- **Agent and CLI surfaces:** [Claude Code](kit/implementation/platforms/claude/code/README.md), [Codex](kit/implementation/platforms/codex/README.md), [Copilot CLI](kit/implementation/platforms/copilot-cli/README.md), and [Hermes](kit/implementation/platforms/hermes/README.md).

For full depth, load the core constitution files from [`kit/constitution/`](kit/constitution/README.md). Load the professional overlay only when its activation conditions apply. Voice material is supplied separately through the [`my-voice` skill](kit/implementation/skills/my-voice/SKILL.md) when producing output on the owner's behalf.

## Maintenance rules

- **Change the source first.** Amend the constitution before any derived platform prompt, then run the cascade check.
- **Gate high-authority changes.** Use the eval harness and a cold critique pass for changes above the implementation layer.
- **Keep personal material out of the framework.** Every framework change receives an anonymisation check.
- **Preserve the memory boundary.** The repository governs deliberate actions at persistent stores but does not contain the knowledge store or control ambient product memory.
- **Keep the public baseline self-contained.** Current files must explain the adopted system without depending on private development history.
- **Keep navigation rename-safe.** Use relative links and `Home` as the root breadcrumb label. Do not embed the repository slug or an absolute checkout path.
- **Require explicit approval for deliberate persistent changes.** Tools and agents never change user-visible instruction surfaces, files, store entries or explicit memory entries autonomously. Product-managed ambient memory is configured and audited through product settings.

Version: 2026.07.25 @ 3.0
