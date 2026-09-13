← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Skills](README.md) · **Implementation plan**

# Implementing the Selected Capabilities

Use a small provider-native catalogue to configure Claude and Codex consistently for thinking and useful output. The [catalogue](README.md) owns the selections; [Claude](../platforms/claude/configuration-baseline.md) and [Codex](../platforms/codex/configuration-baseline.md) own delivery and observed state. The constitution, authored voice skill and existing knowledge system retain their roles.

**Status: repository simplification completed; current Claude Customize lists reconciled on 13 September 2026.** The [snapshot](../../../governance/evidence/2026-09-claude-customize-snapshot.md) records seven listed plugins, 39 Skills-page entries, two connected connectors, five added marketplaces and six Anthropic sources. A follow-up confirms Obsidian 1.0.1 enabled with six skills, closing that initial gap. All eight selected plugins are evidenced across the views; 45 entries is the aggregate of 39 plus six, not a refreshed single-list count. Other enable switches, automatic updates and runtime behaviour remain unverified; Codex deployment remains unverified.

## Agreed scope

- Retain native document, spreadsheet, presentation, PDF, search and visual capabilities.
- Use Anthropic's own published skills within Claude and OpenAI's within Codex. Do not cross-deploy provider packages for symmetry.
- Give selected Data and Design plugins an On target, including Claude's dedicated frontend-design plugin; retain Claude PDF Viewer On. In Claude, all skills in an enabled plugin are available. Use native drafting and leave unselected provider packages Off.
- Park `my-voice`. Impeccable, i-have-adhd, Taste Skill and Obsidian are recorded independent third-party selections, with all four evidenced in Claude, including Obsidian 1.0.1 explicitly enabled in the follow-up screenshot. Assess further additions individually; shared deployment requires useful fit and supported delivery on each harness.
- Harmonise output standards and operating boundaries. Package names, distribution mechanisms and native runtime internals can differ.

## 1. Repository configuration — implemented

| Owner | Implemented change |
|---|---|
| [Skills catalogue](README.md) | One maintained selection list with upstream provenance, On/Off choices and platform links. |
| [Review method](review-method.md), [authoring guidance](best-practices.md) | Proportionate source, configuration and real-use checks. Comparative evaluation is reserved for uncertainty. |
| [Claude baseline](../platforms/claude/configuration-baseline.md), [Codex baseline](../platforms/codex/configuration-baseline.md) | Adopted target separated from verified deployment; concrete controls and unresolved surface limits. |
| [Implementation index](../README.md), [platform index](../platforms/README.md), [deployment map](../platforms/deployment-map.md), [Claude index](../platforms/claude/README.md), [Code guide](../platforms/claude/code/README.md), [Codex guide](../platforms/codex/README.md) | Navigation and the relationship between instruction deployment and capability configuration. |
| [Current architecture](../../../governance/current-architecture.md), [design decisions](../../../governance/design-decisions.md) | Canonical ownership and the superseding file-level decision. |
| [Framework layer model](../../../framework/layer-model.md), [adoption guide](../../../framework/adoption-guide.md) | Generic lesson: prefer the provider-native route and scale adoption checks to the decision. |
| [Eval index](../../evals/README.md) | Existing capability examples remain unexecuted and reusable, without a compulsory full pilot. |

The [capability matrix](capability-matrix.md), [package register](package-register.md) and [source register](source-register.md) have historical notices; their original contents remain available. The [first-party inventory](first-party-inventory.md) is unchanged dated evidence, including its local observations. No files are deleted, renamed or moved. There is no new marketplace, registry format, runtime router or installation automation.

The constitution, shared contract sources, generated contract bodies, voice files, skill template, eval fixtures and unrelated working-tree changes are outside this edit batch. Platform wrappers can change without altering generated contract text.

## 2. Prepare the live change — pending

Start with Claude Desktop Chat/Cowork and Codex desktop, the primary thinking surfaces. Inspect Claude Code separately; do not infer Code configuration from Chat/Cowork. Other Codex surfaces and ChatGPT are not implicitly deployment targets.

