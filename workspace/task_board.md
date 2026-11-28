# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and scheduler contract.

## Scheduler contract

Follow the Worker's scheduling and decision-collection procedure. This board publishes state and does not define operating rules.

The Worker is the sole scheduler. This board publishes its current selection and ordered eligible queue. It is not a second scheduler. Compare the board with task records and child indexes before declaring the queue empty.

Check eligibility before priority or age. Dependencies must be satisfied, execution must be authorized, and status must be Ready. Rank eligible tasks by priority (P0 first), then age within the same priority unless a documented dependency or material constraint changes the order. Keep ineligible tasks out of the queue. List them in the appropriate deferred section with the exact reason.

After every task completion, blocker, pause, cancellation, approval change, or dependency change, the Worker must reconcile records and rebuild the full eligible queue. A blocked task does not stop execution while an independent eligible task remains. Quiescence means no eligible task remains within the user's authorized focus. At quiescence, follow The Worker's decision-collection phase. Record all user calls before batching work they unlock. Await the explicit, case-insensitive `execute` cue before starting the prepared batch.

**Approval:** Approved records explicit authorization for the documented scope or applicable standing authorization. Pending means the user has not authorized execution. Declined means the user rejected the proposal. Approval does not depend on status or eligibility. Approval is log-only, not execution authorization. Execution requires the explicit standalone `execute` cue, case-insensitive, after decision collection. `Next` only navigates the decision queue.

This is the sole index of active task parents. Each parent folder contains `task.md` and `subtasks/README.md`. The parent index lists substantive children. Board links point to parents, except Current Execution may link to the selected child. Keep a parent open while a required child remains open. The Worker owns status, selection, and deletion at closeout.

## Current Execution

_None. Template Fix is complete and its task folder will be removed under normal lifecycle rules. No task is selected._

## Ordered Eligible Execution Queue

_No task is selected in this execution batch._

## Next Task

No task is selected. Other open parents remain unselected:

- [Repair CI task generation and clear active reports](tasks/20261126-142500/task.md) — P1, In Progress. Its child 02 is active outside this batch.
- [Refactor Skills](tasks/20261127-173000/task.md) — Persistent P0 parent at quiescence. No eligible child remains.

## Deferred Work

### Blocked

_No blocked subtasks._

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

_No dependency-waiting tasks._
