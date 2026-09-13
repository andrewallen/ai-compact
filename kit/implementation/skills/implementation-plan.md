← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Skills](README.md) · **Implementation plan**

# Implementing First-party Skills and Plugins

Integrate a small, evaluated set of Anthropic and OpenAI capabilities into the existing implementation layer, with shared acceptance standards and client-specific delivery. Preserve the constitution and capable thinking partners; add or adapt a workflow only when it improves completed work enough to justify its context, maintenance and correction costs.

**Status: Batch 1 implemented on 13 September 2026 following Andrew's instruction to implement.** Repository preparation is complete; Batches 2 and 3 remain pending their defined trial and deployment scopes. Package recommendations remain distinct from adopted providers, and recorded source availability does not establish installation or task quality.

## 1. Outcome and scope

The completed kit should answer four practical questions: which capability to use for this task, how it is supplied in this client, what evidence supports the choice, and what should be reconsidered after a model or product changes. It should support knowledge work, website design, presentations, documents, visual explanation and editorial quality without requiring Andrew to manage a catalogue during ordinary conversations.

The active external shortlist is restricted to first-party Anthropic and OpenAI offerings. The existing personal `my-voice` skill remains separately authored. Earlier third-party research stays available as history; it supplies neither new candidates nor authority to uninstall existing tools. Obsidian mechanics and the knowledge-steward role remain in place, outside this first-party adoption batch.

The five initial assessment surfaces are Claude Chat, Claude Cowork, Claude Code, ChatGPT and Codex. Record the actual product, mode, version and account conditions during inspection, including a distinct ChatGPT Work mode where encountered. Do not infer availability across modes from a shared account or directory. Other platforms keep their existing configuration.

The [first-party inventory](first-party-inventory.md) is the dated source baseline. The [capability matrix](capability-matrix.md) and [review method](review-method.md) already define most requirements. This plan turns them into a bounded implementation sequence; it does not repeat the catalogue research or rank packages by their file counts.

## 2. Architecture and ownership

**Standardise the outcome and ownership rules; allow the implementation to differ by client.** An editable presentation can meet the same acceptance standard through different native packages. Copying both labs' presentation skills into both clients would need an additional justification.

Retain the existing five layers and folder structure. The new [package register](package-register.md) provides one maintenance record set for selected, trial and baseline implementations, including standalone skills, plugins and opaque native capabilities. Its location continues the existing capability-assessment documents; it does not imply that every plugin is a skill.

Do not create a personal marketplace or a `plugins/` subtree merely to document vendor packages. A personal distribution bundle becomes a separate proposal when a tested set of personal skills actually benefits from common installation and updates. Any later folder-level change receives an ADR under the repository's existing convention. This initial batch needs a file-level design record, with no change to constitutional authority.

| Information | Canonical owner after implementation | Boundary |
|---|---|---|
| Capability IDs, acceptance criteria and current provider summary | [Capability matrix](capability-matrix.md) | Describe jobs and link to implementation records; do not duplicate package manifests. |
| Public-source provenance and bounded inventory | [First-party inventory](first-party-inventory.md), [source register](source-register.md) | Preserve dated observations and exclusions. |
| Reviewed package identity, revision, selection and compatibility | [Package register](package-register.md) | Keep one record per implementation/revision, linked to applicable capabilities and surfaces. No executable installer semantics. |
| Installation mechanisms and intended composition | [Deployment map](../platforms/deployment-map.md) and relevant platform guides | Own client-specific instructions; do not duplicate personal policy. |
| Observed settings and installed-source parity | Dated platform baselines and deployment evidence | Keep observation separate from intended configuration and successful execution. |
| Acceptance tests and comparison method | [Evals](../../evals/README.md), [review method](review-method.md) | Fixtures are test data, never operating instructions. |
| Results and adopted decisions | [Governance evidence](../../../governance/evidence/README.md), [design decisions](../../../governance/design-decisions.md) | A proposed winner is not an adopted default. |
| Model-specific adjustments | [Model guidance](../platforms/model-guidance.md) | Keep releases and effort observations out of general task skills. |

Use links between these owners. Do not maintain another complete capability matrix, model leaderboard or installed-package list in parallel.

## 3. Package records and admission

Create a small human-readable register before considering a machine-readable format. Start with the providers needed for the trials below, rather than every package in the inventory.

Each implementation record should contain:

