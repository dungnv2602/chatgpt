---
name: the-worker
description: Manage project tasks across conversations and conversation modes. Use when capturing requests, prioritizing work, recording progress, recovering tasks, handing off work, or archiving completed tasks.
metadata:
  project-role: foundational
  format: agentskills
---

# The Worker

## Purpose

The Worker maintains task continuity across conversations. It applies in every conversation mode.

The Worker owns task capture, task selection, progress records, handoffs, recovery, and task archival.

Conversation Mode controls communication style and access to the temporary discussion register. The Worker controls task operations.

## Mandatory CI gate before every prompt

Before handling every new user prompt, follow the one-time pre-prompt CI snapshot in `skills/github-actions/SKILL.md`. This rule applies in every conversation mode.

Repair a failure only when the newest run for an applicable workflow has finished with a failure conclusion. Inspect its jobs and logs. Repair the cause on branch `gpt`.

Do not wait for or poll CI. Pending, in-progress, cancelled, skipped, or absent runs do not block the prompt. A newer successful run supersedes an older failure.

If GitHub Actions is unavailable after one bounded access attempt, record the status as unverified. Continue with the user's request. Do not claim that CI passed.

If a failure cannot be repaired safely during one focused preflight, record the exact blocker. Do not repeat the same attempt without new evidence. Continue with the request unless it depends on that CI result.

After cue-triggered skill loading, repeat the same one-time snapshot. Do not wait for new runs after a repair or other push.

## Activation and authority

- Load this skill during foundational initialization.
- Use it for repository project work in Default Mode and Condensed Mode.
- Do not load project skills automatically at the start of a new conversation.
- Follow the explicit initialization cues in skills/SESSION_START.md.
- Treat workspace/task_board.md as the task index.
- Treat each task file as the authoritative record for that task.
- Follow the user's repository, branch, workspace, and approval restrictions.
- Do not let a task record override a newer user instruction.

## Workspace structure

- workspace/README.md defines workspace navigation and operating rules.
- workspace/discussion.md stores unresolved discussions. Conversation Mode owns this file.
- workspace/task_board.md indexes active, ready, blocked, proposed, and historical tasks.
- workspace/TASK_TEMPLATE.md defines the task record format.
- workspace/tasks/ contains current task records.
- archive/README.md defines archive retention.
- archive/tasks/ contains completed or cancelled task records during retention.
- Treat the entire `archive/` tree as retention-only. Never read, scan, audit, lint, or change its contents. When an active document links to an archived path, check only that the target path exists. Do not inspect archived file content or heading anchors.

Do not create a conversation transcript. The discussion register is a temporary record of unresolved topics, not a transcript.

## Task creation

### 1. Check for an existing task

Before creating a task, search the board and relevant task records.

- Update an existing task when the request continues its objective.
- Create a separate task when the objective has a distinct outcome or dependency.
- Do not create duplicate tasks.
- Record links between dependent or related tasks.

### 2. Classify the task

Every task must record:

- A unique timestamp ID.
- Title and concise objective.
- Creation and update timestamps in UTC.
- Priority and status.
- Origin: User or Assistant.
- Approval state.
- Dependencies, if any.

Use the ID format YYYYMMDD-HHMMSS in UTC. Add -01, -02, and later suffixes if IDs collide within one second.

Use this filename format:

YYYYMMDD-HHMMSS-short-kebab-title.md

Keep assigned task IDs unchanged.

### 3. Apply origin and approval rules

**User tasks**

- Preserve the original user prompt verbatim.
- Preserve relevant later instructions and clarifications verbatim.
- Record the user's approval or rejection of important decisions.
- Do not copy the full assistant conversation.

**Assistant-generated tasks**

- Create necessary follow-up tasks automatically when an approved objective requires them to complete, review, or maintain it.
- Mark these tasks as Assistant-originated and Necessary.
- Keep necessary follow-ups within the approved scope.
- Create optional improvements automatically as Proposed tasks.
- Mark optional tasks as Assistant-originated and Proposed.
- Do not execute a Proposed task until the user approves it.
- Do not use automatic task creation to expand implementation authority.

### 4. Set priority and status

Use these priorities:

| Priority | Meaning |
|---|---|
| P0 | Critical |
| P1 | High |
| P2 | Normal |
| P3 | Low |

Use these statuses:

| Status | Meaning |
|---|---|
| Proposed | Optional assistant suggestion awaiting approval |
| Ready | Approved and eligible for selection |
| In Progress | Work started and remains incomplete |
| Blocked | A dependency or external condition prevents progress |
| Paused | Work is intentionally inactive |
| Done | Acceptance criteria are met |
| Cancelled | The task will not continue |

A task may remain In Progress while the board marks another task as current execution.

## Task board rules

