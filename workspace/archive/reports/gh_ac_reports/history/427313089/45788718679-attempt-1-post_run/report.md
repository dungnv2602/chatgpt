# Validate Document Standards — run 45788718679

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45788718679 / 1 |
| Run number | 573 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45788718679 |
| Branch | gpt |
| Commit | 899e6a13dcd918c25ec9a74484e4f15899030b12 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:05:15Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:12:57Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | checkout_or_action_download |
| Jobs | 1 |
| Steps | 9 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

checkout_or_action_download

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 139802010290 | validate-document-standards | completed | failure | 9 | logs/job-139802010290.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 139802010290 | 4 | Run CI Ledger regression tests | Blocking | medium | validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.7917845Z test_new_task_record_is_rolled_back_when_board_publication_fails (test_ledger.LedgerTests.test_new_task_record_is_rolled_back_when_board_publication_fails) ... ERROR |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139802010290 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139802010290 | failure | .github | 75 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139802010290 | validate-document-standards | logs/job-139802010290.log | 34747 | False | validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.7917845Z test_new_task_record_is_rolled_back_when_board_publication_fails (test_ledger.LedgerTests.test_new_task_record_is_rolled_back_when_board_publication_fails) ... ERROR, validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.8253856Z test_task_board_renderer_fails_closed_when_status_table_is_missing (test_ledger.LedgerTests.test_task_board_renderer_fails_closed_when_status_table_is_missing) ... ERROR, validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.8379885Z ERROR: test_new_task_record_is_rolled_back_when_board_publication_fails (test_ledger.LedgerTests.test_new_task_record_is_rolled_back_when_board_publication_fails), validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.8381612Z Traceback (most recent call last):, validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.8395510Z ERROR: test_task_board_renderer_fails_closed_when_status_table_is_missing (test_ledger.LedgerTests.test_task_board_renderer_fails_closed_when_status_table_is_missing), validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.8397206Z Traceback (most recent call last):, validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.8401856Z FAILED (errors=2), validate-document-standards	UNKNOWN STEP	2026-11-26T09:05:25.8534991Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.