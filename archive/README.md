# Task Archive

This directory stores completed and cancelled task records temporarily.

The Worker skill defines task completion and archival procedures.

## Structure

- archive/tasks/ stores archived task records.
- Keep the original task ID and filename when moving a record.
- Record the UTC archive timestamp in the task metadata.
- Do not store full conversation transcripts.

## Retention policy

GitHub Actions checks a small retention index once each week. It retains each indexed task record for at least 90 days from its UTC archive timestamp.

- The index is `.github/archive-retention-index.json`. Each entry contains one exact `archive/tasks/<filename>` path and its UTC archive timestamp.
- The scheduled workflow reads the index only. It does not list, scan, or read the contents of `archive/tasks/`.
- When an indexed record reaches 90 days, the workflow checks and deletes only that exact path. It then removes the entry from the index.
- Preserve `.gitkeep`. Never delete an unindexed record.
- Existing records that were archived before the index was introduced remain protected. Do not scan or backfill them automatically. Add a legacy record only when its exact path and archive timestamp are needed and verified.
- The workflow has only the scheduled trigger. The cleanup script also rejects every GitHub event except `schedule`.
- The workflow checks out `gpt`, verifies that `main` is an ancestor, and atomically fast-forwards `main` to the resulting `gpt` commit. It does not force-push.
- The Worker may read an exact archived record when a task requires it. The Worker must not edit, replace, rename, move, or manually delete an archived record.
- An archived record is immutable after its initial archive write. Only the scheduled retention workflow may delete indexed records from `archive/tasks/`.
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
