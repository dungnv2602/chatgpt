---
record_type: decision-draft
template_version: "1.0"
id: "DRAFT-0003"
revision: 1
status: "in-review"
created: "2026-11-24"
updated: "2026-11-24"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs:
  - "ADR-0001"
---

# Retire Source Drafts After Verified ADR Promotion

## Proposal Summary

Change the Draft-to-ADR lifecycle so that a Draft is a temporary proposal, while an accepted ADR is the permanent decision record. After the user approves a Draft, create and validate the ADR. Delete the source Draft only after a documented completeness check confirms that the ADR preserves all material decision rationale.

Do not keep promoted Drafts in the Draft folder or create an archive for them. Keep the source Draft when the completeness check fails. Do not delete it to make the workflow appear complete.

This proposal supersedes the source-Draft preservation rule in ADR-0001. It does not change the user approval gate, ADR immutability, implementation-task approval, ADR confirmation, or permanent ADR archival rules except where this proposal states a narrow migration requirement.

## Context and Problem Statement

The current workflow preserves a Draft after promotion. It changes the Draft status to `promoted`, adds a link to the resulting ADR, and keeps the file in `workspace/draft/`.

This creates two records for one accepted decision:

- The ADR is the permanent and authoritative decision record.
- The promoted Draft is a proposal that has already completed its purpose.

The duplicate can create uncertainty about which record governs the decision. It also keeps completed proposals in the active Draft collection. The user has clarified that a Draft is no longer needed after it becomes an ADR. The accepted ADR should replace it.

A direct deletion rule would create another risk. An ADR may not preserve every important reason, constraint, rejected alternative, trade-off, or safeguard from its source Draft. Deleting the Draft before checking the ADR could remove the only record that explains the decision.

The existing records show why this safeguard matters. ADR-0001 is archived and permanent. DRAFT-0001 contains a longer proposal than ADR-0001. The repository must compare them before it deletes DRAFT-0001. It must not assume that the existence of an ADR proves that the conversion preserved all material rationale.

The current policy also requires the source Draft to remain. A new accepted ADR must supersede that rule before the repository changes the lifecycle.

## Goals and Non-Goals

### Goals

- Make the accepted ADR the only permanent record of an approved decision.
- Delete a source Draft after successful and verified promotion.
- Preserve every material reason needed to understand the accepted decision.
- Prevent deletion when the ADR omits important decision rationale.
- Remove promoted Drafts from the active Draft index.
- Make promotion recoverable if the ADR is created but source-file deletion fails.
- Avoid dead links to deleted source Drafts.
- Preserve rejected, withdrawn, and superseded Drafts under their existing rules.

### Non-Goals

- Delete rejected, withdrawn, or superseded Drafts under this proposal.
- Create an `archive/draft/` folder, a tombstone file, or a separate proposal-history archive.
- Rewrite the decision outcome or rationale of ADR-0001.
- Change the user approval requirement for Drafts.
- Make ADR approval sufficient to authorize implementation tasks.
- Change ADR confirmation or permanent ADR archival.
- Introduce scripts, hooks, or automatic promotion.

## Decision Drivers

- One accepted decision should have one authoritative permanent record.
- Drafts should not remain in the active proposal collection after promotion.
- The repository must preserve decision rationale and provenance.
- A failed or partial promotion must not cause data loss.
- The process must remain recoverable through repository files.
- Archived ADRs must remain immutable.
- The user remains the final decision-maker.

## Considered Options

### Option 1 — Preserve every promoted Draft

- **Description:** Keep the current rule. Change the Draft status to `promoted` and link the ADR.
- **Good:** The original proposal remains available without further work.
- **Neutral:** The repository retains both the proposal and the decision record.
- **Bad:** The Draft remains after it has completed its purpose.
- **Bad:** The Draft index includes documents that no longer need user review.
- **Bad:** Readers may not know whether the Draft or ADR is authoritative.

### Option 2 — Delete the Draft as soon as the ADR is created

- **Description:** Create the ADR, then immediately delete the source Draft.
- **Good:** The Draft collection contains only unfinished proposals.
- **Neutral:** The process is short.
- **Bad:** The ADR may omit important rationale from the Draft.
- **Bad:** A failed or incomplete write could remove the only complete decision explanation.
- **Bad:** The process has no explicit recovery check.

### Option 3 — Verify the ADR, then delete the source Draft

