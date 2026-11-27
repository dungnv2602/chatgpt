# Subtask: Active-task migration and folder archive compatibility

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-05
- **Parent Task ID:** 20261126-232913
- **Type:** Implementation
- **Status:** Done
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** ADR-0004
- **Dependencies:** 20261126-232913-01
- **Required:** Yes
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-27 00:58 UTC

## 1. Objective
Active-task migration and folder archive compatibility as part of the accepted ADR-0004 implementation.

## 2. Scope
Implement only this subtask within ADR-0004. Parent: [20261126-232913](../task.md). Governing decision: [ADR-0004](../../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md).

## 3. Acceptance Criteria
1. Migrate every active flat task record to workspace/tasks/<task-id>/task.md while preserving task IDs, content, status, approval, progress, evidence, and relative links.
2. Give every migrated task a subtasks/README.md and preserve existing task links.
3. Archive new tasks as complete folders under .archive/task/<task-id>/ with task.md as the indexed parent record.
4. Read both folder archives and historical flat-file archives without rewriting historical archives.
5. Update retention index entries and cleanup logic to retain child records and remove only the intended complete task folder.
6. Read back all active task folders, board links, archive paths, and retention entries.

## 4. Decisions
- Follow ADR-0004.
- Preserve existing evidence and validation/security checks.
- Do not inspect hosted results before explicit user trigger.

## 5. Progress Log
### 2026-11-27 00:20 UTC
- **Action:** Began inventory of active flat task records and review of archive retention/index cleanup behavior.
- **Result:** Task-folder and Ledger generation contracts are in place. Migration must preserve all active task IDs and metadata, create at least one subtask record per task, update board pointers and relative evidence links, and leave historical flat archives immutable. Archive cleanup currently indexes exact file paths, so new folder archives must index every child file.
- **References:** workspace/tasks/; workspace/task_board.md; .github/archive-retention-index.json; .github/scripts/cleanup-archive.py; ADR-0004.
- **Next:** Enumerate exact active flat task files and inspect cleanup/index schema before moving any record.

## 6. Current State
In Progress. Active task inventory and archive cleanup compatibility are being audited; no active flat task records have been migrated yet.

## 7. Evidence
- **Commit SHA:** Multiple remote commits; key commits are recorded in the progress log.
- **Changed paths:** Six migrated task folders and subtask indexes, `workspace/task_board.md`, `.github/scripts/cleanup-archive.py`, `.github/scripts/test_cleanup_archive.py`.
- **Read-back:** All six task.md files, all six subtasks/README.md files, board links, cleanup script, tests, and retention index were read back.
- **Other evidence:** All six old flat paths returned NOT_FOUND. All local evidence targets checked exist. No archive record or retention-index entry was changed.

## 8. Completion Record
- **Status:** Done
- **Completed at:** 2026-11-27 00:58 UTC
- **Completion basis:** All six active flat tasks were migrated, all required task folders and subtask indexes were verified, board and relative links were reconciled, and folder/legacy archive retention compatibility was implemented with regression coverage.
- **Evidence:** Remote read-back of every changed path. Hosted tests were not executed or reviewed.

## 10. Handoff
Subtask 05 is complete. Continue with subtask 06 — regression coverage and documentation/catalog alignment. Preserve the deferred hosted-results-review boundary.
