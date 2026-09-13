← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Skills** · [Prompts](../prompts/README.md)

# Skills and Capability Catalogue

The selected capabilities for Andrew's thinking and output work, linked to their upstream sources and harness configuration. This catalogue owns **what to use**; the [Claude baseline](../platforms/claude/configuration-baseline.md) and [Codex baseline](../platforms/codex/configuration-baseline.md) own **how to configure it**. These are maintenance references, not standing instructions or a runtime router.

**Policy adopted on 13 September 2026; live harmonisation partially recorded in the platform baselines.** Prefer Anthropic's own published capabilities in Claude and OpenAI's in Codex. Retain useful native capabilities before adding packages. Do not cross-deploy the providers' skills to make the installations match. Consistency means comparable output standards and operating boundaries, with delivery appropriate to each harness. Provider authorship is a reason to start there, not evidence of a measured quality advantage.

## Selection states

| State | Meaning |
|---|---|
| **On** | Keep the capability or plugin enabled and available. Enabling a Claude plugin makes every included skill available; availability does not mean every skill body is loaded or executed in every conversation. |
| **Off** | Keep disabled or undeployed. A disabled Claude plugin is unavailable to select in chat. Do not uninstall merely to reduce the package count. |

These are adopted target choices, not claims about installed state. There is no task-only configuration state in this catalogue. For Claude, enablement is at plugin level: all included skills are available when On; none are available to select when Off. Do not prescribe switching plugins on and off around each job. Assess the complete bundle when choosing whether to keep it enabled; relevance of invocation is a separate concern. Verify other harness controls independently.

## Core provider capabilities

