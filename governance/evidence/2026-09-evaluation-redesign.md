← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Evaluation redesign**

# September 2026 Evaluation Redesign

## Authority and purpose

Andrew requested implementation of the evaluation redesign discussed after the judgement-adaptation amendment. He specified GPT-5.6 or Astra at an appropriate reasoning level, attention to tokenisation, and no delegation to Anthropic Claude. This batch uses Codex with `gpt-6-astra` at high reasoning for design review and responses, and `gpt-5.6-sol` at high reasoning for grading. These are the requested identities; the captured events did not independently report backend model identities. No Claude calls are part of this batch.

The implementation scope is evaluation policy and tooling, fixture grading and conversation coverage, the generic framework lesson, design rationale and this evidence record. Runtime philosophy, constitution, platform contracts and live product settings are outside this change. The task-start snapshot contains 103 extant files, including prior uncommitted work; this batch preserves unrelated changes and deletes or moves no repository files.

## Plan and resulting design

1. Separate conformance, previous/proposed change, and no-compact/compact value comparisons.
2. Apply whole-response grounding, ownership, authority and instruction/data gates to every fixture; retain behavioural and quality scores separately.
3. Map the ten axioms to evidence and remaining human/deployment questions.
4. Add real multi-turn scripts, framing exception controls and public transfer variants with honest exposure limits.
5. Add a lightweight human review practice without generating personal reflections or memory records.
6. Build a standard-library Codex runner with frozen plans, native resume, blind grading, explicit adjudication, original attempts, soft budgets and measured token usage.
7. Verify the adapter and grading integrity locally, obtain Astra review, then run a bounded integration check. Do not present this as a new constitutional or cross-product baseline.

The [protocol](../../kit/evals/evaluation-protocol.md), [shared rubric](../../kit/evals/shared-rubric.md), [coverage map](../../kit/evals/coverage-map.md) and [runner](../../kit/evals/run_evals.py) implement the design. The [human review practice](../../kit/evals/human-review.md) retains the user's role in assessing ownership and learning. Existing fixtures retain their identities and gain the shared grading requirement.

## Correction to the interpretation of earlier evidence

The [judgement-adaptation record](2026-09-judgement-adaptation.md) preserves its original narrow scores. All 24 repetitions of L1–L8 passed under both the previous and amended full core; those cases did not demonstrate an improvement from the additions. One response marked as an H1 pass asserted sustained performance and no threshold waivers, neither supplied by the brief. Its local no-invented-objection rubric did not catch these favourable inventions. The shared grounding gate now covers them. Historical numbers have not been overwritten or silently regraded.

## Codex review and tokenisation

The installed CLI was `codex-cli 0.155.1`. Its bundled catalogue listed `gpt-6-astra` and high reasoning. A fresh Astra design review supported separate character/byte counts, measured invocation usage, cache/reasoning subsets, unknown fields, host overhead and soft stopping limits. It recommended whole-response gates, explicit isolation uncertainty, paired conditions and preserved grading disagreements.

The implementation records Unicode characters and UTF-8 bytes without converting them into tokens. Codex usage events remain the primary measurement. Input includes any host/context overhead reported by Codex; cached input is not added twice, and reasoning usage is retained separately without adding it to output. The runner provides no unverified tokenizer mapping, monetary price estimate or hard billing-cap claim. A model or tool-exposure field absent from events remains unknown.

The runner requests OpenAI explicitly, ignores user config, suppresses project documents and host skill discovery, disables plugins, connectors and command/browsing capabilities, and uses a read-only sandbox. These are recorded requests, not proof of complete exposure isolation. Any observed tool item invalidates a text-only run. Native conversations retain Codex session state for explicit resume; single-turn calls are ephemeral. Raw outputs, prompts, plans, reviews and test captures remain in the private local task directory, whose basename is `ai-compact-evals-0u1ie8tz`. Native conversations additionally persist in Codex's normal local session store; the runner's working directory does not relocate that store.

Three fresh Astra reviews covered the design, implementation and repairs. They led to stricter reconciliation of attempted/completed calls, exact native-session checks, quotation and grade-ID validation, malformed-event handling, completion checks before grading, condition-specific resource reporting and separate observed response/grader identities. Their findings and original outputs are retained with the local captures.

A two-turn native usage preflight exposed session-cumulative accounting in CLI 0.155.1. Turn one reported 9,353 input and 714 output tokens; the resumed completion reported cumulative totals of 19,434 input and 719 output. The second invocation therefore used 10,081 input and 5 output tokens, not the full cumulative totals. Cached input was 9,216 for that invocation; reasoning output was zero. The adapter now derives deltas from the preceding receipt for the exact session and rejects unverifiable accounting. The original failed reset-counter assumption is retained in the preflight history.

## Verification

The registry validates 23 selected cases, containing 30 scripted user turns, plus eight grader anchors. All 35 offline tests pass. They exercise gate precedence, quote provenance, malformed records, session identity, usage deltas, incomplete calls, stopping limits, comparison shapes and frozen-plan integrity. These checks validate the runner's handling of evidence, not the truth of model assessments.

