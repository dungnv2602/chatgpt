# Drawing Pattern Index

The global pattern indexes contain reusable lessons extracted from the historical prompt archive and future drawing sessions.

## Indexes

- [Successful patterns](successful-patterns.md) — techniques supported by actual accepted outputs.
- [Failure patterns](failure-patterns.md) — recurring failures, observed impacts, hypotheses, tested countermeasures, and prevention rules.
- [Entry templates](../../assets/pattern-entry-templates.md) — copy-ready formats and the review checklist.

## Historical prompt indexes

- [Historical successful prompts](../../../../drawings/history/successful-prompts.md) — pointers to successful or user-approved authored prompts before 19 November 2026.
- [Historical failed prompts](../../../../drawings/history/failed-prompts.md) — rejected prompts, missed targets, partial matches, and unverified edit attempts from the same period.

The chronological logs remain the canonical source for full prompt wording and attempt-by-attempt outcomes. The historical indexes are navigational and do not replace or rewrite those records.

## Governance

The operational consultation checkpoint is in the
[Drawing Skill](../../SKILL.md). The complete prompt-fidelity standard is in the
[Prompt Fidelity and Unrequested Restrictions note](../prompt-fidelity.md).
That note is the authoritative rule for prompt drafting, revision, and
pre-generation review. This index provides navigation and governance.
Do not reread the full library when you have already reviewed the relevant
entries and no refresh condition applies.

1. Consult the relevant global patterns before drafting a new prompt.
2. Treat the active drawing brief and its explicit constraints as the highest authority. Global patterns are guidance, never overrides.
3. Evaluate the returned image against the actual requested requirements. A successful tool call is not automatically a successful prompt.
4. Preserve user-designated successes as such, but distinguish user approval from independently verified prompt compliance or edit provenance.
5. Add a pattern only when it expresses a reusable lesson. Keep individual attempts in their chronological records.
6. Link each pattern to the exact source evidence. Separate observed facts from suspected causes.
7. Increase confidence only when additional evidence supports the same lesson. Retire rather than delete a pattern that becomes unreliable or is superseded.

## Post-attempt review and approval

The Drawing Skill requires a pattern review after every generation or edit attempt. Assess each returned image against its recorded acceptance criteria. Inspect refusals, failed calls, no-output results, partial matches, and off-target outputs.

### Success candidates

- Propose a success pattern only when the output meets its critical criteria or the user explicitly accepts it.
- The technique must contribute to a meaningful improvement or protect an important requirement.
- A successful tool call alone is not evidence of a successful image.
- A partial result may support a success candidate only for a specific requirement it visibly satisfies.

### Failure candidates

- Review failures, refusals, partial matches, missed targets, wrong operations, source-linkage failures, and workflow deviations.
- Propose a failure pattern only for a recurring problem or an important reusable risk.
- Do not promote every isolated failure.
- Separate observed facts from suspected causes. List a countermeasure as tested only when an attempt tested it.

### Existing-pattern review

- Compare each candidate with existing entries. Avoid duplicates.
- Propose an evidence, confidence, scope, limitation, or retirement change when new evidence supports it.
- Assess each output separately. One attempt may support both success and failure candidates.
- If no reusable lesson exists, do not create a candidate.

### User approval gate

1. Present each proposed change to the user before editing either index.
2. Include its change type, target entry or new entry, scope, principle or observed failure, impact, evidence, hypotheses, tested countermeasures, confidence, and limitations.
3. Discuss and revise the proposal until the user approves its exact content and scope.
4. Require explicit approval for each new entry or existing-entry change. One approval may cover several proposals only when it identifies each one.
5. Silence, image approval, prompt approval, and approval of this workflow do not approve a pattern change.
6. Assign a new permanent ID only after approval. Preserve the existing ID for an approved update.
7. Write only the approved change. Record its approval date and exact attempt evidence.
8. Read back the updated entry. Do not write a rejected or deferred proposal.

## IDs and confidence

- Successful patterns use permanent IDs: `S-001`, `S-002`, etc.
- Failure patterns use permanent IDs: `F-001`, `F-002`, etc.
- Never reuse an ID, including after retirement.
- Confidence levels: **Provisional**, **Supported**, **Validated**, and **Retired**. Their definitions are in [pattern-entry-templates.md](../../assets/pattern-entry-templates.md).

## Evidence discipline

- A prompt's authored text is not necessarily the image tool's compiled payload.
- A source filename mentioned in prose is not proof of an attachment.
- Do not call an operation an edit unless the source was actually attached and the returned result supports that claim.
- A suspected cause is not a confirmed cause. A proposed countermeasure is not an effective remedy until tested.
- Where the archive does not preserve exact wording or prompt-to-image mapping, record that limitation instead of reconstructing or guessing.
