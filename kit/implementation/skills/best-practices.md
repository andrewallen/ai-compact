← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Skills](README.md) · **Best practices**

# Skills Best Practices

A living reference for designing effective skills. Grounded in Anthropic's official guidance and refined through experience. Update this as patterns emerge from real use.

## Design principles

**Progressive disclosure.** Put navigation and decision logic in SKILL.md and detail in supporting files. Metadata, bodies, references and tools have different loading paths that must be verified in the actual host. Discovery descriptions can be shortened or omitted, and reading a reference introduces its own cost. Do not assume a fixed token count per skill or infer savings from installed file size. Measure actual exposure, loading and accepted-task usage where observable.

**Degrees of freedom.** Match instruction specificity to how fragile the task is. Procedural tasks — deployments, migrations, anything where a wrong step has consequences — need low freedom: specific steps, explicit commands, validation checkpoints. Analytical tasks — code review, research, exploration — need high freedom: guidelines, heuristics, and room for judgement. The question is not "how detailed should my skill be?" but "how much latitude does this task safely tolerate?"

**Description-driven discovery.** Claude decides whether to load a skill based on its description. The description must include both what the skill does and when to use it. Write in third person — descriptions are injected into the system prompt, and first person causes discovery problems. Be specific with trigger terms rather than generic. Test both intended and unwanted activation. Broad triggers can load conflicting workflows or move exploration into production; neither undertriggering nor overtriggering is universally the less costly failure.

**One-level-deep references.** SKILL.md should link directly to every supporting file Claude might need. Avoid chains where SKILL.md references A.md, which references B.md, which references C.md. Claude may partially read files in nested chains rather than loading them completely. All important files should be reachable in one step from SKILL.md.

**Conciseness.** Keep SKILL.md under 500 lines. Only include what Claude does not already know. Challenge each sentence: does Claude genuinely need this, or am I explaining something it already understands? The context window is a shared resource — every token consumed by a skill is unavailable for the actual work.

## Skill types

**Reference skills** carry conventions, style guides, domain knowledge, or organisational context. Their descriptions invite activation for matching work where the client supports it; actual discovery and invocation must be verified. They shape how Claude does its existing work rather than introducing new tasks. Examples: API conventions, coding standards, brand guidelines.

**Task skills** carry step-by-step workflows for specific actions. They are often invoked manually because they involve side effects or because timing matters. Examples: deployment procedures, PR creation workflows, data migration scripts. Set `disable-model-invocation: true` for task skills that should only run when explicitly requested.

**Hybrid skills** combine reference material with embedded workflows. The reference content shapes ongoing work; the workflow triggers for specific actions within that domain. These are common in practice — a database skill might carry schema conventions (reference) plus a migration procedure (task).

## Invocation control

The following table describes intended Claude Code invocation controls, not portable permissions or guarantees in another client. Verify support and actual discovery before deployment:

| | Model can invoke | Model cannot invoke |
|---|---|---|
| **User can invoke** | Default — both trigger it | `disable-model-invocation: true` — manual only |
| **User cannot invoke** | `user-invocable: false` — background knowledge only | Both set — skill is effectively disabled |

**Use `disable-model-invocation: true`** for skills with side effects: deployments, sending messages, creating PRs, deleting resources. Anything irreversible or visible to others. The user controls timing.

**Use `user-invocable: false`** for background knowledge that Claude should apply automatically but that does not make sense as a slash command. Legacy system context, project-specific conventions, domain knowledge that informs decisions without being directly invoked.

## Writing effective descriptions

The description field determines whether Claude ever loads the skill. A weak description means the skill sits unused regardless of how good its content is.

**Include what and when.** "Extract text and tables from PDF files. Use when working with PDF files, forms, or document extraction" gives Claude two paths to discovery — the capability and the trigger context.

**Use specific trigger terms.** "Analyzes Excel spreadsheets and generates summary charts. Use when analyzing .xlsx files, spreadsheets, pivot tables, or financial data" is better than "Helps with data analysis." Include the terms a user would naturally use.

**Write in third person.** "Generates deployment scripts and runs pre-flight checks" — not "I can help you deploy." Descriptions inject into the system prompt as metadata about available tools.

**Avoid:** "Helps with documents," "Processes data," "Useful utility for files." These match too many contexts to be useful and too few to reliably trigger.

## Structuring content

**SKILL.md as table of contents.** For larger skills, SKILL.md should provide an overview and navigation, pointing Claude to the right supporting file for each sub-task. Keep the decision logic in SKILL.md; keep the depth in supporting files.

**Supporting files for depth.** Reference material, examples, API documentation and lengthy templates belong in separate files. Link relevant resources directly and verify what the host actually reads. Unread content is not the same as measured total savings; metadata and tool exposure still matter.

**Template pattern.** When a skill must produce output in a strict format, provide the exact template structure. Use explicit language: "ALWAYS use this exact template." For flexible guidance, invite adaptation based on context.

**Conditional workflow pattern.** When a skill handles multiple task types, branch explicitly:
```
1. Determine the task type:
   - Creating new content → follow "Creation workflow" below
   - Editing existing content → follow "Editing workflow" below
2. [detailed steps for each branch]
```

