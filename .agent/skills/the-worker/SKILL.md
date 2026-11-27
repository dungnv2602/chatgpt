# The Worker

## Authority

The Worker owns request capture, task hierarchy, selection, execution, continuity, and closeout. The task board is its published schedule, not a second scheduler.

Use repository `dungnv2602/chatgpt`, branch `gpt`, as the sole project source of truth. Use remote GitHub operations only. Do not use local shell, Python, container, or local Git for repository work. Do not inspect, poll, dispatch, rerun, or wait for hosted CI results.

Initialize only on the cue in `.agent/SESSION_START.md`. That file owns session initialization.

## Prompt capture — mandatory

Before substantive work, find or create its task record. Do not begin work that can change project state until the request is recorded.

- **New objective:** create a parent task folder from `workspace/TASK_TEMPLATE.md`.
- **Follow-up, correction, extension, or next step of an existing objective:** create a separate child record under that genuine parent from `workspace/SUBTASK_TEMPLATE.md`. Do not overwrite an earlier prompt or silently enlarge its record.
- **Several related requirements in one prompt:** record the prompt once and group them under one coherent task. Split independent outcomes into sibling tasks or subtasks.
- **Clarification, decision, or approval with no independent deliverable:** append the exact user wording and timestamp to the relevant record's Subsequent Instructions. Do not create an empty task.
- **Greeting or acknowledgement with no request:** no task is needed.
- **Unclear parentage:** do not guess. Preserve the request in the discussion register and ask one concise question at quiescence.

Preserve each actionable user prompt verbatim in its own task or subtask under Original Request/Original Prompt. Preserve later clarifications, constraints, and approvals verbatim under Subsequent Instructions. Link the record from its parent index and keep the task board current. A request is not tracked merely because its words appear in chat, the parent summary, or the discussion register.

Before creating a record, inspect active task records and the board. Reuse a parent only when the objective is genuinely the same. A substantive follow-up still receives its own child record. Never place unrelated requests under one parent to reduce task count.

## Task hierarchy and CI attribution

A user task is the genuine parent. Its follow-up requests and CI remediation are child subtasks. The Ledger must never create a synthetic parent for a file, rule, workflow, job, or CI finding.

Every task-specific implementation commit must include one exact commit trailer:

```text
Task-ID: <active-task-or-subtask-id>
```

The CI report must preserve this source task ID. If it names a subtask, resolve its Parent Task ID. Create CI remediation children only when the source ID resolves to an existing, active, genuine user parent. If it does not resolve, retain the finding in the Ledger as unassigned. Never infer attribution from the current board pointer, changed file, workflow name, branch, or timing.

The CI Ledger owns finding identity, evidence, grouping, and child creation. It may update only the attributed parent’s finding summary, its child records, and its subtask index. It must not create parent tasks, change parent status/priority/current execution, or edit the task board.

CI remediation children are P0, Approved, and Ready under the standing authorization. Use Proposed only when a specific unresolved decision is required for that remediation. Routine implementation does not need a new ADR merely because it changes code. Keep a genuine decision gate narrow to the dependent work.

## Status, approval, and scheduling

Approval records authority for a scope. It is independent of status and priority. Record the approval source and scope. Never infer approval from status.

Statuses are Proposed, Ready, In Progress, Blocked, Paused, Done, and Cancelled. Ready requires satisfied dependencies and any real decision gate. Use Blocked only for a genuine external or user-resolvable blocker. Use Paused only for intentional suspension.

The Worker is the sole scheduler. Check eligibility and dependencies first, then priority and age. Keep dependency-waiting work out of the eligible queue. Detect cycles; do not repeatedly retry an impossible dependency chain. Correct an edge only when the error is clear and authorized. Ask for essential input only at quiescence.

The board publishes:
- one Current Execution pointer, or none;
- the ordered eligible queue;
- the next task;
- deferred tasks and their reasons.

Do not duplicate the queue in task records, README files, or skill references. The Ledger never schedules.

## Execution and closeout

1. Read the selected task, its parent, dependencies, applicable decisions, and owner instructions.
2. Execute approved work to quiescence. Do not interrupt for routine choices or a blocker isolated to one task.
3. Record progress, decisions, changed paths, commit SHAs, readback, and limitations in the task record.
4. For every task-specific implementation commit, add the Task-ID trailer shown above.
5. Close a subtask only after its acceptance criteria pass and the intended-branch commit is read back. CI remediation completion is commit-based; hosted validation is separate metadata.
6. A parent cannot be Done while a required child remains open.
7. After closeout checks, delete the completed or cancelled task folder and remove its board row. Do not archive it, create a retention copy, or add a Historical row. Preserve Ledger finding identity, evidence, resolution history, and prior task references.

Do not claim tests or validation passed unless they were executed and observed. Do not run repository scripts, tests, or lint locally. Use hosted workflows only when required; do not inspect their results unless the user explicitly requests that review.

## Run-to-quiescence and user input

Process independent eligible work sequentially. A blocker on one task must not stop unrelated work. At quiescence, deduplicate essential questions and ask one question per turn. Do not repeat answered questions. Record answers in the relevant task, then execute dependent work as a batch.

Ask only when proceeding would cross an authority, governance, safety, access, privacy, or materially outcome-changing boundary. Otherwise use the narrowest safe interpretation.

## Execution cues and startup

After a proposal receives approval, wait for `proceed` or `execute` before starting that proposal. Approval alone is not an execution cue. The explicit `/start` procedure is a separate governing workflow cue.

At `/start`, follow `.agent/SESSION_START.md`. The mandatory P0 batch uses the rules above. Do not inspect hosted CI results. At batch completion, state readiness and remaining blockers.
