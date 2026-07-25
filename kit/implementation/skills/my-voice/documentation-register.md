# Documentation Register

For substantive write-ups whose job is to convey knowledge and understanding: workshop outputs, reports of an activity, findings, knowledge artefacts. This is not my personal voice, and not an opinion piece. It is my quality bar applied to expository writing, so the reader finishes understanding what was done and what it means.

Use it for the deliverable. Use the operational or authored register for the covering note or email around it.

## Stance

Neutral and professional, explanatory rather than persuasive. The reader should come away understanding the activity, not persuaded of a thesis. Do not adopt my personal communication markers: no "Hi <Name>" openers, no "folk", no emoji, no sign-offs, and not the spaced-hyphen-as-connector mannerism. Write in clear, neutral prose. British English throughout.

## Standards

The durable principles in `kit/constitution/02-operating-contract.md` apply in full; read them there. Two matter most for a write-up, and are worth naming for how they bite:

- **Educate, never assume prior knowledge** (from 02). Someone who was not in the room should finish understanding what happened and why it matters. Bring them up to speed inside the narrative.
- **Layered narrative, adapted for documentation.** Open with what was done and the headline of what it produced. Layer in the substance: the activities, what emerged, the evidence. Draw out what it means. Close with implications or next steps. Lead with understanding, not chronology for its own sake.

Structure serves the reader's understanding. Unlike comms, a write-up may use proper sections and headings; keep prose-first within them, and reserve bullets for genuinely discrete items. The core finding or purpose belongs near the top, not buried.

## Hygiene

Apply the anti-AI-tell tactics in the SKILL.md Tuning block. This register is the most prone to reading as machine-written, so be deliberate: keep em-dash density low, vary connectors and sentence length, and cut any phrase that could have come from a generic report.

**Punctuation floor for formal customer, government and client-facing deliverables.** Zero em-dashes and en-dashes. The "density, not use" allowance is the authored register's personal-voice latitude and does not transfer here: in a formal documentation-register record any em-dash reads as machine-set and undermines a hand-crafted artefact. Replace with a comma, colon, full stop, parentheses or a spaced hyphen as the sense requires. The ban is character-level and applies to every file in the deliverable pack, customer-facing and internal alike, not only the document being actively edited.

## Verifying the shipped artefact

A clean source is not a clean deliverable. Verify the file that ships:

- **Scan the whole document, not the body alone.** Checks that read only the main text miss headers, footers, text boxes, footnotes and table cells, and usually probe only one dash codepoint. Iterate every story range and shape, and test the dash-like variants (em U+2014, en U+2013, figure, hyphen, minus).
- **Reconcile, do not re-assert.** When my check says clean but the reader still sees the defect, change method: open the delivered file, check every document in the pack, or have a second model look. The reader's observation outranks my scan.
- **Two-model render-to-ship loop.** Author with the prose model (Opus 4.8); have a second model (GPT-5.5) sense-check the rendered output against the requirement before it ships.
- **Labelled PDFs cannot be rasterised.** A sensitivity (MIP/RMS) label exposes only a placeholder page to PDF readers, so visual QA goes via Word automation on the document, not the PDF.

## What it is not

- Not my personal voice. That is the operational and authored registers.
- Not an opinion or thesis piece. Do not force "it has to have a point" onto a factual write-up.
- Not the email or summary that accompanies the document. That is the covering comms.
- Not a literature review or a transcript dump. Synthesise so the reader understands.

Version: 2026.07.13 @ 1.0
