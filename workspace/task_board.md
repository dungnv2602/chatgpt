# Task Board

## Scheduler contract

The Worker is the sole scheduler. This board publishes the Worker's current selection and ordered candidates. It does not independently calculate or override working order.

The Worker selects by eligibility first. It then respects dependencies, priority, and age. Only eligible tasks appear in the execution queue. Deferred work stays outside that queue and includes its reason.

**Approval column:** Approved records explicit authorization for the task's documented scope or applicable standing authorization. Pending means execution authorization is not granted; Declined means the scope was rejected. Approval is independent of status and eligibility. Record approval scope/source in task records.

This file is the single index for active task records. Each active task is a folder that contains task.md and subtasks/README.md. Child records live under subtasks/. Board links point to parent task.md. The parent cannot be Done while any required child remains open. The Worker owns task status, selection, and direct deletion at closeout.

## Current Execution

[20261126-142500 — Repair CI task generation and clear active reports](tasks/20261126-142500/task.md)

## Ordered Eligible Execution Queue

<text>Ranked by the Worker's scheduler. Only eligible candidates are listed.</text>

_No eligible tasks. The board was reconciled after the ADR editorial commits and cancellation/deletion of search task 20261126-090154. Any deferred work must be listed by its exact task record and reason; no cancelled task is queued._

## Next Task

<text color="success" weight="medium">None — the eligible queue is empty.</text>

## Deferred Work

### Proposed — governance decision pending

These editorial P0 groups have been remediated and removed at direct closeout. Ledger findings retain stable identities, resolution history, task references, and commit evidence. Hosted validation is optional and is not reviewed.

| ID | Title | Priority | Status | Approval | ADR(s) | Task record |
|---|---|---:|---|---|---|---|

_No proposed editorial remediation groups remain._

### Paused

| ID | Title | Priority | Status | Approval | Task record |
|---|---|---:|---|---|---|
_No tasks currently paused._

### Dependency-waiting

_No tasks currently listed. The Worker reevaluates these tasks after prerequisite completion. They are not queue candidates._

#
