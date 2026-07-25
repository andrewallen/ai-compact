← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-007**

# ADR-007 — Add the evolution objective alongside protection

**Status:** Accepted (2026-07-08); wording landed 2026-07-13 and was eval-gated — see `governance/evidence/2026-07-baseline.md`

## Context

The kit's stated objective is protective: keep Andrew's thinking his as models converge on a competent average. The July conversation surfaced a second objective the kit nowhere states: help the thinking evolve. Protection is defensive; evolution is generative. A system optimising only for protection asks "how do I avoid degrading Andrew's thinking"; one that also optimises for evolution asks "how do I help him become a better thinker next year than he is today."

The two objectives are in tension — challenge could erode distinctiveness; preservation could fossilise it. The conversation supplied the resolving principle: **the objective is not to preserve current beliefs but to preserve the capacity for independent judgement.**

## Decision

The dual objective enters at two layers:

1. **Philosophy** (Phase 1) carries it natively — it is the first axiom.
2. **Constitution** (Phase 3): `02-operating-contract.md` gains a minimal amendment stating that the system's purpose includes the evolution of Andrew's judgement over time, delivered **through provocation, challenge, and reflection — never through producing developed positions on his behalf**. The posture-by-mode rules are not weakened; they gain a second reason to exist.

The constraint clause is load-bearing. Without it, "help my thinking evolve" licenses exactly the behaviour the provoke/produce boundary exists to prevent — a model doing the evolving for him. Evolution happens in Andrew; the system supplies the pressure.

Verification: baseline probe runs before the amendment; a new evolution fixture in `kit/evals/` (does the model surface shifts in Andrew's thinking; paired over-trigger probe: does it refrain from producing his conclusions); post-amendment runs must show parity on all existing fixtures.

## Consequences

- The steward's reflection cadence (ADR-005) becomes the operational arm of this objective.
- Condensed platform prompts change only if standalone behaviour changes, and the ChatGPT 1,500-character ceiling makes any addition there a displacement decision.
- If the evals show the amendment eroding exploratory restraint, the wording is reverted and reworked — the objective is accepted; any particular sentence is not.

## Alternatives considered

- **Philosophy-only** (no constitutional wording): rejected — the philosophy is not runtime-loaded (ADR-002), so the objective would never reach a live conversation.
- **A full new section in 02:** rejected — the file's length is already earned line by line; a minimal amendment respects that.
