# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](TASK_BOARD_TEMPLATE.md). Preserve its structure and scheduler contract.

## Scheduler contract

The Worker is the sole scheduler. This board publishes its current selection and ordered eligible queue. It is not a second scheduler. Compare the board with task records and child indexes before declaring the queue empty.

Check eligibility before priority or age. Dependencies must be satisfied, execution must be authorized, and status must be Ready. Rank eligible tasks by priority (P0 first), then age within the same priority unless a documented dependency or material constraint changes the order. Keep ineligible tasks out of the queue. List them in the appropriate deferred section with the exact reason.

**Approval:** Approved records explicit authorization for the documented scope or applicable standing authorization. Pending means the user has not authorized execution. Declined means the user rejected the proposal. Approval does not depend on status or eligibility.

This is the sole index of active task parents. Each parent folder contains `task.md` and `subtasks/README.md`. The parent index lists substantive children. Board links point to parents, except Current Execution may link to the selected child. Keep a parent open while a required child remains open. The Worker owns status, selection, and deletion at closeout.

## Current Execution

[Refactor Skills — P0](tasks/20261127-173000/task.md), a persistent skills-refactoring parent; completed child 01 closed. Keep this parent open for future skills-refactoring subtasks.

## Ordered Eligible Execution Queue

_No additional eligible tasks; the selected P0 task is in Current Execution._

## Next Task

Current execution: Refactor Skills (P0). Child 01 completed. Remaining children are paused; no additional eligible child.

## Deferred Work

### Blocked

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261126-142500-03 | Fix lint tooling check: Markdown links and heading anchors | P0 | Blocked | Approved | The repository report JSON was read. It provides captured anchor diagnostics. Blocker status requires re-evaluation; captured diagnostics are available for remediation. | [03](tasks/20261126-142500/subtasks/03-ci-remediation-fix-lint-tooling-check-markdown-links-and-heading-anchors.md) |
| 20261126-142500-23 | Fix lint tooling check: Lint report regression tests | P0 | Blocked | Approved | The repository report JSON was read. It includes full output for both failed regression assertions. Blocker status requires re-evaluation; captured diagnostics are available for remediation. | [23](tasks/20261126-142500/subtasks/23-ci-remediation-fix-lint-tooling-check-lint-report-regression-tests.md) |

### Proposed — decision pending

_No proposed tasks._

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261127-173000-03 | Correct objective-based task parent selection | P1 | Paused | Approved | Reparented under Refactor Skills. Remaining audit is deferred behind P0 work. | [subtask](tasks/20261127-173000/subtasks/03-correct-objective-based-task-parent-selection.md) |
| 20261127-173000-02 | Consolidate specialist skills into The Worker | P1 | Paused | Approved | Refactor Skills child. Deferred behind P0 work. | [subtask](tasks/20261127-173000/subtasks/02-consolidate-specialist-skills-into-worker.md) |

### Dependency-waiting

_No dependency-waiting tasks._
