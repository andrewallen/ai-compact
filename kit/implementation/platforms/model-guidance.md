← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Platforms](README.md) · **Model guidance**

# Model Guidance

Maintenance reference: **23 September 2026** review of Opus 5.5 and the GPT-6 family; other model observations retain their **13 September 2026** source check. Model guidance, host configuration and the owner's operating policy are separate concerns. Do not load this whole page as standing instructions or apply every row to every model. Select only a relevant adjustment; it remains subordinate to the constitution.

## Design targets and evidence

Andrew named Fable 5.1 and GPT-6 Astra as his primary thinking partners and Grok and models accessed through OpenCode Go, including GLM-5.3-Flash, mainly for execution. This describes his use, not an independently established capability ranking. One constitution remains the source; [the execution derivation](execution-contract.md) supports bounded work on any model.

The observations below are vendor documentation, not local behavioural results. Proposed steering has been documented, not deployed or proven. Effort names are not a common unit across families or products.

## Model-specific notes

| Model | Vendor observation and source | Application to this kit |
|---|---|---|
| Fable 5.1 | Anthropic describes denser prose, reduced formatting and progress updates, occasional early stopping, and less retrieval at low effort. [Prompting Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1). | Prefer direct sentences and useful paragraph breaks. Permit structure when it clarifies. A short progress instruction may help on long tasks. Preserve scope and completion rules. Client support determines progress delivery and history handling. |
| Opus 5.5 | Adaptive thinking is mandatory; default effort is `medium`, and the same effort label can produce more thinking than on Opus 5. Inter-tool progress text moves into thinking blocks and is omitted by default. [What's new](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5). | Start an effort comparison at explicit `medium`; measure before increasing it. Diagnose host rendering before adding progress instructions. Existing contracts remain the baseline; no local behavioural validation or adoption decision is recorded. |
| GPT-6 Astra | OpenAI warns about unnecessary clarification, conflicts in accessible skills, detailed formatting and excess verification on small coding tasks. [Astra guidance](https://developers.openai.com/api/docs/guides/latest-model). | Remove duplicate gates and clarify existing authorisation. Keep necessary checks without importing blanket autonomy. Audit host and skill instructions before blaming the constitution. |
| GPT-6 Sol | Positioned for complex coding and agentic workflows. API effort supports `none`, `low`, `medium` (default), `high`, `xhigh`, `max`. [Model reference](https://developers.openai.com/api/docs/models/gpt-6-sol). | Evaluate demanding bounded work with the unchanged compact at a fixed effort. Runner selection is supported; successful CLI invocation and behavioural suitability remain unverified. |
| GPT-6 Luna | Positioned for focused, high-volume tasks, with the same documented API effort choices and default as Sol. [Model reference](https://developers.openai.com/api/docs/models/gpt-6-luna). | Evaluate repeatable tasks and recognition of ambiguity before choosing an escalation policy. A lower-cost model is not automatically suitable for judgement or grading. No local behavioural result is recorded. |
| Grok | The Grok 4.6 page documents tools and configurable reasoning, without a comparable general text-prompting prescription. [Grok 4.6](https://docs.x.ai/developers/grok-4-6). | Begin with a clear brief and shared boundaries. Do not infer a need for emphatic rules or transfer speech-to-speech advice into text work. Native tool availability does not establish availability through another host. |
| GLM-5.3-Flash | Z.ai documents `reasoning_effort` values `low`, `high`, `max`, defaulting to `max`; its chat-template advice includes `clear_thinking=true` for chat. [Model card](https://huggingface.co/zai-org/GLM-5.3-Flash). | These are native configuration details. Gateway forwarding needs separate confirmation. Do not prescribe maximum effort for every task or extra chain-of-thought instructions from the model name alone. |
| Other Go models | [OpenCode Go](https://opencode.ai/docs/go/) offers multiple model families; the catalogue changes. | Identify the actual model and provider. A subscription is not a prompting profile. No model-specific claims are made for the remainder of the catalogue. |

## Common guidance, limited implications

OpenAI's [GPT-6 family guidance](https://developers.openai.com/api/docs/guides/latest-model) now covers Sol and Luna, but explicitly bases its behavioural prompting examples on Astra and asks users to evaluate them on the chosen workload. Do not attribute Astra's observed tendencies to Sol or Luna without evidence. Preserve effective effort where supported for a migration comparison; API options do not establish what a host exposes or forwards.

Anthropic's [Fable 5 guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) supports shorter steering and reviewing overly prescriptive older scaffolding. It does not establish that Andrew's independence or permission requirements are obsolete. OpenAI's [reasoning guidance](https://developers.openai.com/api/docs/guides/reasoning-best-practices) favours clear goals and constraints without demanding private reasoning. Retain reviewable rationale and evidence.

Effort, token limits, caching, compaction, tool schemas and progress rendering belong to implementation. No setting on this page authorises a configuration change. July skill model-routing advice is historical, not a current choice rule for these models.

## Opus 5.5: conditional techniques

Anthropic's [prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) offers task-specific techniques, not a replacement operating policy:

- Its chat-latency suggestion to treat earlier answers as settled can inhibit spontaneous correction. Keep it out of sustained thinking and analysis under this compact.
- Its unattended-agent persistence prompt excludes human-in-the-loop applications. Keep exploratory stopping and scoped approval intact. A task-specific unattended loop needs explicit completion conditions and bounded continuations.
- Mark third-party pasted text separately from the user's own directions. The guide proposes application-generated delimiters; they are an additional defence, not guaranteed isolation. [N1/N2](../../evals/instruction-boundary-probes.md) test the underlying distinction without introducing that steering.
- Broad multi-app discovery should remain relevant to the task and within available authority. Retrieved instructions remain data.

These are maintenance dispositions. No account prompt, shared contract or personal skill was changed by the source review. The [release review and evaluation specification](../../../governance/evidence/2026-09-model-release-review.md) records the implementation and remaining checks.

## Host compatibility before prompt changes

For custom integrations, consult the [Opus 5.5 migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide): forced tool selection is removed, thinking blocks depend on model and conversation history, and computer-use compatibility depends on the provider. Progress rendering may require `thinking.display: "updates"` with its beta header. Claude Code, Claude.ai, Managed Agents and the Agent SDK already maintain append-only history; this does not establish a particular account's deployment or adherence.

For Sol and Luna, use Responses for reasoning with tools; Chat Completions function calling requires effort `none` ([Sol](https://developers.openai.com/api/docs/models/gpt-6-sol), [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna)). The current eval runner uses the native Codex CLI, not a custom API client. Diagnose the actual host before changing the compact to compensate for missing capabilities.

## Maintenance rule

For an adjustment, record the exact model and host, source date, observed problem, proposed wording and evidence status. Distinguish vendor guidance, local observations and owner decisions. Remove an obsolete adjustment rather than adding a counter-instruction. Preserve constitutional requirements through condensation.

Version: 2026.09.23 @ 1.1
