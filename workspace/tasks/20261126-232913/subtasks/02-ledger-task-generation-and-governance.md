# Subtask: Ledger task generation and governance handoff

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-02
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
Make Ledger-generated task folders, CI subtasks, task refs, task discovery, board links, and governance states consistent.

## 2. Scope
Implement only this subtask within ADR-0004. Parent: [20261126-232913](../task.md). Governing decision: [ADR-0004](../../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md).

## 3. Acceptance Criteria
1. Generate a parent task folder and typed CI remediation subtask for each eligible grouped finding.
2. Ledger task_refs identify stable parent Task IDs.
3. Generated implementation tasks remain Proposed with Governing ADR(s) Pending until Worker review and accepted ADR linkage.
4. Folder task discovery and task.md board links work.
5. New P0 generation preserves valid Worker-selected Current Execution.
6. Regression tests cover folder generation, task_refs, governance gating, and current-task preservation.

## 4. Decisions
- Follow ADR-0004.
- Keep implementation evidence separate from hosted validation evidence.
- Do not weaken existing checks or inspect hosted results before explicit user trigger.

## 5. Progress Log
### 2026-11-26 23:31 UTC
- **Action:** Registered this implementation subtask and its acceptance criteria.
- **Result:** Ready; no implementation changes for this subtask yet.
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
