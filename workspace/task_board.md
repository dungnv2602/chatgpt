# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

- **20261126-142500 — Repair CI task generation and clear active reports** — P1, In Progress, Approved. [Task](tasks/20261126-142500/task.md)

## Ordered Eligible Execution Queue

_None. Current execution is active._

## Next Task

_Current execution remains active._

## Deferred Work

### Current focus reconciliation

Accepted [ADR-0008](adr/0008-ci-validation-error-tasks-and-automatic-feedback-loop.md) governs task 20261126-142500. Its implementation remains in progress, and the parent is not operationally accepted. Preserve the current report pipeline until the replacement passes ADR-0008 Confirmation and every producer/consumer has migrated. Completed child records were removed during lifecycle cleanup; the remaining objective is migration and Confirmation.

### Blocked

_None._

### Proposed — decision pending

~~20261126-142500 — Repair CI task generation and clear active reports.~~ Removed from Proposed after execution authorization. — [task](tasks/20261126-142500/task.md)

**DRAFT-0009 — Project, Task, and Knowledge Lifecycle.** Proposal in review; no implementation authorization.

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

_None._