- **Description:** Create a complete ADR, verify its contents against the approved Draft, accept the ADR, and delete the Draft only after the completeness gate passes.
- **Good:** The ADR becomes the sole permanent decision record.
- **Good:** The process protects important rationale before deletion.
- **Good:** A partial promotion can be recovered without creating a second ADR.
- **Neutral:** Promotion requires a documented content comparison.
- **Bad:** The process adds a validation step before deletion.

## Proposed Recommendation

Choose **Option 3 — Verify the ADR, then delete the source Draft**.

### 1. Draft lifecycle

Keep these Draft statuses:

- `draft` — preparation is in progress.
- `in-review` — the exact revision is ready for the user.
- `changes-requested` — the user requested revisions.
- `approved-for-adr` — the user approved the exact revision and scope.
- `rejected` — the user rejected the proposal.
- `withdrawn` — the proposal was withdrawn.
- `superseded` — another Draft replaced the proposal before approval.

Remove `promoted` as a steady-state status. A successful promotion deletes the source Draft. Do not keep a Promoted Drafts section in the index.

Keep rejected, withdrawn, and superseded records under the existing retention rules. This proposal does not establish a new deletion policy for them.

### 2. Tightened Draft-to-ADR promotion workflow

Promote a Draft only after the user approves its exact revision and scope.

1. **Verify approval.** Re-fetch the complete Draft from branch `gpt`. Confirm its ID, revision, approval, and scope. Stop if the approved revision does not match the current file.
2. **Prepare the ADR.** Map the Draft's decision-bearing content into the ADR. Do not copy text mechanically. Preserve the meaning and the reasoning.
3. **Complete the rationale cross-check.** Compare the prepared ADR against the source Draft by using the completeness checklist below. Resolve every material omission before the ADR becomes accepted.
4. **Create the ADR.** Assign the next unused global ADR ID. Record the source Draft ID as provenance, the approver, approval date, related ADRs, implementation state, and approved scope.
5. **Read back and verify.** Fetch the written ADR from branch `gpt`. Check its complete content, required sections, metadata, internal links, and the rationale cross-check. Do not delete the Draft if any required check fails.
6. **Accept the ADR.** Set the ADR status to `accepted` only after the content check passes. Read back the accepted record and confirm that its decision content matches the validated version.
7. **Delete the source Draft.** Delete the exact source file only after the accepted ADR has passed the completeness gate. Do not move it to another folder and do not retain a full copy.
8. **Update indexes.** Remove the source Draft from `workspace/draft/README.md`. Ensure the ADR index points to the accepted ADR. Do not leave a Promoted Drafts entry.
9. **Verify closeout.** Read back both indexes. Confirm that the ADR exists, the source Draft does not exist, and no active index points to the deleted file. Check repository references for stale Markdown links.
10. **Record the result.** Record the source Draft ID, resulting ADR ID, completeness result, deletion result, and commit references in the promotion task or other active decision record.

Do not reuse a Draft ID or ADR ID after deletion or promotion. Keep the source Draft ID in the ADR's `source_draft` field as a provenance identifier. Do not link that field to a file that the workflow deletes.

### 3. ADR completeness checklist

Before deleting a source Draft, confirm that the ADR preserves every material item that a future reader needs to understand the accepted decision:

- The problem, relevant repository state, and decision scope.
- The user's goals, non-goals, constraints, and decision drivers.
- The viable options that were considered.
- The material reasons for rejecting the alternatives.
- The chosen outcome and why it best meets the decision drivers.
- The accepted consequences, trade-offs, risks, and safeguards.
- The implementation boundary, dependencies, migration, and rollback approach.
- Observable Confirmation criteria.
- Material assumptions, evidence, and source references.
- User approval details, including the approved Draft ID and revision.

The ADR does not need to repeat incidental wording, drafting notes, duplicate explanations, or details that do not affect the decision. It must preserve the decision rationale, not every sentence in the proposal.

The reviewer must make a direct comparison. The existence of an ADR, a matching title, or a source Draft ID is not enough to pass.

If the ADR omits important rationale:

- Do not delete the source Draft.
- Do not mark the promotion complete.
- Add the missing rationale to the ADR before it is accepted.
- Re-run the complete comparison and read back the corrected ADR.
- If the information cannot be preserved without changing an already accepted or archived decision, keep the Draft and present a separate proposal for the required migration. Do not edit an archived ADR under this proposal.

