← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · [Platforms](README.md) · **Contract maintenance**

# Contract Maintenance

The constitution is the policy source. Two reviewed derivations are authored here: [chat-contract.md](chat-contract.md) for conversational use and [execution-contract.md](execution-contract.md) for defined tasks. The [distribution script](sync_contracts.py) copies their marked bodies into product files; it does not interpret the constitution or establish semantic equivalence.

## Distribution

| Authored source | Generated body destinations |
|---|---|
| Chat contract | [Claude preferences](claude/personal-preferences.md), [ChatGPT instructions](chatgpt/custom-instructions.md), [Gemini instructions](gemini/saved-instructions.md). |
| Execution contract | [Codex](codex/README.md), [Claude Code](claude/code/README.md), [Copilot CLI](copilot-cli/README.md), [Hermes](hermes/README.md). |

Product wrappers remain manually maintained. Only the body and generated source-version/length metadata are replaced. Existing detached files remain available for copying; duplication in distributed artefacts is intentional, but their text is authored once. Grok and OpenCode reference the execution source directly.

From the repository root, using Python 3.9 or newer:

```sh
python3 kit/implementation/platforms/sync_contracts.py --check
python3 kit/implementation/platforms/sync_contracts.py --write
```

`--check` is read-only: exit 0 means all seven copies match, 1 means drift, 2 means malformed or unavailable input. `--write` validates all sources, targets and markers before writing and reports changed targets. It preserves text outside the two managed regions. An I/O failure during writing can leave earlier reported updates in place; rerun after resolving the failure. Neither mode installs instructions or edits the constitution.

Edit the appropriate source body and increment its source version before regeneration. Generated metadata carries that version; the product file's own version tracks wrapper changes. Review constitutional amendments against the coverage map before updating either derivation. The chat source must fit the repository's 5,000-character budget; verify actual product limits at deployment. A copy check establishes textual identity only, not behavioural adherence or completeness of the editorial derivation.

## Loading combinations

| Use | Supply |
|---|---|
| Ad hoc chat | Generated chat body, or the identical source body. |
| Sustained thinking | Core constitution; a pre-existing standing chat body may coexist and defers within the host hierarchy. No need to add another execution body. |
| Defined agent task | Execution body plus task handover, or the full core when deeper context is needed. Do not routinely stack both derivations. |
| Cowork | Core constitution **or** chat body, plus the [Cowork addendum](claude/cowork/global-instructions.md). Verify the base is actually supplied; profile-preference inheritance is not assumed. |
| Personal output | The selected base plus the four-file `my-voice` package when available and relevant. Its shared audience/form guidance works with either condensed body; full-core references identify provenance and are not unavailable-file prerequisites. Its craft does not style thinking dialogue. |
| Model adjustment | Only the applicable steering from [model guidance](model-guidance.md), through the actual host's supported mechanism. Do not load the whole maintenance reference. |

The full constitution governs when available within the supplied instruction set; host instructions and permissions still apply. Cowork and task-specific safeguards supplement that base. Project templates record local context, decisions and authority, rather than replicating shared policy.

## Coverage map

“Preserved” means the operative boundary is explicit in the derivation. “Compressed” means its intent is expressed more briefly, with examples or finer mechanics omitted. “Omitted” means the information must come from full context when needed. These are editorial dispositions, not parity claims.

| Constitutional source | Chat derivation | Execution derivation | Deliberate limit / additional context |
|---|---|---|---|
| Bootstrap: precedence and loading boundaries | Preserved | Preserved | Authority-level table and maintenance-only philosophy explanation omitted; host boundaries remain explicit. |
| Calibration: identity and thinking context | Compressed: role and systems thinking | Omitted: name only | Career, years of experience, personal thinking moves and professional background require calibration when useful; task handover supplies relevant context. Both bodies carry the binding method-fit rule without requiring the personal examples. |
| Opening purpose and attribution | Preserved | Compressed: expansion, ownership and attribution | Full statement of personal purpose remains in the constitution. |
| Partner register and agreement discipline | Compressed | Compressed | Neutral voice, no praise/validation, direct prose and single pushback explicit. Full examples, phrase lists and mirroring diagnostic omitted. |
| Expansion and challenge | Compressed | Compressed | Consequential lenses, active scrutiny, method fit, concrete alternatives, material pause and no manufactured objections retained; useful familiar methods remain valid. Detailed trigger catalogue and candidate-generation mechanics shortened. |
| Mode, invitation and posture | Preserved | Compressed | Both protect exploratory framing and explicit posture. Chat retains unfinished-sketch mechanics; execution provides a fallback for exploration, with full context preferred for sustained thinking. |
| Execution and refinement | Preserved | Compressed | Completion, material clarification, stance/ownership preservation and semantic-change signalling retained. Chat explicitly describes corrections steering an ongoing task; execution relies on its defined task and handover. |
| Scope and approval | Preserved | Preserved | Specified requests supply scoped approval; hidden records, open choices, narrower safeguards and separate sending/commit/deployment authority remain explicit. |
| Memory and tool evidence | Preserved | Preserved | Ambient settings distinguished from deliberate writes; current-session evidence and exact targets retained. |
| Long conversations | Compressed | Compressed | Objective/decisions, rationale, scope, attribution and approval limits retained. Detailed thread disposition and compaction mechanics require full core/host support; execution has handover fields. |
| My Voice | Compressed | Compressed | Owned positions versus neutral factual documentation, British English, facts/caveats and durable vocabulary bans retained. The voice package supplies audience/form guidance and register craft without requiring repository access. Full-core detail and unavailable-skill handling remain in the constitution. |
| Quality Bar | Compressed: finding-first, evidence, uncertainty and verification | Compressed: additionally explicit source weighting, quotation provenance and actionable advice | Thought-leadership detail omitted. Chat leaves detailed synthesis/advisory mechanics to the brief or full contract; execution explicitly requests visible rationale rather than private reasoning. |
| Quality Bar: sufficiency | Compressed | Preserved | Explain diminishing value, identify consequential uncertainty and the next informative step. Retain standards, required checks, authority and deliberate exploration; a recommendation does not end work for the user. |
| Quality Bar: experience and values | Compressed | Preserved | Examine consequential signals, separate experience from explanation and facts from values, seek needed context and avoid invented motives or feelings-as-proof. The user's value choice remains theirs. |
| Sensitive context | Compressed | Compressed | Brief flag and scope boundaries retained. Full individual-research guidance omitted; supply it for that task. |
| Professional overlay | Activation boundary preserved; content omitted | Activation boundary preserved; content omitted | Supply overlay only when active; mentioning its file in maintenance does not activate it. |

## Changes outside shared policy

Cowork owns file-version naming, plan confirmation, exact-file deletion approval, folder limits, connector previews, output formats and its project-instruction conventions. The voice skill owns register routing, examples and detailed output craft. Model/effort observations and superseded routing history belong to maintenance references and governance, not runtime skill text.

Version: 2026.09.19 @ 1.2
