# Task: Correct objective-based task parent selection

## Metadata

- **Template version:** 2.6
- **ID:** 20261127-102300
- **Created:** 2026-11-27 10:23 UTC
- **Updated:** 2026-11-27 10:23 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit instruction to identify workflow gaps and fix the workflow.
- **Governing ADR(s):** None
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — workflow correction initiated.
- **Related tasks:** None

## 1. Original Request

> You're treating every task are subtasks of that task. Identify gaps, fix your workflow.

## 2. Subsequent Instructions

- **2026-11-27:** The parent selection rules must not default to the current/active task. Compare objective and acceptance criteria, identify unrelated objectives, and correct misclassified task relationships.

## 3. Objective and Acceptance Criteria

Add an objective-based parent-selection test, prevent active-parent bias, and define a hierarchy correction process that preserves records and evidence.

1. Parent selection compares objectives and acceptance criteria, not repository or topic overlap alone.
2. The Worker distinguishes direct follow-ups from independent outcomes and CI-attribution exceptions.
3. Uncertain parentage remains unassigned until resolved rather than guessed.
4. Misparented tasks can be corrected without loss of original prompt, approvals, status, progress, evidence, or history.
5. Relevant task templates, indexes, and board rules reflect this selection and correction process.
6. Changed files are committed and remotely read back. No unobserved validation is claimed.

## 4. Decisions

- Active parent status is not a parent-selection criterion.
- CI finding attribution is a specific exception and does not imply blanket parent reuse.

## 5. Progress

### 2026-11-27 10:23 UTC

- **Action:** Identified ambiguity in parent-selection logic and added an objective/acceptance-criteria test and hierarchy correction procedure to The Worker.
- **Result:** Worker rule committed; task hierarchy and indexes remain to be reconciled.
- **References:** `.agent/skills/the-worker/SKILL.md`
- **Next:** Correct task 22 parentage and reconcile the task-board/index references.

## 6. Current State and Remaining Work

Workflow text updated. Task 22 was incorrectly nested under a CI/reporting parent and must be moved to its own genuine document-governance parent.

## 7. Verification and Evidence

- **Commit SHA:** 0b7f1b5b2c340fa59e718aa650d2e55fbc2b00d8
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** No hosted CI review.

## 8. Handoff

Reconcile parent indexes, board, and task records. Read back committed changes. Do not inspect hosted CI.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
