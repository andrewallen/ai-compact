← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Skills](README.md) · **Evaluation and re-review**

# Skill Evaluation and Model Re-review

Initial method proposed on 13 September 2026 in response to Andrew's request for token-efficient support that preserves appropriate use of state-of-the-art thinking partners. This is maintenance guidance, not additional standing context. The [capability matrix](capability-matrix.md) defines jobs; the [source register](source-register.md) identifies candidates. No behavioural runs, token benchmarks or model-routing changes were performed in preparing these documents.

The [package register](package-register.md) identifies baseline and candidate implementations; the [composition fixtures](../../evals/capability-composition-probes.md) make the initial pilot concrete. Both were prepared in Batch 1; no behavioural runs are implied.

## Optimisation target

Prefer the least costly configuration that meets the task's quality and operating-boundary requirements, accounting for corrections and Andrew's time. A shorter prompt, cheaper model or fewer output tokens is not sufficient evidence of improvement. Keep capable thinking-partner models available for ambiguous framing, substantive judgement, unfamiliar synthesis and consequential challenge. Do not route those jobs to a weaker model solely to reduce visible token counts.

Model improvement may remove the need for procedural scaffolding; it does not remove the need to state personal preferences, ownership, authority and scope. Distinguish:

| Instruction purpose | Review question | Possible response |
|---|---|---|
| Personal contract and boundaries | Is it still clear and reliably applied? | Preserve the requirement; propose condensation only with equivalence checks. |
| Domain/task facts and personal craft | Does the model have this specific context? | Supply relevant facts and examples on demand. |
| Reusable procedure or deterministic tool | Does it improve accuracy or save repeated work? | Retain when useful; test shorter instructions around it. |
| Workaround for an older model | Does the failure still occur with the current model and host? | Compare without the workaround; propose removal if obsolete. |
| Duplicate routing/style/gates | Does another loaded component already cover it? | Remove duplication in the lower-authority implementation when authorised. |

The current intended thinking-partner targets and dated vendor observations remain in [model guidance](../platforms/model-guidance.md). Do not duplicate a rolling model leaderboard here or equate effort labels across providers.

## Token and effort accounting

Measure a whole accepted task, including retries and repair turns. Compare within a documented model/client configuration before making cross-model conclusions.

| Cost component | Record where observable | Interpretation limit |
|---|---|---|
| Standing context | Contract source, project instructions, skill metadata and tool exposure. | Installed file size is not loaded context. Hidden client context may be unavailable. |
| Task context | Skill bodies/references actually read, retrieved material, images and tool output. | Bytes/characters are rough size indicators, not token counts. Images and tools have different accounting. |
| Model work | Input/output and reasoning usage where reported; effort and context settings. | Unreported reasoning is unknown. Lower verbosity does not establish lower total cost. |
| Reuse | Cached/uncached input where reported. | Cache savings affect billing/latency differently from context capacity. |
| Completion | Tool calls, retries, elapsed time, corrections and human editing time. | One cheap failed run can cost more than one successful capable-model run. |
| Outcome | Accuracy, usefulness, artifact integrity and contract adherence. | Model self-scores alone do not establish quality. |

Use token counts from the actual host/provider when available. Otherwise record unavailable and compare observable latency, loaded material and correction effort. Do not invent savings from skill count, assume every skill body loads, or extrapolate the approximate metadata figures in older guidance to another client. Progressive disclosure is an authoring method whose actual behaviour must be verified in the host. See [Anthropic authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) and [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills).

## Bounded comparison

