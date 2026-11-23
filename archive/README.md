# Task Archive

This directory stores completed and cancelled task records temporarily.

The Worker skill defines task completion and archival procedures.

## Structure

- archive/tasks/ stores archived task records.
- Keep the original task ID and filename when moving a record.
- Record the UTC archive timestamp in the task metadata.
- Do not store full conversation transcripts.

## Retention policy

GitHub Actions deletes archived task records in one batch every 14 days.

- The cleanup is periodic, not a rolling per-record retention period.
- On each due cleanup, delete the entire contents of `archive/tasks/`, regardless of each record's individual archive timestamp.
- Preserve `.gitkeep` so the directory remains in the repository.
- The workflow runs on the default branch. It checks out `gpt`. It deletes the contents of `archive/tasks/`. It then fast-forwards `main` to the same commit.
- The Worker may read an exact archived record when a task requires it. The Worker must not edit, replace, rename, move, or manually delete an archived record.
- An archived record is immutable after its initial archive write. Only the scheduled retention workflow may delete records from `archive/tasks/`.
- Git history retains prior committed versions. This policy controls files in the current archive folder.

GitHub Actions cron does not provide an exact every-14-days expression. The workflow checks weekly and uses a committed UTC timestamp to ensure a batch purge occurs only after at least 14 days have elapsed. The first purge occurs on the first scheduled run after that interval.

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
