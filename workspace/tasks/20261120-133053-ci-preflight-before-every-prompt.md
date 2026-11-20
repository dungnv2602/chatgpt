# Task: Require CI preflight before every prompt and after skill loading

## Metadata

- **ID:** 20261120-133053
- **Created:** 2026-11-20 13:30 UTC
- **Updated:** 2026-11-20 13:33 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261120-123000
- **Archived:** No

## 1. Original Request

---
Do not inspect CI results unless you explicitly ask. When you ask, inspect failures and fix them.
---

Wrong. You must check and fix CI before taking my prompt, ve whatever it is. You always check CI and fix first. You also must check and fix CI after loading skills by following my cue. 

---

Update your workflow accordingly.

## 2. Subsequent Instructions

No subsequent clarifications recorded.

## 3. Objective

Make CI inspection and repair a mandatory gate before every user prompt. Repeat the gate after cue-triggered skill loading.

## 4. Requirements

- Inspect the latest applicable GitHub Actions run for each workflow on branch `gpt` before handling every user prompt. Check the current branch head status.
- Wait for applicable runs that remain in progress.
- Inspect failed jobs, steps, and logs. Fix the underlying cause before handling the prompt.
- Wait for the new applicable runs to pass after each repair. Repeat the repair cycle if needed.
- Repeat the CI gate after loading skills in response to `start session`, `start a drawing session`, or `Be the novelist`.
- Complete the post-load gate before project work or an initialization-complete report.
- Stop and report a blocker if GitHub Actions cannot be accessed or the required run state cannot be established.
- Never run the STE linter locally. Use GitHub Actions.
- Do not weaken tests, workflow coverage, or lint baselines to force a pass.
- Keep the rules consistent across the GitHub Actions skill, The Worker, Session Archiving, Session Start, Agent Skill Authoring, and ASD-STE100 documentation.
- Read back every changed path and commit all changes to branch `gpt`.

## 5. Decisions

- The CI gate applies to every prompt, regardless of request type or conversation mode.
- The pre-prompt gate and the post-skill-load gate are separate required checks.
- A cancelled run counts as superseded only when a newer run exists for the same workflow and branch.
- A rerun is acceptable only when logs establish a transient infrastructure failure. Do not rerun to hide a repository failure.

## 6. Progress Log

### 2026-11-20 13:30 UTC

