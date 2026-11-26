# Subtask: Active-task migration and folder archive compatibility

## Metadata
- **ID:** 20261126-232913-05
- **Parent:** [20261126-232913](../task.md)
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P0
- **Approval:** Approved
- **Governing ADR:** [ADR-0004](../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md)
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-26 23:29 UTC
- **Required:** Yes

## Objective
Active-task migration and folder archive compatibility as part of the accepted ADR-0004 implementation.

## Acceptance Criteria
1. Migrate every active flat task record to workspace/tasks/<task-id>/task.md while preserving task IDs, content, status, approval, progress, evidence, and relative links.
2. Give every migrated task a subtasks/README.md and preserve existing task links.
3. Archive new tasks as complete folders under .archive/task/<task-id>/ with task.md as the indexed parent record.
4. Read both folder archives and historical flat-file archives without rewriting historical archives.
5. Update retention index entries and cleanup logic to retain child records and remove only the intended complete task folder.
6. Read back all active task folders, board links, archive paths, and retention entries.

## Progress
- **Current state:** Ready; follow the execution order in the parent subtask index.
- **Evidence:** None recorded.
- **Completion record:** Not Done. Record commit SHA(s), changed paths, and verification evidence on completion.

## Handoff
Execute only this subtask's scope. Record meaningful changes and evidence here and in the parent task. Do not mark Done until every acceptance criterion passes.
