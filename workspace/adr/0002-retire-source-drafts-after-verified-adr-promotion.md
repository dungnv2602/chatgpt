---
record_type: decision-record
template_version: "1.1"
id: "ADR-0002"
status: "accepted"
decision_date: "2026-11-24"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0003"
source_draft_revision: 2
approved_scope: "Option 3, including the rationale completeness gate, Promotion Cleanup Pending recovery, and the DRAFT-0001 migration safeguard in DRAFT-0003 revision 2."
related_adrs:
  - "ADR-0001"
supersedes: []
superseded_by: null
implementation_status: "complete"
implementation_tasks:
  - "20261124-160500"
review_triggers:
  - "A promotion completeness check fails."
  - "A source Draft cannot be deleted after ADR acceptance."
  - "The migration reveals a material decision-rationale gap."
  - "The user changes the Draft or ADR lifecycle."
---

# Retire Source Drafts After Verified ADR Promotion

## Context and Problem Statement

The current Draft-to-ADR workflow preserves a source Draft after promotion. It marks the Draft `promoted`, links it to the accepted ADR, and keeps it in `workspace/draft/`.

This leaves two records for one accepted decision. The ADR is authoritative, but the promoted Draft remains visible in the proposal collection. It can create uncertainty about which record governs the decision and leaves completed proposals in an active workspace.

Deleting a Draft immediately after writing an ADR creates a data-loss risk. The ADR may omit material rationale, constraints, rejected alternatives, trade-offs, safeguards, or approval scope from the Draft. The source Draft must remain until the Worker reads the resulting ADR and compares it with the complete approved proposal.

DRAFT-0003 revision 2 proposed a transaction-like promotion process. The user approved that exact revision and its scope on 2026-11-24. This ADR records the accepted decision. It supersedes only the source-Draft preservation rule established by ADR-0001. ADR-0001 remains the authoritative record for its other decisions.

### Historical context retained from DRAFT-0001

The source Draft included decision rationale that ADR-0001 summarized rather than fully restated:

- Keep `workspace/analysis/` inside `workspace/` because workspace is the repository's planning and coordination area. A root-level `analysis/` directory would create another peer domain without a clear owner. Keep automated CI diagnostics under `reports/`. The analysis area synthesizes repository state. It does not duplicate the CI Ledger.
- Use one flat folder and a global ADR sequence. Decisions can affect multiple repository areas. Their categories may be unclear when a proposal begins. This sequence is easier to reference across skills, tasks, workflows, and reports.
- Preserve the boundary between analysis, Drafts, ADRs, tasks, and CI diagnostics. Analysis records evidence at a specific commit. Drafts propose changes. ADRs record accepted decisions. Tasks implement those decisions. The CI Ledger remains the source of truth for operational findings.

These points preserve material rationale from the approved DRAFT-0001 without changing ADR-0001's accepted outcome.

## Decision Drivers

- One accepted decision must have one authoritative permanent record.
- A Draft is temporary and exists to develop and review a proposal.
- An ADR must preserve all material decision rationale before the Worker deletes its source Draft.
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

### Option 3 — Check the ADR, then delete the source Draft

Create a provisional ADR. Compare it with the approved Draft. Accept the ADR only after the completeness check passes. Then delete the source Draft.

- **Good:** The ADR becomes the only permanent decision record.
- **Good:** The rationale check prevents premature deletion.
- **Good:** Partial promotion can be recovered without creating a duplicate ADR.
- **Neutral:** Promotion requires a documented content comparison.
- **Bad:** Promotion takes more work than a direct file conversion.

## Decision Outcome

Chosen option: **Option 3 — Check the ADR, then delete the source Draft.**

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

Do not use `promoted` as a steady-state status. A successful promotion deletes the source Draft. Keep rejected, withdrawn, and superseded records under their existing retention rules. This ADR does not establish a new deletion policy for those records.

### Tightened Draft-to-ADR promotion workflow

Promote a Draft only after the user approves its exact revision and scope.

1. **Check approval.** Re-fetch the complete Draft from branch `gpt`. Check its ID, revision, approval, and scope. Stop if the approved revision does not match the current file.
2. **Prepare the ADR.** Map the Draft's decision-bearing content into the ADR. Preserve its meaning and reasoning. Do not copy text mechanically.
3. **Check rationale completeness.** Compare the prepared ADR with the source Draft using the completeness checklist below. Resolve every material omission before the Worker accepts the ADR.
4. **Create a provisional ADR.** Assign the next unused global ADR ID and create the record with status `promotion-pending`. Record the source Draft ID as provenance, approver, approval date, related ADRs, implementation state, and approved scope. This state reserves the ID but is not an accepted decision and cannot govern an implementation task.
5. **Read back and check.** Fetch the provisional ADR from branch `gpt`. Check its complete content, required sections, metadata, internal links, and rationale. Correct material omissions and repeat the full check. Do not accept the ADR or delete the Draft while a required check fails.
6. **Accept the ADR.** The Worker changes its status from `promotion-pending` to `accepted` only after the completeness check passes. Read back the accepted record. Check that its decision content matches the checked version. Do not change its decision content after acceptance.
7. **Delete the source Draft.** Delete the exact source file only after the accepted ADR passes the completeness gate. Do not move it to another folder or retain a full copy.
8. **Update indexes.** Delete the source Draft entry from `workspace/draft/README.md`. Ensure the ADR index points to the accepted ADR. Do not leave a Promoted Drafts entry.
9. **Check closeout.** Read back both indexes. Check that the ADR exists, the source Draft does not exist, and no active index points to the deleted file. Search repository references for stale Markdown links.
10. **Record the result.** Record the source Draft ID and resulting ADR ID. Include the completeness result, deletion result, and commit references in the promotion task or another active decision record.

