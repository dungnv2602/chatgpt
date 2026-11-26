# Subtask: Active-task migration and folder archive compatibility

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-05
- **Parent Task ID:** 20261126-232913
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** ADR-0004
- **Dependencies:** 20261126-232913-01
- **Required:** Yes
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-26 23:31 UTC

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
### 2026-11-26 23:31 UTC
- **Action:** Registered this implementation subtask and its acceptance criteria.
- **Result:** Ready; implementation has not started.
- **References:** ADR-0004 and parent task folder.
- **Next:** Execute after dependencies are complete.

## 6. Current State
Ready; implementation has not started.

## 7. Evidence
- **Commit SHA:** Not applicable yet.
- **Changed paths:** None.
- **Read-back:** Not performed.
- **Other evidence:** None.

## 8. Completion Record
- **Status:** Ready
- **Completed at:** Not applicable
- **Completion basis:** Not Done.
- **Evidence:** Not applicable.

## 10. Handoff
Follow the parent subtask index. Record exact commits and read-back evidence. Do not mark Done until all acceptance criteria pass.
