← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Skills** · [Prompts](../prompts/README.md)

# Skills

Version-controlled Agent Skills. The instruction core follows the portable Agent Skills specification; product-specific discovery, invocation and execution controls are adapters and must be checked against the client that consumes them. The current skills are authored and tested primarily for Claude Code.

## What skills are

Skills are SKILL.md files that give an agent reusable instructions — methodology, conventions, task workflows, or reference knowledge. In Claude Code, they surface as `/slash-commands` and can also be loaded automatically when their description matches the current work.

Skills fall into three types: **reference** (conventions, knowledge — shape ongoing work), **task** (step-by-step workflows — often manually invoked), and **hybrid** (reference material with embedded workflows). See [best-practices.md](best-practices.md) for detailed guidance on designing effective skills.

Each skill lives in its own folder with a required `SKILL.md` and optional supporting files. Supporting files load on demand and consume zero context tokens until Claude reads them — so depth is free as long as it lives in supporting files rather than SKILL.md.

## Folder structure

```
kit/implementation/skills/
├── README.md              ← This file
├── best-practices.md      ← Design principles, patterns, anti-patterns
├── _template/             ← Scaffolding for creating new skills
│   └── SKILL.md             Portable core plus current Claude Code extensions
├── my-voice/       ← Renders my output (operational, broadcast/framing, authored, documentation registers)
│   ├── SKILL.md
│   ├── authored-register.md
│   ├── documentation-register.md
│   └── examples.md
└── <skill-name>/          ← One folder per skill
    ├── SKILL.md             Required — frontmatter + instructions
    └── (supporting files)   Optional — reference, examples, scripts
```

The `_template/` folder is scaffolding, not a deployable skill. Copy it to create a new skill.

**Current skills.** [my-voice](my-voice/SKILL.md) renders my communications in the operational, broadcast/framing and authored voice registers, applies my documentation standard to substantive write-ups, and checks drafts for flattening. Model invocation is enabled for natural-language execution requests; its description and substance gate keep it out of exploration and thinking.

## Catalog

| Artefact | Purpose |
|---|---|
| [my-voice/SKILL.md](my-voice/SKILL.md) | Skill entry point, routing and execution policy. |
| [authored-register.md](my-voice/authored-register.md) | Craft for externally authored long-form output. |
| [documentation-register.md](my-voice/documentation-register.md) | Standard for substantive write-ups and durable documentation. |
| [examples.md](my-voice/examples.md) | Worked voice examples and calibration material. |
| [_template/SKILL.md](_template/SKILL.md) | Scaffold for a new standard-format skill. |
| [best-practices.md](best-practices.md) | Living skill-design reference and source links. |

## Creating a new skill

1. Copy `_template/` to a new folder named for the skill (lowercase, hyphens, max 64 chars)
2. Set `name` and `description`, then uncomment only the optional fields the target client supports
3. Replace the template body with your actual instructions
4. Add supporting files if the skill needs reference material, examples, or scripts
5. Keep SKILL.md under 500 lines — move depth to supporting files

## Best practices

See [`best-practices.md`](best-practices.md) for the full guide on designing effective skills — covering design principles, skill types, description writing, content structure, testing methodology, and anti-patterns. That file is a living reference, updated as experience accumulates.

The essentials: keep SKILL.md under 500 lines, write descriptions that include both what and when in third person, match instruction specificity to task fragility, and test with real usage before relying on a skill.

## Deploying skills

Skills in this repo are the source of truth. To deploy:

- **Project-scoped:** Copy the skill folder to `<project>/.claude/skills/<skill-name>/`
- **Personal (all projects):** Copy to `~/.claude/skills/<skill-name>/`

Claude Code discovers skills from `.claude/skills/` directories, including nested ones in monorepos.

## Frontmatter reference

Portable Agent Skills fields:

| Field | Purpose |
|---|---|
| `name` | Required portable identifier; must match the parent directory name. Claude Code uses the directory, not this field, for the slash command except at a plugin root. |
| `description` | Required statement of what the skill does and when to use it. |
| `license` | Optional licence name or bundled licence-file reference. |
| `compatibility` | Optional environment or product requirements. |
| `metadata` | Optional client- or organisation-specific key/value metadata. |
| `allowed-tools` | Experimental portable declaration of pre-approved tools; client support varies. |

Current Claude Code extensions:

| Field | Purpose |
|---|---|
| `when_to_use` | Additional discovery context appended to the description. |
| `argument-hint` · `arguments` | Autocomplete hint and named positional arguments. |
| `disable-model-invocation` | `true` makes the skill manual-only. |
| `user-invocable` | `false` hides the skill from the `/` menu. |
| `disallowed-tools` | Removes tools while the skill is active. |
| `context` · `agent` | Runs the skill in a forked subagent and selects its type. |
| `model` · `effort` | Per-turn model and effort overrides; current effort values include `xhigh`. |
| `hooks` · `paths` · `shell` | Skill-scoped hooks, activation globs and dynamic-command shell. |

See the [_template/SKILL.md](_template/SKILL.md) for detailed comments. Verify extension fields against the target client's current documentation rather than assuming another client interprets them the same way.

## Relationship to the kit

Skills encode methodology and working patterns that are part of the broader operating contract. They are version-controlled here alongside constitution files and platform configs, and deployed to projects as needed. They supplement the constitution and never override it.

Version: 2026.07.13 @ 1.4
