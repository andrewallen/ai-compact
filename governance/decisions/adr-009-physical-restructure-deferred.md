← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-009**

# ADR-009 — Defer physical alignment until it can be atomic

**Status:** Superseded by ADR-010 (2026-07-13)

## Context

Layer names affect imports, deployment guides, eval load lists and copies held in external products. Renaming one path at a time would leave the maintained source and deployed references temporarily inconsistent. The numbered constitution filenames also provide useful load-order insurance.

## Decision

At the time of this decision, defer physical layer alignment until it can be performed as one controlled change with:

- a complete reference and breadcrumb sweep;
- updates to every deployment path;
- unchanged numbered constitution filename prefixes; and
- a closing behavioural evaluation.

ADR-010 superseded the deferral by defining the atomic alignment.

## Consequences

- Logical layer declarations could be used before paths changed.
- No partial rename was treated as an acceptable intermediate state.
- The numbered constitution filenames remained stable.
- ADR-010 became responsible for the final semantic paths.

## Alternatives considered

- **Rename incrementally:** rejected because it creates path drift across products and documentation.
- **Never align the paths:** rejected because semantic paths improve navigation once the cascade can be handled safely.
