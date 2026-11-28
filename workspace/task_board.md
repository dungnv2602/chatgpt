# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

_None. ADR-0008 implementation is blocked by external repository settings._

## Ordered Eligible Execution Queue

_None. No eligible task remains in the authorized focus._

## Next Task

_None within the authorized focus._

## Deferred Work

### Current focus reconciliation

The Worker skill-governance prevention correction completed under child 74 of the persistent Refactor Skills parent. That parent remains open. ADR-0008 implementation remains authorized under **20261128-230000** but is not Current Execution while external activation prerequisites are unmet. Preserve `.takeout/reports/` until migration and Confirmation gates are satisfied. The permanent system-owned CI fallback parent is [20261128-193800](tasks/20261128-193800/task.md); it is never selected as Current Execution and must never be deleted.

### Blocked

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-230000 | ADR 8 implementation | P1 | Blocked | Approved | Default branch is `main` and lacks the dispatcher/recovery workflows; effective branch protection is unverified. | [task](tasks/20261128-230000/task.md) |
| 20261128-230000-04 | Worker queue, review/remediation lifecycle, attribution, grouping, and report migration | P1 | Blocked | Approved | Exact-SHA validation awaits dispatcher/recovery availability on the default branch and verified branch protection. | [subtask](tasks/20261128-230000/subtasks/04-worker-migration.md) |

### Proposed — decision pending

**DRAFT-0009 — Project, Task, and Knowledge Lifecycle.** Proposal in review; no implementation authorization.

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

| ID | Title | Priority | Status | Approval | Dependencies | Task record |
|---|---|---:|---|---|---|---|
| 20261128-230000-05 | Operational Confirmation, scenario demonstrations, coverage reconciliation, and gated retirement | P1 | Ready | Approved | 20261128-230000-02; 20261128-230000-03; 20261128-230000-04 | [task](tasks/20261128-230000/subtasks/05-confirmation-retirement.md) |
