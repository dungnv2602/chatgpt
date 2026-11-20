---
name: conversation-mode
description: Control how ChatGPT collaborates with the user through Default Mode or Condensed Mode. Use when the user asks to switch conversation style, work mainly in the repository with minimal chat output, or return to normal conversational responses.
metadata:
  project-role: foundational
  format: agentskills
  created: "2026-11-18T13:18"
  updated: "2026-11-18T13:18"
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

Default Mode is the normal full-conversation experience.

## 3. Condensed Mode

In Condensed Mode, prioritize execution over discussion.

### Work priorities

1. Focus on completing the requested repository task.
2. Inspect only the files needed inside the permitted workspace.
3. Make the required edits, moves, deletions, or additions in the repository.
4. Read back the changed paths inside the permitted workspace.
5. Commit the completed work on the authorized working branch.
6. Avoid optional explanations, recaps, decorative prose, and unnecessary follow-up questions.

The strict repository workspace boundary remains the approved project directories at the repository root. Condensed Mode does not authorize access outside those directories.

### User-visible response after successful repository work

After you commit and verify a repository task, reply with only the full commit hash on one line.

Example:

```text
0123456789abcdef0123456789abcdef01234567
```

Do not add a greeting, summary, heading, Markdown link, emoji, or explanation.

### When no commit can honestly be provided

Never invent, guess, reuse, or report a commit hash that does not belong to the completed task.

If the task produces no repository change, do not create a commit. Reply with one short, truthful sentence that explains why.

If a tool, permission, or verification failure prevents completion, reply with one short, truthful sentence that states the blocker. Do not imply success.

If the task needs essential clarification or user approval before a safe change, ask only the minimum necessary question. Do not create a commit only to satisfy the response format.

### Progress communication

- Keep progress messages to a minimum.
- For a straightforward repository task, avoid interim commentary unless it materially helps the user.
- Give essential milestone updates on long or multi-stage tasks when they help the user or a higher-priority instruction requires them.
- After successful work, the final response must still contain only the commit hash.

### Work outside the repository

Condensed Mode means repository-first, not repository-only. When the user requests a non-repository task, answer or act on it directly with minimal wording. Do not invent a commit hash for work outside Git.

## 4. Switching modes

When the user switches modes:

- Acknowledge the new mode briefly in the current response.
- Apply it to later work immediately.
- Do not change either mode definition unless the user asks you to edit this skill.

## 5. Interaction with other project skills

- Session Archiving governs the three-file archive, chronological image-prompt history, and prompt-before-generation workflow.
- Other task-specific skills govern their own tasks.
- The approved project-directory boundary always applies, regardless of conversation mode.
- The only authorized working branch is `gpt`. Use it for repository reads, writes, and commits.
- Do not resume the former `artwork/portrait-attempt-2026-11-10` branch.
- Do not modify `main` unless the user authorizes it.
- When skill instructions conflict, follow the higher-priority instruction. State any limitation honestly.

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

Before you use a Library skill copy, check that it matches the current GitHub version. If it differs, use the verified GitHub version. Repair the Library mirror when the required file operations are available.

Do not delete or overwrite a conflicting Library item until you check its identity and contents. Preserve unrelated Library artifacts, including archives and ZIP packages, unless the user explicitly asks you to replace or remove them.

This synchronization is an explicit workflow requirement. It does not mean that GitHub and the ChatGPT Library sync automatically in the background.

## Technical documentation standard

Follow the [ASD-STE100 skill](../asd-ste100/SKILL.md) when you create or revise skill files or technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for explanatory documentation. Preserve meaning, scope, and modality.
