← [Home](../../README.md) · [Governance](../README.md) · [Evidence](README.md) · **Voice plugin validation**

# September 2026 Voice Plugin Validation and Repair

## Scope and implementation plan

Andrew requested an Agent Plugins wrapper for my-voice, validation against the constitution and available Codex interaction history, then a plan and implementation of the repairs with removal of the installed Codex skill.

The implemented plan is:

1. Repair conflicting punctuation rules, evidence exceptions, representative capacity and purpose-based routing.
2. Preserve supplied emotion, make audience research proportionate, and strengthen narrative progression and economy.
3. Add clearly labelled broadcast and authored worked examples without claiming human authorship or endorsement.
4. Rebuild the portable plugin, check its structure and source alignment, and perform bounded text checks and independent source review.
5. Remove the standalone local Codex skill and update the deployment records.

The [four-file source](../../kit/implementation/skills/my-voice/SKILL.md) remains canonical. The [plugin wrapper](../../kit/implementation/plugins/my-voice/README.md) targets published Agent Plugins 1.0.0, preserving the skill body and companions while omitting the client-specific invocation field from the packaged copy. The constitution and generated operating contracts are unchanged.

## Repairs

- Purpose and ownership select the register; audience and representative capacity shape its expression. Medium defaults cannot create a call, commitment or new ask. Personal correspondence has no automatic Microsoft signature.
- Sensitive writing retains Andrew's supplied interpersonal meaning. A sufficient brief needs no compulsory recipient research.
- Craft constraints apply to new prose, preserving exact quotations, source wording, titles, identifiers and legitimate notation. Documentation no longer recommends the spaced-hyphen mannerism it prohibits elsewhere.
- Verification stays within authorised access and approved editing targets. A text draft cannot establish rendered-artifact verification.
- Broadcast craft permits short complete sentences and checks repeated asks, thanks and conclusions. Authored craft develops evidence or supplied experience into an owned position, without inventing an anecdote.
- Examples distinguish constructed demonstrations, retained source samples and authentic historical writing. The empty argument-example description now points to the passage it describes.

Retained Codex interactions support the importance of explanatory narrative, practical consequences and evidence limits. Those observations do not establish a corpus of endorsed finished writing. Contemporary, explicitly endorsed broadcast and sustained authored pieces remain a calibration gap; the new demonstrations do not close it.

## Validation and limits

The initial review used the full constitution, both condensed bases, canonical source and packaged copy. Ten fresh-context text probes and an independent source review identified the repairs. Ownership, neutral exploration, audience fit and factual attribution held in those examples; a broadcast repeated requests and thanks. These were diagnostic observations, not a reliability estimate.

After repair, six fresh-context text probes used the full core plus the explicit portable package. The ownership case requested missing substance; the personal email omitted the corporate title; the sensitive note retained supplied warmth without a new promise; the quotation case preserved exact punctuation; the scope case limited its correction and stated that the rendered document remained unverified. The broadcast still restated its request, prompting a specific opening-versus-closing economy check. A separate fresh-context source review found no actionable contradictions or losses of intent in the four-file revision it received. The subsequent economy and punctuation-summary refinements were checked separately.

One additional broadcast probe after that refinement still restated the recommendation as a closing request. No further tuning or repeated sampling was performed. The source now states the economy requirement explicitly, but these observations do not establish reliable adherence to it. Skill-use notices also remained outside the copy in the test responses. These are residual output-quality limits, not reasons to weaken the ownership or evidence boundaries.

All model calls requested `gpt-6-astra` at medium effort through `codex-cli 0.155.1`, in ephemeral contexts with project instructions, host skill discovery and execution tools disabled using the existing runner's command construction. The package was supplied explicitly. CLI warnings reported experimental discovery isolation and disabled code mode; calls completed without tool execution. Raw inputs, responses and source snapshots remain in private temporary working material. This diagnostic batch did not use the harness's blinded grading protocol and does not establish host discovery, plugin installation, cross-model reliability, rendered-file quality or Andrew's endorsement of the prose.

Structural checks passed: published plugin manifest schema, generic skill validation on the portable copy, exact archive freshness, documentation links, whitespace and all seven generated operating-contract copies. The canonical frontmatter retains its existing client extension; the portable copy is the standard-format validation target.

## Codex removal and remaining deployment state

The removed target was the standalone personal my-voice skill directory, containing exactly `SKILL.md`, `authored-register.md`, `documentation-register.md` and `examples.md`. Before removal, the entry point and documentation register matched the earlier repository source; the authored register and examples were older.

An exact four-file restoration copy was verified outside discovery roots in private temporary storage. The four installed files and their directory were deleted, and absence was verified. This does not remove text already loaded into an existing conversation. No replacement plugin, marketplace entry or other skill was installed or changed. The [Codex baseline](../../kit/implementation/platforms/codex/configuration-baseline.md) records the requested absent state.

Claude's last verified enabled package is v4 from the earlier instruction refresh. The current source repair was not deployed there; the [Claude baseline](../../kit/implementation/platforms/claude/configuration-baseline.md) records that gap. Source packaging and explicit-package text probes do not establish a live deployment. No commit or publication is included in this batch.
