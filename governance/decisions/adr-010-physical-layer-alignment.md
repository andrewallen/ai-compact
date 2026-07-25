← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-010**

# ADR-010 — Physically align the repository to the five-layer model

**Status:** Accepted (2026-07-13); root placement partially superseded by ADR-011 and public evidence placement by ADR-012

## Context

ADR-001 adopted the five-layer architecture logically. ADR-009 deferred physical alignment to Phase 5 and deliberately limited any later change to `context/` → `constitution/`, with the numbered filenames left unchanged. Living with the logical model exposed a wider mismatch: layers 1–3 are visible at the repository root, while layer 4 is split across three peer folders, and `architecture/` mixes governance records with live deployment mapping.

Phase 4 steward deployment has not started. Restructuring after that deployment would mean wiring Hermes, the steward charter and its probes to paths already known to be temporary. The structural pass therefore moves ahead of Phase 4 so the deployment is built once against the final layout.

Andrew explicitly approved reconsidering all folder and file names needed for alignment. The repository name itself is excluded and remains governed by ADR-008.

## Decision

Adopt this physical structure:

```text
framework/                         generic, anonymised pattern
philosophy/                        layer 1
constitution/                      layer 2
roles/                             layer 3
implementation/                    layer 4
  platforms/
  skills/
  prompts/
evals/                             cross-cutting verification
governance/                        cross-cutting governance
  decisions/
  diagrams/
  evidence/
```

Memory remains absent because layer 5 is external state, not a repository artefact.

The material path changes are:

- `philosophy/philosophy.md` → `philosophy/axioms.md`
- `context/` → `constitution/`
- `constitution/01-about-me.md` → `constitution/01-calibration.md`
- `constitution/02-how-we-work.md` → `constitution/02-operating-contract.md`
- `platforms/`, `skills/`, `prompts/` → `implementation/` beneath their existing names
- `architecture/` → `governance/`
- `governance/platform-mapping.md` → `implementation/platforms/deployment-map.md`

The `00-`…`03-` prefixes remain: they are load-order insurance within the constitution and explicitly separate from the architecture's layer numbering. `framework/`, `roles/` and `evals/` keep their names. No `kit/`, `instance/` or numbered-layer wrapper is added; the extra path depth would make runtime loading and human navigation worse without strengthening the authority model.

Historical evidence keeps its meaning. ADR-012 later established that the public repository carries concise evidence records while raw development material remains private.

## Consequences

- ADR-009 is superseded: its sequencing decision was followed, but its restricted rename scope no longer applies.
- Phase 5 physical alignment executed before any steward deployment; later activation uses the settled paths.
- Every live path reference, breadcrumb, load list, platform guide and diagram must be updated in the same change.
- Renamed constitution files must be re-uploaded wherever copies are held in product projects. Local agent and Hermes configurations that use hard-coded paths must be repointed deliberately.
- The full behavioural eval suite runs from the new paths. File contents are not substantively changed by the move.
- The implementation-to-framework lesson is recorded in `framework/README.md`, followed by the framework anonymisation check required by ADR-003.
- At the time of this decision ADR-008 remained Proposed. ADR-008 was resolved on 2026-07-25.

## Alternatives considered

- **Only rename `context/`:** rejected because it leaves layer 4 physically fragmented and governance mixed with deployment documentation.
- **Number the layer directories:** rejected because layer order is architectural metadata, while directory names should remain stable if the model evolves; it would also collide visually with the constitution's internal load-order numbering.
- **Wrap the personal implementation in `kit/` or `instance/`:** rejected because the repository itself already defines that boundary and `framework/` is the single explicit exception. The wrapper adds path ceremony without a new authority distinction.
- **Complete Phase 4 first:** rejected because it would wire the steward to paths scheduled to move immediately afterwards.
