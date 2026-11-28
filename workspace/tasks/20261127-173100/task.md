# Task: Template Fix

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173100
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-28 03:13 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to create a task-board template; scan documents for missing templates and create any missing templates; audit and update stale templates against the current repository/workflow; relocate all templates currently outside skills into appropriate skill locations in accordance with the skill standard.
- **Governing ADR(s):** None
- **Current execution:** Yes
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — user-selected current focus; child 02 is active.
- **Related tasks:** None

## 1. Original Request

> Create another task named "template fix", create Subtask to create a task board template, create another Subtask to scan repo if any document still haven't have its template, then create its template.

## 2. Subsequent Instructions

> When templates are created, scan the repository to update stale templates compared to the current workflow/repository. Then relocate all templates outside of skills into skills at appropriate places, respecting the skill standard.

## 3. Objective and Acceptance Criteria

Improve template coverage, freshness, and canonical placement across the repository.

1. Create a canonical task-board template and define its maintenance/usage contract.
2. Scan the repository systematically for documents that lack an applicable canonical template, schema, or embedded contract.
3. Before creating any identified missing template, read the applicable existing template/contract first and establish the gap and document owner/type.
4. As part of template creation and coverage work, inventory existing templates repository-wide and compare each against the current workflow, repository structure, governance contracts, and applicable skill standards; update stale templates and references where necessary.
5. Relocate every template currently outside skill directories into the appropriate skill location, grouping it with the skill that owns the workflow/document type. Ensure each relocated template conforms to the repository's current skill standard, update all inbound references/catalogs/indexes, and remove obsolete duplicate copies only after references are reconciled.
6. Create missing templates only where the scan establishes a genuine gap; do not introduce redundant templates where an existing schema or embedded contract already governs.
7. Reconcile catalogs, indexes, ownership metadata, and coverage references for created, updated, and relocated templates.
8. Commit and read back all changes and results. Verify references and applicable skill-standard requirements; make no unobserved validation claims.

## 4. Decisions

- Repository scan, stale-template review, and template relocation are assigned to the document-template coverage child, separate from task-board-template creation.
- Skill placement must follow the current repository skill standard; do not create a parallel template system outside skills.

## 5. Progress

### 2026-11-28 03:13 UTC — child 02 resumed

- **Action:** Resumed the user-selected Template Fix workstream after `/start`. Completed the startup baseline and reviewed the task, child index, Worker procedures, report index, Ledger, and template catalog.
- **Result:** Child 02 is the only open required child. The repository already contains the 12 novel templates under the Romantic Storyteller skill's `assets/templates/` directory. The project-local template directory is absent. The catalog records a 277-Markdown / 30-template audit baseline and reports no missing recurring document format.
- **Next:** Independently verify template freshness, correct any remaining stale owner guidance, and complete placement/reference reconciliation.


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

Child 01 (canonical task-board template) is Done. Child 03 (duplicate P0 lint-report remediation) is complete and closed through shared commit `1e697f0e5167e9c0778cadef69d7cf084249be27`. Child 02 (repository template coverage audit, stale-template updates, and relocation of templates into appropriate skills) is In Progress. The existing catalog records the prior inventory and relocation, but the task still requires independent verification and correction of any remaining stale guidance.

## 7. Verification and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Task records and board
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** Repository-wide template coverage, freshness, and placement audit not performed.

## 8. Handoff

Execute children independently, template-first, with evidence. For child 02, inventory all repository templates, identify missing and stale templates, then relocate templates outside skills into their appropriate skill locations while maintaining skill-standard compliance and reconciling references.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| `lint-tooling-fd63ee164167664baaa97d9b` | high | Lint tooling check failed: Lint report regression tests | [report](../../../.takeout/reports/lint_reports/on_changed/history/45979960470-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45979960470) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45981806913-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45981806913) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45984083069-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45984083069) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985300823-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985300823) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985475477-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985475477) |
