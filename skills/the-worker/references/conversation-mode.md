# Conversation Mode and Discussion Register

## Purpose

Give the user two explicit ways to work:

- **Default Mode** supports normal collaboration, explanations, and useful context.
- **Condensed Mode** prioritizes repository work and uses extremely short chat output.

This skill controls response style and workflow priorities. It does not override higher-priority safety, privacy, tool-use, or workspace-boundary instructions.

## 1. Mode selection and persistence

- Default Mode applies at the start of each new conversation unless the user selects another mode.
- A mode remains active for the current conversation until the user switches it.
- Accept natural-language commands such as:
  - "Default mode", "Switch to default mode", or "Conversation mode: default mode".
  - "Condensed mode", "Switch to condensed mode", or "Conversation mode: condensed mode".
- Treat an unquoted mode command as valid when it appears with other task instructions.
- Ignore mode commands that the user quotes, discusses, or presents as hypothetical examples.
- At the start of every turn, resolve the active mode before processing the rest of the prompt.
- Apply a mode command in the same turn that contains it.
- When the user asks which mode is active, answer directly and briefly.
- Do not switch modes silently because of task length, urgency, or complexity.
- Do not assume that a mode selection carries into a new conversation. Carry it forward only when the user or an available session handoff explicitly does so.

### Per-turn mode gate

Before any tool call, progress message, or answer:

1. Check the current user message for an unquoted mode command.
2. If there is no new command, retain the mode already active in this conversation.
3. At the start of a new conversation, use an explicit mode in the session handoff when one exists.
4. Otherwise, use Default Mode.
5. Apply the resolved mode to the entire turn, including tool use, error handling, and the final response.

If a mode command and a task appear in the same message, switch modes first. Then handle the task under the selected mode.

## 2. Default Mode

In Default Mode:

- Converse normally and warmly.
- Explain the plan for multi-step work when useful.
- Give concise progress updates when a task takes time or reaches a meaningful milestone.
- Explain decisions, trade-offs, blockers, and verification results.
- For repository work, execute the task. Do not only explain how the user could do it.
- Follow all standing repository restrictions, including the user's approved project-directory boundary.
- Maintain `workspace/discussion.md` under the shared register rules in Section 3.
- Publish and read back a Current Step brief before each meaningful project-work step.
- Update Open Discussions and Reports when their state changes.
- Include the discussion link in Default Mode chat when the register contains an active brief, open discussion, or retained report. Normal explanatory chat may accompany the link.

Default Mode is the normal full-conversation experience.

## 3. Condensed Mode

In Condensed Mode, prioritize execution and navigation.

### Work priorities

1. Focus on completing the requested task.
2. Use The Worker for task selection, progress records, handoffs, and recovery.
3. Inspect only the files needed inside the permitted workspace.
4. Make the required authorized changes.
5. Read back changed paths and check their contents.
6. Commit completed repository work on the authorized branch.
7. Keep detailed progress in the task record, not in chat. The CI Ledger creates and groups Proposed tasks when findings enter the ledger during report ingestion; the Worker reviews those tasks under the normal approval rules. Do not periodically poll or scan the ledger.

The Worker applies in every conversation mode. Condensed Mode changes only the amount and format of user-visible communication.

### Shared discussion register and reports

These register rules apply in Default Mode and Condensed Mode. Only the amount of chat output changes.

Use `workspace/discussion.md` as a compact, current register with exactly three sections, in this order:

`## Current Step`

`## Open Discussions`

`## Reports`

The file is not a transcript, general progress log, or task-history archive. `Current Step` contains only the one active pre-step brief. The other sections are ordered newest first. Use UTC timestamps. Determine the section from the item's current state, not from its original source or the kind of task.

#### Current Step

This section is the user's short, live briefing surface while work proceeds.

