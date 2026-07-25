← [Home](../../README.md) · [Governance](../README.md) · **Decisions**

# Architecture Decision Records

Numbered records of structural, layer-level decisions about the kit and the framework. Each ADR states the context, the decision, its consequences, and the alternatives considered.

Scope split (ADR-006): ADRs record decisions that change the shape of the system — layers, seams, folder-level structure, naming. `../design-decisions.md` continues as the narrative log for file-level design reasoning. Each references the other where they touch.

Statuses: **Proposed** (awaiting Andrew's decision), **Accepted**, **Deferred** (accepted in principle, deliberately sequenced later), **Superseded** (with a pointer to the successor).

| ADR | Title | Status |
|---|---|---|
| [001](adr-001-five-layer-architecture.md) | Adopt the five-layer architecture | Accepted |
| [002](adr-002-philosophy-is-background.md) | Philosophy is a versioned background artefact, not a runtime dependency | Accepted |
| [003](adr-003-framework-and-implementation-converge.md) | Framework and implementation converge in one repo | Accepted |
| [004](adr-004-thinking-partner-stays-embedded.md) | The thinking-partner role stays embedded in the constitution | Accepted |
| [005](adr-005-stewardship-is-behaviour.md) | Knowledge stewardship enters the kit as behaviour; structure stays with the Vault | Accepted |
| [006](adr-006-formal-adrs.md) | Adopt formal ADRs alongside the design-decisions log | Accepted |
| [007](adr-007-evolution-objective.md) | Add the evolution objective alongside protection | Accepted; wording landed 2026-07-13, eval passed |
| [008](adr-008-repo-rename.md) | Publish the project as AI Compact | Accepted |
| [009](adr-009-physical-restructure-deferred.md) | Physical folder restructure is deferred to the final phase | Superseded by ADR-010 |
| [010](adr-010-physical-layer-alignment.md) | Physically align the repository to the five-layer model | Accepted; root placement partially superseded by ADR-011 |
| [011](adr-011-three-domain-containment.md) | Contain the personal kit within a three-domain repository | Accepted |
| [012](adr-012-clean-public-baseline.md) | Begin public history from a clean, self-contained baseline | Accepted |

Version: 2026.07.25 @ 2.0
