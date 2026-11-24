# Workspace

The workspace is the task-management and conversation-navigation area. The Worker owns task records, selection, progress, handoffs, archive closeout, and the shared discussion register. Document Standards governs workspace document formats.

## Files

| Path | Purpose |
|---|---|
| [discussion.md](discussion.md) | Current-step brief, open discussions, and the three latest verified success reports |
| [task_board.md](task_board.md) | Task index, priorities, states, and current execution |
| [TASK_TEMPLATE.md](TASK_TEMPLATE.md) | Canonical task-record format |
| [tasks/](tasks/) | Active task records |
| [draft/](draft/README.md) | Proposals awaiting user review and decision |
| [adr/](adr/README.md) | Accepted decisions awaiting implementation and confirmation |
| [analysis/](analysis/README.md) | Evidence-based repository analysis snapshots |
| [../reports/README.md](../reports/README.md) | Lint, Actions, and issue-ledger navigation |
| [../archive/README.md](../archive/README.md) | Archive and retention policy |

## Draft and ADR workflow

Use a Draft to present a proposal. Do not implement a proposed decision.

After the user approves the exact Draft, create its accepted ADR. Preserve the Draft and link it to the ADR.

Every new implementation task must reference one or more accepted ADRs. Keep the task's execution approval separate from the ADR's decision approval.

When all implementation tasks and the ADR's confirmation checks pass, move the ADR to `archive/adr/`. Keep archived ADRs permanently. Never add them to the 90-day task/report retention index.

The decision-governance skill owns Draft, ADR, and repository-analysis lifecycles. Load it only when a task requires decision governance. Do not add it to foundational initialization.

## Task workflow

1. Check the board and active records before creating work. Update an existing task when the objective continues; otherwise create a distinct task.
2. Record the user's request, scope, constraints, approval, priority, dependencies, and acceptance criteria.
3. Select one current execution task. Follow explicit user direction, then dependencies, priority, and age.
4. Record meaningful actions, decisions, verification, and blockers in the task record. Keep the board as an index.
5. Close only after acceptance criteria pass, the archive copy is created and read back, the retention index is updated, the active record is removed, and the board links to the archive commit.

Task IDs use UTC `YYYYMMDD-HHMMSS`. Use only the statuses Proposed, Ready, In Progress, Blocked, Paused, Done, and Cancelled. Optional assistant improvements remain Proposed until approved. Necessary follow-ups may be created automatically within the approved scope.

## CI issue workflow

GitHub Actions publishes diagnostic evidence into the lint and Actions report families. The event-driven Ledger creates grouped Proposed tasks for newly identified actionable findings and links them through `task_refs`. The Worker retains prioritization, approval, remediation, verification, and closeout.

The first complete tooling-valid full audit in each lint scope establishes a baseline without creating tasks. Later runs create tasks only for genuinely new actionable findings. Recurring untracked baseline findings do not flood the backlog. The Ledger retains at most five evidence paths per finding while preserving cumulative occurrence counts.

A lint report can seed a baseline when every required tooling check passes, even when the report records lint failures. The baseline prevents recurring findings from appearing as new work.

A Ledger-generated task cannot close as Done while any linked finding remains non-terminal. After the task is archived Done and indexed, the `archive/tasks/**` push triggers the normal diagnostics sweep. The Ledger then retires the terminal findings from the active backlog. The archived task and its archived report references preserve the audit history. Do not delete Ledger entries manually or run periodic retirement scans.

A clean-start reset is destructive and requires explicit user authorization. It clears generated active report data, prior `archive/reports/**` snapshots, report indexes, and the active Ledger, then establishes new unseeded lint baselines. It preserves scripts, schemas, templates, workflows, operating guides, task archives, and unrelated tasks. See `reports/triage/README.md` and `archive/README.md` for exact reset and closeout rules.

Do not run periodic triage or poll workflows. Review CI when the user asks, a known failure blocks work, or the task requires validation. A successful validation run URL and UTC timestamp are sufficient resolution evidence; capture a full successful-run diagnostic report only when its detailed evidence is specifically required.

The changed-document lint workflow uses GitHub Actions concurrency to cancel superseded push runs. Do not add a separate run-list preflight guard. GitHub may not list the current run when its first job queries the run list, which can cause the guard to cancel the current run.

## Discussion register

The Worker maintains [discussion.md](discussion.md) in both conversation modes. Its Conversation Mode reference defines the section order, pre-step brief, open-discussion lifecycle, and three-report limit. Keep technical progress and handoffs in task records, not in the register.

## Recovery

Read this file, the board, and the selected task record. Check the current `gpt` repository state before resuming. Follow the task's Next Actions. Reconcile discrepancies against the latest user instruction and committed repository state.