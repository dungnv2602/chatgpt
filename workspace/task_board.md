# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

- **20261128-230000 — ADR 8 implementation** — P1, In Progress, Approved. [task](tasks/20261128-230000/task.md)

## Ordered Eligible Execution Queue

_None. Current execution is active._

## Next Task

- **20261128-230000 — ADR 8 implementation** — Current execution. [task](tasks/20261128-230000/task.md)

## Deferred Work

### Current focus reconciliation

The Worker skill-governance prevention correction completed under child 74 of the persistent Refactor Skills parent. That parent remains open. ADR-0008 implementation is again the current execution under **20261128-230000**. Preserve .takeout/reports until migration and Confirmation gates are satisfied.

### Blocked

_None._

### Proposed — decision pending

**DRAFT-0009 — Project, Task, and Knowledge Lifecycle.** Proposal in review; no implementation authorization.

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

| ID | Title | Priority | Status | Approval | Dependencies | Task record |
|---|---|---:|---|---|---|---|
| 20261128-230000-04 | Worker queue, review/remediation lifecycle, attribution, grouping, and report migration | P1 | Ready | Approved | 20261128-230000-02 | [task](tasks/20261128-230000/subtasks/04-worker-migration.md) |
| 20261128-230000-05 | Operational Confirmation, scenario demonstrations, coverage reconciliation, and gated retirement | P1 | Ready | Approved | 20261128-230000-02; 20261128-230000-03; 20261128-230000-04 | [task](tasks/20261128-230000/subtasks/05-confirmation-retirement.md) |
