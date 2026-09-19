← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Voice maintenance**

# September 2026 Voice Maintenance

## Scope and result

On 19 September, Andrew requested the first three follow-ups from the repository review: establish current behavioural evidence, resolve Claude and local Codex voice deployment drift, and remove the voice package's implicit dependence on repository access. The starting tree was clean at `863a1d5`.

The package repair and both deployments are complete. **Andrew declined behavioural evaluation for this batch** and requested a static consolidation review instead. The proposed 108-response comparison never ran and is no longer awaiting approval. Connectivity smoke checks do not constitute behavioural evidence. The July baseline and later source-review records retain their original claim boundaries.

**Subsequent source changes.** The later [repository consolidation](2026-09-repository-consolidation.md) revises `authored-register.md` and `examples.md`. The deployment results below identify the loading-repair revision, not those later source edits. Product baselines own the resulting deployment gaps.

This batch does not change the constitution, shared contract bodies, skill examples, other eval rubrics, provider package selections or account permissions. No repository files were deleted, renamed or moved. No commit or publication was performed.

## Package repair

The four-file [my-voice package](../../kit/implementation/skills/my-voice/SKILL.md) now declares its loading contract: use the full core or a supplied condensed chat/execution body. A constitution path identifies the policy source and does not imply repository access. The full core governs when actually supplied.

The entry point carries a bounded derivation of the constitution's audience, form, ownership and completeness rules. The authored and documentation registers link to it locally. This supplies the guidance needed with either condensed base without adding a fifth file or moving canonical policy out of the constitution. The existing natural-language invocation setting, examples and register craft are preserved.

[Contract maintenance](../../kit/implementation/platforms/contract-maintenance.md) records the supported composition. The [framework](../../framework/layer-model.md#capability-package-and-runtime) records the generic package-dependency lesson, and [design decisions](../design-decisions.md#voice-craft-lives-in-a-skill-durable-principles-stay-portable) records the implementation rationale. D5 now defines explicit standalone-package variants without repository access.

## Verified deployments

| Destination | Before | Action and verified state |
|---|---|---|
| Claude app | Enabled my-voice v2. A fresh download matched the historical package, including the superseded authored-register wording. | Replaced the existing skill with the repaired four-file archive. Refreshed the app, confirmed **v3 current and enabled**, downloaded that version and compared all four file contents byte for byte with source. |
| Local Codex personal skill | All four installed files differed from source. | Preserved the existing four files, replaced those exact files and compared all four resulting contents byte for byte with source. No provider-managed package was changed. |

At deployment, the source, downloaded Claude v3 and local Codex files had these SHA-256 values:

| File | SHA-256 |
|---|---|
| `SKILL.md` | `00dc812363de5ad81f48b1fcca08e50ca69593b6ee4b43eac547c044d31f5a44` |
| `authored-register.md` | `97f9b8b72961b3e473fd1e0e9b2aa85e2ad90c6f4a9a74254bc266b82503d961` |
| `documentation-register.md` | `4e3a279d8febbc2812f772ac391ba13b15b9c7d2cccbe272660ffa166ae63ecc` |
| `examples.md` | `8295c06884a2e4aca38e4040483d7ae75c70c98618730bab1620490c91e8b1de` |

Restoration copies and comparison manifests are held in the private temporary working directory for this task, outside the public repository. The Claude v2 archive can be re-uploaded through Replace; the previous Codex files can be copied back to the same four destinations. The source revisions remain recoverable through Git. Temporary backups are not a durable archive.

Saved package identity is verified; fresh-session discovery, invocation and output quality are not. Existing sessions may retain previously loaded material. Claude General preferences and Cowork instructions were not changed or freshly verified. Separate Claude Code, Codex IDE/cloud and ChatGPT deployments remain separate targets.

## Behavioural evidence boundary

The declined comparison would have covered C2, H1, capability F5 (now K5), D5 and the reusable C4/C5 sequence on two models. Its unexecuted runner and input manifest remain private working material, not maintained repository assets or results. No model-quality improvement, invocation success or cross-product parity is claimed. The general evaluation policy remains in place; Andrew's exclusion is specific to this work.

## Static verification

- All seven generated contract copies remain current under `sync_contracts.py --check`.
- Source links and anchors, folder-index navigation, allowed version-marker placement and whitespace were checked after the documentation updates.
- The generic skill validator does not accept the existing `disable-model-invocation` client extension. A temporary copy omitting only that field passes; the actual source and both deployments preserve `false`. This is a qualified structural check, not proof of invocation or behaviour.
- Framework additions contain no personal names, employer identifiers or local paths.

Fresh behaviour and invocation remain unverified; no evaluation is scheduled by this record. The subsequent consolidation review corrected the Codex guide's stale drift statement by referring current deployment status to its configuration baseline.
