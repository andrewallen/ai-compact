← [Home](../../README.md) · [Governance](../README.md) · [Decisions](README.md) · **ADR-001**

# ADR-001 — Adopt the five-layer architecture

**Status:** Accepted (2026-07-08)

## Context

AI Compact contains enduring principles, binding operating rules, conditional roles, product-specific components and changing knowledge. Without an explicit hierarchy, those materials can be mistaken for peers even though they carry different authority and change at different rates.

## Decision

Organise a personal AI system as five layers, ordered by authority and inverse rate of change:

1. **Philosophy** — why AI is in the system; changes rarely.
2. **Constitution** — enduring behavioural principles; changes occasionally.
3. **Role charters** — mission and decision policy per role; change with the roles.
4. **Implementation** — platform adapters, skills and prompts; changes frequently.
5. **Memory** — knowledge stores, product memory and conversation history; changes continuously and remains outside the repository.

Evals and governance are cross-cutting rather than additional runtime layers. The generic model lives in `framework/`; the personal instance lives in `kit/`.

## Consequences

- Authority flows downward; a lower layer may adapt but never override a higher one.
- Runtime loading is selective: constitution files provide the core, role charters load only when active, and implementation components load or execute when needed.
- Philosophy governs maintenance but is not ordinary runtime context.
- Memory can change products or stores without changing the portable system.

## Alternatives considered

- **Constitution plus derived artefacts:** rejected because it gives philosophy and role-specific judgement no explicit place.
- **Treat memory and reflection as the architecture:** rejected because that models knowledge management rather than authority across the AI system.
