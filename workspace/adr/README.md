# Accepted Decision Records

This folder stores user-approved decisions that still require implementation or confirmation.

## Files

- `ADR_TEMPLATE.md` — canonical template for accepted decisions.
- `ADR-*.md` — active accepted decision records. File names use a numeric sequence and a lowercase dashed title.

## Numbering and organization

- Assign a global, permanent `ADR-NNNN` ID only after the user approves the source Draft.
- Use the filename `NNNN-title-with-dashes.md`. Keep the Markdown title unnumbered.
- Keep one flat folder. Use optional metadata tags to group decisions. Do not create category folders or local numbering.
- Never reuse an ADR ID.

## Status and implementation

The decision status and implementation status are separate.

Decision status values:

- `accepted` — the approved decision is active.
- `superseded` — a later ADR replaces the decision. Link the replacement.
- `deprecated` — the decision is no longer recommended, with no direct replacement.
- `reversed` — the user explicitly reversed the decision.

Implementation status values:

- `not-started`
- `in-progress`
- `complete`
- `not-required`
- `superseded`

Only create an ADR with status `accepted`. A rejected proposal remains a Draft.

## Implementation rules

1. Every new implementation task must link one or more accepted ADRs.
2. Task approval remains separate from decision approval.
3. Each task must state which ADR requirements it implements.
4. An accepted ADR does not authorize unrelated scope.
5. If new work is not covered by an accepted ADR, create a Draft and obtain approval before implementation.
6. Update the ADR's task links and implementation status when task state changes.
7. Record evidence for each Confirmation criterion in the ADR or linked task records.

## Immutability and archive

The accepted decision is immutable. Do not rewrite its rationale or chosen outcome. Create a new ADR that supersedes it when the decision changes.

Only update lifecycle metadata, task links, review history, and implementation confirmation. Record why and when each lifecycle change occurred.

When all linked implementation tasks are Done and the Confirmation criteria pass, move the ADR to `archive/adr/`. Also archive a decision whose implementation status is `not-required` after its confirmation check.

Never add ADRs to `.github/archive-retention-index.json`. The archive retention workflow must not delete ADRs. Keep the original ID and filename when you archive an ADR. Do not edit or delete an archived ADR.
