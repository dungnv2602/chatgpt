# Conversation Mode

## Modes

Use Default Mode for detailed work updates and Condensed Mode for concise delivery when the user prefers it. The repository brief is the shared continuity surface.

## Brief contract

`workspace/discussion.md` contains:
- Current Step: the immediate action, exact task/file links, and the next verification.
- Open Discussions: unresolved decisions, essential user inputs, external gates, and access/safety boundaries. Remove resolved entries.
- Reports: three latest successful summaries.

Keep task-level details in task records. Before each meaningful step, replace Current Step with the current task and action. Record meaningful progress and commits in the task record.

## User-input coordination

Do not interrupt an execution batch for routine choices, blockers isolated to one task, or ordinary implementation decisions. Drain all independent work first.

At quiescence, deduplicate essential input requests. Present exactly one question per turn, wait for the user's answer, then present the next question. Do not execute input-dependent tasks until all queued inputs have been collected or declined. Do not repeat answered questions. Record input and scope in the relevant task.

Request input only when necessary to resolve an authority, governance, safety, access, privacy, or materially outcome-changing boundary. Otherwise, decide and proceed within scope.

## Approval

Approval is explicit scope authorization, not status or eligibility. A concise `Approve` applies only to the immediately preceding proposal and scope. Record it.

## Delivery

Use the repository branch `gpt` as source of truth and remote operations only. Provide direct links to relevant records and commits. Do not claim a change was verified unless remote readback confirms it. Do not inspect hosted CI results unless the user explicitly requests review.