- Before each meaningful work step, replace this section with one concise brief that states the next action, its scope, and the expected result. A meaningful step is a coherent unit of inspection, decision, editing, or validation. Do not create a brief for every individual API call.
- Commit the brief to `gpt`, fetch the committed file, and check its content before starting that step.
- After the read-back, send the direct `discussion.md` link to the user before executing the step. Do not bury the brief in chat. The file is the briefing surface.
- Keep exactly one current brief. Do not retain completed briefs as history or duplicate them in Reports.
- Link every active task record that the assistant is working on from the Current Step brief. Include multiple task links when work spans multiple tasks. Remove links when work stops or closes.
- After the step, record detailed actions and verification in the task record. Before the next meaningful step, replace the brief and send the updated link.
- If work stops, fails, or needs a user decision, state that execution is paused and why in the current brief. Record any unresolved failure or required user input under Open Discussions.
- When no step is active, use `_No active step._`.

#### Open Discussions

This section contains every matter that is unresolved or needs the user's attention, judgment, or response. This includes:

- A direct question, request for clarification, approval, permission, preference, or decision.
- Ambiguous or conflicting prompt instructions when the assistant cannot safely choose an interpretation.
- A clarification the assistant asks the user to provide, until the user answers or withdraws the request.
- A failed operation, failed validation, unsuccessful outcome, or unresolved defect. Never put a failure report in Reports.
- A blocker that requires user action, access, a choice, or an exception.
- A material trade-off where the user's priorities determine the appropriate next step.
- A partial result when the remaining scope requires a user decision.
- A follow-up question raised by an otherwise successful task.

Treat "needs the user's call" broadly. Keep the matter open and ask one focused question if proceeding requires any of these actions:

- Guessing the user's intent.
- Changing the approved scope.
- Accepting a material risk.
- Choosing between materially different outcomes.
- Claiming acceptance without evidence.

Keep a failure in Open Discussions while it remains unresolved or unsuccessful, even when the next step seems obvious. The task record holds the technical details. After you resolve the failure and establish the outcome, remove the discussion. When useful, add a success-only report with the final result. Do not report internal retries that you resolved before you reported the work.

For each open item:

- State the unresolved point, why it needs attention, and the exact user decision or information required. Include the minimum context needed to understand it.
- Link every Draft that is under user review. Keep each Draft link in the discussion item that asks for its decision. Do not link a Draft that does not exist. A blocker with no Draft may link its task record when one exists.
- Preserve the user's relevant wording verbatim when it prevents ambiguity. Do not copy the full conversation.
- Keep separate decisions separate. Combine messages only when they concern the same decision or dependency.
- Put the item with the latest creation or meaningful update first. When the user adds a clarification to an existing thread, update that thread and move it to the top. Do not create a duplicate.
- Keep an item open while awaiting the user's answer, even if the conversation or task is paused.
- Do not close an item merely because it is old, another item is newer, work has stopped, or the assistant has proposed a solution.
- Close the item when the user answers and no further input is needed. Also close it when evidence answers the question. Close it when the user withdraws or rejects the proposal. Close it after you implement the decision and resolve the matter. Close it when the blocker is resolved.
- If the user answers only part of a multi-part question, keep the remaining unresolved part open and revise the entry to show only what remains.
- If a later instruction supersedes an earlier open item, close the superseded item and retain the current decision or question. Preserve unrelated open items.

A clarification request is not itself a successful report. Once the user clarifies, remove the clarification entry when it no longer needs their input. If the clarification changes scope, record that decision in the task record and proceed only within the clarified scope.

#### Reports

This section contains only successful reports. Add a report after a discrete piece of work reaches a successful and supportable outcome. The report must not require more user input for its interpretation or acceptance.

A report must:

- Describe the completed result, not merely an intention, attempt, or progress update.
- Be supported by the required verification. State any meaningful verification limit.
- Avoid claiming that CI, tests, read-back, deployment, or another check passed unless the relevant result was actually observed.
- Link or name the authoritative task record when more detail is needed, without duplicating its progress log.
- Be concise and useful as a recent-outcome summary.

