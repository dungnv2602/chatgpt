# Task: Remove the standalone latest lint report copy

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173500
- **Created:** 2026-11-27 17:40 UTC
- **Updated:** 2026-11-28 22:30 +07:00
- **Priority:** P0
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit execution cue and task scope following accepted ADR-0007.
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

- DRAFT-0005 revision 1, Option 2 approved; accepted ADR-0007 governs the implementation.
- Execution authorized and underway.

## 5. Progress

### 2026-11-27 17:40 UTC

- Created this independent task.

### 2026-11-28

- ADR-0007 accepted and execution authorized.
- Generator latest-copy output removed (commit `3975531703365e3b5c8dd4cd71f05abade021d7d`).
- Regression assertions changed to index/history-based checks (commit `cc76ac95683ab6fbd9806ab2ef37979ada58465f`). Tests were not run.
- Changed-document baseline selection migrated to index/history retrieval, with full-audit fallback for baseline retrieval failure (commits `4939316a0e350d49432649410df93c1d5e332fae`, `e2e4ad93b5a3b3b90133c6473e4e3485473c0f78`, `bc62fa39442403f0435ac69da784d590923efe6c`, `911532c9a3caec0334231d3be77d882ac73a90fe`). Not validated.
- Report guide updated (commit `b287e7cba57027af90851252e44fbd56db5ce4b2`).
- Full-docs workflow baseline retrieval and staging migrated (commit `a581ff4b24356ba234fd34d341c4ac104c5bf06c`).
- Workflow autonomy/blocker discipline strengthened in canonical Worker instructions (commit `c87fa200c648e22e3d482d90f3cf92f475e750aa`).
- A regression assertion for report index ordering requires correction before closeout. Final consumer audit, marker deletion, readback, and reconciliation remain outstanding.

## 6. Current State and Remaining Work

ADR-0007 supersedes the latest-copy requirement. Coordinated migration is incomplete. Correct the index-order regression assertion, verify active consumers and workflow references, remove the reset marker, reconcile the board/discussion and read back the committed changes.

## 7. Verification and Evidence

- **Commit SHA:** Multiple commits listed in Progress.
- **Readback:** Partial; final readback remains.
- **Checks:** Not run, per scope.
- **Limitations:** Hosted CI not inspected. Migration not complete.

## 8. Handoff

Complete the remaining coordinated migration and verify repository readback. Do not claim completion until every active producer and consumer is reconciled.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

Not applicable.
