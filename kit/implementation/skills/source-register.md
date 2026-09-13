← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Skills](README.md) · **Source register**

# Skill Source Register

> **Historical — superseded on 13 September 2026.** The [selected catalogue](README.md) now owns current choices; the [Claude](../platforms/claude/configuration-baseline.md) and [Codex](../platforms/codex/configuration-baseline.md) baselines own configuration. The original record below is retained as research history, including its former ownership, shortlist and trial assumptions. It is no longer an active register or a deployment instruction.

Research snapshot prepared on 13 September 2026. Maintenance reference, not an installed-skill inventory or runtime instruction. See the [capability matrix](capability-matrix.md) for coverage and the [review method](review-method.md) for admission and re-review.

The current shortlist is restricted to Anthropic/OpenAI first-party offerings. The [first-party inventory](first-party-inventory.md) supplies pinned source revisions, complete package lists and attribution exclusions. Earlier external candidates below are retained as research history and are outside this validation.

The [package register](package-register.md) links S01/S02/S11/S12/S13 to concrete baseline and candidate implementation IDs. It owns package selection and composition; this register owns source provenance. A package row is not a deployment or performance claim.

## Evidence and revision boundaries

The linked public repositories and selected skill bodies were inspected during the research conversation. The original links below are moving URLs. The later first-party inventory captures pinned revisions and relevant manifests for five lab repositories; external candidates remain unpinned. Neither establishes deployment readiness or complete component-level licence review. Maintainer statements, visible methods and local measurements are different evidence. No candidate has a local comparative quality or token result in this register.

Before a trial or installation, record the exact repository commit, all files used, licence, actual client/model and dependencies. A matching skill name or a directory's popularity does not establish provenance or version parity. Licences must be checked per skill, including bundled scripts/assets, before copying or redistribution.

## Primary sources and candidates

