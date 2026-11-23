# Lint Evidence Repository

This directory is the primary review surface for hosted STE lint results. Read the generated report before retrieving GitHub Actions artifacts.

## Scopes

- [on_repo/](on_repo/README.md) stores repository-wide technical-document audits.
- [on_changed/](on_changed/README.md) stores changed-document STE runs. Full-audit fallbacks remain in this scope because the changed-document workflow initiated them.

## Evidence layers

Each report run has an immutable history directory containing:

- `report.md`: the detailed review document. It lists exact file coverage, every per-file result and metric, all normalized diagnostics, rule totals, validation-check output, baseline changes, and run provenance.
- `report.json`: the structured record. It retains original per-file linter JSON payloads, normalized findings, fingerprints, check output, exact paths, runtime metadata, and execution results.
- `integrity.json`: SHA-256 checksums for the Markdown and JSON reports.

Each scope also maintains:

- `latest-lint-report.md` and `latest-lint-report.json`: latest completed report, including failures.
- `index.json`: run locator and summary metrics. Read it before opening historical reports.

The root `latest-lint-report.md` remains a compatibility copy of the latest repository-wide report. Scope-specific reports are canonical. Historical run folders are append-only. Older runs cannot move a latest pointer backward.

## Review order

1. Read the relevant scope index.
2. Read the latest Markdown report for the complete human-readable analysis.
3. Read JSON for exact source records, finding fingerprints, and machine processing.
4. Retrieve Actions logs or artifacts only when the report lacks runner-level evidence.

## Status and integrity

- `Passed`: all evaluated checks completed successfully.
- `Failed`: at least one lint file, report-tooling test, or validation check failed.
- `Incomplete`: evidence capture or execution did not complete.
- `Cancelled` and `Superseded`: the run did not complete a current audit.

A finding fingerprint is derived from the file path and stable diagnostic fields. It is a correlation key, not proof that two findings have identical meaning. The report distinguishes lint findings from validation-check failures and preserves both. Do not infer repository-wide coverage from an incremental report.


## Reporting periods

The pre-reset lint history, indexes, and prior latest-pointer snapshots are preserved at `archive/reports/superseded-2026-11-23/lint_reports/`, except capture directories retained at their existing paths because open Ledger findings reference them. The active `on_changed` and `on_repo` indexes retain only lint reports belonging to source runs that were still pending at the reset cutoff. Latest pointers are rebuilt from those carried-forward captures. Evidence-only directories are not indexed for new ingestion. The Ledger and its processed-report state are unchanged.
