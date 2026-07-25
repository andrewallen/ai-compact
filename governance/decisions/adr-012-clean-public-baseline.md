← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-012**

# ADR-012 — Begin public history from a clean, self-contained baseline

**Status:** Accepted (2026-07-25)

## Context

The private development repository contains superseded personal material, raw conversations, migration working documents, account audits and commit metadata that are not part of the adopted design. Deleting those files in a later commit would leave them in Git history. Rewriting the existing history would also retain operational complexity around branches, pull requests, cached references and old clones.

The public project must expose Andrew's approved current kit while remaining understandable without the private development journey.

## Decision

Start `ai-compact` as a new Git repository from a reviewed snapshot of the stable system.

The public repository contains the reusable framework, Andrew's current personal kit, active eval fixtures, current architecture, adopted decisions, diagrams and concise evidence records. It omits raw source conversations, superseded personal files, migration plans, raw transcripts and account-level audit findings.

The former repository remains private and frozen as historical evidence. It is never an active source, deployment target or dependency of the public project.

## Consequences

- Public Git history begins with one stable baseline commit.
- Every maintained public claim must be supported by current files; private Git history and conversational memory are not required.
- Future changes use ordinary branches and commits in `ai-compact`.
- Publication requires a current-tree privacy and secret scan, not an attempt to prove that old private history is safe.
- Existing clones of the private repository must not push to the public remote.

## Alternatives considered

- **Make the private repository public:** rejected because removed personal material would become visible through history and other refs.
- **Rewrite the private repository in place:** rejected because it creates avoidable recontamination and reference-management risk.
- **Maintain separate active framework and kit repositories:** rejected because it would split changes that need to evolve together.
