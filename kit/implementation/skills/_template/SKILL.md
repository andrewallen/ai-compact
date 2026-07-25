---
# name: my-skill-name
#   Portable Agent Skills field: required and must match the parent directory.
#   Lowercase letters, numbers, hyphens only (max 64 chars; no leading,
#   trailing or consecutive hyphens).
#   Claude Code normally derives the /slash-command from the directory name;
#   name changes the display label, except for a plugin-root SKILL.md.
#
# description: What this skill does and when to use it.
#   Portable Agent Skills field: required (max 1024 characters).
#   Clients use this to decide when the skill applies.
#   Include BOTH what it does AND when to use it.
#   Write in third person ("Generates..." not "I can help...").
#   Be specific with trigger terms — vague descriptions undertrigger.
#   Example: "Extract text and tables from PDF files. Use when working
#   with PDF files, forms, or document extraction."
#
# license: Proprietary. LICENSE.txt has complete terms
#   Portable optional field: licence name or bundled licence-file reference.
#
# compatibility: Requires git and network access
#   Portable optional field (max 500 characters): environment or product needs.
#
# metadata:
#   author: example-owner
#   version: "1.0"
#   Portable optional mapping for client- or organisation-specific metadata.
#
# --- Claude Code discovery and invocation extensions ---
#
# when_to_use: Use when the user asks for [specific trigger].
#   Additional discovery context appended to description.
#
# argument-hint: [optional-args]
#   Hint shown during autocomplete. E.g. [issue-number] or [filename].
#
# arguments: source destination
#   Named positional arguments for $source and $destination substitutions.
#
# disable-model-invocation: false
#   Set true to prevent Claude from loading this automatically.
#   User can still invoke with /skill-name.
#   Use for: deployments, sends, irreversible side effects.
#
# user-invocable: true
#   Set false to hide from the / menu.
#   Claude can still load it automatically.
#   Use for: background knowledge that isn't a command.
#
# --- Portable execution field and Claude Code execution extensions ---
#
# allowed-tools: Read, Grep, Glob
#   Portable experimental field, also supported by Claude Code.
#   Pre-approves these tools while the skill is active; client support varies.
#
# disallowed-tools: WebSearch, Write
#   Claude Code extension: remove tools while the skill is active.
#
# context: fork
#   Run in a forked subagent context (isolated, no conversation history).
#   Use for research, analysis, or tasks that should not see prior turns.
#
# agent: Explore
#   Which subagent to use when context: fork is set.
#   Options: Explore, Plan, general-purpose, or custom subagent names.
#
# model: sonnet
#   Model override when this skill is active.
#
# effort: high
#   Effort level. Current options: low, medium, high, xhigh, max;
#   availability depends on the selected model.
#
# hooks:
#   PreToolUse: []
#   Claude Code extension: hooks scoped to this skill's lifecycle.
#
# paths: "src/**/*.ts"
#   Glob patterns that limit when this skill activates.
#   Claude loads the skill only when working with matching files.
#
# shell: bash
#   Shell for !`command` blocks. Options: bash (default), powershell.
---

# Skill Name

Brief description of what this skill does, who it is for, and when it should be used.

## Instructions

Step-by-step instructions Claude follows when this skill is invoked. Write as direct instructions, not documentation.

Match specificity to the task: procedural tasks (deployments, migrations) need explicit steps with validation checkpoints. Analytical tasks (research, review) need guidelines and heuristics with room for judgement.

1. First step
2. Second step
3. Third step

## Supporting files

Reference any additional files bundled with this skill:

- `reference.md` — detailed reference material (keep SKILL.md under 500 lines; move depth here)
- `examples.md` — usage examples
- `scripts/` — utility scripts referenced by the instructions

## Variables

These placeholders are replaced at runtime:

- `$ARGUMENTS` — all arguments passed when invoking the skill
- `$ARGUMENTS[0]`, `$ARGUMENTS[1]` — individual arguments by position; `$0`, `$1` are shorthand
- `$name` — named positional argument declared in the `arguments` field
- `${CLAUDE_SKILL_DIR}` — directory containing this SKILL.md
- `${CLAUDE_PROJECT_DIR}` — current project root
- `${CLAUDE_SESSION_ID}` — current session ID
- `${CLAUDE_EFFORT}` — current effort level
