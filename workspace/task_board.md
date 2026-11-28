# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

_None. Template Fix is complete and its task records will be removed under the Worker lifecycle rules._

## Ordered Eligible Execution Queue

_No task is selected; no execution queue is active._

## Next Task

No task is selected. Other open parents remain unselected:

- **P1** — [Repair CI task generation and clear active reports](tasks/20261126-142500/task.md) — In Progress; not selected.
- **P0** — [Refactor Skills](tasks/20261127-173000/task.md) — Persistent parent at quiescence; no eligible child; not selected.

## Deferred Work

### Blocked

_No blocked subtasks._

### Proposed — decision pending

_No proposed tasks._

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

_No dependency-waiting tasks._
