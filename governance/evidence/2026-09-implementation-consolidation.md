← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Implementation consolidation**

# September 2026 Implementation Consolidation

## Plan and authority

Andrew requested a plan followed by implementation of the duplication and alignment findings. This batch covers implementation sources, their distribution mechanism and the documentation that describes them. It preserves the constitution, role charter, authored voice examples, historical evidence and live product configuration. No files are deleted, renamed or moved. Behavioural testing remains excluded from this workstream; static source and generator checks are included.

1. **Canonical derivations.** Add a shared chat-contract source alongside the execution contract. Keep constitution-to-derivation work a reviewed editorial process. Add a coverage map distinguishing preserved, compressed and deliberately omitted material. Restore the identified execution omissions and the data/instruction boundary in both derivations.
2. **Deterministic distribution.** Add a dependency-free maintenance script with explicit write and read-only check modes. Update only marked blocks in the three chat files and four agent guides; preserve product wrappers. Detect malformed markers before writing, report drift, track source version and chat length, and enforce the repository's historical 5,000-character chat budget without claiming a current product limit.
3. **Implementation additions.** Make Cowork a declared addendum requiring supplied shared operating context. Preserve plan confirmation, no overwrites, exact deletion approval, folder scope, connector previews and output defaults. Remove duplicate general policy and identify the base context in its project template. Remove obsolete source attribution and maintenance history from the voice skill without changing invocation or registers.
4. **Documentation and verification.** Update navigation, deployment instructions, framework lessons and architecture accounts. Record the intended loading combinations and distinguish authored sources from generated copies. Check generation, idempotence, drift detection, malformed-input handling, wrapper preservation, relative links and source preservation. Review the source coverage and Cowork safeguards statically; do not claim behavioural or deployed parity.

## Acceptance criteria

- Exactly two maintained condensed policy sources; all seven detached policy copies generated from them.
- A read-only command detects edited or stale output blocks, including metadata; the write command makes only in-scope marked changes and reports them.
- The execution derivation explicitly retains anti-validation, semantic-change signalling, data/instruction separation and the analytical quality bar.
- Cowork's shared-context dependency is explicit in runtime instructions, setup guidance and its project template; its additional safeguards remain intact.
- Maintenance history is outside runtime skill text; coverage omissions and composition rules are documented.
- Constitution files, role charter, existing behavioural fixtures and earlier evidence are unchanged by this consolidation.

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