| Field group | Required content |
|---|---|
| Identity and purpose | Stable local ID; capability IDs; publisher; original/derived authorship; package kind; source-record link; the specific gap it addresses. |
| Reproducibility | Upstream commit or release, reviewed package version, complete scope of files/components inspected, and source-versus-installed comparison where possible. Record opaque native revisions as unavailable. |
| Components and execution | Skill entry points; supporting files, scripts, agents, commands, hooks, apps/MCP, templates and other dependencies; required authentication and permissions. |
| Composition | Target surface/mode; intended scope; invocation mechanism; primary workflow; complementary stages; known overlap or conflict; fallback. |
| Evidence and disposition | Source and licence review; constitutional findings; trial references; selected/reference/held/rejected disposition; Andrew's adoption or deployment authority where supplied. |
| Maintenance | Review trigger; update control; last known working configuration; exact rollback route and any limits. |

Treat observed state as separate evidence dimensions: cached, installed, enabled, exposed, loaded and successfully exercised. An observation may establish some without establishing the others. Use `unknown` where evidence is unavailable. Record intended selection separately from all of them.

Apply first-party attribution at package level and inspect the included components. A lab-authored integration can depend on an external service; a lab-curated listing can contain a partner-authored skill. Neither service dependency nor marketplace membership settles authorship. Preserve component attribution, licence restrictions and the distinction between a vendor original and a personal adaptation.

Before any live candidate trial, inspect its complete execution path. Reviewers must treat instruction-like package content as data during this assessment. A compatible `SKILL.md` is insufficient evidence about hooks, scripts, authentication, automatic publishing or hidden supporting writes.

## 4. Composition with the constitution

