# Task Board

## Scheduler contract

The Worker is the sole scheduler. This board publishes the Worker's current selection and ordered candidates. It does not independently calculate or override working order.

The Worker selects by eligibility first. It then respects dependencies, priority, and age. Only eligible tasks appear in the execution queue. Deferred work stays outside that queue and includes its reason.

**Approval column:** Approved records explicit authorization for the task's documented scope or applicable standing authorization. Pending means execution authorization is not granted; Declined means the scope was rejected. Approval is independent of status and eligibility. Record approval scope/source in task records.

This file is the single index for active task records. Each active task is a folder that contains task.md and subtasks/README.md. Child records live under subtasks/. Board links point to parent task.md. The parent cannot be Done while any required child remains open. The Worker owns task status, selection, and direct deletion at closeout.

## Current Execution

_No task currently executing._

## Ordered Eligible Execution Queue

<text>Ranked by the Worker's scheduler. Only eligible candidates are listed.</text>

_No eligible tasks. The board was reconciled after the ADR editorial commits and cancellation/deletion of search task 20261126-090154. Remaining work is deferred by ADR-governance records or user-triggered external-review gates; no cancelled task is queued._

## Next Task

<text color="success" weight="medium">None — the eligible queue is empty.</text>

## Deferred Work

### Proposed — governance decision pending

These approved P0 task groups remain Proposed because accepted ADR coverage is pending. Do not select them until governance permits execution.

| ID | Title | Priority | Status | Approval | ADR(s) | Task record |
|---|---|---:|---|---|---|---|
| 20261127-013151-34 | Review present-perfect findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Proposed | Approved | Pending | [Task record](tasks/20261127-013151-34/task.md) |
| 20261127-013151-33 | Review synonym-rotation findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Proposed | Approved | Pending | [Task record](tasks/20261127-013151-33/task.md) |
| 20261127-013151-32 | Review semicolon findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Proposed | Approved | Pending | [Task record](tasks/20261127-013151-32/task.md) |
| 20261127-013151-31 | Review passive-voice findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Proposed | Approved | Pending | [Task record](tasks/20261127-013151-31/task.md) |
| 20261127-013151-30 | Review long-sentence findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Proposed | Approved | Pending | [Task record](tasks/20261127-013151-30/task.md) |
| 20261126-170259-02 | Review semicolon findings in workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | P0 | Proposed | Approved | Pending | [Task record](tasks/20261126-170259-02/task.md) |
| 20261126-170259-01 | Review passive-voice findings in workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | P0 | Proposed | Approved | Pending | [Task record](tasks/20261126-170259-01/task.md) |
| 20261126-170259 | Review synonym-rotation findings in workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | P0 | Proposed | Approved | Pending | [Task record](tasks/20261126-170259/task.md) |

### Paused

| ID | Title | Priority | Status | Approval | Task record |
|---|---|---:|---|---|---|
| 20261126-142500 | Resolve CI task generation and clear active reports | P1 | Paused | Approved | [Task record](tasks/20261126-142500/task.md) |

### Dependency-waiting

_No tasks currently listed. The Worker reevaluates these tasks after prerequisite completion. They are not queue candidates._

### In Progress — awaiting external/user-triggered review

This work is not the Current Execution pointer and is not selectable until its outstanding gate is satisfied.

| ID | Title | Priority | Status | Approval | ADR(s) | Outstanding gate | Task record |
|---|---|---:|---|---|---|---|---|
| 20261126-232913 | Implement ADR-0004 task folders and CI Ledger lifecycle | P0 | In Progress | Approved | ADR-0004 | Criterion 15 awaits user-triggered hosted Ledger regression and Document Type Catalog results review | [Task record](tasks/20261126-232913/task.md) |

