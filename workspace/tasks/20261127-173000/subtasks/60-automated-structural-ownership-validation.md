# Subtask: Automated structural validation for canonical ownership and drift

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-60
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User explicitly approved DRAFT-0007 Revision 1, Option 2 and instructed Proceed. Authorized scope is ADR-0006 implementation: focused deterministic structural checks, tests and existing validation workflow integration, diagnostics only.
- **Governing ADR(s):** ADR-0006
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — approved scope and ADR-0006 accepted; implementation underway.
- **Required:** Yes
- **Created:** 2026-11-28
- **Updated:** 2026-11-28
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

 > Proceed preparing draft 7 for me

## 2. Subsequent Instructions

> Proceed

## 3. Objective and Scope

Implement ADR-0006 Option 2: a lightweight structural ownership validator with focused regression tests and integration into the existing validation workflow. No semantic interpretation or auto-repair.

## 4. Acceptance Criteria

1. ADR-0006 accepted and indexed; source Draft retired after readback.
2. Validator checks defined structural markers and pointer boundary/target.
3. Regression tests cover passing and failure cases.
4. Existing document standards workflow invokes tests and validator.
5. Validator remains deterministic, diagnostic-only and non-semantic.
6. Readback verifies changes; no hosted CI inspection.

## 5. Decisions and Progress

- User approved DRAFT-0007 Option 2; ADR-0006 is accepted.
- Implementation is underway under ADR-0006.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Draft, subtask index, task board, discussion register
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** No validator prototype, tests, or hosted CI review. Recommendation is based on structural repository evidence and qualitative assessment.

## 7. Completion

- **Status:** In Progress
- **Completed at:** Not applicable
- **Completion basis:** Implementation underway; readback and verification pending

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Canonical owner: The Worker. Draft and task governance reference loaded. Parentage confirmed under Refactor Skills. Scope and preparation approval explicit. Implementation decision gate remains pending. Remote readback and cleanup defined.

## 10. Handoff

Complete the validator, tests and workflow integration; reconcile ADR and task governance; read back changes.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
