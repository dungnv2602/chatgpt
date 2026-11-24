# Task: Implement verified source-Draft retirement and complete DRAFT-0001 migration

## Metadata

- **Template version:** 1.3
- **ID:** 20261124-160500
- **Created:** 2026-11-24 16:05 UTC
- **Updated:** 2026-11-24 16:05 UTC
- **Priority:** P1
- **Status:** Proposed
- **Origin:** User
- **Approval:** Pending — decision approval is recorded in ADR-0002; task execution approval is separate.
- **Governing ADR(s):** [ADR-0002 — Retire Source Drafts After Verified ADR Promotion](../adr/0002-retire-source-drafts-after-verified-adr-promotion.md)
- **Current execution:** No
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
- **2026-11-24:** Task execution approval remains pending for the remaining implementation work. Do not infer it from approval of ADR-0002.

## 3. Objective

Implement ADR-0002's verified source-Draft retirement workflow across the repository. Complete the legacy DRAFT-0001 migration only after the completeness and cross-reference gates pass. Keep the approved ADR as the permanent decision record and remove the source Draft file only after all safeguards pass.

## 4. Requirements

- Update the decision-governance skill with the complete promotion sequence, `promotion-pending` state, completeness checklist, partial-write recovery, and migration rules.
- Update the Draft and ADR indexes, workspace navigation, Draft and ADR templates, archive guidance, and Document Type Catalog.
- Define `promotion-pending` as temporary and non-authoritative. Only accepted ADRs can govern implementation tasks.
- Remove `promoted` as a steady-state Draft status.
- Keep **Current Drafts** limited to proposals requiring preparation, review, or approval.
- Use **Promotion Cleanup Pending** only for a verified accepted ADR whose source Draft deletion has not completed.
- Do not create `archive/draft/` or a Promoted Drafts section.
- Verify the complete DRAFT-0001 / ADR-0001 content mapping. ADR-0002 retains the material historical rationale not fully restated in ADR-0001.
- Keep archived ADR-0001's decision content unchanged. Its source-Draft link was corrected under the user's explicit narrow permission; retain the historical provenance commit.
- Delete DRAFT-0001 only after the migration coverage check passes and all active links to its working path are removed.
- Read back every changed file and obtain hosted Document Standards validation. Do not claim validation before observing a successful run.
- Do not modify foundational initialization or introduce hooks, scripts, or automatic approval.

## 5. Decisions

- **Accepted:** ADR-0002 selects verified ADR promotion followed by source-Draft deletion.
- **Accepted:** The ADR must preserve all material decision rationale before source deletion.
- **Accepted:** A provisional ADR uses `promotion-pending` and cannot authorize implementation.
- **Accepted:** Rejected, withdrawn, and superseded Draft retention is outside this decision.
- **Approved narrow change:** The user authorized the reference-only correction to ADR-0001.
- **Pending:** Task execution approval for the remaining repository-wide implementation and DRAFT-0001 deletion.

## 6. Progress Log

### 2026-11-24 16:05 UTC

- **Action:** Re-fetched DRAFT-0003 revision 2 and verified its approved revision and scope.
- **Result:** Exact approved revision 2 was present on branch `gpt`.
- **References:** `workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md`.
- **Next:** Promote the approved Draft to ADR-0002.

### 2026-11-24 16:05 UTC

- **Action:** Created ADR-0002 with provisional status, read it back, checked its decision scope, promotion sequence, rationale checklist, recovery rules, and DRAFT-0001 migration safeguard, then changed its status to accepted and read it back again.
- **Result:** ADR-0002 is accepted. The provisional state was not used as an implementation authority.
- **References:** `workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md`; acceptance commit `b4da3f285c103bf7960dc07faabafb9a39f4fbbf`.
- **Next:** Finish promotion closeout and wait for task execution approval before the broader workflow rollout.

### 2026-11-24 16:05 UTC

- **Action:** Corrected the source-Draft reference in archived ADR-0001 under the user's explicit permission. Replaced the dead working-tree link with DRAFT-0001 provenance and the immutable promotion commit reference. Did not change the accepted decision outcome or rationale.
- **Result:** ADR-0001 no longer contains a link to the DRAFT-0001 working path. Its original approved source remains available in Git history.
- **References:** `archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md`; commit `3008876a4e25152bed0293ac92100d9123742dfe`; original DRAFT-0001 promotion commit `241ba8ad5e4aa7cff683ecf49df31c0ad11945ef`.
- **Next:** Complete the migration coverage assessment and remove the source file only after task execution approval.

## 7. Current State

- ADR-0002 is accepted and indexed.
- ADR-0001 has a reference-only correction. Its accepted decision content remains unchanged.
- DRAFT-0001 remains in the repository pending final migration and deletion authorization through this task.
- DRAFT-0003 is the approved source Draft for ADR-0002 and awaits promotion closeout.
- The repository-wide governance files still contain the old preserve-after-promotion rule.
- This task is Proposed. No remaining implementation work is authorized until the user approves this task's execution scope.

## 8. Remaining Work

- Complete the DRAFT-0001 completeness coverage table and read back all linked permanent records.
- Resolve any remaining reference to the DRAFT-0001 working path.
- After task execution approval, delete DRAFT-0001 and verify its absence.
- Delete DRAFT-0003 as part of the completed promotion transaction and verify its absence.
- Update all governance files and indexes required by ADR-0002.
- Update ADR-0002 implementation task metadata and Confirmation evidence.
- Run and inspect the relevant hosted Document Standards validation.
- Record the final migration and validation evidence.

## 9. Next Actions

1. Present this task for explicit execution approval.
2. After approval, finish the DRAFT-0001 completeness assessment, close out source deletion, and implement the remaining ADR-0002 requirements.
3. Read back all changed paths and inspect hosted validation results.

## 10. References

- [ADR-0002 — Retire Source Drafts After Verified ADR Promotion](../adr/0002-retire-source-drafts-after-verified-adr-promotion.md)
- [ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis](../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md)
- [DRAFT-0001 original promotion commit](https://github.com/dungnv2602/chatgpt/commit/241ba8ad5e4aa7cff683ecf49df31c0ad11945ef)
- [ADR-0001 reference correction commit](https://github.com/dungnv2602/chatgpt/commit/3008876a4e25152bed0293ac92100d9123742dfe)

## 11. Verification

- **Check:** DRAFT-0003 exact revision and approval state.
- **Method:** Re-fetch from branch `gpt` and inspect metadata and approved revision.
- **Result:** Passed.
- **Limitations:** Approval of the decision does not authorize the remaining implementation task.

- **Check:** ADR-0002 provisional record and accepted record.
- **Method:** Read back after each write and verify status, source Draft ID, decision outcome, completeness checklist, recovery procedure, and migration safeguards.
- **Result:** Passed; ADR-0002 is accepted.
- **Limitations:** Repository-wide implementation and hosted validation remain pending.

- **Check:** ADR-0001 legacy source link.
- **Method:** Read back archived ADR-0001 and verify that the working-tree Draft path is absent while provenance commit remains.
- **Result:** Passed.
- **Limitations:** DRAFT-0001 itself remains until its migration gate and task approval pass.

## 12. Handoff Instructions

The next Worker must load the task-specific decision-governance skill and Document Standards. The task is Proposed and requires explicit user approval before the remaining implementation work starts. Do not treat ADR-0002 acceptance as task execution approval. Preserve DRAFT-0001 until the full completeness check and cross-reference checks pass. Do not edit ADR-0001 beyond the already authorized reference-only correction. Do not modify foundational initialization.

## 13. Ledger Findings

_No findings linked._
