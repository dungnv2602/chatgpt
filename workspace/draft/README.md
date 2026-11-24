# Drafts

This folder stores proposals that require a user decision.

## Files

- [DRAFT_TEMPLATE.md](../DRAFT_TEMPLATE.md) — canonical template for new proposals.
- DRAFT-*.md — one record for each distinct proposal.

## Current Drafts

- [DRAFT-0002 — Phase-Aware Planning and Evidence Capture](DRAFT-0002-phase-aware-planning-and-evidence-capture.md) — In review. User approval is pending.

## Workflow

1. Create one Draft for each decision that may change repository structure, policy, architecture, workflow, or long-lived practice.
2. Use a unique DRAFT-NNNN ID. Do not reuse an ID.
3. Record the problem, scope, decision drivers, options, recommendation, consequences, risks, affected files, and user questions.
4. Link the Draft in the matching workspace/discussion.md Open Discussion item.
5. Set its status to in-review when you present it to the user.
6. Revise the same Draft when the user requests changes. Record each meaningful revision.
7. Create an ADR only after the user approves the exact Draft revision and its scope.
8. Create the ADR as promotion-pending. Complete the rationale comparison and read-back before changing its status to accepted.
9. Read back the accepted ADR. Delete the source Draft only after this check passes.
10. Remove the source Draft from this index. Keep its ID as ADR provenance. Do not link the ADR to the deleted source file.

If deletion fails after acceptance, keep the source Draft temporarily. Record the resulting ADR ID and cleanup reason in its metadata. List it only under Promotion Cleanup Pending. Retry deletion without creating another ADR or repeating approval.

## Status values

- draft — work is in progress and is not ready for review.
- in-review — the user can review the proposal.
- changes-requested — the user requested revisions.
- approved-for-adr — the user approved the exact proposal. ADR creation remains pending.
- rejected — the user rejected the proposal.
- withdrawn — the proposal was withdrawn.
- superseded — a later Draft replaces this proposal before approval.

Do not use promoted as a Draft status. A successful promotion deletes the source Draft after the accepted ADR passes its completeness and read-back checks.

Approval applies only to the Draft revision and scope that the user identifies. Silence, task creation, or approval of a related item is not approval.

A Draft is not authority to implement its proposal. A design task may prepare a Draft. An implementation task must reference an accepted ADR.

Do not create archive/draft/ or a Promoted Drafts section. ADR-0002 does not change retention rules for rejected, withdrawn, or superseded Drafts.
