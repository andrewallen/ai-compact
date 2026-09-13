← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Skills](README.md) · **Package register**

# Capability Package Register

> **Historical — superseded on 13 September 2026.** The [selected catalogue](README.md) now owns current choices; the [Claude](../platforms/claude/configuration-baseline.md) and [Codex](../platforms/codex/configuration-baseline.md) baselines own configuration. The original record below is retained as research history, including its former ownership, shortlist and trial assumptions. It is no longer an active register or a deployment instruction.

Maintenance reference established in Batch 1 on 13 September 2026. It records baseline and candidate implementations for the [capability matrix](capability-matrix.md). It is not a runtime router, installer manifest or adoption decision. The dated [first-party inventory](first-party-inventory.md) supplies provenance and revision evidence; observations below inherit that date and its limitations. No package trial or fresh account inspection was performed when creating this register.

## Record conventions

An implementation ID identifies one reviewed-source or observed-runtime record. Keep public and installed variants distinct even when their names match. A materially changed revision receives a new record linked to its predecessor; IDs are not recycled. Capabilities may reference several implementations, and one implementation may cover several capabilities.

Selection disposition is independent of observed state. Use **baseline reference**, **candidate**, **held**, **trialled**, **selected**, **rejected** or **retired** for disposition. Record **cached**, **installed**, **enabled**, **exposed**, **loaded** and **successfully exercised** individually with dates and evidence links. Unknown is not false. A selected provider is not automatically deployed.

Source IDs resolve in the [source register](source-register.md). Public revision pins are inherited through S01/S02/S12 and the inventory; runtime versions below are dated observations, not update instructions. A package-publisher attribution does not certify every component's authorship or licence.

## Baseline references

| ID | Capabilities | Implementation and identity | Entry points / components | Observation and disposition |
|---|---|---|---|---|
| P01 | C01-C11, C13 | Native model/host capability plus applicable existing contract; vendor package identity may be opaque. | Native conversation, retrieval and editing tools as actually supplied; no additional thinking skill. | Baseline reference. Exact model/effort, native revisions and tool set must be captured per trial. Historical settings are in the matrix; behaviour and usage unmeasured. |
| P02 | C12-C13 | Personal `my-voice`, S11; canonical source is the four files in [my-voice](my-voice/SKILL.md). | SKILL.md, authored-register.md, documentation-register.md, examples.md; client-specific discovery. | Baseline reference. Claude v2 enabled/source parity is historical deployment evidence; Codex exposure was recorded, parity unknown. No fresh invocation test. Source revision/hash must be captured at trial; do not infer from the label v2. |
| P03 | C06-C07 | OpenAI Presentations runtime, S13, observed 26.909.12148. | `presentations`; format-generation and rendering tools/dependencies require package inspection. | Baseline reference. Exposed in the inventory session; installed parity, successful exercise and ChatGPT availability unknown. |
| P04 | C09-C10 | OpenAI Documents runtime, S13, observed 26.909.12148. | `documents`; document generation, rendering and optional service dependencies require inspection. | Baseline reference. Session exposure recorded; task quality and source parity untested. |
| P05 | C10 | OpenAI PDF runtime, S13, observed 26.909.12148. | `pdf`; rendering/extraction/generation tools require inspection. | Baseline reference. Session exposure recorded; task quality and source parity untested. |
| P06 | C04 | OpenAI Spreadsheets runtime, S13, observed 26.909.12148. | `spreadsheets`, `excel-live-control`; file and live-app routes have different tool/access requirements. | Baseline reference. Both entry points exposed in inventory session; live-session access is not established. |
| P07 | C11 | OpenAI visualize, S13, observed 1.0.37. | `visualize`; client rendering/runtime contracts require inspection. | Baseline reference. Session exposure recorded; durable export and output quality untested. |
| P08 | C05, C08 | OpenAI Sites, S13, observed 0.1.66. | `sites-building`, `sites-hosting`; build and publication paths must be assessed together. | Baseline reference. Session exposure recorded; deployment dependencies and publication authority not established. No publication is authorised by listing it. |

## Initial first-party candidates

These entries identify the source to inspect and the intended comparison. They do not establish that every contained workflow should activate. Conditional craft stages may complement the primary workflow; two competing task directors need explicit resolution.

