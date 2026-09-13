← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Platforms](../README.md) · [Claude](README.md) · **Configuration baseline**

# Claude Configuration Baseline

The adopted personal configuration for Claude. This is a maintenance reference, not standing instructions to load into conversations. Instruction sources remain in their existing files; product controls enforce access and permissions.

## Status and scope

Adopted and implemented on 13 September 2026 in Claude Desktop for macOS, version 1.52386.6. The baseline establishes a small optional capability catalogue for subsequent evaluation. It does not establish an optimal token budget or measured improvement in output quality.

Keep three states distinct: **adopted** means a configuration decision has been approved; **verified** means a specific surface was inspected; **proposed** means no change has been authorised or applied. The [dated verification record](../../../../governance/evidence/2026-09-claude-configuration.md) records deployment drift and claim boundaries. Desktop observations do not establish equivalent CLI, web, mobile or every existing conversation state.

## Adopted capability baseline

| Setting | Baseline | Scope and rationale |
|---|---|---|
| Optional plugins | Disabled, retained installed | Evaluate specialist workflows individually before adding them to ordinary use. |
| Standalone skills | my-voice enabled; other 13 disabled | Retain the personal output capability. The later deployment saved my-voice v2 and verified all four files against current source. See deployment alignment below. |
| Tool access mode | Load tools when needed | Verified new-conversation setting; not proof of exact tool-schema loading or token savings. |
| Connector search | Off | Keep discovery of additional connectors out of the initial baseline. |
| Cloud code execution and file creation | On | Retain document, spreadsheet, presentation and analysis capabilities. |
| Artifacts, AI-powered artifacts, inline visualisations | On | Retain useful output capabilities. |
| Memory | Existing enabled configuration retained | Product-managed continuity; memory contents remain outside the kit. |
| Personal and Cowork instructions | Updated in the later instruction deployment | Shared chat body and Cowork addendum saved and read back exactly; see deployment alignment below. |
| Research | Off for ordinary baseline work | Enable deliberately for substantial research. |
| Web search | Available when relevant | On in the inspected new chat; select according to freshness and source-verification needs. |
| Optional connector tools | Select per task | Chrome tools off and Context7 off in the inspected new chat only. Account connections retained; no universal reset claimed. |

### Plugins retained but disabled

Engineering; Enterprise Search; Sales; Finance; Data; Legal; Marketing; Customer Support; Product Management; Operations; Human Resources; Design; PDF Viewer; Productivity; Bio research.

### Standalone skills retained but disabled

influence-psychology; import-memory; morning; theme-factory; slack-gif-creator; mcp-builder; internal-comms; canvas-design; brand-guidelines; web-artifacts-builder; algorithmic-art; skill-creator; doc-coauthoring.

No plugin was uninstalled and no custom skill was deleted. Disabled vendor skills may disappear from the personal list; re-enablement can require finding them in the directory. Package presence, enabled state, discovery and actual execution are separate observations.

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

1. Start a fresh conversation on the surface being evaluated. Record the model, effort, relevant instructions, memory posture and tools exposed.
2. Test a real task against this baseline before enabling one additional capability. Compare completion, factual fidelity, unnecessary activation and correction effort.
3. Re-enable through the client's skill/plugin controls or directory. Check actual availability after the change; do not assume an existing conversation discards previously loaded instructions.
4. Keep a capability enabled when its value is established; otherwise disable it again. Uninstall only when deciding to remove the package, rather than as an assumed extra context saving.
5. When deploying a source update, compare every packaged file with the source revision and verify the installed enabled state. Record mismatches rather than silently replacing the source or client copy.
6. Update this maintained baseline for adopted decisions and add dated evidence for material verification. Recheck after meaningful product changes; avoid copying rolling model lists and prices into enduring guidance.

Early evaluation candidates: doc-coauthoring, Data, Operations and Productivity. Review influence-psychology's full content before deciding to reactivate it.

## Open decisions — not implemented

- Review duplicated standing instructions without changing the operating contract by implication.
- Consider selected working folders in place of broad drive access; actual paths and grants remain private and tool-side.
- Consider package-manager-only code-execution network access; All domains was observed and retained.
- Review Claude Code sandboxing and bypass-mode availability. Sandbox off and bypass availability on were observed in Desktop; availability does not prove a session is using bypass mode.
- Evaluate model/effort choices by task. Fable 5.1 Medium was observed; it is not a cross-surface or permanent model prescription.

## Boundaries and source guidance

Do not copy account identifiers, credentials, billing records, active-session inventories, exact trusted paths or memory contents into this public baseline. Record portable choices and verification limits. Raw audit material stays outside the repository under [ADR-012](../../../../governance/decisions/adr-012-clean-public-baseline.md).

Vendor guidance consulted on 13 September 2026: [skills and enablement](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [skill loading architecture](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [usage guidance](https://support.claude.com/en/articles/9797557-usage-limit-best-practices). The small enabled catalogue is a personal evaluation decision, not a vendor requirement. No measured token-saving claim is made.

Version: 2026.09.13 @ 1.5
