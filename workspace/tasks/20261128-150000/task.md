# Task: Correct branch-read and commit-SHA provenance in The Worker

## Metadata
- **ID:** 20261128-150000
- **Created:** 2026-11-28 15:00 UTC
- **Updated:** 2026-11-28 15:00 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User approved and issued standalone Execute for the minimal workflow correction addressing unexplained commit SHA selection.
- **Governing ADR(s):** None
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready, dependencies and authorization satisfied
- **Related tasks:** None

## 1. Original Request
Correct the workflow so commit SHAs used for file reads have a traceable source, preventing unexplained SHA selection.

## 2. Subsequent Instructions
- **2026-11-28:** User asked whether the correction forces reading the latest commit of a branch; clarified that branch reads normally resolve the current branch state and a separate latest-commit lookup is not required.
- **2026-11-28:** Approved.
- **2026-11-28:** Execute.

## 3. Objective and Acceptance Criteria
Add a minimal canonical rule in The Worker:
1. Ordinary file reads use the intended branch.
2. Commit-specific reads only use explicitly supplied or workflow-obtained SHAs.
3. SHA provenance is identified, and stale/unexplained SHAs are not reused.
4. On a failed commit-specific read, verify the exact path against the intended branch.
5. Update the Workflow Map if needed, read back changed files, and commit.

## 4. Decisions
Keep the correction narrow. No mandatory latest-commit lookup is added.

## 5. Progress

- **Action:** Added the branch-first file-read and SHA-provenance rule to The Worker and the routing summary to Workflow Map.
- **Result:** The canonical workflow defaults to branch refs and prohibits unexplained/stale SHAs; no mandatory latest-commit lookup is imposed.
- **References:** `.agent/skills/the-worker/SKILL.md`; `.agent/WORKFLOW_MAP.md`; `workspace/task_board.md`.
- **Next:** Complete readback and closeout.

## 6. Current State and Remaining Work
Acceptance criteria met. Readback is confirmed below; no runtime checks were required.

## 7. Verification and Evidence
- **Commit SHA:** See implementation commit references: `a63e263496a8dc7070a32a3ae579ed59fbeda666` (Worker), `2b2c739f6d1bd0164fe874fecc6364829270affd` (map), `a61a0fd8689138319ef6c666e5ec579c700f3492` (board)
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`, `.agent/WORKFLOW_MAP.md`, `workspace/task_board.md`
- **Readback:** Confirmed on branch `gpt`
- **Checks:** Not performed
- **Limitations:** No runtime validation expected.

## 8. Execution self-check
Canonical owner, scope, approval, task parentage, and branch-read approach confirmed; standalone execute cue issued. Readback completed. No local scripts or hosted CI inspection.

## 9. Handoff
Complete the canonical rule, map pointer, readback and closeout.

## 10. Subtasks
Canonical index: [subtasks/README.md](subtasks/README.md). No child deliverables required.
