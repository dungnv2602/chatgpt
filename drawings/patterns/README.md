# Drawing Pattern Index

The global pattern indexes contain reusable lessons extracted from the historical prompt archive and future drawing sessions.

## Indexes

- [Successful patterns](successful-patterns.md) — techniques supported by actual accepted outputs.
- [Failure patterns](failure-patterns.md) — recurring failures, observed impacts, hypotheses, tested countermeasures, and prevention rules.
- [Entry templates](PATTERN-TEMPLATES.md) — copy-ready formats and the review checklist.

## Historical prompt indexes

- [Historical successful prompts](../history/successful-prompts.md) — pointers to successful or user-approved authored prompts before 19 November 2026.
- [Historical failed prompts](../history/failed-prompts.md) — rejected prompts, missed targets, partial matches, and unverified edit attempts from the same period.

The chronological logs remain the canonical source for full prompt wording and attempt-by-attempt outcomes. The historical indexes are navigational and do not replace or rewrite those records.

## Governance

The operational consultation checkpoint lives in
[Drawing Skill](../../skills/drawing/SKILL.md). The complete prompt-fidelity
standard is maintained in the dedicated
[Prompt Fidelity and Unrequested Restrictions note](../../skills/drawing/references/prompt-fidelity.md);
that note is the authoritative, exhaustive rule for prompt drafting, revision,
and pre-generation review. This index remains the library's navigation and
governance reference. Do not repeatedly reread the full library when the
relevant entries have already been reviewed and no refresh condition applies.

1. Consult the relevant global patterns before drafting a new prompt.
2. Treat the active drawing brief and its explicit constraints as the highest authority. Global patterns are guidance, never overrides.
3. Evaluate the returned image against the actual requested requirements. A successful tool call is not automatically a successful prompt.
4. Preserve user-designated successes as such, but distinguish user approval from independently verified prompt compliance or edit provenance.
5. Add a pattern only when it expresses a reusable lesson. Keep individual attempts in their chronological records.
6. Link each pattern to the exact source evidence. Separate observed facts from suspected causes.
7. Increase confidence only when additional evidence supports the same lesson. Retire rather than delete a pattern that becomes unreliable or is superseded.

## IDs and confidence

- Successful patterns use permanent IDs: `S-001`, `S-002`, etc.
- Failure patterns use permanent IDs: `F-001`, `F-002`, etc.
- Never reuse an ID, including after retirement.
- Confidence levels: **Provisional**, **Supported**, **Validated**, and **Retired**. Their definitions are in [PATTERN-TEMPLATES.md](PATTERN-TEMPLATES.md).

## Evidence discipline

- A prompt's authored text is not necessarily the image tool's compiled payload.
- A source filename mentioned in prose is not proof of an attachment.
- Do not call an operation an edit unless the source was actually attached and the returned result supports that claim.
- A suspected cause is not a confirmed cause. A proposed countermeasure is not an effective remedy until tested.
- Where the archive does not preserve exact wording or prompt-to-image mapping, record that limitation instead of reconstructing or guessing.