### 4. Partial promotion and recovery

GitHub file operations may commit the ADR, index update, and Draft deletion separately. The process must therefore support a partial state.

- If the ADR does not exist, continue from the approved Draft. Do not assign a second ID if an ADR ID has already been reserved in a recorded promotion attempt.
- If an ADR exists but is not yet accepted, resume its completeness checks. Do not create another ADR.
- If the ADR is accepted and verified but the Draft deletion fails, keep the Draft. Add it to a clearly named **Promotion Cleanup Pending** section in the Draft index, record the resulting ADR ID in the Draft metadata, and retry only the cleanup step.
- Do not list a cleanup-pending Draft as a proposal awaiting a decision.
- After deletion succeeds, remove the cleanup-pending entry and verify the final state.

A cleanup-pending entry is a temporary recovery aid. It is not a historical Draft archive.

### 5. Index and cross-reference rules

- The **Current Drafts** section contains only proposals that still require preparation, review, or approval.
- Do not add a **Promoted Drafts** section.
- Use **Promotion Cleanup Pending** only when a verified accepted ADR exists but deletion of its source Draft has not completed.
- The ADR index contains accepted ADRs awaiting implementation or confirmation.
- The ADR's `source_draft` field keeps the Draft ID as provenance. It does not link to the deleted source file.
- Before deletion, search repository references to the source Draft path. Do not create new links to a source Draft that promotion will delete.
- Do not edit an archived ADR as part of ordinary promotion. A legacy archived ADR that already contains a source-Draft link requires a separately authorized, narrowly scoped migration decision before any reference-only correction.

### 6. Migration of existing promoted Drafts

After this policy is accepted, review each existing promoted Draft individually.

For DRAFT-0001:

1. Compare the complete source Draft with archived ADR-0001.
2. Record a coverage result for each completeness checklist item.
3. Identify any material rationale present only in DRAFT-0001.
4. Do not delete DRAFT-0001 while a material gap remains.
5. Because ADR-0001 is archived and immutable, do not edit it to fill gaps. If material rationale is missing, prepare a separate proposal for a permitted supplemental or superseding decision record.
6. Delete DRAFT-0001 only after the required information is preserved in a valid permanent decision record and the reference issue has an approved resolution.

Do not migrate or delete other Drafts unless they are confirmed as promoted and their corresponding ADRs pass the same completeness gate.

### 7. Repository changes required after approval

Update the following records and instructions:

| Path | Required change |
|---|---|
| `skills/decision-governance/SKILL.md` | Replace the preserve-after-promotion rule with the verified promotion, deletion, recovery, and migration procedure. |
| `workspace/draft/README.md` | Remove `promoted` from steady-state statuses; remove promoted records from Current Drafts; define Promotion Cleanup Pending. |
| `workspace/README.md` | Describe Draft deletion after verified ADR promotion. |
| `workspace/DRAFT_TEMPLATE.md` | Remove the steady-state `promoted` status and clarify source-file retirement. |
| `workspace/ADR_TEMPLATE.md` | Record the source Draft ID as provenance without a link to a file that will be deleted. |
| `workspace/adr/README.md` | Clarify that accepted ADRs replace source Drafts and that the source ID remains as provenance. |
| `archive/README.md` | State that ADR archives remain permanent while source Draft files are retired after promotion. |
| `archive/adr/README.md` | Keep ADR immutability and permanent retention rules; do not add source Draft archives. |
| `workspace/discussion.md` | Keep only Drafts that still need a decision in Open Discussions. |
| `skills/document-standards/references/document-type-catalog.md` | Confirm that the Draft path and status rules match the new lifecycle. |

Do not change the session-start sequence or make decision governance a foundational skill.

### 8. Validation and migration acceptance criteria

The implementation of this decision passes only when:

1. The decision-governance skill describes every promotion step and the completeness gate.
2. The Draft README does not list any successfully promoted Draft.
3. The Draft and ADR templates use the revised source-Draft rules.
4. No new ADR contains a Markdown link to a source Draft that is scheduled for deletion.
5. A promotion cannot delete its source Draft before the ADR read-back and completeness check pass.
6. A failed deletion leaves a recoverable Promotion Cleanup Pending entry and does not create a duplicate ADR.
7. The existing DRAFT-0001 / ADR-0001 pair has an explicit completeness assessment.
8. No material rationale is lost during the existing-record migration.
9. Archived ADRs remain unchanged unless a separate user-approved decision explicitly authorizes a narrow reference-only correction.
10. Every changed path is read back and relevant hosted Document Standards validation passes.

