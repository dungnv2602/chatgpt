# Task Board

## Scheduler contract

The Worker is the sole scheduler. This board publishes the Worker's current selection and ordered eligible queue; it is not a second scheduler. Reconcile the board against the task records and child indexes before declaring the queue empty.

Eligibility is checked before priority and age: dependencies must be satisfied, execution authorized, and status Ready. Ready tasks are ranked by priority (P0 first), then age within equal priority unless a documented dependency or material constraint changes ordering. Ineligible tasks must not appear in the queue; list them under the appropriate deferred section with the precise reason.

**Approval:** Approved records explicit authorization for the documented scope or applicable standing authorization. Pending means execution authorization is not granted; Declined means rejected. Approval is independent of status and eligibility.

This is the single index of active task parents. Every parent folder contains `task.md` and `subtasks/README.md`; substantive children are listed in the parent index. Board links point to parent tasks, except Current Execution may point directly to the selected child. The parent cannot be Done while a required child remains open. The Worker owns status, selection, and direct deletion at closeout.

## Current Execution

[20261126-142500-04 — Review semicolon findings in .agent/skills/github-actions/SKILL.md](tasks/20261126-142500/subtasks/04-ci-remediation-review-semicolon-findings-in-agent-skills-github-actions-skill-m.md)

Parent: [20261126-142500 — Repair CI task generation and clear active reports](tasks/20261126-142500/task.md)

## Ordered Eligible Execution Queue

<text>Ordered by the Worker. P0 tasks precede lower priorities; age breaks ties among eligible tasks.</text>

| Rank | ID | Title | Priority | Status | Approval | Record |
|---:|---|---|---|---|---|---|
| 1 | 20261126-142500-04 | Review semicolon findings in .agent/skills/github-actions/SKILL.md | P0 | Ready | Approved | [04](tasks/20261126-142500/subtasks/04-ci-remediation-review-semicolon-findings-in-agent-skills-github-actions-skill-m.md) |
| 2 | 20261126-142500-05 | Review semicolon findings in .agent/skills/the-worker/SKILL.md | P0 | Ready | Approved | [05](tasks/20261126-142500/subtasks/05-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-skill-md.md) |
| 3 | 20261126-142500-06 | Review passive-voice findings in .agent/skills/the-worker/SKILL.md | P0 | Ready | Approved | [06](tasks/20261126-142500/subtasks/06-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-skill-m.md) |
| 4 | 20261126-142500-07 | Review present-perfect findings in conversation-mode reference | P0 | Ready | Approved | [07](tasks/20261126-142500/subtasks/07-ci-remediation-review-present-perfect-findings-in-agent-skills-the-worker-refer.md) |
| 5 | 20261126-142500-08 | Review long-sentence findings in .agent/skills/github-actions/SKILL.md | P0 | Ready | Approved | [08](tasks/20261126-142500/subtasks/08-ci-remediation-review-long-sentence-findings-in-agent-skills-github-actions-ski.md) |
| 6 | 20261126-142500-09 | Review synonym-rotation findings in .agent/skills/github-actions/SKILL.md | P0 | Ready | Approved | [09](tasks/20261126-142500/subtasks/09-ci-remediation-review-synonym-rotation-findings-in-agent-skills-github-actions.md) |
| 7 | 20261126-142500-10 | Review semicolon findings in workspace/task_board.md | P0 | Ready | Approved | [10](tasks/20261126-142500/subtasks/10-ci-remediation-review-semicolon-findings-in-workspace-task-board-md.md) |
| 8 | 20261126-142500-11 | Review synonym-rotation findings in .agent/skills/the-worker/SKILL.md | P0 | Ready | Approved | [11](tasks/20261126-142500/subtasks/11-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-skil.md) |
| 9 | 20261126-142500-12 | Review present-perfect findings in workspace/task_board.md | P0 | Ready | Approved | [12](tasks/20261126-142500/subtasks/12-ci-remediation-review-present-perfect-findings-in-workspace-task-board-md.md) |
| 10 | 20261126-142500-13 | Review passive-voice findings in .agent/skills/ci-ledger/SKILL.md | P0 | Ready | Approved | [13](tasks/20261126-142500/subtasks/13-ci-remediation-review-passive-voice-findings-in-agent-skills-ci-ledger-skill-md.md) |
| 11 | 20261126-142500-14 | Review long-sentence findings in .agent/skills/the-worker/SKILL.md | P0 | Ready | Approved | [14](tasks/20261126-142500/subtasks/14-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-skill-m.md) |
| 12 | 20261126-142500-15 | Review semicolon findings in conversation-mode reference | P0 | Ready | Approved | [15](tasks/20261126-142500/subtasks/15-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-references.md) |
| 13 | 20261126-142500-16 | Review synonym-rotation findings in .agent/skills/ci-ledger/SKILL.md | P0 | Ready | Approved | [16](tasks/20261126-142500/subtasks/16-ci-remediation-review-synonym-rotation-findings-in-agent-skills-ci-ledger-skill.md) |
| 14 | 20261126-142500-17 | Review long-sentence findings in conversation-mode reference | P0 | Ready | Approved | [17](tasks/20261126-142500/subtasks/17-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-referen.md) |
| 15 | 20261126-142500-18 | Review passive-voice findings in workspace/task_board.md | P0 | Ready | Approved | [18](tasks/20261126-142500/subtasks/18-ci-remediation-review-passive-voice-findings-in-workspace-task-board-md.md) |
| 16 | 20261126-142500-19 | Review semicolon findings in .agent/skills/ci-ledger/SKILL.md | P0 | Ready | Approved | [19](tasks/20261126-142500/subtasks/19-ci-remediation-review-semicolon-findings-in-agent-skills-ci-ledger-skill-md.md) |
| 17 | 20261126-142500-20 | Review passive-voice findings in conversation-mode reference | P0 | Ready | Approved | [20](tasks/20261126-142500/subtasks/20-ci-remediation-review-passive-voice-findings-in-workspace-task-board-md.md) |

## Next Task

[20261126-142500-04](tasks/20261126-142500/subtasks/04-ci-remediation-review-semicolon-findings-in-agent-skills-github-actions-skill-m.md) — P0, Ready, Approved.

## Deferred Work

### Blocked

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261126-142500-03 | Fix lint tooling check: Markdown links and heading anchors | P0 | Blocked | Approved | Immutable report evidence was unavailable through remote readback; do not infer a fix or substitute hosted result review. | [03](tasks/20261126-142500/subtasks/03-ci-remediation-fix-lint-tooling-check-markdown-links-and-heading-anchors.md) |

### Proposed — decision pending

_No proposed tasks._

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261126-142500-22 | Consolidate Document Standards into The Worker | P1 | In Progress | Approved | Supporting consolidation work; current CI P0 queue remains scheduled first. | [22](tasks/20261126-142500/subtasks/22-consolidate-document-standards-into-worker.md) |

### Paused

_No paused tasks._

### Dependency-waiting

_No dependency-waiting tasks._