- **Action:** Completed the mandatory CI preflight before accepting this request.
- **Result:** The latest runs before the repair failed. The changed-document run failed because the link checker treated valid tracked directories as missing Markdown files. The full-document run also exposed hard lint findings above the configured baselines in five files.
- **Repair:** Updated the link checker to accept links to tracked directories. Corrected mode-specific synonym use in the archive README, Session Start, The Worker, and the task template. Split the long ASD-STE100 skill description. Updated the wrapper to disable synonym rotation for the STE-flavored archive README.
- **Commits:** Link-checker repair `c7bf4c17a6343a1ced9780d3fa8d5daa8deaf8f8`. Lint repairs `a5ce29072ba5a983c1c769e744dd86962d4a5c41`.
- **CI:** Full-document run [44744854167](https://github.com/dungnv2602/chatgpt/actions/runs/44744854167) passed. Changed-document run [44744854156](https://github.com/dungnv2602/chatgpt/actions/runs/44744854156) passed.
- **Read-back:** Fetched all five lint-repair paths and confirmed their changes. The anchor-check step and full technical-document lint passed in GitHub Actions.
- **Validation:** Did not run the linter locally. Did not change a lint baseline.
- **Next:** Update the authoritative CI policy and every cue-based initialization path. Remove obsolete instructions that defer CI inspection until the user asks.

### 2026-11-20 13:33 UTC

- **Action:** Updated the authoritative CI policy and its task-execution and skill-loading integrations.
- **Result:** The GitHub Actions skill now requires a pre-prompt gate and a second gate after cue-triggered skill loading. The Worker, Session Archiving, and Session Start now enforce those gates. Agent Skill Authoring and ASD-STE100 documentation no longer defer CI review until the user asks.
- **Changed paths:** `skills/github-actions/SKILL.md`, `skills/the-worker/SKILL.md`, `skills/session-archiving/SKILL.md`, `skills/SESSION_START.md`, `skills/agent-skill-authoring/SKILL.md`, `skills/asd-ste100/SKILL.md`, `skills/asd-ste100/references/repository-writing-policy.md`.
- **Read-back:** Pending.
- **CI:** Pending the normal push-triggered workflows. No local linter execution.
- **Next:** Read back every changed path. Inspect and repair any failed applicable workflow before proceeding.

### 2026-11-20 13:34 UTC

- **Action:** Reviewed the first CI run after the workflow-policy update.
- **Finding:** Both applicable workflows failed because the repository writing policy used `validate` after it already used `check` for the same action. The linter reported one hard synonym-rotation finding.
- **Change:** Replaced `validate` with `check` in the policy. Preserved the mandatory CI-gate reference.
- **Read-back:** Pending.
- **CI:** The next push-triggered runs must pass before this task proceeds.
- **Next:** Read back the policy and task record. Inspect the new workflow runs and repair any remaining failure.

### 2026-11-20 13:35 UTC

- **Action:** Inspected the next full-document CI result after the first policy update.
- **Finding:** The full-document run failed on one hard synonym-rotation finding in the repository writing policy. The policy used `validate` after it used `check` for the same action.
- **Repair:** Changed `validate` to `check`. Full-document run [44745555375](https://github.com/dungnv2602/chatgpt/actions/runs/44745555375) passed on commit `a259f689d470299bac74d08e62f4b60965aaf1da`.
- **Additional clarification:** Made a cancelled latest run an explicit CI blocker unless a newer run supersedes it. This change will trigger the changed-document workflow.
- **Read-back:** The repository writing policy was fetched after its update. The GitHub Actions skill will be read back after this commit.
- **Next:** Inspect the changed-document run triggered by this clarification. Resolve any failure before completing the task.

## 7. Current State

The initial CI preflight is clear. Both applicable workflows passed on commit `a5ce29072ba5a983c1c769e744dd86962d4a5c41`.

The current repository policy contradicts the user's instruction. The GitHub Actions skill still prohibits routine CI inspection. Other skills and references also defer inspection until the user asks.

## 8. Remaining Work

- Replace the deferred CI policy with the mandatory pre-prompt gate.
- Add the post-load gate to foundational, drawing, and novelist cue workflows.
- Update The Worker so every user prompt begins with CI preflight.
- Remove stale CI instructions from skill-authoring and ASD-STE100 documentation.
- Verify all changed files and wait for applicable CI runs to pass.

## 9. Next Actions

1. Update `skills/github-actions/SKILL.md` as the authoritative CI policy.
2. Add the pre-prompt gate to `skills/the-worker/SKILL.md`.
3. Add the post-load gate to `skills/session-archiving/SKILL.md` and `skills/SESSION_START.md`.
4. Reconcile `skills/agent-skill-authoring/SKILL.md`, `skills/asd-ste100/SKILL.md`, and `skills/asd-ste100/references/repository-writing-policy.md`.
5. Search the approved skill workspace for stale CI deferral instructions.
6. Read back every changed file and inspect the resulting GitHub Actions runs.

## 10. References

- `skills/github-actions/SKILL.md`
- `skills/the-worker/SKILL.md`
- `skills/session-archiving/SKILL.md`
- `skills/SESSION_START.md`
- `skills/agent-skill-authoring/SKILL.md`
- `skills/asd-ste100/SKILL.md`
- `skills/asd-ste100/references/repository-writing-policy.md`
- `workspace/discussion.md`
- [Full-document CI run](https://github.com/dungnv2602/chatgpt/actions/runs/44744854167)
- [Changed-document CI run](https://github.com/dungnv2602/chatgpt/actions/runs/44744854156)

## 11. Verification

- **Check:** Latest applicable CI runs before accepting the request.
- **Method:** Inspected workflow runs, job steps, and failure logs through GitHub Actions.
- **Result:** Fixed the link-checker and lint-baseline failures. Both applicable workflows passed on commit `a5ce29072ba5a983c1c769e744dd86962d4a5c41`.
- **Limitations:** The linter did not run locally. The CI result applies to the named commit.

## 12. Handoff Instructions

The next action is to update the authoritative GitHub Actions policy and its cue-based initialization integrations. Keep the pre-prompt and post-load gates distinct. Do not proceed with project work when the latest applicable CI run fails or cannot be inspected.
