# Task: Implement verified source-Draft retirement and complete DRAFT-0001 migration

## Metadata

- **Template version:** 1.3
- **ID:** 20261124-160500
- **Created:** 2026-11-24 16:05 UTC
- **Updated:** 2026-11-24 16:20 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved by user for execution on 2026-11-24 16:12 UTC.
- **Governing ADR(s):** [ADR-0002 — Retire Source Drafts After Verified ADR Promotion](../adr/0002-retire-source-drafts-after-verified-adr-promotion.md)
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** None
- **Ledger group:** None
- **Archived:** No

## 1. Original Request

> A draft turned to ADR is no longer needed, we need to delete it.

> Approve. And I give you permission to modify ADR-0001 to deal with its linking with DRAFT-0001.

## 2. Subsequent Instructions

- **2026-11-24:** The user approved DRAFT-0003 revision 2, including the rationale completeness safeguard and the complete promotion protocol.
- **2026-11-24:** The user explicitly authorized a narrow modification to archived ADR-0001 to resolve its link to DRAFT-0001. This permission does not authorize rewriting ADR-0001's accepted decision.
- **2026-11-24:** ADR-0002 was created from the exact approved Draft, read back, checked, and accepted.
- **2026-11-24 16:12 UTC:** The user explicitly approved execution of task 20261124-160500. This approval authorizes the remaining implementation scope in this task under ADR-0002.

## 3. Objective

Implement ADR-0002's verified source-Draft retirement workflow across the repository. Complete the legacy DRAFT-0001 migration only after the completeness and cross-reference gates pass. Keep the approved ADR as the permanent decision record and remove the source Draft file only after all safeguards pass.

## 4. Requirements

- Update the decision-governance skill with the complete promotion sequence, promotion-pending state, completeness checklist, partial-write recovery, and migration rules.
- Update the Draft and ADR indexes, workspace navigation, Draft and ADR templates, archive guidance, and Document Type Catalog.
- Define promotion-pending as temporary and non-authoritative. Only accepted ADRs can govern implementation tasks.
- Remove promoted as a steady-state Draft status.
- Keep Current Drafts limited to proposals requiring preparation, review, or approval.
- Use Promotion Cleanup Pending only for a verified accepted ADR whose source Draft deletion has not completed.
- Do not create archive/draft/ or a Promoted Drafts section.
- Verify the complete DRAFT-0001 / ADR-0001 content mapping. ADR-0002 retains the material historical rationale not fully restated in ADR-0001.
- Keep archived ADR-0001's decision content unchanged. Its source-Draft link was corrected under the user's explicit narrow permission; retain the historical provenance commit.
- Delete DRAFT-0001 only after the migration coverage check passes and all active links to its working path are removed.
- Read back every changed file and obtain hosted Document Standards validation. Do not claim validation before observing a successful run.
- Do not modify foundational initialization or introduce hooks, scripts, or automatic approval.

## 5. Decisions

- **Accepted:** ADR-0002 selects verified ADR promotion followed by source-Draft deletion.
- **Accepted:** The ADR must preserve all material decision rationale before source deletion.
- **Accepted:** A provisional ADR uses promotion-pending and cannot authorize implementation.
- **Accepted:** Rejected, withdrawn, and superseded Draft retention is outside this decision.
- **Approved narrow change:** The user authorized the reference-only correction to ADR-0001.
- **Approved execution:** The user approved task execution on 2026-11-24 16:12 UTC.

## 6. Progress Log

### 2026-11-24 16:05 UTC

- **Action:** Re-fetched DRAFT-0003 revision 2 and verified its approved revision and scope.
- **Result:** Exact approved revision 2 was present on branch gpt.
- **References:** workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md.
- **Next:** Promote the approved Draft to ADR-0002.

### 2026-11-24 16:05 UTC

- **Action:** Created ADR-0002 with provisional status, read it back, checked its decision scope, promotion sequence, rationale checklist, recovery rules, and DRAFT-0001 migration safeguard, then changed its status to accepted and read it back again.
- **Result:** ADR-0002 is accepted. The provisional state was not used as an implementation authority.
- **References:** workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md; acceptance commit b4da3f285c103bf7960dc07faabafb9a39f4fbbf.
- **Next:** Finish promotion closeout and wait for task execution approval before the broader workflow rollout.

### 2026-11-24 16:05 UTC

- **Action:** Corrected the source-Draft reference in archived ADR-0001 under the user's explicit permission. Replaced the dead working-tree link with DRAFT-0001 provenance and the immutable promotion commit reference. Did not change the accepted decision outcome or rationale.
- **Result:** ADR-0001 no longer contains a link to the DRAFT-0001 working path. Its original approved source remains available in Git history.
- **References:** archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md; commit 3008876a4e25152bed0293ac92100d9123742dfe; original DRAFT-0001 promotion commit 241ba8ad5e4aa7cff683ecf49df31c0ad11945ef.
- **Next:** Complete the migration coverage assessment and remove the source file only after task execution approval.

