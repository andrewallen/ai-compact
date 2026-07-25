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

- When a change to the implementation forces a rethink of the framework, that is evidence of a general lesson. Record it here, in the changelog below (and in an architecture decision record — ADR — if it is structural).
- When it does not, the lesson was personal. It stays in the implementation.

One repository is what makes that measurement possible. See [ADR-003](../governance/decisions/adr-003-framework-and-implementation-converge.md).

**Anonymisation discipline.** Nothing in this folder names the practitioner, their employer, or any personal detail. Checked at every framework change, two ways: a search of the folder for names, employers, and personal tooling, and a cold read asking whether anything narrows the author's identity. The folder must remain publishable with nothing removed beyond its repository navigation links (this file's breadcrumb and ADR pointers).

## Changelog

General lessons forced by implementation experience, newest first.

| Date | Lesson |
|---|---|
| 2026-07 | Ask reasoning models for reviewable decision artefacts such as structure, rationale, evidence and trade-offs rather than asking them to expose their thinking. Regression-test the reword so refusal risk falls without losing useful explanation. |
| 2026-07 | A reusable skill can have a portable package core without having identical behaviour on every client. Discovery, invocation, permissions and execution context belong to the product adapter and must be verified per surface. |
| 2026-07 | The layer hierarchy and the repository's reader-facing domains are different structures. A personal instance can retain shallow layers beneath one stable `kit/` boundary while the generic framework and governance remain peers. Active evals belong with the instance they test; historical results belong with dated governance evidence. Architecture is a view across these domains, not another content bucket. |
| 2026-07 | Once the logical layers proved durable, the filesystem was aligned to them. Higher-authority layers stay shallow and directly addressable; product-shaped components sit beneath one implementation directory; memory remains absent because state is not system; governance and evals stay cross-cutting. Numeric layer folders and an extra instance wrapper were rejected because authority belongs in declarations, not path ceremony. |
| 2026-07 | Framework extracted from the implementation's archived methodology during the July 2026 architecture review. Two lessons arrived with it: a rule that sounds protective can rest on nothing (a charter cited a constitutional rule that existed only in documentation — cold critique caught it), and coexisting numbering schemes must be explicitly disambiguated or a model will map one onto the other. Both are now design principles in `layer-model.md`. |

Version: 2026.07.19 @ 1.4
