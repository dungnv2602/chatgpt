# Task: Template Fix

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173100
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-27 11:08 UTC
- **Priority:** P1
- **Status:** Ready
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to create Template Fix with two approved subtasks: create a task-board template; scan documents for missing templates and create any missing templates.
- **Governing ADR(s):** None
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready; approved, no dependencies.
- **Related tasks:** None

## 1. Original Request

> Create another task named "template fix", create Subtask to create a task board template, create another Subtask to scan repo if any document still haven't have its template, then create its template.

## 2. Subsequent Instructions

None.

## 3. Objective and Acceptance Criteria

Improve template coverage for task-board and repository document types.

1. Create a canonical task-board template and define its maintenance/usage contract.
2. Scan the repository systematically for documents that lack an applicable canonical template, schema, or embedded contract.
3. Before creating any identified missing template, read the applicable existing template/contract first and establish the gap and document owner/type.
4. Create missing templates only where the scan establishes a genuine gap; reconcile catalog, indexes, and coverage references.
5. Commit and read back all changes and results. No unobserved validation claimed.

## 4. Decisions

- Repository scan and template creation are assigned to a separate child from task-board-template creation.

## 5. Progress

### 2026-11-27 17:31 UTC

- **Action:** Created the Template Fix parent with two children for task-board template creation and document template coverage audit/remediation.
- **Result:** Child records established; implementation is not yet started.
- **References:** Parent and subtask index.
- **Next:** Execute children in Worker queue order.

### 2026-11-27 11:08 UTC — shared P0 remediation closeout

- **Action:** Closed CI child `20261127-173100-03` using the shared report-test correction completed under Refactor Skills child `20261127-173000-04`.
- **Result:** Commit `1e697f0e5167e9c0778cadef69d7cf084249be27` corrects both stale assertions. The indexed repository report `45987814713` records all six lint-report regression tests as Passed. Remote readback confirmed the test assertions and canonical template.
- **Limitations:** No local tests or scripts were run. No hosted CI result page or logs were inspected.
- **Next:** Continue child 02, the repository template coverage audit.

## 6. Current State and Remaining Work

Child 01 (canonical task-board template) is Done. Child 03 (duplicate P0 lint-report remediation) is complete and closed through shared commit `1e697f0e5167e9c0778cadef69d7cf084249be27`. Child 02 (repository template coverage audit and missing-template remediation) remains Ready. The repository-wide coverage audit has not started.

## 7. Verification and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Task records and board
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** Repository-wide template audit not performed.

## 8. Handoff

Execute children independently, template-first, with evidence.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| `lint-tooling-fd63ee164167664baaa97d9b` | high | Lint tooling check failed: Lint report regression tests | [report](../../../.takeout/reports/lint_reports/on_changed/history/45979960470-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45979960470) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45981806913-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45981806913) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45984083069-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45984083069) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985300823-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985300823) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985475477-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985475477) |