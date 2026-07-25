# Task Decomposition

**What it does.** A meta-prompt: before executing a complex task, generates the optimal prompt chain by identifying the distinct reasoning types involved and proposing a staged approach.

**When to use it.** When a task feels too large or multi-faceted for a single prompt but you are not sure how to break it down. The AI identifies the structure before you commit to one.

## Prompt

> Before we start, I want you to plan how to approach this.
>
> The task is: [DESCRIBE THE TASK]
>
> Identify the distinct types of thinking this task requires. Propose a staged approach where each stage has a single clear objective and one type of reasoning. Show me what information flows between stages. Then wait for me to confirm or adjust before executing.

## Notes

This is the most meta prompt in the collection. It asks the model to design the prompt architecture before using it. Useful when you do not know the shape of the task well enough to decompose it yourself.

May be redundant with exploratory mode in some cases — but exploratory mode is open-ended, while this prompt produces a concrete execution plan. Test both and see which produces better results for your task type.

Version: 2026.04.02 @ 1800