# Task: Implement the centralized CI issue ledger

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-071000
- **Created:** 2026-11-23 07:10 UTC
- **Updated:** 2026-11-23 08:03 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** 20261123-054904 — Build GitHub Actions diagnostic reports and remove the CI preflight gate
- **Related tasks:** 20261123-054904 — Build GitHub Actions diagnostic reports and remove the CI preflight gate
- **Archived:** No

## 1. Original Request

A centralized CI issue ledger.

## 2. Subsequent Instructions

- **2026-11-23:** The user approved creating a separate P1 task to implement the centralized CI issue ledger, distinct from the existing diagnostic-report infrastructure task.
- **2026-11-23:** The repository `dungnv2602/chatgpt`, branch `gpt`, is the sole source of truth. Do not use the user's Library.
- **2026-11-23:** Keep all repository changes on branch `gpt`; do not modify `main`.
- **2026-11-23:** Keep reports under the established `reports/` root. Use `reports/triage/ledger.json` and its existing schema as the starting point. Do not create a separate ledger or report-retention system.

## 3. Objective

Turn the existing triage-ledger foundation under `reports/triage/` into an operational, machine-maintained register of distinct CI issues. Consolidate recurring lint and GitHub Actions findings across runs without duplicating source evidence or treating every failed run as a new issue.

## 4. Requirements

1. Inspect the existing lint and GitHub Actions report schemas, indexes, fingerprints, immutable history, collector workflows, and the current triage ledger schema before designing ingestion.
2. Define deterministic finding identity:
   - Reuse stable lint fingerprints where available.
   - Normalize GitHub Actions findings using stable workflow/job/step/category identity and a normalized diagnostic signature where available.
   - Avoid merging unrelated findings merely because they share a workflow or broad error category.
3. Implement an idempotent ingestion/upsert process that consumes newly published reports and updates `reports/triage/ledger.json`.
4. Deduplicate repeated observations across workflow runs and report scopes while retaining evidence references to each relevant immutable source report and run URL.
5. Maintain first-seen and last-seen timestamps, occurrence counts, source family, category, severity, owner, status, and resolution metadata in accordance with the ledger schema. Extend the schema only when required and document migrations.
6. Handle recurrence: reopen a resolved finding when the same issue is observed again, preserving its prior resolution history.
7. Preserve explicit lifecycle states, including open, investigating, planned, fixing, verifying, resolved, accepted, false-positive, and duplicate. Require fix-commit and successful relevant validation evidence before marking an issue resolved.
8. Keep human decisions (owner, severity overrides, accepted risk, duplicate relationships, resolution notes) stable across automated ingestion. Automation must not silently overwrite curated fields.
9. Do not treat cancelled, skipped, neutral, queued, in-progress, or unavailable evidence as defects by themselves.
10. Add validation and regression tests for stable identity, deduplication, idempotency, recurrence/reopening, evidence accumulation, curated-field preservation, malformed input, and safe publication/concurrency.
11. Integrate ingestion with the existing report publication flow without creating recursive workflow triggers or allowing concurrent writers to corrupt the ledger.
12. Provide a concise operator guide covering triage, prioritization, ownership, duplicate linking, resolution, and historical backfill policy.
13. Do not bulk-import all historical reports as separate findings. Any historical backfill must deduplicate first and preserve provenance.
14. Run repository tests and validation only on GitHub-hosted runners. Do not run repository code locally and do not poll or wait for workflow runs.
15. Keep this task independent from unrelated CI repairs and preserve all source workflow conclusions and lint thresholds.

## 5. Decisions

- **Approved:** Implement the ledger as an extension of `reports/triage/ledger.json`; do not create a second issue database.
- **Approved:** Keep the original lint and GitHub Actions reports immutable. The ledger stores normalized issue records and references source evidence rather than replacing reports.
- **Approved:** Use stable finding identity and idempotent upserts so repeated observations update one finding.
- **Approved:** Keep this as a separate P1 task from the diagnostic-report pipeline task.
- **Proposed:** Begin with forward-only ingestion of new reports; perform historical backfill only after identity and deduplication behavior is validated.

## 6. Progress Log

### 2026-11-23 08:03 UTC

- **Action:** Started execution after the user explicitly reprioritized this approved task.
- **Result:** The diagnostic-report infrastructure task is paused, not closed. Its natural-run validation and pending captures remain follow-up work. The ledger task is now the sole current execution.
- **Next:** Complete the source-contract and ingestion-design inspection, then implement forward-only ingestion.

### 2026-11-23 07:10 UTC

- **Action:** Created this approved task record after the user authorized a separate implementation task.
- **Result:** Scope is defined around the existing ledger foundation, automated ingestion, deduplication, lifecycle management, and safe publication. No implementation changes have been made under this task yet.
- **References:** `reports/triage/README.md`, `reports/triage/ledger.json`, `reports/triage/ledger-schema.json`; related task `20261123-054904`.
- **Next:** Start this task after the current diagnostic-report infrastructure task is complete or explicitly reprioritized.

## 7. Current State

The repository already contains an initial triage README, a JSON schema, and an empty `ledger.json`. The README describes deduplication and lifecycle states, but there is no automated ingestion/upsert process and no populated issue register. The existing ledger is therefore a foundation, not an operational issue tracker.

This task is approved and In Progress. It is the current execution task following explicit user reprioritization. The diagnostic-report infrastructure task is paused, not closed. No files have been changed for implementation.

## 8. Remaining Work

- Inspect the current report formats and collector publication lifecycle.
- Finalize finding identity and normalization rules.
- Implement idempotent ingestion and ledger persistence.
- Preserve human-curated fields and resolution history.
- Add regression coverage and hosted validation.
- Document operator procedures and decide whether/when historical backfill is safe.

## 9. Next Actions

1. Complete source-contract and ingestion-design inspection on the current `gpt` branch.
2. Implement forward-only ingestion, validation, regression tests, and operator guidance.
3. Integrate ingestion into report publication without recursive triggers or concurrent ledger writers.
4. Use GitHub-hosted Actions for validation. Do not poll or wait for runs.

## 10. References

- `reports/triage/README.md`
- `reports/triage/ledger.json`
- `reports/triage/ledger-schema.json`
- `reports/lint_reports/`
- `reports/gh_ac_reports/`
- `workspace/task_board.md`
- Related task: `workspace/tasks/20261123-054904-gh-actions-diagnostic-reports-and-remove-ci-preflight-gate.md`

## 11. Verification

- **Check:** Existing ledger foundation and task-board state.
- **Method:** Read the current files from branch `gpt`.
- **Result:** Confirmed that `ledger.json` is empty and that the schema and README exist. Confirmed that the diagnostic-report infrastructure task remains the current execution task.
- **Limitations:** No ingestion implementation or automated ledger validation has been performed. This task record and board entry only establish the approved work item.

## 12. Handoff Instructions

This task is approved and Ready, but not current execution. Do not interrupt the active diagnostic-report infrastructure task unless the user explicitly reprioritizes. When starting, inspect the latest report schemas, indexes, publication concurrency controls, and triage files on branch `gpt`; implement forward-only ingestion first. Preserve immutable source reports, curated ledger fields, source workflow conclusions, and the restriction against modifying `main`. Do not run repository code locally or poll hosted workflows.
