# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

**20261128-230000 — ADR 8 implementation**

## Ordered Eligible Execution Queue

_Authorized current task: subtask 04, ADR-0008 implementation._

## Next Task

Subtask 04 — Worker queue, review/remediation lifecycle, attribution, grouping, and report migration.

## Deferred Work

### Current focus reconciliation

The Worker skill-governance prevention correction completed under child 74. Child 75's implementation is readback-verified and awaiting exact-SHA CI reconciliation; no permitted CI review was performed. ADR-0008 implementation under **20261128-230000** is restored as Current Execution. Child 75 remains tracked under the persistent Refactor Skills parent, pending validation lifecycle reconciliation. Operational activation gates remain separate from implementation availability. Preserve `.takeout/reports/` until migration and Confirmation gates are satisfied. The permanent system-owned CI fallback parent is [20261128-193800](tasks/20261128-193800/task.md); it is never selected as Current Execution and must never be deleted.

### Blocked

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| None | — | — | — | — | No blocked work currently identified. | — |

### Proposed — decision pending

**DRAFT-0009 — Project, Task, and Knowledge Lifecycle.** Proposal in review; no implementation authorization.

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

| ID | Title | Priority | Status | Approval | Dependencies | Task record |
|---|---|---:|---|---|---|---|
| 20261128-230000-05 | Operational Confirmation, scenario demonstrations, coverage reconciliation, and gated retirement | P1 | Dependency-waiting | Approved | 20261128-230000-02; 20261128-230000-03; 20261128-230000-04 | [task](tasks/20261128-230000/subtasks/05-confirmation-retirement.md) |