Read actual settings to determine the **delta from the target**, not to rediscover which skills exist. For the selected additions, resolve the public source revision and verify supported delivery, package boundaries, account availability and dependencies. For native features with opaque revisions, record that limit.

Produce one concrete change list: target surface and scope, current state, desired state, exact skill/plugin identity, control to use, dependency impact, verification and restoration route. A package already off needs no mutation. A selected native feature already supplied needs no duplicate installation.

Configure real On/Off states. A disabled Claude plugin is unavailable to select in chat; enabling one makes all its skills available. Assess complete plugins and keep the selected set enabled, rather than prescribing per-job settings changes. Verify other harness controls separately. Use managed provider delivery and update controls; leave unavailable additions undeployed instead of copying or patching provider files.

The live batch must name any necessary installation or setting changes and the location of verification outputs/evidence. Resolve material account, access or spending choices only if the selected work needs them. Approval to implement this repository batch does not authorise those later live actions.

## 3. Apply and verify the live change — pending

Apply the exact authorised delta. Preserve unrelated tools, account connections, permissions, memory and working files. Use native distribution routes; do not overwrite provider-managed caches or uninstall packages merely to reduce the installed count.

Verify saved state, discovery and actual use in fresh sessions. Check one representative native file output, an exploratory request where optional workflows should stay inactive, and a matching task for each optional package being activated. Inspect rendered output and source fidelity; test calculations or editability where requested. Select additional [fixtures](../../evals/README.md) only for an unresolved concern.

If value or interference remains uncertain, compare the native route and the addition on the same task. There is no requirement to multiply every package by every harness or run the former complete pilot before useful configuration changes.

Record the material results in one dated governance evidence file, chosen and indexed with that batch. Update both baselines with verified surface/version, saved controls, tested behaviour and remaining unknowns. Do not convert a UI toggle or valid file into a broader quality or token-saving claim.

Keep a restoration route for the settings changed. Vendor-managed native versions may not be pinnable or recoverable; fallback can be disabling the optional addition and using the retained native workflow. State that limit instead of promising full runtime rollback.

## 4. Refine through use — ongoing after deployment

Use repeated value, correction effort and unwanted activation to retain or narrow the selected set. Record usage where the host exposes it, without estimates from file size or package count. Revisit after meaningful model/package/host changes; avoid a standing review programme for every skill.

Independent-skill selection has begun with Impeccable and Taste Skill for design, i-have-adhd for interaction formatting, and Obsidian for knowledge work. The screenshots show the first three plugins; a follow-up confirms Obsidian 1.0.1 enabled with all six skills. Codex deployment and comparative quality are not established. Further candidates should have credible GitHub usage, maintained tests/examples and a clear use case, then be configured on each harness as needed. `my-voice` remains a separate, straightforward authored deployment concern.

## Verification of this repository batch

The read-only contract distribution check passed before and after editing: all seven generated copies are current. Both edited agent-guide wrappers retain their generated bodies and metadata byte for byte. All 634 checked repository Markdown file/anchor links resolve; the new Codex baseline is indexed by its parent and the platform index. Whitespace checks pass.

A comparison with the pre-batch working-tree snapshot confirms 19 existing files changed and one new Codex baseline, all within the approved scope. All 92 other snapshotted repository files are unchanged, including the dated inventory, constitution, voice files, template, eval fixtures and unrelated existing edits. Changes to the three historical registers are limited to their notices. Review of the overlapping framework/governance files confirms the earlier edits were preserved; framework additions contain no personal identifiers, provider selections or checkout paths.

These are static checks. No live trials, settings changes, installations, commits or publication occurred in this repository batch. Output quality, activation behaviour and token savings remain unmeasured for the new target.

## Prior preparation

The earlier Batch 1 on 13 September 2026 created a 24-record package register, aligned capability research and authored synthetic composition fixtures. Its reported static checks passed, including seven generated contracts; it performed no behavioural trials or new package deployments. Git history retains that plan and its detailed scope.

This simplification supersedes that plan's mandatory multi-stage pilot and active matrix/register ownership. It preserves the earlier records as history and uses the selected catalogue plus platform baselines for future work.
