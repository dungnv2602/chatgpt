# Subtask: Worker queue, review/remediation lifecycle, attribution, grouping, and report migration

## Metadata

- **Template version:** 1.8
- **ID:** 20261128-230000-04
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** 20261128-230000-02; 20261128-230000-03
- **Eligibility / deferral reason:** Implementation continues on `gpt`; automated missing-dispatch recovery and coordinator activation remain gated pending policy activation, publisher readiness, and operational recovery readiness.
- **Required:** Yes
- **Created:** 2026-11-28 23:00 UTC
- **Updated:** 2026-11-28 23:00 UTC
- **Root-cause group:** None
- **Ledger group:** None (legacy reports only)
- **Legacy Task IDs:** None

## Validation Contract

Declare task-specific checks in this JSON block. The coordinator binds the contract to the exact source commit SHA. Use an empty array when no additional checks are required. Repository policy checks remain mandatory and cannot be removed or overridden. Use only registered adapters and repository-relative entrypoints. Never add shell command strings, credentials, environment overrides, or permission settings.

```json
{
  "contract_revision": "1",
  "checks": []
}
```

## Validation Lifecycle

```json
{
  "state": "review_required",
  "source_sha": "7814758586f68b3226822f760b4cbf06e86e108e",
  "policy_revision": "3e0efd87728646c0be2eb5854f95140151a3c44b",
  "coordinator_run_id": 46164069720,
  "attempt": 1,
  "outcome": "capture_failure",
  "reconciled_at": null
}
```

## 1. Original Prompt

Implement the accepted ADR-0008 as part of the user's new parent task “ADR 8 implementation”.

## 2. Subsequent Instructions

- **2026-11-28:** User explicitly requested task creation, adequate subtasking, and Current selection; “Execute”.

## 3. Objective and Scope

Integrate non-blocking Worker lifecycle, index-first review, failure-only diagnosis, root-cause grouped child task reuse, attribution/fallback, cleanup lifecycle, and stage all producers/consumers onto the replacement.

## 4. Acceptance Criteria

1. Worker is non-blocking while validation runs and uses index-first triage.
2. Logs are inspected only for actionable recorded failures; failures grouped by root cause and child folders reused.
3. Parent attribution uses source Task-ID trailer; unresolved attribution uses permanent fallback without guessing.
4. Cancelled/superseded attempts create no feedback tasks and do not mutate task lifecycle.
5. Every producer and consumer migrates without weakening coverage; report tree remains until retirement gates are met.

## 5. Decisions and Progress

- ADR-0008 governs this work.
- Preserve existing validation coverage and legacy report system until migration gates are met.
- **Progress:** Added task lifecycle schema and task-record metadata, exact-SHA missing-dispatch recovery, and staged cutover gates for legacy producers/consumers. This commit completes the Worker lifecycle procedure, root-cause group reuse contract, migration inventory, catalog/navigation updates, and legacy Ledger ownership boundary. Added fail-closed direct-push cutover gates that require source/current policy activation and recovery dispatch availability; task-owned workflow-run diagnostics are suppressed while unrelated workflow-run diagnostics and push backfill remain available. Remaining: reconcile exact-SHA validation when authorized, complete operational Confirmation, and gated producer cutover/retirement.

### 2026-11-28 — residual policy gate correction and review-index assessment

- **Correction:** Found a remaining `protection.enforcement_status` prerequisite in `.github/workflows/task-validation.yml` after the earlier gate cleanup. Removed it in commit `a991bebd5a166805c18eadd1aebfa305797d4e14`. The coordinator now relies on the exact source-SHA/policy-blob binding and mandatory-check manifest; GitHub branch protection remains optional hardening, not an ADR-0008 gate.
- **Recovery availability:** Read back `main`'s dispatcher workflow with `workflow_dispatch` and recovery workflow with the 15-minute schedule. Updated the `gpt` policy's schedule and workflow-dispatch availability fields to `verified` in commit `d2f5b4b9e28fe935e77fc2c79e5ee519d9dad804`. Coordinator activation remains staged.
- **Documentation:** Corrected the task-validation interface and subtask 01 wording; updated the task-validation README to reflect verified default-branch workflow availability. Read back each changed file.
- **Review queue:** Read `workspace/task-validation/status-index.json` first. It contains 211 attempts; all 211 are `capture_failure`, all have `check_set_id: null`, all remain unreconciled, and `closed_through` remains `{run_id: 0, attempt: 0}`. Hosted logs were not inspected. No root cause is asserted for the full set, no remediation child was fabricated, and no unresolved record or checkpoint was changed.
- **Lifecycle:** Bound this subtask to source commit `7814758586f68b3226822f760b4cbf06e86e108e` and policy blob `3e0efd87728646c0be2eb5854f95140151a3c44b` in metadata commit `e67c2dc5f23e52cabadab769c9ec5fdc5343ac18`.
- **Remaining:** Continue producer/consumer migration and preserve `.takeout/reports/`. Subtask 04 is not Done; operational Confirmation remains gated by the unresolved review queue and the ADR's required scenario demonstrations.

