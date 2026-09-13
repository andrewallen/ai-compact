← [Home](../README.md) · [Governance](README.md) · **Design decisions** · [ADRs](decisions/README.md)

# Design Decisions

Why AI Compact is shaped the way it is. Each decision addresses a specific problem. Understanding the reasoning prevents changes from recreating the same failure.

## Constitution files are model-agnostic

The files in `kit/constitution/` contain no product-specific syntax, no platform assumptions, and no references to features that only exist on one product. Plain markdown with standard structural markup (headers, tables, bold, blockquotes). They are intended to travel across models that accept text instructions; portability of format does not establish equivalent behaviour.

Models and products change frequently. Identity and thinking style change slowly. Coupling the slow-changing content to a fast-changing product format would mean rewriting the most valuable files every time a product updates its architecture. The portable layer stays stable; the product-specific layer absorbs the churn.

## Self-declaring classification in every file

Each constitution file carries an inline prose declaration at the top — bold text stating its classification (e.g. "**Calibration (authority level 1).**"). The bootstrap also declares the full hierarchy in a table. The intended precedence remains explicit regardless of reading order, subject to the host’s instruction hierarchy and permissions.

There is no guaranteed load order when files are uploaded to a project or conversation. The model might read the operating contract before the bootstrap, or calibration before anything else. Without self-declaration, calibration content could be treated as binding rules, or the hierarchy could be missed entirely. Numbered filenames (00, 01, 02, 03) improve the odds of correct ordering but cannot guarantee it. Self-declaration is the belt; numbered filenames are the braces.

## The bootstrap exists as insurance

The bootstrap gives a single view of internal authority and loading boundaries. It distinguishes the architecture’s layers from file authority levels, keeps review material from becoming runtime instructions, and makes clear that file labels do not override the host. Ordinary work does not need a recital of these instructions; an explicit review of the compact can discuss them. Keep this cross-cutting guidance short and tied to a concrete ambiguity.

## Derivations are authored once and distributed deterministically

