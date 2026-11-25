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


## Baselines and flood control

The changed-document workflow selects the latest complete tooling-valid report commit as its comparison baseline. It does not depend on the last successful GitHub Actions conclusion. A report may have status `Failed` because lint found violations and still serve as the baseline when report capture and tooling checks passed.

After a clean-start reset, the first complete full audit in each scope establishes a baseline without creating Ledger findings or tasks. For `on_changed`, this is a full-audit fallback. For `on_repo`, this is the repository-wide audit. The Ledger tracks baseline state independently for each scope.

Later reports distinguish new from recurring findings. New findings may enter the Ledger. Recurring findings refresh evidence only when the finding is already tracked. An untracked recurring finding from the baseline remains excluded, preventing a new reporting period from recreating the old task backlog.

An incomplete report or a report with failed tooling checks cannot seed a baseline. The scope remains unseeded until a complete, tooling-valid full audit arrives. Do not weaken lint rules or infer full-repository coverage from an incremental report.

## Reporting periods

A user-authorized clean-start reset removes the generated report history and all prior `archive/reports/**` snapshots. It empties the active indexes and Ledger and marks both lint baselines as unseeded. The first complete tooling-valid full audit in each scope then seeds the new baseline without task creation.

Normal rollover preserves open-finding evidence and does not clear the Ledger. See `reports/triage/README.md` for the complete reset, ingestion, and retirement rules.
