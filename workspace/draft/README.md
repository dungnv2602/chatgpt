# Drafts

This folder stores proposals that require a user decision.

## Files

- [DRAFT_TEMPLATE.md](../DRAFT_TEMPLATE.md) — canonical template for new proposals (Version 1.2). It requires detailed, evidence-qualified assessments of every viable option.
- DRAFT-*.md — one record for each distinct proposal.

## Current Drafts

- [DRAFT-0002 — Phase-Aware Planning and Evidence Capture](DRAFT-0002-phase-aware-planning-and-evidence-capture.md) — Revision 4. Style-only wording update. The discussion register records approval of Option 3 with added requirements. The Draft metadata and task record still show review-pending state. Reconcile the exact approved revision and scope before ADR promotion.
- [DRAFT-0003 — Area, Project, and Task Architecture](DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md) — Revision 1 in review. Companion to DRAFT-0002. Recommends project folders with nested task folders, one global task board, scoped resources, and the existing global Draft/ADR and archive contracts.

## Workflow

1. Create one Draft for each decision that may change repository structure, policy, architecture, workflow, or long-lived practice.
2. Use a unique DRAFT-NNNN ID. Do not reuse an ID.
3. Record the problem, scope, goals and non-goals, decision drivers, and assessment basis. Include every materially viable option and its comparative assessment. Record the recommendation, consequences, risks, affected files, implementation outline, user questions, and source/evidence register.
4. Assess every viable option in comparable depth. Include the current approach/no-change option when viable and materially distinct variants when their trade-offs differ. For each option, cover its operating model, repository/environment fit, concrete strengths, neutral trade-offs, weaknesses, implementation/migration cost, dependencies, operational burden, risks/safeguards, evidence/confidence, and limitations/unknowns.
5. Compare options against the same decision drivers in a qualitative matrix when multiple viable options exist. Explain the decisive differences and why the recommendation is preferable to the strongest alternative. Do not invent numeric scores or force a matrix when only one option is genuinely viable. Explain why alternatives are infeasible.
6. Preserve evidence provenance. Identify source versions, dates, commits, hosts, samples, test protocols, and untested scenarios where applicable. Separate repository facts, external claims, tests/benchmarks, inferences, and hypotheses. State what the evidence does not establish.
7. Complete the Draft quality gate in the canonical template and the Worker's [decision-governance reference](../../.agent/skills/the-worker/references/decision-governance.md). Assess every option before you present the list. Link the recommendation to the criteria and evidence.
8. Link the Draft in the matching workspace/discussion.md Open Discussion item.
9. Set its status to in-review when you present it to the user.
10. Revise the same Draft when the user requests changes. Record each meaningful revision.
11. Create an ADR only after the user approves the exact Draft revision and its scope.
12. Create the ADR as promotion-pending. Complete the rationale comparison and read-back before changing its status to accepted.
13. Read back the accepted ADR. Delete the source Draft only after this check passes.
14. Delete the source Draft from this index. Keep its ID as ADR provenance. Do not link the ADR to the deleted source file.

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

Do not create `.archive/draft/` or a Promoted Drafts section. ADR-0002 does not change retention rules for rejected, withdrawn, or superseded Drafts.
