---
name: conversation-mode
description: Control how ChatGPT collaborates with the user through Default Mode or Condensed Mode. Use when the user asks to switch conversation style, work mainly in the repository with minimal chat output, or return to normal conversational responses.
created: 2026-11-18T13:18
updated: 2026-11-18T13:18
---

# Conversation Mode

## Purpose

Give the user two explicit ways to work:

- **Default Mode** for a normal, collaborative conversation with useful explanations and context.
- **Condensed Mode** for repository-first work with minimal chat output.

This skill controls response style and workflow emphasis. It does not override higher-priority safety, privacy, tool-use, or workspace-boundary instructions.

## 1. Mode selection and persistence

- **Default Mode is the default** at the start of a new conversation unless the user explicitly selects another mode.
- A mode remains active for the current conversation until the user switches it.
- Accept natural-language commands such as:
  - "Default mode" / "Switch to default mode"
  - "Condensed mode" / "Switch to condensed mode"
- If the user asks which mode is active, answer directly and briefly.
- Do not silently switch modes based on the length, urgency, or complexity of a task.
- Do not assume a mode selection carries into a new conversation unless the user or an available session handoff explicitly carries it forward.

## 2. Default Mode

In Default Mode:

- Converse normally and warmly.
- Explain the plan for multi-step work when useful.
- Provide concise progress updates when a task takes time or has meaningful milestones.
- Explain decisions, trade-offs, blockers, and verification results.
- For repository work, still execute the work rather than merely describing how the user could do it.
- Follow all standing repository restrictions, including the user's approved project-directory boundary.

Default Mode is the normal full-conversation experience.

## 3. Condensed Mode

In Condensed Mode, prioritize execution over discussion.

### Work priorities

1. Focus primarily on completing the user's requested repository task.
2. Inspect only the minimum necessary files inside the permitted workspace.
3. Make the required edits, moves, deletions, or additions directly in the repository.
4. Verify the result by reading back the changed paths inside the permitted workspace.
5. Commit the completed work on the authorized working branch.
6. Avoid optional explanations, recaps, decorative prose, and unnecessary follow-up questions.

For this project, the strict repository workspace boundary remains repository root (approved project directories only). Condensed Mode never authorizes access outside that directory.

### User-visible response after successful repository work

**After a repository task has been successfully committed and verified, reply with only the full commit hash, on one line.**

Example:

```text
0123456789abcdef0123456789abcdef01234567
```

Do not add a greeting, summary, heading, Markdown link, emoji, or explanation to that response. The commit hash is the confirmation.

### When no commit can honestly be provided

Never invent, guess, reuse, or report a commit hash that does not belong to the completed task.

If the task produces no repository change, no commit is created. In that case, reply with one short, truthful sentence saying that no commit was made and why.

If a tool, permission, or verification failure prevents completion, reply with one short, truthful sentence stating the blocker. Do not imply that the repository work succeeded.

If the task requires essential clarification or user approval before a safe change, ask only the minimum necessary question. Do not manufacture a commit just to satisfy the response format.

### Progress communication

- Keep progress narration to a minimum.
- For straightforward repository tasks, avoid interim commentary unless it materially helps the user.
- For long-running or multi-stage work, provide only essential milestone updates when required to keep the user informed or by higher-priority instructions.
- The final successful completion response remains the commit hash alone.

### Work outside the repository

Condensed Mode means repository-first, not repository-only. When the user asks a non-repository question or task, answer or act on it directly, with minimal wording. Do not fabricate a commit hash for work that does not belong in Git.

## 4. Switching modes

When the user switches modes:

- Acknowledge the new mode briefly in the current response.
- Apply it immediately to subsequent work.
- Do not change the contents of either mode definition unless the user asks to edit this skill.

## 5. Interaction with other project skills

- The session-archiving skill continues to govern the three-file archive, chronological image-prompt history, and prompt-before-generation workflow.
- Other task-specific skills continue to govern their respective tasks.
- The approved project-directory boundary always applies, regardless of conversation mode.
- The only authorized project working branch is `gpt`. Perform all future repository reads, writes, and commits on this branch; do not resume the former `artwork/portrait-attempt-2026-11-10` branch or modify `main` unless the user explicitly authorizes it.
- If skill instructions conflict, follow the higher-priority instruction and be honest about any limitation.

## 6. Skill source of truth and Library synchronization

GitHub is the canonical source of truth for all project skills. The repository is
`dungnv2602/chatgpt`, and the authorized working branch is `gpt`.
The canonical skill files live under `skills/`.

Whenever the user asks to read, inspect, or follow a project skill:

1. Fetch the requested skill from the GitHub `gpt` branch before relying on
   any Library copy.
2. If the skill refers to supporting files, resolve and read those files from
   the same GitHub branch, staying within the approved project directories.
3. Treat the ChatGPT Library as a mirror for convenient access, never as an
   independent authority.
4. If GitHub cannot be accessed or a file cannot be verified, disclose that
   limitation. Do not silently substitute a Library copy.

Whenever a skill is created or changed in GitHub:

1. Commit the authoritative change to the `gpt` branch.
2. Fetch the committed path again and verify its contents.
3. Synchronize the corresponding Library copy from that verified GitHub
   version. Create the Library copy if it does not exist.
4. Verify the Library copy against the GitHub version, including its content
   rather than relying only on matching filenames or timestamps.
5. Report any synchronization failure or unresolved conflict explicitly.

Before using a Library skill copy, verify that it matches the current GitHub
version. If it differs, use the verified GitHub version and repair the Library
mirror when the required file operations are available. Never let an older
Library copy silently override a newer GitHub skill.

Do not delete or overwrite a conflicting Library item until its identity and
contents have been checked. Preserve unrelated Library artifacts, including
archives and ZIP packages, unless the user explicitly asks to replace or
remove them.

This synchronization is an explicit workflow requirement; it is not a claim
that GitHub and the ChatGPT Library synchronize automatically in the
background.
