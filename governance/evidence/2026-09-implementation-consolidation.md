← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Implementation consolidation**

# September 2026 Implementation Consolidation

## Plan and authority

Andrew requested a plan followed by implementation of the duplication and alignment findings. This batch covers implementation sources, their distribution mechanism and the documentation that describes them. It preserves the constitution, role charter, authored voice examples, historical evidence and live product configuration. No files are deleted, renamed or moved. Behavioural testing remains excluded from this workstream; static source and generator checks are included.

The approved plan established two reviewed condensed sources, a coverage map and deterministic distribution to seven detached copies. Acceptance required read-only drift detection, preflight validation, wrapper preservation and repeatable writes. The execution derivation had to restore the identified policy omissions; Cowork had to declare its base while preserving its additional safeguards. Voice maintenance history moved out of runtime text. Navigation, source preservation and static generator checks completed the batch; the results and verification below record their outcomes.

## Result

**Implemented.** The two authored derivations now distribute into seven existing detached files through `sync_contracts.py`. Product wrappers remain manually maintained. This is an implementation mechanism within the existing layer model, not a new policy layer; no structural ADR was needed.

- Added [chat contract](../../kit/implementation/platforms/chat-contract.md), [contract maintenance and coverage](../../kit/implementation/platforms/contract-maintenance.md), and the [distribution script](../../kit/implementation/platforms/sync_contracts.py).
- Restored the identified execution requirements: no praise/opening validation, semantic-change signalling, data/instruction separation and analytical quality. Added the data/instruction boundary to the chat derivation as well. Coverage limits are explicit; neither condensed body claims full constitutional equivalence.
- Reduced Cowork to its additional safeguards and declared its required base context in the addendum, project template and deployment guidance. No reliance on unverified profile-preference inheritance remains in that loading path.
- Removed model-maintenance history from the runtime voice skill, renamed its craft section, preserved invocation metadata, and aligned the documentation audience rule with the constitution. The skill's authored register and examples were unchanged.
- Updated platform navigation, configuration records, deployment documentation, framework lessons and current architecture. Earlier evidence records were preserved; this record supersedes their manually maintained-copy account for current implementation.

## Verification

The generator passed functional checks in an isolated copy: read-only drift detection, exact regeneration, wrapper preservation, no-op second write, malformed-target preflight with no partial changes, and source-budget preflight. A final `--check` on the real repository reported all seven copies current. Its guarantee is exact distribution of reviewed text, not semantic derivation or model adherence.

Static checks found no broken relative links or unresolved heading anchors across 96 Markdown files. `git diff --check` passed. All task-start files remain present; the 23 protected files (constitution directory, role charter, evals, earlier evidence and voice references) are byte-identical to this consolidation's starting snapshot. Framework inspection found no personal identifiers or account paths. No version markers were introduced outside constitution/platform files.

The chat body is 673 words / 4,930 characters; execution is 581 words / 4,321 characters. Generated metadata reports the source version and character count. The chat budget remains 5,000 characters as a repository constraint derived from historical observation; current product UI limits were not checked.

The generic skill validator rejected the retained `disable-model-invocation` extension because it accepts only portable fields. The actual frontmatter is unchanged. Validation of the portable fields in an isolated copy passed after excluding that client extension; this does not establish client invocation behaviour.

## Limits and maintenance responsibility

No behavioural probes, independent model review, live deployment, commit or publication occurred in this consolidation. Existing behavioural-test exclusions remain specific to this workstream.

Future constitutional changes still require editorial review of the two derivations and their coverage map. The distribution command removes copy maintenance, not that judgement. Product-specific wrapper changes remain manual. For sustained full-context sessions, avoid adding redundant derived bodies; existing standing preferences may coexist under the declared host-bound precedence. Cowork must receive its base and addendum together before use.
