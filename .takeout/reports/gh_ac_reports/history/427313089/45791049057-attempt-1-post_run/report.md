# Validate Document Standards — run 45791049057

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45791049057 / 1 |
| Run number | 581 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45791049057 |
| Branch | gpt |
| Commit | daa409b9dee82b46a39be507ee691169a5c36871 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:20:26Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:13:29Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 1 |
| Steps | 9 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

validation_or_test

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 139809861997 | validate-document-standards | completed | failure | 9 | logs/job-139809861997.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139809861997 | 4 | Run CI Ledger regression tests | Blocking | medium | 2026-11-26T09:20:36.5407830Z test_actions_identity_uses_workflow_job_step_and_signature (test_ledger.LedgerTests.test_actions_identity_uses_workflow_job_step_and_signature) ... ERROR |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139809861997 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139809861997 | failure | .github | 410 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139809861997 | validate-document-standards | logs/job-139809861997.log | 91601 | False | validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.5407830Z test_actions_identity_uses_workflow_job_step_and_signature (test_ledger.LedgerTests.test_actions_identity_uses_workflow_job_step_and_signature) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.5437100Z test_actions_repeat_observation_increments_once_per_run (test_ledger.LedgerTests.test_actions_repeat_observation_increments_once_per_run) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.5479802Z test_all_lint_severities_create_and_reuse_grouped_tasks (test_ledger.LedgerTests.test_all_lint_severities_create_and_reuse_grouped_tasks) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.5762893Z test_cancelled_run_keeps_independent_failure_and_ignores_cancellation_propagation (test_ledger.LedgerTests.test_cancelled_run_keeps_independent_failure_and_ignores_cancellation_propagation) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.5934933Z test_evidence_is_bounded_but_occurrence_count_keeps_growing (test_ledger.LedgerTests.test_evidence_is_bounded_but_occurrence_count_keeps_growing) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6092775Z test_later_high_severity_finding_promotes_active_group_priority (test_ledger.LedgerTests.test_later_high_severity_finding_promotes_active_group_priority) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6157931Z test_lint_fingerprint_deduplicates_across_scopes_and_is_idempotent (test_ledger.LedgerTests.test_lint_fingerprint_deduplicates_across_scopes_and_is_idempotent) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6195394Z test_lint_new_run_increments_occurrence_and_tracks_dates (test_ledger.LedgerTests.test_lint_new_run_increments_occurrence_and_tracks_dates) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6250467Z test_low_severity_advisory_findings_create_p3_tasks (test_ledger.LedgerTests.test_low_severity_advisory_findings_create_p3_tasks) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6337804Z test_migrate_1_1_hands_off_unlinked_lint_findings_at_all_severities (test_ledger.LedgerTests.test_migrate_1_1_hands_off_unlinked_lint_findings_at_all_severities) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6436543Z test_recurring_untracked_lint_baseline_findings_do_not_create_tasks (test_ledger.LedgerTests.test_recurring_untracked_lint_baseline_findings_do_not_create_tasks) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6467484Z test_related_findings_reuse_one_active_task_across_ingestion_events (test_ledger.LedgerTests.test_related_findings_reuse_one_active_task_across_ingestion_events) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6493037Z test_resolved_finding_reopens_and_preserves_resolution_history (test_ledger.LedgerTests.test_resolved_finding_reopens_and_preserves_resolution_history) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6551534Z test_task_board_rows_stay_inside_their_status_section (test_ledger.LedgerTests.test_task_board_rows_stay_inside_their_status_section) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6593838Z test_untrusted_diagnostic_text_is_escaped_in_worker_task (test_ledger.LedgerTests.test_untrusted_diagnostic_text_is_escaped_in_worker_task) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6600223Z ERROR: test_actions_identity_uses_workflow_job_step_and_signature (test_ledger.LedgerTests.test_actions_identity_uses_workflow_job_step_and_signature), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6603347Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6631842Z ERROR: test_actions_repeat_observation_increments_once_per_run (test_ledger.LedgerTests.test_actions_repeat_observation_increments_once_per_run), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6633646Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:20:36.6654668Z ERROR: test_all_lint_severities_create_and_reuse_grouped_tasks (test_ledger.LedgerTests.test_all_lint_severities_create_and_reuse_grouped_tasks) |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.