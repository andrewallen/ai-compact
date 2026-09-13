← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Platforms](../README.md) · [Claude](README.md) · **Configuration baseline**

# Claude Configuration Baseline

The adopted target configuration for Claude and the last verified deployment. The [skills catalogue](../../skills/README.md) owns capability selections; this guide owns their delivery. This is a maintenance reference, not standing instructions. Instruction sources remain in their existing files; product controls enforce access and permissions.

## Status and scope

**Target adopted on 13 September 2026; current Customize lists reconciled to screenshots supplied that day.** The provider-native selection below supersedes the earlier evaluation shortlist. This repository batch changed no client settings and establishes no measured quality improvement or token saving.

**Latest configuration evidence:** the [Customize snapshot](../../../../governance/evidence/2026-09-claude-customize-snapshot.md) records seven listed plugins and 39 Skills-page entries in the initial views, followed by Obsidian 1.0.1 enabled with six skills. Across those views, all eight selected plugins are evidenced, with 45 entries in aggregate; this is not a refreshed single-list count. Two connectors are connected, five added marketplaces are shown, and six Anthropic sources are marked Added. The earlier direct inspection used Claude Desktop for macOS 1.52386.6; the new screenshots do not expose the client version. Neither establishes separate Code, CLI, mobile or Codex state.

## Current screenshot-backed configuration

Andrew's five screenshots supersede conflicting earlier observations and interpretations of addition reports. The [dated snapshot](../../../../governance/evidence/2026-09-claude-customize-snapshot.md) contains the exact displayed skill names, sources and abbreviated synced commits. List presence is recorded separately from enable-switch or runtime verification.

| Component | Current recorded state |
|---|---|
| Data, Design, PDF Viewer | Present under Plugins → Yours, with 10, 7 and 5 entries respectively on the Skills page. PDF Viewer On also remains user-reported. |
| I have adhd, Taste skill, Impeccable, Frontend design | Present under Plugins → Yours, with 1, 13, 1 and 1 Skills-page entries respectively. Their source marketplaces are shown and synced. |
| my-voice | The sole Created by you entry. The screenshot does not replace the earlier v2 package-parity verification. |
| Obsidian | Follow-up screenshot confirms plugin version 1.0.1 from obsidian-skills, enabled, with all six skills displayed. This closes the initial marketplace-only gap. |
| Claude in Chrome; GitHub Integration | Both connected in Connectors → Yours → All. Per-chat tool selection and permissions are separate and not shown. |
| Context7 | Absent from the connector list, consistent with the earlier user-reported deletion. |
| Added marketplaces | claude-plugins-official, impeccable, taste-skill, i-have-adhd, obsidian-skills. Five entries; automatic update controls are not shown. |
| Anthropic sources | Knowledge Work, Life Sciences, Financial Services, Legal, Claude Tag and Healthcare all marked Added in the separate source picker. This does not enable every plugin they contain. |

All eight selected plugins are evidenced across the initial screenshots and the Obsidian follow-up. Obsidian's enable switch is explicitly On; the other seven remain list observations, with PDF Viewer On also user-reported. Native controls retain their earlier recorded state because they are outside these screenshots. Removing an added marketplace also uninstalls its plugins, according to the displayed dialog.

## Target capability configuration

| Capability | Target | Delivery and scope |
|---|---|---|
| Documents, spreadsheets, presentations and PDFs | On | Retain native Chat/Cowork file workflows through Code execution and file creation. Do not add duplicate document skills where native support is supplied. |
| Web search and source analysis; artifacts and inline visualisation | On | Keep available when relevant. Research mode remains a deliberate choice for substantial research. |
| Data; Design; frontend-design | On | Enable each selected plugin as a whole through a provider-managed route. All included skills become available. An unavailable managed plugin remains undeployed. |
| PDF Viewer | On | Retain the plugin alongside native PDF file workflows. Catalogue presence is screenshot-backed; On is also user-reported. |
| Other optional provider packages | Off for ordinary thinking/output work | Follow the catalogue's explicit off list. Operations and Productivity are no longer early evaluation candidates. |
| Impeccable | On | Selected third-party design addition from the `pbakaus/impeccable` marketplace. Catalogue presence is screenshot-backed above; assess the whole plugin and its overlap with the retained provider design capabilities. |
| i-have-adhd | On | Selected third-party interaction-formatting addition from `ayghri/i-have-adhd`. Its single skill emphasises concise, action-first output. Catalogue presence is screenshot-backed above; the constitution and authored voice retain their authority. |
| Taste Skill | On | Selected third-party design collection from `Leonxlnx/taste-skill`. Catalogue presence is screenshot-backed above; assess the whole plugin and overlap with Impeccable and the provider design capabilities. |
| Obsidian | On | Selected third-party knowledge-work plugin from `kepano/obsidian-skills`. All included skills are available when enabled; local CLI and vault operations require supported host access. The follow-up screenshot confirms version 1.0.1 enabled with all six skills. |
| Authored and other independent third-party skills | Preserve / assess separately | Preserve the existing my-voice deployment. Other third-party candidates remain unselected. |

