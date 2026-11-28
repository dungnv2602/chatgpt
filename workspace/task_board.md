# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

**20261127-173000-75 — Universal execution cue and authorization lifecycle hardening**

## Ordered Eligible Execution Queue

_Authorized current task: child 75, approved execution-cue lifecycle hardening._

## Next Task

Child 75 — Universal execution cue and authorization lifecycle hardening.

## Deferred Work

### Current focus reconciliation

The Worker skill-governance prevention correction completed under child 74. Child 75 is the current focused workflow correction under the persistent Refactor Skills parent. ADR-0008 implementation under **20261128-230000** is temporarily unselected; resume after child 75 closeout. Operational activation gates remain separate from implementation availability. Preserve `.takeout/reports/` until migration and Confirmation gates are satisfied. The permanent system-owned CI fallback parent is [20261128-193800](tasks/20261128-193800/task.md); it is never selected as Current Execution and must never be deleted.

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
