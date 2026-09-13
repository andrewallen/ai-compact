← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Claude Customize snapshot**

# Claude Customize Snapshot — 13 September 2026

**Follow-up received the same day:** Obsidian 1.0.1 is now shown enabled with six skills. The initial five-screenshot observations below are preserved; the final section records the resolved gap.

Andrew supplied five screenshots as the current Claude configuration: Plugins → Yours, Connectors → Yours → All, Skills → Yours, Manage marketplaces, and Anthropic sources. This record transcribes the visible state. The long Skills screenshot was inspected at its original resolution. Screenshots are deployment evidence, not instructions or the discovery catalogue. Source repositories remain authoritative for published package contents.

No client controls were changed for this reconciliation. No account identifiers, credentials or raw screenshots are copied into the repository. The [Claude baseline](../../kit/implementation/platforms/claude/configuration-baseline.md) owns current configuration guidance; this is dated evidence.

## Plugins shown under Yours

Seven plugins are visible: three under From Anthropic & Partners and four under From marketplaces you added. These are list observations; the screenshots do not expose the individual enable switches.

| Displayed plugin | Displayed source | Entries on the Skills page |
|---|---|---:|
| Data | Anthropic | 10 |
| Design | Anthropic | 7 |
| PDF Viewer | Anthropic | 5 |
| I have adhd | i-have-adhd | 1 |
| Taste skill | taste-skill | 13 |
| Impeccable | impeccable | 1 |
| Frontend design | claude-plugins-official | 1 |

Obsidian is absent from the supplied plugin and skill lists, although its marketplace is present and synced. The supported current record is **marketplace added; plugin installation/availability not shown**. This corrects the earlier interpretation of Andrew's addition report. Its On target remains in the selected catalogue.

## Exact entries displayed on the Skills page

The page shows **39 entries**: 1 Created by you, 22 From Anthropic & Partners, and 16 From marketplaces you added. Names below preserve the UI labels; they need not equal upstream frontmatter names. The page can include command-like entries, so 39 is not a count of unique loaded skill bodies.

| Parent plugin / category | Displayed entries |
|---|---|
| Created by you | `my-voice` |
| Data | `analyze`, `build-dashboard`, `create-viz`, `data-context-extractor`, `data-visualization`, `explore-data`, `sql-queries`, `statistical-analysis`, `validate-data`, `write-query` |
| Design | `accessibility-review`, `design-critique`, `design-handoff`, `design-system`, `research-synthesis`, `user-research`, `ux-copy` |
| PDF Viewer | `annotate`, `fill-form`, `open`, `sign`, `view-pdf` |
| I have adhd | `i-have-adhd` |
| Taste skill | `brandkit`, `brutalist-skill`, `gpt-tasteskill`, `image-to-code-skill`, `imagegen-frontend-mobile`, `imagegen-frontend-web`, `minimalist-skill`, `output-skill`, `redesign-skill`, `soft-skill`, `stitch-skill`, `taste-skill`, `taste-skill-v1` |
| Impeccable | `impeccable` |
| Frontend design | `frontend-design` |

The screenshot shows only one Created by you entry, my-voice. It does not show the earlier manually uploaded Frontend Design copy; this establishes absence from this view, not the mechanism or permanence of its removal. No Obsidian skill is displayed. The provider document skills supplied natively are not required to appear as separate entries here.

## Connectors

| Displayed connector | Type | Status shown |
|---|---|---|
| Claude in Chrome | Desktop; Included | Connected (checkmark) |
| GitHub Integration | Web | Connected (checkmark) |

The All tab shows these two connectors. Context7 is absent, consistent with Andrew's earlier report that it was deleted. Connected status does not establish which tools are selected in any conversation or their permission scope. The earlier observation of Chrome tools being off in one chat is a different control.

## Added marketplaces

Manage marketplaces shows five entries and their abbreviated synced commits:

| Marketplace | Repository | Synced commit displayed |
|---|---|---|
| claude-plugins-official | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | `f0dce59` |
| impeccable | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | `cb56ed6` |
| taste-skill | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `ccbc156` |
| i-have-adhd | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | `6f1f982` |
| obsidian-skills | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | `8ccef29` |

These are displayed repository sync references, not verified installed-file hashes or proof that the source is at its latest revision. Automatic update settings are not shown. The dialog states that removing a marketplace also uninstalls its plugins; source removal therefore has a deployment effect.

## Anthropic sources

A separate source picker shows all six as Added:

| Source | Repository |
|---|---|
| Knowledge Work | `anthropics/knowledge-work-plugins` |
| Life Sciences | `anthropics/life-sciences` |
| Financial Services | `anthropics/financial-services` |
| Legal | `anthropics/claude-for-legal` |
| Claude Tag | `anthropics/claude-tag-plugins` |
| Healthcare | `anthropics/healthcare` |

These are distinct from the five entries in Manage marketplaces. Source inclusion does not establish that every plugin from that source is installed or enabled. Only the seven plugins listed above are visible in Yours.

## Verification limits and remaining delta

The selected catalogue has eight On-target plugins; seven are shown, with Obsidian the visible gap. The screenshots corroborate catalogue presence, skill labels, connector status and marketplace sync references. They do not establish runtime invocation, active hooks, installed package versions, file parity, update automation, token usage, output quality, or separate Claude Code/Codex deployment.

Native capabilities, memory, tool-loading mode, connector search and standing instructions are not shown in this screenshot set; retain their earlier recorded status without treating them as newly checked. No behaviour tests or configuration changes were performed. The whole-plugin On/Off model is unchanged.

## Follow-up: Obsidian installed and enabled

Andrew subsequently supplied the Obsidian plugin detail screenshot and stated that it had now been added. The page shows **Obsidian**, source **obsidian-skills**, version **1.0.1**, a blue On enable switch and **6 skills**. The visible entries are:

- `/defuddle`
- `/obsidian-bases`
- `/obsidian-markdown`
- `/knap`
- `/obsidian-cli`
- `/json-canvas`

The UI describes slash invocation and automatic use for relevant tasks. This is displayed capability guidance, not an observed invocation test.

This follow-up supersedes the earlier marketplace-only gap. All eight selected plugins are now evidenced across the supplied screenshots. The initial 39 entries plus these six reconcile to **45 entries in aggregate**; no refreshed full Skills list was supplied. The enabled switch and version are directly visible for Obsidian. Automatic-update configuration, execution of its local tools and separate Code/Codex deployment remain untested. No client controls were changed during this documentation update.
