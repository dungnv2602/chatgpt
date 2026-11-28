# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

- **20261128-230000 — ADR 8 implementation** — P1, In Progress, Approved. [Task](tasks/20261128-230000/task.md)

## Ordered Eligible Execution Queue

_None. Current execution is active._

## Next Task

- **20261128-230000 — ADR 8 implementation** — Current implementation parent. [Task](tasks/20261128-230000/task.md)

## Deferred Work

### Current focus reconciliation

ADR-0008 implementation is tracked under current task **20261128-230000**. The previous task 20261126-142500 was administratively superseded and deleted; no implementation acceptance or successful validation was claimed. Preserve .takeout/reports until migration and Confirmation gates are satisfied.

### Blocked

_None._

### Proposed — decision pending

**DRAFT-0009 — Project, Task, and Knowledge Lifecycle.** Proposal in review; no implementation authorization.

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

_None._
