# Task Archive

This directory stores completed and cancelled task records for a limited period.

The Worker skill defines task completion and archival procedures.

## Structure

- archive/tasks/ stores archived task records.
- Keep the original task ID and filename when moving a record.
- Record the UTC archive timestamp in the task metadata.
- Do not store full conversation transcripts.

## Retention policy

The retention period is **14 days** from the recorded archive timestamp.

- Keep an archived task record for 14 days.
- Treat a record as eligible for deletion when its age reaches 14 days.
- Check for expired records during each Worker activation and task closeout.
- Delete every eligible task record from the archive folder.
- Do not delete active task records.
- If no Worker activity occurs, cleanup waits until the next Worker activation or closeout.
- Git history retains prior committed versions. This policy controls files in the current archive folder.

## Task board history

Keep a compact historical entry on the task board after an archive file expires.

Before deleting an expired file, ensure the board entry links to the commit that contains the archived record. Do not leave a dead link to the removed path.

## Archive record requirements

Before moving a task into this folder, confirm that it contains:

- Final status and outcome.
- Archive timestamp in UTC.
- Completed acceptance criteria.
- Actual verification results and limitations.
- Relevant file and commit references.
- A final handoff or closure note.
