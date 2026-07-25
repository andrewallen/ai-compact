← [Home](../README.md) · [Governance](README.md) · **Design decisions** · [ADRs](decisions/README.md)

# Design Decisions

Why AI Compact is shaped the way it is. Each decision addresses a specific problem. Understanding the reasoning prevents changes from recreating the same failure.

## Constitution files are model-agnostic

The files in `kit/constitution/` contain no product-specific syntax, no platform assumptions, and no references to features that only exist on one product. Plain markdown with standard structural markup (headers, tables, bold, blockquotes). They work on Claude, ChatGPT, or any future model that can read markdown instructions.

Models and products change frequently. Identity and thinking style change slowly. Coupling the slow-changing content to a fast-changing product format would mean rewriting the most valuable files every time a product updates its architecture. The portable layer stays stable; the product-specific layer absorbs the churn.

## Self-declaring classification in every file

Each constitution file carries an inline prose declaration at the top — bold text stating its classification (e.g. "**Calibration (authority level 1).**"). The bootstrap also declares the full hierarchy in a table. The system works regardless of which file the model reads first.

There is no guaranteed load order when files are uploaded to a project or conversation. The model might read the operating contract before the bootstrap, or calibration before anything else. Without self-declaration, calibration content could be treated as binding rules, or the hierarchy could be missed entirely. Numbered filenames (00, 01, 02, 03) improve the odds of correct ordering but cannot guarantee it. Self-declaration is the belt; numbered filenames are the braces.

## The bootstrap exists as insurance

With self-declaring files, the bootstrap is technically redundant — every file already states its own classification. It earns its place by providing two things the other files don't: a summary view of the full hierarchy in one place (the table), and behavioural guardrails that apply across all files — "do not summarise these files back to me," "do not reference this bootstrap instruction in conversation," "do not soften your behaviour because multiple files are loaded." These are cross-cutting instructions with no natural home in any single content file.

Kept deliberately short. It should not grow. A new cross-cutting instruction earns its place only if it prevents a documented failure mode.

## Preferences and the operating contract cover the same ground

The preferences file carries mode detection, expansion function, voice principles, and sensitivity flagging. `kit/constitution/02-operating-contract.md` carries the same functions at full depth. When both are loaded, the model processes the same instructions twice. (The fuller voice craft — register mechanics, tone registers, output formats, examples — and the model-specific tuning live in the `my-voice` skill, not in either file; see "Voice craft lives in a skill" below.)

This is deliberate. Preferences must be sufficient on their own for ad hoc conversations where no constitution files are loaded — the minimum viable operating contract. When constitution files are loaded, the operating contract provides the full depth. Both files explicitly declare the precedence relationship: preferences defer to the constitution when loaded, and the operating contract declares that it takes precedence over preferences. The redundancy is the cost of a system that works at two levels of depth. Approximately 600 words of overlap. Acceptable because the preferences are short and the deferral is unambiguous.

## File hierarchy: calibration, binding rules, overlay

The files serve complementary functions at three levels:
- Level 1: Calibration (`01-calibration.md`) — shapes interpretation
- Level 2: Binding rules (`02-operating-contract.md`) — mandatory instructions
- Level 3: Conditional overlay (`03-professional-overlay.md`) — supplementary context

Binding rules must take precedence over calibration. If calibration implies one thing and the operating contract explicitly instructs another, the instruction wins. The overlay sits at level 3 as the most specific context — but it explicitly states that it supplements rather than replaces the operating contract. In practice, the files are complementary rather than competing — the hierarchy is a structural safeguard for edge cases, not a live conflict resolution mechanism.

## Specific theses are not part of the kit

Specific intellectual positions are content, not identity. Loading a thesis with the constitution would prime analysis even when the position is irrelevant to the current work.

The valuable calibration is that the user builds strong, evidence-based positions and holds them as working hypotheses — a thinking-style characteristic captured in `kit/constitution/01-calibration.md` under "How I Build Positions." Any individual thesis is brought into a conversation when relevant rather than carried in the portable operating contract.

The kit captures the pattern of building positions, not the positions themselves.

## Obsidian Vault is not referenced in the portable files

