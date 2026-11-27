# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](TASK_BOARD_TEMPLATE.md). Preserve its structure and scheduler contract.

## Scheduler contract

The Worker is the sole scheduler. This board publishes its current selection and ordered eligible queue. It is not a second scheduler. Compare the board with task records and child indexes before declaring the queue empty.

Check eligibility before priority or age. Dependencies must be satisfied, execution must be authorized, and status must be Ready. Rank eligible tasks by priority (P0 first), then age within the same priority unless a documented dependency or material constraint changes the order. Keep ineligible tasks out of the queue. List them in the appropriate deferred section with the exact reason.

**Approval:** Approved records explicit authorization for the documented scope or applicable standing authorization. Pending means the user has not authorized execution. Declined means the user rejected the proposal. Approval does not depend on status or eligibility.

This is the sole index of active task parents. Each parent folder contains `task.md` and `subtasks/README.md`. The parent index lists substantive children. Board links point to parents, except Current Execution may link to the selected child. Keep a parent open while a required child remains open. The Worker owns status, selection, and deletion at closeout.

## Current Execution

[20261127-173000-19: CI remediation — Review passive-voice findings in .agent/skills/asd-ste100/SKILL.md](tasks/20261127-173000/subtasks/19-ci-remediation-review-passive-voice-findings-in-agent-skills-asd-ste100-skill-m.md). This P0 child is active under the persistent Refactor Skills parent.

## Ordered Eligible Execution Queue

1. **P0** — [20261127-173000-50: CI remediation — Fix lint tooling check: Markdown links and heading anchors](tasks/20261127-173000/subtasks/50-ci-remediation-fix-lint-tooling-check-markdown-links-and-heading-anchors.md) — Approved, Ready, no dependencies.
2. **P1** — [20261127-173100-02: Audit document template coverage and create missing templates](tasks/20261127-173100/subtasks/02-audit-document-template-coverage.md) — Approved, Ready, no dependencies.
3. **P1** — [20261127-173000-04: Enforce template-first document editing](tasks/20261127-173000/subtasks/04-enforce-template-first-document-editing.md) — Approved, Ready, no dependencies.

## Next Task

[20261127-173000-50](tasks/20261127-173000/subtasks/50-ci-remediation-fix-lint-tooling-check-markdown-links-and-heading-anchors.md) is next after child 10 completes.

## Deferred Work