1. Pick one capability and an actual recurring task. Define acceptance before choosing a skill. Keep input facts, requested output, tools, permissions, model/effort and memory posture comparable.
2. Pin the candidate and complete the package admission record: component attribution/licences, every reachable script/hook/tool/agent, dependencies, persistence and publication effects, actual host controls and fallback. Source review treats package instructions as data. Start fresh sessions so earlier loaded content does not contaminate the baseline.
3. Run **A: current native capability plus the existing applicable contract**, **B: A plus one candidate**, and only if justified **C: A plus a smaller task-specific adaptation**. A is not a constitution-free baseline. Run model-upgrade comparisons separately so a model change is not misattributed to a skill.
4. Start with a representative task, a difficult or incomplete-input case, and an out-of-scope request where the skill should stay inactive. For editorial work include a strong personal passage needing little or no editing. For design include a constrained/reference-led brief as well as a freer one.
5. Judge outcomes against the brief. Inspect rendered pages/slides/sites, not just source or file validity. Check facts, citations and ownership. Where possible hide the provider label during human preference review. Keep objective checks separate from aesthetic preference.
6. Record total cost and repair work. Repeat near-ties or variable outcomes before selecting; a small pilot is directional evidence, not a universal benchmark.
7. Recommend retain, adapt, narrow activation, use manually, or omit. Deployment and removal remain separately authorised actions. Keep raw private test material outside the public repo; save only concise evidence when approved.

Anthropic's [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) is a useful reference for comparative runs and human review. Its complete client-specific workflow is not automatically part of this method.

## Plugin-aware evaluation

The current trial scope is the [first-party inventory](first-party-inventory.md). Earlier external observations below remain research history, outside the lab-only shortlist. Inspect publisher attribution separately from marketplace inclusion. Evaluate package components and effects—skills, routers, apps/MCP, commands, hooks, scripts and templates—not only SKILL.md. Record cached, installed, enabled, exposed and actually loaded as separate states.

OpenAI [plugin-eval](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/plugin-eval) is a first-party evaluation candidate. Its static checks and budget explanations can inform inspection; live benchmarking is a separate execution step. Neither static size estimates nor package counts establish token savings. Keep the tool at maintenance time and preserve the same capable-model baseline for thinking work.

Anthropic discernment-nudge adds prompts to scrutinise AI output. Review whether this duplicates the constitution’s existing independence and uncertainty requirements; availability alone is not a reason to add standing nudges.

## Composition and admission decision

Use implementation IDs to tie every comparison to the exact native baseline and added package. Record cache, installation, enablement, exposure, loading and successful exercise separately, with unknowns where unavailable. A public source and a same-named runtime are not interchangeable revisions. Keep the approved corpus, output targets, run/spend limits and evidence destination explicit before live execution.

One primary workflow may coordinate required complementary stages. Test positive invocation, an unrelated request, exploration with production skills available, and both absent and explicit write authority. Reuse existing ownership, clarification, persistence and evidence fixtures. Host-required routes and their unavoidable effects are part of the configuration, not instructions this kit can override. Reject an unresolved material conflict in that host.

Assess marginal value rather than cataloguing features: correct and usable output, preserved boundaries, human preference, repair effort and actual usage. A source inspection, static byte budget or fixture definition never counts as a behavioural result. A native-only result is valid; an inconclusive small pilot stays inconclusive. Preserve rejected/unnecessary candidate records so re-review needs a new reason.

## Initial trial order

| Priority | Comparison | What the result would decide |
|---|---|---|
| 1 | Current thinking-partner configuration versus reduced duplicate implementation context, with the same capable model. | Whether context can shrink without losing useful challenge, nuance, scope or ownership. No constitutional text removed as part of this documentation task. |
| 2 | Existing my-voice review versus native editing; evaluate first-party doc-coauthoring or ux-copy only for matching work. | Whether the editor repairs remaining defects or mainly duplicates rules and flattens voice. |
| 3 | Native website design versus Anthropic frontend-design/Design or OpenAI Product Design, one candidate per run. | Which adds appropriate design quality per completed task. |
| 4 | Native editable presentation with an approved reference; compare the other lab’s first-party format/design workflow only where a gap appears. | Whether the gap is visual design, output mechanics or medium choice. |
| 5 | Native synthesis versus targeted knowledge-synthesis; native analysis versus targeted validation. | Whether procedural additions improve evidence handling enough to justify their cost. |

