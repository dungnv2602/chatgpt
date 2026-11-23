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

Repair a failure only when the newest run for an applicable workflow finishes with a failure conclusion. Inspect its jobs and logs. Repair the cause on branch `gpt`.

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

## Remote-only repository operations

The repository on GitHub is the only project workspace. Do not assume that a local checkout or local execution environment exists.

- Read, search, inspect, create, update, move, and delete repository files through the GitHub connector and GitHub APIs. Use exact paths and branch `gpt`.
- The only archive-retention index exception is `.github/archive-retention-index.json`. Read or update it only to register the exact path and UTC archive timestamp of a task record during closeout. Never enumerate `archive/tasks/` to backfill the index.
- Never use local shell, Git, Python, container, filesystem, or similar execution tools to clone, pull, checkout, inspect, edit, test, build, or commit repository work.
- Create commits and update refs through GitHub's remote APIs. Read back every changed path and verify the resulting branch head.
- Run repository scripts, tests, and validation only on GitHub-hosted Actions runners when an approved workflow invokes them. Inspect their results through GitHub Actions logs and artifacts. Do not reproduce them locally.

This rule is mandatory because no local project environment is provided and the GitHub repository is the sole source of truth. A local checkout may be absent, stale, or detached from the authorized branch. A local test result cannot validate the current remote commit and must never be reported as repository verification.

## Workspace structure

- workspace/README.md defines workspace navigation and operating rules.
- workspace/discussion.md stores one active pre-step brief, anything awaiting user input, unresolved failures, and the three most recent successful reports in Condensed Mode. Conversation Mode owns this file.
- workspace/task_board.md indexes active, ready, blocked, proposed, and historical tasks.
- workspace/TASK_TEMPLATE.md defines the task record format.
- workspace/tasks/ contains current task records.
- archive/README.md defines archive retention.
- archive/tasks/ contains completed or cancelled task records during retention.
- Treat `archive/` as read-only after each record's initial archive write. You may read an exact archived record when a task requires its content. Do not perform broad archive scans or audits unless the user asks.
  - Create the final task record in `archive/tasks/` as the initial archive write.
  - Read back that exact path and verify its complete content.
  - After verification, never edit, replace, rename, move, or manually delete the archived record.
  - Update the active task board with a link to the archived record and the archival commit.
  - Only the scheduled retention workflow may delete expired archive contents.
  - For links from active documents to archived paths, check path existence. Read the target when its content is needed for the task.

Do not create a conversation transcript. The discussion register is a temporary record of open discussions and a short success-report window, not a transcript or task history.

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

## Document authoring gate

Before a repository task creates or materially revises a document, load `skills/document-standards/SKILL.md` and its Document Type Catalog.

- Identify the document type and its owner.
- Retrieve and use its canonical template, schema, or embedded contract.
- Follow the owning project's workflow in addition to the general document standard.
- Record a missing template when a recurring type has no canonical format.
- Do not invent a new structure or migrate unrelated historical documents.

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

Conversation Mode controls access to workspace/discussion.md. The Worker must not read or write that file directly. In Condensed Mode, Conversation Mode reads and updates it. It publishes one short, committed Current Step brief before each meaningful work step, then maintains open discussions and up to three recent successful reports. The Worker does not write the brief or otherwise access the register.

If the board and task record disagree, reconcile them against the latest user instruction and actual repository state. Record the correction.

Ask the user only when a genuine decision, missing requirement, or approval blocks safe progress.

## Task completion and archive

Task closeout is a mandatory workflow transaction. The Worker owns it in every conversation mode. Condensed Mode does not change or shorten these steps.

Use only the canonical task statuses in this skill: Proposed, Ready, In Progress, Blocked, Paused, Done, and Cancelled. Do not use alternate values such as "Completed".

The Worker closes a task only after it archives the record and reconciles the task board.

