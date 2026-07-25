← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-001**

# ADR-001 — Adopt the five-layer architecture

**Status:** Accepted (2026-07-08)

## Context

The kit grew from a set of constitution files into an estate-wide system: constitution-grade constitution files, a skill, prompts, platform deployments, evals and governance records. Its organising model remained "constitution files plus derived artefacts," which left the purpose layer undeclared and gave new components (the knowledge steward) no natural home. The July 2026 review (ChatGPT conversation `644717ec` reconciled against the repo) surfaced a layered model that matches how the system already behaves.

## Decision

Adopt five layers, ordered by authority and by inverse rate of change:

1. **Philosophy** — why intelligence is in the system; changes rarely.
2. **Constitution** — enduring behavioural principles (the constitution files); changes occasionally.
3. **Role charters** — mission and decision policy per role; change with the roles.
4. **Implementation** — platforms, skills, prompts; changes constantly.
5. **Memory** — Vault, platform memory, conversation history; changes daily and lives outside the repo.

Evals and governance records are cross-cutting. `framework/` sits alongside as the generic pattern the layers instantiate (ADR-003). Adoption is logical first: layers are declared in documentation and new folders are added; existing folders are not renamed or moved until Phase 5, if at all (ADR-009).

## Consequences

- New artefacts: `kit/philosophy/`, `kit/roles/`, `framework/`, this decisions folder.
- The existing authority hierarchy (calibration / binding rules / overlay) becomes the constitution's internal structure, unchanged.
- The rate-of-change ordering generalises an instinct the kit already had (the disposable tuning block versus the stable constitution files) into a system-wide principle.
- Runtime load for ordinary conversations is unchanged; charters load only when their role is active.

## Alternatives considered

- **Stay with the two-part model** (context + derived): rejected — it has no home for roles or philosophy, and the steward was about to be bolted on ad hoc.
- **Adopt the conversation's four layers** (principles, working memory, durable knowledge, reflection): rejected — it is a memory-system model, not a governance model; reflection enters here as steward cadence, not as a layer.
