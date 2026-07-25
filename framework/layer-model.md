← [Home](../README.md) · [Framework](README.md) · **Layer model** · [Adoption guide](adoption-guide.md)

# The Layer Model

A personal AI operating system organised as five layers, ordered by two properties that turn out to be the same property: how much authority a layer carries, and how slowly it changes. The higher the layer, the more it governs and the less often it moves.

```
┌────────────────────────────────────────────────────────────┐
│  1  PHILOSOPHY        why AI is in the system at all       │  changes rarely
│                       axioms; never loaded at runtime      │
├────────────────────────────────────────────────────────────┤
│  2  CONSTITUTION      enduring behavioural principles      │  changes occasionally
│                       always loaded                        │
├────────────────────────────────────────────────────────────┤
│  3  ROLE CHARTERS     mission + decision policy per role   │  change with the roles
│                       loaded only when the role is active  │
├────────────────────────────────────────────────────────────┤
│  4  IMPLEMENTATION    how it deploys and executes          │  changes constantly
│                       adapters, capabilities, entry points │
├────────────────────────────────────────────────────────────┤
│  5  MEMORY            evolving knowledge and context       │  changes daily
│                       outside the kit: the knowledge       │
│                       store, platform memory, history      │
└────────────────────────────────────────────────────────────┘
     cross-cutting: evals (behavioural regression probes)
     and governance (ADRs, design decisions, reviews)
```

For a software practitioner, the mapping that motivated the model (the implementation layer appears as its three components, and the cross-cutting concerns get rows of their own):

| Layer | Software analogue |
|---|---|
| Philosophy | The spec — what the system is for |
| Constitution | The architecture — enduring constraints every component obeys |
| Role charters | Interfaces — contracts a component implements |
| Skills | Libraries — reusable capabilities invoked at need |
| Prompts | Entry points — ways in, never the source of truth |
| Platform files | Adapters — one per product, derived, disposable |
| Memory | State — the data the system operates on, not the system |
| Evals | Regression tests |

## The layers

**1 — Philosophy.** One short file of axioms: the owner's theory of why AI is in their system, what counts as knowledge, what must never be optimised away. It is background, not instruction — never loaded into conversations. Its authority operates at maintenance time: when a constitutional question is ambiguous during review, the philosophy is the tiebreaker, and a change to it triggers a review of the constitution. Writing it is a thinking exercise the owner cannot delegate; an assistant can interview and challenge, but axioms drafted by a model are scaffolding until the owner has rewritten each one or struck it.

**2 — Constitution.** The always-loaded core: who the owner is (calibration), how the AI must engage (binding operating rules), and any conditional overlays for specific professional contexts. This is the most tuned layer, and deliberately hard to change once it works. Every file declares its own classification inline — binding rules, calibration, or conditional — and a short bootstrap file declares the hierarchy across them, so the set survives being loaded in any order on any platform.

**3 — Role charters.** One page per role the AI can hold: mission, decision policy, boundaries, cadence. A charter supplements the constitution and never overrides it — the same subordination pattern conditional overlays and skills declare. Charters load only when their role is active, so ordinary conversations carry no extra weight. The default role (the everyday thinking partner) can legitimately stay embedded in the constitution rather than being extracted: if that file is the most tuned artefact in the system and the regression probes are written against it, extraction is a risk with no behavioural payoff until a second consumer needs the charter standalone.

**4 — Implementation.** Everything product-shaped: platform adapters (a condensed contract per product, derived from the constitution, never forked), skills (reusable capabilities with a portable package core and client-specific discovery, invocation and permission semantics), and prompts (starting points that graduate into skills when they need structure). This layer changes constantly and is deliberately disposable — a vendor changing its configuration model should cost an adapter update, never a rewrite of the layers above.

**5 — Memory.** The knowledge store, platform memory, and conversation history. It lives outside the kit: memory is state, not system. The kit governs deliberate actions taken through tools at the boundary; product settings govern ambient memory and history retained automatically by a service. The store's internal structure belongs to the store. Keeping the seam clean is what lets the store or product be replaced without touching the operating system.

## What loads at runtime

- **Always:** the constitution — or a condensed platform prompt derived from it when files cannot be attached. Deferral is written into the condensed prompt itself: an explicit instruction that the full files take precedence on everything they cover, so double-loading resolves cleanly instead of by accident.
- **Conditionally:** overlays and role charters. Each declares its own activation rule inline, naming an observable trigger — a professional context, a task type, a named surface — and the default when the trigger is ambiguous is inactive.
- **At execution only:** output-voice material. The owner's voice is a rendering capability invoked when producing output on their behalf, never the register of the thinking dialogue.
- **Never:** philosophy, framework documents, governance records, evals.

The consequence to preserve: an ordinary conversation costs no more tokens than the constitution. Layers add load only when genuinely active.

## Design principles proven in use

These are not aspirations; each earned its place by failing when absent or catching a real defect when present.

**Declare authority; never imply it.** Files with different operational weight — binding rules, calibration, working memory, conditional overlays — will be interpreted inconsistently if the model has to guess which is which. The failure is insidious: the content is all read, the output is competent, and the operating rules are followed in some sessions but not others. Every file self-declares its classification, and a bootstrap file declares the hierarchy.

**Platform prompts are derived, never forked.** The constitution is the single source of truth; each product gets a condensed derivation. The moment a platform prompt is edited directly, two sources of truth exist and will drift. Drift also happens without a fork — by staleness — so every constitutional amendment ends with a cascade check: does each derived prompt still say what the constitution now says?

**Separate durable rules from model tuning.** Some instructions correct a specific model generation's habits (banned phrases, formatting tics). Keep them in a clearly marked disposable block, apart from the durable rules, so they can be replaced when models change without destabilising what works.

**Keep the register seam visible.** The assistant reasons in its own neutral voice; the owner's voice is applied only to output produced on their behalf. The reason is protection, not style: a partner that drifts into the owner's register gets scrutinised less, because it reads like their own reasoning coming back at them.

**Gate constitutional change on evals.** Maintain a small set of behavioural regression probes — sycophancy, premature convergence, posture, voice separation — and run them before and after any amendment to the constitution or the condensed prompts, several runs per fixture, judged against the baseline rather than a single sample. A change that regresses a probe is reverted or reworked. Without this gate, tuning decays invisibly.

**Critique cold before committing.** Changes to high-authority layers get a second pass by a fresh-context model that has not seen the drafting conversation. The author in context cannot see a rule that sounds protective while resting on nothing, or an instruction that reads correctly and permits exactly the failure it exists to prevent; a cold reader finds both readily. This is the two-model workflow, and it is mandatory above the implementation layer.

**Disambiguate coexisting numbering schemes.** If the architecture numbers its layers and a file inside one layer numbers its own internal hierarchy, name them as distinct schemes wherever both could load. A model given "level 3" twice will eventually apply one scheme's rules to the other's content.

**Lifecycles run capture-and-graduate.** Prompts graduate into skills when they need structure; observations graduate into principles through repeated application, not at the moment of capture. Nothing enters the system at its final maturity.

Version: 2026.07.13 @ 1.3
