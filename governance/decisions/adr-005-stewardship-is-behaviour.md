← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-005**

# ADR-005 — Knowledge stewardship enters the kit as behaviour; structure stays with the Vault

**Status:** Accepted (2026-07-08)

## Context

Two recorded decisions already govern this territory: the Obsidian Vault is not referenced in the portable files (most surfaces cannot reach it), and cognitive-architecture structure was removed because vault structure is Vault territory, not kit territory. The knowledge-steward operating policy could, read carelessly, reverse those decisions by bringing the knowledge system back into the kit.

The reconciliation: what was removed was **structure** (folders, schema, lifecycle stages tied to one tool chain). What the charter supplies is **behaviour** (a decision policy any agent applies to anything Andrew brings, against any store). Behaviour is portable; structure is not.

## Decision

The knowledge steward enters the kit as a role charter, `kit/roles/knowledge-steward.md`: mission, decision policy (worth remembering; new/strengthens/contradicts; throwaway or candidate principle; where else it applies), knowledge maturity (observation → principle through repeated application), independence rules (never normalise, competing hypotheses, provenance), reflection cadence, and boundaries (proposes, never disposes; no autonomous writes to persistent stores).

The charter names no vault paths, no schema, no folder structure. Vault-side structure remains outside the kit. Tool wiring (how Hermes loads the charter and reaches the vault) lives in `kit/implementation/platforms/hermes/README.md`, per the existing platform pattern.

## Consequences

- Both prior decisions stand unmodified; this ADR extends them rather than reversing them.
- The charter must survive a store migration (Obsidian to anything else) without edits — that is the test of whether structure has leaked in.
- A live steward deployment and role-specific probes begin together only when a real workflow justifies activating the role. They are not unfinished repository work.

## Alternatives considered

- **Reinstate the cognitive architecture in the kit:** rejected — re-couples the portable layer to one tool chain and re-creates the instructions-the-model-cannot-act-on problem.
- **Keep stewardship entirely in Hermes configuration:** rejected — the decision policy is model- and tool-agnostic judgement, exactly what the kit exists to version; leaving it tool-side forfeits portability and review.