Never reuse a Draft ID or ADR ID after deletion or promotion. Keep the source Draft ID in the ADR's `source_draft` field as provenance. Do not link that field to a source file that the workflow deletes.

### ADR completeness checklist

Before deleting a source Draft, check that the ADR preserves every material item a future reader needs to understand the accepted decision:

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
- Add the missing rationale before the Worker accepts the ADR.
- Re-run the complete comparison and read back the corrected ADR.
- If the information cannot be preserved without changing an accepted or archived decision, keep the Draft. Present a separate proposal for the required migration. Do not edit an archived ADR unless the user explicitly authorizes a narrow correction.

### Partial promotion and recovery

GitHub file operations may commit the ADR, index update, and Draft deletion separately. The workflow must support partial states.

- If the provisional ADR does not exist, continue from the approved Draft. Do not assign a second ID if a recorded promotion attempt already reserved an ADR ID.
- If an ADR exists with status `promotion-pending`, resume its completeness checks. Correct material omissions before the Worker accepts it. Do not create another ADR.
- A `promotion-pending` ADR is provisional. Do not list it as accepted or use it to govern an implementation task.
- If the Worker accepts and checks the ADR but source Draft deletion fails, keep the Draft. Add the Draft to a **Promotion Cleanup Pending** section in the Draft index. Record the resulting ADR ID in its metadata. Retry only the cleanup step.
- Do not list a cleanup-pending Draft as a proposal awaiting a decision.
- After the Worker deletes the source Draft, delete the cleanup-pending entry and check the final state.

A cleanup-pending entry is a temporary recovery aid, not a historical Draft archive.

### Index and cross-reference rules

- **Current Drafts** contains only proposals that still require preparation, review, or approval.
- Do not add a **Promoted Drafts** section.
- Use **Promotion Cleanup Pending** only after the Worker checks and accepts an ADR but cannot delete its source Draft.
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
5. Do not rewrite ADR-0001's decision outcome or rationale. ADR-0001 remains in the permanent archive. The user must explicitly authorize a narrow reference-only correction. Preserve any missing material rationale in a valid permanent decision record.
6. Delete DRAFT-0001 only after a permanent decision record preserves all material rationale and the approved resolution addresses the legacy reference issue.

Do not migrate or delete other Drafts unless the Worker checks that the repository promoted them. Their corresponding ADRs must also pass the same completeness gate.

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
| The Worker deletes the Draft before checking the ADR | Low / High | Require read-back and completeness checks before deletion. | An incorrect check may still pass. |
| Partial writes leave duplicate records | Medium / Medium | Use Promotion Cleanup Pending and resume from the existing ADR. | Cleanup may remain open until a later write succeeds. |
| An archived ADR links to a deleted Draft | Medium / Medium | Search references before deletion. Require explicit approval for any correction to an archived record. | Legacy references may remain until migration. |
| A process reuses an ID | Low / High | Keep global sequences monotonic. | Index errors may hide an existing ID. |
| A process deletes rejected or withdrawn history | Low / Medium | Limit this decision to successful ADR promotion. | A separate retention decision may be needed. |

## Implementation Scope

- **In scope:** Update the decision-governance skill, Draft and ADR indexes, and workspace navigation. Update the Draft and ADR templates, archive guidance, Document Type Catalog, and discussion register. Add the provisional `promotion-pending` state. Migrate DRAFT-0001 only after its rationale and legacy link checks pass.
- **Out of scope:** This decision does not authorize deletion of rejected, withdrawn, or superseded Drafts. It does not authorize an `archive/draft/` folder. It does not authorize hooks or automatic approval. It does not change foundational initialization or ADR-0001's accepted decision. It does not authorize unrelated proposals.
- **Tasks:** A separate implementation task must link ADR-0002. Task execution approval remains separate from this decision approval.
- **Dependencies:** ADR-0001 remains authoritative except for its source-Draft preservation rule, which this ADR supersedes.
- **Migration / rollback:** Keep a source Draft until its ADR passes the completeness gate. If any check fails, stop and preserve the Draft. Do not roll back by deleting an accepted ADR. Use a superseding ADR for later decision changes.

## More Information

