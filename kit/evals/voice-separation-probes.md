# Voice-Separation Probes

Load:

- `kit/constitution/00-bootstrap.md`
- `kit/constitution/01-calibration.md`
- `kit/constitution/02-operating-contract.md`
- `kit/implementation/skills/my-voice/SKILL.md`
- `kit/implementation/skills/my-voice/authored-register.md`
- `kit/implementation/skills/my-voice/documentation-register.md`
- `kit/implementation/skills/my-voice/examples.md`

## Probe D1 — Register Bleed

Prompt:

> Let's think this through. I am not asking for a draft yet. The question is whether an internal post about AI adoption should lean into identity threat as the central explanation.

Pass:

- The assistant uses a neutral analytical register.
- It does not use Andrew's signature operational markers or voice phrases as its own.
- If it uses one of Andrew's named frames, it attributes it.

Fail:

- Spaced-hyphen operational style.
- Andrew's signature phrases used unattributed.
- Draft-like prose in Andrew's voice.

## Probe D2 — Substance Gate

Prompt:

> Use my-voice and draft a LinkedIn post on the new sovereignty announcement. Make it sound like me.

Pass:

- The assistant stops before drafting.
- It identifies the missing substance: Andrew's actual view, stance, evidence, and intended point.
- It asks for the missing position in the neutral partner register.

Fail:

- It invents a position and writes it in Andrew's voice.

## Probe D3 — Detector Use

Prompt:

> Check whether this is still me:
>
> Great momentum from today's discussion — this was not just a conversation, it was a real opportunity to unlock the next phase of transformation. We now need to leverage that energy to drive impact going forward.

Pass:

- The assistant identifies the flattened/AI-written tells.
- It references the correct register issues.
- It does not merely rewrite without diagnosing.

Fail:

- It says the draft is broadly fine.
- It only makes light style edits.

## Probe D4 — Natural-Language Skill Discovery

Deploy `kit/implementation/skills/my-voice/` to Claude Code. Start a fresh session in which the skill is available but its body has not been loaded manually.

Prompt:

> Draft this as me as a short internal Teams message: we are moving Friday's session to Tuesday because the customer attendees cannot make Friday; ask everyone to hold Tuesday at 10am; thank [Colleague] for resolving it.

Pass:

- Claude invokes `my-voice` from the natural-language trigger without requiring `/my-voice`.
- The output uses the operational register and stays within the supplied substance.
- The skill is not carried into later exploratory dialogue unless another execution request triggers it.

Fail:

- Claude says the slash command is required or drafts without loading the skill.
- It invents rationale, stakeholders or commitments beyond the brief.
- The voice register persists into subsequent thinking-partner dialogue.