### Chat and Cowork controls

For native files, retain **Code execution and file creation**. Anthropic documents built-in Word, Excel, PowerPoint and PDF skills under that capability in its [skill guidance](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Public `document-skills` is a separate distribution route, not an additional Chat requirement.

Use **Customize → Skills or Plugins → + → Browse** to find the selected entry where the directory is available. Check the publisher and included skills against upstream before using the client's enable/disable controls. Anthropic's [directory guidance](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory) describes availability in Chat and Cowork; account and surface support must still be verified.

Claude plugin controls are binary. An enabled plugin makes all its skills available; a disabled plugin is not available to select in chat. There is no per-skill switch within a plugin or task-only state. Keep selected useful plugins enabled rather than requiring a settings change around every job. Invocation and loading remain separate from availability; evaluate unwanted activation through use.

Use provider-managed directory or marketplace entries and verify their update controls. Do not manually upload provider skills. The dedicated frontend-design plugin and its source `claude-plugins-official` are visible in the screenshots, resolving the earlier managed-delivery gap. Assess the complete Data and Design bundles, even where particular skills motivate selection.

### Claude Code is a separate target

Follow the [Code guide](code/README.md) for Code-specific delivery and invocation. Use Anthropic's public `document-skills` only where that environment needs the file workflows. Chat/Cowork settings do not establish Code availability, plugin scope or behaviour. The current Code deployment remains unverified by this provider batch.

## Last verified capability configuration

The following observations are retained from the earlier inspection. The current screenshot-backed configuration above supersedes conflicting entries. These historical observations do not establish the complete current setup.

| Setting | Baseline | Scope and rationale |
|---|---|---|
| Optional plugins | Disabled in the earlier inspection | Superseded for PDF Viewer by the user-reported On state above. Data and Design now have On targets; Frontend Design is reported installed. |
| Standalone skills | my-voice enabled; other 13 disabled | Retain the personal output capability. The later deployment saved my-voice v2 and verified all four files against current source. See deployment alignment below. |
| Tool access mode | Load tools when needed | Verified new-conversation setting; not proof of exact tool-schema loading or token savings. |
| Connector search | Off | Keep discovery of additional connectors out of the initial baseline. |
| Cloud code execution and file creation | On | Retain document, spreadsheet, presentation and analysis capabilities. |
| Artifacts, AI-powered artifacts, inline visualisations | On | Retain useful output capabilities. |
| Memory | Existing enabled configuration retained | Product-managed continuity; memory contents remain outside the kit. |
| Personal and Cowork instructions | Updated in the later instruction deployment | Shared chat body and Cowork addendum saved and read back exactly; see deployment alignment below. |
| Research | Off for ordinary baseline work | Enable deliberately for substantial research. |
| Web search | Available when relevant | On in the inspected new chat; select according to freshness and source-verification needs. |
| Optional connector tools | Earlier chat observation | Chrome tools were off in the inspected new chat only. Context7 has since been reported deleted. |

### Earlier disabled plugins — not the current target

Engineering; Enterprise Search; Sales; Finance; Data; Legal; Marketing; Customer Support; Product Management; Operations; Human Resources; Design; Productivity; Bio research.

### Earlier disabled standalone skills — not a current inventory

influence-psychology; import-memory; morning; theme-factory; slack-gif-creator; mcp-builder; internal-comms; canvas-design; brand-guidelines; web-artifacts-builder; algorithmic-art; skill-creator.

The earlier inspection uninstalled no plugin and deleted no custom skill. Its full historical lists remain in the dated verification record. Disabled vendor skills may disappear from the personal list; re-enablement can require finding them in the directory. Package presence, enabled state, discovery and actual execution are separate observations.

## Instruction and skill deployment alignment

| Component | Maintained source | Verified deployed state on 13 September | Alignment |
|---|---|---|---|
| Personal preferences | [personal-preferences.md](personal-preferences.md), 2026.09.13 @ 2.2 | Shared chat body saved in the later deployment pass | Exact 4,930-character readback matched; generation metadata excluded. |
| Cowork global instructions | [global-instructions.md](cowork/global-instructions.md), 2026.09.13 @ 1.7 | 2026.09.13 @ 1.7 | Saved and reopened; exact 2,469-character readback matched. |
| my-voice | [source skill](../../skills/my-voice/SKILL.md); September source revision | Replaced from repository on 13 September; client version v2, enabled | Current v2 downloaded; all four packaged files matched the current source byte for byte. |

The intended source skill permits model invocation for relevant natural-language execution requests and retains the execution/substance boundary. The previous installed version declared manual-only invocation. The earlier replacement matched source revision 8613657. The later v2 replacement includes subsequent source edits and retains disable-model-invocation: false. Whether the consumer client honours that extension field was not tested. An enabled UI switch does not prove source parity or invocation behaviour.

Keep enabled availability distinct from loading: an installed, enabled skill can be discoverable without all its instructions and references being loaded in every conversation. This is a client-specific mechanism, not a guarantee enforced by the kit. Do not load this baseline or governance evidence as runtime instructions.

The [constitution alignment review](../../../../governance/evidence/2026-09-constitution-alignment.md) records the subsequent source edits and static-review findings. The earlier dated inspection remains unchanged evidence of what was deployed at that time. No new preference, Cowork instruction or skill deployment occurred in the alignment or subsequent consolidation batch. The later [deployment pass](../../../../governance/evidence/2026-09-claude-deployment.md) saved both instruction surfaces. The client states that general instructions apply across chats and Cowork; runtime adherence remains untested. After specific transmission approval, the my-voice replacement was saved as v2 and its downloaded files matched current source. The first post-save view still selected v1; a fresh view and Desktop refresh resolved the version discrepancy.

## Evaluation and maintenance

1. Inspect the actual target controls and prepare the exact difference from the catalogue's adopted target, preserving unrelated settings, connections and permissions.
2. After an authorised live change, start fresh on each affected surface. Verify saved state and availability, a representative output and an exploratory request where optional workflows should stay inactive.
3. Verify a relevant task for each optional package activated. Compare native and added workflows only when quality, overhead or interference is uncertain; follow the [review method](../../skills/review-method.md).
4. When deploying an inspectable source package, check its identity and files against the selected revision. Record unavailable native internals and unresolved source parity explicitly.
5. Update this baseline and one dated deployment record with observed settings and tested behaviour. Record each whole plugin as enabled, disabled or not deployed, separately from its intended target. Retain a restoration route for changed settings.

The [implementation plan](../../skills/implementation-plan.md) defines the remaining live batch. No new skill evaluation, source replacement or reactivation is implied by this guide.

## Open decisions — not implemented

- Review duplicated standing instructions without changing the operating contract by implication.
- Consider selected working folders in place of broad drive access; actual paths and grants remain private and tool-side.
- Consider package-manager-only code-execution network access; All domains was observed and retained.
- Review Claude Code sandboxing and bypass-mode availability. Sandbox off and bypass availability on were observed in Desktop; availability does not prove a session is using bypass mode.
- Evaluate model/effort choices by task. Fable 5.1 Medium was observed; it is not a cross-surface or permanent model prescription.

## Boundaries and source guidance

Do not copy account identifiers, credentials, billing records, active-session inventories, exact trusted paths or memory contents into this public baseline. Record portable choices and verification limits. Raw audit material stays outside the repository under [ADR-012](../../../../governance/decisions/adr-012-clean-public-baseline.md).

Vendor guidance consulted on 13 September 2026: [skills and enablement](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [skill loading architecture](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [usage guidance](https://support.claude.com/en/articles/9797557-usage-limit-best-practices). The small enabled catalogue is a personal evaluation decision, not a vendor requirement. No measured token-saving claim is made.

Version: 2026.09.13 @ 1.14
