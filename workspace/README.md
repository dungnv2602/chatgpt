# Workspace

The workspace is the task-management and conversation-navigation area. The Worker owns task records, selection, progress, handoffs, direct deletion at closeout, and the shared discussion register. Document Standards governs workspace document formats.

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
| [tasks/](tasks/) | Active task folders. Each contains task.md and subtasks/README.md. Child records live under subtasks/ |
| [draft/](draft/README.md) | Proposals awaiting user review and decision |
| [adr/](adr/README.md) | Accepted decisions awaiting implementation and confirmation |
| [analysis/](analysis/README.md) | Evidence-based repository analysis snapshots |
| [../.takeout/reports/README.md](../.takeout/reports/README.md) | Lint, Actions, and issue-ledger navigation |

## Draft and ADR workflow

Use a Draft to present a proposal. Do not implement a proposed decision.

After the user approves the exact Draft, create a provisional ADR with status promotion-pending. Compare the complete ADR with the approved Draft. Review every material rationale, scope, trade-off, safeguard, dependency, migration, rollback, Confirmation criterion, source, and approval detail.

Read back the provisional ADR. Change its status to accepted only after the completeness check passes. Read back the accepted ADR before deleting the source Draft.

After successful promotion, delete the source Draft. Keep its ID and approved revision as ADR provenance. Do not link the ADR to a source file that no longer exists. Do not create a `workspace/archive/draft/` folder or a Promoted Drafts index.

If source deletion fails after acceptance, retain the Draft temporarily. Record the resulting ADR ID and cleanup reason in its metadata. List it only under Promotion Cleanup Pending. Retry deletion without creating another ADR or repeating approval.

Only accepted ADRs can govern implementation tasks. Keep task execution approval separate from the ADR's decision approval.

**Approval semantics:** Approved means explicit user authorization for the presented scope or applicable documented standing authorization. Pending means authorization is not granted; Declined means the scope was rejected. A concise "Approve" authorizes the immediately preceding proposal within its stated scope, not unrelated or materially expanded work. Approval is distinct from task status and eligibility: an approved task may remain Proposed until governance and dependencies are satisfied. Record the source and scope of approval. Never infer approval from Ready, In Progress, priority, or origin.

Keep every accepted ADR permanently in the flat `workspace/adr/` folder. When implementation and Confirmation finish, update its implementation status and lifecycle history. Do not move it to a separate archive folder or add it to the 90-day task/report retention index.

The decision-governance skill owns Draft, ADR, and repository-analysis lifecycles. Load it only when a task requires decision governance. Do not add it to foundational initialization.

## Task workflow

1. Check the board and active records before creating work. Update an existing task when the objective continues. Otherwise, create a distinct task.
2. Record the user's request, scope, constraints, approval, priority, dependencies, and acceptance criteria.
3. Select one current execution task. Follow explicit user direction, then dependencies, priority, and age.
4. Record meaningful actions, decisions, verification, and blockers in the task record. Keep the board as an index.
5. Close only after the Worker checks every acceptance criterion and marks each required subtask Done. Delete the complete task folder, including task.md, subtasks/README.md, and every child record. Remove the task from the board. Do not create a copy, archive, retention entry, or Historical row.

Task IDs use UTC YYYYMMDD-HHMMSS. Use only the statuses Proposed, Ready, In Progress, Blocked, Paused, Done, and Cancelled. Optional assistant improvements remain Proposed until approved. Necessary follow-ups may be created automatically within the approved scope.

## CI issue workflow

GitHub Actions publishes diagnostic evidence into the lint and Actions report families. The event-driven Ledger creates one Proposed parent per affected file or workflow and typed CI remediation child subtasks for each stable finding group. It never creates standalone per-rule, per-step, or per-finding CI tasks. Every parent folder contains task.md and subtasks/README.md. The Ledger stores parent Task IDs in task_refs, child IDs in subtask_refs, and migrated former IDs in legacy_task_refs. The user's standing instruction makes CI-generated P0 remediation mandatory and execution-approved. The Worker checks accepted-ADR coverage and links the ADR before moving a task to Ready or In Progress. Keep the task Proposed while Governing ADR(s) is Pending. P0 does not bypass decision governance.

The first complete tooling-valid full audit in each lint scope establishes a baseline without creating tasks. Later runs create tasks only for genuinely new actionable findings. Recurring untracked baseline findings do not flood the backlog. The Ledger retains at most five evidence paths per finding while preserving cumulative occurrence counts.

The user's standing instruction makes CI-generated P0 remediation mandatory and execution-approved. The Worker checks whether an accepted ADR covers each finding. Link the accepted ADR before moving a task to Ready or In Progress. Keep the task Proposed while Governing ADR(s) is Pending. If no accepted ADR covers the work, prepare a Draft and wait for user approval and ADR acceptance. P0 does not bypass decision governance.

A lint report can seed a baseline when every required tooling check passes, even when the report records lint failures. The baseline prevents recurring findings from appearing as new work.

The Worker marks a CI remediation subtask Done after committing its fix to the intended branch. The Worker checks the commit and records its SHA and summary. Hosted validation remains separate metadata. The Worker closes a parent only after every required subtask reaches Done. The Ledger retains terminal finding identities, resolution history, and prior task references after the Worker deletes a task folder. A later observation can reopen the same finding and create new remediation. Task deletion does not delete terminal Ledger findings.

A clean-start reset is destructive and requires explicit user authorization. It clears generated active report data, report indexes, and the active Ledger, then establishes new unseeded lint baselines. It preserves scripts, schemas, templates, workflows, operating guides, and unrelated tasks. See .takeout/reports/triage/README.md for reset rules.

Do not run periodic triage or poll workflows. Review CI when the user asks, a known failure blocks work, or the task requires validation. A finding becomes resolved after the Worker checks the intended-branch fix commit and records its SHA, remediation summary, and UTC resolution timestamp. Hosted validation is separate metadata. A pending or failed hosted run does not reopen completed remediation.

The changed-document lint workflow uses GitHub Actions concurrency to cancel superseded push runs. Do not add a separate run-list preflight guard. GitHub may not list the current run when its first job queries the run list, which can cause the guard to cancel the current run.

## Discussion register

The Worker maintains [discussion.md](discussion.md) in both conversation modes. Its Conversation Mode reference defines the section order, pre-step brief, open-discussion lifecycle, and three-report limit. Keep technical progress and handoffs in task records, not in the register.

## Recovery

Read this file, the board, and the selected task record. Check the current gpt repository state before resuming. Follow the task's Next Actions. Reconcile discrepancies against the latest user instruction and committed repository state.
