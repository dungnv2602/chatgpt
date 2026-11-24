---
record_type: decision-record
template_version: "1.0"
id: "ADR-0002"
status: "accepted"
decision_date: "2026-11-24"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0003"
related_adrs:
  - "ADR-0001"
supersedes: []
superseded_by: null
implementation_status: "not-started"
implementation_tasks:
  - "20261124-160500"
review_triggers:
  - "A promotion completeness check fails."
  - "A source Draft cannot be deleted after ADR acceptance."
  - "A material decision-rationale gap is found during migration."
  - "The user changes the Draft or ADR lifecycle."
---

# Retire Source Drafts After Verified ADR Promotion

## Context and Problem Statement

The current Draft-to-ADR workflow preserves a source Draft after promotion. It marks the Draft `promoted`, links it to the accepted ADR, and keeps it in `workspace/draft/`.

This leaves two records for one accepted decision. The ADR is authoritative, but the promoted Draft remains visible in the proposal collection. It can create uncertainty about which record governs the decision and leaves completed proposals in an active workspace.

Deleting a Draft immediately after writing an ADR creates a data-loss risk. The ADR may omit material rationale, constraints, rejected alternatives, trade-offs, safeguards, or approval scope from the Draft. The source Draft must remain until the resulting ADR has been read back and checked against the complete approved proposal.

DRAFT-0003 revision 2 proposed a transaction-like promotion process. The user approved that exact revision and its scope on 2026-11-24. This ADR records the accepted decision. It supersedes only the source-Draft preservation rule established by ADR-0001. ADR-0001 remains the authoritative record for its other decisions.

### Historical context retained from DRAFT-0001

The source Draft included decision rationale that ADR-0001 summarized rather than fully restated:

- Keep `workspace/analysis/` inside `workspace/` because workspace is the repository's planning and coordination area. A root-level `analysis/` directory would create another peer domain without a clear owner. Keep automated CI diagnostics under `reports/`; analysis synthesizes repository state rather than duplicating the CI Ledger.
- Use one flat folder and a global ADR sequence because decisions can affect multiple repository areas and their categories may be unclear when a proposal begins. A global sequence is easier to reference consistently across skills, tasks, workflows, and reports.
- Preserve the boundary between analysis, Drafts, ADRs, tasks, and CI diagnostics: analysis describes evidence at a fixed commit; Drafts propose changes; ADRs record accepted decisions; tasks implement them; the CI Ledger remains the source of truth for operational findings.

These points preserve material rationale from the approved DRAFT-0001 without changing ADR-0001's accepted outcome.

## Decision Drivers

- One accepted decision must have one authoritative permanent record.
- A Draft is temporary and exists to develop and review a proposal.
- An ADR must preserve all material decision rationale before its source Draft is deleted.
- A failed or partial promotion must not cause data loss or create duplicate ADRs.
- Source Draft deletion must be verifiable and recoverable.
- The user remains the final decision-maker.
- The repository must not retain broken links to deleted source Drafts.
- Rejected, withdrawn, and superseded Draft retention remains outside this decision.

## Considered Options

### Option 1 — Preserve every promoted Draft

Keep the current rule. Mark the Draft `promoted` and link the resulting ADR.

- **Good:** The original proposal remains available.
- **Neutral:** Both the proposal and decision record remain in the repository.
- **Bad:** Completed proposals remain in the active Draft collection.
- **Bad:** Readers may be uncertain which record is authoritative.

### Option 2 — Delete the Draft immediately after ADR creation

Create the ADR and delete the Draft without a content comparison.

- **Good:** The Draft collection contains only unfinished proposals.
- **Neutral:** The workflow is short.
- **Bad:** The ADR may omit important rationale.
- **Bad:** A partial or incorrect write could destroy the only complete explanation.

### Option 3 — Verify the ADR, then delete the source Draft

Create a provisional ADR, compare it with the approved Draft, accept it only after the completeness check passes, then delete the source Draft.