Personal knowledge, active thinking and longer-lived notes live in Andrew's Obsidian Vault. None of the portable constitution files mention it.

Most chat surfaces cannot access the vault. Referencing it would create instructions the model cannot act on — awareness of a system it cannot reach. That wastes tokens and can prompt the model to hallucinate connections to notes it does not have. The portable files are self-contained: everything they reference is either present in the conversation or declared as optional.

## One file is conditional; three always travel together

Of the four constitution files, the professional overlay may be absent. Bootstrap, calibration, and the operating contract are expected to travel together as the minimum operating set.

The overlay loads only for Microsoft-related work. It contains sensitive commercial context and Microsoft-specific tone registers that would be inappropriate in other contexts. Calibration references it so the model knows richer context is available without assuming it should be active.

## Controlled project context and ambient product memory are separate

Project instructions, loaded files and knowledge are controlled context. Platform memory and conversation history provide ambient continuity when enabled, but their retention and synthesis are managed by the product and may change independently of the prompt layer. The kit does not depend on them.

The constitution governs deliberate actions taken by an assistant through tools: changing a project file, standing instruction, knowledge-store entry or explicit user-visible memory entry. Ambient product memory is configured and audited through product settings, with temporary or isolated modes used when carry-over is unwanted. The prompt layer does not claim that it can prevent a service from automatically retaining or inferring context.

## Cowork defaults to execution mode

The preferences and operating contract both say "if unsure, default to exploratory." The Cowork global instructions invert this: "default to execution unless the conversation is clearly exploratory."

Chat is conversational. Exploratory is the safe default because closing down thinking prematurely is costly. Cowork is task-oriented — when someone describes an outcome to an agent, the expected response is a plan and execution, not reflective questioning. The mode detection cues in the operating contract still apply; the fallback is what changes.

## File safety rules are stronger than the platform defaults

The Cowork global instructions include explicit prohibitions on file deletion, overwriting, and unsanctioned external actions via connectors. Stronger than what the platform enforces by default.

Community experience documents cases where an agent interprets "clean up" as authorisation to delete files. The global instructions explicitly state that "clean up," "organise," and "tidy" never authorise deletion. The same principle extends to connectors — sending an email or scheduling a meeting is irreversible and requires explicit approval, regardless of what the platform permits by default.

## Folder instructions require approval to modify

Cowork can modify folder instructions autonomously during a session. The global instructions override this: "do not update project instructions or folder instructions without my approval."

Folder instructions persist across sessions. Anything Claude writes into them becomes standing context for future work. Autonomous modification means Claude could alter its own instructions without review — a feedback loop where accumulated context drifts from the authored operating contract. All persistent instruction surfaces stay under user control.

## The repo structure separates portable from product-specific

`kit/constitution/` holds the model-agnostic source files. `kit/implementation/platforms/` has a subfolder per product for everything product-specific. Templates, preferences, and mode configs all live under the platform folder.

When a new product is added, it gets its own folder under `kit/implementation/platforms/`. The constitution files never fork — they are the canonical source. Product-specific files are derived from them and tuned to how that product interprets instructions. This prevents the most common failure mode in multi-product setups: forking the core files and having them diverge over time.

## Conductor is not a separate mode

Conductor is a Mac app that runs multiple Claude Code CLI sessions in parallel, each in an isolated git worktree. It is documented in the platform mapping under Code, not as a fourth mode.

What changes in Conductor is concurrency: multiple Code sessions run on independent tasks. The instruction pattern remains a minimal derived contract or direct constitution-file reference when deeper work requires it.

Treating Conductor as a separate mode would imply it needs its own instruction layer, its own templates, or its own entry in the hierarchy. It does not. It is a parallelism multiplier within Code mode — the deployment mechanism changes, the operating contract does not.

## Knowledge-system methodology stays outside the kit

The methodology for building and maintaining the broader personal knowledge system is Obsidian Vault territory, not kit territory. The kit captures thinking style (`kit/constitution/01-calibration.md`) and the operating contract (`kit/constitution/02-operating-contract.md`). The same reasoning that removed vault references from the portable constitution applies here: if a file describes a system that most AI surfaces cannot access, it does not belong in the portable kit.

