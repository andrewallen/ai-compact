← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-010**

# ADR-010 — Use semantic paths for the five-layer model

**Status:** Accepted (2026-07-13); top-level placement superseded by ADR-011

## Context

The logical layer model needs filesystem names that readers and tools can interpret consistently. Scattered product-shaped folders obscure the distinction between high-authority sources and frequently changing adapters, while generic names such as “context” understate the binding role of the constitution.

## Decision

Use these semantic directories inside the personal instance:

```text
philosophy/
constitution/
roles/
implementation/
  platforms/
  skills/
  prompts/
evals/
```

Use `axioms.md`, `01-calibration.md` and `02-operating-contract.md` as the canonical descriptive filenames. Retain the `00-` through `03-` prefixes inside the constitution because they provide load-order insurance.

Place live deployment mapping with platform adapters. Keep governance and active evals cross-cutting rather than treating either as another runtime layer. ADR-011 determines the final top-level `kit/` boundary.

## Consequences

- Higher-authority material remains shallow and directly addressable.
- Product-shaped components share one implementation boundary.
- The deployment map sits beside the artefacts it maps.
- Path changes require a full cascade through links, imports, diagrams and external copies.
- Memory remains outside the repository because it is state rather than portable system definition.

## Alternatives considered

- **Keep generic or scattered folder names:** rejected because the filesystem would obscure the authority model.
- **Number the layer directories:** rejected because layer order is architectural metadata and may evolve independently of stable paths.
- **Rename the constitution files without prefixes:** rejected because descriptive names and deterministic load order are both useful.