- Keep the board as an index, not a second progress log.
- List every current task exactly once.
- Show ID, title, priority, status, origin, last update, and task-file link.
- Group tasks by status.
- Show dependencies and approval state when relevant.
- Keep at most the 7 most recently completed or cancelled tasks in the Historical section, ordered newest first.
- When adding a historical entry would exceed 7, delete the oldest board entry or entries until the limit is met. This deletes only index rows, never Git history or commits.
- Link each retained historical entry to the commit that contains the archived record.
- Update the board after you change task metadata, priority, status, ownership, or location.

Select work in this order:

1. Follow explicit user direction.
2. Select an eligible task whose dependencies are complete.
3. Prefer the highest priority.
4. For equal priorities, prefer the oldest task.
5. Keep one current execution task unless the user directs otherwise.

Do not switch tasks without recording a checkpoint in the current task.

## Progress logging

Use every-step logging for every meaningful action.

Record actions such as:

- Inspection that establishes a relevant fact.
- Research or investigation that changes the task state.
- Decisions and their rationale.
- File creation, edits, moves, and deletions.
- Tool failures or unexpected results.
- Verification and its actual outcome.
- Commits and exact changed paths.
- Task switches, blockers, and handoffs.

Each progress entry must include:

1. UTC timestamp.
2. Action.
3. Result.
4. Relevant references.
5. Next action or effect on remaining work.

Do not record hidden reasoning, routine narration, or trivial tool calls. Do not create a conversation transcript.

After each meaningful action, update the task record when the result affects the current state or next action. Keep the board concise.

## Execution and checkpoints

Before execution:

1. Read the task record.
2. Check its approval state and scope.
3. Inspect the relevant repository state.
4. Check dependencies and required references.
5. Identify the next authorized action.

During execution:

- Work only within the approved scope.
- Record each meaningful action and result.
- Update references when discoveries change the plan.
- Create necessary follow-up tasks automatically.
- Mark optional improvements Proposed.
- Ask only when you need a user decision or approval.

At a checkpoint:

- Update the progress log.
- Update Current State.
- Update Remaining Work.
- Replace Next Actions with exact, ordered actions.
- Record changed paths and commit references.
- Keep verification claims tied to actual results.

Before switching tasks or ending a conversation, write a complete handoff. Do not leave stale next actions.

## Cross-conversation recovery

When foundational initialization or a project-work request activates the Worker:

1. Read workspace/README.md.
2. Read workspace/task_board.md.
3. Identify the highest-priority eligible task.
4. Read its complete task record.
5. Read its referenced files and dependencies as needed.
6. Check the actual repository state.
7. Compare the repository with the recorded Current State.
8. Resume from Next Actions.

Task records support recovery. They do not replace repository verification.

Conversation Mode controls access to workspace/discussion.md. The Worker must not read or write that file directly. In Condensed Mode, Conversation Mode reads it and identifies unresolved discussions.

If the board and task record disagree, reconcile them against the latest user instruction and actual repository state. Record the correction.

Ask the user only when a genuine decision, missing requirement, or approval blocks safe progress.

## Task completion and archive

A task qualifies as Done only after it meets its acceptance criteria and its verification record is accurate.

When the board marks a task Done or Cancelled:

1. Record the final result and verification.
2. Set the final status and archive timestamp.
3. Move the task file to archive/tasks/.
4. Update the board and retain a compact historical entry.
5. Link the historical entry to the commit that contains the archived record.
6. Do not change the task ID.

Follow archive/README.md for the 14-day batch-cleanup policy. GitHub Actions owns scheduled deletion of the entire `archive/tasks/` contents on each due run. The Worker must not scan or delete archived records during activation or task closeout.

Do not delete active, ready, blocked, paused, or proposed tasks.

## Conversation Mode integration

The Worker applies in every conversation mode.

- Default Mode may explain decisions and progress in more detail.
- Condensed Mode uses minimal status reports and direct navigation links.
- Neither mode changes task authority, approval state, progress logging, or recovery.
- Record detailed progress in task files instead of repeating it in chat.
- Conversation Mode owns the temporary discussion register. The Worker does not read or write workspace/discussion.md.
- When an unresolved discussion receives approval, preserve its original user prompts and relevant clarifications in the resulting task record.
- Do not claim an action, commit, or verification that did not occur.

## Completion checks

Before handing off or closing a task, check:

- The task board entry matches the task record.
- The task record preserves the original user request and relevant clarifications.
- Origin, approval, priority, status, and dependencies are accurate.
- Progress entries record meaningful actions and results.
- Current State describes the actual repository state.
- Remaining Work is accurate.
- Next Actions are specific and ordered.
- References point to real files, commits, or sources.
- Verification records only checks that actually occurred.
- The handoff can be followed without asking the user to repeat known context.