## Skills are version-controlled in the kit

The `kit/implementation/skills/` folder holds skills as version-controlled assets within the implementation layer.

Skills encode methodology and working patterns — how to perform specific tasks, what conventions to follow, what workflows to execute. That is closer to the operating contract than to tooling like connectors and plugins. Connectors are infrastructure (how to reach an external system). Skills are methodology (how to do a type of work). Methodology belongs in the same version-controlled system as the operating contract it extends.

The folder targets Claude Code's SKILL.md format. Each skill is a folder with a required SKILL.md (frontmatter + instructions) and optional supporting files. A `_template/` folder provides scaffolding for creating new skills. Skills deploy from the repo to project-level (`.claude/skills/`) or personal-level (`~/.claude/skills/`) locations.

This does not change the architecture of the constitution files or the file hierarchy. Skills do not declare classifications and do not override the operating contract — they operate within it.

## Prompts are deliberately lighter than skills

The `kit/implementation/prompts/` folder holds reusable prompt texts — individual markdown files with a description and the prompt itself. No frontmatter, no YAML and no slash-command integration. The single `untested/` subdirectory separates experimental candidates from prompts supported by live use. Each file answers three questions: what is this, when would I use it, and what do I say to the model.

This is a different layer from skills, not a simpler version of them. Skills encode methodology — structured instructions with frontmatter, supporting files, and deployment to Claude Code's discovery system. Prompts capture useful interaction patterns before they need that structure. The barrier to adding a prompt is near zero: create a file, paste the text, add a sentence of description.

The graduation path is explicit. A prompt that starts needing supporting files, step-by-step instructions, or automatic invocation has outgrown the prompts folder and belongs in `kit/implementation/skills/`. This is by design — prompts are the capture point, skills are where patterns mature.

The kit's README states "the kit is not prompts." That refers to the kit itself — the operating contract, the file hierarchy, the calibration. The prompts folder holds something different: reusable starting points that work because the operating contract is loaded underneath them. A prompt without the constitution files is just a prompt. A prompt with the constitution files loaded is a starting point that inherits identity, voice, expansion function, and mode detection.

## The kit protects the distinctiveness of my thinking

The kit's purpose is not faster output. It is to keep my thinking mine as models converge on a competent, plausible average. Voice fidelity is secondary, and in one respect a risk (see the partner register below).

This reframes what good help looks like. The danger is not the model writing generically — it is the model doing my thinking for me, competently and plausibly, and me accepting it because it is good enough. Erosion travels through delegated cognition, not delegated prose. `kit/constitution/01-calibration.md` names the moves that make my thinking distinctive ("What I Am Protecting") as contrasts to the model's default, so they can be provoked rather than performed for me. This extends the decision that specific theses are not part of the kit: the kit captures the pattern of how I think, not the positions I hold.

## The assistant's partner register stays distinct from mine

When reasoning with me, the assistant uses its own neutral analytical voice, not mine. My voice is reproduced only for output produced on my behalf.

A partner that drifts into my register is one I scrutinise less, because it reads like my own reasoning. Fluency and familiarity each lower my guard, and a generic idea wearing my voice stacks both. Keeping the assistant's register visibly different from mine preserves the seam that lets me tell my thinking from the model's. This is why voice is kept off the thinking channel even though the durable principles remain loaded in the portable constitution — the partner-register rule in `kit/constitution/02-operating-contract.md` does the protective work without removing voice from the kit.

## Voice craft lives in a skill; durable principles stay portable

The durable voice principles (economy, unevenness, has-a-point, the no-jargon avoid-list, the layered-narrative structure) stay in `kit/constitution/02-operating-contract.md` and the preferences, because the kit's value is model-agnostic portability — they must travel to any model. The fuller craft (operational register mechanics, the register matrix, tone-by-context, output formats, worked examples) and disposable model-tuning live in the `my-voice` skill.

