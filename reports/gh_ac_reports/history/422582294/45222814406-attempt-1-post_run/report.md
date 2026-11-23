# Process Image Takeout and Create WebP Derivatives — run 45222814406

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Process Image Takeout and Create WebP Derivatives |
| Workflow path | .github/workflows/convert-images-to-webp.yml |
| Run / attempt | 45222814406 / 1 |
| Run number | 60 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45222814406 |
| Branch | gpt |
| Commit | c07921efe1a22db2237caa647d828e66fdd0236d |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T17:00:21Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T23:00:25Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | checkout_or_action_download |
| Jobs | 1 |
| Steps | 11 |
| Issues | 1 |
| Annotations | 1 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

checkout_or_action_download

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137861327980 | process-image-takeout | completed | failure | 11 | logs/job-137861327980.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 137861327980 | 5 | Test takeout processor | Blocking | medium | process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.7862409Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137861327980 | failure | .github | 201 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137861327980 | process-image-takeout | logs/job-137861327980.log | 67639 | False | process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.7862409Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.7891753Z     self.assertEqual(error, ""), process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8024117Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8030177Z AssertionError: 1 != 0 : Takeout batch batch-attempt-six-eleven failed: upload-six.png: supplied source_asset_id and generation/output identity do not match the same output in drawings/2026-11-19/attempt-06.md., process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8035940Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8040737Z AssertionError: 1 != 0 : Takeout batch batch-session-link failed: portrait.png: supplied source_asset_id and generation/output identity do not match the same output in drawings/2026-11-19/attempt-01.md., process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8045799Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8053219Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8061406Z AssertionError: 'Duplicate output_id' not found in "# Takeout Processing — batch-duplicate-output-id\n\n- Batch: batch-duplicate-output-id\n- Attempt: attempt-001\n- Status: FAILED\n- Items: 2\n- Generated: 2026-11-23T17:00:42+00:00\n\n## Verification checks\n- Inbox is flat and contains only PNG/JPG/JPEG files, HANDOFF.yml, and the reserved history/ and webp/ directories.\n- Batch was not marked successful; sources were restored to, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8069827Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8077868Z AssertionError: 'Duplicate output_id' not found in '# Takeout Processing — batch-existing-output-id\n\n- Batch: batch-existing-output-id\n- Attempt: attempt-001\n- Status: FAILED\n- Items: 1\n- Generated: 2026-11-23T17:00:42+00:00\n\n## Verification checks\n- Inbox is flat and contains only PNG/JPG/JPEG files, HANDOFF.yml, and the reserved history/ and webp/ directories.\n- Batch was not marked successful; sources were restored to t, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8085865Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8090733Z AssertionError: 1 != 0 : Takeout batch batch-hash-match failed: unchanged.png: conversation_record has no exact image mapping row for attempt 'Not applicable', asset ID 'Not applicable', and generation ID 'A001-O01'., process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8095473Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8100612Z AssertionError: 1 != 0 : Takeout batch batch-hash-mismatch failed: mismatch.png: supplied source_asset_id and generation/output identity do not match the same output in drawings/2026-11-19/attempt-01.md., process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8106148Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8111561Z AssertionError: 1 != 0 : Takeout batch batch-identical-outputs failed: output-one.png: supplied source_asset_id and generation/output identity do not match the same output in drawings/2026-11-19/attempt-01.md., process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8116180Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8124584Z AssertionError: 'missing or unsafe WebP asset' not found in '# Takeout Processing — batch-stale-webp-link\n\n- Batch: batch-stale-webp-link\n- Attempt: attempt-001\n- Status: FAILED\n- Items: 1\n- Generated: 2026-11-23T17:00:44+00:00\n\n## Verification checks\n- Inbox is flat and contains only PNG/JPG/JPEG files, HANDOFF.yml, and the reserved history/ and webp/ directories.\n- Batch was not marked successful; sources were restored t, process-image-takeout	UNKNOWN STEP	2026-11-23T17:00:45.8132622Z Traceback (most recent call last): |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.