← [Home](../../README.md) · [Kit](../README.md) · **Evals** · [Governance evidence](../../governance/evidence/README.md)

# AI Compact Evaluation Harness

The evaluation system asks whether the compact supports better-informed, independently owned judgement. It separates **conformance**, **change** and **value over the same Codex host without the compact**. A local behaviour pass does not override invented facts, lost ownership or an authority violation. Human learning remains a separate observation.

These documents and scenarios are evaluator data, never standing operating context. Retain the existing diagnostic cases, use the shared gates in every family, and select a bounded comparison before running. No new constitution or live-product validation is implied merely by maintaining this harness.

## Maintained components

| Component | Purpose |
|---|---|
| [Evaluation protocol](evaluation-protocol.md) | Comparison design, frozen plans, transfer exposure, stopping rules, grading and token accounting. |
| [Shared rubric](shared-rubric.md) | Whole-response grounding, ownership, authority and instruction/data gates; separate behavioural quality. |
| [Coverage map](coverage-map.md) | Axioms, constitutional commitments, evidence and remaining human/deployment questions. |
| [Human review](human-review.md) | A small review practice for understanding, ownership, friction and later application. |
| [Case registry](cases.json) | Selected text-only cases; prompts and local criteria remain canonical in the Markdown fixtures. |
| [Grader anchors](grader-calibration.json) | Authored calibration examples, including favourable inventions and unnecessary framing; not a human-validated gold standard. |
| [Codex runner](run_evals.py) | Freeze, run native conversations, blind-grade and report with measured usage. OpenAI Codex routes only. |
| [Runner tests](test_run_evals.py) | Offline checks for evidence integrity, gate precedence, usage and limits. |

The [September source-alignment batch](../../governance/evidence/2026-09-constitution-alignment.md) explicitly excluded behavioural runs at Andrew’s request. Fixtures and historical results are retained; no result certifies the revised source. This is a named-batch exception, not a change to the general evaluation policy.

The [19 September voice maintenance record](../../governance/evidence/2026-09-voice-maintenance.md) documents the package repair and verified deployments. Andrew declined the proposed behavioural comparison and requested a static consolidation review instead. No run is awaiting approval and no new behavioural baseline is claimed. This decision applies to that batch; the fixtures and general evaluation policy are retained. D5 includes package-with-condensed-base loading variants, separate from natural-language discovery.

## How to run

Use Python 3.9 or newer and an authenticated Codex CLI with a verified usage adapter (currently `codex-cli 0.155.1`), using the flags recorded in the [protocol](evaluation-protocol.md). Use `-B` so imports do not leave cache files in the repository. Local source checks do not make model calls:

```sh
python3 -B kit/evals/run_evals.py validate
python3 -B -m unittest discover -s kit/evals -p 'test_run_evals.py'
```

First run the grader anchors with the same grader and effort intended for the batch. Each output directory must be new and private, outside the repository. These example limits are soft planning limits, not a claim about needed tokens or a hard billing cap:

```sh
python3 -B kit/evals/run_evals.py prepare --calibration --repeats 1 --comparison conformance --question "Does the grader recognise the shared gates?" --model gpt-6-astra --effort high --max-calls 2 --token-stop 60000 --out /tmp/compact-grader-check
python3 -B kit/evals/run_evals.py run --plan /tmp/compact-grader-check/plan.json
python3 -B kit/evals/run_evals.py grade --plan /tmp/compact-grader-check/plan.json
python3 -B kit/evals/run_evals.py summarise --plan /tmp/compact-grader-check/plan.json
```

A small native conversation comparison, with one repetition, validates the integration. It cannot establish superiority or reliability:

```sh
python3 -B kit/evals/run_evals.py prepare --cases M1,H1 --condition baseline=none --condition core=core --comparison value --question "What changes with the compact in this bounded sample?" --model gpt-6-astra --effort high --repeats 1 --max-calls 9 --token-stop 180000 --out /tmp/compact-smoke
python3 -B kit/evals/run_evals.py run --plan /tmp/compact-smoke/plan.json
python3 -B kit/evals/run_evals.py grade --plan /tmp/compact-smoke/plan.json
python3 -B kit/evals/run_evals.py summarise --plan /tmp/compact-smoke/plan.json
```

For a change comparison, supply two immutable checkouts or snapshots, for example `--condition before=core:/path/to/before --condition after=core:/path/to/after --comparison change`. For detached routes use `chat` or `execution`. Use the same case scripts, model and effort, ordinarily three to five repetitions, and set the call/token limits to cover the selected work. GPT-5.6 Sol is available as the explicit `gpt-5.6-sol` option; no silent fallback occurs. Repeat with another model only to answer a model-specific question.

