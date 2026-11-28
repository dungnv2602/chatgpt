# Task: Template Fix

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173100
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-28 03:13 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to create a task-board template; scan documents for missing templates and create any missing templates; audit and update stale templates against the current repository/workflow; relocate all templates currently outside skills into appropriate skill locations in accordance with the skill standard.
- **Governing ADR(s):** None
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** Done — all required child work and acceptance criteria are complete.
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



### 2026-11-28 — Template Fix closeout

- **Action:** Completed the repository-wide template coverage, freshness, and placement audit. Updated stale templates and owner guidance. Reconciled the catalog, validator, tests, and all references.
- **Result:** No new template type was needed. All 30 template assets are in skill-owned `assets/` directories. Twelve novel templates were relocated to the Romantic Storyteller skill. Two stale templates were updated. The catalog now covers every in-scope Markdown file.
- **Evidence:** `6cc29c784b7103bc425998ebfbfa5acfdf79399b`, `eb57d251600e4a86b78d9e62a1e49a5a65484003`, `11a44d28907f116f751babc3ede78fe436b8031c`, `be62841f0776a8c62e45d17ade01751c065a59b3`, `b59167b89e9c35ab071cf37e3fd5f74e6d14a264`, `56d2e4b515f79d15f01619d58af7983cd620280a`, and `98f8baf117c187edfc3dc76d16969a8228ed558e`. Independent path audit: 277/277 Markdown files covered, zero uncovered. Template placement audit: 30/30 under skill assets, zero outside. Local-link audit: 35 checked, zero broken. Readback confirmed all 12 moved template blobs retained their original SHA values.
- **Limitations:** No local scripts or tests were run. Hosted workflow results were not inspected.
- **Closeout:** All required children are complete. The task folder will be deleted under normal lifecycle rules.

## 6. Current State and Remaining Work

Child 01 (canonical task-board template) is complete and its record was removed under lifecycle rules. Child 03 (duplicate P0 lint-report remediation) is complete and closed through shared commit `1e697f0e5167e9c0778cadef69d7cf084249be27`. Child 02 is Done. All recurring document types have catalogued coverage. All 30 template assets now live under skill assets. The 12 novel templates are owned by the Romantic Storyteller skill. The two stale templates and the ongoing template-maintenance procedure were updated. The task is ready for normal folder closeout.

## 7. Verification and Evidence

- **Commit SHA:** `6cc29c784b7103bc425998ebfbfa5acfdf79399b`, `eb57d251600e4a86b78d9e62a1e49a5a65484003`, `11a44d28907f116f751babc3ede78fe436b8031c`, `be62841f0776a8c62e45d17ade01751c065a59b3`, `b59167b89e9c35ab071cf37e3fd5f74e6d14a264`, `56d2e4b515f79d15f01619d58af7983cd620280a`, and `98f8baf117c187edfc3dc76d16969a8228ed558e`
- **Changed paths:** Novel template assets and owner indexes; Worker document catalog, validator, tests, and template policy; task-board template; Prompt Master template; drawing and novel skill references; workflow path filters; task records and board.
- **Readback:** Verified from branch `gpt` at audit commit `98f8baf117c187edfc3dc76d16969a8228ed558e`.
- **Checks:** 30 template assets found, all in skill `assets/` locations; no external templates; former novel template directory absent. Independent catalog-pattern audit covered 277/277 in-scope Markdown files with 54 rules and zero uncovered paths. Link audit checked 35 local links with zero broken targets. All 12 moved template blobs match their original content hashes.
- **Limitations:** Repository scripts and tests were not run locally. Hosted Document Standards results were not inspected; no hosted pass is claimed.

## 8. Handoff

Closeout complete. Remove the completed task folder and clear its Current Execution pointer. Do not select unrelated work without a new user instruction.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| `lint-tooling-fd63ee164167664baaa97d9b` | high | Lint tooling check failed: Lint report regression tests | [report](../../../.takeout/reports/lint_reports/on_changed/history/45979960470-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45979960470) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45981806913-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45981806913) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45984083069-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45984083069) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985300823-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985300823) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985475477-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985475477) |
