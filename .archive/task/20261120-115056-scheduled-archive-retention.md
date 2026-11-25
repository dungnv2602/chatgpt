# Task: Automate 14-day archive retention with GitHub Actions

## Metadata

- **ID:** 20261120-115056
- **Created:** 2026-11-20 11:50 UTC
- **Updated:** 2026-11-20 12:24 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Approved
- **Current execution:** No
- **Dependencies:** None
- **Related tasks:** 20261120-112500
- **Archived:** Yes
- **Archive timestamp:** 2026-11-20T12:24:35Z

## 1. Original Request

"I want to prevent unnecessary read, so use Recurring Cron Schedules (schedule) - GitHub's native schedule event to automatically delete them. The skill github action skill should deal with scheduled deletion from now on."

## 2. Subsequent Instructions

- 2026-11-20 11:50 UTC — User: "The scheduled deletion workflow should be reusable when it done its job."
- 2026-11-20 11:50 UTC — User: "Approve."
- 2026-11-20 11:50 UTC — User: "Start session."
- 2026-11-20 11:52 UTC — User: "My mistake, the policy is 14 days."
- The user clarified that retention is a periodic batch operation: delete the contents of `archive/tasks/` together every 14 days, not 14 days after each record's own archive timestamp.
- 2026-11-20 — User: "You only need to delete gpt, then merge gpt to main, no need to delete both. It will conflicts since gpt always ahead."

## 3. Objective

Implement a reusable GitHub Actions workflow that periodically purges the complete task archive in one batch every 14 days, then fast-forwards `main` to the updated `gpt` branch. GitHub Actions owns scheduled archive deletion.

## 4. Acceptance Criteria

- [x] Use GitHub's native `schedule` event.
- [x] Purge the full contents of `archive/tasks/` as a batch after at least 14 days; do not calculate per-record expiry.
- [x] Preserve `.gitkeep`.
- [x] Preserve compact task-board history and archival commit links.
- [x] Support reusable invocation through `workflow_call`.
- [x] Support operator invocation through `workflow_dispatch`, with an explicit force input.
- [x] Use a committed UTC marker because GitHub cron has no exact every-14-days expression.
- [x] Run from default branch `main`, clean `gpt`, then atomically fast-forward `main` to the same commit.
- [x] Refuse to push if `main` is not an ancestor of `gpt`; never force-push.
- [x] Keep cleanup scoped to the archive directory and its state marker.
- [x] Remove archive-cleanup responsibility from The Worker skill.
- [x] Assign scheduled deletion ownership to the GitHub Actions skill.
- [x] Keep implementation on `gpt` and synchronize `main` only through the authorized fast-forward.

## 5. Implementation

- Added `.github/workflows/archive-retention.yml` with weekly schedule, reusable `workflow_call`, operator `workflow_dispatch`, explicit contents-write permission, concurrency protection, branch ancestry validation, and an atomic fast-forward push to both refs.
- Added `.github/scripts/cleanup-archive.py`. It removes every item under `archive/tasks/` except `.gitkeep` when the 14-day interval is due. It supports an explicit `--force` option for operator-triggered cleanup.
- Added `.github/archive-retention-state.json` to persist the last successful batch-cleanup timestamp in UTC.
- Rewrote `archive/README.md` to define batch retention rather than rolling per-record expiry.
- Updated `skills/github-actions/SKILL.md` to own the scheduled cleanup design and branch synchronization.
- Updated `skills/the-worker/SKILL.md` to prohibit Worker-side archive scanning and deletion.
- Preserved task-board historical records and their archival commit links.

## 6. Decisions

- Retention means deleting the entire current archive folder contents as a batch, not keeping each record for 14 days after its individual archive timestamp.
- The scheduled workflow runs weekly and checks a committed timestamp. A cleanup is due only after at least 14 days; under normal schedule delivery, the weekly Monday run executes on the first scheduled date after the interval.
- Cleanup is performed on `gpt` only. The same commit is atomically pushed to `gpt` and `main`, which fast-forwards `main` without a merge commit or force push.
- If branch ancestry is not fast-forwardable, the workflow fails before modifying either ref.
- `.gitkeep` and task-board history remain.

## 7. Progress Log

### 2026-11-20 12:20 UTC

- **Action:** Inspected the GitHub Actions skill, existing workflow conventions, Worker skill, archive policy, task board, archive contents, and branch heads.
- **Result:** `main` and `gpt` were aligned at `a6647fe3db4418645b9f660c1182e68d8d468db7`. The archive contained two task records and `.gitkeep`. The archive documentation still described rolling per-record expiry.

### 2026-11-20 12:24 UTC

- **Action:** Added the scheduled/reusable workflow, cleanup script, state marker, and policy/skill documentation. Committed the implementation on `gpt`.
- **Result:** Implementation commit `30083015efc1d8e43399cabd3a372ac9c5355c46`.
- **Action:** Corrected the cleanup script's JSON newline output.
- **Result:** Fix commit `29681a6cfbbe05550485a7f89dd1d74150aa3856`.
- **Action:** Fast-forwarded `main` to the same `gpt` commit.
- **Result:** Both branches point to `29681a6cfbbe05550485a7f89dd1d74150aa3856`.
- **Verification:** Read back all eight changed paths. Tested the cleanup logic in a temporary directory: a due run removed files and nested directories, preserved `.gitkeep`, and wrote valid JSON; a not-yet-due run preserved archive contents.
- **Limitations:** The scheduled workflow has not yet reached its first scheduled run. CI was not manually dispatched, polled, or inspected.

## 8. Final State

Implementation is committed and synchronized. The scheduled workflow exists on the default branch `main`, checks out `gpt`, and performs the batch cleanup only when the UTC marker indicates that at least 14 days have elapsed. It then atomically advances both refs to the same commit.

## 9. Verification

- **Repository read-back:** Passed for the workflow, cleanup script, state marker, archive README, Worker skill, GitHub Actions skill, task record, and task board.
- **Cleanup behavior test:** Passed for due cleanup, recursive removal, `.gitkeep` preservation, valid state JSON, and early-run no-op behavior.
- **Branch synchronization:** Passed. `main` and `gpt` both point to `29681a6cfbbe05550485a7f89dd1d74150aa3856`.
- **CI:** Not inspected, in accordance with repository policy.
- **Scheduled execution:** Not yet observed; the first scheduled run remains future behavior.

## 10. Handoff

The task is complete. Future scheduled archive cleanup is owned by GitHub Actions. The Worker must not scan or delete archived task records during activation or closeout. If `main` and `gpt` diverge, the scheduled workflow will stop safely until the branch relationship is restored.