Use `core-overlay` to supply all four constitution files for G1/G2 and the professional-context cases G4–G6. Plain `core` intentionally omits the overlay and only tests the absent-overlay control for G1. The runner freezes the overlay's text and hash with the core; supply the same route for both conditions in an overlay change comparison. G4's future date is a synthetic scenario, and its uncertainty handling does not establish live retrieval quality.

`prepare` freezes source text, cases, rubric, CLI version and runner hash. `run` submits only the current user turn and resumes the exact native session for later turns. It never submits future turns or rubrics to the responding model. `grade` uses fresh contexts and opaque condition IDs, in bounded batches to avoid resending the same host/rubric overhead for every sample. `summarise` derives overall dispositions, preserves gate failures and reports dimension-wise paired comparisons without a compensating overall quality score.

Run and grade commands are single-use for a plan, including failed attempts. A changed runner requires a new plan; a new CLI version also needs usage-capture validation before the adapter accepts it. Native multi-turn transcripts additionally reside in Codex's normal local session store. An interrupted or budget-stopped run remains incomplete; do not replace it with the best later attempt. Unknown usage stops further budget-controlled calls. Summaries are new files; use `--out` for a later summary rather than overwriting evidence.

For a reviewed grade, `summarise --adjudications /private/path/review.json --out /private/path/reviewed-summary.json` accepts an object keyed by opaque job ID. Each entry requires `reviewer`, `reason`, `evidence`, `original_disposition`, and a complete replacement `assessment` matching the generated grade schema. Original grades remain unchanged. Report machine/reviewer disagreement; the runner does not assert that an unaudited adjudication is correct.

The text runner is not a live tool, skill-discovery, retrieval, memory or compaction harness. It requests isolation and records observed calls, but does not verify the complete tool/context exposure or backend model identity. Treat comparisons as provisional where those remain unverified. Follow the product-specific fixture setup for deployment claims. Use [human review](human-review.md) for claims about Andrew's learning.

## Fixture Set

| Fixture | What it tests |
|---|---|
| [sycophancy-probes.md](sycophancy-probes.md) | Agreement discipline, challenge, capitulation, praise reflex. |
| [agreeable-middle-probes.md](agreeable-middle-probes.md) | Option diversity, false balance, false breakthrough. |
| [provoke-produce-probes.md](provoke-produce-probes.md) | Exploratory restraint, reframe-first mechanism, mode transitions. |
| [evolution-probes.md](evolution-probes.md) | Shift surfacing, evolution boundary (ADR-007 under/over-trigger pair). |
| [judgement-adaptation-probes.md](judgement-adaptation-probes.md) | L1–L8: method fit, sufficiency, emotional or intuitive signals, values and deliberate exploration, with controls against over-intervention. |
| [conversation-probes.md](conversation-probes.md) | M1–M3: development, values, pushback, evidence changes and execution across native turns. |
| [transfer-probes.md](transfer-probes.md) | T1–T3: natural personal/community variants reserved from tuning within a frozen comparison. |
| [voice-separation-probes.md](voice-separation-probes.md) | Register separation, my-voice substance gate, detector behaviour, natural-language discovery and audience context. |
| [persistence-boundary-probes.md](persistence-boundary-probes.md) | Approval for deliberate persistent changes, Cowork base-plus-addendum loading and non-claims about ambient product memory. |
| [boundary-durability-probes.md](boundary-durability-probes.md) | Overlay dormancy, open perspectives, dated context, customer capacity, practitioner evidence and long-context durability. G3 requires a separate long-conversation harness. |
| [challenge-threshold-probes.md](challenge-threshold-probes.md) | Material challenge without performative challenge to a sound brief. |
| [clarification-threshold-probes.md](clarification-threshold-probes.md) | Direct execution on a sufficient brief and questions only for material ambiguity. |
| [agent-evidence-scope-probes.md](agent-evidence-scope-probes.md) | Tool-grounded completion claims and exact-target authority. |
| [capability-composition-probes.md](capability-composition-probes.md) | K1–K8: reusable synthetic artifact, editorial and synthesis examples; activation, exploration and persistence under skill/plugin composition. Formerly this file's F1–F8; persistence F1–F3 remain separate. Authored and unexecuted. |

The capability examples remain available for targeted checks when use exposes uncertain value or interference. The [skills tracker](../implementation/skills/README.md) records adoption and deployment; it does not require a capability pilot for every entry. This does not relax the regression policy for constitution, voice or condensed-contract changes above.

Historical aggregate outcomes and claim boundaries are recorded in the [July 2026 evaluation baseline](../../governance/evidence/2026-07-baseline.md). Later source and deployment checks are indexed separately in [governance evidence](../../governance/evidence/README.md).

The [evaluation redesign record](../../governance/evidence/2026-09-evaluation-redesign.md) records implementation, Codex-only review and verification. Earlier totals remain narrow historical scores; no historical result is silently regraded under the shared rubric.
