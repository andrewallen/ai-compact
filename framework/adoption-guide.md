← [Home](../README.md) · [Framework](README.md) · [Layer model](layer-model.md) · **Adoption guide**

# Adoption Guide

How to build your own implementation of the layer model. Start with the minimum viable version below; grow it only as use proves the return. The risk is not starting too small. It is starting too large and collapsing under the maintenance burden before the compounding loop has time to pay.

## Minimum viable implementation

Four files and a critique pass. This is enough to activate the pattern without the structural overhead. (The files are listed in build order, which is not the layer order — the philosophy is layer 1 but written last.)

**One identity file.** Who you are, how you think, what standards your work is held to. This is calibration, not biography — its job is to set the level at which the AI reasons with you. Built through the interview principle (below), not self-authored.

**One operating contract.** The binding rules: how challenge works, how the AI should read what mode you are in (exploring, executing, refining), what its register must be, what to avoid. This is the contract every conversation runs under, and it will become the most tuned file you own.

**One bootstrap.** Five to twenty lines that declare the hierarchy: which file binds, which calibrates, which activates conditionally, and what the model must not do (summarise the files back, reference the hierarchy in conversation). It costs almost nothing to write at the start and prevents the authority-inference failure that becomes hard to diagnose once the kit grows.

**One philosophy stub.** Even three axioms answering one question — why is AI in your system at all? — will discipline every later decision. Expect this file to be the last one finished and the first one consulted when something is ambiguous.

**A critique pass.** Give the drafts to a second model, or the same model in a fresh context, with one instruction: find what is weak, missing, or internally inconsistent. Do this before first use, and repeat it for every later change to any of the four files.

Everything else — role charters, platform adapters, skills, prompts, evals — is added when use demands it, not before.

## The interview principle

Do not write about yourself; have the AI interview you. Self-authoring produces the public narrative — the polished role description. Interview produces the thinking underneath it: *what do you actually believe? What patterns have you observed that others miss? What have you learned that contradicts the conventional view?*

The discovery that makes this the load-bearing practice: articulation changes the thinking itself. You do not know what you think until you try to state it precisely. Ideas that felt clear become visibly incomplete; assumptions that felt settled reveal themselves as untested. Building the kit is itself the first return on the kit.

The same rule applies with more force to the philosophy layer. An assistant can interview, provoke, and challenge, but axioms a model drafted are scaffolding until you have rewritten each one in your own hand or struck it. Delegating that rewrite defeats the file's purpose.

## The two-model workflow

The model that helped build something is not positioned to challenge it, for the same reason a writer needs an editor. Separate the generative function from the evaluative one: build in conversation, then critique cold — a fresh context, no drafting history, hunting for contradictions and exploitable ambiguity.

Expect the cold reader to find a specific species of defect the author cannot: rules that sound protective while resting on nothing, and instructions that read correctly while permitting exactly the failure they exist to prevent. Treat the workflow as mandatory for any change above the implementation layer — philosophy, constitution (bootstrap included), or a role charter — and cheap insurance everywhere else.

## Growing the system

**Add a role charter** when a genuinely distinct job emerges — one with its own decision policy, not just its own topic. One page: mission, decision policy, boundaries, cadence. Subordinate to the constitution always. If a charter starts accumulating workflow steps and supporting files, it is drifting toward being a capability; keep the judgement in the charter and move the mechanics to a skill.

**Add platform adapters** when you work across products. Each is a condensed derivation of the operating contract that works standalone and defers when the full files are loaded. Watch character limits: a condensed prompt near its platform's cap means every future amendment is a displacement decision.

**Add evals** once the contract is tuned enough to be worth protecting. A handful of fixtures probing the failure modes you care most about — sycophancy, premature agreement, the AI producing conclusions you should have produced — each run several times before and after any contract change. Judge results across runs, not on a single sample; the behaviours being probed are probabilistic. Until the probes exist, the critique pass is the only gate on contract changes — that exposure is acceptable early, but it is exposure, so add probes as soon as the contract stabilises.

**Add an output-voice capability** when the AI starts producing work in your name. It holds your voice — registers, structures, banned vocabulary, worked examples — and is invoked only at execution. Keeping it a separate capability rather than a standing instruction is what makes the register seam enforceable.

**Keep memory out.** The knowledge store — whatever tool holds your notes and developing positions — is state, not system. The kit governs deliberate action at the boundary: what is worth keeping, what may be written back, and how anything written is labelled with its origin (yours, the model's, a source's). The store's internal structure belongs to the store. Until you add a memory-facing role charter, the contract should require explicit approval for any tool-mediated change to a persistent artefact. Ambient memory and history managed automatically by a product belong to that product's settings and retention controls; a prompt should not claim authority over them.

## Failure modes

Named in advance because each is quiet while it happens.

**Authority-inference failure.** The model reads everything, behaves competently, and follows the binding rules only sometimes. Cause: files that do not declare their weight. Fix: the bootstrap, plus self-declared classifications in every file.

**AI-flavoured self-confirmation.** The system produces increasingly polished versions of positions that were never seriously tested. The symptom is confident conclusions with no record of the challenge they survived. The contract's challenge rules are the defence, but they decay without evals and the cold-critique habit.

**Register bleed.** The AI drifts into your voice during thinking dialogue. It feels like rapport; it is erosion — you scrutinise a partner less when it sounds like you. Keep the seam explicit in the contract, and reserve your voice for output produced on your behalf.

**Delegated cognition.** The AI hands you a finished reframe and you accept it instead of producing your own. This is the failure the whole pattern exists to prevent, and it arrives disguised as excellent service. The defence is postural: in exploration the AI provokes and withholds conclusions; production waits for an explicit request.

**Over-structuring.** More time filing than thinking. The fix is aggressive simplification, and noticing is the hard part: a well-maintained kit that produces no new insight has already failed.

**Context drift.** The files still say who you were a year ago. The AI's behaviour feels subtly off while remaining technically aligned with what is written. Fix: a deliberate refresh cadence — monthly reread of identity and contract, quarterly simplification pass.

**Model dependence.** The kit works on the model it was tuned on and degrades elsewhere. Mitigation: model-agnostic markdown, explicit instruction rather than reliance on one model's implicit tendencies, model-specific tuning quarantined in disposable blocks, periodic testing on a second model.

**Reasoning-exposure coupling.** An instruction asks the model to "show its thinking" when the real need is a reviewable decision. Some reasoning models may treat that as a request for private reasoning and refuse or distort the response. Ask for visible structure, rationale, evidence and trade-offs instead; those are the artefacts the user can evaluate. Treat the reword as behavioural and regression-test it, because removing the phrase must not remove useful explanation.

## Evaluating whether it works

Qualitative questions, honestly answered, beat metrics here.

- **Restart cost.** Does the first substantive contribution in a new session show the context has been absorbed, or does the conversation begin as if nothing was ever established?
- **Challenge record.** Does your written thinking include positions that were tested and revised — or abandoned? A history showing only additive polish means the challenge function is not operating.
- **Explicitness.** Can you state your own core positions more precisely after six months of use than before?
- **Cross-model consistency.** Loaded into a different model, do the binding rules still hold? Variation in depth and style is expected; variation in whether the rules are followed at all means the authority hierarchy is not explicit enough.
- **Maintenance load.** Still a small fraction of thinking time? If maintenance grows faster than insight, cut structure.
