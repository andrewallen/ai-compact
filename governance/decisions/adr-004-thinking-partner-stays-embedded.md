← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-004**

# ADR-004 — The thinking-partner role stays embedded in the constitution

**Status:** Accepted (2026-07-08)

## Context

Under a strict reading of the layer model, `02-operating-contract.md` mixes two layers: constitutional principles (register separation, agreement discipline, the expansion function, voice principles) and the default role's mechanics (mode detection, posture, the partnership division of labour). Purity would argue for extracting a `kit/roles/thinking-partner.md`.

But 02 is the most load-bearing, most-tuned file in the kit. The eval fixtures are written against it, the condensed platform prompts are derived from it, and its internal ordering reflects deliberate attention-placement decisions. Splitting it is the highest-risk possible operation on the estate, for a benefit that is currently conceptual.

## Decision

The thinking-partner role remains embedded in `02-operating-contract.md`, documented as a known and accepted impurity in the layer model. New roles — the knowledge steward first — get standalone charters in `kit/roles/`.

Extraction is deferred until there is a concrete need: a surface that requires the partner mechanics without the full constitution, or a second reasoning role whose charter would duplicate 02 content. If extraction happens, it is gated on full eval parity before and after.

## Consequences

- `kit/roles/README.md` names the embedded default role so the layer model reads honestly.
- Charters must not restate constitutional content; they add mission, decision policy, boundaries and cadence, and declare subordination to the constitution — the same pattern the overlay and `my-voice` already use.
- The thinking partner is the default role, active in every conversation unless another charter is explicitly loaded.

## Alternatives considered

- **Split 02 now:** rejected — maximum regression risk on the system's core for zero behavioural gain today.
- **Treat 02 wholesale as the thinking-partner charter** and promote something else to constitution: rejected — 02 contains genuinely constitutional rules (the register seam, agreement discipline) that must bind every role, including the steward.
