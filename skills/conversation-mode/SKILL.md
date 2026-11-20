---
name: conversation-mode
description: Control how ChatGPT collaborates with the user through Default Mode or Condensed Mode. Use when the user asks to switch conversation style, work mainly in the repository with minimal chat output, or return to normal conversational responses.
metadata:
  project-role: foundational
  format: agentskills
  created: "2026-11-18T13:18"
  updated: "2026-11-20T12:03"
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

### Open discussion register

Use `workspace/discussion.md` as a temporary register for unresolved discussions. This file is not a conversation transcript or task index.

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

### User-visible report

After repository work, keep the report minimal and direct. Include navigation links whenever the relevant GitHub paths exist.

Use this order:

1. **Outcome:** one short sentence.
2. **Task:** direct link to the task record or task board.
3. **Changes:** direct links to the changed files.
4. **Commit:** direct link to the actual commit.
5. **Next:** one short next action or blocker, when applicable.

Do not provide a full progress narrative, routine tool details, or a long recap. Do not report only a raw commit hash when useful navigation links are available.

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

## 6. Skill source of truth and Library synchronization

GitHub is the canonical source of truth for all project skills. The repository is `dungnv2602/chatgpt`. The authorized branch is `gpt`. The canonical skill files are under `skills/`.

Whenever the user asks you to read, inspect, or follow a project skill:

1. Fetch the requested skill from the GitHub `gpt` branch before you rely on a Library copy.
2. If the skill cites supporting files, resolve and read them from the same branch. Stay inside the approved project directories.
3. Treat the ChatGPT Library as a mirror for convenient access, not as an independent authority.
4. If GitHub access fails or a file cannot be verified, disclose that limit. Do not silently use a Library copy instead.

Whenever you create or change a skill in GitHub:

1. Commit the authoritative change to branch `gpt`.
2. Fetch the committed path again. Verify its contents.
3. Synchronize the matching Library copy from the verified GitHub version. Create the Library copy if it does not exist.
4. Compare the Library content with the GitHub content. Do not rely only on filenames or timestamps.
5. Report any synchronization failure or unresolved conflict.

Before you use a Library skill copy, verify that it matches the current GitHub version. If it differs, use the verified GitHub version. Repair the Library mirror when the required file operations are available.

Do not remove or overwrite a conflicting Library item until you verify its identity and contents. Preserve unrelated Library artifacts, including archives and ZIP packages, unless the user explicitly asks you to replace or remove them.

This synchronization is an explicit workflow requirement. It does not mean that GitHub and the ChatGPT Library sync automatically in the background.

## Technical documentation standard

Follow the [ASD-STE100 skill](../asd-ste100/SKILL.md) when you create or revise skill files or technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for explanatory documentation. Preserve meaning, scope, and modality.
