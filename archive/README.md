# Task and Report Archive

This directory stores completed and cancelled task records and individually archived CI report files.

## Structure

- `archive/tasks/` stores immutable archived task records.
- `archive/reports/` stores individually archived CI report files, preserving their path below the report-family root.
- Keep task IDs and filenames unchanged.
- Record each archive timestamp in UTC.
- Do not store full conversation transcripts.

## Task resolution and Ledger retirement

The active CI issue Ledger is an operational backlog, not a permanent archive.

1. Before closing a Ledger-generated task as Done, verify that every finding in its Ledger Findings section is terminal: `resolved`, `accepted`, `false_positive`, or `duplicate`. Each status must satisfy the Ledger schema's evidence requirements.
2. Move report files needed for the historical handoff to `archive/reports/`, preserving their relative paths. Update the task's evidence links to the new archive paths before writing its final archive copy.
3. Archive the completed task and register its exact path in `.github/archive-retention-index.json`.
4. The archive-task push triggers the normal diagnostics sweep. The Ledger reads only indexed task archives and removes the covered terminal findings from the active `reports/triage/ledger.json`. Findings remain active until that event-driven retirement runs.
5. Do not manually delete resolved findings from the Ledger or run a periodic retirement scan. The archived task record and its report references preserve the audit trail.

A task with any open or non-terminal finding must not be closed as Done. Cancelled tasks do not retire open findings.

## Normal report filing and retention

When a report is no longer required by an open finding or active investigation:

1. Move the exact report file to `archive/reports/`, preserving its report-family path.
2. Add one index entry to `.github/archive-retention-index.json` with the exact archive path and the UTC timestamp of the move (`archived_at_utc`).
3. Do not archive a file still referenced by an open finding or active investigation.
4. Do not manually delete an indexed archived file. The weekly retention workflow deletes each exact indexed file after 90 days from its own archive timestamp.

Task and report archives use the same index, schedule, cleanup script, and 90-day per-file retention policy.

## Explicit clean-start reset

A complete reporting reset is a separate, destructive operation. Perform it only when the user explicitly authorizes a clean start.

The reset must:

- Delete generated report payloads under active report history, workflow snapshots, latest pointers, and pending/processed request queues.
- Delete all prior report-period content under `archive/reports/`, including superseded-period snapshots.
- Reset the GitHub Actions index and both lint-scope indexes to empty indexes with a new UTC watermark.
- Replace `reports/triage/ledger.json` with an empty schema-valid Ledger, empty processed-report state, and unseeded lint baselines.
- Remove report-file entries from `.github/archive-retention-index.json`.
- Preserve report scripts, schemas, templates, assets, operating guides, workflow definitions, `archive/tasks/`, and the task retention entries.
- Preserve unrelated task records. Any unapproved Ledger-generated proposals whose evidence is being deleted must be cancelled and archived before their active board rows are removed.
- Do not bulk-import the old report history after the reset. The first complete tooling-valid full audit in each lint scope establishes its baseline without task creation. New and later actionable findings enter through normal event-driven ingestion.

This explicit reset is the only exception to the normal immutable report-period archive rule. Record the reset commit and cutoff in the active Ledger task.

## Retention policy

GitHub Actions checks the shared retention index weekly. It retains each indexed file for at least 90 days from its UTC archive timestamp.

- The index is `.github/archive-retention-index.json`. Entries reference one exact file under `archive/tasks/` or `archive/reports/`.
- The cleanup script reads the index only. It does not list, scan, or read either archive directory.
- When an indexed file reaches 90 days, the workflow deletes only that exact path and removes its index entry.
- Preserve `.gitkeep`. Never delete an unindexed record except during the explicit user-authorized clean-start reset described above.
- Legacy unindexed records remain protected unless their exact path and archive timestamp are verified.
- The cleanup workflow checks out `gpt`, verifies that `main` is an ancestor, and atomically fast-forwards `main` to the resulting `gpt` commit. It does not force-push.
- The cleanup writer and all report/ledger publishers share the non-cancelling `gh-ac-report-writer` concurrency group. The diagnostics job runs after cleanup and acquires the same group sequentially.
- Archived records are immutable after their initial write. Only scheduled retention may delete individually indexed archived files, except for an explicit user-authorized full report reset.

## Task board history

Keep at most the seven most recently completed or cancelled tasks in the board's Historical section. After an archive file expires, preserve its board entry's link to the commit containing the archived record; do not leave a dead path link.

## Archive record requirements

Before archiving a task, confirm that it contains:

- Final status and outcome.
- Archive timestamp in UTC.
- Completed acceptance criteria.
- Actual verification results and limitations.
- Relevant file and commit references.
- A final handoff or closure note.
