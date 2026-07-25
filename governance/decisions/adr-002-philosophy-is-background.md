← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-002**

# ADR-002 — Philosophy is a versioned background artefact, not a runtime dependency

**Status:** Accepted (2026-07-08)

## Context

The July conversation debated whether the philosophy should attach to every conversation. Attaching it would let the model interpret every constitutional rule against its purpose; not attaching it keeps the always-loaded context lean, consistent with the kit's token-consciousness principle and the recorded decision that the bootstrap stays short.

## Decision

`kit/philosophy/axioms.md` is versioned in the repo, kept to half a page of axioms, and is **not** part of the runtime load set. The constitution derives from it and may quote individual axioms where anchoring a rule in its reason materially improves compliance. The philosophy is loaded deliberately only when the foundations themselves are under review.

A philosophy change triggers a constitution review — the derivation must be re-checked, not assumed.

## Consequences

- Token budget for ordinary conversations is unchanged.
- The constitution must be self-sufficient: every binding rule works without the philosophy present. The philosophy explains; it does not operate.
- Drafting is Andrew's work. The candidate axioms in the target architecture are scaffolding extracted from his own statements; the file is written in his hand or it defeats its purpose.

## Alternatives considered

- **Attach philosophy to every conversation:** rejected for token cost and because a short axiomatic quote inside the constitution captures most of the anchoring benefit.
- **Leave the philosophy implicit:** rejected — that is the current state, and it means the system's rules cannot be audited against their intent, by a model or by a future Andrew.
- **Fold the axioms into `00-bootstrap.md`:** rejected — the bootstrap is deliberately minimal insurance, and a documented decision keeps it from growing.
