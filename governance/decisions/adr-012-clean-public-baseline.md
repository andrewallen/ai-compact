← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-012**

# ADR-012 — Keep the public repository self-contained

**Status:** Accepted (2026-07-25)

## Context

AI Compact publishes a real personal kit as well as a reusable framework. Readers need enough architecture, rationale and evidence to understand the maintained system, while raw conversations, account audits and transient working material would add sensitivity and volume without becoming sources of truth.

## Decision

Maintain a self-contained public repository containing:

- the reusable framework;
- the current personal kit;
- active eval fixtures;
- current architecture, ADRs, diagrams and concise evidence records.

Do not make maintained claims depend on conversational context, local files or unpublished working history. Keep raw conversations, account-level audits, credentials and raw eval transcripts outside the repository.

## Consequences

- Every current claim must be supported by a maintained file in this tree.
- Evidence records summarise scope, results and limitations without carrying raw transcripts.
- Privacy and secret scans are part of publication checks.
- Ordinary Git branches and commits record future project changes.
- Framework and kit continue to evolve together without duplicating their sources.

## Alternatives considered

- **Publish all working material:** rejected because volume and sensitivity would obscure rather than strengthen the maintained design.
- **Publish only the framework:** rejected because the personal implementation is the reference that tests and demonstrates it.
- **Split framework and kit into separate active repositories:** rejected because changes often need to be reviewed together.
