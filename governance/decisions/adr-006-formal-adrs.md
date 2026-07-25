← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-006**

# ADR-006 — Use formal ADRs alongside the design-decisions register

**Status:** Accepted (2026-07-08)

## Context

Structural decisions and file-level behavioural decisions need different records. A single narrative register is useful for explaining why individual rules exist, but it is harder to cite when a decision changes the system's layers, seams, domains or naming.

## Decision

Use two complementary instruments:

- `governance/decisions/` contains numbered ADRs for structural, layer-level, boundary and naming decisions.
- `governance/design-decisions.md` contains narrative reasoning for file-level and behavioural choices.

A material evaluation may also produce a dated evidence record. Evidence supports decisions but is not a third decision log.

## Consequences

- Structural choices have stable identifiers and explicit statuses.
- File-level reasoning remains readable as a continuous design register.
- At the margin, changes to the repository tree or layer boundaries use an ADR; changes within an established layer use the design register.
- Each maintained record must be understandable from public sources in this repository.

## Alternatives considered

- **Use ADRs for every decision:** rejected because file-level reasoning would become fragmented and ceremonial.
- **Use only the narrative register:** rejected because structural choices need stable, citable records and supersession semantics.
