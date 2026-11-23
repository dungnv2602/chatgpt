# Task Archive

This directory stores completed and cancelled task records temporarily.

The Worker skill defines task completion and archival procedures.

## Structure

- `archive/tasks/` stores archived task records.
- `archive/reports/` stores individually archived resolved report files, preserving their paths below this directory.
- Keep the original task ID and filename when moving a record.
- Record the UTC archive timestamp in the task metadata.
- Do not store full conversation transcripts.

## Superseded report-period archives

When the user authorizes a fresh reporting baseline, archive the prior period as one immutable snapshot under `archive/reports/superseded-YYYY-MM-DD/`. Preserve each report family's relative paths, including history captures, indexes, and prior latest-pointer snapshots. Add a period manifest with the cutoff, source baseline, path mapping, archived file counts, and pending run IDs carried forward.

Before moving report history, retain any complete capture directory referenced by an open Ledger finding or active investigation at its existing report-root path. These evidence-only directories must be excluded from the new operational indexes but remain readable at their existing paths. Keep incomplete pending run IDs and their capture directories in the active indexes. Archive all other prior history, indexes, and latest-pointer snapshots. Reset active indexes to the pending records and advance the sweep watermark to the new cutoff. Do not clear the Ledger or re-import historical findings.

A superseded period archive may contain old indexes and captures that are no longer active. Keep the period snapshot unindexed in `.github/archive-retention-index.json`; the shared policy preserves unindexed records. The archive is immutable after its initial commit. This period-snapshot procedure is distinct from individual resolved-report filing below.

## Resolved report filing

When a finding is verified as resolved in `reports/triage/ledger.json`:

1. Keep the triage entry and fix/verification references.
2. Move each no-longer-needed report file individually to `archive/reports/`, preserving its path below the report-family root.
3. Add one index entry per moved file to `.github/archive-retention-index.json` with its exact archive path and the UTC timestamp of that move (`archived_at_utc`).
4. Do not archive a file still referenced by an open finding, a current/latest pointer, or an active investigation.
5. Do not manually delete an archived file. The existing weekly retention workflow deletes each exact indexed file after 90 days from its own archive timestamp.

The report archive uses the same index, schedule, cleanup script, and 90-day individual-file retention as task records. There is no separate report archive policy or workflow.

## Retention policy

GitHub Actions checks a small retention index once each week. It retains each indexed task record for at least 90 days from its UTC archive timestamp.

- The index is `.github/archive-retention-index.json`. Each entry contains one exact file path under `archive/tasks/` or `archive/reports/` and its individual UTC archive timestamp.
- The scheduled workflow reads the index only. It does not list, scan, or read the contents of either archive directory.
- When an indexed record reaches 90 days, the workflow checks and deletes only that exact path. It then removes the entry from the index.
- Preserve `.gitkeep`. Never delete an unindexed record.
- Existing records that were archived before the index was introduced remain protected. Do not scan or backfill them automatically. Add a legacy record only when its exact path and archive timestamp are needed and verified.
- The workflow has only the scheduled trigger. The cleanup script also rejects every GitHub event except `schedule`.
- The workflow checks out `gpt`, verifies that `main` is an ancestor, and atomically fast-forwards `main` to the resulting `gpt` commit. It does not force-push.
- The Worker may read an exact archived record when a task requires it. The Worker must not edit, replace, rename, move, or manually delete an archived record.
- An archived record is immutable after its initial archive write. Only the scheduled retention workflow may delete individually indexed files from `archive/tasks/` and `archive/reports/`.
- Git history retains prior committed versions. This policy controls files in the current archive folder.

The weekly check does not inspect archive files unless an indexed entry has reached its expiry date. Unindexed legacy records remain in place until they are individually indexed under an explicitly verified archive timestamp.

## Task board history

Keep a compact historical entry on the task board after an archive file is deleted.

Before deleting an archived file, ensure the board entry links to the commit that contains the archived record. Do not leave a dead link to the removed path.

## Archive record requirements

Before moving a task into this folder, confirm that it contains:

- Final status and outcome.
- Archive timestamp in UTC.
- Completed acceptance criteria.
- Actual verification results and limitations.
- Relevant file and commit references.
- A final handoff or closure note.
