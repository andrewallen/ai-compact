← [Home](../../README.md) · [Governance](../README.md) · **Decisions**

# Architecture Decision Records

Numbered records of structural, layer-level decisions about the kit and the framework. Each ADR states the context, the decision, its consequences, and the alternatives considered.

Scope split (ADR-006): ADRs record decisions that change the shape of the system — layers, seams, folder-level structure, naming. `../design-decisions.md` continues as the narrative log for file-level design reasoning. Each references the other where they touch.

Statuses in this set: **Accepted** (the decision governs the current system) and **Superseded** (retained to explain a decision that a later ADR replaced).

| ADR | Title | Status |
|---|---|---|
| [001](adr-001-five-layer-architecture.md) | Adopt the five-layer architecture | Accepted |
| [002](adr-002-philosophy-is-background.md) | Philosophy is background, not a runtime dependency | Accepted |
| [003](adr-003-framework-and-implementation-converge.md) | Keep the framework and personal kit in one repository | Accepted |
| [004](adr-004-thinking-partner-stays-embedded.md) | Keep the thinking-partner role embedded in the constitution | Accepted |
| [005](adr-005-stewardship-is-behaviour.md) | Keep stewardship behaviour in the kit and store structure outside it | Accepted |
| [006](adr-006-formal-adrs.md) | Use formal ADRs alongside the design-decisions register | Accepted |
| [007](adr-007-evolution-objective.md) | Pair protection with the evolution of judgement | Accepted |
| [008](adr-008-repo-rename.md) | Use AI Compact as the project name | Accepted |
| [009](adr-009-physical-restructure-deferred.md) | Defer physical alignment until it can be atomic | Superseded by ADR-010 |
| [010](adr-010-physical-layer-alignment.md) | Use semantic paths for the five-layer model | Accepted; top-level placement superseded by ADR-011 |
| [011](adr-011-three-domain-containment.md) | Use three reader-facing repository domains | Accepted |
| [012](adr-012-clean-public-baseline.md) | Keep the public repository self-contained | Accepted |