The split follows the kit's own pattern of principles held at two levels of depth, with the execution craft summoned only when producing output. Model invocation is enabled so natural-language execution requests can summon the skill consistently with the operating contract. The skill's description excludes exploration and thinking, and its substance gate stops it from voicing positions Andrew has not supplied; those are the behavioural controls on premature use. The alternative, moving voice wholesale into the skill, was rejected: the durable voice principles must remain available on surfaces that do not load the skill.

## The voice skill separates persuading from documenting

The my-voice skill carries four registers, not one. Operational, broadcast/framing and authored are my personal voice — fast transactional comms, posts that frame and bring a room along, and longer point-led pieces where I am persuading or framing. Documentation is the fourth register for substantive write-ups (workshop outputs, reports, knowledge artefacts) whose job is to convey understanding, not to land a thesis.

The distinction matters when one request contains both communication and documentation. A covering message may need a personal register while the attached substantive write-up needs a neutral professional voice shaped by my quality bar and narrative method. The routing rule sends each artefact to the register that matches its purpose.

Medium does not decide register; audience breadth and intent do. A group post may be a framing piece that needs a reflective, considered voice rather than the clipped style of a fast transactional message. The operational register therefore covers genuinely fast one-to-one exchanges, while broadcast/framing covers material addressed to a room.

## Posture follows mode: provoke in exploration, produce in execution

In exploratory mode the default is to provoke — bring the lens, withhold the worked conclusion. In execution mode, produce. A premature switch to produce while I am still exploring is treated as a near-failure, because it is the moment my thinking gets done for me.

The same act — producing worked thinking — protects me in execution and erodes me in exploration, so the mode boundary is the load-bearing mechanism. A one-word override ("withhold" / "produce") lets me set posture explicitly when a misread would be costly. This sharpens the existing "default to exploratory when unsure" rule by attaching stakes to it under the protect objective.

## Model-specific tuning is disposable and lives in the skill

The churny anti-AI-tell tactics (the banned-word list, the opening and construction bans), effort guidance, and model choice are model-specific and change with each model generation. They live in a dated, model-stamped block inside the `my-voice` skill, not in the portable constitution. The durable structural tells are the exception, and sit in the operating contract; see "Anti-slop hygiene covers every channel" below.

The constitution files are model-agnostic and change only when my thinking changes; letting model-corrective edits leak into them would let the model-of-the-month reshape my self-definition through the back door of maintenance. Keeping the tuning quarantined in the skill means a model release touches one block and nothing else. The maintenance ritual is light and model-triggered: on a major new model, run two real problems at default settings, see what it flattens or over-produces, rewrite the block, re-stamp.

## Ask for visible rationale, not private thinking

Execution work sometimes needs enough visible structure for Andrew to judge the approach. The contract asks for structure and rationale where useful, rather than asking the model to show its thinking. This preserves the evaluative function without requesting private model reasoning.

## Clarification follows material ambiguity

Task size is a poor proxy for whether a question is needed. A substantial brief can already contain everything required, while a short request can omit the target, source or decision that determines the result. The operating contract and standalone chat adapters therefore ask questions only where ambiguity would materially change the work; otherwise the assistant proceeds and invites redirection.

Cowork retains a separate plan-and-wait boundary for file changes. That is a product-specific delegation preference, not a clarification rule. Its exact-target deletion, folder, connector and persistence boundaries remain stronger than the general execution posture.

## Agent completion claims require session evidence

Agent surfaces must ground completion in tool output from the current session. A successful command alone is not enough where the requested action or exact approved target remains unverified; missing targets and failed checks are reported as outcomes, not rounded up to completion. Plausible substitutes do not inherit authority from named targets. The rule is local to tool-mediated agent work rather than expanding the general conversation contract.

## Long-conversation checkpoints disposition held threads

A holdings checkpoint is useful only if it reduces ambiguity. Each held thread is marked resolved, deliberately parked or awaiting Andrew's input, and the checkpoint distinguishes live work from material that no longer needs attention. Bare topic lists preserve nouns while losing state, which is the failure the checkpoint exists to prevent.

## Anti-slop hygiene covers every channel, not just summoned output

The model-specific anti-tell tactics live in the my-voice skill, which is execution-only. That left a gap. The model's partner-channel prose, its analysis, and the text it writes when editing the kit had no anti-slop steering, because the skill is not loaded then, and AI tells surfaced there unchecked.