**Feedback loop pattern.** For quality-sensitive tasks, build validation into the workflow: run a check, fix any issues, re-run the check, proceed only when clean. This is more reliable than a single pass with instructions to "be careful."

## File organisation

One folder per skill. SKILL.md is required; everything else is optional.

```
skill-name/
├── SKILL.md              Required — overview, navigation, core instructions
├── reference.md          Detailed reference material
├── examples.md           Input/output examples
├── templates/            Output templates
│   └── report.md
└── scripts/
    └── validate.sh       Utility scripts
```

A script can run without its source being loaded into model context, but source inspection and output may both consume context. Review scripts and dependencies before execution. Reuse deterministic checks when they improve reliability; do not assume every bundled script is correct or cheaper.

## Portability and product extensions

The portable Agent Skills core is the folder, `SKILL.md`, the required `name` and `description`, and the standard's optional `license`, `compatibility`, `metadata` and experimental `allowed-tools` fields. Invocation control, command naming, arguments, model and effort overrides, hooks, path filters and subagent execution are client behaviour. Claude Code supports them as extensions; another client may ignore them or use different metadata.

Keep the instruction body and supporting files portable where possible. Treat each client's discovery, permissions and execution semantics as an adapter that must be verified in that client.

## Naming conventions

Use gerund form or noun phrases. In Claude Code the containing directory normally becomes the `/slash-command`; the frontmatter `name` is the portable identifier and display label and should match that directory.

**Good:** `processing-pdfs`, `analyzing-data`, `pdf-processing`, `data-analysis`, `reviewing-prs`, `deployment-checks`

**Avoid:** `helper`, `utils`, `tools`, `documents`, `my-skill`, `anthropic-helper`. Names should describe the capability, not the category.

Lowercase letters, numbers, and hyphens only. Maximum 64 characters.

## Testing and iteration

**Evaluation-driven development.** Define three or more representative scenarios before writing the skill. Run the native configuration with the applicable existing contract and without the candidate addition to establish a baseline. Keep model/effort, tools and inputs matched. Write minimal instructions — only what the baseline missed. Iterate until the skill consistently improves the baseline.

**Two-Claude method.** Use one Claude session (the author) to write and refine the skill. Use a separate session (the tester) to exercise it on real tasks. The tester has no memory of the authoring process, so it reveals assumptions the author missed. Feed observations back to the author.

**What to observe during testing:**
- Does Claude find and read the right supporting files?
- Does it navigate the file structure as intended?
- Does it miss important content or get confused by ambiguous instructions?
- Do certain sections get ignored or misinterpreted?
- Does it over-apply the skill in contexts where it should not activate?

**Iterate the cycle:** observe → refine → test. The first version is a hypothesis. Real usage is the evidence.

## Anti-patterns

**Vague descriptions.** "Helps with documents" matches everything and triggers for nothing. Be specific about what and when.

**Too many options without a default.** "You can use X, Y, Z, or W" forces Claude to choose without enough context. Provide a default approach with escape hatches for edge cases.

**Deeply nested references.** SKILL.md → A.md → B.md → C.md causes partial reads. Keep everything one level from SKILL.md.

**Time-sensitive information.** "After August 2025, use the new API" becomes stale. If deprecation context is needed, use a clearly labelled section that can be updated.

**Inconsistent terminology.** Mixing "API endpoint," "URL," "route," and "path" for the same concept creates ambiguity. Pick one term and use it throughout.

**Over-explanation.** Explaining what PDFs are, how HTTP works, or what a database does wastes tokens on knowledge Claude already has. Only include what is specific to your context.

**Assuming packages are installed.** If a skill depends on specific tools or libraries, state the dependency explicitly. Do not assume the environment is pre-configured.

**First person in descriptions.** "I can help you deploy" causes discovery issues because descriptions inject into the system prompt as metadata, not as Claude's voice.

**Magic numbers without justification.** If a timeout is 47 seconds or a retry count is 3, explain why. Constants without reasoning look arbitrary and may be changed incorrectly.

## Package review and maintenance

Use the [package register](package-register.md) for identity and disposition and the [review method](review-method.md) for comparisons. First inspect the complete reachable package: skills, scripts, hooks, agents, commands, apps/MCP, references and templates. Record provenance and licence at component level where relevant, required access, all side effects, exact target surface, invocation and fallback. A marketplace publisher is not evidence that every component is first-party authored.

A primary workflow may use complementary design, format and editorial stages. Test whether their composition duplicates gates, changes stance or claims unauthorised persistence/publication. Use [composition probes](../../evals/capability-composition-probes.md) for positive/negative activation and existing contract fixtures for boundaries. Metadata exposure alone does not prove a body loaded or a task succeeded.

Review changed descriptions, dependencies and effects after a package/host/model update or repeated friction. Compare marginal benefit against the native baseline and a smaller adaptation when justified. Record quality, repairs, actual usage where available and unknowns; retain capable models for substantive judgement. Reject unnecessary additions and propose retirement of obsolete workarounds with exact scope and rollback limits. No automatic update or deletion follows from the register.

## Resources

| Source | URL |
|---|---|
| Anthropic skills documentation | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Skill authoring best practices | [Anthropic skill-authoring guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) |
| Official skills repository | [anthropics/skills](https://github.com/anthropics/skills) |
| Agent Skills standard | [Agent Skills](https://agentskills.io) |
