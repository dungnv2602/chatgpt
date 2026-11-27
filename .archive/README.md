# Task and Report Archive

This directory stores completed and cancelled task records and individually archived CI report files. It also stores permanent accepted ADRs.

## Structure

- .archive/task/ stores immutable archived task records.
- .archive/reports/ stores individually archived CI report files, preserving their path below the report-family root.
- .archive/adr/ stores permanent, immutable accepted Decision Records. ADRs are excluded from 90-day retention.
- Keep task IDs and filenames unchanged.
- Record each archive timestamp in UTC.
- Do not store full conversation transcripts.

## Permanent ADR archive

Move an accepted ADR to .archive/adr/ only after all linked implementation tasks are Done and every Confirmation criterion passes.

- Preserve the ADR ID and filename.
- Read back the archive copy after its initial write.
- Do not edit, replace, rename, move, or delete an archived ADR unless the user explicitly authorizes a narrow reference-only correction. Never change its accepted decision content.
- Never add ADR paths to .github/archive-retention-index.json.
- The 90-day retention workflow applies only to indexed task and report files. It must not delete ADRs.

### Source Drafts after ADR promotion

A successful ADR promotion deletes the source Draft after the provisional and accepted ADR read-back checks pass. The completeness review must preserve all material rationale before deletion.

- Do not move source Drafts into .archive/draft/.
- Do not create a Promoted Drafts index.
- Keep the Draft ID and approved revision as ADR provenance. Do not keep a link to a deleted source file.
- If deletion fails after acceptance, retain the source Draft temporarily. Record its resulting ADR ID and cleanup reason. List it only under Promotion Cleanup Pending.
- Retry only source deletion. After deletion succeeds, remove the cleanup-pending entry and read back the Draft and ADR indexes.
- This rule applies only to successful ADR promotion. It does not change retention for rejected, withdrawn, or superseded Drafts.

## Task resolution and Ledger retention

The active CI issue Ledger keeps finding identity and history. Task archival does not retire or delete findings.

1. Before closing a Ledger-generated task as Done, verify that every finding in its Ledger Findings section is terminal. Valid states are resolved, accepted, false_positive, and duplicate.
2. Move report files needed for the historical handoff to `.archive/reports/`. Preserve their report-family paths. Update the task's evidence links before you prepare its final archive copy.
3. Archive the complete task folder at `.archive/task/<task-id>/`. Include `task.md`, `subtasks/README.md`, and every child record.
4. Add one retention-index entry for every exact archived file path. Use one shared `archived_at_utc` timestamp for all files in the task folder.
5. Read back every archived file and verify every index entry before you delete the active task folder.
6. Keep finding IDs, resolution history, and prior task references in the Ledger after task archival. A later observation can reopen the same finding identity and link new remediation work.
7. On recurrence, the Ledger reads a retained prior task archive through its exact retention-index paths. It supports both folder archives and historical flat task files. It adds a Related tasks link to the new parent when the prior archive remains retained. It does not scan archive directories.

A task with any open or non-terminal finding must not be closed as Done. Cancelled tasks do not change open finding state.

## Normal report filing and retention

When a report is no longer required by an open finding or active investigation:

1. Move the exact report file to .archive/reports/, preserving its report-family path.
2. Add one index entry to .github/archive-retention-index.json with the exact archive path and the UTC timestamp of the move (archived_at_utc).
3. Do not archive a file still referenced by an open finding or active investigation.
4. Do not manually delete an indexed archived file. The weekly retention workflow deletes each exact indexed file after 90 days from its own archive timestamp.

New task-folder archives use one shared timestamp and expire as a complete folder group. The index must include task.md, subtasks/README.md, and every child record. Cleanup removes the exact indexed files together after 90 days. Historical flat task archives and report files retain individual 90-day periods.

## Explicit clean-start reset

A complete reporting reset is a separate, destructive operation. Perform it only when the user explicitly authorizes a clean start.

The reset must:

- Delete generated report payloads under active report history, workflow snapshots, latest pointers, and pending/processed request queues.
- Delete all prior report-period content under .archive/reports/, including superseded-period snapshots.
- Reset the GitHub Actions index and both lint-scope indexes to empty indexes with a new UTC watermark.
- Replace .takeout/reports/triage/ledger.json with an empty schema-valid Ledger, empty processed-report state, and unseeded lint baselines.
- Remove report-file entries from .github/archive-retention-index.json.
- Preserve report scripts, schemas, templates, assets, operating guides, workflow definitions,  .archive/task/, and the task retention entries.
- Preserve unrelated task records. Any unapproved Ledger-generated proposals whose evidence is being deleted must be cancelled and archived before their active board rows are removed.
- Do not bulk-import the old report history after the reset. The first complete tooling-valid full audit in each lint scope establishes its baseline without task creation. New and later actionable findings enter through normal event-driven ingestion.

This explicit reset is the only exception to the normal immutable report-period archive rule. Record the reset commit and cutoff in the active Ledger task. The reset changes the current branch tree only; it does not rewrite Git history or delete GitHub Actions run records. Earlier versions remain available in prior commits unless a separate history-rewrite operation is explicitly authorized.

## Retention policy

GitHub Actions checks the shared retention index weekly. It retains task-folder archives and individual legacy/report files for at least 90 days.

- The index is .github/archive-retention-index.json. Each entry references one exact file under .archive/task/ or .archive/reports/.
- A folder archive requires indexed task.md and subtasks/README.md entries plus every child record. All entries for that folder must share one UTC timestamp.
- The cleanup script reads the index only. It does not list, scan, or read either archive directory.
- When a task folder reaches 90 days, the workflow deletes all exact indexed files in that folder as one unit. It fails closed if required entries or the shared timestamp are missing.
- A missing indexed file before its retention period expires is an archive-integrity error. Do not silently prune the entry or reconstruct historical content.
- Historical flat task files and report files expire individually from their own timestamps.
- Preserve .gitkeep. Never delete an unindexed record except during the explicit user-authorized clean-start reset described above.
- Legacy unindexed records remain protected unless their exact path and archive timestamp are verified.
- The cleanup workflow checks out gpt, verifies that main is an ancestor, and atomically fast-forwards main to the resulting gpt commit. It does not force-push.
- The cleanup writer and all report/ledger publishers share the non-cancelling gh-ac-report-writer concurrency group. The diagnostics job runs after cleanup and acquires the same group sequentially.
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
