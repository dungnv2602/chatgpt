---
name: conversation-mode
description: Control how ChatGPT collaborates with the user through Default Mode or Condensed Mode. Use when the user asks to switch conversation style, work mainly in the repository with minimal chat output, or return to normal conversational responses.
metadata:
  project-role: foundational
  format: agentskills
  created: "2026-11-18T13:18"
  updated: "2026-11-20T20:52"
---

# Conversation Mode

## Purpose

Give the user two explicit ways to work:

- **Default Mode** supports normal collaboration, explanations, and useful context.
- **Condensed Mode** prioritizes repository work and uses minimal chat output.

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
- Do not read, consult, create, or update `workspace/discussion.md`.
- Do not transfer Default Mode conversation content into the discussion register.

Default Mode is the normal full-conversation experience.

## 3. Condensed Mode

In Condensed Mode, prioritize execution and navigation.

### Work priorities

1. Focus on completing the requested task.
2. Use The Worker for task selection, progress records, handoffs, and recovery.
3. Inspect only the files needed inside the permitted workspace.
4. Make the required authorized changes.
5. Read back changed paths and verify their contents.
6. Commit completed repository work on the authorized branch.
7. Keep detailed progress in the task record, not in chat.

The Worker applies in every conversation mode. Condensed Mode changes only the amount and format of user-visible communication.

### Discussion register and assistant replies

Use `workspace/discussion.md` as a temporary register of **open discussions only**. It is not a conversation transcript, progress log, task report, or historical record. Retain only matters that still need a user decision, approval, clarification, or continued discussion.

For each open matter:

- Preserve the user's relevant wording and only the assistant context needed to understand the unresolved point.
- Keep distinct open matters separate and put the newest matter first.
- Keep the entry current. Do not append routine progress, completed work reports, or resolved exchanges.
- At the start of Condensed Mode work in each conversation, read `workspace/discussion.md` once and review only the matters that remain open.
- When the user raises a distinct unresolved matter, add it as a new open entry.

**Close and clear discussions automatically.** A matter becomes inactive when its question has been answered, its decision has been implemented or rejected, its proposal has been withdrawn, or its related task is complete and no further user input is needed. When that happens, remove that matter from `workspace/discussion.md` in the same turn. Do not preserve a closed entry as history. Keep unrelated open matters. If no open matters remain, leave only the empty-state placeholder:

`# Open Discussions`

`_No open discussions._`

Use UTC timestamps for open entries. Do not duplicate task progress or verification details; the task record is authoritative for those details.

### Approval and clearing

Approval authorizes only the scope the user approved. It does not authorize unrelated work or clear unrelated open discussions.

Keep an approved matter open while the approved work is incomplete or still requires user input. Once the work is complete and verified, remove only that resolved matter from `workspace/discussion.md`. A rejected or withdrawn proposal is also removed when no further discussion is needed. Do not wait for a separate approval to clear a resolved discussion.

Never clear an unrelated open matter. Do not retain resolved matters for history. If the last open matter closes, leave only the empty-state placeholder defined above. Keep the file present even when it is empty.

Do not record credentials, access tokens, hidden reasoning, or unrelated sensitive information.

### User-visible output

- In Condensed Mode, send only one of these two links:
  1. The direct link to the task record for the task in progress.
  2. The direct link to `workspace/discussion.md`.
- Do not send any other link in Condensed Mode.
- Do not add labels, headings, status text, progress updates, summaries, or other chat text.
- The only exception is the single response that switches into Condensed Mode. That response must contain only a brief mode acknowledgement. Starting with the next response, send only one permitted link.
- After task creation, provide the task-record link. Continue work immediately when the user has approved the task or the task does not require approval.
- Do not ask for approval again when the user has already approved the task.
- Task creation alone does not count as user approval.
- Pause only when the task requires a decision or approval that the user has not already given.
- Treat approval as authorization to execute the approved scope. Do not expand that scope without approval.
- When you need to communicate anything beyond the task link, write that information in `workspace/discussion.md` and provide only its direct link.
- Put progress that the user needs to know, decisions, blockers, verification results, and task outcomes in `workspace/discussion.md`. Do not send these details as chat text.
- At task completion, keep the factual work report in the task record. Add or retain a discussion entry only when a user decision, clarification, or follow-up remains open. Remove the resolved thread before the final response; if no open discussions remain, leave the empty-state placeholder.
- Fetch the committed discussion file from branch `gpt` and verify its contents before providing its link.
- If task creation fails, do not claim success or provide an invented task link.
- If work fails or stops before completion, record durable progress in the task record. Put only a decision, clarification, or blocker that needs user input in `workspace/discussion.md`, then provide its link.

The task link identifies the active work. The discussion link carries all other user-facing communication.

### When no commit can honestly be provided

Never invent, guess, reuse, or report a commit hash that does not belong to the completed task.

If project work produces no project-file change, do not invent a project-change commit. A required discussion-register update is a separate repository change and may have its own commit.

If a tool, permission, or verification failure prevents completion, record the blocker in `workspace/discussion.md`. Provide only its direct link.

If the task needs essential clarification or user approval, record the minimum necessary question in `workspace/discussion.md`. Provide only its direct link. Do not create a project-change commit only to satisfy the response format.

### Progress communication

- Keep progress messages to a minimum.
- Avoid interim commentary unless it materially helps the user.
- Record every meaningful action in the task file.
- Report only outcomes, decisions, blockers, and next actions.
- Do not claim success before the relevant tool reports success.

### Work outside the repository

Condensed Mode means minimal communication, not repository-only work. Handle non-repository requests directly. Do not invent a commit for work outside Git.

## 4. Switching modes

When the user switches modes:

- Acknowledge the new mode briefly in the current response.
- Apply it to later work immediately.
- Do not change either mode definition unless the user asks you to edit this skill.

## 5. Interaction with other project skills

- GitHub Actions workflow design, maintenance, security, and verification are governed by the [GitHub Actions skill](../github-actions/SKILL.md).
- The Worker governs task capture, priority, progress, recovery, and task archival in every conversation mode.
- Session Archiving governs conversation integrity, drawing-session archives, image provenance, and media closeout.
- Other task-specific skills govern their own tasks.
- The approved project-directory boundary always applies, regardless of conversation mode.
- The only authorized working branch is `gpt`. Use it for repository reads, writes, and commits.
- Do not resume the former `artwork/portrait-attempt-2026-11-10` branch.
- Do not change `main` unless the user authorizes it.
- When skill instructions conflict, follow the higher-priority instruction. State any limitation honestly.
- Conversation Mode alone controls access to `workspace/discussion.md`. The Worker does not read or write the discussion register directly.

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
3. Verify its contents.
4. Do not access or synchronize the ChatGPT Library.

## Technical documentation standard

Follow the [ASD-STE100 skill](../asd-ste100/SKILL.md) when you create or revise skill files or technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for explanatory documentation. Preserve meaning, scope, and modality.