### 2026-11-28 — legacy report producer/consumer inventory refresh

- **Tracked tree:** The recursive `gpt` tree contains seven entries under `.takeout/reports/`: README, `gh_ac_reports/actions/capture/action.yml`, `index.json`, and `ledger.json` (841,526 bytes). No tracked `history/` or `lint_reports/` directories are present. `index.json` currently has zero runs and no latest report.
- **Lint producers/consumers:** `ste-lint-changed.yml` and `ste-lint-full-docs.yml` still read `.takeout/reports/index.json` for baseline reports and publish report history; `.agent/skills/the-worker/scripts/generate_lint_report.py` enforces the legacy history layout and updates the index. The changed-lint workflow has a full-audit fallback when baseline data is unavailable.
- **Actions diagnostics:** `gh-actions-capture.yml` invokes the legacy composite capture action. `gh-actions-diagnostics.yml` invokes `actions-report.py` and `ledger.py`, runs their regression tests, and can publish `.takeout/reports/`, task folders, and the task board. `validate-document-standards.yml` still runs `test_ledger.py` and the composite capture action.
- **Decision:** These producers and consumers remain live. Do not delete the Ledger, report scripts/tests, workflows, or tree while coordinator activation is staged and operational Confirmation is incomplete. The migration must replace or retire each dependency without weakening the existing lint/standards checks; the full report-tree retirement remains reserved for subtask 05.
## 6. State and Evidence

- **Commit SHA:** 4ff2d0799ea1a0e980407d504f7a1ddaff9ca72b
- **Changed paths:** Worker skill, task-validation interfaces, CI Ledger reference, document-type catalog, Workflow Map, task-validation README, task tracking records, and five validation/diagnostic workflows.
- **Readback:** Confirmed from branch `gpt`; all nine owner, interface, workflow, and tracking paths were fetched after commit `4ff2d0799ea1a0e980407d504f7a1ddaff9ca72b` and metadata commit `1b1f248c98ca5833d77064269db62bf90dce8bca`.
- **Checks:** Not performed
- **Limitations:** No local tests or hosted validation performed. Default branch `main` now contains `.github/workflows/task-validation-dispatch.yml` and `.github/workflows/task-validation-recovery.yml` after PR #10. GitHub branch protection is not an ADR-0008 requirement. Existing capture-failure attempts were not inspected or reconciled.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Scope and parent are confirmed. Required, approved, and executed under the authorized parent batch. Preserve evidence and verification boundaries.

## 10. Handoff

Continue repository-side producer/consumer migration. Coordinator activation remains staged pending report migration and operational readiness; default-branch dispatcher and scheduled recovery availability are verified. Branch protection is not required by ADR-0008. Do not inspect hosted logs or retire `.takeout/reports/` before the required authorization and Confirmation.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | None yet | — |


### 2026-11-28 — execution worklist reconciliation

- **Operation 1 — reconcile staged migration and lifecycle procedure:** Completed. Read back the canonical Worker, migration interface, and task records; existing index-first, grouped-root-cause, exact-source attribution, fallback, cancellation/supersession, and nonblocking lifecycle rules remain intact.
- **Operation 2 — verify producer gate and migration scope:** Completed. Reviewed the three validation workflows and the two diagnostic/capture workflows. Exact-SHA reusable calls and gated legacy suppression are staged; coordinator-owned diagnostics suppression is conditional on source/current policy activation and recovery dispatch availability. Unrelated workflow diagnostics and push backfill remain available.
- **Operation 3 — reconcile external prerequisites:** Blocked locally to this operation. Default branch `main` now contains the dispatcher/recovery workflows after PR #10. GitHub branch protection is not required by ADR-0008. No setting change or `main` write is authorized. No hosted CI inspection was authorized for ADR-0008.
- **Operation 4 — operational Confirmation and retirement:** Dependency-waiting in child 05. Preserve `.takeout/reports/` and all legacy producers/consumers. No retirement or coverage weakening.
- **Stop-proof:** Remaining work is confined to policy activation, publisher/report migration, operational readiness, and operational Confirmation; independent repository-side staging and readback operations in this scope are reconciled. Do not retry the unavailable settings verification until access/prerequisites change.