| ID | Capabilities | Publisher, source and revision | Intended entry points / package scope | Disposition and unresolved dependency |
|---|---|---|---|---|
| P09 | C05 | Anthropic `frontend-design`, S01 pinned source. | Standalone `frontend-design`; inventory also records a separate Claude Code plugin distribution, whose parity is not assumed. | Candidate after native web baseline. Review exact package, licence and tools before portability claims. |
| P10 | C05, C13 | Anthropic Design, S02 pinned source, 1.2.0. | `design-critique`, `accessibility-review`, `design-system`, `design-handoff`, `ux-copy`; research paths only for matching work. | Candidate. Complete plugin components and integrations not reviewed here; historical Claude optional-plugin baseline is disabled. |
| P11 | C05 | OpenAI Product Design, S13 observed runtime 0.1.55. | Selected index/audit/ideate/image-to-code/url-to-code entry points exposed in inventory session; inspect complete ten-file package and tools. | Candidate for measured comparison, already exposed historically. Public S12 version 0.1.52 is a separate source reference, not a parity claim. |
| P12 | C04, C06-C10 | Anthropic document skills, S01 pinned source. | `pptx`, `docx`, `pdf`, `xlsx` bundled as document-skills; assess only required format paths and dependencies. | Candidate only for a demonstrated native gap. Source-available terms and scripts need review. Public source is not proof of Claude's native implementation. |
| P13 | C09, C13 | Anthropic `doc-coauthoring`, S01 pinned source. | Coauthoring methodology and any referenced supporting files. | Candidate for matching documentation tasks; general editorial/AI-slop performance unproven. |
| P14 | C06, C09 | Anthropic `theme-factory` and `canvas-design`, S01 pinned source. | Separate craft candidates, to be instantiated as individual trial records if shortlisted. | Held until a design gap appears; no combined activation proposed. Fonts, assets and terms require inspection. |
| P15 | C02-C03 | Anthropic Enterprise Search, S02 pinned source, 1.3.0. | `knowledge-synthesis`, `search-strategy`, `source-management`; inspect retrieval/connector paths. | Candidate. Historical Claude plugin baseline disabled. Source access and synthesis method must be tested separately. |
| P16 | C02-C03 | OpenAI Deep Research, S13 observed 0.1.15. | `deep-research`; explicit deep-research activation boundary, retrieval and artifact tools require review. | Candidate. Session exposure recorded; no deep-research run performed. Ordinary synthesis is not automatic authority to invoke it. |
| P17 | C04, C11 | Anthropic Data, S02 pinned source, 1.1.0. | Relevant analysis/validation/visualisation paths from the inventory. | Candidate. Historical Claude baseline disabled; complete package/dependencies unreviewed. |
| P18 | C04, C11 | OpenAI Data, S13 observed runtime 1.0.8. | Relevant exposed analysis/validation/visualisation routes; 20 cached files include additional paths. | Baseline reference for native data work and candidate for focused comparisons. Public S12 0.2.8 is a different version/layout. Publication and context-persistence paths require inspection. |
| P19 | C11 | OpenAI build-web-data-visualization, S12 pinned source, 0.1.21. | Select a required medium/method from the 18 source skills; inspect full reachable execution path. | Held until native visual output shows a gap. Local installation/exposure unknown; public Codex listing is not ChatGPT availability. |
| P20 | C06, C09 | OpenAI template-creator, S13 observed 26.909.12148. | `template-creator`; creates personal artifact-template skills from accepted references. | Candidate after reference acceptance. Session exposure recorded; persistent output targets need scoped authority. |
| P21 | C06, C09, C11 | OpenAI Creative Production, S12/S13 observed 0.1.25. | `intake`, `produce`; referenced creative tools and all side effects require review. | Candidate for a matching craft gap. Session exposure recorded; public/local version agreement does not establish file parity. |
| P22 | C15 | Anthropic `skill-creator`, S01 pinned source. | Authoring and comparison workflow; scripts, reference files and client assumptions require review. | Candidate for maintenance use only. No evaluation toolchain installed by this record. |
| P23 | C15 | OpenAI `skill-creator`, system skill exposed in inventory session. | Native authoring entry point; exact source revision/dependencies not captured. | Baseline reference for maintenance. Record full package at actual use; no portability or performance claim. |
| P24 | C15 | OpenAI plugin-eval, S12 pinned source, 0.1.2. | `evaluate-plugin`, `evaluate-skill`, `improve-skill`, `metric-pack-designer`, `plugin-eval`; static and live paths distinct. | Candidate for maintenance. CLI/runtime dependencies, installation and usage limits need review before execution. Static budget estimates do not establish token savings. |

P14 is a held discovery grouping, not an executable trial identity. Split its two sources into separate pinned records before any comparison. The same rule applies to any format or subworkflow whose revision, deployment or disposition diverges from its parent record.

## Admission record to complete before a live trial

For each selected candidate, expand its row into a bounded record with these fields. Until completed, all rows above remain reference material rather than deployment-ready packages.

| Field | Required evidence |
|---|---|
| Identity and gap | Implementation ID, capability IDs, exact publisher/component attribution, intended gap and baseline. |
| Revision and scope | Repository commit or native version/hash where accessible; complete reachable files and components reviewed; licence and derivative status. |
| Execution and access | Tools, scripts, hooks, agents, commands, apps/MCP, templates, authentication and permissions; all persistence/publication effects. Keep credentials and private trusted paths out of this register. |
| Target composition | Actual client/mode/version, model/effort, applicable contract, scope, invocation, complementary stages and overlapping installed workflows. |
| Constitutional review | Exact instruction/component location, boundary affected, supported finding, adaptation or exclusion; host limits stated. |
| Observed state | Separate dated cache/install/enable/exposure/loading/exercise observations with evidence. |
| Trial authority and results | Approved output targets, corpus, run/spend limits where relevant; outcome, corrections, elapsed time and reported usage; unknown metrics marked. |
| Disposition and maintenance | Reference/candidate/trialled/selected/etc.; adoption evidence; next meaningful review trigger; previous working configuration, rollback action and limitations. |

## Composition, fallback and maintenance

Use the [review method](review-method.md) and [composition probes](../../evals/capability-composition-probes.md). Keep model and host fixed while estimating a candidate's marginal benefit. Prefer the native baseline if the candidate adds no useful benefit; record that decision and its evidence. A native-only result is a valid selection.

Runtime/version changes, modified descriptions/tools/hooks, repeated friction or a new recurring task trigger a scoped review. No automatic updates or scheduled monitoring follow from this register. Exact previous settings and revisions must be captured before deployment; do not promise restoration of vendor-managed model/runtime versions. Optional additions may be disabled only within an authorised rollback scope. Preserve source history and unrelated work.

No initial record has a local comparative score, measured token saving, selected deployment or approved rollback action. Batches 2 and 3 of the [implementation plan](implementation-plan.md) establish those when their execution scope is defined.
