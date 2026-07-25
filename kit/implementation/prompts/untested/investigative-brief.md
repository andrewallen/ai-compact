# Investigative Brief

**What it does.** Structures background research on individuals, organisations, or commercial relationships into a staged workflow that scopes, gathers, cross-references, and flags gaps.

**When to use it.** Due diligence, stakeholder research, pre-meeting preparation requiring depth, any investigative task where cross-referencing matters and a single prompt would try to do too much.

## Prompt

> I need to conduct background research on [ENTITY] in the context of [PURPOSE/REASON].
>
> Work through this in stages:
> 1. First, identify the categories of information needed and the questions each category should answer
> 2. For each category, state what you find, your confidence level, and what you could not determine
> 3. Review findings across categories — identify connections, contradictions, or patterns that warrant further investigation
> 4. Generate a fact check list: what claims should be independently verified?
>
> Present findings as: executive summary (200 words), detailed findings by category, cross-references and flags, gaps and recommended next steps.

## Notes

This prompt is designed to replace the "multi-page sprawl" pattern where someone tries to do everything in a single prompt. Each stage does one type of thinking. The fact check list at the end is critical — it makes the model's uncertainty explicit and actionable.

For sensitive subjects, add: "Draw only from verifiable public sources. Flag clearly when something is inferred rather than established."

Version: 2026.04.02 @ 1800