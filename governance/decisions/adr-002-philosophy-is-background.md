← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-002**

# ADR-002 — Philosophy is background, not a runtime dependency

**Status:** Accepted (2026-07-08)

## Context

The philosophy explains why the system exists and provides a tiebreaker for maintenance decisions. Loading it into every conversation would consume attention without adding operational detail, and could encourage models to interpret broad purpose as additional instruction.

## Decision

Keep `kit/philosophy/axioms.md` short and outside the ordinary runtime load set. The constitution derives from it and may quote an axiom where the reason materially improves compliance. Load the philosophy only when reviewing the system's foundations.

A philosophy change triggers a constitution review so the derivation is checked explicitly.

## Consequences

- The constitution remains self-sufficient when the philosophy is absent.
- Ordinary conversations retain a smaller, clearer instruction set.
- The owner authors the final axioms; an assistant may interview and challenge but cannot supply the philosophy on the owner's behalf.

## Alternatives considered

- **Load philosophy every time:** rejected because its maintenance purpose does not justify permanent runtime cost.
- **Leave philosophy implicit:** rejected because constitutional rules could not be audited against an explicit purpose.
- **Put the axioms in the bootstrap:** rejected because the bootstrap is deliberately minimal runtime insurance.
