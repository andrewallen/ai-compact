← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-003**

# ADR-003 — Framework and implementation converge in one repo

**Status:** Accepted (2026-07-08); repository boundary clarified by ADR-011

## Context

The system now has two audiences: Andrew (the working implementation) and, potentially, anyone else who wants the pattern (the reusable framework). The July conversation considered separate repos; Andrew chose one repo so the framework and his implementation of it co-evolve in the same context frame.

## Decision

`framework/` holds the generic pattern — the layer model, design principles, and an adoption guide — written abstractly and containing nothing personal. ADR-011 later made the other responsibilities explicit: `kit/` is the personal reference implementation, while `governance/` describes and evidences the framework and kit rather than forming part of the implementation.

The seam rule: when a kit change forces a rethink of the framework, that is evidence of a general lesson — record it in the framework (and an ADR if structural). When it does not, the lesson was personal and stays in the kit. One repository is what makes that measurement possible.

The framework was extracted from an earlier personal methodology that articulated the interview principle, authority declaration, two-model workflow, minimum viable implementation and failure modes. The public framework is the maintained, anonymised result; the superseded personal source is outside the public baseline.

## Consequences

- An anonymisation discipline: nothing in `framework/` names Andrew, Microsoft, or personal detail. Checked at every framework change.
- The framework can later be split out without archaeology because the boundary is maintained from the start.
- Private source material may inform a framework lesson, but the public framework must state that lesson independently.

## Alternatives considered

- **Two repos now:** rejected — doubles maintenance, breaks traceability between a framework change and the implementation experience that motivated it, and the framework is not yet stable enough to publish.
- **No framework layer** (keep teaching by example): rejected — the pattern stays trapped in the instance, and the intellectual contribution the archive already gestured at ("that might be the contribution you can make") remains unmade.