### 2026-11-24 16:05 UTC

- **Action:** Completed ADR-0002 promotion closeout. Removed DRAFT-0003 from the Draft index and Open Discussions, then deleted its source file after ADR-0002 was accepted and read back.
- **Result:** DRAFT-0003 is no longer present in the active Draft collection. Its approved revision remains identifiable through ADR-0002 provenance and the promotion commit.
- **References:** ADR-0002 acceptance commit b4da3f285c103bf7960dc07faabafb9a39f4fbbf; DRAFT-0003 deletion commit cf293d2d7bc3396eefb91360f0b36561d777ceb4; Draft index and discussion register.
- **Next:** Complete DRAFT-0001 migration only after task execution approval.

### 2026-11-24 16:15 UTC

- **Action:** Recorded the user's explicit execution approval and reconciled the task state.
- **Result:** Task status is In Progress. Approval is Approved. The task is the current execution task. The repository baseline was read from branch gpt, including the task record, task board, ADR-0002, complete DRAFT-0001, archived ADR-0001, and the task-specific decision-governance skill.
- **References:** User instruction at 2026-11-24 16:12 UTC; workspace/discussion.md; repository paths listed above.
- **Next:** Complete the DRAFT-0001 rationale coverage assessment and inspect canonical document formats before editing governance files.

### 2026-11-24 16:16 UTC

- **Action:** Updated the task board after the task activation commit. The first board write encountered a stale-blob conflict because an automated lint report had added seven Proposed tasks. Re-fetched the board, preserved those entries, and applied the task-state change using the current blob.
- **Result:** The task record and board both show task 20261124-160500 as In Progress and current execution. Read-back confirmed the approval metadata and board placement. No unrelated Proposed task was removed.
- **References:** Task activation commit e25c025c3f3482a77cc7203625bda16262edbdec; board update commit f9555f83b79fe31ee2f4b08597f29dbac5260308; workspace/task_board.md.
- **Next:** Complete the DRAFT-0001 rationale coverage assessment and inspect canonical document formats before editing governance files.

### 2026-11-24 16:20 UTC

- **Action:** Compared the complete approved DRAFT-0001 revision 1 with archived ADR-0001 and accepted ADR-0002. Inspected the canonical Draft and ADR templates, archive guidance, workspace navigation, indexes, decision-governance skill, Agent Skill Authoring instructions, repository writing policy, and Document Type Catalog.
- **Result:** The completeness checklist passes. ADR-0001 preserves the decision, options, outcome, consequences, implementation scope, migration, Confirmation criteria, approval details, and evidence. ADR-0002 preserves the historical rationale for the analysis location, global flat ADR sequence, and boundaries among analysis, Drafts, ADRs, tasks, and CI diagnostics. The original approved Draft and its complete reference list remain accessible at commit 241ba8ad5e4aa7cff683ecf49df31c0ad11945ef. No material rationale gap was found.
- **References:** workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md; archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md; workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md; workspace/DRAFT_TEMPLATE.md; workspace/ADR_TEMPLATE.md; archive/README.md; archive/adr/README.md; workspace/README.md; workspace/draft/README.md; workspace/adr/README.md; skills/decision-governance/SKILL.md; skills/document-standards/references/document-type-catalog.md.
- **Next:** Apply ADR-0002's promotion, recovery, cleanup, and status rules consistently across the canonical skill, templates, indexes, workspace navigation, archive guidance, and catalog.

## 7. Current State

- ADR-0002 is accepted and indexed.
- ADR-0001 has a reference-only correction. Its accepted decision content remains unchanged.
- DRAFT-0001 remains in the repository pending final index, reference, and deletion closeout.
- DRAFT-0003 was deleted after ADR-0002 acceptance and promotion closeout.
- The rationale completeness assessment for DRAFT-0001 passed. No material gap requires another ADR.
- Task execution is approved. This task is In Progress and is the current execution task.
- The canonical formats and owner guidance have been inspected. They still contain the old preserve-after-promotion rule.

## 8. Remaining Work

- Update the decision-governance skill, Draft and ADR templates, Draft and ADR indexes, workspace navigation, archive guidance, and Document Type Catalog.
- Set ADR-0002 implementation status to in-progress and update its Confirmation evidence after the implementation checks pass.
- Remove the DRAFT-0001 entry from the Draft index and resolve all active Markdown links to its working path.
- Delete DRAFT-0001 only after the index and cross-reference checks pass.
- Read back every changed path.
- Run and inspect the relevant hosted Document Standards validation.
- Record the final migration and validation evidence.

