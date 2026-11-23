# Task: Implement the centralized CI issue ledger

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-071000
- **Created:** 2026-11-23 07:10 UTC
- **Updated:** 2026-11-23 08:40 UTC
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

### 2026-11-23 08:37 UTC

- **Action:** Confirmed the natural sweep re-ingested the previously unprocessed report with the refined generator.
- **Result:** The ledger now contains one open, high-severity `publication_or_push` finding from Actions run `45138510922`. The redundant status-propagation finding is absent. The record uses stable workflow, job, step, and category identity. It links to the immutable report and run URL. The source log confirms a rejected push after the branch ref changed between fetch and push.
- **State:** The ledger contains one finding and 219 processed report paths. The 151 paths present at bootstrap remain excluded from historical import.
- **Validation:** The generator executed in the natural publication flow. The 17-test hosted suite and workflow conclusions have not been inspected. No run was polled or dispatched.
- **Next:** Keep the task In Progress until task-scoped hosted validation can be reviewed in a later bounded check.

### 2026-11-23 08:33 UTC

- **Action:** Reviewed the first naturally ingested Actions report and its immutable job log. The report contained a real rejected push and a second step that only propagated an earlier lint failure.
- **Result:** Refined Actions signatures to extract diagnostic lines from the exact job log. The generator now ignores the two known lint workflow status-propagation steps. Added a regression test for command-echo filtering and exact-step log extraction.
- **Evidence:** Source run `45138510922` recorded a rejected push because the `gpt` ref changed between the workflow's fetch and push. The source workflow was not modified because source-workflow repair is outside this task.
- **Re-ingestion:** Removed the two noisy records and marked only that immutable report path unprocessed. The next natural sweep will ingest it with the refined logic. The ledger currently has no findings.
- **Verification:** Read back the updated generator, 17 regression tests, operator guide, and ledger state. Hosted validation and clean re-ingestion remain unverified. No workflow was polled or dispatched.
- **Commits:** `bf2ac28abe67415a20296ec906e449f22206c443`, `d8f2b4095f5288de563415ff82bcebbcf43c2cb5`, `fc4c511cce34335b75d8747c4f477376b3e26e99`.
- **Next:** Leave the report path pending for the next natural sweep. Review hosted results only when naturally available.

### 2026-11-23 08:23 UTC

- **Action:** Integrated ingestion into the six existing diagnostic capture jobs and the central diagnostics sweep. Added hosted regression execution, atomic ledger publication, and a path exclusion for ledger-only commits.
- **Concurrency:** Read back all six source-workflow diagnostic jobs. Each uses the shared non-cancelling `gh-ac-report-writer` group. The sweep uses the same group.
- **Safety:** Capture-action ingestion remains non-blocking for source workflow conclusions. The sweep ingests complete post-run Actions reports after collection. The ledger-only path is excluded from sweep triggers.
- **Operator guide:** Added identity rules, default severity, curated lifecycle fields, resolution evidence, duplicate links, recurrence, migration, and backfill policy.
- **Tests:** Added 16 regression tests, including publisher-concurrency and recursion configuration checks. GitHub-hosted workflows now compile and run the ledger suite. No tests were run locally.
- **Read-back:** Verified the generator, tests, schema, ledger, catalog, operator guide, capture action, sweep workflow, and all six source-workflow concurrency groups.
- **Commits:** `950b139c13c05f3a8afa045a8d5c5dbdd53479b2`, `ce09697d7a989ea5cbc731b95241791882886baa`, `9516b6cc8794d60e4fb539c9ab5e7b77385bf0cc`, `e55d2123cb151ba9a691ff07469efcad38f06ca7`, `ee089d5a4508afab20fcb8bf988b71d4d12dd27a`.
- **Validation limit:** Hosted tests and workflow checks have not been inspected. Do not poll or wait for runs.
- **Next:** Keep the task In Progress until task-scoped hosted validation results are naturally available for a later bounded review.

### 2026-11-23 08:03 UTC

- **Action:** Started execution after the user explicitly reprioritized this approved task.
- **Result:** The diagnostic-report infrastructure task is paused, not closed. Its natural-run validation and pending captures remain follow-up work. The ledger task is now the sole current execution.
- **Next:** Complete the source-contract and ingestion-design inspection, then implement forward-only ingestion.

### 2026-11-23 07:10 UTC

- **Action:** Created this approved task record after the user authorized a separate implementation task.
- **Result:** Scope is defined around the existing ledger foundation, automated ingestion, deduplication, lifecycle management, and safe publication. No implementation changes have been made under this task yet.
- **References:** `reports/triage/README.md`, `reports/triage/ledger.json`, `reports/triage/ledger-schema.json`; related task `20261123-054904`.
- **Next:** Start this task after the current diagnostic-report infrastructure task is complete or explicitly reprioritized.

