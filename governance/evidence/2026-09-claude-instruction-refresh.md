← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Claude instruction refresh**

# Claude Instruction Refresh

On 19 September 2026, Andrew authorised updating Claude through computer use after the source/deployment comparison. He subsequently excluded individual Claude projects. This record covers the account instruction field, the retained Cowork addendum and my-voice. It is maintenance evidence, not an operating instruction.

## Account instructions

Claude Desktop 2.2553.1 exposed **Settings → Account → Instructions for Claude**. Its description said the instructions apply across chats and Cowork, and a notice said Cowork global instructions had been brought over. The Cowork settings page no longer exposed the previously recorded global-instruction field.

The account field initially contained the earlier 4,930-character base, followed by `\n\n[Imported from Cowork]:\n` and the 2,469-character Cowork addendum. The imported addendum exactly matched [its source](../../kit/implementation/platforms/claude/cowork/global-instructions.md), version 2026.09.13 @ 1.7.

Only the base was replaced with the 5,000-character marked body from [personal preferences](../../kit/implementation/platforms/claude/personal-preferences.md), generated from shared chat source 2026.09.19 @ 1.1. The import separator and addendum were preserved exactly. Claude displayed **Saved**. After navigating away and reopening Account settings, the complete 7,495-character field matched the intended combined text, including independent equality checks for the base and unchanged addendum. This establishes acceptance of that length, not the field's maximum capacity.

| Content | SHA-256 |
|---|---|
| Current shared base, 5,000 characters | `a7a950fc1c056980a2d4d61e42d94c9e82a84aa1b908454049f3d4a74b0b218d` |
| Unchanged Cowork addendum, 2,469 characters | `a292fdbc65db78812572d96b7df4543b7e5806acdbb4390371e37866ba6f8f37` |
| Complete saved field, 7,495 characters | `73d86dc021e6345094be4a6f20e526d4d7fa12c94d79efea7a6ed85ac303d06b` |

Hashes describe the exact source strings checked against UI readback, excluding a trailing file newline. The previous base remains recoverable from Git; a local temporary restoration text combines it with the unchanged addendum. No change to Cowork safeguards or their intended scope was made. Their mode-specific application in the merged field has not been tested.

## My-voice

The enabled v3 package was downloaded before replacement. Its entry point and documentation register matched current source; its authored register and examples matched the earlier deployed versions. Claude's **Replace** flow uploaded a ZIP of the four current repository files and saved **v4**. The UI showed **Replaced my-voice**, **v4 · current**, four contents files and the enable switch **on**. The version selector initially retained a stale accessibility value; opening it confirmed v4 selected as current, with earlier versions listed.

The saved v4 was then downloaded through Claude. All four skill files matched repository bytes exactly:

| File | SHA-256 |
|---|---|
| `SKILL.md` | `00dc812363de5ad81f48b1fcca08e50ca69593b6ee4b43eac547c044d31f5a44` |
| `authored-register.md` | `00b97086bc8ed954b43646f4c6ec2a58c4b6450a698f2bf3ba1e8efdd8956d22` |
| `documentation-register.md` | `4e3a279d8febbc2812f772ac391ba13b15b9c7d2cccbe272660ffa166ae63ecc` |
| `examples.md` | `6ab15886eca7e75e50a7e13a6820bffe9b4de44a56ce9d7e21bccea62499a71b` |

Claude's download adds a plugin manifest and places the files under `skills/my-voice/`; the equality checks compare the four skill files. The before/after downloads and prepared upload remain in local temporary storage. Raw account settings and device details were not copied into the repository.

## Boundaries

This refresh closes the account-base drift and the Claude my-voice drift identified after judgement adaptation and repository consolidation. It verifies saved configuration and package identity. No chat was submitted to test invocation, behavioural adherence or propagation into existing conversations. Individual project instructions and constitution attachments were neither inspected nor updated, following Andrew's direction. Separate Claude Code and local Codex deployment states were not changed.

The [Claude baseline](../../kit/implementation/platforms/claude/configuration-baseline.md) and [skills tracker](../../kit/implementation/skills/README.md) record the resulting state. The preferences wrapper now describes the observed combined field so a later base refresh does not discard the imported addendum; its generated runtime body is unchanged by this deployment record.

Local checks confirmed all seven generated contract copies current, all 61 relative links in the changed documents valid, and no whitespace errors in the tracked patch. The marked preferences body retained the deployed hash after the wrapper edit. These documentation changes were not committed.