## 9. Next Actions

1. Update the decision-governance skill with the exact ADR-0002 promotion sequence, completeness checklist, partial-write recovery, and DRAFT-0001 migration rule.
2. Update the Draft and ADR templates and indexes to remove promoted and define temporary promotion-pending handling.
3. Update workspace navigation, archive guidance, and Document Type Catalog.
4. Set ADR-0002 implementation status to in-progress and link this implementation task.
5. Remove the DRAFT-0001 cleanup-pending entry, verify no active Markdown links target the working file, and delete the source file.
6. Read back all changed paths and inspect hosted Document Standards validation.

## 10. References

- [ADR-0002 — Retire Source Drafts After Verified ADR Promotion](../adr/0002-retire-source-drafts-after-verified-adr-promotion.md)
- [ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis](../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md)
- [DRAFT-0001 original promotion commit](https://github.com/dungnv2602/chatgpt/commit/241ba8ad5e4aa7cff683ecf49df31c0ad11945ef)
- [ADR-0001 reference correction commit](https://github.com/dungnv2602/chatgpt/commit/3008876a4e25152bed0293ac92100d9123742dfe)

## 11. Verification

### DRAFT-0001 rationale coverage

| ADR-0002 completeness criterion | Permanent evidence | Result |
|---|---|---|
| Problem, repository state, and decision scope | ADR-0001, Context and Problem Statement; Decision Outcome; Implementation Scope | Pass |
| User goals, non-goals, constraints, and decision drivers | ADR-0001, Decision Drivers and Implementation Scope; ADR-0002, Decision Drivers and Decision Outcome | Pass |
| Viable options and material reasons for rejecting alternatives | ADR-0001, Considered Options and Pros and Cons of the Options | Pass |
| Chosen outcome and decision rationale | ADR-0001, Decision Outcome | Pass |
| Consequences, trade-offs, risks, and safeguards | ADR-0001, Consequences and Implementation Scope; ADR-0002, Risks and Safeguards for the retirement decision | Pass |
| Implementation boundary, dependencies, migration, and rollback | ADR-0001, Implementation Scope; ADR-0002, Implementation Scope and Partial promotion and recovery | Pass |
| Observable Confirmation criteria | ADR-0001, Confirmation; ADR-0002, Confirmation | Pass |
| Material assumptions, evidence, and source references | ADR-0001, More Information; ADR-0002, Historical context and More Information; complete source Draft at commit 241ba8ad5e4aa7cff683ecf49df31c0ad11945ef | Pass |
| User approval details, exact Draft ID and revision | ADR-0001, Context and Problem Statement and More Information; source Draft metadata and Review and Approval; original approved commit | Pass |
| Historical rationale for analysis location, ADR folder/numbering, and record boundaries | ADR-0002, Historical context retained from DRAFT-0001 | Pass |

**Assessment:** All material decision rationale is preserved in permanent ADR records. ADR-0001's accepted decision content remains unchanged. The original approved Draft remains available in Git history as provenance and retains its complete reference list. No material gap blocks source deletion.

### Other verification

- **Check:** DRAFT-0003 exact revision and approval state.
- **Method:** Re-fetch from branch gpt and inspect metadata and approved revision.
- **Result:** Passed.
- **Limitations:** Approval of the decision does not authorize the remaining implementation task.

- **Check:** ADR-0002 provisional record and accepted record.
- **Method:** Read back after each write and verify status, source Draft ID, decision outcome, completeness checklist, recovery procedure, and migration safeguards.
- **Result:** Passed; ADR-0002 is accepted.
- **Limitations:** Repository-wide implementation and hosted validation remain pending.

- **Check:** ADR-0001 legacy source link.
- **Method:** Read back archived ADR-0001 and verify that the working-tree Draft path is absent while provenance commit remains.
- **Result:** Passed.
- **Limitations:** DRAFT-0001 itself remains until its migration gate and cross-reference checks pass.

- **Check:** Task execution approval.
- **Method:** Direct user instruction on 2026-11-24 16:12 UTC.
- **Result:** Approved. Task activated as In Progress.
- **Limitations:** This approval does not waive ADR-0002's completeness or cross-reference gates.

## 12. Handoff Instructions

Continue under ADR-0002 and the approved task scope. Preserve DRAFT-0001 until the complete rationale comparison and cross-reference checks pass. Do not edit ADR-0001 beyond the already authorized reference-only correction. Do not modify foundational initialization. Do not add hooks, scripts, automatic approval, or unrelated work.

## 13. Ledger Findings

_No findings linked._