Reports may describe a completed milestone even when a larger task continues, provided the milestone is independently complete and successful. If that milestone also leaves a decision or question for the user, record the success in Reports and the distinct unresolved question in Open Discussions. Do not duplicate the same information in both sections.

A report may mention that an issue was encountered and successfully addressed, but it must report the final successful outcome and its verification. Do not classify an unsuccessful final outcome, an unverified claim, a pending check, or a blocked task as a success report.

Retain at most the three most recent reports. Order them newest first by the time the successful outcome was verified or completed. When a new successful report would create a fourth entry, remove the oldest report. This limit applies only to Reports. It does not limit the number of genuinely open discussions. Do not preserve older reports elsewhere in this file.

#### Ordering, timestamps, and maintenance

- Keep the two H2 sections in the exact order shown above. Do not add other sections.
- Within each section, sort entries newest first. Use the time of the latest meaningful update for an open discussion and the completion time for a report.
- Use a clear timestamp for every entry. Use UTC and an unambiguous format such as `2026-11-20 16:14 UTC`.
- Do not move an entry to the top for cosmetic edits. Move it only after a meaningful change to its status, required decision, scope, or verified outcome.
- Review and reconcile the register when entering project work in either mode, after meaningful user clarifications or decisions, after failures, and before the final response. Read it once at the start of project work in each conversation.
- Update the file in the same turn when an item opens, materially changes, or closes. Remove closed discussions immediately. Prune Reports immediately when the three-report limit is exceeded.
- Keep task progress, technical diagnostics, retries, detailed verification, and handoffs in the task record. The register is a short navigation surface, not a substitute for task records.
- Never record credentials, access tokens, hidden reasoning, or unrelated sensitive information.

#### Empty state

Keep all three headings even when one or more sections have no entries. Use these exact placeholders:

`## Current Step`

`_No active step._`

`## Open Discussions`

`_No open discussions._`

`## Reports`

`_No reports._`

If a section is empty, keep its placeholder and retain the entries in the other sections. Never remove a heading.

### Approval and clearing

Decision-governance work keeps its active implementation task in Current Step. Keep each Draft in Open Discussions until the user decides. After promotion, link the accepted ADR from the implementation task.

Approval authorizes only the scope the user approved. It does not authorize unrelated work or clear unrelated open discussions.

Keep an approved matter open while the approved work is incomplete or still requires user input. Once the approved work is complete and verified, remove only the resolved discussion. A rejected or withdrawn proposal is also removed when no further discussion is needed. Do not wait for separate approval to clear a resolved discussion.

Never clear an unrelated open matter. Do not retain resolved discussions as history. Keep the three-report success history separate from open discussions. Do not clear reports merely because the associated discussion closes. Retain them until they fall outside the three most recent successful reports.

Do not treat silence as approval. Do not infer a decision from an unrelated user message. If the user gives a partial answer, retain only the unresolved part.

### User-visible output

- In Condensed Mode, send only one direct link:
  1. Link to `workspace/discussion.md` when it contains an active Current Step brief, any open discussion, or a retained report.
  2. Otherwise, link to the task record for the task in progress.
- In Default Mode, include the discussion link when the register contains an active brief, open discussion, or retained report. You may also provide normal explanations and other relevant links.
- Do not send any other link in Condensed Mode.
- Do not add labels, headings, status text, progress updates, summaries, or other chat text. The brief itself lives in `discussion.md` and must be linked before its step starts.
- The only exception is the single response that switches into Condensed Mode. That response must contain only a brief mode acknowledgement. Starting with the next response, send only one permitted link.
- After task creation, provide the task-record link. Continue work immediately when the user has approved the task or the task does not require approval.
- Do not ask for approval again when the user has already approved the task.
- Task creation alone does not count as user approval.
- Pause only when the task requires a decision or approval that the user has not already given.
- Treat approval as authorization to execute the approved scope. Do not expand that scope without approval.
- When communication requires user input, a decision, approval, or clarification, put only that unresolved matter in Open Discussions and provide the discussion-file link.
- Keep progress, blockers that do not constitute a reported failure, verification details, and task outcomes in the task record. Add a concise Reports entry only for a successful outcome.
- At task completion, remove resolved discussions and add a success report only if the outcome is complete and verified. Keep any distinct follow-up requiring user input in Open Discussions.
- Fetch the committed discussion file from branch `gpt` and inspect its contents before providing its link.
- If task creation fails, do not claim success or provide an invented task link.
- If work fails or stops before completion, record durable progress in the task record. Put the failure in Open Discussions, then provide the discussion link.

