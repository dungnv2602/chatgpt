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
3. Make the required edits, moves, removals, or additions in the repository.
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
- Give milestone updates on long tasks when they help the user or higher-priority instructions require them.
- After successful work, the final response must still contain only the commit hash.

### Work outside the repository

Condensed Mode means repository-first, not repository-only. When the user requests a non-repository task, answer or act on it directly with minimal wording. Do not invent a commit hash for work outside Git.

## 4. Switching modes

When the user switches modes:

- Acknowledge the new mode briefly in the current response.
- Apply it to later work immediately.
- Do not change either mode definition unless the user asks you to edit this skill.

## 5. Interaction with other project skills

- GitHub Actions workflow design, maintenance, security, and verification are governed by the [GitHub Actions skill](../github-actions/SKILL.md).

- Session Archiving governs the three-file archive, chronological image-prompt history, and prompt-before-generation workflow.
- Other task-specific skills govern their own tasks.
- The approved project-directory boundary always applies, regardless of conversation mode.
- The only authorized working branch is `gpt`. Use it for repository reads, writes, and commits.
- Do not resume the former `artwork/portrait-attempt-2026-11-10` branch.
- Do not change `main` unless the user authorizes it.
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

Before you use a Library skill copy, verify that it matches the current GitHub version. If it differs, use the verified GitHub version. Repair the Library mirror when the required file operations are available.

Do not remove or overwrite a conflicting Library item until you verify its identity and contents. Preserve unrelated Library artifacts, including archives and ZIP packages, unless the user explicitly asks you to replace or remove them.

This synchronization is an explicit workflow requirement. It does not mean that GitHub and the ChatGPT Library sync automatically in the background.


## 7. Repository CI preflight and checkpoint policy

Apply this policy to every user turn that may involve repository work, in both conversation modes.

### Before acting on a user request

1. Inspect GitHub Actions runs for branch `gpt` before you execute the user's new repository request.
2. Check the newest run for each applicable workflow. Also check every pending run ID carried from the previous turn.
3. A newer run for the same workflow supersedes an older run on an earlier commit. Do not treat an obsolete cancelled run or a failure superseded by a later successful run as an active CI failure.
4. If the latest applicable run failed, inspect its job logs, identify the cause, and fix the repository issue before you start the user's requested task. Do not defer a known failure.
5. If the failure came from a previous assistant change, correct that change first. If it came from the user's existing project state, make the smallest relevant correction on branch `gpt`. Do not hide a failure by changing a lint baseline or weakening a check.
6. After you commit the correction, read back the changed files. Then continue with the user's request. Do not wait for the correction's new CI run; track it as pending for the next turn.
7. If a relevant run remains in progress, report that status once and continue with the user's request. Do not wait or poll repeatedly.
8. If no applicable run exists, report that CI has no run for the relevant change. Do not imply that CI passed.

### During and after repository work

1. Do not wait for a GitHub Actions run during the task that triggered it.
2. Do not poll a run repeatedly while it is in progress.
3. At task completion, report each relevant run ID and the exact commit SHA it tested. Mark incomplete runs as pending.
4. Report a run as passed only when GitHub reports a successful conclusion.
5. Do not treat a pending or cancelled run as a pass. Do not describe a pending run as a failure.
6. Carry pending run IDs in the conversation handoff. At the next user turn, check their final results as part of the CI preflight.

## 8. Repository execution efficiency

Apply this workflow to every repository task. It supplements the CI checkpoint policy.

1. **Inspect once.** Check the branch head, relevant files, and required validation before editing. Check pending CI run IDs carried from the previous user turn before other work, as Section 7 requires. Do not check runs created during the current task.
2. **Plan the change set.** Identify the files and checks that the task requires. Do not expand the task into unrelated cleanup.
3. **Batch related edits.** Group changes by purpose and file. Avoid separate commits for small changes that can be reviewed and committed together.
4. **Minimize tool calls.** Reuse verified results. Do not repeat reads, searches, or status checks unless new evidence or a changed file requires them.
5. **Use targeted validation.** Run the narrowest relevant checks first. Run broader checks when the change or repository policy requires them. Do not repeat a successful check without a reason.
6. **Review meaning and scope.** Check the complete changed sections. Preserve facts, conditions, exceptions, numbers, scope, and modality.
7. **Verify the final state.** Read back each changed path after the commit. Confirm the branch head and commit result.
8. **Keep evidence precise.** Associate each check result with the exact commit SHA that it tested. A result for a descendant commit does not prove that an earlier commit passed.
9. **Track unresolved work.** Separate verified results, pending checks, blockers, and items that need user authorization. Carry pending CI run IDs into the next-turn handoff.
10. **Report once, accurately.** State the changed paths, commit SHA, checks performed, and unresolved items. Do not claim success without evidence.

### Efficiency constraints

- Do not make speculative edits.
- Do not create one-line commits when related changes can be grouped.
- Do not perform repeated wording reviews without a defined rule or finding.
- Do not wait for CI or poll an in-progress run. Follow Section 7.
- Do not reduce verification to save time. Reduce redundant operations instead.

## Technical documentation standard

Follow the [ASD-STE100 skill](../asd-ste100/SKILL.md) when you create or revise skill files or technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for explanatory documentation. Preserve meaning, scope, and modality.
