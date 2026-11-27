# Subtask: Refactor task board to display scheduler working order

## Metadata

- **ID:** 20261127-082500-01
- **Parent Task ID:** 20261127-082500
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Approved board refactor in the conversation on 2026-11-27.
- **Governing ADR(s):** None — non-implementation subtask
- **Dependencies:** None
- **Required:** Yes
- **Created:** 2026-11-27 08:25 UTC
- **Updated:** 2026-11-27 08:25 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Objective

Refactor the board to show the Worker's scheduler decisions clearly and concisely.

## 2. Scope

Update only the task board's structure and task-record references required to display current execution, ranked eligible queue, next selection, and deferred work. The Worker remains scheduler authority.

## 3. Acceptance Criteria

1. Current Execution is distinct and visible.
2. Eligible queue is ordered and ranked.
3. Next Task is clearly identified.
4. Proposed, Blocked, Paused, and dependency-waiting work is separated and categorized.
5. The board does not introduce duplicate scheduling authority.
6. Links and task state are reconciled.

## 4. Decisions

Use concise rank/order indicators. Deferred work remains outside the executable queue.

## 5. Progress Log

### 2026-11-27 08:25 UTC

- **Action:** Started board refactor.
- **Result:** Source and governing format verified.
- **References:** `workspace/task_board.md`, `workspace/README.md`, Document Type Catalog.
- **Next:** Implement and verify the board.

## 6. Current State

The board is being refactored.

## 7. Evidence

- **Commit SHA:** Pending.
- **Changed paths:** Pending.
- **Read-back:** Pending.
- **Other evidence:** None.

## 8. Completion Record

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable
- **Evidence:** Not applicable

The Worker marks a regular subtask Done after its acceptance criteria pass and the Worker records its work and evidence.

## 9. Hosted Validation

Not applicable.

## 10. Handoff

Complete board changes and verify readback. Do not inspect hosted CI results.

## 11. Ledger Findings

None.
