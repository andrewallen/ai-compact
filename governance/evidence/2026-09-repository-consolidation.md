← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Repository consolidation**

# September 2026 Repository Consolidation

## Authority and scope

Andrew requested the full plan and its implementation following the consolidation review. This authorises the seven identified file removals and the source/documentation changes below. The starting state is `863a1d5` plus the uncommitted voice repair, deployment records and evaluation-cancellation updates from the preceding work. A private snapshot preserves that working state for comparisons; HEAD alone is not the before-state for this batch.

Behavioural evals remain excluded at Andrew's request. This batch changes repository source and its records; it does not deploy the newly revised voice files, commit or publish. Installed versions keep their dated verification evidence, and product baselines must identify any new source drift.

## Implementation plan

| Work | Exact treatment | Acceptance |
|---|---|---|
| Prompt collection | Remove `advisory-synthesis.md`, `analytical-decomposition.md`, `investigative-brief.md`, `multi-perspective-exploration.md`, `structured-critique.md` and `task-decomposition.md` from `kit/implementation/prompts/untested/`. Fold the minimal format from `kit/implementation/prompts/_template.md` into the prompt index, then remove that file. | Discovery interview and the five distinctive experimental prompts remain unchanged. Indexes list only maintained files; no broken references or accidental promotion. The removed generic methods remain covered by the contract. |
| Decision register | Consolidate 44 entries into 12 themes: authority/loading, independent judgement, execution/evidence, voice, knowledge/continuity, derivation/delivery, Cowork safeguards, working-set skills, prompts/methods, model guidance/context, structural decisions and record ownership. | Every prior decision has a retained rationale or an explicit ADR reference. Rejected alternatives and reconsideration conditions survive. Existing inbound anchors resolve. |
| Overview and ownership | Shorten the root overview and prompt guidance. Keep current topology in current architecture, setup/state in product baselines, derivation coverage in contract maintenance, and dated observations in evidence. | Root and folder indexes retain required navigation. Current deployment claims do not compete across guides and evidence. |
| Loading terminology | Clarify the framework's full-core/condensed routes and its maintenance-only philosophy use. Scope the decision register's three-file requirement to the full-core route. | No change to the constitution or loading policy; framework remains generic and independently readable. |
| Voice examples and routing | Separate counter-examples, current illustrative targets and retained source samples. Reconcile current examples with vocabulary, register and finding-first rules. Preserve retained quoted samples verbatim, with applicability notes. Route factual research reports to documentation and owned argument to authored output. | Four-file package and invocation policy retained. Authentic/source quotations are not silently rewritten. Newly changed file hashes are distinguished from installed package hashes. |
| Static fixture repairs | In A1, require a credible alternative hypothesis without inventing its superiority. In G1, load the overlay to test dormancy and retain absence as a separate control. Rename this file's capability fixture identifiers F1–F8 to K1–K8, with an explicit historical mapping; persistence F1–F3 stay unchanged. | No model calls. Capability source data, calculations and quoted prompts remain unchanged. Historical references retain their original meaning. |
| Historical record compression | Condense duplicated completed plans and acceptance lists in the implementation-consolidation and consistency-cleanup records. Clarify that the latter's pending prompt-removal status was historical and is resolved by this batch. | Preserve dates, authority, source revisions, methods, results, hashes, numerical outcomes and limitations. Leave the July results, constitutional clause map and client inspection histories intact. |
| Closing verification | Check navigation, anchors, generated copies, whitespace, allowed version markers, framework anonymisation and the preservation boundaries below. Record results and source/deployment limits here. | No extra repository tooling or test dependency. Failures are resolved before completion; static checks are not described as behavioural evidence. |

## Preservation boundaries

- All twelve ADRs, including superseded ADR-009, remain intact. They retain structural history and rejected alternatives.
- Constitution, philosophy, the steward charter, shared contract bodies, generator and all seven generated bodies remain unchanged.
- Cowork's plan, file and connector safeguards and the documentation register's formal-deliverable checks remain unchanged.
- The five retained experimental prompts and discovery interview remain unchanged. Their presence is not a commitment to test or promote them.
- Dated deployment hashes remain records of the versions actually inspected. New source revisions do not inherit those matches.

## Decision retention

The consolidated register keeps the reasons for explicit authority, independent judgement, neutral partner voice, scoped action, evidence-grounded claims, external memory, shared derivations, portable skill craft and separate product safeguards. It retains the rejection of standalone default-role extraction, per-client skill forks, global deployment files, duplicate package catalogues and speculative promotion of methods. Structural detail points to the existing ADRs instead of being independently retold.

## Result and verification

**Implemented.** Seven files were retired, leaving discovery interview and five experimental prompts. The prompt format now lives in its index. The decision register groups all 44 former entries into 12 themes; a before/after coverage review confirmed each has retained rationale or an ADR reference. The root overview and two historical records are shorter, while current status remains with the product baselines.

Voice examples now distinguish current targets, counter-examples and retained source material. All eight quoted source paragraphs, including the 2014 exemplar, are verbatim. The current documentation example leads with its finding; authored routing distinguishes an owned research-based argument from a neutral factual report. A1, G1 and the K-family identifiers were repaired statically. No fixtures were run or promoted.

Whitespace-delimited counts against the task-start snapshot measure maintained text, not tokens or performance:

| Material | Before | After |
|---|---:|---:|
| Root overview | 1,068 | 822 |
| Decision register | 3,380 | 2,035 |
| Prompt index | 612 | 242 |
| Implementation-consolidation record | 875 | 633 |
| Consistency-cleanup record | 991 | 875 |
| Seven retired files | 1,415 | 0 |
| **Subtotal** | **8,341** | **4,607** |

These areas are 3,734 words shorter (44.8%). Clarifying additions, status updates and this plan/result record are outside that subtotal. Markdown file count falls from 100 to 94: seven removals and one new evidence record.

- Navigation: 509 relative Markdown links and anchors resolve across 94 Markdown files; all 25 folder indexes retain parent and maintained-child links. Embedded versions remain confined to the allowed directories.
- Distribution: all seven generated copies remain current under `sync_contracts.py --check`; the shared sources and generator are unchanged. `git diff --check` passes.
- Preservation: 46 protected files match the task-start snapshot, including every ADR, all constitution and philosophy files, roles, diagrams, Cowork instructions, retained prompts and the historical records named above as intact. Result and verification sections of the two compressed historical records are byte-unchanged. Capability source data, computed checks and quoted prompts are unchanged.
- Skill structure: the portable-field validator passes on a temporary copy excluding only its unsupported `disable-model-invocation` extension. Actual source retains `false`; this qualified check does not prove client invocation.
- Framework: added prose was checked for personal identifiers and local paths and read for independence from personal context.

The consolidated source hashes are `00b97086bc8ed954b43646f4c6ec2a58c4b6450a698f2bf3ba1e8efdd8956d22` for `authored-register.md` and `6ab15886eca7e75e50a7e13a6820bffe9b4de44a56ce9d7e21bccea62499a71b` for `examples.md`. Both differ from the previously verified Claude v3 and local Codex package. The other two voice files retain their verified hashes. Product baselines and the tracker record the source/deployment distinction; no live replacement, commit or publication occurred in this batch.