## Consequences and Trade-Offs

- **Positive:** The accepted ADR is the only permanent decision record.
- **Positive:** Completed Drafts no longer clutter the active proposal collection.
- **Positive:** The completeness check protects the decision's rationale.
- **Positive:** A partial promotion can be resumed without creating duplicate ADRs.
- **Neutral:** Draft IDs remain visible as provenance in ADR metadata.
- **Neutral:** Rejected, withdrawn, and superseded Drafts keep their current retention behavior.
- **Negative:** Promotion takes more work because it requires a complete content comparison.
- **Negative:** Existing promoted Drafts may need individual migration review.
- **Negative:** A source Draft may remain temporarily when the ADR does not preserve enough information.

## Risks and Safeguards

| Risk | Likelihood / Impact | Safeguard | Residual risk |
|---|---|---|---|
| ADR omits material rationale | Medium / High | Use a direct section-by-section completeness check before deletion. | Reviewers may miss an implicit constraint. |
| Draft is deleted before ADR verification | Low / High | Make read-back and completeness checks mandatory preconditions for deletion. | A faulty check may still pass. |
| Partial GitHub writes leave duplicate records | Medium / Medium | Use Promotion Cleanup Pending and resume from the resulting ADR. | Cleanup may remain open until a later write succeeds. |
| An archived ADR links to a deleted Draft | Medium / Medium | Search references before deletion; require a separate approval for any archived-record correction. | Legacy links may remain until a migration decision resolves them. |
| Draft IDs are reused after deletion | Low / High | Keep the global sequence monotonic and never reuse an ID. | Index errors may hide an existing ID. |
| Rejected or withdrawn history is deleted by assumption | Low / Medium | Limit this decision to successful ADR promotion. | A separate retention decision may still be required. |

## Proposed Implementation Outline

After the user approves this exact Draft revision:

1. Create a new ADR that supersedes ADR-0001's source-Draft preservation rule. Do not edit ADR-0001's decision content.
2. Create an implementation task linked to the new accepted ADR.
3. Update the decision-governance skill, Draft and ADR indexes, workspace navigation, templates, archive guidance, and Document Type Catalog.
4. Complete a content comparison of DRAFT-0001 and ADR-0001. Record the result before considering deletion.
5. Resolve any missing rationale through an approved permanent decision record. Keep DRAFT-0001 if the safeguard does not pass.
6. Delete a source Draft only after the accepted ADR and required cross-reference checks pass.
7. Read back every changed path and run the relevant hosted Document Standards validation.
8. Record the migration and validation evidence in the implementation task and new ADR.

Do not delete DRAFT-0001 as part of preparing this proposal. This proposal does not itself authorize implementation.

## Questions for the User

1. Do you approve Option 3 and the complete promotion workflow, including the rationale completeness gate and deletion only after verified ADR acceptance?
2. Do you approve the recovery rule for partial promotion, including the temporary Promotion Cleanup Pending index section?
3. For DRAFT-0001, do you approve the stated migration safeguard: compare it with ADR-0001, preserve it if material rationale is missing, and use a separate approved record to resolve any gap rather than editing the archived ADR?

## Review and Approval

- **Revision presented:** 1
- **User decision:** Pending exact revision review
- **Approved scope:** The user approved the lifecycle direction and rationale safeguard in conversation on 2026-11-24. The complete revision 1 text and its migration details are presented for exact approval.
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-24 | 1 | Initial proposal. Defines Draft retirement after verified ADR promotion, a rationale completeness gate, partial-promotion recovery, and migration controls for DRAFT-0001. | User approved the lifecycle direction and rationale safeguard before this complete revision was prepared. Exact revision approval is pending. |

## References

- [ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis](../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md).
- [DRAFT-0001 — Establish Draft-to-ADR Governance and Repository Analysis](DRAFT-0001-repository-decision-governance-and-analysis.md).
- [Current Draft index](README.md).
- [Accepted ADR index](../adr/README.md).
- [Decision-governance skill](../../skills/decision-governance/SKILL.md).
