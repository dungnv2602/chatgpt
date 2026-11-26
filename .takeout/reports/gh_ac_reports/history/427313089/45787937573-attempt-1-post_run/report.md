# Validate Document Standards — run 45787937573

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45787937573 / 1 |
| Run number | 571 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45787937573 |
| Branch | gpt |
| Commit | 252168c9c2d8c6ef76714fce960ebdb59d0b99b5 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:00:04Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T09:01:53Z |

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
| 139799397409 | validate-document-standards | completed | failure | 9 | logs/job-139799397409.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139799397409 | 4 | Run CI Ledger regression tests | Blocking | medium | 2026-11-26T09:00:13.3588046Z test_actions_identity_uses_workflow_job_step_and_signature (test_ledger.LedgerTests.test_actions_identity_uses_workflow_job_step_and_signature) ... ERROR |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139799397409 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139799397409 | failure | .github | 302 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139799397409 | validate-document-standards | logs/job-139799397409.log | 71045 | False | validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.3588046Z test_actions_identity_uses_workflow_job_step_and_signature (test_ledger.LedgerTests.test_actions_identity_uses_workflow_job_step_and_signature) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.3649963Z test_actions_repeat_observation_increments_once_per_run (test_ledger.LedgerTests.test_actions_repeat_observation_increments_once_per_run) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.3723902Z test_all_lint_severities_create_and_reuse_grouped_tasks (test_ledger.LedgerTests.test_all_lint_severities_create_and_reuse_grouped_tasks) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4047369Z test_later_high_severity_finding_promotes_active_group_priority (test_ledger.LedgerTests.test_later_high_severity_finding_promotes_active_group_priority) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4158217Z test_lint_new_run_increments_occurrence_and_tracks_dates (test_ledger.LedgerTests.test_lint_new_run_increments_occurrence_and_tracks_dates) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4287037Z test_migrate_1_1_hands_off_unlinked_lint_findings_at_all_severities (test_ledger.LedgerTests.test_migrate_1_1_hands_off_unlinked_lint_findings_at_all_severities) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4439129Z test_related_findings_reuse_one_active_task_across_ingestion_events (test_ledger.LedgerTests.test_related_findings_reuse_one_active_task_across_ingestion_events) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4495320Z test_resolved_finding_reopens_and_preserves_resolution_history (test_ledger.LedgerTests.test_resolved_finding_reopens_and_preserves_resolution_history) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4608248Z ERROR: test_actions_identity_uses_workflow_job_step_and_signature (test_ledger.LedgerTests.test_actions_identity_uses_workflow_job_step_and_signature), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4609171Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4617885Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4634993Z ERROR: test_actions_repeat_observation_increments_once_per_run (test_ledger.LedgerTests.test_actions_repeat_observation_increments_once_per_run), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4635869Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4637599Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4644845Z ERROR: test_all_lint_severities_create_and_reuse_grouped_tasks (test_ledger.LedgerTests.test_all_lint_severities_create_and_reuse_grouped_tasks), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4645436Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4646783Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4652514Z ERROR: test_later_high_severity_finding_promotes_active_group_priority (test_ledger.LedgerTests.test_later_high_severity_finding_promotes_active_group_priority), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4653111Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:00:13.4654473Z Traceback (most recent call last): |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.