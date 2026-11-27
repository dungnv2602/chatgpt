# Workspace

The Worker owns task capture, hierarchy, scheduling, progress, handoff, closeout, and document governance.

## Files

| Path | Purpose |
|---|---|
| [discussion.md](discussion.md) | Current step, open decisions, and three latest success reports |
| [DISCUSSION_TEMPLATE.md](../.agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md) | Canonical discussion-register structure and entry conventions |
| [task_board.md](task_board.md) | Current execution, eligible queue, next task, and deferred work |
| [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md) | Canonical task-board structure and scheduler contract |
| [TASK_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_TEMPLATE.md) | Parent task folder |
| [SUBTASK_TEMPLATE.md](../.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md) | Follow-up and remediation child |
| [ADR_TEMPLATE.md](../.agent/skills/the-worker/assets/ADR_TEMPLATE.md) | Accepted decision record |
| [ANALYSIS_TEMPLATE.md](../.agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md) | Repository analysis |
| [DRAFT_TEMPLATE.md](../.agent/skills/the-worker/assets/DRAFT_TEMPLATE.md) | Proposed decision draft |
| [tasks/](tasks/) | Active task folders. Each folder has task.md and subtasks/README.md |
| [draft/](draft/README.md) | Decision proposals |
| [adr/](adr/README.md) | Accepted decisions |
| [analysis/](analysis/README.md) | Evidence-based repository analysis |
| [../.takeout/reports/README.md](../.takeout/reports/README.md) | Lint, Actions, and Ledger navigation |

## Task lifecycle

1. Before substantive work, inspect active tasks and capture the actionable prompt verbatim.
2. A new objective creates a parent task. A substantive follow-up, correction, or scope extension creates its own subtask under the genuine parent. Clarifications and approvals with no independent deliverable are recorded verbatim as subsequent instructions. Greetings and acknowledgements need no task.
3. Split independent objectives. Do not attach unrelated requests to one parent. Do not guess parentage. Record uncertain requests and resolve attribution at quiescence.
4. Keep parent and child indexes current. The Worker alone schedules and updates `task_board.md`.
5. Record commits, readback, checks, decisions, and limitations. Every task-specific implementation commit includes `Task-ID: <task-id>`.
6. A parent cannot be Done while a required child is open. After closeout, delete the complete task folder and board row. Do not archive or retain a copy.

Approval is scope authorization, not status. Use Proposed only when a required decision or authorization is genuinely pending. P0 does not bypass a real decision gate.

## Decision records

Use a Draft for a proposed decision. Do not implement the proposal before approval. After approval, promote it to an accepted ADR only after the full rationale and completeness review. Keep accepted ADRs in `workspace/adr/`. Do not create archive folders or historical copies.

## CI lifecycle

Report evidence must identify the task that caused the run. Worker commits carry a `Task-ID:` trailer. The Ledger resolves a parent ID directly or resolves a child ID through its Parent Task ID. It creates P0, Approved, Ready remediation children under that genuine user task. It never creates a CI work-target parent or changes the board/current execution pointer.

If attribution is missing, invalid, inactive, or points to a deleted task, keep the finding in the Ledger as unassigned. Do not infer a parent from filenames, workflow, branch, current execution, or timing. The Worker can resolve attribution when reliable evidence becomes available.

Lint baselines, finding identity, grouped remediation, bounded evidence, and occurrence history prevent repeat reports from flooding the queue. The same active finding group under the same parent reuses its child. A recurrence after resolution preserves history and creates/reuses a follow-up under the task identified by that run's commit.

The Ledger owns finding state and child evidence. The Worker owns task status, selection, approval checks, parent/child completion, and direct deletion. CI remediation closes after the intended-branch commit is verified. Hosted validation is optional metadata. Do not inspect hosted results unless the user explicitly asks.

See [The Worker](../.agent/skills/the-worker/SKILL.md), [CI Ledger reference](../.agent/skills/the-worker/references/ci-ledger.md), [GitHub Actions reference](../.agent/skills/the-worker/references/github-actions.md), [decision-governance reference](../.agent/skills/the-worker/references/decision-governance.md), and [.takeout report navigation](../.takeout/reports/README.md).