- **Source Draft:** DRAFT-0003, revision 2, approved by the user on 2026-11-24. The promotion workflow retires the source file after success. The Draft ID remains as provenance. Original approved revision commit: `18fd31c84dc42d24619e3cb988d07656fda5a993`.
- **Related ADR:** ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis. This ADR supersedes only the requirement to preserve a source Draft after promotion.
- **Historical source:** DRAFT-0001, revision 1, approved 2026-11-24. ADR-0001 does not fully restate its material rationale. This ADR preserves that rationale in the Historical context section. The Worker may delete the source file only after the authorized link correction and completeness check.
- **Evidence:** DRAFT-0003 revision 2, DRAFT-0001 revision 1, ADR-0001, the workspace Draft and ADR indexes, the decision-governance skill, and the Document Type Catalog.
- **Review trigger:** A failed completeness check, failed source deletion, material migration gap, or user change to the lifecycle.
- **Lint validation:** Hosted STE Lint run [#675](https://github.com/dungnv2602/chatgpt/actions/runs/45456236271) evaluated this ADR directly and recorded zero findings. The report records zero hard findings, zero advisory findings, and zero failed checks.
- **Lint remediation tasks:** [20261124-161334-01](https://github.com/dungnv2602/chatgpt/blob/gpt/workspace/archive/task/20261124-161334-01-review-present-perfect-findings-in-workspace-adr-0002-retire-sou.md), [20261124-161334-02](https://github.com/dungnv2602/chatgpt/blob/gpt/workspace/archive/task/20261124-161334-02-review-passive-voice-findings-in-workspace-adr-0002-retire-sourc.md), [20261124-161334-03](https://github.com/dungnv2602/chatgpt/blob/gpt/workspace/archive/task/20261124-161334-03-review-semicolon-findings-in-workspace-adr-0002-retire-source-dr.md), [20261124-161334-04](https://github.com/dungnv2602/chatgpt/blob/gpt/workspace/archive/task/20261124-161334-04-review-long-sentence-findings-in-workspace-adr-0002-retire-sourc.md), and [20261124-161334-05](https://github.com/dungnv2602/chatgpt/blob/gpt/workspace/archive/task/20261124-161334-05-review-synonym-rotation-findings-in-workspace-adr-0002-retire-so.md).

## Confirmation

- [x] The decision-governance skill defines the complete promotion sequence, completeness checklist, and partial-promotion recovery.
- [x] Draft statuses no longer include `promoted` as a steady-state state.
- [x] The ADR template and index define `promotion-pending` as temporary and non-authoritative.
- [x] The Draft index has no Promoted Drafts section and lists only active proposals plus any cleanup-pending transaction.
- [x] No accepted ADR links to a source Draft file scheduled for deletion.
- [x] Permanent ADR records preserve DRAFT-0001's material rationale.
- [x] The authorized ADR-0001 reference correction is complete and read back.
- [x] The repository deletes DRAFT-0001 only after the completeness and cross-reference checks pass.
- [x] The Worker read back every changed path. The hosted Document Standards workflow passed.
- [x] ADR-0002 passes hosted STE lint with zero findings.

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| 2026-11-24 | Accepted | User approved DRAFT-0003 revision 2. The Worker read back the provisional ADR and compared it with the complete approved Draft. The record preserves the approved lifecycle, promotion, completeness, recovery, and migration rules. |
| 2026-11-24 | Implementation in progress | User approved task 20261124-160500 on 2026-11-24. The task remains In Progress. ADR-0002 lists it in implementation_tasks. DRAFT-0001 passed its rationale completeness review. |
| 2026-11-24 | DRAFT-0001 source retired | The complete rationale comparison passed. The Worker deleted the cleanup-pending index entry and corrected ADR-0001's working-path link under explicit user permission. The Worker then deleted DRAFT-0001 in commit 4082efd9a5dadb8b8bd0b41ccd3cf69b5e9405ce. |
| 2026-11-25 | Lint-only editorial remediation authorized | The user authorized wording corrections to ADR-0002 so it can be retired. The authorization covers lint-only edits. It does not change the accepted decision, rationale, options, scope, or safeguards. The five linked remediation tasks record the approved work. |
| 2026-11-24 | ADR-0002 editorial lint corrections committed | The Worker updated wording for the five lint rule groups. The full ADR read-back passed. Manual review found zero semicolons and no sentences over 25 words. Hosted STE lint remains pending. Commit: `3d2f2cec2b901aaae72976bfd9093859299b468f`. |
| 2026-11-24 | Implementation checks passed | Document Standards run 45445313265 passed. It ran 37 CI Ledger tests and 32 catalog-validator tests. Catalog checks passed for 18 document types and 28 exact references. STE Lint run 45445313404 passed with zero findings in the one changed file. Diagnostics run 45445313378 passed. The STE Lint run used incremental scope. It did not evaluate ADR-0002. Earlier findings in ADR-0002's accepted decision content remained unchanged under the approved immutability boundary. |
| 2026-11-24 | Implementation and lint remediation complete | Task 20261124-160500 is Done and archived. The five lint remediation tasks are Done and archived. Hosted STE Lint run 45456236271 evaluated ADR-0002 and found zero findings. Document Standards run 45456236127 and Diagnostics run 45456236357 passed. |
