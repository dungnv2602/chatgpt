# Task and Report Archive

This directory stores immutable task records and individually retained CI report evidence. Accepted ADRs remain permanently in the flat `workspace/adr/` directory and never enter this retention area.

## Structure

- `workspace/archive/task/` stores completed and cancelled task records.
- `workspace/archive/reports/` stores report files that no longer support an open finding or active investigation. Preserve each report family's relative path.
- Keep task IDs, filenames, folder structure, and report payload bytes unchanged during archival.
- Record each archive timestamp in UTC. Do not store full conversation transcripts.

## Task archival

1. Before closing a Ledger-generated task as Done, verify that every finding in its Ledger Findings section is terminal: resolved, accepted, false_positive, or duplicate.
2. Archive the complete task folder at `workspace/archive/task/<task-id>/`. Include `task.md`, `subtasks/README.md`, and every child record.
3. Add one retention-index entry for every exact archived file path. Use one shared `archived_at_utc` timestamp for every file in the task folder.
4. Read back every archived file and verify every index entry before deleting the active task folder.
5. Keep finding IDs, resolution history, and prior task references in the Ledger after task archival. Recurrence may reopen the same finding identity and link new remediation work.
6. The Ledger reads retained task archives only through exact paths in the retention index. It supports folder archives and historical flat task files. It does not scan archive directories.

A task with any open or non-terminal finding must not be closed as Done. Cancelled tasks do not change open finding state.

## Report filing

When a report is no longer required by an open finding or active investigation:

1. Move the exact report file to `workspace/archive/reports/`, preserving its report-family path.
2. Add one entry to `.github/archive-retention-index.json` with the exact path and UTC move timestamp.
3. Do not archive a file that an open finding or active investigation still references.
4. Do not manually delete an indexed archived file. The weekly retention workflow deletes each exact indexed file after 90 days.

## Clean-start reset

A complete reporting reset is destructive. Perform it only when the user explicitly authorizes a clean start.

The reset may delete generated active report payloads, workflow snapshots, latest pointers, request queues, and prior `workspace/archive/reports/**` snapshots. It may reset report indexes and Ledger state only within the approved reset scope. It must preserve scripts, schemas, templates, assets, operating guides, task archives, task-retention entries, accepted ADRs, and unrelated tasks unless the user explicitly includes them.

Normal reporting-period rollover is not a full reset. It preserves open-finding evidence and processed state.

## Retention policy

GitHub Actions checks `.github/archive-retention-index.json` weekly. It retains task-folder archives and individual legacy/report files for at least 90 days.

- Each index entry references one exact file under `workspace/archive/task/` or `workspace/archive/reports/`.
- A folder archive requires indexed `task.md`, `subtasks/README.md`, and every child record. All entries for that folder share one UTC timestamp.
- The cleanup script reads the index only. It does not list, scan, or read archive directories.
- When a task folder reaches 90 days, the workflow deletes all exact indexed files in that folder as one unit. It fails closed if required entries or the shared timestamp are missing.
- A missing indexed file before expiry is an archive-integrity error. Do not silently prune the entry or reconstruct historical content.
- Remove a stale index entry only after exact-path repository-history lookup confirms that the original file is unrecoverable and the user explicitly approves the correction. Record the paths and rationale in the discussion register and governing task.
- Historical flat task files and report files expire individually from their own timestamps.
- Preserve `.gitkeep`. Never delete an unindexed record during normal cleanup.
- Legacy unindexed records remain protected unless their exact path and archive timestamp are verified.
- The cleanup workflow checks out `gpt`, verifies that `main` is an ancestor, and atomically fast-forwards `main` to the resulting `gpt` commit. It does not force-push.
- The cleanup writer and report/Ledger publishers share the non-cancelling `gh-ac-report-writer` concurrency group.
- ADRs do not belong here and are never subject to 90-day retention.
