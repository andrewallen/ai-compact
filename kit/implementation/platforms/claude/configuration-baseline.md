← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Platforms](../README.md) · [Claude](README.md) · **Configuration baseline**

# Claude Configuration Baseline

Where the kit is supplied to Claude, the settings Andrew maintains and the latest verified deployment. The [skills tracker](../../skills/README.md) owns package choices and their deployment notes. This guide is maintenance material.

## Where instructions go

| Surface | Supply | Destination and method |
|---|---|---|
| Account instructions | [Personal preferences](personal-preferences.md) | Settings → Account → Instructions for Claude. Replace the base with only the marked body, excluding wrapper, generation metadata and footer. Preserve the separately identified Cowork addendum already in this field. Verify the complete saved text; the inspected client accepted 7,495 characters in total. |
| Chat project | [Chat project template](chat/template-chat-project.md), completed for the project | Project instructions. Attach the core constitution for sustained work; identify supplied context without claiming it has been read. |
| Cowork | [Global addendum](cowork/global-instructions.md) plus core constitution or shared chat body | The inspected client migrated the addendum into Account → Instructions for Claude, following the base under `[Imported from Cowork]:`. Keep it separately identified there. The UI says the field applies across chats and Cowork; runtime adherence and mode-specific application were not tested. |
| Cowork project | [Cowork project template](cowork/template-cowork-project.md), completed for the work | Project or folder instructions. Record working locations, context, objectives and task-specific authority. |
| Code | [Code guide](code/README.md) | Supply the marked execution body in the opening task message, or have Code read the core files at session start. Configure this surface separately. |

The core is bootstrap, calibration and operating contract from the [constitution](../../../constitution/README.md); add the professional overlay only when relevant. Supply my-voice separately for its execution work. Edit generated contracts through their [shared sources](../contract-maintenance.md), then verify the saved destination after deployment.

## Maintained settings

| Setting | Preference and last recorded observation |
|---|---|
| Code execution and file creation | On; retain native document, spreadsheet, presentation and PDF workflows. |
| Artifacts and inline visualisations | On, including AI-powered artifacts in the inspected settings. |
| Tool access mode | Load tools when needed. |
| Connector search | Off. |
| Research and web search | Research selected deliberately for substantial work; off in the inspected ordinary chat. Web search available and On there. |
| Memory | Existing enabled configuration retained; memory contents stay outside the kit. |
| Connections | Claude in Chrome and GitHub Integration recorded connected. Per-chat tool selection is separate. |
| Skill delivery | Use managed provider packages. Assess and enable the whole selected plugin; invocation is separate from availability. Check update controls, and avoid duplicate native or standalone copies. |

The [initial settings inspection](../../../../governance/evidence/2026-09-claude-configuration.md) supports the retained native settings. The [Customize snapshot](../../../../governance/evidence/2026-09-claude-customize-snapshot.md) records later package and connector observations. Earlier disabled inventories remain in evidence and Git history.

For product controls, use Anthropic's [skill guidance](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [directory guidance](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory) and [Cowork instructions guide](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork). Managed provider delivery is the default; the personal my-voice package has a separate upload/replacement route. These choices do not change account connections or permissions automatically.

## Latest verified instruction deployment

The [19 September instruction refresh](../../../../governance/evidence/2026-09-claude-instruction-refresh.md) verifies the account instructions and my-voice package at that revision. It supersedes the saved-state observations in the [13 September deployment record](../../../../governance/evidence/2026-09-claude-deployment.md) and earlier [voice maintenance record](../../../../governance/evidence/2026-09-voice-maintenance.md), including the two source revisions from [repository consolidation](../../../../governance/evidence/2026-09-repository-consolidation.md). The later [voice plugin repair](../../../../governance/evidence/2026-09-voice-plugin-validation.md) changes all four source files; that revision has not been deployed to Claude.

| Component | Recorded result |
|---|---|
| Account instructions | Shared chat source 2026.09.19 @ 1.1: exact 5,000-character base saved. The complete field, including the imported Cowork section, is 7,495 characters and matched after navigating away and reopening settings. |
| Cowork addendum | Version 2026.09.13 @ 1.7; exact 2,469-character match to source, preserved unchanged within the combined account field. |
| my-voice | 19 September: enabled v4; all four downloaded files exactly matched the instruction-refresh source. The later plugin-repair source is not deployed. |

These results come from fresh inspection in Claude Desktop 2.2553.1, a saved account-field readback and a downloaded skill comparison. Package identity does not establish invocation or behavioural adherence. Andrew explicitly excluded individual projects from this refresh; their attachments and separate Code deployments remain unverified.

## Outstanding gaps and decisions

- Account instructions match the refreshed sources. Claude my-voice v4 retains the earlier skill revision; the later four-file repair needs a separately authorised deployment. Invocation and behaviour in Claude remain unverified; local Codex text probes do not establish Claude behaviour.
- Verify remaining plugin enable switches, update controls and representative use on the actual surface; the tracker distinguishes list presence from confirmed enablement.
- Establish Code's installed packages and permission configuration separately. Review its observed sandbox/bypass availability before choosing any change.
- The earlier folder-access and code-execution network restrictions remain undecided. Exact paths, account details and grants stay private.
- Cowork's plan confirmation, no-overwrite rule and connector previews remain as written. The review identified their extra confirmation cost and the breadth of “external connector action”; changing them requires an explicit behavioural decision.
- Model and effort choices belong in [model guidance](../model-guidance.md), rather than another package or settings register.

When a live change is requested, identify the exact settings and packages affected, preserve a restoration route, and verify saved state and useful use. Record material results once in governance evidence. Native runtime versions may not be recoverable; neither package count nor source size establishes token savings.

Version: 2026.09.19 @ 1.20
