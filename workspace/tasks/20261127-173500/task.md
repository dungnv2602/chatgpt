# Task Folder: Remove the standalone latest lint report copy

**Template version:** 2.7

## Metadata

- **ID:** 20261127-173500
- **Created:** 2026-11-27 17:35 UTC
- **Updated:** 2026-11-28
- **Priority:** P0
- **Status:** Proposed
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User-approved DRAFT-0005 revision 1. The approval applies to the report-layout proposal; implementation requires an accepted ADR.
- **Governing ADR(s):** Pending — DRAFT-0005
- **Current execution:** No
- **Dependencies:** DRAFT-0005 promotion to an accepted ADR, including provenance/ID reconciliation.
- **Eligibility / deferral reason:** Proposed — accepted ADR prerequisite remains unresolved.
- **Related tasks:** Refactor Skills (recovery performed during workflow integrity review; not a parent-child relationship).

## 1. Original Request

Remove the standalone latest lint report copy and use the unified index as the latest-report locator.

## 2. Subsequent Instructions

- **2026-11-27:** The user separated this report-layout work from Refactor Skills. It is an independent task and must not be nested under the skills parent.
- **2026-11-28:** Reconstructed this missing task record from the approved Draft, discussion-register entry, task-board history and repository evidence. The reconstruction does not authorize implementation.
- **2026-11-28:** The source Draft ID conflicts with an accepted ADR's historical provenance. Reconcile the ID and references before promotion.

## 3. Objective and Acceptance Criteria

Remove the standalone latest lint report JSON and make the unified index the sole latest-report locator, without changing canonical report history or unrelated report architecture.

1. Confirm the exact approved Draft scope and reconcile source-Draft ID provenance.
2. Promote the exact approved Draft to an accepted ADR after the completeness and readback gates pass.
3. Update report producer, consumers, references and regression coverage within the approved ADR scope.
4. Remove only the redundant latest copy and reconcile the index, documentation and task references.
5. Commit and read back all changed paths. Do not inspect hosted CI results or run local scripts/tests.

## 4. Decisions

- **Status:** Proposed. No implementation is authorized before accepted ADR linkage.
- **Recovery:** The original task record was missing. This reconstructed record preserves the separate workstream and its decision gate.

## 5. Progress

### 2026-11-28 — task record recovery

- **Action:** Reconstructed the parent task from DRAFT-0005, workspace discussion and previous task-board references.
- **Result:** Restored the task as Proposed. The approved Draft remains the scope source; implementation is not started.
- **References:** DRAFT-0005; workspace/discussion.md; task-board history; accepted ADR metadata.
- **Next:** Reconcile DRAFT ID provenance and promote the approved Draft to an accepted ADR before implementation.

## 6. Current State and Remaining Work

This task is Proposed and outside the current Refactor Skills execution focus. Its decision prerequisite and source-Draft ID reconciliation remain outstanding.

## 7. Verification and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Reconstructed task folder and board/discussion tracking
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** This record is a recovery only. It does not establish accepted ADR authority or implementation.

## 8. Execution self-check

- Canonical task template consulted.
- Parentage and distinct scope confirmed.
- Approval and execution authority separated.
- The explicit standalone execute cue for implementation remains pending after ADR acceptance.

## 9. Handoff

Keep Proposed until source-Draft provenance is reconciled and the Draft is promoted to an accepted ADR. Do not implement within the Refactor Skills batch.

## 10. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 11. Ledger Findings

The CI Ledger is canonical for findings. No findings are attributed to this recovered task.
