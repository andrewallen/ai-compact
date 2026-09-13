← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Platforms** · [Governance](../../../governance/README.md)

# Platforms

Product-specific deployment and configuration guidance. Start with the [deployment map](deployment-map.md) to choose a route; use the product guide for setup and recorded gaps. Source availability, saved configuration and successful use are separate claims.

## Shared sources and maintenance

| Reference | Responsibility |
|---|---|
| [Deployment map](deployment-map.md) | Cross-product routes and deployment boundaries. |
| [Chat contract](chat-contract.md) | Authored body for generated chat adapters. |
| [Execution contract](execution-contract.md) | Authored body for generated agent guides and a defined-task handover. |
| [Contract maintenance](contract-maintenance.md) | Coverage, required loading combinations and distribution commands. |
| [Distribution script](sync_contracts.py) | Deterministic copying and drift checks. |
| [Model guidance](model-guidance.md) | Dated vendor observations and host limits. |

## Product guides

| Product | Guide |
|---|---|
| Claude | [Chat, Cowork and Code](claude/README.md) |
| ChatGPT | [Configuration](chatgpt/README.md) |
| Gemini | [Configuration](gemini/README.md) |
| Codex | [Configuration](codex/README.md) |
| Copilot CLI | [Configuration](copilot-cli/README.md) |
| Hermes | [Configuration](hermes/README.md) |
| Grok | [Host-specific guidance](grok/README.md) |
| OpenCode and Go | [Configuration and model access](opencode/README.md) |

## Adding a product

Create a product folder and guide, selecting the appropriate shared contract and declaring any required base context. Keep product controls and additional safeguards in the wrapper or addendum. If a detached body is needed, register its marked regions in the distribution script instead of maintaining another independent copy. Update this index and the deployment map, then run the checks in contract maintenance. Add deeper navigation through the product's own index.

Version: 2026.09.13 @ 1.12
