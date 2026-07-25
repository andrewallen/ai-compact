← [Home](../../README.md) · [Kit](../README.md) · [Philosophy](../philosophy/README.md) · **Constitution** · [Roles](../roles/README.md)

# Constitution

Model-agnostic source-of-truth files that define identity, calibration, the operating contract, and a conditional professional overlay. These are the files everything else in the kit derives from.

## What constitution files are

Constitution files are plain markdown with no product-specific syntax. They work on any AI product that can read markdown instructions — Claude, ChatGPT, or anything else. They carry the operating contract: who I am, how I think, how the model should work with me, and what quality standard it is held to.

These files are designed to be loaded into conversations, projects, or agent sessions that read them from the filesystem. They are not documentation — they are active instructions that govern model behaviour when loaded.

## File hierarchy

Each file declares its own classification so the system works regardless of load order. The files serve complementary functions.

| Level | File | Role |
|---|---|---|
| 1 — Calibration | [01-calibration.md](01-calibration.md) | Standards, thinking style and intellectual level. Shapes interpretation. |
| 2 — Binding rules | [02-operating-contract.md](02-operating-contract.md) | Operating contract. The expansion function, mode detection and posture, the partner register, voice principles, sensitivity flagging. |
| 3 — Conditional | [03-professional-overlay.md](03-professional-overlay.md) | Microsoft/CDTO role and professional thinking lenses. Only when relevant. |

The bootstrap (`00-bootstrap.md`) defines this hierarchy. It is the insurance layer — if files load out of order or without external instruction, the bootstrap ensures correct interpretation.

See [00-bootstrap.md](00-bootstrap.md) for the full declaration.

Voice reproduction is not in these files. The durable voice principles live in [02-operating-contract.md](02-operating-contract.md); the full craft and the model-specific tuning live in the [my-voice skill](../implementation/skills/my-voice/SKILL.md), summoned at execution. This keeps the always-loaded constitution lean and keeps the assistant's own register distinct from mine while we think.

## Folder structure

```
kit/constitution/
├── README.md                    ← This file
├── 00-bootstrap.md              File hierarchy (insurance layer)
├── 01-calibration.md            Calibration — standards, thinking style, intellectual level
├── 02-operating-contract.md     Binding rules — operating contract
└── 03-professional-overlay.md   Conditional — Microsoft/CDTO role
```

## Loading constitution files

Load all four files for the full constitution. For conversations that do not involve the professional role, omit `03-professional-overlay.md` to save token budget — the core operating set is bootstrap + calibration + operating contract.

The numbered prefixes improve load-order odds but do not guarantee it. The self-declaring classifications in each file are the safety net.

## Relationship to the kit

The constitution is the runtime foundation. Everything else either derives from it, supplements it, or governs its evolution. The implementation layer defines how the contract deploys and executes without becoming a second source of truth.
