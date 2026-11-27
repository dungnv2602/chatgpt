# Subtask: Remove latest lint report copy and use the unified index

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-54
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to delete `.takeout/reports/latest-lint-report.json` and continue the Refactor Skills workstream.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — selected under the user's explicit execution instruction.
- **Required:** Yes
- **Created:** 2026-11-27 17:05 UTC
- **Updated:** 2026-11-27 17:05 UTC
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
- **Changed paths:** Pending.
- **Readback:** Pending.
- **Checks:** Not performed.
- **Limitations:** Hosted CI results and local test execution are outside scope.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

After this correction, continue the Refactor Skills workstream. Select the next eligible child under this parent.

## 10. Ledger Findings

Not applicable. This task does not remediate a CI finding.
