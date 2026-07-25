← [Home](../README.md) · **Kit** · [Governance](../governance/README.md)

# Personal Kit

The personal instance of the [generic framework](../framework/README.md). These are the files that define, deploy and verify how AI works with the owner. Unlike the framework, this domain is intentionally personal.

## Layers

| Layer | Location | Purpose | Loaded when |
|---|---|---|---|
| 1 — Philosophy | [philosophy/](philosophy/README.md) | Axioms the constitution derives from. | Maintenance and foundational review only. |
| 2 — Constitution | [constitution/](constitution/README.md) | Calibration, binding operating contract and conditional overlay. | Core set for full operating context. |
| 3 — Roles | [roles/](roles/README.md) | Mission, judgement and boundaries for distinct AI roles. | Only while the role is active. |
| 4 — Implementation | [implementation/](implementation/README.md) | Platform adapters, skills and reusable prompts. | Deployed or invoked as needed. |
| 5 — Memory | Outside the repository | Knowledge store, platform memory and conversation history. | Product- and task-dependent. |

[Evals](evals/README.md) are cross-layer regression probes for this instance. They are active verification assets, not runtime context and not a sixth layer.

## Authority and derivation

The [constitution](constitution/README.md) is the behavioural source of truth. Role charters and implementation components supplement or derive from it and never override it. The [philosophy](philosophy/README.md) is the maintenance-time tiebreaker when the constitution itself is under review.

The kit instantiates the [framework layer model](../framework/layer-model.md). Structural decisions and historical evidence live in [governance](../governance/README.md); the current relationship between the kit, memory and platforms is documented in [current architecture](../governance/current-architecture.md).

## Common routes

- Deploy to a product: [platforms](implementation/platforms/README.md) and [deployment map](implementation/platforms/deployment-map.md).
- Invoke a reusable capability: [skills](implementation/skills/README.md).
- Start a recurring thinking pattern: [prompts](implementation/prompts/README.md).
- Test a change: [eval harness](evals/README.md).
- Review the foundations: [philosophy](philosophy/README.md), then [constitution](constitution/README.md).
