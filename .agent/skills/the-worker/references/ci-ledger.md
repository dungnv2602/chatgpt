# CI Ledger Operations

> Worker-owned reference. The Worker controls activation. This file is not a standalone skill.

## Ownership

The Ledger owns finding identity, report intake, classification, evidence, recurrence, and remediation-child linkage. The Worker owns request capture, parent identity, approval, scheduling, status, and closeout. The Worker's GitHub Actions reference governs technical diagnosis and workflow operation.

The Ledger never creates a parent task. Use a user-created task as the genuine parent for follow-ups and CI remediation.

## Intake

1. Read only reports listed in the published lint and Actions indexes. Do not scan report history or modify source reports.
2. Ingest only complete, eligible reports. Keep incomplete Actions captures retryable. Fail closed for a missing indexed complete report or unsafe path.
3. Lint findings are eligible only after a complete, tooling-valid baseline. A failed tooling check is its own stable finding. Do not taskify unbaselined or recurring, untracked baseline findings.
4. Ingest completed Actions reports with independently classified errors. Ignore cancellation propagation, skipped, neutral, successful, queued, and incomplete outcomes unless the report contains a separate eligible error.
5. Make processing idempotent. Preserve finding identity, occurrence count, first/last seen, bounded evidence, resolution history, accepted risk, and duplicate links.

## Attribution and child creation

Every task-specific source commit must include one trailer:

`Task-ID: <parent-or-child-task-id>`

- Lint reports carry `source_task_id` from the source commit trailer.
- Actions reports carry the source run's commit message. parse the same trailer.
- A parent task ID resolves to `workspace/tasks/<id>/task.md`.
- A child ID resolves through that child's `Parent Task ID`.
- The resolved parent must exist, match its recorded ID, carry `Origin: User`, and remain active. Do not use the current board pointer as a fallback.
- If the marker is absent, malformed, or ambiguous, or the task is missing or inactive, leave the evidence unassigned. Do not create a task or guess.
- A finding's latest observation controls attribution for that ingestion. Never reuse an older observation's parent for a new, unattributed run.

For attributed findings, group by genuine parent ID and stable `task_group`. Create or reuse one P0 CI remediation child per active group under that parent's `subtasks/` directory. Use `NN-ci-remediation-<slug>.md` and ID `<parent-id>-NN`.

Set new CI children to P0, Approved, Ready under the standing authorization. Use Proposed only when a specific unresolved decision is required. Routine implementation does not need an ADR just because the code differs. Keep a real decision gate limited to the dependent child.

Store genuine parent IDs in `task_refs` and child IDs in `subtask_refs`. Keep retired synthetic IDs in `legacy_task_refs`. Never add a synthetic parent, modify parent status or priority, select work, or edit `task_board.md` or Current Execution.

Update the parent's Ledger Findings section without modifying its priority. Update the child and `subtasks/README.md`. Preserve manual children. Roll back if child/index publication fails. Commit the Ledger, parent summary, children, and report-index modifications in one serialized writer transaction.

## Flood control

- Lint fingerprints deduplicate findings across scopes.
- Stable task groups merge related findings.
- Repeated observations update the same finding and child. do not create a new child for each run.
- Keep the first and four most recent distinct evidence paths. Preserve total occurrences and timestamps.
- Baseline comparisons suppress recurring untracked lint findings.
- Reopen a resolved finding while preserving its earlier resolution. Use the new observation's Task-ID attribution. If that observation is unassigned, do not reuse an older parent link.
- Do not poll, scan old history, or backfill. Historical backfill and clean reset need separate explicit authorization.

## Finding lifecycle

Statuses: `open`, `investigating`, `planned`, `fixing`, `verifying`, `resolved`, `accepted`, `false_positive`, `duplicate`.

- `resolved` requires a verified intended-branch fix commit, SHA, summary, and UTC timestamp. Hosted validation is separate metadata.
- `accepted` requires an accepted-risk record.
- `false_positive` requires a closure note.
- `duplicate` requires another existing finding ID.

Never erase terminal finding identity or resolution history when deleting a task folder. Keep old synthetic task refs as provenance, not as current parent links.

## Integrity

Reject malformed IDs, unsafe report paths, inconsistent indexed run identities, and missing complete reports. Do not weaken classification, baselines, schemas, or tests. Do not run repository scripts or tests locally. Read back every changed file. Use hosted validation only when authorized and do not inspect hosted results unless the user requests review.

Schema: `.takeout/reports/triage/ledger-schema.json`. Generator and regression tests: `.takeout/reports/triage/scripts/ledger.py` and `.takeout/reports/triage/scripts/test_ledger.py`.
