# Task: Automate 14-day archive retention with GitHub Actions

## Metadata

- **ID:** 20261120-115056
- **Created:** 2026-11-20 11:50 UTC
- **Updated:** 2026-11-20 12:03 UTC
- **Priority:** P1
- **Status:** Blocked
- **Origin:** User
- **Approval:** Approved
- **Current execution:** No
- **Dependencies:** User decision on GitHub default-branch strategy
- **Related tasks:** 20261120-112500
- **Archived:** No

## 1. Original Request

"I want to prevent unnecessary read, so use Recurring Cron Schedules (schedule) - GitHub's native schedule event to automatically delete them. The skill github action skill should deal with scheduled deletion from now on."

## 2. Subsequent Instructions

- 2026-11-20 11:50 UTC — User: "The scheduled deletion workflow should be reusable when it done its job."
- 2026-11-20 11:50 UTC — User: "Approve."
- 2026-11-20 11:50 UTC — User: "Start session."
- 2026-11-20 11:52 UTC — User corrected the retention policy: "My mistake, the policy is 14 days." This confirms a 14-day period, but does not resolve the default-branch blocker.

## 3. Objective

Replace Worker-triggered archive cleanup with a reusable GitHub Actions scheduled cleanup workflow. Assign workflow ownership and operational instructions to the GitHub Actions skill.

## 4. Requirements

- Use GitHub's native `schedule` event with a recurring cron expression.
- Retain archived task records for 14 days from their recorded UTC archive timestamp.
- Delete only expired records from `archive/tasks/`.
- Preserve compact historical task-board entries and links to archival commits.
- Make cleanup reusable by supporting an operator-triggered run and reusable cleanup logic.
- Make cleanup idempotent. Repeated runs must not change unexpired records.
- Minimize reads. Do not scan unrelated workspace files.
- Remove archive-cleanup responsibility from The Worker skill.
- Assign scheduled deletion ownership to the GitHub Actions skill.
- Work on branch `gpt`. Do not modify `main` or repository settings without explicit user authorization.

## 5. Decisions

- User approved implementation.
- The user confirmed the retention policy is 14 days.
- The workflow should use a reusable cleanup implementation and support manual invocation.
- GitHub Actions `schedule` only runs when the workflow file exists on the repository's default branch.
- The repository default branch is currently `main`. The authorized working branch is `gpt`.
- **Blocked:** Obtain explicit user authorization to change the default branch to `gpt`, or to place the required scheduled workflow on `main`. Do not proceed with either change without that authorization.

## 6. Progress Log

### 2026-11-20 11:50 UTC

- **Action:** Completed foundational session initialization and recovered the task workspace.
- **Result:** All required foundational skills were retrieved from branch `gpt`. The task board had no active task. The existing archive policy assigns cleanup to Worker activation and task closeout.
- **References:** `skills/SESSION_START.md`, `skills/session-archiving/SKILL.md`, `skills/conversation-mode/SKILL.md`, `skills/the-worker/SKILL.md`, `skills/agent-skill-authoring/SKILL.md`, `skills/asd-ste100/SKILL.md`, `skills/github-actions/SKILL.md`, `workspace/README.md`, `workspace/task_board.md`, `archive/README.md`.
- **Next:** Resolve the default-branch authorization blocker.

### 2026-11-20 11:52 UTC

- **Action:** Created the task record and added it to the task board. Read back both changed files.
- **Result:** Both files match the intended content. Task record commit: `4a4a02ace9b3c9bb98405ddaa411de5d3b88de7c`. Task board commit: `e059a34dc942e0bb6c5e8500223b8b02bf448017`.
- **References:** [Task record commit](https://github.com/dungnv2602/chatgpt/commit/4a4a02ace9b3c9bb98405ddaa411de5d3b88de7c), [Task board commit](https://github.com/dungnv2602/chatgpt/commit/e059a34dc942e0bb6c5e8500223b8b02bf448017).
- **Next:** Resolve the default-branch authorization blocker.

### 2026-11-20 11:51 UTC

- **Action:** Inspected the repository branch and workflow directory. Checked GitHub's current schedule-event documentation.
- **Result:** Branch `gpt` points to `f9e1705417c3d9646b51a0b8c72a540391b936dd`. The repository default branch is `main`. GitHub states that scheduled workflows run only from the default branch. No archive-cleanup workflow exists in `.github/workflows/`.
- **References:** [Branch gpt](https://github.com/dungnv2602/chatgpt/tree/gpt), [workflow directory](https://github.com/dungnv2602/chatgpt/tree/gpt/.github/workflows), [GitHub schedule event documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).
- **Next:** Ask the user to authorize one default-branch strategy. Do not modify `main` or repository settings before approval.

## 7. Current State

No implementation changes have been made. The task is blocked by GitHub's default-branch requirement and the repository's branch authorization rule.

## 8. Remaining Work

- Resolve the default-branch strategy.
- Inspect only the existing workflow and cleanup-related paths required for implementation.
- Implement reusable cleanup logic and the scheduled workflow.
- Update GitHub Actions, Worker, and archive-retention documentation.
- Validate the cleanup logic, workflow syntax, retention boundary, and idempotency.
- Commit the related changes coherently to the authorized branch.
- Read back and verify every changed path.

## 9. Next Actions

1. Obtain explicit authorization to change the repository default branch to `gpt`, or to add the scheduled workflow to `main`.
2. Resume implementation only after the user resolves this authorization blocker.

## 10. References

- [GitHub Actions skill](../../skills/github-actions/SKILL.md)
- [The Worker skill](../../skills/the-worker/SKILL.md)
- [Archive policy](../../archive/README.md)
- [GitHub schedule event documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- Related task: `20261120-112500`

## 11. Verification

- **Check:** Foundational initialization.
- **Method:** Retrieved and read all six required skill files from branch `gpt`.
- **Result:** Passed.
- **Limitations:** This does not validate the future workflow.

- **Check:** Repository default branch and branch head.
- **Method:** Read GitHub repository and branch metadata.
- **Result:** Default branch is `main`. Branch `gpt` points to `f8c83048627821b11f95d0e3cc15eb96ea7e3c1e`.
- **Limitations:** No branch settings were changed.

- **Check:** Scheduled workflow requirement.
- **Method:** Reviewed current GitHub documentation.
- **Result:** GitHub runs scheduled workflows only when the workflow file exists on the default branch.
- **Limitations:** The workflow has not been created or run.

## 12. Handoff Instructions

Wait for the user's explicit decision on the default-branch strategy. Keep all project changes on `gpt` unless the user authorizes a narrowly scoped change on `main`. Do not manually dispatch, poll, or inspect CI. Resume from the default-branch decision.
