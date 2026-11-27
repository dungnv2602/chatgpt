# Task: Correct objective-based task parent selection

## Metadata

- **Template version:** 2.6
- **ID:** 20261127-102300
- **Created:** 2026-11-27 10:23 UTC
- **Updated:** 2026-11-27 10:23 UTC
- **Priority:** P1
- **Status:** Paused
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit instruction to identify workflow gaps and fix the workflow.
- **Governing ADR(s):** None
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** Paused — hierarchy correction started; remaining index reconciliation deferred behind P0 queue.
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

### 2026-11-27 10:25 UTC

- **Action:** Added the parent-selection test to both task templates, created distinct parents for this correction and the document-governance consolidation, migrated the consolidation record, removed its old path, and updated board/index references.
- **Result:** Remote readback confirmed the Worker, both templates, task board, parent indexes, migrated record, and discussion register. The old misparented record path no longer exists.
- **References:** Worker commit `0b7f1b5b2c340fa59e718aa650d2e55fbc2b00d8`; task template `9488c10f150ca0a8d2e7bf02668ee7d52bb1a0df`; subtask template `871743475e325dce4098df5256df8d91f99dfb66`; hierarchy/index commits recorded in the branch.
- **Next:** After the P0 queue, audit parentage and reconcile any remaining indexes or rules, then read back and close.

## 6. Current State and Remaining Work

Workflow and task templates now enforce objective-based parent selection. Task 22 was moved from the CI/reporting parent to a separate document-governance parent. Remaining closeout/reconciliation is deferred behind the P0 queue.

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