### 2026-11-23 08:18 UTC

- **Action:** Implemented the ledger generator, versioned schema, regression suite, catalog classification, and forward-only bootstrap state.
- **Result:** The generator reads only indexed immutable report paths. It reuses lint fingerprints and derives Actions identities from workflow, job, step, category, and normalized diagnostic text. It deduplicates evidence by report path and counts unique workflow observations. It preserves curated fields, reopens recurring resolved findings with resolution history, and rejects resolution without a fix commit and successful validation evidence.
- **Bootstrap:** Seeded 151 currently indexed report paths as already processed. The ledger remains empty, so no historical findings were imported.
- **Verification:** Read back the generator, tests, schema, ledger, and catalog from \`gpt\`. Regression tests have not run. The generator has not yet been integrated into report publication.
- **Commits:** \`199dbf3694d547f2fbcbdde23a44c16250493d0c\`, \`022614b002e0b61016264d71e341a550a7c244a2\`, \`820bc4bde0bf1d9bd5921af59a24d2d1b29022fd\`, \`bce52d2b894fa6eb592b9cb9a84d79d8a4aec2b4\`, \`19a92ad73f4c6bfcff49f19a7f2f8e1b0a9e59ba\`.
- **Next:** Integrate ingestion with the serialized diagnostics publishers and write the operator guide.

### 2026-11-23 08:23 UTC

- **Action:** Integrated ingestion into the six existing diagnostic capture jobs and the central diagnostics sweep. Added hosted regression execution, atomic ledger publication, and a path exclusion for ledger-only commits.
- **Concurrency:** Read back all six source-workflow diagnostic jobs. Each uses the shared non-cancelling \`gh-ac-report-writer\` group. The sweep uses the same group.
- **Safety:** Capture-action ingestion remains non-blocking for source workflow conclusions. The sweep ingests complete post-run Actions reports after collection. The ledger-only path is excluded from sweep triggers.
- **Operator guide:** Added identity rules, default severity, curated lifecycle fields, resolution evidence, duplicate links, recurrence, migration, and backfill policy.
- **Tests:** Added 16 regression tests, including publisher-concurrency and recursion configuration checks. GitHub-hosted workflows now compile and run the ledger suite. No tests were run locally.
- **Read-back:** Verified the generator, tests, schema, ledger, catalog, operator guide, capture action, sweep workflow, and all six source-workflow concurrency groups.
- **Commits:** \`950b139c13c05f3a8afa045a8d5c5dbdd53479b2\`, \`ce09697d7a989ea5cbc731b95241791882886baa\`, \`9516b6cc8794d60e4fb539c9ab5e7b77385bf0cc\`, \`e55d2123cb151ba9a691ff07469efcad38f06ca7\`, \`ee089d5a4508afab20fcb8bf988b71d4d12dd27a\`.
- **Validation limit:** Hosted tests and workflow checks have not been inspected. Do not poll or wait for runs.
- **Next:** Keep the task In Progress until task-scoped hosted validation results are naturally available for a later bounded review.

## 7. Current State

The repository contains a generator-owned ledger pipeline with schema version 1.1.0. It reads indexed immutable reports, preserves curated fields, and tracks unique run observations. The initial bootstrap excluded 151 existing report paths from historical import.

The capture and sweep publishers use the shared non-cancelling writer group. The operator guide and 17 regression tests are committed. Natural ingestion now records one open high-severity publication issue from Actions run 45138510922. It excludes the redundant status-propagation step. Hosted test results remain unverified.

This task is approved and In Progress. The diagnostic-report infrastructure task remains paused, not closed.
## 8. Remaining Work

- Review task-scoped GitHub-hosted test and workflow results when they are naturally available. Do not poll or wait for runs.
- Correct any verified ledger-task defect.
- Complete the required task archive and board closeout after validation.
## 9. Next Actions

1. Review the next naturally available hosted results in a bounded snapshot.
2. Correct only verified ledger-task defects.
3. Complete the required task archive and board closeout after validation.

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

This task is In Progress on branch `gpt`. The forward-only ledger generator, schema, operator guide, tests, capture action, and diagnostics sweep are committed. One immutable Actions report is intentionally unprocessed so the next natural sweep can ingest it with the refined log-signature logic. Review hosted results only when naturally available. Do not poll or wait for runs. Preserve immutable source reports, curated ledger fields, source workflow conclusions, and the restriction against modifying `main`. Do not run repository code locally.