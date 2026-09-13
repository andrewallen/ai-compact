← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Skills](README.md) · **First-party inventory**

# Anthropic and OpenAI First-party Inventory

Validated on 13 September 2026. Maintenance evidence for the [capability matrix](capability-matrix.md), [source register](source-register.md) and [review method](review-method.md); not runtime instructions or an installation decision.

## Scope and what validation establishes

First-party means a package published or maintained by the lab with affirmative attribution in its manifest, official repository documentation or lab announcement. Marketplace membership, a curated directory, or an Anthropic Verified badge is insufficient. Package publishing does not establish that every included script or skill was originally authored by the lab. Third-party attribution found during inspection is called out; complete component-level authorship and licence audits remain necessary before copying a package. A lab-published integration with an external service is distinguishable from a partner-published plugin.

The audit enumerated untruncated recursive Git trees and plugin/marketplace manifests at the revisions below. Skill counts count SKILL.md files under the stated source path, including nested entry points. They are not counts of unique capabilities, enabled skills, production guarantees or independent quality tests. Names can recur across repositories. Local manifests supplement public sources; a cached package is not necessarily enabled or exposed.

| Public source | Pinned revision | Coverage |
|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624) | `34040c9c568585f6929bedeaad110ad08f079624` | Recursive tree; relevant plugin/marketplace manifests. |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4) | `9d2f91967414abcf3e15f08a53b7de347f81c5e4` | Recursive tree; relevant plugin/marketplace manifests. |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537) | `f0dce59fec064db10450cb6ed6e33c1080d61537` | Recursive tree; relevant plugin/marketplace manifests. |
| [openai/skills](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431) | `49f948faa9258a0c61caceaf225e179651397431` | Recursive tree; relevant plugin/marketplace manifests. |
| [openai/plugins](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89) | `1dc195897af4161d039b80d8471ec0a10c9bbc89` | Recursive tree; relevant plugin/marketplace manifests. |

These are bounded snapshots of the audited sources, not a claim to enumerate every private, enterprise or account-specific lab offering. One third-party ClickUp manifest fetch failed; it does not affect the first-party package list. Public skill and licence text was additionally inspected for openai/skills. Other package internals were not exhaustively audited.

## Anthropic standalone skills and bundles

