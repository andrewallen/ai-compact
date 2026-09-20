← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-013**

# ADR-013: Publish generated plugins through a shared marketplace

**Status:** Accepted

## Context

The maintained my-voice skill is a four-file implementation capability. The initial Agent Plugins wrapper generated a local ZIP, but a GitHub marketplace needs a complete fetchable package and update identity. Andrew requested marketplace distribution across Claude, GitHub Copilot and Codex with publication when source changes reach GitHub.

## Decision

Keep canonical craft in `kit/implementation/skills/my-voice/` and packaging sources in `kit/implementation/plugins/`. Maintain a shared `.claude-plugin/marketplace.json` at the source repository root. It points to the generated plugin at the root of `codex/plugin-marketplace`, allowing hosts to add the ordinary repository URL.

Generate a portable root manifest and a Claude compatibility manifest from the same metadata. Current Codex and GitHub Copilot support the portable root manifest and the shared catalogue location; no separate craft or native Codex catalogue is maintained. Carry the existing licence, attribution, source revision and file hashes with each complete package.

GitHub Actions validates changes and publishes changed payloads after successful checks on `main`. Each release receives a generated `0.1.<workflow run number>` package version, an immutable `my-voice-v<version>` tag and a commit on the distribution branch. No force-pushes are used. Payload comparison skips identical releases, and remote-main checks reject obsolete runs. Rollback is a new release from reverted source.

Generated package versions are a narrow exception to the document-marker policy: they identify distributed content for host update detection. Maintained skill documents continue relying on Git history. The schema identifier identifies the package format, not its content revision.

## Consequences

- The source branch retains the three content domains. Root catalogue and workflow files are packaging infrastructure.
- The distribution branch is generated output, never a second authoring location or a fourth content domain.
- Host updates remain host-controlled. Publishing a plugin does not install it, supply the constitution or establish correct invocation and behaviour.
- The catalogue follows a release branch without a version pin; generated manifests supply the actual release identity.
- Account settings, removed standalone skills and existing deployments remain unchanged by publication.
- The public marketplace is not Claude's private organisation-managed sync route.

## Alternatives considered

- **Manual ZIP replacement:** retained as an export option, but does not meet the requested marketplace-update workflow.
- **Hand-maintained copies per host:** rejected because they create competing craft owners and version drift.
- **Generated files committed into main after every build:** rejected because it creates bot commits in the source history and requires additional loop prevention.
- **A separate distribution repository:** unnecessary for a single personal plugin; reconsider if ownership or access requirements diverge.
- **One self-updating script inside the skill:** rejected because installation, trust and activation belong to hosts and their update mechanisms.
