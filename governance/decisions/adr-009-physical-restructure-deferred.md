← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-009**

# ADR-009 — Physical folder restructure is deferred to the final phase

**Status:** Superseded by ADR-010 (2026-07-13)

## Context

The layer model (ADR-001) invites physical renames: `context/` → `constitution/` most obviously. The names carry real meaning — "context sounds temporary; constitution is closer to what you're doing," as the July conversation put it. But the folder path is referenced across the estate: every platform README lists `context/...` paths, `AGENTS.md` imports the files by path, eval fixtures name them in load lists, and the deployment docs tell Andrew which files to upload. The individual filenames (`00-bootstrap.md` and siblings) are also deployed artefacts, uploaded into ChatGPT and Claude projects; renaming them would desynchronise every live deployment until re-uploaded.

Meanwhile, everything the layer model needs behaviourally is achievable logically: the bootstrap, READMEs and AGENTS.md can declare which layer each folder implements without a single path changing.

## Decision

Adopt the layers logically first (Phases 1–3). Physical restructure is a single deliberate pass in Phase 5, executed only if living with the logical model proves the physical names matter — and scoped, if it runs, to the folder rename (`context/` → `constitution/`) with filenames unchanged, plus the full cascade sweep in the migration plan's register and a closing eval run.

Filename renames (the `00-`…`03-` files) are out of scope in all phases: the numbered names are load-order insurance and live deployment artefacts, and no layer-model benefit justifies breaking them.

## Consequences

- A period in which the folder is named `context/` while the docs call it the constitution layer. Tolerable and honest: the docs say what it is; the path says where it is.
- Phase 5 needs Andrew's explicit approval per the file-safety rules, a complete reference sweep, and re-verification of the deployment docs.

## Alternatives considered

- **Rename in Phase 1:** rejected — maximum cascade at the moment of least evidence that the rename buys anything.
- **Never rename:** viable; that is exactly what deferral leaves open. Phase 5 exists so the option is exercised deliberately rather than by default.
