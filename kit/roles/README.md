← [Home](../../README.md) · [Kit](../README.md) · [Constitution](../constitution/README.md) · **Roles** · [Implementation](../implementation/README.md)

# Roles

Role charters — layer 3 of the architecture. A charter defines one role the AI can hold: its mission, decision policy, boundaries, and cadence, on a single page.

Numbering note: "layer 3" is the repo's architecture layering (philosophy, constitution, roles, implementation, memory). The authority levels 1–3 declared in `kit/constitution/00-bootstrap.md` are a separate scheme that orders files within the constitution layer. A charter never inherits the overlay's level-3 activation rules by number.

## What a charter is

A charter supplements the constitution and never overrides it. The binding rules in `kit/constitution/02-operating-contract.md` — register separation, agreement discipline, the expansion function — apply to every role, including the ones defined here. A charter adds what the constitution does not: what this role is *for*, and the judgement policy it applies within the constitutional rules. The same subordination pattern the professional overlay and the `my-voice` skill already declare.

Charters load conditionally: a charter is attached only when its role is active. Ordinary conversations carry no charter and cost no extra tokens.

## The embedded default role

The **thinking partner** is the default role, active in every conversation. Its charter is deliberately embedded in [02-operating-contract.md](../constitution/02-operating-contract.md) rather than extracted here — that file is the most tuned artefact in the kit and the eval fixtures are written against it. See [ADR-004](../../governance/decisions/adr-004-thinking-partner-stays-embedded.md) for the reasoning and the conditions under which extraction would be revisited.

## Current roles

| Role | Charter | When active |
|---|---|---|
| Thinking partner | Embedded in [02-operating-contract.md](../constitution/02-operating-contract.md) | Every conversation (default) |
| Knowledge steward | [knowledge-steward.md](knowledge-steward.md) | Knowledge-stewardship work: capture triage, vault sessions, the Hermes steward profile, reflection reviews |

## Writing a new charter

One page. Mission, decision policy, boundaries and cadence are the required sections; add whatever role-specific policy sections the role needs (the steward adds knowledge maturity and independence rules). Do not restate constitutional content — declare subordination to it and add only what is role-specific. A charter that needs supporting files or workflow steps is drifting toward being a skill; keep the judgement here and the mechanics in [skills](../implementation/skills/README.md).