- **Good:** The ADR becomes the only permanent decision record.
- **Good:** The rationale check prevents premature deletion.
- **Good:** Partial promotion can be recovered without creating a duplicate ADR.
- **Neutral:** Promotion requires a documented content comparison.
- **Bad:** Promotion takes more work than a direct file conversion.

## Decision Outcome

Chosen option: **Option 3 — Verify the ADR, then delete the source Draft.**

A Draft is a temporary proposal. An accepted ADR is the permanent decision record. A successful promotion deletes the source Draft after the ADR passes the required completeness and read-back checks. Do not create an `archive/draft/` folder or a Promoted Drafts index.

This decision does not change the user approval gate, task execution approval, ADR Confirmation, or permanent ADR archival rules. It does not authorize implementation outside the approved scope.

### Draft lifecycle

Draft statuses are:

- `draft` — preparation is in progress.
- `in-review` — the exact revision is ready for the user.
- `changes-requested` — the user requested revisions.
- `approved-for-adr` — the user approved the exact revision and scope.
- `rejected` — the user rejected the proposal.
- `withdrawn` — the proposal was withdrawn.
- `superseded` — another Draft replaced it before approval.

Remove `promoted` as a steady-state status. A successful promotion deletes the source Draft. Keep rejected, withdrawn, and superseded records under their existing retention rules; this ADR does not establish a new deletion policy for them.

### Tightened Draft-to-ADR promotion workflow

Promote a Draft only after the user approves its exact revision and scope.

1. **Verify approval.** Re-fetch the complete Draft from branch `gpt`. Confirm its ID, revision, approval, and scope. Stop if the approved revision does not match the current file.
2. **Prepare the ADR.** Map the Draft's decision-bearing content into the ADR. Preserve its meaning and reasoning; do not copy text mechanically.
3. **Complete the rationale cross-check.** Compare the prepared ADR with the source Draft using the completeness checklist below. Resolve every material omission before the ADR becomes accepted.
4. **Create a provisional ADR.** Assign the next unused global ADR ID and create the record with status `promotion-pending`. Record the source Draft ID as provenance, approver, approval date, related ADRs, implementation state, and approved scope. This state reserves the ID but is not an accepted decision and cannot govern an implementation task.
5. **Read back and verify.** Fetch the provisional ADR from branch `gpt`. Check its complete content, required sections, metadata, internal links, and rationale cross-check. Correct material omissions and repeat the full check. Do not accept the ADR or delete the Draft while a required check fails.
6. **Accept the ADR.** Change its status from `promotion-pending` to `accepted` only after the completeness check passes. Read back the accepted record and confirm that its decision content matches the validated version. Do not change its decision content after acceptance.
7. **Delete the source Draft.** Delete the exact source file only after the accepted ADR passes the completeness gate. Do not move it to another folder or retain a full copy.
8. **Update indexes.** Remove the source Draft from `workspace/draft/README.md`. Ensure the ADR index points to the accepted ADR. Do not leave a Promoted Drafts entry.
9. **Verify closeout.** Read back both indexes. Confirm that the ADR exists, the source Draft does not exist, and no active index points to the deleted file. Check repository references for stale Markdown links.
10. **Record the result.** Record the source Draft ID, resulting ADR ID, completeness result, deletion result, and commit references in the promotion task or other active decision record.

Never reuse a Draft ID or ADR ID after deletion or promotion. Keep the source Draft ID in the ADR's `source_draft` field as provenance. Do not link that field to a source file that the workflow deletes.

### ADR completeness checklist

Before deleting a source Draft, confirm that the ADR preserves every material item a future reader needs to understand the accepted decision:

- The problem, relevant repository state, and decision scope.
- The user's goals, non-goals, constraints, and decision drivers.
- The viable options considered.
- The material reasons for rejecting alternatives.
- The chosen outcome and why it best meets the decision drivers.
- The accepted consequences, trade-offs, risks, and safeguards.
- The implementation boundary, dependencies, migration, and rollback approach.
- Observable Confirmation criteria.
- Material assumptions, evidence, and source references.
- User approval details, including the approved Draft ID and revision.

