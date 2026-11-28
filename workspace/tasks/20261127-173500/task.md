# Task: Remove the standalone latest lint report copy

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173500
- **Created:** 2026-11-27 17:40 UTC
- **Updated:** 2026-11-28
- **Priority:** P0
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit user instruction to delete `.takeout/reports/latest-lint-report.json`.
- **Governing ADR(s):** ADR-0007
- **Current execution:** Yes
- **Dependencies:** ADR-0007 accepted; implementation underway.
- **Eligibility / deferral reason:** Eligible and authorized; incomplete coordinated migration.
- **Related tasks:** ADR-0003; Refactor Skills parent 20261127-173000 (subsequent workstream instruction only).

## 1. Original Request

> `.takeout/reports/latest-lint-report.json`
>
> Delete this as we agreed on the format

## 2. Subsequent Instructions

> Then proceed to the task "refactor skills"
>
> /start

The Refactor Skills workstream continues under its own parent. This report-layout task remains separate because its objective does not refactor repository skills.

## 3. Objective and Acceptance Criteria

Remove the standalone latest lint report JSON and use the unified `.takeout/reports/index.json` as the only locator for the latest lint report.

1. Obtain approval for DRAFT-0005 revision 1 and promote it to a new accepted ADR. Keep ADR-0003 immutable.
2. Stop the lint generator from writing the standalone latest JSON file.
3. Resolve the latest eligible lint baseline from the shared index and its `history_path`.
4. Update both lint workflows, regression tests, and active report documentation.
5. Delete `.takeout/reports/latest-lint-report.json`.
6. Read back all changed paths and confirm no active producer or consumer depends on the deleted path.
7. Do not inspect hosted CI results or run local tests.

## 4. Decisions

- **Proposal:** DRAFT-0005 revision 1 recommends an index-only latest-report locator.
- **Decision status:** Pending user approval.
- **Execution status:** Proposed. Task approval does not replace decision approval.

## 5. Progress

### 2026-11-27 17:40 UTC

- Created this independent task.

### 2026-11-28

- ADR-0007 accepted and execution authorized.
- Generator latest-copy output removed (commit `3975531703365e3b5c8dd4cd71f05abade021d7d`).
- Regression assertions changed to index/history-based checks (commit `cc76ac95683ab6fbd9806ab2ef37979ada58465f`). Tests were not run.
- Changed-document baseline selection migrated to index/history retrieval (commits `4939316a0e350d49432649410df93c1d5e332fae`, `e2e4ad93b5a3b3b90133c6473e4e3485473c0f78`). Not validated.
- Report guide updated (commit `b287e7cba57027af90851252e44fbd56db5ce4b2`).
- Full-docs workflow migration, final consumer audit, deletion of the empty reset-marker file, and readback verification remain outstanding. Task is not complete.

## 6. Current State and Remaining Work

ADR-0007 supersedes the latest-copy requirement. Coordinated migration is incomplete. Finish full-docs workflow, verify consumers, remove the marker file, and read back all changes.

## 7. Verification and Evidence

- **Commit SHA:** Multiple commits listed in Progress.
- **Readback:** Remaining.
- **Checks:** Not run, per scope.
- **Limitations:** Hosted CI not inspected. Migration not complete.

## 8. Handoff

Complete the remaining coordinated migration and verify repository readback. Do not claim completion until every active producer and consumer is reconciled.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

Not applicable.
