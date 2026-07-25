← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-011**

# ADR-011 — Use three reader-facing repository domains

**Status:** Accepted (2026-07-13)

## Context

The five layers describe authority inside a personal AI system, but they do not describe every kind of content in this repository. Readers need a clear distinction between the generic pattern, the personal instance and the records that explain how both are governed.

## Decision

Use three top-level content domains:

```text
framework/                   generic, anonymised specification
kit/                         personal instance
  philosophy/
  constitution/
  roles/
  implementation/
  evals/
governance/                  architecture, decisions, diagrams and evidence
```

Memory remains outside the repository. Root maintenance files govern all three domains.

The canonical documentation split is:

- `framework/layer-model.md` defines the generic architecture;
- `kit/README.md` explains the personal instance;
- `governance/current-architecture.md` describes the current relationship between framework, kit, memory and products;
- the root README orients readers without becoming a competing specification.

## Consequences

- The repository root exposes its three intellectual domains directly.
- “Kit” means the complete personal instance; “implementation” means layer 4 only.
- Active evals stay with the instance they test; dated results sit in governance.
- Relative navigation and the `Home` breadcrumb make internal links independent of repository naming.
- ADR-010 remains the source for semantic layer paths; this ADR supersedes only its top-level placement.

## Alternatives considered

- **Expose every personal layer at the root:** rejected because the reusable framework and governance would appear to be peer layers.
- **Create an architecture domain:** rejected because generic architecture belongs in the framework and instantiated topology belongs in governance.
- **Leave evals at the root:** rejected because active fixtures verify the personal kit.
