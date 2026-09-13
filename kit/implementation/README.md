← [Home](../../README.md) · [Kit](../README.md) · [Constitution](../constitution/README.md) · [Roles](../roles/README.md) · **Implementation** · [Evals](../evals/README.md)

# Implementation

Layer 4 of the kit: the product-shaped components that deploy or execute the higher-authority layers. Implementation artefacts may adapt the constitution and active role charters to a platform, package a capability, or provide a reusable starting point. They never override the constitution.

| Folder | Purpose |
|---|---|
| [platforms/](platforms/README.md) | Product-specific deployment instructions, condensed contracts and the cross-platform deployment map. |
| [skills/](skills/README.md) | Personal skills plus capability, provenance and package records for first-party plugins and native implementations. Execution components are supplied only for relevant work. |
| [prompts/](prompts/README.md) | Reusable entry points for recurring work; prompts invoke the system but do not define it. |

Memory is not stored here. It remains outside the repository and is governed through the products and knowledge systems that hold state.

The [package register](skills/package-register.md) describes reviewed candidates and observed native baselines. It is maintenance material; client-specific installation and composition belong in [platform guidance](platforms/deployment-map.md#skills-plugins-and-native-capabilities). A plugin is a distribution package within this layer, not a new authority level. The [implementation plan](skills/implementation-plan.md) distinguishes repository preparation from trials and deployment.