The fix keeps the split clean. The durable, structural tells (em-dash density, the "not just X, it's Y" construction, rule-of-three padding, uniform sentence length) sit in `kit/constitution/02-operating-contract.md`'s partner-register hygiene, because they are stable across models and are really just good-writing rules. The churny, model-specific banned-word list stays in the skill's disposable Tuning block. So the operating contract steers every channel against the tells that matter, without copying the disposable list into the durable constitution, and without letting model-of-the-month quirks reshape it.

## Measuring the protection

The kit guards my thinking but cannot show me the guard is working. To get a direct read, `kit/constitution/02-operating-contract.md` adds a practice: periodically, on a real problem, I produce my own reframe before reading the model's, and compare. The gap is the only direct evidence of whether my thinking is staying distinct. Tuning adjusts the model; this checks me.

## Token budget awareness

Constitution files consume tokens in every conversation. The kit is designed with this constraint visible throughout: the bootstrap is kept short, the preferences are approximately 500 words, the overlay is only loaded when relevant. The operating contract is the longest file but earns its length through the depth of its expansion function, mode definitions, and posture rules.

The most critical instructions sit near the beginning of each file, where model attention is strongest. Voice craft and worked examples live in the `my-voice` skill, which loads only at execution, so they do not consume attention on every turn.

## The voice skill is named my-voice

The name `my-voice` makes the user-facing purpose explicit: it is the execution-only instrument for producing Andrew's written output and applying his documentation standard. It retains the standard SKILL.md folder structure.

## The platform layer covers the full AI estate

The maintained platform layer spans Claude Chat, Claude Cowork, Claude Code, ChatGPT, Gemini, Codex, Copilot CLI and Hermes.

The platform model uses two deployment patterns. Configurable chat surfaces receive a standalone condensed operating contract in their native settings: Claude preferences, ChatGPT custom instructions and Instructions for Gemini. Agent and CLI surfaces receive configuration references that carry a minimal derived contract and point them at the constitution files for deeper work.

The condensed prompts must work when no constitution files are attached. They must also defer to the constitution files when those files are loaded. They are deployments, not forks.

## Platform files carry only the voice boundary

Platform files are minimal derived configurations from `kit/constitution/`, not deployment instructions for every related kit component. They must work alone, and they must work alongside the full constitution files, but they should not depend on `my-voice` being loaded or instruct a platform to load it.

The platform layer therefore carries only the durable boundary from `kit/constitution/02-operating-contract.md`: the assistant reasons in its own neutral analytical voice, and Andrew's voice is reserved for output produced on his behalf. The execution craft, register routing and model-specific tuning remain in `kit/implementation/skills/my-voice/`, supplied separately when needed. This keeps the execution-only boundary clean and avoids duplicating skill deployment guidance across product documentation.

## Agent surfaces read the source directly

Agent and CLI tools receive a minimal derived contract, or read the source files directly for deeper work: `kit/constitution/00-bootstrap.md`, `kit/constitution/01-calibration.md`, `kit/constitution/02-operating-contract.md`, and the conditional overlay when relevant.

The root `CLAUDE.md` and `AGENTS.md` stay because they govern work on this repo. They are not deployment artefacts for other tools.

No standing global `AGENTS.md` deployment is maintained. Reconsider that choice only if current product behaviour creates a demonstrated need.

## Agent surfaces do not get converted skills

Codex, Copilot CLI and Hermes do not receive converted copies of `my-voice`. The repo does not define Codex-specific, Copilot-specific or Hermes-specific skill formats.

This keeps the skill source canonical and prevents drift between per-tool adaptations. The platform files also no longer instruct these tools to read the skill; voice material is supplied separately when execution needs it.

## Disposable variations are contribution, not output

Some of what Andrew knows is only reachable by reaction. He may recognise the right framing, structure or opening on sight without being able to specify it upfront. The provoke/produce boundary therefore distinguishes disposable alternatives from developed output.

