← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-008**

# ADR-008 — Publish the project as AI Compact

**Status:** Accepted (2026-07-25)

## Context

`personal-context-kit` described the project's origin but not its expanding purpose. The system now governs both conversational collaboration and agents that may operate under delegated authority. A long descriptive repository name would be accurate but difficult to type, reference in conversation and use in talks.

The name needs to identify the governing relationship: the terms under which AI can think with Andrew and act for him.

## Decision

Publish the project as **AI Compact**, with the repository slug `ai-compact`.

A compact is a governing agreement. It stretches from the terms of a conversation to the purpose, authority and boundaries of an autonomous role. It is short enough to work as a URL and spoken reference while leaving the README to explain the architecture.

## Consequences

- The public source is `andrewallen/ai-compact`.
- Internal navigation remains repository-name-neutral.
- The working checkout and any tool references move to the new repository.
- The previous private repository remains a frozen development-history archive and is never a deployment source.

## Alternatives considered

- **Long descriptive names:** rejected because they optimise for completeness at the expense of everyday use.
- **Metaphorical names:** rejected because they require explanation before communicating the project's relationship to AI.
- **Keep `personal-context-kit`:** rejected because context is only one part of the system.