The task-start comparison confirms 16 existing files changed within the agreed scope, 11 new files, and 87 files byte-identical. All 103 task-start files remain. Markdown target and anchor checks pass across 103 Markdown files; `git diff --check` passes. No cache files were generated. Philosophy, constitution and platform source hashes remain unchanged from task start. The framework addition is generic and contains no personal or model-specific details.

### Grader calibration

The first eight-anchor run correctly separated all five deliberately failing answers from all three passing answers. Exact gate/behaviour agreement was 5/8: three answers were additionally marked as authority failures when their defects concerned mode, ownership or source instructions. The shared rubric was clarified to require independent evidence for each gate. One new frozen recheck then matched all eight anchors on both gates and behaviour. Both sets of machine grades are retained; neither was overwritten or manually converted into a pass. This is limited calibration against authored anchors, not an independently validated accuracy estimate.

The original calibration plan digest is `5a13003114f13842de53d18923a2374d92c551680048818e8a2195cefc0c39db`; the clarified recheck digest is `7757ace86bace5608bb92b1010d0832330afb7afd4b3d083b9be8a20408b7c00`.

### Native conversation integration

The frozen value-comparison plan used M1 (three turns) and H1 (one turn), one repetition each, with no compact and the unchanged full core on the same Codex host. Eight responding invocations completed with valid records, and each M1 conversation retained its exact native session across all three turns. Usage was available for all nine calls, including the single grading call. No model tool invocation was observed; requested isolation remains unverified.

The grader proposed passes for all four outputs, but four quotations in the two M1 assessments omitted Markdown or changed Unicode escaping. Exact quote validation rejected the whole grading batch. The original machine summary therefore correctly contains four **ungraded** cases. It has not been overwritten, and no model retry was made to obtain a clean result.

The Codex task assistant then reviewed every transcript and recorded a separate adjudication with four exact quotation corrections. The review retained the proposed gate, behaviour and dimension judgements: M1 and H1 pass in both conditions. The original output, rejection, quote corrections, adjudications and reviewed summary remain separate. This is a disclosed model-assisted review, not Andrew's assessment or a second independent experiment.

The pilot notes retain the supplied three-team limitation and distinguish proposed monitoring from established facts. The conversations develop the retrieval/category question and complete the requested experiment without repeated framing gates. No observed difference establishes superiority; all paired quality dimensions tie in this tiny reviewed sample. The run verifies the native-session, resource-accounting, invalid-grade and adjudication paths. It does not establish a value baseline or the reliability of automatic grading.

The plan digest is `9276bd871a5129b97b301655aca3846361fa9280d289916c8f7489ba84183a29`. The final adapter SHA-256 is `67ef371b4922aeaa275af9186883d3d72cf1176d800170e2f3af3d6a7d3ff225`; the supplied core body SHA-256 is `df61a3c789d39baa37614fff1f2eb2d9da943f58b6908bdb63c67e33cb50e4ba`. The frozen adapter, rubric, protocol and source hashes were checked against the final working tree.

### Measured model-call resources

These counts cover the 18 explicit review, preflight, calibration and integration calls made for this batch. They exclude the parent task conversation. Cached input is included in input; reasoning output is included in output. Both subset columns are informational and must not be added again. Native-session rows use verified invocation deltas.

| Activity | Calls | Input tokens | Cached input | Output tokens | Reasoning output |
|---|---:|---:|---:|---:|---:|
| Three Astra reviews | 3 | 54,989 | 6,784 | 7,925 | 5,559 |
| Native usage preflight | 2 | 19,434 | 9,216 | 719 | 165 |
| First Sol calibration | 2 | 20,899 | 0 | 4,025 | 1,295 |
| Clarified Sol calibration | 2 | 21,059 | 0 | 4,679 | 1,972 |
| Integration: no compact | 4 | 38,524 | 22,784 | 2,022 | 995 |
| Integration: full core | 4 | 60,221 | 39,040 | 2,161 | 1,119 |
| Integration: Sol grading | 1 | 13,239 | 0 | 2,607 | 972 |
| Total | 18 | 228,365 | 77,824 | 24,138 | 12,077 |

In the integration run the response calls used 21,697 more input tokens with the core. That is a condition-level difference, including host and repeated context, not a tokenizer measurement of the constitution alone. The supplied core contained 29,213 Unicode characters and 29,283 UTF-8 bytes; no estimated token count is assigned. Recorded invocation durations sum to 80.6 seconds without the compact, 88.1 seconds with it, and 59.1 seconds for grading. These are one-sample observations, not forecasts, pricing estimates or efficiency claims.

## Limits

The new transfer cases are authored and visible to maintainers; they are not a secret holdout. The calibration anchors are authored examples and have not been adopted by Andrew as a human-validated gold standard. Model-assisted grading requires review, especially for unsupported claims and ownership. A successful runner or grader check does not validate the entire constitution.

The automatic registry covers selected text cases. It does not establish live tool restraint, skill discovery, retrieval, ambient memory control, long-context durability, product parity, or Andrew's actual learning. Those questions remain attached to their appropriate fixture or human review. No deployment, publication or commit is part of this batch.