The operating contract treats disposable variations offered for reaction as contribution, provided they stay plural, sketch-like and unfinished. Developing the direction that lands remains output and waits for an explicit request. The risk runs both ways: withholding useful variations weakens exploration, while treating a reaction as a commission lets the model produce the finished work too early. `provoke-produce-probes.md` includes C4/C5 and a standalone platform variant.

The cascade is scoped by behaviour, not vocabulary. Claude preferences carry the contribution/output wording directly; ChatGPT and Gemini get compact self-contained clauses because their standalone prompts carry the same provoke/produce boundary. Cowork is excluded deliberately because it defaults toward execution and carries no exploratory mechanics to attach this rule to. Provenance: reaction-based elicitation from Thariq's "A Field Guide to Fable: Finding Your Unknowns", translated out of its agentic-coding context.

## External methods enter at the lowest sufficient layer

Useful methods from adjacent domains stay at the mechanism level unless evidence justifies a constitutional rule: reaction-based elicitation, learning what good looks like before judging, blind-spot questions, and a light comprehension check after delegated synthesis.

Coding-specific patterns such as deviation logs, implementation notes, reference-code workflows and quiz-before-merge gates remain outside the kit. The portable files also omit an external unknowns taxonomy; the kit uses useful mechanisms without adopting another author's vocabulary as standing context. The blind-spot pass is constrained to questions rather than answers because a taught map of a domain can become a received frame before Andrew has formed his own read.

Candidate mechanisms live in `kit/implementation/prompts/untested/` without creating a commitment to promote them. `own-the-synthesis.md` remains prompt-only: it gives practical shape to the delegation principle without adding another permanent rule to the operating contract.

## Constitution files are distributed directly

Surfaces that cannot read the repository receive constitution files by direct attachment or paste. The repository does not automatically republish personal constitution content to secondary stores. This keeps one maintained source and avoids hidden deployment paths.

## The operating contract carries the evolution objective and persistence rule

The evolution objective and persistence rule sit in `kit/constitution/02-operating-contract.md` and are covered by active fixtures (ADR-007; see the [evaluation baseline](evidence/2026-07-baseline.md)).

The evolution objective sits directly under the expansion function's opening statement: the function serves a dual objective — help the thinking evolve, and protect the capacity for independent judgement while it does. The constraint clause is load-bearing. Without "never by producing developed positions on my behalf", the evolution objective licenses exactly what the provoke/produce boundary prevents. The posture rules serve both objectives. The `evolution-probes.md` E1/E2 under/over-trigger pair verifies that the model names shifts in Andrew's position without rebuilding the position for him.

The persistence rule anchors approval constitutionally: tools and agent capabilities do not change user-visible persistent artefacts without explicit approval, per item or named batch. Role charters and platform adapters inherit rather than invent that boundary.

The bootstrap states the constitution's place in the layer model and disambiguates its internal authority levels from the architecture's layer numbers.

Condensed and minimal contracts carry the persistence boundary where they must work independently. The constitution governs deliberate tool-mediated changes; ambient memory and history retained automatically by a service are governed through product settings. Fixtures test unspecified-change restraint, explicit-item approval and refusal to claim control over ambient product state.

## The physical layout mirrors the five-layer model

Philosophy, constitution and roles remain shallow and directly addressable because they carry the highest-authority, slowest-changing material. Platforms, skills and prompts sit together beneath `kit/implementation/` because they are product-shaped executions of higher-authority rules. Governance and evals remain cross-cutting rather than becoming false runtime layers, and memory remains outside the repository because state is not system.

Numeric layer folders remain rejected: they would duplicate authority already declared inside the files and make the paths ceremonial. The `kit/` prefix distinguishes the personal instance from the generic framework and governance without changing the shallow structure inside each layer.

## The repository has three content domains

The five layers describe authority inside a personal AI system; they do not describe every kind of material held in the repository. Treating those as the same structure left the personal instance spread across the root and made “implementation” mean both the whole instance and layer 4.

ADR-011 separates the generic framework, personal kit, and governance. Active evals sit with the kit because they verify that instance; concise dated evidence sits in governance. Architecture is documented at two levels rather than placed in a competing folder: the generic model in `framework/layer-model.md`, and the instantiated topology in `governance/current-architecture.md`.