### Blocked

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261127-173000-20 | CI remediation — Review passive-voice findings in .agent/skills/the-worker/references/ci-ledger.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](20-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md) |
| 20261127-173000-21 | CI remediation — Review semicolon findings in workspace/README.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](21-ci-remediation-review-semicolon-findings-in-workspace-readme-md.md) |
| 20261127-173000-22 | CI remediation — Review synonym-rotation findings in .agent/skills/the-worker/references/github-actions.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](22-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-refe.md) |
| 20261127-173000-23 | CI remediation — Review long-sentence findings in .agent/skills/the-worker/SKILL.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](23-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-skill-m.md) |
| 20261127-173000-24 | CI remediation — Review passive-voice findings in .agent/skills/the-worker/references/document-type-catalog.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](24-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md) |
| 20261127-173000-26 | CI remediation — Review long-sentence findings in .agent/SESSION\\\_START.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](26-ci-remediation-review-long-sentence-findings-in-agent-session-start-md.md) |
| 20261127-173000-27 | CI remediation — Review passive-voice findings in workspace/README.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](27-ci-remediation-review-passive-voice-findings-in-workspace-readme-md.md) |
| 20261127-173000-28 | CI remediation — Review marketing-adjective findings in .agent/skills/asd-ste100/SKILL.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](28-ci-remediation-review-marketing-adjective-findings-in-agent-skills-asd-ste100-s.md) |
| 20261127-173000-29 | CI remediation — Review nominalization findings in .agent/skills/asd-ste100/SKILL.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](29-ci-remediation-review-nominalization-findings-in-agent-skills-asd-ste100-skill.md) |
| 20261127-173000-30 | CI remediation — Review present-perfect findings in .agent/skills/asd-ste100/SKILL.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](30-ci-remediation-review-present-perfect-findings-in-agent-skills-asd-ste100-skill.md) |
| 20261127-173000-31 | CI remediation — Review semicolon findings in .agent/skills/the-worker/references/document-type-catalog.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](31-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-references.md) |
| 20261127-173000-32 | CI remediation — Review long-sentence findings in .agent/skills/the-worker/references/github-actions.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](32-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-referen.md) |
| 20261127-173000-33 | CI remediation — Review present-perfect findings in .agent/SESSION\\\_START.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](33-ci-remediation-review-present-perfect-findings-in-agent-session-start-md.md) |
| 20261127-173000-34 | CI remediation — Review synonym-rotation findings in workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](34-ci-remediation-review-synonym-rotation-findings-in-workspace-adr-0003-canonical.md) |
| 20261127-173000-35 | CI remediation — Review semicolon findings in workspace/TASK\\\_TEMPLATE.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](35-ci-remediation-review-semicolon-findings-in-workspace-task-template-md.md) |
| 20261127-173000-36 | CI remediation — Review passive-voice findings in workspace/SUBTASK\\\_TEMPLATE.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](36-ci-remediation-review-passive-voice-findings-in-workspace-subtask-template-md.md) |
| 20261127-173000-37 | CI remediation — Review semicolon findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](37-ci-remediation-review-semicolon-findings-in-workspace-adr-0004-task-folders-sub.md) |
| 20261127-173000-38 | CI remediation — Review passive-voice findings in workspace/TASK\\\_TEMPLATE.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](38-ci-remediation-review-passive-voice-findings-in-workspace-task-template-md.md) |
| 20261127-173000-39 | CI remediation — Review synonym-rotation findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](39-ci-remediation-review-synonym-rotation-findings-in-workspace-adr-0004-task-fold.md) |
| 20261127-173000-40 | CI remediation — Review passive-voice findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](40-ci-remediation-review-passive-voice-findings-in-workspace-adr-0004-task-folders.md) |
| 20261127-173000-41 | CI remediation — Review long-sentence findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](41-ci-remediation-review-long-sentence-findings-in-workspace-adr-0004-task-folders.md) |
| 20261127-173000-42 | CI remediation — Review passive-voice findings in workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](42-ci-remediation-review-passive-voice-findings-in-workspace-adr-0001-establish-dr.md) |
| 20261127-173000-43 | CI remediation — Review semicolon findings in workspace/SUBTASK\\\_TEMPLATE.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](43-ci-remediation-review-semicolon-findings-in-workspace-subtask-template-md.md) |
| 20261127-173000-44 | CI remediation — Review semicolon findings in workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](44-ci-remediation-review-semicolon-findings-in-workspace-adr-0001-establish-draft.md) |
| 20261127-173000-45 | CI remediation — Review semicolon findings in workspace/adr/README.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](45-ci-remediation-review-semicolon-findings-in-workspace-adr-readme-md.md) |
| 20261127-173000-46 | CI remediation — Review passive-voice findings in .agent/skills/the-worker/references/conversation-mode.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](46-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md) |
| 20261127-173000-47 | CI remediation — Review passive-voice findings in .agent/skills/asd-ste100/references/repository-writing-policy.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](47-ci-remediation-review-passive-voice-findings-in-agent-skills-asd-ste100-referen.md) |
| 20261127-173000-48 | CI remediation — Review synonym-rotation findings in .agent/skills/agent-skill-authoring/SKILL.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](48-ci-remediation-review-synonym-rotation-findings-in-agent-skills-agent-skill-aut.md) |
| 20261127-173000-49 | CI remediation — Review passive-voice findings in workspace/task\\\_board.md | P0 | Blocked | Approved | Complete CI Ledger content is unavailable. The connector returns an empty body, so evidence review and Ledger resolution cannot proceed safely. | [subtask](49-ci-remediation-review-passive-voice-findings-in-workspace-task-board-md.md) |

### Proposed — decision pending

_No proposed tasks._

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261127-173000-03 | Correct objective-based task parent selection | P1 | Paused | Approved | Remaining audit is deferred behind the current Refactor Skills consolidation. | [subtask](tasks/20261127-173000/subtasks/03-correct-objective-based-task-parent-selection.md) |

### Dependency-waiting

_No dependency-waiting tasks._
