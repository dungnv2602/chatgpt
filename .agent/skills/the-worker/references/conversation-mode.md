# Conversation Mode

## Modes

Use Default Mode for detailed work updates and Condensed Mode for concise delivery when the user prefers it. The repository brief is the shared continuity surface.

## Brief contract

`workspace/discussion.md` contains:
- Current Step: the immediate action, exact task/file links, and the next verification.
- Open Discussions: unresolved decisions, essential user inputs, external gates, and access/safety boundaries. Remove resolved entries.
- Reports: three latest successful summaries.

Keep task-level details in task records. The Worker’s mandatory Prompt capture rule governs every request. this brief is not a substitute for a task or subtask record. Before each meaningful step, replace Current Step with the current task and action. Record progress and commits in the task record.

## User-input coordination

Do not interrupt an execution batch for routine choices, blockers isolated to one task, or ordinary implementation decisions. Drain all independent work first.

At quiescence, deduplicate essential input requests. Ask one question per turn and wait for the answer before asking the next. Do not execute input-dependent tasks until the user answers or declines each queued input. Do not repeat answered questions. Record input and scope in the task.

Request input only when necessary to resolve an authority, governance, safety, access, privacy, or materially outcome-changing boundary. Otherwise, decide and proceed within scope.

## Approval and execution cue

Approval authorizes a scope. It does not depend on status or eligibility and does not start execution. A concise `Approve` applies only to the preceding proposal. After approval, wait for `proceed` or `execute`. If the user omits the cue, remind them. When the cue arrives, run authorized work to quiescence. Ask essential questions one at a time, wait for answers, and record approval and input scope.

## Delivery

Use the repository branch `gpt` as source of truth and remote operations only. Provide direct links to relevant records and commits. Do not claim a change was verified unless remote readback confirms it. Do not inspect hosted CI results unless the user explicitly requests review.
