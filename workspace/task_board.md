# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

**20261126-142500 — Repair CI task generation and clear active reports** (P1, In Progress, Approved) — [task](tasks/20261126-142500/task.md)

## Ordered Eligible Execution Queue

_None._

## Next Task

_None._

## Deferred Work

### Current focus reconciliation

The current authorized focus is CI task lifecycle repair under 20261126-142500. Implementation of the newly approved folder-based CI lifecycle is pending the required superseding decision and canonical subtask-folder format update. The report-directory deletion target also requires path clarification.

### Blocked

_None._

### Proposed — decision pending

**DRAFT-0010 — CI Error Task Folders and Automatic Feedback Loop.** Revision 1, draft; exact report path confirmation and formal decision review pending.

**DRAFT-0009 — Project, Task, and Knowledge Lifecycle.** Proposal in review; no implementation authorization.

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

_None._
