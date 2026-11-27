# Task Board

The Worker is the sole scheduler. This board publishes its current selection and ordered eligible queue. It is not a second scheduler.

## Scheduler contract

- Compare the board with active task records and child indexes before declaring the queue empty.
- Check eligibility before priority or age. Dependencies must be satisfied, execution must be authorized, and status must be Ready.
- Rank eligible tasks by priority (P0 first), then age within priority unless a documented dependency or material constraint changes the order.
- Keep ineligible tasks out of the eligible queue. List them in the appropriate deferred section with an exact reason.
- Approval is explicit scope authorization. Pending means authorization is not granted; Declined means rejected. Approval does not depend on status or eligibility.
- This board is the sole index of active task parents. Parent folders contain `task.md` and `subtasks/README.md`. The parent index lists substantive children. Board links point to parents, except Current Execution may link to the selected child.
- Keep a parent open while required children remain open. The Worker owns status, selection, and deletion at closeout.

## Current Execution

[One selected task/child, or _None._]

## Ordered Eligible Execution Queue

[Ordered list of all eligible Ready, approved tasks with dependencies satisfied, or _No eligible tasks._]

## Next Task

[Next task when execution is occupied or selection is deferred; otherwise _None._]

## Deferred Work

### Blocked

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| [Populate rows, or _No blocked tasks._] |

### Proposed — decision pending

[List tasks requiring approval/decision, or _No proposed tasks._]

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| [Populate rows, or _No paused tasks._] |

### Dependency-waiting

[List tasks waiting on prerequisites that are not external blockers, or _No dependency-waiting tasks._]

## Template usage

Canonical template: [TASK_BOARD_TEMPLATE.md](TASK_BOARD_TEMPLATE.md). Keep section order and required fields. Replace placeholders with current verified state; omit unused table rows and use explicit empty-state statements. The board is a publication of Worker selection, not a parallel scheduler.
