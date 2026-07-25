← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-007**

# ADR-007 — Pair protection with the evolution of judgement

**Status:** Accepted (2026-07-08); supported by the [evaluation baseline](../evidence/2026-07-baseline.md)

## Context

Protecting independent judgement is not the same as preserving current beliefs. A system concerned only with protection can become defensive and static; a system concerned only with improvement can let the model do the user's thinking. The architecture needs both objectives and a clear boundary between them.

## Decision

Make the dual objective explicit:

- Philosophy states that the system should help judgement evolve while protecting its independence.
- The operating contract delivers that objective through provocation, challenge and reflection, never by producing developed positions on Andrew's behalf.
- Mode and posture rules decide when contribution should stop short of output.
- Eval fixtures test both under-triggering and over-triggering.

## Consequences

- Challenge serves development rather than contradiction for its own sake.
- The knowledge steward can surface changes and tensions without deciding what Andrew should believe.
- Platform adapters carry the behaviour only to the extent needed to work independently.
- Wording changes remain subject to regression evaluation.

## Alternatives considered

- **Protection only:** rejected because it can preserve a static snapshot rather than strengthen judgement.
- **Evolution only in philosophy:** rejected because philosophy is not ordinary runtime context.
- **Permit the model to develop positions for the user:** rejected because it collapses the boundary the objective is meant to protect.
