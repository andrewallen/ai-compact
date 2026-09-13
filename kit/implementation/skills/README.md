← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Skills** · [Prompts](../prompts/README.md)

# Skills

Version-controlled personal Agent Skills and maintenance references for first-party vendor packages and native capabilities. A plugin can bundle skills, tools, apps, hooks or other components; an opaque native capability may have no inspectable skill file. The instruction core follows the portable Agent Skills specification; product-specific discovery, invocation and execution controls are adapters and must be checked against the client that consumes them. The current skills are authored and tested primarily for Claude Code.

The current `my-voice` source is part of the [September source-alignment review](../../../governance/evidence/2026-09-constitution-alignment.md). The later [Claude deployment record](../../../governance/evidence/2026-09-claude-deployment.md) verifies the enabled v2 package against all four source files; it does not establish installation in other clients or runtime invocation. The [implementation consolidation](../../../governance/evidence/2026-09-implementation-consolidation.md) removes maintenance history from runtime skill text and aligns the documentation audience rule. Cross-model steering is documented in [model guidance](../platforms/model-guidance.md); detailed output craft remains with the skill.

## What skills are

Skills are SKILL.md files that give an agent reusable instructions — methodology, conventions, task workflows, or reference knowledge. In Claude Code, they surface as `/slash-commands` and can also be loaded automatically when their description matches the current work.

Skills fall into three types: **reference** (conventions, knowledge — shape ongoing work), **task** (step-by-step workflows — often manually invoked), and **hybrid** (reference material with embedded workflows). See [best-practices.md](best-practices.md) for detailed guidance on designing effective skills.

Each personal skill lives in its own folder with a required `SKILL.md` and optional supporting files. Put detailed references behind focused entry points, then verify actual loading in the target host. Discovery metadata, tools, retrieved files and execution output can each consume context. Supporting-file size is not a token measurement, and on-demand organisation does not make depth free.

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

**Current skills.** [my-voice](my-voice/SKILL.md) renders my communications in the operational, broadcast/framing and authored voice registers, applies my documentation standard to substantive write-ups, and checks drafts for flattening. Model invocation is enabled for natural-language execution requests. Its declared scope covers owned personal-voice output and authorised factual documentation, excluding exploration and thinking; actual discovery and loading depend on the client.

## Catalog

| Artefact | Purpose |
|---|---|
| [my-voice/SKILL.md](my-voice/SKILL.md) | Skill entry point, routing and execution policy. |
| [authored-register.md](my-voice/authored-register.md) | Craft for externally authored long-form output. |
| [documentation-register.md](my-voice/documentation-register.md) | Standard for substantive write-ups and durable documentation. |
| [examples.md](my-voice/examples.md) | Worked voice examples and calibration material. |
| [_template/SKILL.md](_template/SKILL.md) | Scaffold for a new standard-format skill. |
| [best-practices.md](best-practices.md) | Living skill-design reference and source links. |

## Cross-client capability assessment

The [package register](package-register.md) owns implementation IDs, reviewed-source/runtime identities, selection status and composition requirements. It links source evidence to capability IDs without acting as a runtime router. [Capability composition probes](../../evals/capability-composition-probes.md) provide the pilot fixtures; they have been authored, not run.

The [first-party inventory](first-party-inventory.md) validates Anthropic/OpenAI package provenance, contained skills and public-versus-local availability, including plugins. The initial [capability matrix](capability-matrix.md) maps knowledge-work and design requirements across Claude and OpenAI surfaces, distinguishing recorded settings, session exposure and unknown coverage. The [source register](source-register.md) links candidate providers and their evidence limits. The [evaluation and re-review method](review-method.md) covers token efficiency, capable thinking partners, preliminary constitution intersections and model-upgrade reviews. These are maintenance references, not runtime skills or deployment decisions.

The [implementation plan](implementation-plan.md) defines the proposed repository preparation, bounded capability trials and subsequent client deployment, including exact initial file scope, constitutional checks, efficiency measures and rollback. Batch 1 repository preparation is implemented. Client trials and deployment remain pending their defined execution scopes.

## Creating a new skill

1. Copy `_template/` to a new folder named for the skill (lowercase, hyphens, max 64 chars)
2. Set `name` and `description`, then uncomment only the optional fields the target client supports
3. Replace the template body with your actual instructions
4. Add supporting files if the skill needs reference material, examples, or scripts
5. Keep SKILL.md under 500 lines — move depth to supporting files
6. Add the skill and its maintained supporting files to this index

## Best practices

See [`best-practices.md`](best-practices.md) for the full guide on designing effective skills — covering design principles, skill types, description writing, content structure, testing methodology, and anti-patterns. That file is a living reference, updated as experience accumulates.

The essentials: keep SKILL.md under 500 lines, write descriptions that include both what and when in third person, match instruction specificity to task fragility, and test with real usage before relying on a skill.

## Deploying skills

The filesystem routes below describe Claude Code. For Claude Chat/Cowork client enablement and verified source alignment, see the [Claude configuration baseline](../platforms/claude/configuration-baseline.md). An enabled skill need not be an exact copy of this source; compare all packaged files when verifying deployment.

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
