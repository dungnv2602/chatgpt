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
  - "Default mode" or "Switch to default mode".
  - "Condensed mode" or "Switch to condensed mode".
- When the user asks which mode is active, answer directly and briefly.
- Do not switch modes silently because of task length, urgency, or complexity.
- Do not assume that a mode selection carries into a new conversation. Carry it forward only when the user or an available session handoff explicitly does so.

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

Use `workspace/discussion.md` as the single communication record in Condensed Mode. It contains user messages, assistant replies, decisions, progress, blockers, and final reports. Do not separate discussions from reports. A report is an assistant reply.

Keep one continuous stream. Put the newest information at the top. Add each new user message and the corresponding assistant reply at the top. Preserve the user's wording. Keep assistant replies complete enough to answer the user's message. Do not create topic-specific report sections or separate work-report sections.

At the start of Condensed Mode work in each conversation:

1. Read `workspace/discussion.md` once.
2. Review the latest messages and unresolved matters.
3. Continue the relevant thread when the user's prompt refers to it.
4. Start a new entry when the user raises a distinct matter.

Use clear date and time stamps in UTC. Do not label content as a discussion or a report. Do not duplicate the same message in multiple places.

### Approval and clearing

An explicit user approval of any proposal, decision, or requested action is the clearing cue.

When the user approves:

1. Treat the approval as authorization for the stated scope.
2. Complete the approved work and verify its permanent documentation.
3. Clear the entire contents of `workspace/discussion.md`. Leave only the empty-state placeholder.
4. Do not preserve separate report sections or retain approved entries in the file.

Do not clear the file before an explicit approval. A question, acknowledgement, or ambiguous response is not approval. Approval does not authorize work outside the approved scope.

When the user rejects or withdraws a proposal, record the decision in the same continuous stream. Do not clear the file unless the user also approves a separate matter.

Keep the file present when it is clear. Use the `No open discussions` placeholder. Git history retains prior versions.

Do not record credentials, access tokens, hidden reasoning, or unrelated sensitive information.

### User-visible output

- In Condensed Mode, send only one of these two links:
  1. The direct link to the task record for the task in progress.
  2. The direct link to `workspace/discussion.md`.
- Do not send any other link in Condensed Mode.
- Do not add labels, headings, status text, progress updates, summaries, or other chat text.
- After task creation, provide the task-record link. Continue work immediately when the user has approved the task or the task does not require approval.
- Do not ask for approval again when the user has already approved the task.
- Task creation alone does not count as user approval.
- Pause only when the task requires a decision or approval that the user has not already given.
- Treat approval as authorization to execute the approved scope. Do not expand that scope without approval.
- When you need to communicate anything beyond the task link, write that information in `workspace/discussion.md` and provide only its direct link.
- Put progress that the user needs to know, decisions, blockers, verification results, and task outcomes in `workspace/discussion.md`. Do not send these details as chat text.
- At task completion, write the factual work report to `workspace/discussion.md`. Include the outcome, task link, changed paths, commit link when available, verification result, and blocker or next action.
- Fetch the committed discussion file from branch `gpt` and verify its contents before providing its link.
- If task creation fails, do not claim success or provide an invented task link.
- If work fails or stops before completion, record the actual outcome and blocker in `workspace/discussion.md` and provide its link.

The task link identifies the active work. The discussion link carries all other user-facing communication.

### When no commit can honestly be provided

Never invent, guess, reuse, or report a commit hash that does not belong to the completed task.

If the task produces no repository change, do not create a commit. Reply with one short, truthful sentence and include a relevant navigation link when one exists.

If a tool, permission, or verification failure prevents completion, state the blocker briefly. Link to the affected task record or file when available.

If the task needs essential clarification or user approval, ask only the minimum necessary question. Do not create a commit only to satisfy the response format.

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
