# Task: Correct branch-read and commit-SHA provenance in The Worker

## Metadata
- **ID:** 20261128-150000
- **Created:** 2026-11-28 15:00 UTC
- **Updated:** 2026-11-28 15:00 UTC
- **Priority:** P1
- **Status:** Ready
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
Implementation pending.

## 6. Current State and Remaining Work
Update canonical Worker instruction and Workflow Map, read back, commit.

## 7. Verification and Evidence
- **Commit SHA:** Not committed
- **Changed paths:** Pending
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** No runtime validation expected.

## 8. Execution self-check
Scope and approval are explicit; standalone execute cue issued. Use branch refs for reads. No local scripts or hosted CI inspection.

## 9. Handoff
Complete the canonical rule, map pointer, readback and closeout.

## 10. Subtasks
Canonical index: [subtasks/README.md](subtasks/README.md). No child deliverables required.
