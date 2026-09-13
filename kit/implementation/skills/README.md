← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Skills** · [Prompts](../prompts/README.md)

# Skills

The skills Andrew has chosen for his working set: what each is for, where it comes from and where it is available. Deployment notes distinguish an adopted choice from observed installation or successful use. This is a maintenance tracker; it does not route tasks or catalogue every available package.

Prefer Anthropic's own capabilities in Claude and OpenAI's in Codex, retaining useful native workflows. Use independent skills across platforms where useful and supported. Keep provider packages on their managed delivery routes; do not copy them into this repo or cross-deploy them solely to match installations.

## Working set

Deployment observations below are dated **13 September 2026**. Claude observations come from the [deployment record](../../../governance/evidence/2026-09-claude-deployment.md) and [Customize snapshot](../../../governance/evidence/2026-09-claude-customize-snapshot.md). Codex observations are limited to this review's exposed skill catalogue and local voice-file comparison. Availability alone does not establish actual use or output quality.

| Skill or package / source | Used for | Platform | Deployment note |
|---|---|---|---|
| [my-voice](my-voice/SKILL.md) | Personal output, register selection and factual documentation standards | Claude; Codex | Claude: v2 recorded enabled; the later authored-register correction awaits deployment (see [baseline](../platforms/claude/configuration-baseline.md)). Codex: the last comparison found all four local files divergent from source. |
| Native [document skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | Word, Excel, PowerPoint and PDF work | Claude Chat/Cowork | Code execution and file creation recorded On. Separate document-skill installation is unnecessary where native workflows are supplied. |
| OpenAI-supplied Documents, Spreadsheets, Presentations and PDF workflows | Create, edit and inspect files | Codex | All four workflows exposed in the review session; execution not tested here. |
| OpenAI-bundled visualize | Inline visual explanations and interactive tools | Codex | Skill exposed in the review session. |
| [imagegen](https://github.com/openai/skills/tree/main/skills/.system/imagegen) | Image creation and editing | Codex | System skill exposed in the review session. |
| [Data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data) | Quantitative analysis, charts and dashboards | Claude | Plugin and skills listed; enable switch not independently verified in the latest screenshots. |
| [Data Analytics](https://github.com/openai/plugins/tree/main/plugins/data-analytics) | Data analysis, validation, reports and dashboards | Codex | Workflows exposed in the review session; public/local source parity not established. |
| [Design](https://github.com/anthropics/knowledge-work-plugins/tree/main/design) | Design critique, accessibility and UX work | Claude | Plugin and skills listed; enable switch not independently verified in the latest screenshots. |
| [frontend-design](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design) | Frontend design and implementation | Claude | Managed plugin listed; separate Code deployment unverified. |
| [Product Design](https://github.com/openai/plugins/tree/main/plugins/product-design) | Design exploration, implementation and UX audits | Codex | Workflows exposed in the review session; public/local source parity not established. |
| [PDF Viewer](https://github.com/anthropics/knowledge-work-plugins/tree/main/pdf-viewer) | Interactive PDF viewing and related tools | Claude | Plugin listed; enabled state user-reported. |
| [Impeccable](https://github.com/pbakaus/impeccable) | Frontend design, critique and refinement | Claude | Plugin listed; Codex deployment unverified. |
| [i-have-adhd](https://github.com/ayghri/i-have-adhd) | Concise, action-first response formatting | Claude | Plugin listed; Codex deployment unverified. Applies within the constitution and voice boundaries. |
| [Taste Skill](https://github.com/Leonxlnx/taste-skill) | Frontend design, redesign and visual treatments | Claude | Plugin collection listed; Codex deployment unverified. |
| [Obsidian skills](https://github.com/kepano/obsidian-skills) | Vault formats, vault operations and web extraction | Claude; Codex | Claude: plugin 1.0.1 enabled with six skills. Codex: Markdown, Bases, Canvas, CLI and Defuddle exposed; knap not exposed in the review session. Tool execution untested. |

Impeccable, Taste Skill and the provider design workflows overlap. Their separate value remains to be established through use; listing them records the adopted set rather than a comparative quality judgement.

## Maintained personal source

The four files in [my-voice](my-voice/SKILL.md) are maintained here: the skill entry point, [authored register](my-voice/authored-register.md), [documentation register](my-voice/documentation-register.md) and [examples](my-voice/examples.md). External packages remain with their maintainers.

## Keeping this useful

Add an entry when Andrew adopts a skill, with its recurring job, upstream source and platform. Update it when use or deployment changes; installed or exposed does not mean used. Track a bundle once unless individual skills are selected separately. Revisit overlap or unwanted activation when use exposes friction, using a representative task and a comparison only when it would resolve uncertainty.

[Claude configuration](../platforms/claude/configuration-baseline.md) and [Codex configuration](../platforms/codex/configuration-baseline.md) own setup and remaining deployment gaps. Keep detailed verification in dated governance evidence and link it once. Ordinary use needs no new formal record. Unselected offerings and superseded research remain outside the tracker; Git history preserves the removed research and planning documents.