## Preliminary constitution intersections

These are static observations from selected instructions, not a completed audit of every candidate. They do not activate the quoted instructions. The [operating contract](../../constitution/02-operating-contract.md) remains canonical.

| Candidate or overlap | Specific observation | Relevant boundary and proposed disposition |
|---|---|---|
| [Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md), Voice/workflow | Inspected text allows an opinion or reaction when the voice calls for one. | Ownership: adapt to prohibit invented personal positions before adoption. |
| [No-ai-slop](https://github.com/petergyang/no-ai-slop), editing patterns | Local copy preserves meaning and offers detect-only mode, but has broad word bans and overlaps my-voice. | Voice/refinement: trial as a separate requested pass; preserve legitimate technical terms and personal constructions. No parity claim with upstream. |
| [Impeccable](https://github.com/pbakaus/impeccable), init/install | Init creates PRODUCT.md; design/state files and optional hooks are part of the workflow. | Scope/persistence: define exact project artifacts and hook effects before an installation or use proposal. No blanket approval for new records. |
| [Anthropic productivity](https://github.com/anthropics/knowledge-work-plugins/tree/main/productivity) | Own task and two-tier memory arrangement. | Memory/architecture: reference only until deliberate integration is chosen. |
| [Literature review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md) | Requires generated figures and supporting tools. | Proportionality/evidence: adapt unconditional figures and verify dependency fit for the actual research job. |
| [Anthropic pptx](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) | Requires a visual on every slide; provides size/layout defaults. | Quality/judgement: brief and delivery context should determine density and visual need. Preserve useful rendering checks. |
| Generic brainstorming/reasoning skills | Could duplicate framing, impose conclusions or activate personal voice during thinking. | Exploration/independence: inspect exact instructions before use; no generic add-on proposed for C01. |
| Multiple design or editorial routers | Simultaneous activation can supply conflicting style rules or repeated review gates. | Authority/completion: one primary workflow per job; narrow or manually invoke alternatives where the client supports it. |

A full intersection review records exact revision, instruction location, conflict, evidence, proposed adaptation and disposition. Static compatibility and task quality are separate gates. Failed ownership or authority checks cannot be offset by prettier output or lower usage.

## Re-review when models or products improve

Use meaningful events rather than continual catalogue expansion: a primary model upgrade; a material client/skill/tool change; repeated live friction; a new recurring task; or a vendor feature that appears to replace custom scaffolding. A release announcement is a review trigger, not proof of benefit. This document creates no scheduled monitoring or automatic package updates. Inspect changes to discovery descriptions as well as bodies, hooks and tools; a metadata change can alter activation. Capture the previous working configuration and rollback limits before an authorised deployment, especially where a vendor runtime cannot be pinned or restored.

For each event:

1. Record exact old/new model and host, changed controls and relevant official guidance. Preserve the previous configuration for comparison where practical.
2. Re-run a small representative set, including thinking-partner behaviour, source fidelity and unwanted skill activation. Reuse existing [eval categories](../../evals/README.md); designing this method does not claim those fixtures have been run.
3. Separate the model's native improvement from instruction effects. Test removing one obsolete workaround or reducing one duplicated context block at a time within an authorised batch.
4. Check whether the new model needs less scaffolding, different effort or fewer repair loops. Consider a smaller model for bounded mechanical work only if measured reliability and correction costs justify it; keep ambiguous judgement with the capable partner when needed.
5. Propose exact changes and their evidence. If a constitutional requirement changes, flag the derived-platform cascade and apply the established governance process. If only a skill/adapter changes, avoid rewriting higher-authority policy to accommodate it.
6. Record the result, adopted decision if any, deployment verification and the next meaningful trigger. Remove obsolete guidance when authorised instead of accumulating counter-instructions.

No target percentage of token savings is set before measurement. The first decision is which additions produce a material benefit over the current kit and which can remain outside ordinary working context.
