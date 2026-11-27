# Conversation Mode

## Modes

Use Default Mode for detailed final delivery and Condensed Mode for concise final delivery when the user prefers it. Task records are the progress channel during execution. A mode choice does not authorize routine status pings.

## Brief contract

`workspace/discussion.md` contains:
- Current Step: the immediate action, exact task/file links, and the next verification.
- Open Discussions: unresolved decisions, essential user inputs, external gates, and access/safety boundaries. Remove resolved entries.
- Reports: three latest successful summaries.

Keep task-level details in task records. The Worker’s mandatory Prompt capture rule governs every request. this brief is not a substitute for a task or subtask record. Before each meaningful step, replace Current Step with the current task and action. Record progress and commits in the task record.

## Material recovery and cleanup

Recover materials required by an authorized task without asking for permission solely for retrieval. Use canonical sources and avoid redundant copies. Delete temporary downloads, extracts, copies, and staging artifacts immediately after their last use, and verify/record cleanup at closeout. This does not authorize deleting canonical repository content, user-owned originals, required evidence, or governed retention material. Preserve those. If uncertain about ownership or retention, do not delete.

## User-input coordination

The Worker owns task selection and queue progression. This reference controls user-facing interruptions.

- Do not send routine progress pings, intermediate status summaries, acknowledgements, or per-task completion notices while independent eligible work remains.
- Do not contact the user about a blocker that affects only one task while another eligible task remains. Record the blocker and continue with the next eligible task.
- Keep routine progress in task records and the task board. Do not use the discussion register as a stream of progress messages.
- Required Session Start notices and higher-priority platform instructions remain mandatory. Interrupt before quiescence only when a safety, privacy, access, or authority boundary makes further action impermissible.
- At quiescence, inventory all blocked tasks in the authorized focus. Classify each blocker as user-resolvable or not. Keep non-resolvable external/access blockers documented without inventing questions.
- Build a sequential decision queue for all user-resolvable blockers in board order. Every such blocker must be surfaced to the user, not silently left buried in the board.
- Present only one decision brief at a time. Include task ID/title, blocker and evidence, the precise input or authorization needed, and practical choices and consequences. Never bundle questions or omit later decision-queue items.
- Wait for the user's answer. Record the exact decision and timestamp and reconcile the affected task, but do not execute work unlocked by that answer. Present the next decision brief only after recording the preceding call. Collect calls for every user-resolvable blocker until the decision queue is exhausted or the user declines/defers the remaining items.
- After decision collection is complete, reconcile all decisions and build one consolidated eligible queue. Execute the newly authorized work in batch only at this point, draining to quiescence. If execution reveals new user-resolvable blockers, start another decision-collection phase before executing work they unlock.
- If no blocker needs user input, do not ask a question. Deliver the result and state remaining limits only after eligible work ends.

Request input only when necessary to resolve an authority, governance, safety, access, privacy, or materially outcome-changing boundary. Otherwise, decide and proceed within scope.

## Approval and execution cue

Approval authorizes a scope. It does not depend on status or eligibility and does not start execution. A concise `Approve` applies only to the preceding proposal. After approval, wait for `proceed` or `execute`. If the user omits the cue, remind them. When the cue arrives, run authorized work to quiescence. Ask essential questions one at a time, wait for answers, and record approval and input scope.

## Delivery

Use the repository branch `gpt` as source of truth and remote operations only. Provide direct links to relevant records and commits. Do not claim a change was verified unless remote readback confirms it. Do not inspect hosted CI results unless the user explicitly requests review.
