← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Platforms](../README.md) · [Claude](README.md) · **Configuration baseline**

# Claude Configuration Baseline

Where the kit is supplied to Claude, the settings Andrew maintains and the latest verified deployment. The [skills tracker](../../skills/README.md) owns package choices and their deployment notes. This guide is maintenance material.

## Where instructions go

| Surface | Supply | Destination and method |
|---|---|---|
| General instructions | [Personal preferences](personal-preferences.md) | Paste only the marked body into Settings → General → Instructions for Claude. Exclude the wrapper, generation metadata and footer. Check the current field limit before replacement. |
| Chat project | [Chat project template](chat/template-chat-project.md), completed for the project | Project instructions. Attach the core constitution for sustained work; identify supplied context without claiming it has been read. |
| Cowork | [Global addendum](cowork/global-instructions.md) plus core constitution or shared chat body | Put the addendum in Settings → Cowork → Global instructions. At setup, establish how the base reaches the session. The recorded General settings description says its instructions apply to Chat and Cowork; runtime adherence was not tested. |
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

The [13 September deployment record](../../../../governance/evidence/2026-09-claude-deployment.md) covers Claude Desktop 1.52386.6. A subsequent read-only comparison found that the current source still matches its recorded hashes.

| Component | Recorded result |
|---|---|
| General instructions | Exact 4,930-character shared chat body saved and read back. |
| Cowork addendum | Version 2026.09.13 @ 1.7; exact 2,469-character readback. |
| my-voice | Enabled v2; all four downloaded files matched source. |

This establishes alignment with the recorded deployment, not a fresh inspection of the app or behavioural adherence. Project attachments and separate Code deployments were not verified by that pass.

## Outstanding gaps and decisions

- Verify remaining plugin enable switches, update controls and representative use on the actual surface; the tracker distinguishes list presence from confirmed enablement.
- Establish Code's installed packages and permission configuration separately. Review its observed sandbox/bypass availability before choosing any change.
- The earlier folder-access and code-execution network restrictions remain undecided. Exact paths, account details and grants stay private.
- Cowork's plan confirmation, no-overwrite rule and connector previews remain as written. The review identified their extra confirmation cost and the breadth of “external connector action”; changing them requires an explicit behavioural decision.
- Model and effort choices belong in [model guidance](../model-guidance.md), rather than another package or settings register.

When a live change is requested, identify the exact settings and packages affected, preserve a restoration route, and verify saved state and useful use. Record material results once in governance evidence. Native runtime versions may not be recoverable; neither package count nor source size establishes token savings.

Version: 2026.09.13 @ 1.15
