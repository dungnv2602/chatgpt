# Drafts

This folder stores proposals that require a user decision.

## Files

- [`DRAFT_TEMPLATE.md`](../DRAFT_TEMPLATE.md) — canonical template for new proposals.
- `DRAFT-*.md` — one record for each distinct proposal.

## Current Drafts

- [DRAFT-0002 — Phase-Aware Planning and Evidence Capture](DRAFT-0002-phase-aware-planning-and-evidence-capture.md) — In review. User approval is pending.
- [DRAFT-0003 — Retire Source Drafts After Verified ADR Promotion](DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md) — In review. The user approved the lifecycle direction and rationale safeguard; exact revision 1 approval is pending.
- [DRAFT-0001 — Establish Draft-to-ADR Governance and Repository Analysis](DRAFT-0001-repository-decision-governance-and-analysis.md) — Promoted to [ADR-0001](../adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md).

## Workflow

1. Create one Draft for each decision that may change repository structure, policy, architecture, workflow, or long-lived practice.
2. Use a unique `DRAFT-NNNN` ID. Do not reuse an ID.
3. Record the problem, scope, decision drivers, options, recommendation, consequences, risks, affected files, and user questions.
4. Link the Draft in the matching `workspace/discussion.md` Open Discussion item.
5. Set its status to `in-review` when you present it to the user.
6. Revise the same Draft when the user requests changes. Record each meaningful revision.
7. Create an ADR only after the user approves the exact Draft revision and its scope.
8. Mark the Draft `promoted` and link the new ADR. Preserve the Draft.

## Status values

- `draft` — work is in progress and is not ready for review.
- `in-review` — the user can review the proposal.
- `changes-requested` — the user requested revisions.
- `approved-for-adr` — the user approved the exact proposal. ADR creation remains pending.
- `promoted` — the accepted decision now has an ADR.
- `rejected` — the user rejected the proposal.
- `withdrawn` — the proposal was withdrawn.
- `superseded` — a later Draft replaces this proposal before approval.

Approval applies only to the Draft revision and scope that the user identifies. Silence, task creation, or approval of a related item is not approval.

A Draft is not authority to implement its proposal. A design task may prepare a Draft. An implementation task must reference an accepted ADR.

Do not delete Drafts after promotion, rejection, or withdrawal. They preserve proposal history. Use the ADR link to navigate from a promoted Draft to its accepted decision.
