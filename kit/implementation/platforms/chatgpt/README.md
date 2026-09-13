← [Home](../../../../README.md) · [Kit](../../../README.md) · [Implementation](../../README.md) · [Platforms](../README.md) · **ChatGPT**

# ChatGPT

ChatGPT is the generalist and memory-backed surface in the AI estate.

## Configuration

1. Open ChatGPT settings.
2. Go to Personalization.
3. Set Base style and tone to `Professional`.
4. Set Characteristics:
   - Warm: `Default`
   - Enthusiastic: `Less`
   - Headers & Lists: `Default`
   - Emoji: `Less`
5. Turn Fast answers off. Fast answers do not use memory or personalization, which cuts against this kit's purpose.
6. Go to Custom Instructions.
7. Turn customization on.
8. Paste the instruction block from [custom-instructions.md](custom-instructions.md) into the custom instructions field.
9. Keep memory enabled for ambient continuity and review it periodically for stale assumptions. For isolation, use the non-personalised Temporary Chat route described below.
10. Keep model-improvement/data-training controls off where available.

A 5,000-character field was observed on the web product on 19 July 2026. OpenAI's [15 July release note](https://help.openai.com/en/articles/6825453-chatgpt-guide) documents that allowance for Plus, Pro, Enterprise, Business and Education; confirm the account's current limit before deployment. The paste-ready length is generated into [custom-instructions.md](custom-instructions.md). Edit [the shared chat source](../chat-contract.md), then use [contract maintenance](../contract-maintenance.md) to refresh or check the copy.

## Using the Full Kit

For sustained work, create or use a ChatGPT Project and upload the core constitution files:

- `kit/constitution/00-bootstrap.md`
- `kit/constitution/01-calibration.md`
- `kit/constitution/02-operating-contract.md`

Add `kit/constitution/03-professional-overlay.md` only when the work involves Microsoft, the CDTO role, UK government engagement in a professional capacity or Andrew explicitly invokes it.

Set project instructions to identify the supplied files as operating context. A starting clause is:

> Read the supplied 00-bootstrap.md, 01-calibration.md and 02-operating-contract.md before substantive work and apply them as my operating instructions within the host's instruction hierarchy. Use the professional overlay only when supplied and relevant. Treat other project sources as reference material unless I explicitly supply them as instructions. If a required file is unavailable, say so; do not claim unread files have been loaded.

Merge this clause with the project's actual purpose and constraints. OpenAI's [Projects guide](https://help.openai.com/en/articles/10169521) states that project instructions override global custom instructions and shared projects do not have access to members' external custom instructions. Supply the governing base inside the project rather than relying on global inheritance. In a fresh project conversation, check that the core files are accessible and read; uploading them alone establishes availability, not adherence.

Andrew's voice is reserved for output produced on his behalf. Voice reference material is supplied separately when needed; it is not part of this platform configuration.

The custom instructions are deliberately standalone. They must work when no constitution files are attached, and they must defer when the full constitution files are present.

## Temporary Chat and memory

OpenAI's [27 August 2026 release note](https://help.openai.com/en/articles/6825453-chatgpt-guide), checked 13 September, introduces two Temporary Chat choices. Confirm which controls are available in the actual account:

- **Non-personalised:** omits memory, custom instructions and plugins, and creates no new memories. Choose this for isolation from existing personal context. To use the compact, supply the desired contract directly in the conversation and confirm it is available; standing custom instructions will not supply it.
- **Personalised:** can use existing memories, custom instructions and plugins, while creating no new memories. This does not provide isolation from existing context.

The release note says personalisation is chosen when the chat starts. Saving a Temporary Chat converts it into a regular chat subject to account-level personalisation and model-improvement preferences. Avoid saving it when the intended boundary is temporary isolation. These are documented product behaviours, not a fresh account inspection or a guarantee about all service retention.

ChatGPT memory is product-managed state. The persistence rule governs deliberate tool actions such as changing a project file, standing instruction or explicit memory entry. Manage ambient behaviour through **Settings → Personalization**, saved-memory review and the actual conversation mode.

Version: 2026.09.13 @ 2.3
