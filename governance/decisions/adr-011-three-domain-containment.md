← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-011**

# ADR-011 — Contain the personal kit within a three-domain repository

**Status:** Accepted (2026-07-13)

## Context

ADR-010 aligned the filesystem to the five-layer model and deliberately rejected a `kit/` or `instance/` wrapper as unnecessary path ceremony. Reviewing that completed structure against human navigation exposed a different problem: the repository's intellectual boundary is not the same as its layer boundary.

There are three reader-facing domains:

1. the generic, anonymised framework that another practitioner could adopt;
2. the personal kit that instantiates that framework; and
3. the governance material that describes the current architecture, records decisions, preserves evidence and explains change.

The completed Phase 5 tree contains the framework and governance domains, but spreads the personal kit across five root-level directories. It also overloads “implementation”: the word can mean the complete personal instance or layer 4 specifically. Evals sit as a further root peer even though the active fixtures verify the personal instance.

“Architecture” is not a clean fourth content domain. The generic architecture belongs in the framework; the current instantiated topology and concise evidence records belong in governance.

## Decision

Adopt three top-level content domains:

```text
<repository-root>/
├── framework/                   generic, anonymised specification
├── kit/                         personal instance
│   ├── philosophy/              layer 1
│   ├── constitution/            layer 2
│   ├── roles/                   layer 3
│   ├── implementation/          layer 4
│   │   ├── platforms/
│   │   ├── skills/
│   │   └── prompts/
│   └── evals/                   active verification of the instance
└── governance/                  current architecture, decisions and provenance
```

Memory remains layer 5 and remains outside the repository. Repository-maintenance files stay at the root because they govern work on all three domains.

The canonical documentation split is:

- `framework/layer-model.md` defines the generic architecture;
- `kit/README.md` explains how the personal instance implements the framework;
- `governance/current-architecture.md` describes how the framework, personal kit, external memory, platforms and tooling currently relate;
- the root README orients readers and routes them to those sources rather than becoming a competing architecture specification.

Active eval fixtures move with the personal kit. A material completed change cycle may produce a concise governance evidence record; raw transcripts remain outside the public baseline.

Repository navigation uses relative Markdown links and `Home` as the root breadcrumb label. It must not depend on the repository's current name or an absolute local path.

ADR-010 remains the record of the Phase 5 alignment. This decision supersedes only its rejection of a wrapper and its placement of the five personal directories at the root. The five-layer model, shallow structure within each layer and governance boundary remain in force.

## Consequences

- The repository root exposes its three intellectual domains without requiring the root README to explain away a flat set of mixed-purpose folders.
- The complete personal instance can be named unambiguously as “the kit”; “implementation” refers only to layer 4.
- Runtime and deployment paths gain one stable `kit/` prefix. Uploaded filenames do not change, but local imports, platform guidance and external hard-coded paths require a cascade update.
- Documentation and breadcrumb repair happens after the move so indexes describe final paths once.
- Framework anonymisation remains mandatory. Its repository-navigation links may point to the personal kit and governance, but its substantive content remains generic.
- The public baseline retains concise current evidence rather than carrying raw migration material.
- A future repository rename does not require internal navigation changes.

## Alternatives considered

- **Keep the Phase 5 root and explain the domains in documentation:** rejected because the filesystem would continue to contradict the primary reader model and the term “implementation” would remain overloaded.
- **Create an `architecture/` peer:** rejected because architecture exists at both generic and instantiated levels; a peer directory would duplicate `framework/` and `governance/` responsibilities.
- **Use `instance/` or `personal/`:** viable but less consistent with the established language. `kit/` is short, already defined, and remains meaningful if the repository is renamed.
- **Leave evals at the root:** rejected because active fixtures verify this personal instance. Completed evaluation evidence remains under governance, preserving the active/evidence distinction.
