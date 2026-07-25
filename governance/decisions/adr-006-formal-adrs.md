← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-006**

# ADR-006 — Adopt formal ADRs alongside the design-decisions log

**Status:** Accepted (2026-07-08)

## Context

`governance/design-decisions.md` is a working decision log in prose form — it records reasoning, rejected alternatives, and supersessions, and it predates this review. The July conversation proposed an architecture decision log as if none existed. The genuine gap is narrower: the prose log records file-level design reasoning well, but structural decisions (layers, seams, renames) were being carried in commit messages and conversation history.

## Decision

Two instruments with a declared scope split:

- **`governance/decisions/`** — numbered ADRs for structural, layer-level decisions: anything that changes the shape of the system, its seams, its folders, or its name.
- **`governance/design-decisions.md`** — continues unchanged as the narrative log for file-level design reasoning (why a rule lives where it does, why a register was split, what a live failure taught).

Each references the other where they touch. A completed change cycle may add a concise record under `governance/evidence/`; raw working material does not become a permanent public governance surface.

## Consequences

- Nothing is frozen or migrated; the existing log keeps its history and its role.
- The boundary needs judgement at the margin. Default: if it changes the repo tree or a layer, it is an ADR; if it changes the content of a file within its layer, it is a design-decisions entry.
- Evidence records capture the outcome and claim boundary of material change cycles without creating a third current decision log.

## Alternatives considered

- **ADRs replace the log:** rejected — the prose log is richer for its purpose, and rewriting working history for format's sake violates evolve-don't-rewrite.
- **Keep only the log:** rejected — structural decisions were demonstrably falling through it, and the framework needs a citable decision format for adopters.