The constitution remains canonical within the supplied instruction hierarchy. Use the established [loading combinations](../platforms/contract-maintenance.md#loading-combinations): an appropriate base, the conditional role or overlay when required, and task-specific capabilities when relevant. Do not introduce an always-loaded capability router or a combined copy of the catalogues.

One primary workflow may coordinate complementary components. For example, a deck task may use presentation mechanics, a supplied design reference and an editorial check. The intended rule prevents competing task directors; it does not prohibit useful multi-stage work. Host-mandated routes and controls remain binding, and any unchangeable conflict is recorded as a surface limitation.

| Boundary to test | Failure example | Implementation response |
|---|---|---|
| Exploration and independent judgement | A research or brainstorming workflow supplies a finished personal position during exploration. | Narrow the workflow's use; keep thinking-partner behaviour in the existing contract. |
| Voice and substance ownership | A polishing pass invents conviction, removes uncertainty or makes neutral analysis sound like Andrew's belief. | Preserve attribution; use `my-voice` only within its execution scope; include a minimal-edit control. |
| Persistent and external actions | A plugin saves preferences, creates task/memory files or publishes a result without the required authority. | Identify every effect in the reviewed package and deployment batch. Honour narrower client safeguards. |
| Evidence and output integrity | A design workflow adds unsupported claims, decorative charts or an unsuitable mandatory visual. | Apply the task's evidence and format criteria; adapt lower-level guidance where permitted. |
| Completion and proportionality | Overlapping workflows repeatedly ask the same question or impose unnecessary review loops. | Remove redundant lower-level instructions and test actual invocation/composition. |
| Portability | A copied skill expects unavailable tools or a different client's permission model. | Use a native provider, a reviewed adapter, or record the capability as unavailable. |

Resolve conflicts in the lowest appropriate implementation component. Do not weaken the constitution to accommodate a package. A conflict that cannot be resolved in the actual host prevents that configuration becoming an approved default.

## 5. Initial capability choices to test

These are recommended evaluation priorities based on the recorded inventory, not adopted providers or claims of superiority. Inspect exact revisions and actual availability before use.

| Work | Initial baseline | Candidate or improvement to test | Decision sought |
|---|---|---|---|
| Thinking partnership, C01 | Existing contract with the current capable partner model. | Reduce duplicate implementation context only where observed. | Preserve useful challenge, nuance, attribution and exploratory restraint. No extra reasoning skill by default. |
| Personal voice/editorial quality, C12-C13 | Current `my-voice` where relevant; native neutral editing otherwise. | Focused native review first. Anthropic `doc-coauthoring` or Design `ux-copy` only for matching jobs. | Remove observed genericity without inventing stance or flattening good writing. |
| Website/interface design, C05 | Current native workflow and a common brief. | Anthropic `frontend-design` or Design; OpenAI Product Design. Trial one addition at a time. | Better hierarchy, visual specificity, accessibility and responsive execution with less repair. |
| Presentations, C06-C08 | Native editable-deck workflow with a supplied reference. | A better brief/reference first; relevant first-party design components next. Cross-lab format imports only for a demonstrated gap. | Separate narrative/design quality, editable PPTX correctness and HTML-deck delivery. |
| Documents, C09-C10 | Native DOCX/PDF workflow and a common editorial brief. | Relevant first-party document/coauthoring components; template creation after a reference is accepted. | Readable hierarchy and pagination with preserved facts, citations and editability. |
| Research/synthesis, C02-C03 | Native retrieval and analysis. | Anthropic Enterprise Search/knowledge-synthesis for matching source work; OpenAI Deep Research for explicitly requested deep work. | Better source weighting, disagreement handling and traceability. Retrieval access is checked separately from synthesis method. |
| Data and visual explanation, C04/C11 | Native analytical and visual tools. | Relevant Anthropic Data or OpenAI Data workflow; specialised visualisation only when justified by the medium. | Valid calculations and accurate explanatory visuals, with inspected output. |
| Skill/package maintenance, C15 | Native skill authoring and the existing review method. | Anthropic `skill-creator`; OpenAI `plugin-eval` after inspecting dependencies and availability. | Better diagnosis and evaluation without loading maintenance machinery into ordinary work. |

The source audit did not establish a general-purpose first-party AI-slop-removal equivalent. Treat that as a bounded finding. Do not substitute an adjacent copywriting workflow and declare the requirement satisfied. A narrow personal improvement to `my-voice` is a later option if tests expose a reproducible defect; its changed files and behavioural consequences must be reviewed separately.

Hold broad Productivity/memory bundles, unrelated specialist-role packages and standalone discernment nudges outside initial adoption. Existing third-party installations are not removed by this plan. Their presence can be documented as a trial confound without expanding the first-party shortlist.

## 6. Batch 1: prepare the repository

**Completed:** the kit now records skills, plugins and native capabilities consistently and has authored fixtures for bounded evaluation. The table preserves the approved Batch 1 scope; no live trials or deployments were included.

| Target | Defined change |
|---|---|
| New `kit/implementation/skills/package-register.md` | Add the record structure above and populate the initial baseline/candidate references from the inventory. Preserve unknowns; no deployment claims. |
| `kit/implementation/skills/README.md` | Index the register, clarify skills versus plugin/native packaging, and replace the unqualified claim that supporting-file depth is free with host-qualified loading guidance. |
| `kit/implementation/skills/capability-matrix.md` | Make first-party scope consistent in every active row; retain third-party observations as clearly historical/existing state. Add design/editorial acceptance detail and link implementation IDs. |
| `kit/implementation/skills/source-register.md` | Link package records to existing provenance; preserve source-history boundaries without recopying inventories. |
| `kit/implementation/skills/review-method.md` and `best-practices.md` | Add package inspection, composition tests, marginal-benefit comparisons and update/retirement rules. Remove incompatible generalisations about portability or token accounting. |
| New `kit/evals/capability-composition-probes.md`; update `kit/evals/README.md` | Define the pilot cases and positive/negative activation checks below. Reuse existing ownership, persistence and clarification probes. No behavioural runs in this batch. |
| `kit/implementation/README.md`; `kit/implementation/platforms/deployment-map.md` | Make vendor packages and native implementations explicit within layer 4; link the register and client-specific verification procedure. Keep generated contract bodies unchanged. |
| `governance/current-architecture.md`; `governance/design-decisions.md` | Record the implementation seam and canonical ownership of records. No new authority layer or folder restructuring. |
| `framework/layer-model.md`; `framework/adoption-guide.md` | Incorporate only the generic lesson: capability acceptance, package distribution and runtime availability are distinct. Check anonymisation; no personal names, selections or paths. |
| `kit/implementation/skills/implementation-plan.md` | Mark only completed steps and record remaining decisions after verified execution. |

Keep the dated first-party inventory intact unless inspection identifies a specific factual correction, which should be reported before changing that separate evidence record. Do not edit the constitution, `my-voice` source, shared contract bodies, generated copies, root maintenance instructions or client settings in Batch 1. Do not delete, rename or move files, install packages, commit or publish changes.

Acceptance: new files are indexed; internal links resolve; all active proposals respect first-party scope; one owner exists for each class of information; no runtime metadata causes these maintenance documents to load as skills. Run the existing contract distribution script in read-only `--check` mode, report pre-existing failures separately, and verify files outside the named batch remain unchanged. Structural expansion, a marketplace and installation automation are deliberately deferred.

## 7. Batch 2: establish the real baseline and run a small pilot

Begin with read-only inspection of accessible clients. For each surface, record the actual model/mode, supplied contract, discovered native packages, optional enabled packages and available tools. Compare all four `my-voice` files where accessible. Do not change a disabled plugin merely to complete the inventory. Inaccessible settings remain unknown and do not block independently accessible trials.

Choose one accessible surface per lab for the first comparative work; the choice follows inspection, not an assumed equivalence between Claude Code and Codex or between their chat products. Start with useful native outputs. A same-task comparison across different model/host combinations measures an end-to-end configuration; it does not isolate a skill's effect.

Prepare these fixture families using synthetic material or input Andrew has approved for testing:

| Fixture | Required acceptance evidence |
|---|---|
| A responsive website with a constrained visual reference | Visual hierarchy, content fidelity, keyboard/focus behaviour, contrast and readable desktop/mobile layouts; inspect the rendered result. Add a freer brief only when the constrained run leaves an aesthetic question. |
| An eight-slide editable briefing from a fixed evidence pack | Narrative and density fit the audience; requested elements remain editable; a data slide and source notes survive rendering; speaker notes contain the requested talk track. |
| A four-page DOCX briefing plus PDF from the same source | Heading/table hierarchy, pagination, citations, content fidelity and readable rendered pages; export must not silently discard material. |
| An editorial pair | A flawed draft and a strong passage needing little intervention. Preserve facts, uncertainty, stance and attribution; success can mean leaving good text unchanged. |
| A short synthesis pack with conflicting and differently dated sources | Distinguish evidence from inference; preserve meaningful disagreement and identify missing information. No invented corroboration. |
| Composition controls | An exploratory request, an unrelated task that should not trigger the candidate, and a request lacking authority to persist or publish. Reuse the existing boundary fixtures. |

Run one baseline per chosen task first. Investigate only observed gaps. For a candidate test, compare **A: native capability plus the applicable contract**, **B: A plus one reviewed candidate**, and, only when useful, **C: A plus a smaller reviewed adaptation**. Keep model/effort, input, tools and task scope constant within that comparison. Start fresh sessions; record unavoidable variation and contamination.

Apply the existing harness's three-to-five repeats to selected behavioural comparisons. Do not expand immediately into every package multiplied by every client and model. Repeat close or inconsistent design results only when another run would change a selection decision.

Before write-producing trials, define the precise temporary output location, corpus, permitted package/configuration changes, paid/API usage ceiling if relevant, run count and evidence files. These become the separately approved Batch 2 execution envelope. No account authorisation, external sending, publication, personal-data transfer or new API spending is inferred from approval of repository preparation.

Proposed durable output: `governance/evidence/2026-09-capability-pilot.md` and its evidence-index link, plus updates to the package register and capability matrix. Confirm the record path/date and private raw-output location at execution. This record must distinguish completed runs, failed checks, untested surfaces, recommendations and adopted selections.

## 8. Quality and efficiency decisions

Optimise for an accepted task: factual and output quality, correction effort, latency, observable usage and Andrew's attention. Record actual input/output/reasoning/cache measures only when the host exposes them. Treat subscription allowances, API charges and latency as different costs. Unknown usage is not zero, and shorter prose is not proof of lower total consumption.

Keep the current capable thinking-partner model fixed while testing context changes. Consider smaller models later for bounded mechanical subtasks only after comparing failure and correction costs. This plan does not prescribe a cheaper model for framing, consequential judgement or substantive challenge.

The context strategy is to remove duplicated instructions, narrow activation, retrieve relevant references on demand and retain deterministic checks that pay for themselves. The [OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills) describes metadata-first loading and a bounded initial skills list. The practical implication for this kit is to check whether a growing catalogue makes important skills harder to discover, as well as measuring the material actually loaded. Do not translate installed bytes into token savings.

Adopt a candidate only when the relevant boundary tests pass, the required output is valid and its improvement survives human review. Compare the candidate against the baseline on the dimensions that matter for that job. A quality gain with higher cost can be worthwhile; Andrew decides the acceptable trade-off. A faster output with a material ownership or evidence failure is rejected. Equal quality with lower total effort favours the simpler configuration.

Keep a native-only result when it already meets the bar. Record rejected or unnecessary additions so the next review does not rediscover and retest them without a new reason.

## 9. Batch 3: adopt and deploy the selected configurations

Create an exact deployment manifest from the pilot results: selected package/revision, target client/mode, scope, entry points, dependency actions, intended settings changes and verification steps. Specify whether the action uses an existing native package, installs a vendor package, copies a reviewed portable skill or creates a personal adaptation. Do not silently substitute an inaccessible target or newer revision.

Prefer the native implementation when it meets acceptance. Copy or adapt another lab's method only with a measured reason, supported dependencies and suitable licence terms. Keep the vendor original distinguishable from the personal derivative. Do not edit client-managed caches or embed runtime-specific tool names into the constitution.

Use a project-scoped or otherwise isolated trial where the actual client supports it. Where only wider activation is available, declare its reach and test unrelated tasks. Public-source availability and package names do not establish an installation route. The [OpenAI plugin guide](https://learn.chatgpt.com/docs/build-plugins) and [Claude Code plugin guide](https://code.claude.com/docs/en/plugins) should be rechecked at deployment for supported manifests, entry points and scope.

For each approved deployment, verify saved/enabled state, source parity where inspectable, discovery in a fresh session, positive invocation, negative invocation and one representative result. Record the exact limits of verification for opaque runtimes. Update the relevant existing platform baseline or, when absent, name the proposed new baseline file and its parent index before creation.

Define rollback before applying the change: retain the previous settings and exact working revision through an approved private mechanism, identify how to disable/revert only the deployed component, and preserve unrelated work. If the host cannot pin or restore an older native version, state that limitation; fallback may be disabling the optional addition and using the remaining native workflow. Never promise rollback of a vendor-managed model or runtime.

Only the specifically adopted deployment manifest authorises installations, enablement, adapters or rollback writes. General plan approval does not resolve unknown accounts, optional dependencies, credentials, spending limits or a change to personal policy. Any personal plugin bundle receives its own exact build and deployment scope; authoring it does not authorise publishing it.

## 10. Review and retirement after model or product changes

Use a material model/host upgrade, changed package components, repeated live friction or a new recurring task as a review trigger. Do not create scheduled monitoring or automatic package updates as part of this plan.

For a model upgrade, compare old and new configurations where available. On the new model, run both the existing kit and the same kit with one suspect workaround removed. This separates native improvement from an instruction's continuing value. When the old model is unavailable, compare against the stored result and disclose that the old environment was not rerun.

Inspect changed descriptions, skill bodies, hooks, tools and dependencies; a metadata change can affect selection before a skill is loaded. Use the smallest relevant fixture subset. Reassess duplicate procedures and retain personal authority, ownership and voice boundaries. Keep any proposed removal as an exact, separately authorised change.

Every review should end in a recorded disposition: retain, narrow activation, adapt, replace, retire, or insufficient evidence. Update model guidance only for supported model observations; update the package record for package decisions and the deployment evidence after actual changes. A release announcement starts an assessment, not automatic adoption.

## 11. Completion and next action

The implementation is complete when the priority capabilities have a usable, evidenced route on the adopted surfaces; missing coverage is explicit; composition preserves the operating boundaries; selected packages have reproducible identities where possible; and deployment, rollback and re-review instructions are accurate. Completion does not require matching package counts across labs or installing every shortlisted candidate.

**Batch 1 is complete.** The package register contains 24 baseline/candidate/held records tied to source evidence and capability IDs. The composition fixture contains a fixed synthetic source pack and eight test families. Existing matrix, review, deployment, governance and generic framework references have been aligned within the approved file scope.

Verification: internal links and anchors resolve; implementation IDs referenced by the matrix exist; new files are indexed; maintenance references have no runtime skill metadata; generic framework changes contain no personal identifiers. The read-only contract check passed before and after the batch, with all seven generated copies current. A file-hash comparison against the pre-batch working tree confirms all 96 pre-existing files outside the named scope are unchanged, including the dated inventory, constitution, personal voice source and generated contract bodies. These are static checks, not behavioural evaluation.

Next is **Batch 2: actual-client baseline and bounded pilot**. Its open execution details are the accessible target surfaces, exact corpus/output and evidence locations, permissible package/configuration changes, run count and any relevant usage/spending limits. The synthetic fixtures now supply the initial corpus option. No new package has been selected for deployment; no live trial, installation, enablement, commit or publication occurred in Batch 1.
