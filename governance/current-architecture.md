← [Home](../README.md) · [Framework](../framework/README.md) · [Kit](../kit/README.md) · [Governance](README.md) · **Current architecture**

# Current Architecture

The canonical current view of how the generic framework, personal kit, external memory and product surfaces relate. The [framework layer model](../framework/layer-model.md) remains the generic specification; this document describes this implementation.

## Repository domains

| Domain | Responsibility | Boundary |
|---|---|---|
| [Framework](../framework/README.md) | Reusable layer model, design principles and adoption method. | Generic and anonymised; no personal content. |
| [Kit](../kit/README.md) | Personal philosophy, constitution, roles, implementation components and active evals. | The deployable reference implementation. |
| [Governance](README.md) | Current topology, decisions, diagrams and evidence. | Describes and evolves the system; never runtime context. |

Architecture is therefore a view across domains, not a fourth content domain. The generic architecture belongs to the framework; this instantiated topology and its history belong to governance.

## Runtime stack

```text
philosophy         maintenance-time axioms; never ordinary runtime context
    ↓ derives
constitution       source-of-truth calibration and binding operating rules
    ↓ governs
role charters      conditional judgement for distinct roles
    ↓ governs
implementation     platform adapters, skills, plugins/native capabilities and prompts
    ↕ acts across
memory             external knowledge store, platform memory and history
```

Authority flows downward. Evidence from use flows back upward through evals and explicit decisions. A lower layer may adapt a higher layer but cannot override it.

![Authority and load hierarchy](diagrams/authority-hierarchy.svg)

## Deployment topology

The constitution is maintained once in [`kit/constitution/`](../kit/constitution/README.md). Configurable chat products receive condensed standing instructions that work alone and defer to the full constitution. Agent and CLI surfaces receive a minimal derived contract or read the source files directly. Skills and prompts are supplied only when their work is active.

![Deployment paths](diagrams/deployment-paths.svg)

The operational source is the [deployment map](../kit/implementation/platforms/deployment-map.md). Product files are adapters, not additional sources of truth. [Chat](../kit/implementation/platforms/chat-contract.md) and execution bodies are authored once and generated into seven detached copies; [contract maintenance](../kit/implementation/platforms/contract-maintenance.md) records coverage and loading combinations. Cowork is an addendum requiring supplied core or chat context. The [consolidation record](evidence/2026-09-implementation-consolidation.md) documents this implementation change. The [shared execution contract](../kit/implementation/platforms/execution-contract.md) derives by task; [model guidance](../kit/implementation/platforms/model-guidance.md) records dated vendor observations and host limits for Fable, Astra, Grok and Go-accessed models. These remain layer 4. One model can serve exploration and execution without requiring a different constitution. Internal authority declarations remain subject to host instructions and permissions.

The latest recorded [Claude instruction deployment](evidence/2026-09-claude-deployment.md) verifies saved chat instructions, the Cowork addendum and all four files of the enabled `my-voice` v2 package against the revised source. It follows the earlier configuration inspection and source-alignment work. Project-specific constitution attachments were not changed; runtime loading, adherence and deployment to other products were not established by that record. The [Claude configuration baseline](../kit/implementation/platforms/claude/configuration-baseline.md) owns the maintained settings account.

## Capability implementation records

Skills, vendor plugins and native workflows remain within layer 4. The [skills catalogue](../kit/implementation/skills/README.md) owns selected outcomes, upstream provenance links and On/Off choices. The [Claude](../kit/implementation/platforms/claude/configuration-baseline.md) and [Codex](../kit/implementation/platforms/codex/configuration-baseline.md) baselines translate those choices into supported controls and separate adopted targets from verified deployment. Dated governance evidence records observed results. These are maintenance references, not runtime routing instructions.

The [implementation plan](../kit/implementation/skills/implementation-plan.md) records the repository simplification and pending live harmonisation. Use each provider's own native or published capabilities in its harness, without cross-provider imports for symmetry. Independent third-party selection has begun with Impeccable, i-have-adhd, Taste Skill and Obsidian, with current Claude list evidence in the catalogue and baseline (the follow-up confirms Obsidian 1.0.1 enabled with six skills); the authored voice skill is parked. Claude enables complete plugins: disabled plugins are unavailable to select in chat. The catalogue does not prescribe a task-only state or per-job toggling. Use provider-managed delivery; a matched comparative trial is reserved for uncertainty rather than required for every addition.

The previous matrix and registers are historical. The [source inventory](../kit/implementation/skills/first-party-inventory.md) remains unchanged dated evidence, including local observations that do not define the new catalogue. Capability fixtures remain authored and unexecuted. The [superseding file-level decision](design-decisions.md#provider-selections-drive-harness-configuration) records the simpler ownership model. No new authority layer, marketplace or folder restructuring is introduced.

## Memory boundary

Memory is layer 5 but remains outside the repository because it is changing state rather than portable system definition:

- the personal knowledge store manages curated knowledge;
- platform memory supplies ambient continuity and may be toggled or retained differently by product;
- conversation history belongs to the products that hold it.

The kit governs deliberate actions at this boundary through the constitution and role charters: an agent needs scoped approval before using a tool to change a persistent artefact, including hidden supporting records. A specified change request or instruction to implement a defined plan supplies that approval within its scope; narrower safeguards still apply. Ambient memory and history retained or inferred automatically by a service are product state. Their enablement, retention and review belong in platform settings and deployment guidance; the constitution does not claim to control them. The kit does not prescribe or duplicate the knowledge store's schema.

## Change and evidence flow

![Work flow between modes](diagrams/work-flow-between-modes.svg)

- High-authority changes receive a cold critique and behavioural evaluation.
- Constitution changes trigger a derived-platform cascade check.
- Structural changes receive an ADR.
- A material evaluation may produce a concise dated record in [evidence](evidence/README.md).
- Raw working material remains outside maintained governance.

The [architecture decisions](decisions/README.md) explain binding structural choices. The [July 2026 evaluation baseline](evidence/2026-07-baseline.md) remains historical behavioural evidence. The [September alignment record](evidence/2026-09-constitution-alignment.md) records the source rewrite, static review and the owner’s explicit exclusion of behavioural runs for this named batch. The general evaluation policy remains; the exception does not establish runtime parity or deployment.
