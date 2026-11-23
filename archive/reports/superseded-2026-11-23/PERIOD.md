# Superseded reporting period — 2026-11-23

- **Status:** Superseded; immutable archive snapshot
- **Archived at (UTC):** 2026-11-23T16:09:08Z
- **Previous Actions baseline:** 2026-11-23T05:49:04Z
- **Previous Actions sweep watermark:** 2026-11-23T14:53:22Z
- **Previous Actions index records:** 850
- **Previous changed-lint index records:** 44
- **Previous repository-lint index records:** 16
- **Ledger findings preserved:** 462
- **Evidence-only capture directories retained in active history:** 59
- **Files in evidence-only capture directories retained:** 200
- **Pending capture directories retained in active history:** 6
- **Files in pending capture directories retained:** 24
- **Historical report files moved to this archive:** 3,954
- **Pending source run IDs carried forward:** 45207707231, 45204490379, 45202163346, 45198986957

## Path mapping

Every archived report file preserves its path below the former report-family root:

- `reports/gh_ac_reports/<path>` → `archive/reports/superseded-2026-11-23/gh_ac_reports/<path>`
- `reports/lint_reports/<path>` → `archive/reports/superseded-2026-11-23/lint_reports/<path>`

The archived indexes and latest-pointer files are point-in-time snapshots. Their internal history paths retain the original report-root-relative names; use the path mapping above to locate the archived capture. The active report roots contain a fresh index baseline and only the pending captures carried forward at the cutoff.

## Evidence and retention

The Ledger remains intact. All 462 findings and their 59 distinct evidence captures remain available at their original paths. Those evidence-only captures are excluded from active indexes, so they cannot be re-ingested. The prior processed-report set remains intact. No finding was resolved or discarded as part of this reset.

The period snapshot is deliberately unindexed in `.github/archive-retention-index.json`; the shared archive policy preserves unindexed records. The 90-day cleanup therefore cannot delete this historical period.

No workflows were dispatched, polled, or rerun for this archival operation. Pending runs will be handled by the next natural diagnostics sweep.