The ADR need not repeat incidental wording, drafting notes, duplicate explanations, or details that do not affect the decision. It must preserve decision rationale, not every sentence in the proposal.

The reviewer must make a direct comparison. The existence of an ADR, a matching title, or a source Draft ID is not enough.

If the ADR omits important rationale:

- Do not delete the source Draft or mark promotion complete.
- Add the missing rationale before the ADR is accepted.
- Re-run the complete comparison and read back the corrected ADR.
- If the information cannot be preserved without changing an already accepted or archived decision, keep the Draft and present a separate proposal for the required migration. Do not edit an archived ADR unless the user explicitly authorizes a narrow correction.

### Partial promotion and recovery

GitHub file operations may commit the ADR, index update, and Draft deletion separately. The workflow must support partial states.

- If the provisional ADR does not exist, continue from the approved Draft. Do not assign a second ID if an ADR ID has already been reserved in a recorded promotion attempt.
- If an ADR exists with status `promotion-pending`, resume its completeness checks. Correct material omissions before acceptance. Do not create another ADR.
- A `promotion-pending` ADR is not accepted, must not appear in the accepted-decision list, and must not govern an implementation task.
- If the ADR is accepted and verified but source Draft deletion fails, keep the Draft. Add it to a **Promotion Cleanup Pending** section in the Draft index, record the resulting ADR ID in its metadata, and retry only the cleanup step.
- Do not list a cleanup-pending Draft as a proposal awaiting a decision.
- After deletion succeeds, remove the cleanup-pending entry and verify the final state.

A cleanup-pending entry is a temporary recovery aid, not a historical Draft archive.

### Index and cross-reference rules

- **Current Drafts** contains only proposals that still require preparation, review, or approval.
- Do not add a **Promoted Drafts** section.
- Use **Promotion Cleanup Pending** only when a verified accepted ADR exists but source Draft deletion has not completed.
- The ADR index contains accepted ADRs awaiting implementation or confirmation. Do not list `promotion-pending` records as accepted.
- The ADR's `source_draft` field keeps the Draft ID as provenance. It does not link to a deleted source file.
- Before deletion, search repository references to the source Draft path. Do not create new links to a source Draft that promotion will delete.
- An archived ADR that contains a legacy source-Draft link requires a separate, explicit user authorization before a narrowly scoped reference-only correction.

### Migration of existing promoted Drafts

Review each existing promoted Draft individually.

For DRAFT-0001:

1. Compare the complete source Draft with archived ADR-0001.
2. Record a coverage result for each completeness checklist item.
3. Identify material rationale present only in DRAFT-0001.
4. Do not delete DRAFT-0001 while a material gap remains.
5. Do not rewrite ADR-0001's decision outcome or rationale. ADR-0001 is archived and permanent. A narrow reference-only correction requires explicit user authorization. Any missing material rationale must be preserved in a valid permanent decision record.
6. Delete DRAFT-0001 only after all material rationale is preserved in a permanent decision record and the legacy reference issue has an approved resolution.

Do not migrate or delete other Drafts unless they are confirmed as promoted and their corresponding ADRs pass the same completeness gate.

## Consequences

- **Good:** The accepted ADR is the only permanent record of an approved decision.
- **Good:** Completed Drafts no longer clutter the active proposal collection.
- **Good:** The completeness check protects decision rationale.
- **Good:** Partial promotion can be resumed without creating duplicate ADRs.
- **Neutral:** Draft IDs remain as provenance in ADR metadata.
- **Neutral:** Rejected, withdrawn, and superseded Drafts retain their existing behavior.
- **Bad:** Promotion requires a content comparison and read-back.
- **Bad:** Existing promoted Drafts require individual migration review.
- **Bad:** A source Draft may remain temporarily when its ADR does not preserve enough information.

