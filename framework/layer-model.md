← [Home](../README.md) · [Framework](README.md) · **Layer model** · [Adoption guide](adoption-guide.md)

# The Layer Model

A personal AI operating system organised as five layers, ordered by two properties that turn out to be the same property: how much authority a layer carries, and how slowly it changes. The higher the layer, the more it governs and the less often it moves.

```
┌────────────────────────────────────────────────────────────┐
│  1  PHILOSOPHY        why AI is in the system at all       │  changes rarely
│                       axioms; never loaded at runtime      │
├────────────────────────────────────────────────────────────┤
│  2  CONSTITUTION      enduring behavioural principles      │  changes occasionally
│                       core or condensed contract           │
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
     and governance (ADRs, design decisions, evidence)
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

**1 — Philosophy.** One short file of axioms: the owner's theory of why AI is in their system, what counts as knowledge, what must never be optimised away. It is background rather than ordinary runtime instruction; supply it only when reviewing the foundations. Its authority operates at maintenance time: when a constitutional question is ambiguous during review, the philosophy is the tiebreaker, and a change to it triggers a review of the constitution. Writing it is a thinking exercise the owner cannot delegate; an assistant can interview and challenge, but axioms drafted by a model are scaffolding until the owner has rewritten each one or struck it.

**2 — Constitution.** The policy source, supplied as the full core or a condensed derivation: who the owner is (calibration), how the AI must engage (binding operating rules), and any conditional overlays for specific professional contexts. This is the most tuned layer, and deliberately hard to change once it works. Every file declares its own classification inline — binding rules, calibration, or conditional — and a short bootstrap file declares the hierarchy across them, so the intended precedence remains explicit when loading order varies. This is an internal instruction hierarchy within the host’s controls, not a guarantee of adherence or a way to elevate a file’s message authority.

**3 — Role charters.** One page per role the AI can hold: mission, decision policy, boundaries, cadence. A charter supplements the constitution and never overrides it — the same subordination pattern conditional overlays and skills declare. Charters load only when their role is active, so ordinary conversations carry no extra weight. The default role (the everyday thinking partner) can legitimately stay embedded in the constitution rather than being extracted: if that file is the most tuned artefact in the system and the regression probes are written against it, extraction is a risk with no behavioural payoff until a second consumer needs the charter standalone.

**4 — Implementation.** Everything product-shaped: platform adapters (a condensed contract per product, derived from the constitution, never forked), skills (reusable capabilities with a portable package core and client-specific discovery, invocation and permission semantics), vendor plugins and native capabilities (distribution/runtime forms that may combine skills, tools and other components), and prompts (starting points that graduate into skills when they need structure). This layer changes constantly and is deliberately disposable — a vendor changing its configuration model should cost an adapter update, never a rewrite of the layers above.

**5 — Memory.** The knowledge store, platform memory, and conversation history. It lives outside the kit: memory is state, not system. The kit governs deliberate actions taken through tools at the boundary; product settings govern ambient memory and history retained automatically by a service. The store's internal structure belongs to the store. Keeping the seam clean is what lets the store or product be replaced without touching the operating system.

## What loads at runtime

- **Always:** the full-core constitution or a supported condensed derivation. Deferral is written into the condensed prompt itself: an explicit instruction that the full files take precedence on everything they cover, so intended precedence is explicit. Actual composition and adherence still depend on the host and model.
- **Conditionally:** overlays and role charters. Each declares its own activation rule inline, naming an observable trigger — a professional context, a task type, a named surface — and the default when the trigger is ambiguous is inactive.
- **At execution only:** output-voice material. The owner's voice is a rendering capability invoked when producing output on their behalf, never the register of the thinking dialogue.
- **Maintenance and review only:** philosophy, framework documents, governance records and evals. They are not standing instructions for ordinary work; material supplied for review remains review data.

The intended loading discipline is to supply only relevant conditional material. Actual context cost also depends on host instructions, discovery metadata, tools and retrieved content. Verify what the host exposes and loads; file organisation alone cannot establish token savings.

## Capability, package and runtime

A capability defines an outcome and acceptance standard. A package distributes an implementation, potentially combining skills, tools, hooks, agents and references. A runtime supplies or executes it in a particular host. These are distinct: shared capability standards can be satisfied by different native implementations, and a portable instruction file does not reproduce an entire plugin.

A portable package must carry the guidance needed to complete its job with its declared base. References to a policy's source location establish provenance; they do not imply that a deployed host can read the source repository. Supply a bounded derivation where a condensed base omits required detail, keep the full policy authoritative when present, and test the package without repository access.

Maintain one concise tracker of the adopted working set: purpose, upstream source, platform and a brief deployment note. Distinguish actual use from selection or installation. Keep unselected offerings and superseded research out of the active tracker; preserve useful history through version control or dated evidence.

Prefer the host provider's useful native or own published implementation, checking authorship separately from marketplace membership. Independent skills can be shared where useful and supported. Platform guides own setup and supported controls; evidence records detailed observations. Assess the whole bundle when enablement is package-wide. Use managed delivery and compare alternatives when value or interference is uncertain. More installed packages or fewer source bytes establish neither better results nor token savings.

## Design principles

These principles combine lessons from use with explicit architecture choices. Dated evidence belongs with the implementation; documenting a principle does not establish its effectiveness on every model.

**Declare authority; never imply it.** Files with different operational weight — binding rules, calibration, working memory, conditional overlays — will be interpreted inconsistently if the model has to guess which is which. The failure is insidious: the content is all read, the output is competent, and the operating rules are followed in some sessions but not others. Every file self-declares its classification, and a bootstrap file declares the hierarchy.

**Platform prompts are derived, never forked.** Maintain reviewed shared derivations by use, with an explicit account of preserved, compressed and omitted rules. Generate detached copies where needed and check them for drift; keep product-specific wrappers separate. Constitution-to-derivation review is semantic work, while distribution is deterministic. A matching copy does not prove complete coverage. Additional product safeguards should declare their required base rather than duplicating its general policy. When a loading combination changes, update the corresponding evaluation fixtures. Keep source alignment and recorded deployment separate: an earlier result applies to the version tested, not automatically to later edits.

**Separate policy, craft and model guidance.** Keep durable judgement, ownership and approval rules in the constitution; keep output craft in the relevant capability. Dated model and host guidance belongs in implementation references. A personal writing preference need not be a claim about every model’s defaults. Select only applicable adjustments, and distinguish vendor advice from observed local behaviour.

**Separate enduring role guidance from changing context.** A professional overlay can carry a stable remit, incentives and useful perspectives while current assignments, agreements and organisational structures require review. Prefer fixed historical anchors to rolling tenure counts. Date a contextual snapshot when it materially helps ordinary work, state when it needs checking, and keep named contacts, active initiatives and publication lists in task context or the external knowledge store. A file's revision date does not certify every embedded fact. Describe the owner's experience and developed views with their evidential limits, and keep professional perspectives open to revision rather than turning them into a compulsory checklist.

**Derive by task before model.** One model may serve both exploration and execution. A condensed execution contract should preserve scope, attribution and handover state without importing the full thinking-partner context into every bounded task. A model-access subscription is not itself a prompting profile. Split a constitution only if durable policies diverge, rather than because models differ in formatting or effort settings.

**Keep the register seam visible.** The assistant reasons in its own neutral voice; the owner's voice is applied only to output produced on their behalf. The reason is protection, not style: a partner that drifts into the owner's register gets scrutinised less, because it reads like their own reasoning coming back at them.

**Keep personalisation open to revision.** Calibration describes useful tendencies without making habitual reasoning methods immune to challenge. Test their fit when a concrete detail, a weak analogy or a missing approach could change the result; retain methods that work. Give the assistant responsibility to identify when further work adds little, while preserving standards, required checks, authority and deliberate exploration. Treat expressed reactions as potentially informative signals whose explanations need examination, and distinguish factual uncertainty from choices between values. These are interaction rules to evaluate, not personality diagnoses or permission to decide for the owner.

**Gate constitutional change on evals.** Maintain a small set of behavioural regression probes — sycophancy, premature convergence, posture, voice separation — and run selected cases before and after an amendment, several runs per fixture. Apply factual grounding, ownership and authority checks to every response; a local behaviour pass cannot override a failed boundary. Separate change comparisons from comparisons with the same host and model without the personal instructions. Freeze cases, rubrics, conditions and stopping rules before running, retain failed attempts, and check transfer beyond the prompts used for repair. Evaluate usefulness and friction alongside compliance; evidence of the owner's learning requires their participation. A change that regresses a probe is reverted or reworked, and an unchanged baseline failure remains visible. If the owner explicitly excludes behavioural runs for a named change batch, record that bounded exception and retain the uncertainty; static review does not replace behavioural evidence or abolish the standing policy.

**Critique cold before committing.** Changes to high-authority layers get a second pass by a fresh-context model that has not seen the drafting conversation. The author in context cannot see a rule that sounds protective while resting on nothing, or an instruction that reads correctly and permits exactly the failure it exists to prevent; a cold reader finds both readily. This is the two-model workflow, and it is mandatory above the implementation layer.

**Disambiguate coexisting numbering schemes.** If the architecture numbers its layers and a file inside one layer numbers its own internal hierarchy, name them as distinct schemes wherever both could load. A model given "level 3" twice will eventually apply one scheme's rules to the other's content.

**Lifecycles run capture-and-graduate.** Prompts graduate into skills when they need structure; observations graduate into principles through repeated application, not at the moment of capture. Nothing enters the system at its final maturity.

**Give each record one responsibility.** Keep current state in its maintained reference and observations in dated evidence. Consolidate repeated rationale without losing the decision, its reason, rejected alternatives or conditions for reconsideration. Historical examples illustrate selected qualities; label them so superseded wording does not compete with current rules.
