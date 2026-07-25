← [Home](../README.md) · **Framework** · [Personal kit](../kit/README.md) · [Governance](../governance/README.md)

# Framework

The generic, reusable pattern instantiated by the personal kit: a layered architecture for governing how AI works with one person. Everything in this folder is written abstractly and contains nothing personal. The personal reference implementation lives in [`kit/`](../kit/README.md); its architecture decisions and evidence live in [`governance/`](../governance/README.md).

The test these files are held to: a stranger could read this folder alone and build their own implementation.

## What the framework is

Most AI use starts from zero. Every conversation re-establishes who the person is, what standard the output is held to, and how challenge should work — or, more often, never establishes it at all. The framework is a pattern for fixing that structurally: a small set of versioned, model-agnostic files — the kit — ordered by authority, that carry a person's identity, operating rules, and roles into any AI conversation on any platform.

It is not a prompt library. Prompts are the thinnest layer of the pattern — entry points, never the source of truth. The framework's substance is the authority structure: which files bind, which calibrate, which activate conditionally, and how the whole set survives moving between models and products.

## Contents

| File | What it covers |
|---|---|
| [layer-model.md](layer-model.md) | The five layers, the authority and rate-of-change ordering, what loads at runtime, the subordination rules, and the design principles the reference implementation has proven in use. |
| [adoption-guide.md](adoption-guide.md) | The minimum viable implementation — four files and a critique pass — and how to grow it: the interview principle, the two-model workflow, failure modes, and evaluation criteria. |

## Who it is for

The pattern is most productive for practitioners in knowledge-intensive work — strategy, policy, research, technology leadership — with substantial accumulated expertise that has never been systematically articulated, and a genuine willingness to have their thinking challenged rather than confirmed. It is a practice, not a project: the compounding property depends on sustained use. Someone wanting better one-off answers from AI does not need this; someone wanting a consistent, challenging, cumulative thinking partnership does.

## The seam rule

The framework and the reference implementation co-evolve in one repository, deliberately. The rule that maintains the boundary:

- When a change to the implementation forces a rethink of the framework, that is evidence of a general lesson. Incorporate it into the relevant framework document and record an architecture decision if it is structural.
- When it does not, the lesson was personal. It stays in the implementation.

One repository is what makes that measurement possible. See [ADR-003](../governance/decisions/adr-003-framework-and-implementation-converge.md).

**Anonymisation discipline.** Nothing in this folder names the practitioner, their employer, or any personal detail. Checked at every framework change, two ways: a search of the folder for names, employers, and personal tooling, and a cold read asking whether anything narrows the author's identity. The folder must remain publishable with nothing removed beyond its repository navigation links (this file's breadcrumb and ADR pointers).

## Maintaining the framework

Framework changes must remain independently understandable and anonymised. Durable lessons belong in the relevant framework document; structural changes also require an ADR. Every rule must trace to an operative source rather than a comment elsewhere, and any coexisting numbering or authority schemes must be explicitly disambiguated.
