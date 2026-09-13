← [Home](../README.md) · [Governance](README.md) · **Design decisions** · [ADRs](decisions/README.md)

# Design Decisions

Why AI Compact is shaped the way it is. Each decision addresses a specific problem. Understanding the reasoning prevents changes from recreating the same failure.

## Constitution files are model-agnostic

Identity and thinking style change slowly; products change frequently. The constitution uses plain Markdown and keeps product syntax and configuration assumptions in implementation, so product changes do not force rewrites of the portable core. Portability of format does not establish equivalent behaviour.

## Self-declaring classification in every file

Uploaded files have no guaranteed reading order. Each constitution file therefore declares its classification inline, while the bootstrap provides the complete hierarchy. Numbered filenames aid navigation but cannot substitute for that declaration. Intended precedence remains explicit within the host's instruction hierarchy and permissions.

## The bootstrap exists as insurance

The bootstrap gives a single view of internal authority and loading boundaries. It distinguishes the architecture’s layers from file authority levels, keeps review material from becoming runtime instructions, and makes clear that file labels do not override the host. Ordinary work does not need a recital of these instructions; an explicit review of the compact can discuss them. Keep this cross-cutting guidance short and tied to a concrete ambiguity.

## Derivations are authored once and distributed deterministically

Independent condensed copies drift. Two reviewed implementation sources therefore own the shared wording; detached adapters receive their marked bodies and source metadata through a distribution script. Product wrappers remain independently maintained. The script verifies copying, while constitution-to-derivation review remains semantic work.

[Contract maintenance](../kit/implementation/platforms/contract-maintenance.md) owns the coverage map and loading combinations. Cowork retains a base-dependent addendum so its extra safeguards do not become a third copy of general policy. A derivation is useful standalone without claiming equivalence to the full core.

## File hierarchy: calibration, binding rules, overlay

Calibration shapes interpretation; binding rules control behaviour; the conditional overlay adds specific context. Binding rules win if calibration suggests otherwise, and the overlay supplements rather than replaces them. The [bootstrap](../kit/constitution/00-bootstrap.md) owns the exact classification and precedence table. This is a safeguard for conflicting instructions, not an additional architecture layer.

## Specific theses are not part of the kit

A particular thesis is content, not identity: loading it universally would prime unrelated analysis. Calibration describes how Andrew builds and tests positions, while an individual position is supplied when relevant. The kit protects the pattern of thinking without carrying its current conclusions.

## Obsidian Vault is not referenced in the portable files

The vault holds personal knowledge and active thinking, but many receiving surfaces cannot access it. Referring to absent notes as operating context would create unusable instructions and invite invented connections. Portable files therefore rely on supplied context and explicitly optional material; the external knowledge store is described in governance.

## One file is conditional; three always travel together

Of the four constitution files, the professional overlay may be absent. Bootstrap, calibration, and the operating contract are expected to travel together as the minimum operating set.

The overlay activates for Microsoft/CDTO work, professional UK government engagement or explicit invocation, as declared in the constitution. Repository-maintenance instructions keep it dormant during kit review unless explicitly invoked for a Microsoft-related task. It contains professional context and Microsoft-specific tone registers that would be inappropriate in other contexts. Calibration references it so the model knows richer context is available without assuming it should be active.

## Controlled project context and ambient product memory are separate

Supplied files and project instructions are controlled context; ambient continuity is product-managed and can change independently. The constitution governs deliberate tool-mediated changes to persistent artefacts. Product settings govern automatic retention and inference, including available isolation controls. Keeping these responsibilities separate avoids claiming a prompt can control service behaviour.

## Cowork reads mode from the task

Cowork commonly receives defined outcome requests, which are execution under the shared contract. A surface label does not change the fallback: genuinely ambiguous work remains exploratory, and a request for a read or reframe retains the framing invitation. The global instructions preserve Cowork’s separate plan-and-confirm safeguard for file work; confirmation already given for the exact plan need not be repeated.

## Cowork file safety is an explicit delegation choice

Cowork's deletion, overwrite and connector restrictions are deliberate delegation preferences. Ambiguous requests such as “clean up” do not identify files to delete, and a request to draft a message does not approve sending it. Exact approval boundaries prevent broad task wording from expanding into unintended changes. These safeguards remain in the Cowork addendum; this decision does not depend on a claim about current platform defaults.

## Folder instructions require approval to modify

Folder and project instructions persist into future work. Allowing an assistant to rewrite them merely because it has access would let accumulated context alter the authored contract. The Cowork addendum therefore keeps instruction changes under explicit user approval, regardless of what editing capabilities the product exposes.

## The repo structure separates portable from product-specific

Product folders absorb configuration changes while the constitution remains canonical. A new product gets an adapter, not a fork of the core. Current paths and loading responsibilities belong in the [deployment map](../kit/implementation/platforms/deployment-map.md).

## Conductor is not a separate mode

