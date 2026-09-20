← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Platforms](../README.md) · [Codex](README.md) · **Configuration baseline**

# Codex Configuration Baseline

Configuration guidance and known deployment gaps for Codex desktop. The [skills tracker](../../skills/README.md) records the adopted working set and source links. This guide is maintenance material.

## Current evidence

**Catalogue review, 13 September 2026; my-voice removal, 19 September 2026.** The earlier review inspected the supplied skill catalogue. The [voice maintenance record](../../../../governance/evidence/2026-09-voice-maintenance.md) documents an earlier four-file replacement. Following consolidation drift and the [plugin validation and repair](../../../../governance/evidence/2026-09-voice-plugin-validation.md), Andrew requested removal of the standalone local Codex skill. Its four files and directory were removed and absence verified. Other account settings and workflows were not changed.

| Component | Observation |
|---|---|
| Native file and visual workflows | Documents, Spreadsheets, Presentations, PDF, visualize and imagegen exposed in the review session. |
| Data Analytics and Product Design | Selected workflows exposed; exact public/local source parity unverified. |
| my-voice | Standalone local Codex installation removed on 19 September at Andrew's request; exact directory absence verified after preserving a temporary restoration copy. Canonical source and the generated Agent Plugins archive remain in the repo. No replacement plugin was installed. |
| Obsidian mechanics | Markdown, Bases, Canvas, CLI and Defuddle exposed; knap not exposed in this session. |
| Desktop settings and runtime behaviour | Enabled-state controls, intended invocation, output quality and usage not tested. |

Session exposure is narrower than verified deployment or use. CLI, IDE, cloud and ChatGPT remain separate targets.

## Setup and controls

Use the [Codex configuration reference](README.md) to supply the operating contract. Retain useful native file, search and visual workflows, and configure additions from the tracker through supported managed routes. Avoid duplicate provider copies and changes to managed caches. Public package attribution and local installation are separate checks.

The [OpenAI plugin guidance](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex) documents distribution and task selection. Verify actual desktop controls before changing them; task selection alone does not establish that other skills disappear from discovery. Do not infer Codex enablement controls from Claude or substitute workspace-wide settings for a personal control.

The [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills) covers separately installed skills and their invocation configuration. Keep personal source packages distinct from provider-managed installations. Preserve shared connector accounts and permissions when changing a plugin.

## Outstanding deployment work

- Leave the standalone my-voice installation absent unless Andrew requests a new deployment. The [marketplace guide](../../plugins/my-voice/README.md) now defines the generated plugin's install and refresh route; this does not record an account installation. The [marketplace evidence](../../../../governance/evidence/2026-09-voice-marketplace.md) distinguishes packaging and release checks from host discovery and use. Existing sessions may retain material loaded before removal. The recorded text probes supplied the package explicitly and do not establish installed invocation.
- Verify saved desktop settings and supported controls for the adopted packages. Confirm independent-skill deployments individually; presence on Claude does not establish presence on Codex.
- Exercise relevant workflows where useful, including an unrelated exploratory request when unwanted activation is a concern. Compare alternatives only when value or interference remains uncertain.
- Record material deployment results once in [governance evidence](../../../../governance/evidence/README.md), linking them here and updating the tracker.

A live change needs exact targets and a restoration route. Vendor-managed runtime versions may not be recoverable. Keep private paths, credentials and raw account material outside this guide; package count and file size do not establish token savings.

Version: 2026.09.20 @ 1.6
