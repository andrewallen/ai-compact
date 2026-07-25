← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Prompts** · [Skills](../skills/README.md)

# Prompts

Reusable starting points for specific types of thinking, analysis, or output. This folder holds prompts that have proven useful across conversations — captured here so they can be reused, refined, and shared.

## What prompts are

Prompts are atomic. Each one is a single markdown file containing a prompt that drives a conversation in a specific direction — a thinking frame, an analysis pattern, a drafting trigger, a way of approaching a particular type of problem. They carry minimal metadata: what the prompt is for, when to use it, and the prompt itself.

Prompts are the lightest-weight layer in the kit. Constitution files define who I am and how the AI should work with me. Skills encode reusable methodology with structure, frontmatter, and optional supporting files. Prompts sit underneath both — they are useful ways of interacting with the model, captured before they need that structure.

## How prompts relate to skills

A prompt that accumulates structure graduates into a skill. If a prompt starts needing supporting files, step-by-step instructions, or slash-command integration, it has outgrown this folder and belongs in `kit/implementation/skills/`. The graduation path is by design — prompts are where useful patterns are captured; skills are where they mature.

The distinction is friction. Adding a prompt should take seconds: create a file, paste the prompt, add a brief description. No frontmatter, no YAML, no folder structure. The barrier to capture is near zero, because the value is in building the collection over time.

## Folder structure

```
kit/implementation/prompts/
├── README.md              ← This file
├── _template.md           ← Starting point for new prompts
├── untested/              ← Experimental prompts without live-use evidence
└── <prompt-name>.md       ← One file per prompt
```

Tested prompts sit at the root of this folder. `untested/` is an experimental catalogue: its contents are available for deliberate trials but carry no commitment to promotion. A prompt moves to the root only after successful live use, evidence-based refinement, and a check that it remains subordinate to the constitution rather than forcing symmetry, convergence, unsupported inference or premature production.

## Catalog

| Status | Prompt | Purpose |
|---|---|---|
| Tested | [Project discovery interview](discovery-interview.md) | Surface the real goal and load-bearing constraints before planning. |
| Experimental | [Untested prompt index](untested/README.md) | Eleven candidate prompts available for deliberate trial. |
| Template | [_template.md](_template.md) | Minimal starting structure for a new prompt. |

## Adding a new prompt

1. Copy `_template.md` to a new file in `untested/` named for the prompt (lowercase, hyphens, `.md`)
2. Fill in the name, description, and the prompt itself
3. Add usage notes or variations if they are useful — leave them out if they are not

The template is minimal by design. A prompt file needs to answer three questions: what is this, when would I use it, and what do I say to the model.

## Using prompts

These are reference material, not executable. Copy the prompt text into a conversation when the situation fits. The prompts work best when the constitution files are already loaded — they complement the operating contract rather than replacing it.

## Relationship to the kit

Prompts capture patterns of interaction that do not need the structure of a skill. They are version-controlled here alongside constitution files, platform configs, and skills. They invoke the system but never become a competing source of truth.
