← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **September model-release review**

# September 2026 Model-Release Review

## Scope and disposition

On 23 September, Andrew requested research into Opus 5.5, GPT-6 Sol and GPT-6 Luna, then requested a plan and its implementation. The agreed first stage updates model guidance, runner selection and evaluation preparation. Live evaluation needs its concrete run specification and resource limits; this record proposes those limits without claiming a run occurred.

The source review found implementation considerations, but no demonstrated defect requiring a constitutional change. The constitution, shared contracts, generated deployments, account settings and model preferences remain unchanged. No Claude adapter, general routing policy or publication is included.

## Sources and interpretation

Official sources were read during the research in this conversation on 23 September. Some Anthropic pages required browser access when direct retrieval failed. No third-party reproduction supports the maintained recommendations.

| Source | Finding used here | Disposition |
|---|---|---|
| [Opus 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) | Conditional advice for reconsideration, unattended execution and pasted source text. | Preserve correction and exploratory stopping; test the instruction/data boundary before introducing a delimiter convention. |
| [Opus 5.5 changes](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5) and [migration](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide) | Effort defaults and thinking, progress-block rendering and integration compatibility. | Recalibrate effort and inspect the actual host before changing prompts. |
| [GPT-6 guidance](https://developers.openai.com/api/docs/guides/latest-model) | Family coverage includes Sol/Luna; behavioural examples remain explicitly Astra-based. | Do not transfer Astra observations into claims about the new models. |
| [Sol](https://developers.openai.com/api/docs/models/gpt-6-sol) and [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) | Model positioning, effort options and tool/API compatibility. | Add explicit evaluation routes; adoption remains a separate decision. |

[Model guidance](../../kit/implementation/platforms/model-guidance.md) owns the maintained recommendations. Its other model rows retain their earlier source dates. Vendor claims, maintenance judgements and local behavioural results remain separate.

## Implemented changes

- Added dated Opus 5.5, Sol and Luna guidance, conditional-technique boundaries and concise host diagnostics.
- Added explicit Sol/Luna choices to the [Codex runner](../../kit/evals/run_evals.py), retaining Astra as default, the existing effort choices and the verified CLI-version restriction.
- Added offline tests covering CLI selection, frozen-plan reload, exact-session resume, separate grader selection and rejection of unsupported models without substitution.
- Added [N1/N2](../../kit/evals/instruction-boundary-probes.md) to the case registry and navigation. Existing fixtures did not provide a paired review-versus-explicit-adoption test. These authored text probes add no standing instruction and make no live-tool claim.

## Bounded evaluation specification

**Status: proposed, not frozen or run.** Prepare separate immutable plans only after confirming the batch, private output location and ceilings. Preparation must capture the final source and runner hashes. Use a new private directory outside the repository for each plan; record its exact location privately at freeze time. Native multi-turn sessions also persist in Codex's normal local session store. No live calls or retained run plans were created during this maintenance change; offline tests exercised temporary plans with a mocked CLI-version lookup.

### Codex stages

All proposed plans use CLI `0.155.1`, fixed effort `high`, grader `gpt-6-astra` at `high`, seed `19`, grading batches of four and a 240-second per-call timeout. High preserves the existing runner baseline; it is not a recommended everyday setting for either new model. Use explicit `gpt-6-sol` and `gpt-6-luna` responder plans separately. Do not pool their outcomes.

| Stage | Conditions and cases | Repetitions | Response / grade calls | Call ceiling | Soft token stop |
|---|---|---:|---:|---:|---:|
| Grader calibration | Eight existing authored anchors; `--calibration --comparison conformance` | 1 | 0 / 2 | 2 | 60,000 |
| Sol integration smoke | `core=core`; M3,I1; conformance | 1 | 5 / 1 | 6 | 180,000 |
| Luna integration smoke | Same as Sol smoke | 1 | 5 / 1 | 6 | 180,000 |
| Sol value comparison | `baseline=none`, `core=core`; M1,M2,M3,H1,H2,I1,I2,N1,N2 | 3 | 96 / 14 | 110 | 1,500,000 |
| Luna value comparison | Same as Sol value comparison | 3 | 96 / 14 | 110 | 1,500,000 |

These are planning ceilings, not predicted usage or a hard billing cap. Full execution would permit 234 calls across five plans with aggregate soft stops of 3,420,000 input-plus-output tokens under the runner's accounting. A call in flight can overshoot. Missing usage, CLI/provider errors or the frozen limits stop further calls. Retain incomplete cases; do not retry failures to improve the record.

Run calibration first and review anchor disagreements. Smoke checks then establish invocation, native continuation and accountable usage, not reliability. Stop before the larger comparisons if either integration is invalid. Confirm the value stages remain useful for the intended adoption decision before spending their budgets. An updated CLI requires separate usage captures before changing the adapter allowlist.

The comparison asks: **does adding the unchanged full core improve the measured interaction on each model while preserving shared gates?** M1/M2/M3 cover exploration, evidence changes, ownership and execution; H1/H2 cover material challenge and its control; I1/I2 cover clarification; N1/N2 cover instruction/data discrimination. Apply every shared gate and keep quality dimensions separate. Review critical failures and borderline grades against the transcripts. No combined model ranking or inference about human learning follows.

This batch does not load the voice skill. M2 checks ownership in a neutral authored message, not personal voice craft. D1/D2 require the documented four-file skill composition and separate setup; F1/F2 and J1–J4 require an isolated tool harness for actual effects. Leave these checks unverified rather than silently substituting a text-only answer. Condensed routes and transfer cases are outside this initial batch.

### Claude and effort follow-up

Choose the actual Claude surface before freezing an Opus plan. Record the client, available model/effort controls, exact supplied instruction revision, skills, memory and tool exposure. Begin with current deployed instructions, not an assumed copy of repository HEAD. The [Claude baseline](../../kit/implementation/platforms/claude/configuration-baseline.md) records known source/deployment differences.

Use the same selected text cases as conformance observations where the native surface supports them. Run skill-loaded D1/D2 separately with their required package and an isolated persistence probe separately where needed. Do not claim a native no-compact control if ambient instructions cannot be removed reliably. Keep results separate from Codex and distinguish a visible model label from verified backend identity.

No Claude run is authorised or claimed by this specification: surface, exact output destination and enforceable resource controls remain to be selected. For effort calibration after an initial behaviour check, propose a separate matched `medium`/`high` comparison, starting Opus at explicit `medium`. Freeze its limits before running; do not vary effort until a case passes.

## Verification and remaining limits

Local inspection on 23 September returned `codex-cli 0.155.1`; `codex exec --help` exposes explicit model selection and native resume. This matches the previously verified adapter version, but does not establish backend access to either new model.

Local checks completed:

- `python3 -B kit/evals/run_evals.py validate`: 30 cases, 37 user turns, eight grader anchors.
- `python3 -B -m unittest discover -s kit/evals -p 'test_run_evals.py'`: all 40 offline tests passed.
- `python3 -B kit/implementation/platforms/sync_contracts.py --check`: all seven generated contract copies current.
- Relative Markdown targets in the changed documents resolve; `git diff --check` passed.
- The selected value batch resolves to nine cases and 16 user turns; two conditions and three repetitions yield 96 response calls and 14 grading calls per model.

No live model invocation, behavioural pass, deployed-product validation, account change or model adoption is claimed.

## Decision after evaluation

Retain the existing instructions where they work. For a repeatable model/host-specific failure, propose the smallest implementation adjustment and a matched before/after check. Only a demonstrated general policy defect should trigger a separate constitutional proposal, cascade review and regression coverage. Record all failures and unresolved observations here rather than treating an unrun check as a pass.
