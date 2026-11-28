# Task: Template Fix

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173100
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-28 03:45 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to create a task-board template; scan documents for missing templates and create any missing templates; audit and update stale templates against the current repository/workflow; relocate all templates currently outside skills into appropriate skill locations in accordance with the skill standard.
- **Governing ADR(s):** None
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** Completed — all required children are closed; parent ready for lifecycle cleanup.
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

### 2026-11-28 03:45 UTC — template audit complete

- **Action:** Completed child 02 after verifying the template inventory, updating the two stale assets and their owner guidance, integrating placement-aware validation into the hosted workflow, and reconciling the catalog and references.
- **Result:** All 30 canonical template assets are under owning skills. The recorded repository scan baseline covers 277 Markdown documents and reports no missing recurring template family. The task-board template and Prompt Master Template N now match current repository contracts. The validator and regression suite are wired into CI.
- **Evidence:** Final commit `a4d42b9f8bde7ff1ff4a52fe7b510bd6627e0433`; supporting commits and verification details are recorded in child 02.
- **Limitations:** No local tests or scripts were run; hosted CI results were not inspected.
- **Next:** Delete the completed parent folder and clear its board selection under the Worker lifecycle.

### 2026-11-28 03:39 UTC — task recovered and resumed

- **Action:** Recovered the active task record from the last known in-progress commit after the current branch deleted the parent and child records prematurely. Reconciled the board and confirmed the remaining acceptance criteria are still open.
- **Result:** Child 02 remains the only open required child. The 12 novel templates are skill-owned under `assets/templates/`; the old project-local directory is absent. The catalog records a 277-Markdown / 30-template baseline, but its audit outcome overstates completion: the Task Board template, Prompt Master guidance, and active validator integration remain stale.
- **Next:** Complete the remaining template freshness and validator-workflow reconciliation, verify references, then close the task.

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

Child 01 (canonical task-board template) is Done and removed after closeout. Child 03 (duplicate P0 lint-report remediation) is complete and closed through shared commit `1e697f0e5167e9c0778cadef69d7cf084249be27`. Child 02 (repository template coverage audit, stale-template updates, and relocation) is Done. All required children are closed. The recorded scan found no missing recurring document family; all 30 canonical template assets are skill-owned. The two stale templates and their owner guidance are updated. The placement-aware validator and regression suite are wired into the hosted document-standards workflow. The parent is ready for lifecycle cleanup.

## 7. Verification and Evidence

- **Final commit:** `a4d42b9f8bde7ff1ff4a52fe7b510bd6627e0433`
- **Supporting commits:** `babd4863ea5517b94f5f3a2e93326fca34ac3da6`, `695cdd4174986c99633caa6f5c3a3d5e9d6ad8f7`, `501bc09bbc646a54c8c422de23a4c5a60efb8298`, `81cbb0d1220fa0165dfa8d06b67b97fda71ca84d`, `9d9ac2e31187aa07076d081f436bcdb5f55fd51a`, `8eb9d12a5c151111ad424520d7b20b1b1737286a`.
- **Changed paths:** Task Board template/live board; Prompt Master Template N, SKILL.md, README.md; placement validator and tests; document-standards workflow; document-type catalog; workspace README; superseded validator/test removal.
- **Readback:** All changed files and all 30 canonical template assets were fetched successfully. The former project-local novel template path and workspace-root template paths are absent. All known inbound references point to skill-owned assets.
- **Checks:** The recorded recursive inventory covers 277 Markdown documents and 30 template assets and found no missing recurring document type. The new regression suite covers external files/directories, misplaced skill templates, and task/archive exclusions. CI is configured to run the suite and validator.
- **Limitations:** No local tests/scripts were run. Hosted CI was not inspected; no test-pass claim is made. The existing high-severity lint-tooling Ledger finding remains open and was not modified by this task.

## 8. Handoff

All required children are complete. Remove this completed task folder after clearing its current-execution pointer. Do not select another parent without a new user instruction.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| `lint-tooling-fd63ee164167664baaa97d9b` | high | Lint tooling check failed: Lint report regression tests | [report](../../../.takeout/reports/lint_reports/on_changed/history/45979960470-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45979960470) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45981806913-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45981806913) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45984083069-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45984083069) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985300823-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985300823) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985475477-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985475477) |
