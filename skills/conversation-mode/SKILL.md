---
name: conversation-mode
description: Control how ChatGPT collaborates with the user through Default Mode or Condensed Mode. Use when the user asks to switch conversation style, work mainly in the repository with minimal chat output, or return to normal conversational responses.
metadata:
  project-role: foundational
  format: agentskills
  created: "2026-11-18T13:18"
  updated: "2026-11-20T12:46"
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

### Discussion register and final work report

Use `workspace/discussion.md` for unresolved discussions and the latest completed-work report. This file is not a conversation transcript or task index.

Keep a separate `## Latest Work Report` section at the top of the file. Replace its contents only when a newer task reaches an outcome. Keep the report after the related discussion is resolved. Include:

- Outcome.
- Task link, when available.
- Changed paths.
- Commit link, when available.
- Verification result.
- Blocker or next action.

Keep unresolved discussion entries below the report. Remove a resolved discussion entry only after its permanent documentation is complete and verified. Do not remove the latest work report during discussion cleanup.

At the start of Condensed Mode work in each conversation:

1. Read `workspace/discussion.md` once.
2. Identify open topics and their latest status.
3. Continue a matching topic when the user's prompt refers to it.
4. Create a new topic when the user starts a distinct unresolved discussion.

Record each relevant user prompt verbatim. Put the newest discussion first and the newest message at the top of its discussion. Keep assistant notes brief. Record only conclusions, proposals, findings, rejected options, and outstanding questions that help continue the discussion. Do not copy full assistant replies or hidden reasoning.

Each discussion entry must include:

- A concise topic heading.
- Its status: `Open`, `Awaiting approval`, or `Approved — documentation pending`.
- The date and time in UTC for each recorded message.
- User prompts as blockquotes, without paraphrasing.
- Short assistant notes where they materially help recovery.
- Outstanding decisions or questions, when any remain.

When a new message changes a discussion, add it at the top of that discussion. Move the most recently updated discussion to the top of the file. Keep separate topics distinct. Do not add unrelated conversation or routine status messages.

### Approval and cleanup

A discussion remains open until the user explicitly approves, rejects, or withdraws it.

When the user approves a proposal:

1. Mark the entry `Approved — documentation pending`.
2. Transfer the original user prompts and relevant clarifications into the appropriate task record or permanent project document.
3. Create or update the task board entry when the approved outcome requires a task.
4. Read back every changed document and verify the required content.
5. Remove only the resolved discussion entry after documentation is complete and verified.

Approval does not authorize work outside the approved scope. Do not clear an entry merely because the user approved it. Keep it until the required documentation is complete.

When the user rejects or withdraws a proposal, record any lasting decision in the appropriate permanent record when needed. Then remove the resolved entry. Do not remove other open discussions.

If documentation is incomplete, a write fails, or verification does not pass, keep the entry. Update its status and outstanding work. Do not claim that the discussion is finalized.

Keep the file present when it has no open discussions. Use the `No open discussions` placeholder. Do not create a separate discussion archive. Git history retains committed prior versions.

Do not record credentials, access tokens, hidden reasoning, or unrelated sensitive information. Preserve user prompts verbatim except for content that must not be retained for safety or privacy.

### User-visible output

- Condensed Mode replies contain direct GitHub links only.
- Do not add labels, headings, status text, progress updates, or summaries.
- After successful task creation, provide only the direct task-record link.
- Stop after providing the task link. Wait for the user's explicit instruction to continue.
- Do not treat task creation or a recorded approval state as permission to pass this inspection gate.
- When the task reaches an outcome, write a factual report to `workspace/discussion.md`.
- Include the outcome, task link, changed paths, commit link when available, verification result, and blocker or next action.
- Fetch the committed report from branch `gpt` and verify it before replying.
- After verification, provide only the direct link to `workspace/discussion.md`.
- If task creation fails, do not claim success or provide an invented task link.
- If work fails or stops before completion, still report the actual outcome and blocker in `workspace/discussion.md`.

The task link is the inspection gate. The discussion link is the final report.

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
- Do not claim success before the relevant tool confirms it.

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