Conductor is treated as concurrency within the Claude Code route. Running several sessions changes coordination, not the operating contract, so it does not justify another adapter, template or authority layer.

## Knowledge-system methodology stays outside the kit

The kit governs the assistant's thinking and actions at the knowledge-store boundary. The store's organisation and maintenance methodology belong to the store. Absorbing them here would couple the portable system to an external implementation many surfaces cannot access.

## Skills are version-controlled in the kit

Personal skills encode methodology worth maintaining alongside the contract they extend. They use the portable `SKILL.md` folder structure and remain subordinate to the operating contract. Client discovery, invocation and permissions still need verification; a portable instruction file does not reproduce an entire plugin.

The [skills tracker](../kit/implementation/skills/README.md) links maintained personal source and external packages. Connectors provide access, while plugins may bundle methodology with tools, hooks and other runtime components. Distribution form alone does not determine architectural responsibility.

## Prompts are deliberately lighter than skills

Prompts capture useful interaction patterns before they need package structure. Each is a Markdown file explaining purpose, use and the text to supply, linked from its parent index. The `untested/` folder distinguishes candidates from patterns supported by live use.

Supporting files, procedural complexity or automatic invocation can justify graduation into a skill. Until then, frontmatter and another delivery mechanism add little. Prompts remain entry points within the constitution rather than independent sources of standing policy.

## The kit protects the distinctiveness of my thinking

The kit's purpose is not faster output. It is to keep my thinking mine as models converge on a competent, plausible average. Voice fidelity is secondary, and in one respect a risk (see the partner register below).

This reframes what good help looks like. The danger is not the model writing generically — it is the model doing my thinking for me, competently and plausibly, and me accepting it because it is good enough. Erosion travels through delegated cognition, not delegated prose. `kit/constitution/01-calibration.md` names the moves that make my thinking distinctive ("What I Am Protecting") as personal patterns to protect from identified risks, so they can be provoked rather than performed for me. This extends the decision that specific theses are not part of the kit: the kit captures the pattern of how I think, not the positions I hold.

## The assistant's partner register stays distinct from mine

When reasoning with me, the assistant uses its own neutral analytical voice, not mine. My voice is reproduced only for output produced on my behalf.

A partner that drifts into my register is one I scrutinise less, because it reads like my own reasoning. Fluency and familiarity each lower my guard, and a generic idea wearing my voice stacks both. Keeping the assistant's register visibly different from mine preserves the seam that lets me tell my thinking from the model's. This is why voice is kept off the thinking channel even though the durable principles remain loaded in the portable constitution — the partner-register rule in `kit/constitution/02-operating-contract.md` does the protective work without removing voice from the kit.

## Voice craft lives in a skill; durable principles stay portable

The constitution owns voice separation, durable writing principles and purpose-sensitive structure. The skill adds register routing, craft and examples; model and host settings stay in implementation guidance. Keeping durable principles portable supports surfaces that cannot load the skill, while detailed craft need only travel when execution requires it.

Model invocation is enabled so natural-language output requests can summon the skill. Its description excludes exploration, and its substance gate prevents it voicing positions Andrew has neither supplied nor adopted. Moving voice wholesale into the skill was rejected because those durable boundaries must remain available without it.

## The voice skill separates persuading from documenting

Operational, broadcast/framing and authored output use Andrew's personal voice. Documentation uses a neutral professional register to convey understanding. Purpose and audience select the register, so a covering message and its attached report can legitimately use different ones; a group post does not automatically call for clipped operational prose.

Factual documentation may organise verified material without a prewritten personal thesis. New implications and recommendations remain distinguishable from Andrew's recorded decisions. This allows useful synthesis without concealing a new position inside familiar voice.

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

## Tool-mediated completion claims require session evidence

