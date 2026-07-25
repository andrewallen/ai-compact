← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-008**

# ADR-008 — Use AI Compact as the project name

**Status:** Accepted (2026-07-25)

## Context

The project governs both conversational collaboration and agents operating under delegated authority. Its name needs to describe that governing relationship while remaining short enough for a URL, spoken reference and presentation.

## Decision

Use **AI Compact** as the project name and `ai-compact` as the repository slug.

A compact is a governing agreement. It covers the terms of a conversation and the purpose, authority and boundaries of an agentic role without tying the project to a particular model or product.

## Consequences

- Reader-facing material uses AI Compact consistently.
- Internal navigation remains repository-name-neutral through relative links.
- The README explains the architecture rather than making the name carry every detail.
- Product and model names remain implementation details rather than project identity.

## Alternatives considered

- **A long descriptive name:** rejected because it would be harder to type, say and remember.
- **A metaphorical name:** rejected because the governing relationship would need explanation before the project itself could be discussed.
- **A context-focused name:** rejected because context is only one part of the system.