| Job and required outcome | Claude implementation | Codex implementation | Target |
|---|---|---|---|
| Documents, spreadsheets, presentations and PDFs: usable files, faithful content, readable rendering; editability where requested | Native file workflows with Code execution and file creation enabled. In Claude Code, use Anthropic's [document-skills](https://github.com/anthropics/skills/blob/main/.claude-plugin/marketplace.json) only where the environment needs them. | Supplied Documents, Spreadsheets, Presentations and PDF workflows where available. Product-managed availability is checked in the harness; these are not all public marketplace entries. | **On** |
| Research and synthesis: current sources when needed, traceable claims, evidence distinguished from inference | Native web search and source analysis; deliberate Research mode for substantial research. | Native search and source analysis; any specialised research mode selected for the task where available. | **On** for ordinary search/source work |
| Visual explanation: a useful diagram, artifact or interactive explanation when it helps understanding | Native artifacts and inline visualisations. | Native visual explanation and artifact tools where supplied. Retain OpenAI's [imagegen](https://github.com/openai/skills/tree/main/skills/.system/imagegen) for requested image work. | **On** |
| Quantitative analysis: sound calculations, inspectable evidence and a decision-useful report or dashboard | Anthropic [Data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data), package `data`. | OpenAI [Data Analytics](https://github.com/openai/plugins/tree/main/plugins/data-analytics), package `data-analytics`. | **On** |
| Design creation: coherent visual hierarchy and a usable, responsive result | Anthropic [frontend-design](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design), shown installed from `claude-plugins-official` in the supplied screenshots. The [Claude baseline](../platforms/claude/configuration-baseline.md) separates installation from enabled-state verification. | OpenAI [Product Design](https://github.com/openai/plugins/tree/main/plugins/product-design), package `product-design`. | **On** |
| Design critique: evidence-based UX and accessibility findings with actionable fixes | Anthropic [Design](https://github.com/anthropics/knowledge-work-plugins/tree/main/design), package `design`. Critique/accessibility motivate selection, but enabling the plugin makes all its skills available. | Relevant audit/QA workflows in the same Product Design package. | **On** |
| Interactive PDF viewing | PDF Viewer plugin, retained alongside native PDF file workflows. Shown in the current plugin list and reported enabled; see the [Claude baseline](../platforms/claude/configuration-baseline.md). | Retain native PDF workflows; no additional viewer plugin selected. | **On** |

Native file support is documented in [Claude's skill guidance](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [OpenAI's artifact guidance](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work). Availability varies by surface and account. Public source code establishes a published implementation, not that a particular native runtime uses the same revision. Ordinary file creation and simple charts do not require enabling a broad Data or Design package.

## Provider additions off for now

These choices concern the ordinary thinking and output configuration. Engineering packages can be considered within a separately defined engineering task; disabling an optional security workflow does not mean disabling host security controls.

| Provider | Leave off | Reason to reconsider |
|---|---|---|
| Anthropic | `enterprise-search`; `productivity` | A recurring need for connected workplace search, or an explicitly designed task/memory workflow. Neither is required for general synthesis; productivity storage needs to fit the existing knowledge system. |
| Anthropic | `sales`, `finance`, `legal`, `marketing`, `customer-support`, `human-resources`, `operations`, `product-management`, `small-business`, `bio-research` | A specific recurring specialist job with useful outputs. Topic overlap alone is insufficient. |
| Anthropic | `brand-guidelines`, `internal-comms`, `theme-factory`, `canvas-design`, `algorithmic-art`, `slack-gif-creator`, `discernment-nudge` | A concrete output need beyond native tools and the existing contract. Anthropic's brand guidelines are not Andrew's brand. |
| Anthropic | Optional `skill-creator`, `mcp-builder`, `plugin-dev`, `engineering`, `code-review`, `pr-review-toolkit`, `feature-dev` | A defined authoring or engineering task. |
| OpenAI | `creative-production`; `build-web-data-visualization` | Campaign production or an advanced visualisation job that the selected native/Data/Design routes do not adequately cover. |
| OpenAI | `public-equity-investing`, `life-science-research`, `ngs-analysis` | A recurring specialist research workflow. |
| OpenAI | `game-studio`, `build-ios-apps`, `build-macos-apps`, `build-web-apps`, `test-android-apps` | A defined application-development or testing task. |
| OpenAI | `codex-security`, `openai-developers`, `plugin-eval` and optional extra authoring packages | A security review, API/agent build or skill/plugin maintenance task. Retain supplied system utilities; avoid duplicate installations. |

The [Anthropic skills manifest](https://github.com/anthropics/skills/blob/main/.claude-plugin/marketplace.json), [knowledge-work manifest](https://github.com/anthropics/knowledge-work-plugins/blob/main/.claude-plugin/marketplace.json), [Claude plugin manifest](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json) and [OpenAI plugin manifest](https://github.com/openai/plugins/blob/main/.agents/plugins/marketplace.json) identify these public offerings. Connector access is a separate dependency decision: preserve existing accounts and permissions, and check affected workflows before disabling a package that supplies shared tools.

## Source and deployment rules

Use the labs' GitHub repositories to identify provider offerings and the original authors' repositories for independent skills and packages. Check authorship in the relevant package, not just marketplace membership: both providers also distribute partner work. Use official product documentation for native capabilities and supported controls. Local installations are evidence of deployment only, never the discovery catalogue or proof of provenance.

The selection above was checked against upstream sources on 13 September 2026. Use provider-managed native capabilities, marketplaces or directories, retaining their supported update mechanism. Verify update controls rather than assuming every route automatically applies releases. Do not manually upload provider skills, vendor copies into the kit, edit managed caches, create a personal marketplace or introduce an installer solely to maintain this list. If a managed route is unavailable, leave the addition undeployed and record the gap.

Keep review proportional. The [review method](review-method.md) covers fit, source checks, configuration and useful live evidence. The [implementation plan](implementation-plan.md) records the completed repository work and remaining deployment sequence. No comparative output results or token savings have yet been established for this selection.

## Authored and independent skills

**Authored — parked in this batch.** [my-voice](my-voice/SKILL.md) remains the single maintained personal skill. Its [authored register](my-voice/authored-register.md), [documentation register](my-voice/documentation-register.md) and [examples](my-voice/examples.md) remain unchanged. The [Claude deployment record](../../../governance/evidence/2026-09-claude-deployment.md) verifies all four files in the enabled v2 package; it does not establish other harness deployments or runtime invocation.

**Independent third-party selection has begun.** Independently authored skills may be deployed across both harnesses where they add recurring value and each host supports their dependencies and controls. Prioritise demonstrated use, maintained examples/tests and credible user results; popularity is a discovery signal, not proof. Existing third-party installations are not removal targets in this work.

| Plugin / skill | Marketplace and source | Purpose and scope | Recorded deployment |
|---|---|---|---|
| Impeccable (`impeccable`) | Marketplace `impeccable`, from [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Frontend design, critique and refinement. The published plugin includes the impeccable skill, commands, agents and hooks; the installed components and their execution have not been inspected. | Claude: plugin and `impeccable` entry shown in the 13 September screenshots; source marketplace is synced. **On target**; enable switch, hooks and automatic updates are not shown. Codex deployment is not established. See the [Claude baseline](../platforms/claude/configuration-baseline.md). |
| i-have-adhd (`i-have-adhd`) | Published marketplace and plugin `i-have-adhd`, from [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | One skill, `i-have-adhd`, for concise, action-first responses, numbered steps and fewer tangents. This is interaction formatting; the constitution and authored voice retain their authority. | Claude: plugin and skill shown in the 13 September screenshots; source marketplace is synced. **On target**; enable switch, hooks and automatic updates are not shown. Codex deployment is not established. |
| Taste Skill (`taste-skill`) | Published marketplace and plugin `taste-skill`, from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | A collection of frontend implementation, redesign, aesthetic and image-generation skills, including `design-taste-frontend`, `redesign-existing-projects` and `image-to-code`. Enabling the plugin exposes the included collection; it is not just one taste instruction. | Claude: plugin and 13 displayed skill entries shown in the 13 September screenshots; source marketplace is synced. **On target**; UI names differ from some upstream install names. Exact labels are in the [snapshot](../../../governance/evidence/2026-09-claude-customize-snapshot.md). Enable switch and automatic updates are not shown. Codex deployment is not established. |
| Obsidian (`obsidian`) | Marketplace `obsidian-skills`, from [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Six upstream skills: `obsidian-markdown`, `obsidian-bases`, `json-canvas`, `obsidian-cli`, `defuddle` and `knap`. Supports vault formats, local vault operations, web-content extraction and template generation; local-tool workflows depend on host access. | Claude: follow-up screenshot on 13 September confirms plugin **1.0.1 enabled**, from `obsidian-skills`, with all six skills displayed. This closes the initial marketplace-only gap. Automatic updates and local-tool execution remain untested. Codex deployment is not established by this update. |

The provider design selections remain in place. Impeccable and Taste Skill overlap with those capabilities and each other; incremental value is to be judged through use. Their installations do not establish a measured quality improvement. Other researched third-party candidates have not been adopted.

For authoring, use [best practices](best-practices.md) and the [_template](_template/SKILL.md). The template is scaffolding, not a deployable skill. Keep the portable `SKILL.md` core separate from client-specific invocation extensions; index each new maintained skill and supporting file. Skills supplement the constitution and never override it.

## Historical research

These documents are retained for traceability and are no longer required registers to maintain when making a selection.

| Record | Boundary |
|---|---|
| [First-party inventory](first-party-inventory.md) | Unchanged dated research, including local runtime observations. Its local observations are not the source of truth for this catalogue. |
| [Capability matrix](capability-matrix.md) | Superseded assessment structure and historical provider summaries. |
| [Package register](package-register.md) | Superseded implementation IDs, candidates and former pilot composition records. |
| [Source register](source-register.md) | Superseded candidate/source register; follow current upstream links above for selections. |
| [Capability composition probes](../../evals/capability-composition-probes.md) | Authored, unexecuted examples available for targeted checks; no compulsory full pilot. |
