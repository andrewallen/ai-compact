← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Claude instruction deployment**

# September 2026 Claude Instruction Deployment

Andrew requested updating the Claude app through computer use with the revised configuration. The deployment used Claude Desktop 1.52386.6. Account, privacy, security and capability settings were not changed.

## Saved and verified

- **Instructions for Claude:** replaced the older preferences with the exact marked body from the shared chat contract (4,930 characters). The app displayed Saved, and accessibility readback matched the supplied source body exactly. Wrapper, generation metadata and version footer were excluded from the field.
- **Cowork global instructions:** replaced the older global instructions with the current addendum, version `2026.09.13 @ 1.7`. After saving, the editor was reopened and its 2,469-character body matched the source excluding its final newline.
- **Composition evidence:** the General settings description explicitly states that Instructions for Claude apply across chats and Cowork. This establishes the product's stated delivery scope; runtime loading and adherence were not behaviourally tested.

| Source body | SHA-256 (UTF-8, no trailing newline) |
|---|---|
| Chat | `ad6d9ff63294438e52c548b7bfe2a1aebd21fc581ee9a33884ac753441a9f266` |
| Cowork | `a292fdbc65db78812572d96b7df4543b7e5806acdbb4390371e37866ba6f8f37` |

## Skill replacement saved and verified

Automatic approval review initially rejected the upload before transmission because it required specific permission for the personal voice material and examples. Andrew then explicitly approved uploading the four-file package to Claude. The Replace flow completed with a “Replaced my-voice” confirmation; the existing skill remained enabled.

The initial post-save Contents view still selected v1, and its download contained the older SKILL.md and documentation-register.md. A fresh browser view showed **My voice v2 · current** and the updated description. Downloading that selected version established byte-for-byte parity for all four source files. The refreshed Desktop view also showed v2 as current. This verifies saved package content and enabled availability, not runtime invocation or adherence.

| Saved file | SHA-256 (complete source bytes) |
|---|---|
| SKILL.md | `0079d4effe21acd6a3150285c2e6573c8e5dfc534c7ec21ce6122ebbffe433d7` |
| authored-register.md | `fca5cc5bbd06c3ba69e2148cb130e93ce3707a6d6b82c9254877c42e1469b479` |
| documentation-register.md | `1de625a73cfabbec5cb4d1f81f00f4bdf71af2c57a2304a6bbce4458469d830b` |
| examples.md | `8295c06884a2e4aca38e4040483d7ae75c70c98618730bab1620490c91e8b1de` |

No project-specific constitution attachments or project instructions were changed, and no behavioural probes were run. Earlier configuration and consolidation records remain historical evidence.
