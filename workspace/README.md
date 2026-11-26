# Workspace

The workspace is the task-management and conversation-navigation area. The Worker owns task records, selection, progress, handoffs, archive closeout, and the shared discussion register. Document Standards governs workspace document formats.

## Files

| Path | Purpose |
|---|---|
| [discussion.md](discussion.md) | Current-step brief, open discussions, and the three latest verified success reports |
| [task_board.md](task_board.md) | Task index, priorities, states, and current execution |
| [TASK_TEMPLATE.md](TASK_TEMPLATE.md) | Canonical parent task-folder record format |
| [SUBTASK_TEMPLATE.md](SUBTASK_TEMPLATE.md) | Canonical child subtask format |
| [DRAFT_TEMPLATE.md](DRAFT_TEMPLATE.md) | Canonical decision-draft format |
| [ADR_TEMPLATE.md](ADR_TEMPLATE.md) | Canonical decision-record format |
| [ANALYSIS_TEMPLATE.md](ANALYSIS_TEMPLATE.md) | Canonical repository-analysis format |
| [tasks/](tasks/) | Active task folders; each contains task.md and subtasks/ |
| [draft/](draft/README.md) | Proposals awaiting user review and decision |
| [adr/](adr/README.md) | Accepted decisions awaiting implementation and confirmation |
| [analysis/](analysis/README.md) | Evidence-based repository analysis snapshots |
| [../.takeout/reports/README.md](../.takeout/reports/README.md) | Lint, Actions, and issue-ledger navigation |
| [../.archive/README.md](../.archive/README.md) | Archive and retention policy |

## Draft and ADR workflow

Use a Draft to present a proposal. Do not implement a proposed decision.

After the user approves the exact Draft, create a provisional ADR with status promotion-pending. Compare the complete ADR with the approved Draft. Review every material rationale, scope, trade-off, safeguard, dependency, migration, rollback, Confirmation criterion, source, and approval detail.

Read back the provisional ADR. Change its status to accepted only after the completeness check passes. Read back the accepted ADR before deleting the source Draft.

After successful promotion, delete the source Draft. Keep its ID and approved revision as ADR provenance. Do not link the ADR to a source file that no longer exists. Do not create a `.archive/draft/` folder or a Promoted Drafts index.

If source deletion fails after acceptance, retain the Draft temporarily. Record the resulting ADR ID and cleanup reason in its metadata. List it only under Promotion Cleanup Pending. Retry deletion without creating another ADR or repeating approval.

Only accepted ADRs can govern implementation tasks. Keep task execution approval separate from the ADR's decision approval.

When all implementation tasks and the ADR's confirmation checks pass, move the ADR to `.archive/adr/`. Keep archived ADRs permanently. Never add them to the 90-day task/report retention index.

The decision-governance skill owns Draft, ADR, and repository-analysis lifecycles. Load it only when a task requires decision governance. Do not add it to foundational initialization.

## Task workflow

1. Check the board and active records before creating work. Update an existing task when the objective continues. Otherwise, create a distinct task.
2. Record the user's request, scope, constraints, approval, priority, dependencies, and acceptance criteria.
3. Select one current execution task. Follow explicit user direction, then dependencies, priority, and age.
4. Record meaningful actions, decisions, verification, and blockers in the task record. Keep the board as an index.
5. Close only after all acceptance criteria pass. Create the archive copy and read it back. Update the retention index and delete the active record. Check that the board links to the archive commit.

Task IDs use UTC YYYYMMDD-HHMMSS. Use only the statuses Proposed, Ready, In Progress, Blocked, Paused, Done, and Cancelled. Optional assistant improvements remain Proposed until approved. Necessary follow-ups may be created automatically within the approved scope.

## CI issue workflow

GitHub Actions publishes diagnostic evidence into the lint and Actions report families. The event-driven Ledger creates Proposed parent task folders with typed CI remediation subtasks for newly identified actionable findings and links stable parent Task IDs through task_refs. The Worker retains ADR review, prioritization, execution approval, remediation, verification, and parent closeout.

The first complete tooling-valid full audit in each lint scope establishes a baseline without creating tasks. Later runs create tasks only for genuinely new actionable findings. Recurring untracked baseline findings do not flood the backlog. The Ledger retains at most five evidence paths per finding while preserving cumulative occurrence counts.

A lint report can seed a baseline when every required tooling check passes, even when the report records lint failures. The baseline prevents recurring findings from appearing as new work.

A CI remediation subtask becomes Done when its intended-branch fix commit is verified and its SHA and summary are recorded; hosted validation is separate metadata. A parent task cannot close until all required subtasks are Done. The Ledger retains terminal finding identities and resolution history after task archival so recurrence can reopen the same finding and link new remediation. Do not delete terminal Ledger findings solely because a task was archived.

A clean-start reset is destructive and requires explicit user authorization. It clears generated active report data, prior `.archive/reports/**` snapshots, report indexes, and the active Ledger, then establishes new unseeded lint baselines. It preserves scripts, schemas, templates, workflows, operating guides, task archives, and unrelated tasks. See .takeout/reports/triage/README.md and .archive/README.md for exact reset and closeout rules.

Do not run periodic triage or poll workflows. Review CI when the user asks, a known failure blocks work, or the task requires validation. A successful validation run URL and UTC timestamp provide sufficient resolution evidence. Capture a full successful-run diagnostic report only when the task needs detailed evidence.

The changed-document lint workflow uses GitHub Actions concurrency to cancel superseded push runs. Do not add a separate run-list preflight guard. GitHub may not list the current run when its first job queries the run list, which can cause the guard to cancel the current run.

## Discussion register

The Worker maintains [discussion.md](discussion.md) in both conversation modes. Its Conversation Mode reference defines the section order, pre-step brief, open-discussion lifecycle, and three-report limit. Keep technical progress and handoffs in task records, not in the register.

## Recovery

Read this file, the board, and the selected task record. Check the current gpt repository state before resuming. Follow the task's Next Actions. Reconcile discrepancies against the latest user instruction and committed repository state.
