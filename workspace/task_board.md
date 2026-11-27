# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](TASK_BOARD_TEMPLATE.md). Preserve its structure and scheduler contract.

## Scheduler contract

The Worker is the sole scheduler. This board publishes its current selection and ordered eligible queue. It is not a second scheduler. Compare the board with task records and child indexes before declaring the queue empty.

Check eligibility before priority or age. Dependencies must be satisfied, execution must be authorized, and status must be Ready. Rank eligible tasks by priority (P0 first), then age within the same priority unless a documented dependency or material constraint changes the order. Keep ineligible tasks out of the queue. List them in the appropriate deferred section with the exact reason.

**Approval:** Approved records explicit authorization for the documented scope or applicable standing authorization. Pending means the user has not authorized execution. Declined means the user rejected the proposal. Approval does not depend on status or eligibility.

This is the sole index of active task parents. Each parent folder contains `task.md` and `subtasks/README.md`. The parent index lists substantive children. Board links point to parents, except Current Execution may link to the selected child. Keep a parent open while a required child remains open. The Worker owns status, selection, and deletion at closeout.

## Current Execution

[Refactor Skills — persistent P0 parent](tasks/20261127-173000/task.md). The parent remains selected by the user's explicit priority instruction and must stay open for future skills-refactoring subtasks.

## Ordered Eligible Execution Queue

1. **P1** — [20261127-173000-02: Consolidate specialist skills into The Worker](tasks/20261127-173000/subtasks/02-consolidate-specialist-skills-into-worker.md) — Approved, Ready, dependencies satisfied. Selected next under the user-prioritized Refactor Skills parent.
2. **P1** — [20261127-173100-02: Audit document template coverage and create missing templates](tasks/20261127-173100/subtasks/02-audit-document-template-coverage.md) — Approved, Ready, no dependencies.
3. **P1** — [20261127-173000-04: Enforce template-first document editing](tasks/20261127-173000/subtasks/04-enforce-template-first-document-editing.md) — Approved, Ready, no dependencies.

## Next Task

[20261127-173000-02](tasks/20261127-173000/subtasks/02-consolidate-specialist-skills-into-worker.md) is next under the selected Refactor Skills parent.

## Deferred Work

### Blocked

_No blocked tasks._

### Proposed — decision pending

_No proposed tasks._

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261127-173000-03 | Correct objective-based task parent selection | P1 | Paused | Approved | Remaining audit is deferred behind the current Refactor Skills consolidation. | [subtask](tasks/20261127-173000/subtasks/03-correct-objective-based-task-parent-selection.md) |

### Dependency-waiting

_No dependency-waiting tasks._