The [operating contract](../kit/constitution/02-operating-contract.md#memory-and-evidence) requires current-session evidence for progress and completion claims whenever tools are used, on any surface. A successful command alone is not enough where the requested action or exact approved target remains unverified; missing targets and failed checks are reported as outcomes, not rounded up to completion. Plausible substitutes do not inherit authority from named targets. Agent adapters derive this shared rule; its application depends on tool use rather than a product's chat or agent label.

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

The kit supports both configurable chat and agent surfaces. Standing settings supply a condensed contract where available; direct source reads provide deeper context. The [deployment map](../kit/implementation/platforms/deployment-map.md) owns the current product inventory, so adding a surface does not require repeating that inventory in design rationale. Each route deploys the same policy rather than forking it.

## Platform derivations carry boundaries and compact standards

Shared bodies carry enough policy and writing guidance to work without the execution-only voice skill. Register craft is supplied separately. This keeps ordinary reasoning self-contained while avoiding a second owner for detailed output methodology. [Contract maintenance](../kit/implementation/platforms/contract-maintenance.md#loading-combinations) distinguishes standalone bodies, base-dependent addenda and maintenance references.

## Agent surfaces read the source directly

Agents use a minimal derived contract or read the core files for deeper work. The root `CLAUDE.md` and `AGENTS.md` govern this repository; they are not general deployment artefacts. No standing global `AGENTS.md` deployment is maintained. Reconsider that choice if current product behaviour demonstrates a need, rather than creating another maintained copy speculatively.

## Agent surfaces do not get converted skills

Per-client conversions would create multiple owners for the same craft and invite drift. Personal skills retain one portable source, with client-specific delivery described in platform guides. Voice material is supplied separately when execution needs it.

## Disposable variations are contribution, not output

Reaction can reveal a preference Andrew could not specify upfront. Plural, unfinished sketches therefore belong in exploration, while developing a selected direction requires an explicit request. Withholding useful alternatives weakens exploration; treating a reaction as a commission prematurely takes over the work.

The shared chat body carries this boundary; Cowork receives it through its required base. The execution derivation compresses exploratory mechanics, as recorded in the coverage map. [C4/C5 and the reusable prompt variant](../kit/evals/provoke-produce-probes.md) distinguish selecting a sketch from requesting its development. Provenance: reaction-based elicitation from Thariq's “A Field Guide to Fable: Finding Your Unknowns”, adapted from its agentic-coding context.

## External methods enter at the lowest sufficient layer

Useful methods from adjacent domains stay at the mechanism level unless evidence justifies a constitutional rule: reaction-based elicitation, learning what good looks like before judging, blind-spot questions, and a light comprehension check after delegated synthesis.

Coding-specific patterns such as deviation logs, implementation notes, reference-code workflows and quiz-before-merge gates remain outside the kit. The portable files also omit an external unknowns taxonomy; the kit uses useful mechanisms without adopting another author's vocabulary as standing context. The blind-spot pass is constrained to questions rather than answers because a taught map of a domain can become a received frame before Andrew has formed his own read.

Candidate mechanisms live in `kit/implementation/prompts/untested/` without creating a commitment to promote them. `own-the-synthesis.md` remains prompt-only: it gives practical shape to the delegation principle without adding another permanent rule to the operating contract.

## Constitution files are distributed directly

Surfaces that cannot read the repository receive constitution files by direct attachment or paste. The repository does not automatically republish personal constitution content to secondary stores. This keeps one maintained source and avoids hidden deployment paths.

## The operating contract carries the evolution objective and persistence rule

Extending reach while protecting independent judgement is a standing objective, so it belongs in the operating contract rather than a role or platform adapter. The same applies to approval for deliberate persistent changes, including hidden supporting records. ADR-007 records that placement; the [July baseline](evidence/2026-07-baseline.md) contains historical results, not certification of later rewrites.

A specified change request or “implement the plan” authorises its defined batch without settling open choices or waiving narrower safeguards. Role charters and adapters inherit that boundary. Ambient service memory remains a product-settings concern, so fixtures distinguish deliberate writes from automatic retention.

## The physical layout mirrors the five-layer model

Higher-authority material stays shallow and directly addressable. Product-shaped platforms, skills and prompts share the implementation layer; governance and evals remain cross-cutting; memory stays outside because it is changing state.

Numeric layer folders were rejected because they duplicate declared authority and make paths ceremonial. The `kit/` prefix distinguishes the personal instance without adding depth inside each layer.

## The repository has three content domains

The five runtime layers do not describe all repository content. Mixing the two structures scattered the personal instance and made “implementation” mean both the whole kit and layer 4. ADR-011 separates generic framework, personal kit and governance. Evals stay with the instance they test; dated evidence stays in governance. The framework specifies the generic architecture, while governance describes this instance.

## Package records separate capability selection from client delivery

**Historical decision, superseded by [Provider selections drive harness configuration](#provider-selections-drive-harness-configuration).** The initial preparation separated capability criteria, package identities and source provenance into linked research registers. It established source and packaging distinctions, but no comparative quality results. Git history preserves those registers and the unexecuted pilot plan.

## Provider selections drive harness configuration

**Historical decision, superseded by [Skills track the working set](#skills-track-the-working-set).** The next simplification placed provider selections and On/Off targets in a single catalogue, with platform baselines for delivery. It retained the research documents with historical notices. The provider preference remains: use each lab's useful native and published capabilities in its own harness, with independent skills eligible across platforms. This is a configuration choice, not a measured quality ranking.

## Skills track the working set

Andrew clarified that the skills area exists to track the skills he uses. One [tracker](../kit/implementation/skills/README.md) now records purpose, source and concise deployment notes, distinguishing adoption, availability and successful use. Unselected offerings, research registers, the implementation plan, generic authoring guidance and an unused template were removed; Git retains that history. The four-file my-voice package remains maintained source.

Platform baselines own current setup and gaps, with detailed observations in dated evidence. Source changes can make a recorded deployment stale, so alignment belongs in those baselines rather than being repeated here. Cowork's extra confirmations and the documentation register's review requirements remain explicit behavioural choices; simplifying their surrounding documentation does not approve changing them.
