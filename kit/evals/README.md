← [Home](../../README.md) · [Kit](../README.md) · **Evals** · [Governance evidence](../../governance/evidence/2026-07-baseline.md)

# AI Compact Evaluation Harness

These fixtures test whether changes to the constitution files, the `my-voice` skill, and the condensed platform prompts derived from them improve behaviour rather than only improving prose. They are not loaded as operating context. Use them as regression tests after edits to `kit/constitution/`, `kit/implementation/skills/my-voice/`, or condensed platform prompts.

## How to Run

1. Start a fresh conversation or agent session.
2. Load the files named in each fixture.
3. Paste the scenario prompt exactly.
4. Capture the response.
5. Grade against the pass/fail rubric.
6. Run each scenario three to five times when comparing before and after changes; single runs are noisy.

Where possible, use a second model to grade responses against the rubric, then spot-check manually. Do not grade by whether the response sounds clever. Grade by the explicit behaviours in each fixture.

## Fixture Set

| Fixture | What it tests |
|---|---|
| [sycophancy-probes.md](sycophancy-probes.md) | Agreement discipline, challenge, capitulation, praise reflex. |
| [agreeable-middle-probes.md](agreeable-middle-probes.md) | Option diversity, false balance, false breakthrough. |
| [provoke-produce-probes.md](provoke-produce-probes.md) | Exploratory restraint, reframe-first mechanism, mode transitions. |
| [evolution-probes.md](evolution-probes.md) | Shift surfacing, evolution boundary (ADR-007 under/over-trigger pair). |
| [voice-separation-probes.md](voice-separation-probes.md) | Register separation, my-voice substance gate, detector behaviour and natural-language discovery. |
| [persistence-boundary-probes.md](persistence-boundary-probes.md) | Approval for deliberate persistent changes and non-claims about ambient product memory. |
| [boundary-durability-probes.md](boundary-durability-probes.md) | Overlay dormancy, long-context durability, instruction retention. |
| [challenge-threshold-probes.md](challenge-threshold-probes.md) | Material challenge without performative challenge to a sound brief. |
| [clarification-threshold-probes.md](clarification-threshold-probes.md) | Direct execution on a sufficient brief and questions only for material ambiguity. |
| [agent-evidence-scope-probes.md](agent-evidence-scope-probes.md) | Tool-grounded completion claims and exact-target authority. |

Aggregate outcomes and claim boundaries are recorded in the [July 2026 evaluation baseline](../../governance/evidence/2026-07-baseline.md).
