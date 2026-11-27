# Subtask: Remove latest lint report copy and use the unified index

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-54
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** Proposed
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to delete `.takeout/reports/latest-lint-report.json` and continue the Refactor Skills workstream.
- **Governing ADR(s):** Pending — DRAFT-0005
- **Dependencies:** None
- **Eligibility / deferral reason:** Proposed — changing accepted ADR-0003 requires approval of DRAFT-0005 revision 1 and promotion to a new accepted ADR before implementation.
- **Required:** Yes
- **Created:** 2026-11-27 17:05 UTC
- **Updated:** 2026-11-27 17:15 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Delete this as we agreed on the format

## 2. Subsequent Instructions

The complete user instruction is preserved in the parent task's Subsequent Instructions.

## 3. Objective and Scope

Remove the standalone `latest-lint-report.json` copy. Make the unified `.takeout/reports/index.json` the only locator for the latest lint run. Keep immutable report JSON under the shared `history/` directory.

Update every active producer, consumer, workflow, regression fixture, and operating guide that depends on the standalone latest file. Preserve baseline eligibility, run identity, history paths, report integrity, and Ledger ingestion. Do not inspect hosted CI results or run local tests.

## 4. Acceptance Criteria

1. Delete `.takeout/reports/latest-lint-report.json`.
2. Stop the lint generator from creating or updating that file.
3. Resolve the latest eligible lint baseline from the unified index and its `history_path`.
4. Update both lint workflows and all active code, tests, and documentation references.
5. Keep lint and Actions entries in the shared index. Do not create a second index or latest pointer.
6. Read back every changed path and confirm that no active producer or consumer requires the deleted file.

## 5. Decisions and Progress

- **Execution:** P0 and Approved under the user's explicit instruction.
- **Format decision:** The unified index is the sole run locator. The immutable `report.json` in each history entry remains the source for baseline comparison.

## 6. State and Evidence

- **Commit SHA:** Not committed.
- **Changed paths:** Draft only: `workspace/draft/DRAFT-0005-unified-index-without-latest-lint-copy.md`.
- **Readback:** Pending.
- **Checks:** Not performed.
- **Limitations:** The accepted ADR-0003 still requires the file. Implementation is not authorized until the user approves the exact Draft revision and the resulting ADR reaches accepted status.

## 7. Completion

- **Status:** Proposed
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

Wait for user approval of DRAFT-0005 revision 1. Do not delete the file or change its consumers before the resulting ADR reaches accepted status. Child 04 is independent and remains the next Refactor Skills task.

## 10. Ledger Findings

Not applicable. This task does not remediate a CI finding.