**Archive gate — do not mark an active record Done prematurely.** Keep the active task record In Progress and Archived: No until the archive copy exists and its write has been verified. Prepare the final Done/Cancelled and Archived: Yes content for the archive destination; do not commit those final metadata values to the active path. Create the archive copy first. Only after the archive path exists may you remove the active path and reconcile the board. Move the board row to Historical only after the archive commit exists, and link that exact commit. If any step remains incomplete, leave the task open and report the exact blocker. This prevents a status label from claiming an archival operation that never happened.

When acceptance criteria are met:

1. Check the final result, acceptance criteria, and supporting evidence.
2. Prepare the final archive copy with status Done or Cancelled, an archive timestamp in UTC, complete verification, and a final handoff. Set Archived to Yes in that archive copy only.
3. Check whether `archive/tasks/<same-filename>` already exists. If it does, read it and compare its complete content with the prepared final record. Reuse it only when the content matches. Stop if the content differs. Never overwrite an existing archive record.
4. If the archive path does not exist, create it once. Preserve the task ID and filename. This is the only content write for that archive path.
5. Read the exact archive path after the write. Compare its complete content with the prepared final record. Verify the archive commit and changed-path metadata. If you reuse an existing copy, recover the original commit that introduced or contains that archive path from the task board or GitHub history. Never substitute a later board-update commit. Stop if the path is missing or the content differs.
6. Add one entry to `.github/archive-retention-index.json` with the exact archive path and UTC archive timestamp from the verified record. Preserve all existing entries. Verify the new entry. Do not enumerate `archive/tasks/` or backfill other records.
7. Treat the archive record as immutable after this verification. You may read it later when task recovery, board reconciliation, or verification requires it. Never edit, replace, rename, move, or manually delete an archived record. Only the scheduled retention workflow may delete indexed archived records.
8. Only after archive read-back and retention-index verification succeed, delete the active record from `workspace/tasks/`. Keep the active record In Progress with Archived: No until this deletion succeeds. If deletion fails, leave the task open and reconcile the existing archive copy without rewriting it.
9. Update `workspace/task_board.md` in the same closeout pass:
   - Delete the task from Current Execution.
   - Delete its active row from every status section.
   - Add one Historical row with status Done or Cancelled, the archive path, and the exact commit that contains the archived record.
   - Apply the seven-entry history limit. Delete only the oldest index rows when required.
   - Select or identify the next current execution task according to the selection rules. Do not invent a task when no eligible task exists.
10. Fetch the committed task board. Verify that the closed task is absent from active sections and appears exactly once in Historical. Verify its links to the archive path and archival commit. Verify that Current Execution matches the selection rules.
11. Verify that the archival commit includes the archived record in its changed-path metadata. Read the archived record when needed to verify its content or recover board details. Do not modify the archived record.
12. Only after these checks, report the task as closed and provide the appropriate handoff.

Treat the task record, archive path, and task board as one logical transaction even when the GitHub API requires more than one commit. Do not stop after changing task metadata, after creating the archive copy, or after deleting the active record.

If any closeout step fails, keep the task open as In Progress or record the exact recovery blocker. Reconcile the partial repository state before switching tasks or ending work. Do not claim completion while the board and task record disagree. Do not ask the user to approve routine archival or board maintenance. The approved task requires this archival and board maintenance.

Follow archive/README.md for the 90-day per-record retention policy. The Worker may read exact archived records when needed but must not edit, replace, rename, move, or manually delete them. Only the scheduled GitHub Actions retention workflow may delete indexed archived records.

## Conversation Mode integration

The Worker applies in every conversation mode.

- Default Mode may explain decisions and progress in more detail.
- Condensed Mode uses minimal status reports and direct navigation links.
- Neither mode changes task authority, approval state, progress logging, or recovery.
- Record detailed progress in task files instead of repeating it in chat.
- Conversation Mode owns the temporary register. The Worker does not read or write workspace/discussion.md. The register contains one active Current Step brief, unresolved discussions, and up to three recent successful reports. The brief is a navigation aid, not a task log. Task records remain authoritative for detailed progress and verification.
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
