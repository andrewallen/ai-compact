← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-003**

# ADR-003 — Keep the framework and personal kit in one repository

**Status:** Accepted (2026-07-08); domain boundary clarified by ADR-011

## Context

AI Compact serves two related purposes: a generic pattern that other practitioners can adopt and a real personal implementation that tests that pattern. Separating them would make it harder to trace when implementation experience reveals a general design lesson.

## Decision

Maintain both in one repository with a strict content boundary:

- `framework/` holds the generic, anonymised specification;
- `kit/` holds the personal reference implementation;
- `governance/` records the current topology, structural decisions and evidence.

When a kit change forces a change to the framework, record the general lesson in the framework and use an ADR if it is structural. Personal lessons remain in the kit.

## Consequences

- Every framework change receives an anonymisation check.
- Framework documents must stand alone without relying on personal examples or unpublished sources.
- Changes that affect both domains can be reviewed and committed together.
- The repository remains the single maintained source for both pattern and implementation.

## Alternatives considered

- **Separate repositories:** rejected because it doubles maintenance and weakens traceability between evidence and generalisation.
- **Publish only the personal example:** rejected because readers would have to infer the reusable pattern from personal material.
