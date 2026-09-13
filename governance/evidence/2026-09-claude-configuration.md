← [Home](../../README.md) · [Governance](../README.md) · **September 2026 Claude configuration verification**

# September 2026 Claude Configuration Verification

A dated record of configuration inspection and deployment verification. This is evidence, not runtime instruction or behavioural certification. The maintained decision record is the [Claude configuration baseline](../../kit/implementation/platforms/claude/configuration-baseline.md). The [July evaluation baseline](2026-07-baseline.md) remains the separate behavioural evidence reference.

## Scope and method

On 13 September 2026, Claude Desktop for macOS 1.52386.6 was inspected through its settings UI. The review covered every Settings navigation section and the Skills, Connectors and Plugins management surfaces. After explicit approval, 15 optional plugins and 13 standalone skills were disabled. Each switch was checked after saving; my-voice was separately verified enabled. No packages were uninstalled or custom skills deleted.

On-demand tool loading, code execution/file creation, artifacts and inline visualisations were verified retained. Research was off, Web search on and Memory on in the inspected new chat. Chrome connector tools were switched off there; Context7 was already off. Account connections were not revoked. These conversation-specific observations do not establish all future or existing chat selections.

No evaluation prompt was sent to Claude. Token savings, activation behaviour, task quality and persistence across every product surface were not measured.

## Source alignment findings

The source comparison used repository commit **8613657** (Clean public repository narrative). Personal-preference and Cowork version markers differed between the client and source:

| Component | Client marker | Repository marker |
|---|---|---|
| Personal preferences | 2026.07.13 @ 1.5 | 2026.07.25 @ 2.0 |
| Cowork global instructions | 2026.07.13 @ 1.4 | 2026.07.19 @ 1.5 |

These are marker comparisons, not full text-equivalence checks.

### Initial installed my-voice comparison

The enabled skill's Contents view exposed four files. Its current package was downloaded using the client's Download control. Archive contents were compared directly as bytes, with SHA-256 hashes, against the four repository files. File names matched, but **zero of four files were identical**. The installed SKILL.md carried version 2026.07.05 @ 1.2; the source relies on Git history rather than an embedded skill version.

| File | Installed bytes | Source bytes | Difference |
|---|---:|---:|---|
| SKILL.md | 14,321 | 14,964 | Invocation policy, constitution references, model tuning, private-contact handling and version marker. |
| authored-register.md | 2,915 | 2,912 | Updated operating-contract reference and removed version marker. |
| documentation-register.md | 4,023 | 4,047 | Updated operating-contract reference. |
| examples.md | 9,440 | 9,507 | Anonymised scenarios and removed version marker. |

Material distinctions:

- Installed frontmatter declares disable-model-invocation: true; the source declares false. Installed prose says manual-only; source prose permits natural-language execution requests. Both preserve the execution/substance boundary. Consumer-client enforcement of the extension field was not tested.
- The installed files refer to the former 01-about-me / 02-how-we-work names. Source references use the maintained constitution names.
- Installed tuning is stamped 21 June; source tuning is stamped 19 July with an explicitly partial comparison, updated alternative-model guidance and factual-completeness cautions.
- The installed package contains contact details and identifiable examples. The public source substitutes approved-private-source placeholders and anonymised scenarios. Those private contents are not reproduced in this record.

Installed SKILL.md SHA-256: `c49c2fa830eaf3aff1e87c87a9966f2222244f5ee8b8808df456e42fddf7c01e`.

Source SKILL.md SHA-256 at the comparison revision: `57e6e5c853cbbebad11767cdfabe8c38f7c17e6c624bd6eb4ab71123d9e07903`.

At the initial comparison, no replacement had been performed and the enabled skill was an older, divergent deployment. The subsequent authorised replacement is recorded below.

## Subsequent authorised my-voice replacement

Later on 13 September, Andrew explicitly authorised replacement with the repository copy. The four source files were packaged without edits and uploaded through the existing skill's Replace control. Claude confirmed replacement and displayed version v1 as current. The Enable skill switch remained on.

The saved current version was downloaded again. Its four files under skills/my-voice/ were byte-identical to the corresponding repository source, with matching SHA-256 hashes. The client-generated archive also contained .claude-plugin/plugin.json with the skill name and description. The archive container is therefore not byte-identical to the upload, but all four deployed skill files are exact matches.

| File | Verified SHA-256 after replacement |
|---|---|
| SKILL.md | `57e6e5c853cbbebad11767cdfabe8c38f7c17e6c624bd6eb4ab71123d9e07903` |
| authored-register.md | `fca5cc5bbd06c3ba69e2148cb130e93ce3707a6d6b82c9254877c42e1469b479` |
| documentation-register.md | `f338114f02045953a56f2453cf401b9ca2657a20b36af90299a13a064364b6b1` |
| examples.md | `8295c06884a2e4aca38e4040483d7ae75c70c98618730bab1620490c91e8b1de` |

This resolves the my-voice content drift, including the invocation declaration, references, model guidance and public contact handling. It does not resolve personal-preference or Cowork-instruction drift. No behavioural invocation test was run and no source skill files were modified.

## Coverage limits

The original settings inspection did not establish every conditional setup screen: disconnected-connector details were incompletely inspected, the billing Pause subdialog was not reviewed, and steps requiring new uploads, connections or subscriptions were not completed. File-management controls were reviewed without inventorying every uploaded file. Project memory controls were inspected without transcribing all stored memory. These gaps do not invalidate the individually verified disable operations.

Five PDF Viewer-associated items remained visible in the Skills catalogue after its plugin switch was disabled. Catalogue visibility alone does not establish runtime availability; no invocation test was run. The supported claim is that the plugin's Enable switch was verified off.

## Record boundary

Raw account audits, the downloaded package and full comparison diffs remain private working evidence. This record is self-contained about methods, findings and limitations without importing credentials, local paths, contact values, billing details or memory contents. See [ADR-012](../decisions/adr-012-clean-public-baseline.md).
