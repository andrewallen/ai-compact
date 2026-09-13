← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Consistency cleanup**

# September 2026 Consistency Cleanup

## Plan and scope

Andrew requested a plan and implementation following the repository-wide consistency review. The starting tree was clean at `85ea79f`. This batch repairs implementation references and eval definitions, consolidates maintenance documentation and redraws the existing mode diagram. The constitution, role charter, shared contract bodies, Cowork safeguards and formal-document review requirements remain unchanged. Live deployment and commit/publication are separate actions.

| Work | Acceptance |
|---|---|
| ChatGPT guidance | Distinguish Temporary Chat personalisation choices and make project-level constitution loading explicit, with official sources. |
| Eval and prompt repairs | Use valid Cowork base-plus-addendum configurations, current ChatGPT body markers and an explicit request to develop a selected sketch. |
| Voice reference | Refer to current constitutional audience and structure rules; retain register craft and invocation policy. |
| Capability fixtures and historical evidence | Remove abandoned catalogue identifiers while preserving synthetic inputs; qualify the July record without rewriting its results. |
| Maintenance consolidation | Keep rationale in design decisions, setup in product guides, cross-product routes in the deployment map and detailed results in evidence. |
| Mode diagram | Show exploration, execution and refinement independently of product categories; inspect the rendered SVG. |
| Verification and deployment status | Check links, generated copies, preservation boundaries and source hashes; report the voice-source change separately from installed state. |

Removal of six generic experimental prompts remains pending explicit approval: `advisory-synthesis`, `analytical-decomposition`, `investigative-brief`, `multi-perspective-exploration`, `structured-critique` and `task-decomposition`, all under the [untested prompt index](../../kit/implementation/prompts/untested/README.md). They remain in the tree. Changes to Cowork confirmation or document-review safeguards were not selected for this cleanup.

## Result and verification

The source cleanup is implemented. No files were deleted, renamed or moved. One new evidence record, this file, holds the plan and results together.

- [ChatGPT guidance](../../kit/implementation/platforms/chatgpt/README.md) now distinguishes personalised and non-personalised Temporary Chat, accounts for absent standing instructions in the isolated route, and provides an explicit project-level loading clause. The guide cites the official release notes and Projects documentation checked during the review; this batch did not inspect account controls.
- Persistence fixtures now treat Cowork as a base-plus-addendum composition and grade its narrower confirmation safeguards correctly. Provoke/produce fixtures reference current paste-ready bodies and include the copied variations prompt. A new D5 audience-context case targets the authored-register correction. These are authored test definitions, not executed results.
- The authored register refers to the current constitutional audience and structure rules instead of repeating a superseded inventory. The variations prompt requires an explicit development request after selection. Capability fixtures no longer depend on abandoned catalogue identifiers; their synthetic source pack and quoted task inputs are unchanged.
- The July baseline has a historical-scope notice. Its original record is otherwise unchanged. Current indexes point to the evidence index instead of presenting July results as validation of the latest source.
- The platform index now handles navigation, the deployment map owns cross-product routes, and product guides own setup. Architecture summaries link to the maintained sources. Design decisions retain rationale and rejected alternatives. The framework records the generic lessons about matching eval loading to deployment composition and dating evidence to its tested source.
- The [mode diagram](../diagrams/work-flow-between-modes.svg) now shows exploration, execution and refinement across products, with direct entry for defined tasks and persistent scope boundaries. Its final local rendering was visually inspected for legibility, clipping and visible transitions.

## Maintenance reduction

Whitespace-delimited word counts against `85ea79f`; these measure documentation size, not runtime context or model performance.

| Document | Before | After |
|---|---:|---:|
| Root overview | 1,176 | 1,054 |
| Governance index | 288 | 191 |
| Current architecture | 797 | 677 |
| Design decisions | 4,765 | 3,316 |
| Platform index | 896 | 262 |
| Deployment map | 1,741 | 816 |
| **Total** | **9,663** | **6,316** |

The six maintained documents are 3,347 words shorter (34.6%). Corrections, fixture additions and this evidence record are outside that subtotal.

## Verification

- `python3 kit/implementation/platforms/sync_contracts.py --check`: all seven generated copies current.
- `git diff --check`: passed.
- Repository navigation: all internal Markdown links and anchors resolved across 99 Markdown files; all 25 folder indexes link their maintained children and parent. No orphan Markdown documents or embedded version markers outside the allowed directories.
- All four SVGs parsed. The changed mode diagram rendered locally with ImageMagick and an explicit local font map; its final image was inspected. Unchanged diagrams were not newly visually reviewed.
- Preservation comparison: constitution, philosophy, roles, shared contract bodies, distribution code, contract-maintenance definitions, Cowork files, skill entrypoint, documentation register, examples and ADRs are byte-unchanged. July evidence differs only by its historical notice. Capability source data, calculations and quoted task inputs match the starting tree.
- Framework anonymisation check passed. No personal names, employer/role identifiers or local checkout paths were introduced.
- The generic skill validator rejects the existing `disable-model-invocation` client extension. The unchanged YAML parses with that value set to `false`. A temporary copy omitting only that field passes the portable-field validator; the repository field was preserved. This is a validator compatibility limit, not an unqualified package-validation pass.

Checks used temporary local scripts and render files; no new repository tooling or dependency was added.

## Deployment and behavioural limits

Comparing the current voice package with the SHA-256 values in the [Claude deployment record](2026-09-claude-deployment.md) confirms three unchanged files. `authored-register.md` now has SHA-256 `78a435ed5f5306ea2b8456a567006e16812e30de04148a79f44ff3352d18f77d` and differs from that recorded package. The [Claude baseline](../../kit/implementation/platforms/claude/configuration-baseline.md) and skills tracker mark the correction as awaiting deployment. The historical deployment hashes were preserved.

No fresh application inspection, live deployment, commit or publication was performed. No fresh-session behavioural probes were run, so the authored-register and prompt repairs remain behaviourally unverified; no improvement or cross-model parity is claimed. The earlier September exception applies only to its named batch and is not treated as a new exception here. Targeted before/after runs of D5 and the reusable C4/C5 variant remain the relevant behavioural follow-up.

