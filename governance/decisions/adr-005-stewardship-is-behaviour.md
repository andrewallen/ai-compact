← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-005**

# ADR-005 — Keep stewardship behaviour in the kit and store structure outside it

**Status:** Accepted (2026-07-08)

## Context

A knowledge steward needs a portable decision policy: what is worth retaining, how maturity and contradictions are handled, and what it may change. Folder structures, schemas and lifecycle mechanics belong to whichever knowledge store is in use. Combining the two would bind the kit to one tool.

## Decision

Define knowledge-steward behaviour in `kit/roles/knowledge-steward.md`: mission, decision policy, provenance, independence, reflection cadence and persistent-write boundaries.

Do not encode vault paths, schemas or folder structures in the charter. Product wiring belongs in the appropriate platform adapter.

## Consequences

- The charter remains usable with different knowledge stores.
- Store-specific configuration stays outside the portable kit.
- The charter proposes and challenges but never writes to persistent stores without explicit approval.
- The charter is an available role definition; it does not imply a live autonomous deployment.

## Alternatives considered

- **Put the knowledge-store schema in the kit:** rejected because it couples portable behaviour to one implementation.
- **Keep the entire role in a platform configuration:** rejected because its judgement policy is model- and tool-agnostic.
