← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Platforms](../README.md) · [Codex](README.md) · **Configuration baseline**

# Codex Configuration Baseline

The adopted capability target for Codex desktop as a thinking, output and engineering harness. The [skills catalogue](../../skills/README.md) owns the selections and upstream provenance; this guide owns configuration and its verification limits. It is maintenance material, not a runtime instruction set.

## Status and scope

**Target adopted on 13 September 2026; live deployment unverified.** This repository batch did not inspect or modify Codex settings, install packages or exercise the selected workflows. The currently exposed session skills and local cache are not the source of truth for identifying published offerings.

Start live harmonisation with Codex desktop. CLI, IDE, cloud and ChatGPT settings are separate targets; no parity is inferred from a shared account or model. Actual controls depend on product surface, account, workspace and rollout.

| State to establish during deployment | Current evidence |
|---|---|
| Actual desktop version, mode and available controls | Not inspected for this batch. |
| Native file and visual capabilities available on the target | Documented product capabilities; actual target availability unverified. |
| Optional packages installed, enabled and exposed | Unverified; the target catalogue is not an installed inventory. |
| Selected source revision and installed parity | Resolve during live preparation; native runtime revisions may be opaque. |
| Positive invocation, inactive exploratory use and output quality | Not tested. |
| Usage or token savings | Not measured. |

## Target capability configuration

| Capability | Target | Delivery and scope |
|---|---|---|
| Documents, spreadsheets, presentations and PDFs | On | Retain supplied OpenAI workflows where available. Do not import Anthropic's document skills or add duplicate public copies to a working native route. |
| Search, source analysis and visual explanation | On | Retain native tools for relevant work. Select any specialised research mode deliberately for substantial research. |
| Image work | On | Retain supplied OpenAI image generation; the public source is [imagegen](https://github.com/openai/skills/tree/main/skills/.system/imagegen). |
| Quantitative analysis and data reports | On | OpenAI [Data Analytics](https://github.com/openai/plugins/tree/main/plugins/data-analytics), package `data-analytics`. Simple spreadsheet operations remain native. |
| Design creation and critique | On | OpenAI [Product Design](https://github.com/openai/plugins/tree/main/plugins/product-design), package `product-design`; select the relevant creation or audit workflow. |
| Generic coauthoring | Native route | No additional generic coauthoring package selected; use the native document capability. |
| Other optional provider packages | Off for ordinary thinking/output work | Follow the catalogue's explicit off list. Optional engineering packages can be selected for a defined engineering task separately. |
| Supplied system utilities | Retain | Avoid duplicate authoring/install utilities; an optional security plugin is separate from host security controls. |
| Authored and independent third-party skills | Outside this batch | `my-voice` is parked; third-party selection and shared deployment are later work. |

OpenAI documents native document, spreadsheet and presentation entry points for Codex desktop in its [artifact guidance](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work), including composer mentions where available. PDF and image workflows are also described in the [Codex app introduction](https://openai.com/index/introducing-the-codex-app/). These product features need not correspond to public marketplace packages with matching names.

Use the [OpenAI public plugin manifest](https://github.com/openai/plugins/blob/main/.agents/plugins/marketplace.json) and package sources for published optional offerings. A marketplace can also include independent or partner-authored work; check attribution rather than treating every listed plugin as OpenAI-authored. Resolve the chosen revision before installation; a local same-named package does not establish source parity.

## Enablement and invocation controls

In a supported Codex task view, **Sources → Use plugins** lets the user select an installed plugin. Check actual availability and effect on the target surface. OpenAI's [plugin guidance](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex) distinguishes task selection, installation and app access; selecting a plugin does not by itself prove that other installed skills disappeared from discovery.

Data Analytics and Product Design have On targets so their capabilities are available. Verify enabled state and invocation separately. A task selection control is not a third configuration state, and selecting a workflow does not establish that other plugin skills are unavailable. Do not prescribe disabling the selected plugins between jobs or infer Codex controls from Claude.

The exact personal desktop enable/disable controls are **not yet verified**. Inspect the actual account before applying the targets. Workspace administrator controls are not a substitute for a personal setting and can affect other people. If a managed installation or enablement route is unavailable, leave the addition undeployed and record the limitation; do not manually upload provider copies, patch managed caches or claim that a prompt enforces isolation.

For a separately installed skill, OpenAI documents `policy.allow_implicit_invocation: false` in `agents/openai.yaml` as an explicit-invocation control. It is not a portable Claude setting or proof that discovery metadata is absent. Do not modify provider-managed packages to impose it; use supported host controls for the selected plugins. See [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills).

Keep connector accounts and permissions intact. Check required and shared apps before disabling a plugin; disabling an app can affect other workflows and does not necessarily remove the plugin's independent skills. Source access needed for research is a separate dependency choice.

## Deployment and verification

1. Inspect the actual desktop controls and compare saved settings with the catalogue's target. Prepare only the necessary changes, including source identity, package scope, dependencies and restoration route.
2. Apply the exact authorised live batch through supported native distribution and configuration. No cross-provider imports, duplicate native packages or local cache edits.
3. Start fresh and verify saved state and discovery. Record exposed metadata, loaded workflow and successful use separately where observable.
4. Check a representative native file output and an exploratory request that should keep optional production workflows inactive. Exercise a matching task for each optional package activated; inspect rendering, source fidelity and relevant calculations/editability.
5. Use a matched native-versus-addition comparison only for uncertain value or interference. Record repair effort and actual usage where available; no savings are inferred from installed counts.
6. Record material results once in dated [governance evidence](../../../../governance/evidence/README.md), link it here and replace unverified entries only with observed facts.

The [implementation plan](../../skills/implementation-plan.md) defines the remaining live batch; the [review method](../../skills/review-method.md) covers refinement through use. Restoration applies to the settings and optional packages changed. Vendor-managed native runtimes may not be pinnable or recoverable; record that limit.

Do not place credentials, exact trusted paths, account identifiers or private raw test material in this public guide. It records portable target choices and verification limits.

Version: 2026.09.13 @ 1.1

