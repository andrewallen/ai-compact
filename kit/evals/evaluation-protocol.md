← [Home](../../README.md) · [Kit](../README.md) · [Evals](README.md) · **Evaluation protocol**

# Evaluation Protocol

The philosophy supplies the purposes and priorities. Evaluation asks whether the constitution and its deployments serve them; it does not let a model decide which values Andrew should hold. The primary outcome is better-informed judgement whose ownership stays visible. Instruction compliance is necessary evidence, not proof of that outcome.

## Three distinct questions

| Question | Comparison | Permitted conclusion |
|---|---|---|
| Conformance | Response and observed actions against shared gates and the selected scenario | Which boundaries and behaviours held in these runs. |
| Change | Previous and proposed source, same route and conditions | Observed regression or improvement on the selected cases. |
| Value | No compact versus core or a condensed body, same Codex host and conditions | Whether adding the compact improved the measured interaction; not a claim about a model without host instructions. |

Use the [coverage map](coverage-map.md) to select cases and identify claims that require human or live-product evidence. Philosophy stays out of responding contexts. Rubrics, expected answers and future user turns also stay out. A no-compact condition retains the same host instructions, test environment and task brief; only the supplied compact is omitted.

## Freeze before running

Record the question, source snapshots, selected cases and routes, model, effort, repetitions, order, grading rubric, call ceiling, soft token stop and intended decision before seeing candidate responses. A plan has immutable content and a digest; results belong to that plan even if the repository changes later. Do not quietly substitute a model, source, case, or loading route.

Use three to five repetitions for selected before/after comparisons. One repetition is an integration smoke check. Three identical passes do not establish reliability or a meaningful improvement rate. Case selection matters more than accumulating repetitions of an obvious prompt. Preserve the denominator, all attempts and disagreements. Do not combine different case sets into a league table or pool candidates until a pass appears.

Counterbalance condition order within a case. Compare the same model and reasoning effort first; keep results for different models separate. Record tools, skills, memory and instructions actually exposed where available. A requested model is not a verified model identity. Unknowns remain explicit. A provider/model error is an execution failure, never a behavioural failure or a reason to use an unapproved fallback.

## Development and transfer

Use the established diagnostic probes to locate failures. Prompts with explicit guardrails remain useful controls; add natural conversations that require recognising the situation from evidence and history.

The [transfer cases](transfer-probes.md) are public, authored cases reserved from runtime-prompt tuning during a comparison. They are visible to maintainers and are not a secret or statistically independent holdout. Freeze the candidate before running them, record exposure, and retain the first result. Once a result has informed a repair, that case is development evidence for the repaired candidate. Obtain a new, separately reviewed variant before claiming unseen transfer again. The runner does not generate fresh tests after seeing a failure.

A useful framing invitation must be followed through: supply the user's frame, test the assistant's contribution, introduce evidence or pushback, then request execution. Score the complete interaction. Asking a particular sentence is not a success criterion. Fixed follow-up scripts are synthetic user behaviour, not evidence of Andrew's learning. Do not pretend transcript replay is a native multi-turn session.

## Grade the whole response

Apply the [shared rubric](shared-rubric.md) to every scenario, then its specific behavioural criteria. The broad gates also apply to claims outside the scenario's main target. A fluent answer that invents a favourable fact fails just as an invented objection does. Separate proposed future conditions from claims about existing arrangements.

Use blinded variant IDs and a fresh grading context. Wording can still reveal a condition; ID blinding is not perfect masking. Calibrate the grader against the [anchor examples](grader-calibration.json) before trusting a batch. These are authored anchors, not a human-validated gold standard. Review disagreements and borderline answers against quoted evidence. A second model within the approved provider can help; agreement between models does not establish truth.

Keep the original machine grade. Require quoted grading evidence to match a stated turn and speaker; represent absence-based judgements explicitly. This verifies provenance, not the correctness of the inference. Record a human or independent review as a separate disposition with reason and evidence; never overwrite a disagreement to obtain a clean score. In the runner, an explicit adjudication file supplies the reviewed disposition. Unknown or unobservable gates prevent an overall pass. Quality dimensions remain separate rather than compensating for a boundary violation.

## Stop and report

Stop at the frozen call ceiling or before the next call once measured usage reaches the soft token stop. A call already in flight can overshoot; these controls are not a billing cap. Missing or ambiguous usage stops a budget-controlled run. Keep incomplete cases in the record. A failed behavioural response is retained without retry. A separately authorised rerun receives a new plan and cannot replace the original.

For a source change, a newly observed critical violation or regression requires investigation and repair or an explicit recorded disposition before acceptance. An unchanged baseline failure is still a failure, not an exemption. If a result is too ambiguous to support the intended decision, say so rather than changing the question after seeing it.

Report conformance, behavioural quality, human judgement, execution validity and resource use separately. Pair wins, ties and losses only on the same applicable dimension with matched cases and repetitions; show each boundary failure independently. A result on isolated instruction bodies is not a deployed-product result. Do not transfer results between full core, condensed text, skill composition or live tools.

## Tokenisation and resource accounting

Characters, UTF-8 bytes and tokens are different measurements. The runner records characters and bytes of supplied text, plus Codex-reported input, cached input, output and reasoning usage when present. It makes no character-to-token conversion. Optional tokenizer estimates must name library version, encoding and text hash and remain labelled estimates of supplied text, excluding unmeasured host overhead.

Input usage can include host instructions, message framing, tool definitions and earlier turns. Attribute it to the invocation; do not describe it as the constitution's exact token cost. Cached input is reported separately and is not added again to input. Reasoning usage is preserved separately and is not automatically added to output. No monetary estimate is produced without a verified, dated price and accounting basis.

The tested Codex CLI 0.155.1 reports session-cumulative completion usage on resume. Preserve raw events and totals. The runner derives invocation usage by subtracting the preceding verified totals for the exact same native session; a fresh session starts from zero. Missing predecessors, decreasing counters, invalid subset relationships or more than one completion event make accounting unverified. The runner accepts only CLI versions listed as tested in its adapter. Validate new versions against controlled single-turn and resumed-turn captures before adding them. Resumed history can legitimately contribute processed input again; this differs from accidentally adding cumulative totals twice.

Compare resource use alongside quality under matching conditions. A shorter answer is valuable only when it retains useful reasoning and ownership. Keep caching and latency visible; avoid a single tokens-per-quality score. Use high reasoning for the methodological review and a fixed, declared effort for each comparison rather than changing effort until a case passes.

## Implementation boundary

The [runner](run_evals.py) uses the installed Codex CLI with OpenAI models only. It appends the chosen compact as developer instructions and retains the native Codex base. It requests read-only operation, disables user config, project documents, host skill discovery, plugins, connectors, browsing and command tools, and records those requests. Observed tool calls invalidate this text-only run. Absence of a call is not proof of absent tool exposure; controlled-isolation claims need separate exposure evidence.

Single-turn runs are ephemeral. Multi-turn cases use one native Codex session and explicit resume IDs; Codex retains the local session required for continuation. The harness copies raw results and session identifiers to the approved private output directory. Native multi-turn transcripts also persist in Codex's normal local session store (governed by the existing Codex home and host settings); changing the working directory does not relocate that store. The runner never deletes sessions, writes to external services, launches Claude, or silently switches provider. Agent-action and deployed-product probes still need their own isolated tools and loading evidence; this runner cannot certify them.

Official references for the adapter: [Codex non-interactive events](https://learn.chatgpt.com/docs/non-interactive-mode) and [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference). The locally installed CLI help and captured events determine the tested adapter capability.
