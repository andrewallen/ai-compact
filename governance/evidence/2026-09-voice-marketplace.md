← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Voice marketplace**

# Voice marketplace implementation

## Authorised scope and plan

Andrew requested a plan and implementation of marketplace distribution and updates for my-voice across Claude, GitHub Copilot and Codex. The earlier commit-and-push instruction applies to this continuation. Account installation and enablement remain separate; the removed standalone Codex skill stays absent.

1. Retain the four canonical skill files and generate a complete portable package, a Claude compatibility manifest, licence and provenance.
2. Add a shared catalogue on the default branch, pointing at a generated plugin at the root of `codex/plugin-marketplace`. This permits adding the ordinary repository URL in each host.
3. Validate pull requests and pushes. Publish only from this repository's `main` after checks pass, using automatic package versions, immutable tags and ordinary fast-forward branch history. Skip unchanged payloads and reject obsolete publication attempts.
4. Document host installation and updates, including personal Copilot auto-update, and preserve the distinction between publication, installation and behaviour.
5. Exercise packaging and release transitions in temporary repositories, validate host manifests, check documentation and publication hygiene, then commit, push and inspect the first release.

## Acceptance criteria

- Generated skill prose and companions exactly preserve canonical source; only the documented invocation frontmatter field is omitted.
- One complete generated package serves all hosts. All manifests agree on identity and version.
- Unchanged inputs produce identical files and ZIP bytes. Changed payloads receive a new package version; ordinary documentation-only commits do not republish an identical plugin.
- The release workflow cannot publish a pull request, overwrite a tag, force-push a branch or replace a newer release with an obsolete source revision.
- The catalogue can be added using the ordinary repository URL, and publication requires no account installation or secrets in the package.
- Automated checks establish package and release mechanics. Any untested host behaviour remains explicitly unverified.

## Results

Implemented the shared catalogue, deterministic directory/ZIP builder, Claude compatibility manifest, release publisher and GitHub Actions workflow. [ADR-013](../decisions/adr-013-generated-plugin-marketplace.md) records the generated distribution branch and package-version exception. The [installation guide](../../kit/implementation/plugins/my-voice/README.md) owns host setup and refresh commands.

Local validation before publication:

- Package-preservation and Git release tests run entirely in temporary directories and local bare repositories. They cover first publication, changed-content updates, unchanged reruns and documentation-only commits, stale source revisions, immutable tags, version progression, tampered output, unexpected files and symlinks, manifest types and invocation-metadata drift.
- Both source and generated portable manifests pass the official Agent Plugins 1.0.0 JSON Schema using jsonschema 4.25.1.
- Claude Code 2.1.278 validates the shared marketplace without warnings and the generated compatibility manifest in strict mode without warnings.
- actionlint 1.7.12 validates the workflow. Its downloaded binary was checked against the publisher's release checksum. Workflow action references are pinned to verified upstream commit SHAs.
- Relative Markdown links, whitespace, generated-file freshness and the anonymised framework addition are checked. A scoped scan finds no credentials, private account paths or third-party contact details in the new distribution material.

The earlier assessment's uncertainty about personal Copilot CLI auto-update is resolved by its [detailed reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference): a user-level `extraKnownMarketplaces` entry can set `autoUpdate: true`. This setting is documented, not applied to Andrew's account. Personal Codex automatic refresh and personal Claude Desktop refresh cadence remain unverified; their guides state this boundary.

Live publication verification is pending the implementation push. No account plugin is installed or enabled by this work. The standalone Codex skill remains absent. No new behavioural score is claimed: the four canonical skill files are unchanged, and packaging checks establish exact preservation rather than model adherence.