The constitution defines policy. Two editorially reviewed sources in implementation condense it: [chat-contract.md](../kit/implementation/platforms/chat-contract.md) and [execution-contract.md](../kit/implementation/platforms/execution-contract.md). The [coverage map](../kit/implementation/platforms/contract-maintenance.md#coverage-map) records preserved boundaries, compressed mechanics and deliberate omissions. A derivation is useful standalone without claiming equivalence to the full core.

The distribution script copies marked bodies and source metadata into three chat adapters and four agent guides. Product wrappers remain separately maintained; generated bodies do not. This retains detached outputs while removing independent text ownership. The script detects stale copies, not semantic drift between the constitution and its derivations.

A standing chat body can coexist with full project constitution files when the host supplies both. It declares internal deferral; there is no reason to add an execution body to that combination routinely. Cowork is a distinct addendum requiring a supplied core or chat base. Its stronger safeguards remain local without copying general policy into a third contract.

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

The overlay activates for Microsoft/CDTO work, professional UK government engagement or explicit invocation, as declared in the constitution. Repository-maintenance instructions keep it dormant during kit review unless explicitly invoked for a Microsoft-related task. It contains professional context and Microsoft-specific tone registers that would be inappropriate in other contexts. Calibration references it so the model knows richer context is available without assuming it should be active.

## Controlled project context and ambient product memory are separate

Project instructions, loaded files and knowledge are controlled context. Platform memory and conversation history provide ambient continuity when enabled, but their retention and synthesis are managed by the product and may change independently of the prompt layer. The kit does not depend on them.

The constitution governs deliberate actions taken by an assistant through tools: changing a project file, standing instruction, knowledge-store entry or explicit user-visible memory entry. Ambient product memory is configured and audited through product settings, with temporary or isolated modes used when carry-over is unwanted. The prompt layer does not claim that it can prevent a service from automatically retaining or inferring context.

## Cowork reads mode from the task

Cowork commonly receives defined outcome requests, which are execution under the shared contract. A surface label does not change the fallback: genuinely ambiguous work remains exploratory, and a request for a read or reframe retains the framing invitation. The global instructions preserve Cowork’s separate plan-and-confirm safeguard for file work; confirmation already given for the exact plan need not be repeated.

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

Conductor is treated as a way to run concurrent Claude Code sessions, within the Code deployment route. It has no separate maintained adapter or mode in the current platform map.

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

Prompts and skills are different components of the same implementation layer. Skills encode methodology — structured instructions with frontmatter, supporting files, and deployment to Claude Code's discovery system. Prompts capture useful interaction patterns before they need that structure. The barrier to adding a prompt is near zero: create a file, paste the text, add a sentence of description and link it from its parent index.

The graduation path is explicit. A prompt that starts needing supporting files, step-by-step instructions, or automatic invocation has outgrown the prompts folder and belongs in `kit/implementation/skills/`. This is by design — prompts are the capture point, skills are where patterns mature.

The framework describes the broader system as more than a prompt library: its substance is the operating contract, file hierarchy and calibration. The prompts folder supplies reusable starting points that operate within that context. With the constitution loaded, a prompt inherits its identity, voice boundaries, expansion function and mode detection.

## The kit protects the distinctiveness of my thinking

The kit's purpose is not faster output. It is to keep my thinking mine as models converge on a competent, plausible average. Voice fidelity is secondary, and in one respect a risk (see the partner register below).

This reframes what good help looks like. The danger is not the model writing generically — it is the model doing my thinking for me, competently and plausibly, and me accepting it because it is good enough. Erosion travels through delegated cognition, not delegated prose. `kit/constitution/01-calibration.md` names the moves that make my thinking distinctive ("What I Am Protecting") as personal patterns to protect from identified risks, so they can be provoked rather than performed for me. This extends the decision that specific theses are not part of the kit: the kit captures the pattern of how I think, not the positions I hold.

## The assistant's partner register stays distinct from mine

When reasoning with me, the assistant uses its own neutral analytical voice, not mine. My voice is reproduced only for output produced on my behalf.

A partner that drifts into my register is one I scrutinise less, because it reads like my own reasoning. Fluency and familiarity each lower my guard, and a generic idea wearing my voice stacks both. Keeping the assistant's register visibly different from mine preserves the seam that lets me tell my thinking from the model's. This is why voice is kept off the thinking channel even though the durable principles remain loaded in the portable constitution — the partner-register rule in `kit/constitution/02-operating-contract.md` does the protective work without removing voice from the kit.

## Voice craft lives in a skill; durable principles stay portable

The durable voice principles (economy, unevenness, has-a-point, the no-jargon avoid-list, the layered-narrative structure) stay in `kit/constitution/02-operating-contract.md` and the preferences, because the kit's value is model-agnostic portability — they must travel to any model. The fuller craft (operational register mechanics, the register matrix, tone-by-context, output formats, worked examples) remain in the `my-voice` skill. Model and host settings live in the separate dated implementation guidance.

The split follows the kit's own pattern of principles held at two levels of depth, with the execution craft summoned only when producing output. Model invocation is enabled so natural-language execution requests can summon the skill consistently with the operating contract. The skill's description excludes exploration and thinking, and its substance gate stops it from voicing positions Andrew has neither supplied nor adopted; those are the behavioural controls on premature use. The alternative, moving voice wholesale into the skill, was rejected: the durable voice principles must remain available on surfaces that do not load the skill.

## The voice skill separates persuading from documenting

The my-voice skill carries four registers, not one. Operational, broadcast/framing and authored are my personal voice — fast transactional comms, posts that frame and bring a room along, and longer point-led pieces where I am persuading or framing. Documentation is the fourth register for substantive write-ups (workshop outputs, reports, knowledge artefacts) whose job is to convey understanding, not to land a thesis.

The distinction matters when one request contains both communication and documentation. A covering message may need a personal register while the attached substantive write-up needs a neutral professional voice shaped by my quality bar and narrative method. The routing rule sends each artefact to the register that matches its purpose. Authorised factual documentation can organise verified material without a prewritten personal thesis; it labels new implications and recommendations separately from Andrew’s recorded decisions.

Medium does not decide register; audience breadth and intent do. A group post may be a framing piece that needs a reflective, considered voice rather than the clipped style of a fast transactional message. The operational register therefore covers genuinely fast one-to-one exchanges, while broadcast/framing covers material addressed to a room.

## Posture follows mode: provoke in exploration, produce in execution

In exploratory mode the default is to provoke — bring the lens, withhold the worked conclusion. In execution mode, produce. A premature switch to produce while I am still exploring is treated as a near-failure, because it is the moment my thinking gets done for me.

The same act — producing worked thinking — protects me in execution and erodes me in exploration, so the mode boundary is the load-bearing mechanism. A one-word override ("withhold" / "produce") lets me set posture explicitly when a misread would be costly. This sharpens the existing "default to exploratory when unsure" rule by attaching stakes to it under the protect objective.

## Model guidance is separate from policy and voice craft

Model observations, effort advice and host instruction-composition rules live in [model guidance](../kit/implementation/platforms/model-guidance.md). The skill retains output craft, including personal preferences that need no universal claim about model behaviour. Its former July model-choice and effort routing is historical, recoverable through Git.

The September review retains one constitution for Fable 5.1 and GPT-6 Astra, with a [shared execution derivation](../kit/implementation/platforms/execution-contract.md) available for defined work on any model, including Grok and models accessed through OpenCode Go. Differences in brevity, progress reporting, reasoning controls or host composition do not by themselves justify different independence or approval policies. Vendor documentation informs proposed steering; it is not evidence of local success.

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

The partner register is self-contained in the operating contract. It covers readable sentences, proportionate structure and avoidance of stock constructions without loading the execution-only voice skill. Detailed output craft stays with the skill. These are owner-selected writing standards; treating them as universal defects of every current model would confuse a preference with an empirical claim.

## Measuring the protection

An optional personal review practice is to frame a real problem independently before reading the assistant’s reframe, then compare. The current contract’s one-sentence invitation preserves the opportunity to form that view; it does not make every defined analysis wait for an exercise. This practice is complementary to behavioural probes, not proof by itself that independence is protected.

## Token budget awareness

Standing instructions consume context whenever supplied. Keep the bootstrap focused, load the professional overlay only when relevant, and supply detailed voice craft at execution. Condense by preserving substantive protections, not by word count alone. Field lengths belong with the applicable adapter and should be remeasured after edits; historical UI limits require rechecking at deployment. No universal attention-position or token-saving claim is needed to justify this separation.

## The voice skill is named my-voice

The name `my-voice` makes the user-facing purpose explicit: it is the execution-only instrument for producing Andrew's written output and applying his documentation standard. It retains the standard SKILL.md folder structure.

## The platform layer covers the full AI estate

The maintained platform layer spans Claude Chat, Claude Cowork, Claude Code, ChatGPT, Gemini, Codex, Copilot CLI, Hermes, Grok and OpenCode/Go.

The platform model uses two deployment patterns. Configurable chat surfaces receive a standalone condensed operating contract in their native settings: Claude preferences, ChatGPT custom instructions and Instructions for Gemini. Agent and CLI surfaces receive configuration references that carry a minimal derived contract and point them at the constitution files for deeper work.

The condensed prompts must work when no constitution files are attached. They must also defer to the constitution files when those files are loaded. They are deployments, not forks.

## Platform derivations carry boundaries and compact standards

Platform files are minimal derived configurations from `kit/constitution/`, not deployment instructions for every related kit component. They must work alone, and they must work alongside the full constitution files, but they should not depend on `my-voice` being loaded or instruct a platform to load it.

Shared platform derivations carry voice separation, ownership, a compact writing standard and durable vocabulary constraints from `kit/constitution/02-operating-contract.md`. Execution craft and register routing remain in `kit/implementation/skills/my-voice/`, supplied separately when needed; model guidance is a maintenance reference under platforms. This keeps the execution-only boundary clean and avoids duplicating skill deployment guidance across product documentation.

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

The cascade is scoped by behaviour, not vocabulary. Claude preferences carry the contribution/output wording directly; ChatGPT and Gemini get compact self-contained clauses because their standalone prompts carry the same provoke/produce boundary. Cowork receives exploratory mechanics through its required base contract; its addendum carries only additional action and output rules. Provenance: reaction-based elicitation from Thariq's "A Field Guide to Fable: Finding Your Unknowns", translated out of its agentic-coding context.

## External methods enter at the lowest sufficient layer

Useful methods from adjacent domains stay at the mechanism level unless evidence justifies a constitutional rule: reaction-based elicitation, learning what good looks like before judging, blind-spot questions, and a light comprehension check after delegated synthesis.

Coding-specific patterns such as deviation logs, implementation notes, reference-code workflows and quiz-before-merge gates remain outside the kit. The portable files also omit an external unknowns taxonomy; the kit uses useful mechanisms without adopting another author's vocabulary as standing context. The blind-spot pass is constrained to questions rather than answers because a taught map of a domain can become a received frame before Andrew has formed his own read.

Candidate mechanisms live in `kit/implementation/prompts/untested/` without creating a commitment to promote them. `own-the-synthesis.md` remains prompt-only: it gives practical shape to the delegation principle without adding another permanent rule to the operating contract.

## Constitution files are distributed directly

Surfaces that cannot read the repository receive constitution files by direct attachment or paste. The repository does not automatically republish personal constitution content to secondary stores. This keeps one maintained source and avoids hidden deployment paths.

## The operating contract carries the evolution objective and persistence rule

The evolution objective and persistence rule sit in `kit/constitution/02-operating-contract.md` and are covered by active fixtures (ADR-007; see the [evaluation baseline](evidence/2026-07-baseline.md)).

The evolution objective opens the operating contract: extend reach while protecting independent judgement. Exploration offers applied lenses and unfinished sketches; execution completes the requested deliverable. Neither permits attribution of an assistant-developed position to Andrew. The historical `evolution-probes.md` E1/E2 pair checks shift surfacing without rebuilding the owner’s position; its prior results do not certify this rewrite.

The persistence rule anchors approval constitutionally: tools and agent capabilities require explicit scoped approval to change persistent artefacts on Andrew’s behalf, including hidden supporting records. A specified change request or “implement the plan” authorises its defined batch, without settling open choices or waiving narrower safeguards. Role charters and platform adapters inherit rather than invent that boundary.

The bootstrap states the constitution's place in the layer model and disambiguates its internal authority levels from the architecture's layer numbers.

Condensed and minimal contracts carry the persistence boundary where they must work independently. The constitution governs deliberate tool-mediated changes; ambient memory and history retained automatically by a service are governed through product settings. Fixtures test unspecified-change restraint, explicit-item approval and refusal to claim control over ambient product state.

## The physical layout mirrors the five-layer model

Philosophy, constitution and roles remain shallow and directly addressable because they carry the highest-authority, slowest-changing material. Platforms, skills and prompts sit together beneath `kit/implementation/` because they are product-shaped executions of higher-authority rules. Governance and evals remain cross-cutting rather than becoming false runtime layers, and memory remains outside the repository because state is not system.

Numeric layer folders remain rejected: they would duplicate authority already declared inside the files and make the paths ceremonial. The `kit/` prefix distinguishes the personal instance from the generic framework and governance without changing the shallow structure inside each layer.

## The repository has three content domains

The five layers describe authority inside a personal AI system; they do not describe every kind of material held in the repository. Treating those as the same structure left the personal instance spread across the root and made “implementation” mean both the whole instance and layer 4.

ADR-011 separates the generic framework, personal kit, and governance. Active evals sit with the kit because they verify that instance; concise dated evidence sits in governance. Architecture is documented at two levels rather than placed in a competing folder: the generic model in `framework/layer-model.md`, and the instantiated topology in `governance/current-architecture.md`.

## Package records separate capability selection from client delivery

The approved first-party implementation plan's Batch 1 introduces a [package register](../kit/implementation/skills/package-register.md) beside the existing capability research. It records native baselines and candidate vendor packages without claiming adoption, installation or behavioural quality. A package may contain skills, tools, hooks, agents and other execution components. Source availability, publisher attribution and actual runtime state are separate evidence.

The capability matrix owns acceptance and provider summaries; the package register owns implementation/revision identities and dispositions; source references own provenance; platform guidance owns delivery; deployment evidence owns observed settings and execution. Linking these owners avoids parallel complete catalogues. One primary workflow can coordinate complementary craft and format stages, with constitutional boundaries and host controls preserved.

This is a file-level implementation decision. Existing folders and authority remain intact; no personal marketplace, distribution bundle or runtime router is introduced. Trial fixtures are authored but unexecuted. Model efficiency means accepted-task quality, corrections and observed usage, not installed skill count. Cross-lab imports require a demonstrated gap; model upgrades trigger targeted reassessment of procedural scaffolding. The generic lesson is included in the framework without personal selections.