## Risks and Safeguards

| Risk | Likelihood / Impact | Safeguard | Residual risk |
|---|---|---|---|
| ADR omits material rationale | Medium / High | Direct section-by-section comparison before deletion. | Reviewer may miss an implicit constraint. |
| Draft is deleted before ADR verification | Low / High | Require read-back and completeness checks before deletion. | An incorrect check may still pass. |
| Partial writes leave duplicate records | Medium / Medium | Use Promotion Cleanup Pending and resume from the existing ADR. | Cleanup may remain open until a later write succeeds. |
| Archived ADR links to a deleted Draft | Medium / Medium | Search references before deletion; require explicit approval for archived-record correction. | Legacy references may remain until migration. |
| IDs are reused | Low / High | Keep global sequences monotonic. | Index errors may hide an existing ID. |
| Rejected or withdrawn history is deleted | Low / Medium | Limit this decision to successful ADR promotion. | A separate retention decision may be needed. |

## Implementation Scope

- **In scope:** Update the decision-governance skill, Draft and ADR indexes, workspace navigation, Draft and ADR templates, archive guidance, Document Type Catalog, and discussion register. Add the provisional `promotion-pending` state. Migrate DRAFT-0001 only after its rationale and legacy link checks pass.
- **Out of scope:** Delete rejected, withdrawn, or superseded Drafts; create `archive/draft/`; introduce hooks or automatic approval; change foundational initialization; rewrite ADR-0001's accepted decision; or implement unrelated proposals.
- **Tasks:** A separate implementation task must link ADR-0002. Task execution approval remains separate from this decision approval.
- **Dependencies:** ADR-0001 remains authoritative except for its source-Draft preservation rule, which this ADR supersedes.
- **Migration / rollback:** Keep a source Draft until its ADR passes the completeness gate. If any check fails, stop and preserve the Draft. Do not roll back by deleting an accepted ADR; use a superseding ADR for later decision changes.

## More Information

- **Source Draft:** DRAFT-0003, revision 2, approved by the user on 2026-11-24. The source file is retired after successful promotion; its ID remains provenance. Original approved revision commit: `18fd31c84dc42d24619e3cb988d07656fda5a993`.
- **Related ADR:** ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis. This ADR supersedes only the requirement to preserve a source Draft after promotion.
- **Historical source:** DRAFT-0001, revision 1, approved 2026-11-24. Its material rationale not fully restated in ADR-0001 is retained in this ADR's Historical context section. The source file is eligible for deletion only after the authorized link correction and completeness check.
- **Evidence:** DRAFT-0003 revision 2; DRAFT-0001 revision 1; ADR-0001; workspace Draft and ADR indexes; decision-governance skill; Document Type Catalog.
- **Review trigger:** A failed completeness check, failed source deletion, material migration gap, or user change to the lifecycle.

## Confirmation

- [ ] The decision-governance skill defines the complete promotion sequence, completeness checklist, and partial-promotion recovery.
- [ ] Draft statuses no longer include `promoted` as a steady-state state.
- [ ] The ADR template and index define `promotion-pending` as temporary and non-authoritative.
- [ ] The Draft index has no Promoted Drafts section and lists only active proposals plus any cleanup-pending transaction.
- [ ] No accepted ADR links to a source Draft file scheduled for deletion.
- [ ] DRAFT-0001's material rationale is preserved in permanent ADR records.
- [ ] The authorized ADR-0001 reference correction is complete and read back.
- [ ] DRAFT-0001 is deleted only after its completeness and cross-reference checks pass.
- [ ] Every changed path is read back and relevant hosted Document Standards validation passes.

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| 2026-11-24 | Accepted | User approved DRAFT-0003 revision 2. The provisional ADR was read back and checked against the complete approved Draft. The record preserves the approved lifecycle, promotion, completeness, recovery, and migration rules. |
