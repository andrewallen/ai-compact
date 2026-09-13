← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Platforms](README.md) · **Model guidance**

# Model Guidance

Maintenance reference checked on **13 September 2026**. Model guidance, host configuration and the owner's operating policy are separate concerns. Do not load this whole page as standing instructions or apply every row to every model. Select only a relevant adjustment; it remains subordinate to the constitution.

## Design targets and evidence

Andrew named Fable 5.1 and GPT-6 Astra as his primary thinking partners and Grok and models accessed through OpenCode Go, including GLM-5.3-Flash, mainly for execution. This describes his use, not an independently established capability ranking. One constitution remains the source; [the execution derivation](execution-contract.md) supports bounded work on any model.

The observations below are vendor documentation, not local behavioural results. Proposed steering has been documented, not deployed or proven. Effort names are not a common unit across families or products.

## Model-specific notes

| Model | Vendor observation and source | Application to this kit |
|---|---|---|
| Fable 5.1 | Anthropic describes denser prose, reduced formatting and progress updates, occasional early stopping, and less retrieval at low effort. [Prompting Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1). | Prefer direct sentences and useful paragraph breaks. Permit structure when it clarifies. A short progress instruction may help on long tasks. Preserve scope and completion rules. Client support determines progress delivery and history handling. |
| GPT-6 Astra | OpenAI warns about unnecessary clarification, conflicts in accessible skills, detailed formatting and excess verification on small coding tasks. [Astra guidance](https://developers.openai.com/api/docs/guides/latest-model). | Remove duplicate gates and clarify existing authorisation. Keep necessary checks without importing blanket autonomy. Audit host and skill instructions before blaming the constitution. |
| Grok | The Grok 4.6 page documents tools and configurable reasoning, without a comparable general text-prompting prescription. [Grok 4.6](https://docs.x.ai/developers/grok-4-6). | Begin with a clear brief and shared boundaries. Do not infer a need for emphatic rules or transfer speech-to-speech advice into text work. Native tool availability does not establish availability through another host. |
| GLM-5.3-Flash | Z.ai documents `reasoning_effort` values `low`, `high`, `max`, defaulting to `max`; its chat-template advice includes `clear_thinking=true` for chat. [Model card](https://huggingface.co/zai-org/GLM-5.3-Flash). | These are native configuration details. Gateway forwarding needs separate confirmation. Do not prescribe maximum effort for every task or extra chain-of-thought instructions from the model name alone. |
| Other Go models | [OpenCode Go](https://opencode.ai/docs/go/) offers multiple model families; the catalogue changes. | Identify the actual model and provider. A subscription is not a prompting profile. No model-specific claims are made for the remainder of the catalogue. |

## Common guidance, limited implications

Anthropic's [Fable 5 guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) supports shorter steering and reviewing overly prescriptive older scaffolding. It does not establish that Andrew's independence or permission requirements are obsolete. OpenAI's [reasoning guidance](https://developers.openai.com/api/docs/guides/reasoning-best-practices) favours clear goals and constraints without demanding private reasoning. Retain reviewable rationale and evidence.

Effort, token limits, caching, compaction, tool schemas and progress rendering belong to implementation. No setting on this page authorises a configuration change. July skill model-routing advice is historical, not a current choice rule for these models.

## Maintenance rule

For an adjustment, record the exact model and host, source date, observed problem, proposed wording and evidence status. Distinguish vendor guidance, local observations and owner decisions. Remove an obsolete adjustment rather than adding a counter-instruction. Preserve constitutional requirements through condensation.

Version: 2026.09.13 @ 1.0