The discussion link is the navigation surface whenever it contains open matters or recent success reports. Use the task link when the register has no entries and active work needs a direct destination.

### When no commit can honestly be provided

Never invent, guess, reuse, or report a commit hash that does not belong to the completed task.

If project work produces no project-file change, do not invent a project-change commit. A required discussion-register update is a separate repository change and may have its own commit.

If a tool, permission, or verification failure prevents completion, record the blocker in the task record. Put the failure in Open Discussions if it remains unresolved. Do not place it in Reports.

If the task needs essential clarification or user approval, record the minimum necessary question in Open Discussions. Provide only the discussion-file link. Do not create a project-change commit only to satisfy the response format.

### Progress communication

- Use the pre-step briefing protocol in both modes instead of relying on free-form progress narration.
- Before each meaningful work step, publish and link the committed Current Step brief. Do not start the step before the user has been given that link.
- Default Mode may include additional explanation in chat. Condensed Mode uses the single-link output rule.
- Do not publish a second brief for routine sub-operations inside the same coherent step.
- Record every meaningful action and verification in the task file.
- After a step, update the task record. Before proceeding to another meaningful step, replace the Current Step brief and link it.
- Do not claim success before the relevant tool reports success.

### Work outside the repository

Condensed Mode means minimal communication, not repository-only work. Handle non-repository requests directly. Do not invent a commit for work outside Git.

## 4. Switching modes

When the user switches modes:

- Acknowledge the new mode briefly in the current response.
- Apply it to later work immediately.
- Do not change either mode definition unless the user asks you to edit this skill.

## 5. Interaction with other project skills

- GitHub Actions workflow design, maintenance, security, and verification are governed by the [GitHub Actions skill](../../github-actions/SKILL.md).
- The Worker governs task capture, priority, progress, recovery, and task archival in every conversation mode.
- The Worker owns conversation integrity, drawing-session archives, image provenance, and media closeout.
- Other task-specific skills govern their own tasks.
- The approved project-directory boundary always applies, regardless of conversation mode.
- The only authorized working branch is `gpt`. Use it for repository reads, writes, and commits.
- Do not resume the former `artwork/portrait-attempt-2026-11-10` branch.
- Do not change `main` unless the user authorizes it.
- When skill instructions conflict, follow the higher-priority instruction. State any limitation honestly.
- The Worker owns the register format and maintenance in both modes. It supplies task state and uses the register as the shared briefing and navigation surface.

## 6. Skill source of truth

GitHub is the sole source of truth for project files, skills, prompts, references, and archives. The repository is `dungnv2602/chatgpt`. The authorized branch is `gpt`.

Whenever the user asks you to read, inspect, or follow a project skill:

1. Fetch the requested skill from the GitHub `gpt` branch.
2. Fetch supporting files from the same branch when the skill requires them.
3. Stay inside the approved project directories.
4. If GitHub access fails or a file cannot be verified, disclose that limit.

Whenever you create or change a skill:

1. Commit the authoritative change to branch `gpt`.
2. Fetch the committed path again.
3. Inspect its contents.
4. Do not access or synchronize the ChatGPT Library.

## Technical documentation standard

Follow the [ASD-STE100 skill](../../asd-ste100/SKILL.md) when you create or revise skill files or technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for explanatory documentation. Preserve meaning, scope, and modality.