| ID | Source and useful entry points | Why retain it | Portability, dependencies and provisional disposition |
|---|---|---|---|
| S01 | [Anthropic skills](https://github.com/anthropics/skills): [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator), [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design), [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx), [docx](https://github.com/anthropics/skills/tree/main/skills/docx), [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf), [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx). | Official reference; repository states document skills underpin production capabilities. Skill-creator includes baseline comparisons and human/quantitative review. | Methods can inform both labs' workflows; execution scripts, dependencies and client assumptions require inspection. Document skills have source-available terms; other examples often Apache-2.0. Reference first; evaluate selected additions. |
| S02 | [Anthropic knowledge-work plugins](https://github.com/anthropics/knowledge-work-plugins): [knowledge-synthesis](https://github.com/anthropics/knowledge-work-plugins/blob/main/enterprise-search/skills/knowledge-synthesis/SKILL.md), [product-management](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management), [data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data). | Specific synthesis, research, communication and validation methods; official collection positioned as customisable starting points. | Plugin commands/connectors are client-coupled. Extracting a method does not transfer those integrations. Prefer one narrow workflow after native baseline testing. |
| S03 | [OpenAI skills](https://github.com/openai/skills), [curated catalogue](https://github.com/openai/skills/tree/main/skills/.curated). | Lab-maintained Codex catalogue with mixed provenance; not a first-party authorship guarantee. | Notion, Microsoft and Vercel attribution was found in individual skills; these are excluded from the exclusively lab-authored shortlist. Other attribution requires checking. Public source does not establish runtime identity. |
| S04 | [Kepano Obsidian skills](https://github.com/kepano/obsidian-skills). | Focused Markdown, Bases, Canvas, Obsidian CLI and Defuddle mechanics. | MIT repository; formats are portable, CLI and extraction workflows need corresponding tools and access. Verify existing installations before adding copies. |
| S05 | [Impeccable](https://github.com/pbakaus/impeccable). | Design shaping, critique, typography/layout work, browser iteration and deterministic checks. | Current package includes engine, optional hooks and context/state files. Inspect full install effects and licence at pinned revision. Candidate for scoped web-design trial; aesthetic defaults must fit the brief. |
| S06 | [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill). | Searchable design guidance, palettes, font pairings and UI patterns. | Repository advertises MIT and multi-client support. Search tooling/data and client packaging need verification. Reference or alternate trial; no evidence that catalogue size predicts design quality. |
| S07 | [Frontend Slides](https://github.com/zarazhangrui/frontend-slides). | Style previews before the full HTML deck; templates and PowerPoint-to-web conversion. | MIT repository. Browser delivery differs from editable PPTX; conversion/export have additional tooling. Candidate for C08, not proof of C07 coverage. |
| S08 | [Peter Yang no-ai-slop](https://github.com/petergyang/no-ai-slop); secondary [Blader humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md). | No-ai-slop separates detection from minimum-effective editing. Humanizer offers detailed pattern examples and a preservation check. | Text methods are relatively portable; verify exact licence/package. Humanizer's inspected wording permits adding reactions/opinions in some contexts, requiring adaptation for ownership. Current Codex no-ai-slop is exposed, not benchmarked. |
| S09 | [Visual Explainer](https://github.com/nicobailon/visual-explainer). | HTML diagrams, comparisons, tables, reviews and slide decks. | Browser/runtime assets and package terms need pinned inspection. Candidate when native visuals leave a gap, not a universal replacement for document/chart tooling. |
| S10 | [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills), [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md). | Search logging, screening, quality appraisal and citation verification for literature work. | Selected skill references other skills/tools and requires generated figures. Adapt before general research use. Maintainer validation claims are not independent performance evidence. |
| S11 | [Personal my-voice](my-voice/SKILL.md). | Canonical personal output craft, register routing and genericity detector. | Source in this repo; Claude v2 parity historically verified in deployment record. Other installed copies unverified. Preserve exploration/ownership boundary across adapters. |

## Additional first-party sources

| ID | Source | Evidence boundary |
|---|---|---|
| S12 | [OpenAI plugins](https://github.com/openai/plugins) | Mixed marketplace; the inventory identifies 26 affirmatively first-party packages. Includes Product Design, Data, Creative Production, web data visualisation and plugin-eval. |
| S13 | OpenAI local runtime/bundled packages, recorded in the [inventory](first-party-inventory.md#openai-runtime-and-locally-observed-packages) | Manifest attribution and session exposure recorded separately; includes Documents, Presentations, PDF, Spreadsheets, Sites, visualize and additional role packages. |
| S14 | [Anthropic official Claude Code plugins](https://github.com/anthropics/claude-plugins-official) | Internal first-party sources distinguished from external plugins; 38 local marketplace entries, including non-skill packages. |

## Discovery and evaluation sources

| Source | Appropriate use | Limit |
|---|---|---|
| [Skills.sh](https://skills.sh/), [ranking/security explanation](https://www.skills.sh/docs) | Find candidates and inspect upstream links. | Ranking uses installation telemetry; security audits do not establish task quality. |
| [VoltAgent awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Map to official and community maintainers. | Inclusion is not a benchmark result. |
| [Composio awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills), [contribution requirements](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/CONTRIBUTING.md) | Workflow ideas and individual candidates. | Requested contributor testing is not a common published evaluation. Inspect example citations and voice assumptions. |
| [Medici deck bake-off](https://github.com/medici-finance/deck-bakeoff) | Inspect a shared brief, generated artifacts, review records and human judgement. | One product pitch and agent setup; no general presentation ranking inferred. |
| [Agent Skills standard](https://agentskills.io), [Claude Code skills](https://code.claude.com/docs/en/skills), [Anthropic authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), [OpenAI build skills](https://learn.chatgpt.com/docs/build-skills) | Check format, discovery and implementation guidance before adapting. | A common format does not establish common runtime, permissions or model performance. |

## Selection record to complete per trial

Record capability IDs; source URL and commit; complete package scope; licence; target client/version and model/effort; native provider being compared; adapters and dependencies; relevant overlap/constitution findings; loaded resources and observed usage; acceptance results; status and next review trigger. Use **reference**, **candidate**, **trialled**, **selected**, **deployed/verified**, or **retired proposal** as distinct states. Selection is not deployment approval. No automatic updates or subscriptions are created by listing a source.
