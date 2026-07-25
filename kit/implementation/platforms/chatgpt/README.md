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
9. Keep memory enabled for ambient continuity, review it periodically for stale assumptions, and use Temporary Chat when a conversation should neither use nor update memory.
10. Keep model-improvement/data-training controls off where available.

Custom instructions must fit within 5,000 characters in total (confirmed on the web product on 2026-07-19; the earlier 1,500-character limit and the two-field layout with a per-field limit no longer apply). The paste-ready block in [custom-instructions.md](custom-instructions.md) measures 4,844 characters — re-measure after any edit, and re-verify the limit if the UI changes.

## Using the Full Kit

For sustained work, create or use a ChatGPT Project and upload the core constitution files:

- `kit/constitution/00-bootstrap.md`
- `kit/constitution/01-calibration.md`
- `kit/constitution/02-operating-contract.md`

Add `kit/constitution/03-professional-overlay.md` only when the work involves Microsoft, the CDTO role, UK government engagement in a professional capacity or Andrew explicitly invokes it.

Andrew's voice is reserved for output produced on his behalf. Voice reference material is supplied separately when needed; it is not part of this platform configuration.

The custom instructions are deliberately standalone. They must work when no constitution files are attached, and they must defer when the full constitution files are present.

ChatGPT memory is product-managed state, separate from custom instructions. The persistence rule governs deliberate tool actions such as changing a project file, standing instruction or explicit user-visible memory entry. It does not claim to prevent ChatGPT from automatically retaining or inferring context. Manage that behaviour through **Settings → Personalization**, saved-memory review and Temporary Chat.

Version: 2026.07.25 @ 2.0
