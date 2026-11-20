# Task: Automate 14-day archive retention with GitHub Actions

## Metadata

- **ID:** 20261120-115056
- **Created:** 2026-11-20 11:50 UTC
- **Updated:** 2026-11-20 12:30 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261120-112500
- **Archived:** No

## 1. Original Request

"I want to prevent unnecessary read, so use Recurring Cron Schedules (schedule) - GitHub's native schedule event to automatically delete them. The skill github action skill should deal with scheduled deletion from now on."

## 2. Subsequent Instructions

- 2026-11-20 11:50 UTC — User: "The scheduled deletion workflow should be reusable when it done its job."
- 2026-11-20 11:50 UTC — User: "Approve."
- 2026-11-20 11:50 UTC — User: "Start session."
- 2026-11-20 11:52 UTC — User: "My mistake, the policy is 14 days."
- 2026-11-20 12:xx UTC — User clarified that retention is a periodic batch operation: delete the contents of `archive/tasks/` together every 14 days, not 14 days after each record's own archive timestamp.
- 2026-11-20 12:xx UTC — User approved the branch strategy: cleanup only on `gpt`, then merge/fast-forward `gpt` to `main`; do not run a separate cleanup on `main`. The user expects `gpt` to remain ahead of `main`.

## 3. Objective

Implement a reusable GitHub Actions workflow that periodically purges the complete task archive in one batch every 14 days, then fast-forwards `main` to the updated `gpt` branch. GitHub Actions owns scheduled archive deletion.

## 4. Requirements

- Use GitHub's native `schedule` event.
- Perform a full-folder batch purge of `archive/tasks/` after each 14-day interval. Do not use per-record archive timestamps to determine deletion.
- Preserve `.gitkeep`.
- Preserve compact historical task-board entries and links to archival commits.
- Make cleanup reusable through `workflow_call` and operator-accessible through `workflow_dispatch`.
- Allow an explicit forced manual run; scheduled runs must respect the 14-day interval.
- Use a committed UTC marker to enforce the 14-day interval because GitHub cron does not express an exact 14-day cadence.
- Run the scheduled workflow from default branch `main`, check out and clean `gpt`, then atomically fast-forward `main` to the same commit.
- Never force-push. Verify `main` is an ancestor of `gpt`; if not, fail safely.
- Keep cleanup scoped to `archive/tasks/` and its state marker.
- Remove archive-cleanup responsibility from The Worker skill.
- Assign scheduled deletion ownership to the GitHub Actions skill.
- Work on branch `gpt`; update `main` only by the authorized fast-forward strategy.

## 5. Decisions

- User approved implementation.
- Retention semantics: batch purge of the entire archive folder every 14 days.
- Branch strategy: clean `gpt` only, then fast-forward `main` to the same resulting commit. No independent cleanup on `main`.
- The schedule runs weekly and checks a committed last-cleanup timestamp. This enforces at least 14 days between batch purges while avoiding a misleading day-of-month cron expression.
- A manual run may force cleanup only when the operator explicitly sets the `force` input.
- Preserve `.gitkeep` and task-board history.

## 6. Progress Log

### 2026-11-20 12:20 UTC

- **Action:** Recovered the approved task and inspected the GitHub Actions skill, existing workflow conventions, Worker skill, archive policy, task board, archive contents, and current branch heads.
- **Result:** `main` and `gpt` both point to `a6647fe3db4418645b9f660c1182e68d8d468db7`. The archive contains two task records and `.gitkeep`. Existing Worker instructions already prohibit archive scanning/deletion; documentation still incorrectly describes rolling per-record expiry.
- **Decision:** Implement cleanup on `gpt` only and atomically push the same cleanup commit to both refs after verifying `main` is an ancestor of `gpt`.
- **Next:** Add the scheduled/reusable workflow, cleanup script, state marker, and policy/skill documentation.

## 7. Current State

Implementation is being added on `gpt`. The workflow is designed to run from default branch `main`, clean `gpt`, and atomically fast-forward `main` to the same commit. The cleanup script uses a weekly schedule and UTC state marker to enforce the 14-day batch interval.

## 8. Remaining Work

- Commit the workflow, script, state marker, and documentation changes on `gpt`.
- Read back all changed paths.
- Fast-forward `main` to the resulting `gpt` commit, as authorized.
- Verify both branch heads and report the commit.

## 9. Next Actions

1. Create the coherent implementation commit on `gpt`.
2. Verify changed files and branch ancestry.
3. Fast-forward `main` to `gpt`.
4. Read back and verify the final branch heads.

## 10. References

- [GitHub Actions skill](../../skills/github-actions/SKILL.md)
- [The Worker skill](../../skills/the-worker/SKILL.md)
- [Archive policy](../../archive/README.md)
- [GitHub Actions schedule event documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- Related task: 20261120-112500

## 11. Verification

- **Check:** Current branch heads.
- **Method:** Read GitHub branch metadata for `main` and `gpt`.
- **Result:** Both point to `a6647fe3db4418645b9f660c1182e68d8d468db7`; neither branch is protected.
- **Limitations:** This does not validate the workflow or cleanup script.

## 12. Handoff Instructions

Keep implementation on `gpt`. The authorized synchronization method is a fast-forward of `main` to the resulting `gpt` commit after cleanup changes are committed. Never perform a separate cleanup on `main`, create a merge commit, or force-push.