**19 skill directories** in the pinned source: `academy-guide`, `algorithmic-art`, `brand-guidelines`, `canvas-design`, `claude-api`, `discernment-nudge`, `doc-coauthoring`, `docx`, `frontend-design`, `internal-comms`, `mcp-builder`, `pdf`, `pptx`, `skill-creator`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`, `webapp-testing`, `xlsx`.

The marketplace groups `docx`, `pdf`, `pptx`, and `xlsx` as `document-skills`; twelve creative/authoring/development examples as `example-skills`; and `claude-api`, `academy-guide`, and `discernment-nudge` as separate bundles. These are distribution groupings of the same source, not additional skills. Public document implementations may differ from the client-bundled production versions.

For this kit, the most relevant are `frontend-design`, `canvas-design`, `theme-factory`, `doc-coauthoring`, the four file-format skills and `skill-creator`. `brand-guidelines` contains Anthropic brand guidance, so it is not a personal design default. `discernment-nudge` encourages scrutiny of AI output; review its overlap with the constitution before adoption.

## Anthropic knowledge-work plugins

All packages below have Anthropic author attribution in their plugin manifests. Source presence and marketplace listing are separate observations.

| Plugin / source | Version | Skill files | Contained skill paths |
|---|---|---|---|
| [bio-research](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/bio-research) | 1.2.0 | 6 | `instrument-data-to-allotrope`, `nextflow-development`, `scientific-problem-selection`, `scvi-tools`, `single-cell-rna-qc`, `start` |
| [cowork-plugin-management](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/cowork-plugin-management) | 0.2.2 | 2 | `cowork-plugin-customizer`, `create-cowork-plugin` |
| [customer-support](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/customer-support) | 1.3.0 | 5 | `customer-escalation`, `customer-research`, `draft-response`, `kb-article`, `ticket-triage` |
| [data](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/data) | 1.1.0 | 10 | `analyze`, `build-dashboard`, `create-viz`, `data-context-extractor`, `data-visualization`, `explore-data`, `sql-queries`, `statistical-analysis`, `validate-data`, `write-query` |
| [design](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/design) | 1.2.0 | 7 | `accessibility-review`, `design-critique`, `design-handoff`, `design-system`, `research-synthesis`, `user-research`, `ux-copy` |
| [engineering](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/engineering) | 1.2.0 | 10 | `architecture`, `code-review`, `debug`, `deploy-checklist`, `documentation`, `incident-response`, `standup`, `system-design`, `tech-debt`, `testing-strategy` |
| [enterprise-search](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/enterprise-search) | 1.3.0 | 5 | `digest`, `knowledge-synthesis`, `search`, `search-strategy`, `source-management` |
| [finance](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/finance) | 1.3.0 | 8 | `audit-support`, `close-management`, `financial-statements`, `journal-entry`, `journal-entry-prep`, `reconciliation`, `sox-testing`, `variance-analysis` |
| [human-resources](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/human-resources) | 1.3.0 | 9 | `comp-analysis`, `draft-offer`, `interview-prep`, `onboarding`, `org-planning`, `people-report`, `performance-review`, `policy-lookup`, `recruiting-pipeline` |
| [legal](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/legal) | 1.3.0 | 9 | `brief`, `compliance-check`, `legal-response`, `legal-risk-assessment`, `meeting-briefing`, `review-contract`, `signature-request`, `triage-nda`, `vendor-check` |
| [marketing](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/marketing) | 1.2.0 | 8 | `brand-review`, `campaign-plan`, `competitive-brief`, `content-creation`, `draft-content`, `email-sequence`, `performance-report`, `seo-audit` |
| [operations](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/operations) | 1.3.0 | 9 | `capacity-plan`, `change-request`, `compliance-tracking`, `process-doc`, `process-optimization`, `risk-assessment`, `runbook`, `status-report`, `vendor-review` |
| [pdf-viewer](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/pdf-viewer) | 0.2.0 | 1 | `view-pdf` |
| [product-management](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/product-management) | 1.2.0 | 8 | `competitive-brief`, `metrics-review`, `product-brainstorming`, `roadmap-update`, `sprint-planning`, `stakeholder-update`, `synthesize-research`, `write-spec` |
| [productivity](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/productivity) | 1.3.1 | 4 | `memory-management`, `start`, `task-management`, `update` |
| [sales](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/sales) | 1.3.0 | 9 | `account-research`, `call-prep`, `call-summary`, `competitive-intelligence`, `create-an-asset`, `daily-briefing`, `draft-outreach`, `forecast`, `pipeline-review` |
| [small-business](https://github.com/anthropics/knowledge-work-plugins/tree/9d2f91967414abcf3e15f08a53b7de347f81c5e4/small-business) | 0.3.0 | 31 | `business-pulse`, `call-list`, `canva-creator`, `cash-flow-snapshot`, `close-month`, `content-strategy`, `contract-review`, `crm-cleanup`, `crm-maintenance`, `customer-pulse`, `customer-pulse-check`, `friday-brief`, `handle-complaint`, `invoice-chase`, `job-post-builder`, `lead-triage`, `margin-analyzer`, `monday-brief`, `month-end-prep`, `month-heads-up`, `plan-payroll`, `price-check`, `quarterly-review`, `review-contract`, `run-campaign`, `sales-brief`, `smb-onboard`, `smb-router`, `tax-prep`, `tax-season-organizer`, `ticket-deflector` |

Total: **17 source packages and 141 skill files**. `pdf-viewer` has a source manifest but was not listed in the inspected marketplace. Partner-built additions are excluded. Anthropic Design covers accessibility, critique, handoff, systems, research and UX copy; it complements the standalone visual-production skills.

## Anthropic Claude Code plugins

The official repository explicitly distinguishes its Anthropic-maintained `plugins/` from third-party `external_plugins/`. The following entries are local first-party marketplace sources. A plugin with no SKILL.md may provide commands, hooks, agents, output styles or a language server.

| Marketplace package | Skill files under its skills directory |
|---|---|
| [agent-sdk-dev](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/agent-sdk-dev) | No SKILL.md; inspect other plugin components. |
| [clangd-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/clangd-lsp) | No SKILL.md; inspect other plugin components. |
| [claude-code-setup](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/claude-code-setup) | `claude-automation-recommender` |
| [claude-md-management](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/claude-md-management) | `claude-md-improver` |
| [claude-security](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/claude-security) | `claude-security` |
| [code-modernization](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/code-modernization) | No SKILL.md; inspect other plugin components. |
| [code-review](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/code-review) | No SKILL.md; inspect other plugin components. |
| [code-simplifier](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/code-simplifier) | No SKILL.md; inspect other plugin components. |
| [commit-commands](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/commit-commands) | No SKILL.md; inspect other plugin components. |
| [csharp-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/csharp-lsp) | No SKILL.md; inspect other plugin components. |
| [cwc-makers](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/cwc-makers) | `cardputer-buddy`, `m5-onboard` |
| [explanatory-output-style](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/explanatory-output-style) | No SKILL.md; inspect other plugin components. |
| [feature-dev](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/feature-dev) | No SKILL.md; inspect other plugin components. |
| [frontend-design](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/frontend-design) | `frontend-design` |
| [gopls-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/gopls-lsp) | No SKILL.md; inspect other plugin components. |
| [hookify](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/hookify) | `writing-rules` |
| [jdtls-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/jdtls-lsp) | No SKILL.md; inspect other plugin components. |
| [kotlin-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/kotlin-lsp) | No SKILL.md; inspect other plugin components. |
| [learning-output-style](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/learning-output-style) | No SKILL.md; inspect other plugin components. |
| [lua-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/lua-lsp) | No SKILL.md; inspect other plugin components. |
| [math-olympiad](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/math-olympiad) | `math-olympiad` |
| [mcp-server-dev](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/mcp-server-dev) | `build-mcp-app`, `build-mcp-server`, `build-mcpb` |
| [mcp-tunnels](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/mcp-tunnels) | No SKILL.md; inspect other plugin components. |
| [php-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/php-lsp) | No SKILL.md; inspect other plugin components. |
| [playground](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/playground) | `playground` |
| [plugin-dev](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/plugin-dev) | `agent-development`, `command-development`, `hook-development`, `mcp-integration`, `plugin-settings`, `plugin-structure`, `skill-development` |
| [pr-review-toolkit](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/pr-review-toolkit) | No SKILL.md; inspect other plugin components. |
| [project-artifact](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/project-artifact) | `project-artifact` |
| [pyright-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/pyright-lsp) | No SKILL.md; inspect other plugin components. |
| [ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/ralph-loop) | No SKILL.md; inspect other plugin components. |
| [receipts](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/receipts) | `receipts` |
| [ruby-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/ruby-lsp) | No SKILL.md; inspect other plugin components. |
| [rust-analyzer-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/rust-analyzer-lsp) | No SKILL.md; inspect other plugin components. |
| [security-guidance](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/security-guidance) | No SKILL.md; inspect other plugin components. |
| [session-report](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/session-report) | `session-report` |
| [skill-creator](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/skill-creator) | `skill-creator` |
| [swift-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/swift-lsp) | No SKILL.md; inspect other plugin components. |
| [typescript-lsp](https://github.com/anthropics/claude-plugins-official/tree/f0dce59fec064db10450cb6ed6e33c1080d61537/plugins/typescript-lsp) | No SKILL.md; inspect other plugin components. |

**38 marketplace packages**; this is not a skill count. Unlisted example scaffolds and all external-plugin entries are excluded. `frontend-design` and `skill-creator` overlap with the standalone repository.

## OpenAI public first-party plugins

The entries below have OpenAI/OpenAI Codex manifest attribution, or are Data/Creative Production packages corroborated by the [official role-plugin announcement](https://openai.com/index/codex-for-every-role-tool-workflow/). The announcement establishes provenance; its launch totals are not used as current catalogue counts. Component-level authorship is not fully audited.

| Plugin / pinned source | Version | Skill files | Contained skill paths |
|---|---|---|---|
| [build-ios-apps](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/build-ios-apps) | 0.1.2 | 9 | `ios-app-intents`, `ios-debugger-agent`, `ios-ettrace-performance`, `ios-memgraph-leaks`, `ios-simulator-browser`, `swiftui-liquid-glass`, `swiftui-performance-audit`, `swiftui-ui-patterns`, `swiftui-view-refactor` |
| [build-macos-apps](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/build-macos-apps) | 0.1.4 | 11 | `appkit-interop`, `build-run-debug`, `liquid-glass`, `packaging-notarization`, `signing-entitlements`, `swiftpm-macos`, `swiftui-patterns`, `telemetry`, `test-triage`, `view-refactor`, `window-management` |
| [build-web-apps](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/build-web-apps) | 0.1.2 | 6 | `frontend-app-builder`, `frontend-testing-debugging`, `react-best-practices`, `shadcn-best-practices`, `stripe-best-practices`, `supabase-best-practices` |
| [build-web-data-visualization](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/build-web-data-visualization) | 0.1.21 | 18 | `accessibility-and-inclusive-visualization`, `canvas2d-data-visualization`, `d3-data-visualization`, `dashboards-and-real-time-visualization`, `data-visualization`, `gantt-chart-visualization`, `geospatial-and-cartographic-visualization`, `grammar-of-graphics-and-declarative-visualization`, `node-link-and-diagram-layout`, `react-and-nextjs-data-visualization`, `reports-pdfs-and-slide-automation`, `scrollytelling-and-parallax-data-visualization`, `statistical-and-uncertainty-visualization`, `testing-data-visualizations`, `threejs-data-visualization`, `typescript-data-visualization-engineering`, `uml-and-software-architecture-visualization`, `visualization-strategy-and-critique` |
| [codex-security](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/codex-security) | 0.1.24 | 15 | `assess-patch-risk`, `attack-path-analysis`, `deep-security-scan`, `define-security-policy`, `finding-discovery`, `fix-finding`, `propose-security-hardening`, `security-diff-scan`, `security-scan`, `threat-model`, `track-findings`, `triage-finding`, `validation`, `verify-fix`, `vulnerability-writeup` |
| [creative-production](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/creative-production) | 0.1.25 | 2 | `intake`, `produce` |
| [data-analytics](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/data-analytics) | 0.2.8 | 18 | `analyze-data-quality`, `build-dashboard`, `build-report`, `build-report/report-to-google-doc`, `build-report/report-to-google-slides`, `build-report/report-to-pdf`, `create-data-context`, `design-kpis`, `gather-business-context`, `index`, `jupyter-notebooks`, `kpi-reporting`, `market-sizing`, `metric-diagnostics`, `product-business-analysis`, `publish-artifact-to-sites`, `validate-data`, `visualize-data` |
| [game-studio](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/game-studio) | 0.1.2 | 9 | `game-playtest`, `game-studio`, `game-ui-frontend`, `phaser-2d-game`, `react-three-fiber-game`, `sprite-pipeline`, `three-webgl-game`, `web-3d-asset-pipeline`, `web-game-foundations` |
| [github](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/github) | 0.1.11 | 0 | No SKILL.md; inspect other plugin components. |
| [gmail](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/gmail) | 0.1.9 | 0 | No SKILL.md; inspect other plugin components. |
| [google-calendar](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/google-calendar) | 1.2.6 | 0 | No SKILL.md; inspect other plugin components. |
| [google-drive](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/google-drive) | 0.1.15 | 5 | `google-docs`, `google-drive`, `google-drive-comments`, `google-sheets`, `google-slides` |
| [life-science-research](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/life-science-research) | 1.0.3 | 50 | `alphafold-skill`, `bgee-skill`, `bindingdb-skill`, `biobankjapan-phewas-skill`, `biorxiv-skill`, `biostudies-arrayexpress-skill`, `cbioportal-skill`, `cellxgene-skill`, `chebi-skill`, `chembl-skill`, `civic-skill`, `clinicaltrials-skill`, `clinvar-variation-skill`, `efo-ontology-skill`, `encode-skill`, `ensembl-skill`, `epigraphdb-skill`, `eqtl-catalogue-skill`, `eva-skill`, `finngen-phewas-skill`, `genebass-gene-burden-skill`, `gnomad-graphql-skill`, `gtex-eqtl-skill`, `gwas-catalog-skill`, `hmdb-skill`, `human-protein-atlas-skill`, `ipd-skill`, `locus-to-gene-mapper-skill`, `metabolights-skill`, `mgnify-skill`, `ncbi-blast-skill`, `ncbi-clinicaltables-skill`, `ncbi-datasets-skill`, `ncbi-entrez-skill`, `ncbi-pmc-skill`, `opentargets-skill`, `pharmgkb-skill`, `pride-skill`, `proteomexchange-skill`, `pubchem-pug-skill`, `quickgo-skill`, `rcsb-pdb-skill`, `reactome-skill`, `research-router-skill`, `rhea-skill`, `rnacentral-skill`, `string-skill`, `tpmi-phewas-skill`, `ukb-topmed-phewas-skill`, `uniprot-skill` |
| [ngs-analysis](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/ngs-analysis) | 1.0.3 | 18 | `ngs-amplicon-microbiome`, `ngs-analysis-router`, `ngs-atacseq-peaks-qc`, `ngs-bcl-to-fastq`, `ngs-bulk-rnaseq`, `ngs-bulk-rnaseq-counts-qc`, `ngs-bulk-rnaseq-differential-expression`, `ngs-chip-cutrun-peaks-qc`, `ngs-dna-germline-variants`, `ngs-dna-somatic-variants`, `ngs-dna-umi-panel-variants`, `ngs-dna-variant-calling`, `ngs-epigenomics-peaks`, `ngs-fastq-qc`, `ngs-runtime-env`, `ngs-scrna-seq`, `ngs-shotgun-metagenomics`, `scrna-seq-qc` |
| [openai-ads-conversions](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/openai-ads-conversions) | 0.1.2 | 1 | `openai-ads-conversions-setup` |
| [openai-developers](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/openai-developers) | 1.2.3 | 5 | `agents-sdk`, `build-chatgpt-app`, `chatgpt-app-submission`, `openai-api-troubleshooting`, `openai-platform-api-key` |
| [outlook-calendar](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/outlook-calendar) | 0.1.8 | 0 | No SKILL.md; inspect other plugin components. |
| [outlook-email](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/outlook-email) | 0.1.7 | 0 | No SKILL.md; inspect other plugin components. |
| [plugin-eval](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/plugin-eval) | 0.1.2 | 5 | `evaluate-plugin`, `evaluate-skill`, `improve-skill`, `metric-pack-designer`, `plugin-eval` |
| [product-design](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/product-design) | 0.1.52 | 10 | `audit`, `design-qa`, `get-context`, `ideate`, `image-to-code`, `index`, `research`, `share`, `url-to-code`, `user-context` |
| [public-equity-investing](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/public-equity-investing) | 0.1.31 | 23 | `catalyst-calendar`, `company-tearsheet`, `comps-valuation`, `dcf-model-builder`, `deck-report-qc`, `earnings-deep-dive`, `earnings-preview`, `economic-impact-report`, `equity-model-update`, `event-driven-analyzer`, `financials-normalizer`, `idea-generation`, `initiating-coverage`, `long-short-pitch`, `meeting-prep`, `memo-builder`, `model-audit-tieout`, `portfolio-risk-management`, `public-equity-investing`, `scenario-sensitivity-generator`, `thesis-tracker`, `three-statement-model-builder`, `user-context` |
| [sentry](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/sentry) | 0.1.2 | 1 | `sentry` |
| [sharepoint](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/sharepoint) | 0.1.7 | 0 | No SKILL.md; inspect other plugin components. |
| [teams](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/teams) | 0.1.8 | 0 | No SKILL.md; inspect other plugin components. |
| [test-android-apps](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/test-android-apps) | 0.1.2 | 2 | `android-emulator-qa`, `android-performance` |
| [zotero](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins/zotero) | 0.1.2 | 1 | `zotero` |

**26 first-party public packages** under this attribution rule. App-only integrations are included to make the packaging boundary visible; zero skill files does not mean zero functionality. External service access can require separate authentication and permissions. Marketplace product fields specifically identify Codex for some packages, including `plugin-eval` and `build-web-data-visualization`; source availability is not universal ChatGPT availability.

## OpenAI runtime and locally observed packages

Local package manifests provide additional first-party evidence beyond the public repositories. Versions below identify the inspected cache; session exposure is a separate, narrower observation. No private account settings were inspected.

| Package | Observed version | Relevant scope and availability evidence |
|---|---|---|
| documents, pdf, presentations | 26.909.12148 | Each has an OpenAI manifest and corresponding skill exposed in this Codex session. |
| spreadsheets | 26.909.12148 | `spreadsheets` and `excel-live-control` exposed; standalone-file and live-app workflows differ. |
| template-creator | 26.909.12148 | Personal artifact-template creation skill exposed. |
| sites | 0.1.66 | `sites-building`, `sites-hosting` exposed. |
| visualize | 1.0.37 | Inline visualisation skill exposed. |
| deep-research-work | 0.1.15 | `deep-research` exposed, with an explicit deep-research activation boundary. |
| sales | 1.1.0-alpha.2 | 18 source skill files; index entry point exposed. |
| investment-banking | 0.1.29 | 23 source skill files; routing entry point exposed. |
| public-equity-investing | 0.1.31 | 23 source skill files; routing entry point exposed; also in public source above. |
| data-analytics | 1.0.8 | 20 cached skill files; selected workflows exposed. Different version/layout from public 0.2.8. |
| product-design | 0.1.55 | 10 cached skill files; selected entry points exposed. Public snapshot is 0.1.52. |
| creative-production; codex-security | 0.1.25; 0.1.24 | Exposed workflows and matching public package versions; file parity not established. |
| openai-developers | 1.3.0 | Local `agents` entry differs from public 1.2.3 `agents-sdk`; do not assume parity. |
| openai-templates | 0.1.1 | 20 artifact-template skill files cached, including reports, memoranda, letterhead, business reviews and dashboards. Not exposed in this session. |
| plugin-management | 0.1.0 | First-party package-management skill exposed. |
| codex-app-tools | 0.1.4 | First-party app tools; no skill required for the package to be useful. |

The session also exposes system skills `imagegen`, `openai-docs`, `plugin-creator`, `skill-creator` and `skill-installer`. Local runtime dependencies and tool contracts must be retained when assessing portability. Copying a SKILL.md alone does not reproduce these packages.

OpenAI separately [documents education plugins](https://openai.com/index/learn-teach-chatgpt-work-codex/) for K–12 Educator, College Educator and College Student. Treat these as officially documented offerings with account/workspace conditions; their package IDs, constituent skills and availability in Andrew’s account were not verified here.

## Mixed catalogues and exclusions

- `openai/skills` is a lab-maintained catalogue, not blanket proof of OpenAI authorship. Its four `notion-*` skills carry Notion Labs copyright; `playwright` and `playwright-interactive` carry Microsoft attribution; `vercel-deploy` carries Vercel attribution. These are excluded from the exclusively lab-authored shortlist. Other generic licence templates do not by themselves prove authorship; unresolved entries remain references pending attribution checks.
- OpenAI marketplace plugins authored by Adobe, Canva, Figma, Vercel, third-party researchers and other partners are excluded. Notion and Slack plugin manifests have mixed author/contact signals and are not counted as confirmed first-party packages.
- The installed `no-ai-slop` manifest names **Peter Yang**. It is not an OpenAI skill, despite appearing in this Codex session. Humanizer, Impeccable, Frontend Slides, Visual Explainer, Kepano and K-Dense remain third-party sources outside this validation.
- Anthropic marketplace inclusion or an Anthropic Verified badge is a review/distribution signal, not proof of Anthropic authorship. Partner-built plugins, including external brand-voice offerings, are excluded.

No dedicated general-purpose first-party “AI slop removal” skill was identified in the audited sources. Relevant first-party editorial components include Anthropic `doc-coauthoring`, Design `ux-copy`, and Marketing `brand-review`; these are adjacent capabilities, not validated substitutes for a general editor. Personal `my-voice` remains a separately authored kit component.

## Combined capability shortlist

| Need | Anthropic first-party candidates | OpenAI first-party candidates | Implementation implication |
|---|---|---|---|
| Research and synthesis | Enterprise Search; Design research-synthesis; Product Management synthesize-research | Deep Research; Data analysis/report workflows | Select by research job and accessible sources; avoid duplicate orchestration. |
| Web design | frontend-design; Design; canvas-design; theme-factory | Product Design; Sites; build-web-apps | Separate visual direction, implementation and QA. |
| Presentations and documents | pptx/docx/pdf; doc-coauthoring; theme-factory | Presentations/Documents/PDF runtimes; Creative Production; template-creator | Compare native runtime plus suitable reference before importing the other lab’s mechanics. |
| Visual explanation and charts | Data create-viz/data-visualization; algorithmic-art where relevant | visualize; Data; build-web-data-visualization | Pick medium and evidence requirements before choosing package. |
| Editorial quality | doc-coauthoring; ux-copy; brand-review | Native editing and artifact workflows; no dedicated general editor verified | Test concrete defects; preserve ownership and personal voice. |
| Skill improvement and context cost | skill-creator; discernment-nudge as a boundary-overlap review candidate | skill-creator; plugin-creator; plugin-eval | Keep evaluation machinery outside ordinary task context. |

## Plugin-aware implementation record

Plugins belong within the existing implementation layer; they do not require a new authority layer. Record each deployment as **capability → publisher → package and revision → skill entry point → target client/surface**. Also record other components (apps/MCP, hooks, commands, agents, scripts, templates), required tools/authentication, installation scope, enabled state, actually exposed/loaded entry points, licence/provenance, constitution intersections and measured outcome/cost. A package may expose tools without skills, or many source skills through a single router.

Use the [OpenAI plugin documentation](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex) and [Claude directory documentation](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory) to verify client-specific distribution. Common SKILL.md structure does not transfer plugin manifests, permissions, hooks or service integrations between clients.

OpenAI `plugin-eval` is especially relevant to token efficiency: its source includes static review, budget explanation and measurement planning, plus live Codex benchmarking. Static file-size/budget analysis is not measured token savings. Live comparisons require a pinned setup and actual usage/outcome records. No benchmarks or installation were performed for this inventory.

Next validation is a bounded native-versus-one-candidate trial on recurring work, after a complete package review. First-party provenance raises confidence about source identity; it does not establish that the workflow is best, sufficiently tested for this kit, or compatible with the constitution.
