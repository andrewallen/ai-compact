← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-004**

# ADR-004 — Keep the thinking-partner role embedded in the constitution

**Status:** Accepted (2026-07-08)

## Context

The operating contract combines constitutional rules with the mechanics of the default thinking-partner role: mode detection, posture and the division of labour. Extracting those mechanics would make the layer boundary purer, but it would split the most frequently loaded and most heavily evaluated part of the system.

## Decision

Keep the default thinking-partner role in `kit/constitution/02-operating-contract.md`. Standalone role charters are reserved for conditional roles with distinct missions and decision policies.

No extraction is planned. A standalone charter would require a new structural decision and before-and-after eval parity.

## Consequences

- `kit/roles/README.md` identifies the embedded default role explicitly.
- Other charters supplement the constitution and do not restate or override it.
- The operating contract remains one coherent runtime source.
- A separate charter is justified only by a concrete independent consumer.

## Alternatives considered

- **Extract the default role:** rejected because it adds loading and synchronisation risk without changing behaviour.
- **Treat the whole operating contract as a role charter:** rejected because it contains rules that must bind every role.
