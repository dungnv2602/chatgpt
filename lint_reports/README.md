# Lint Evidence Repository

This directory is the primary review surface for hosted STE lint results. Review these reports before retrieving GitHub Actions artifacts.

## Scopes

- [on_repo/](on_repo/README.md) stores repository-wide technical-document audits.
- [on_changed/](on_changed/README.md) stores changed-document STE runs. Full-audit fallbacks remain in this scope because the changed-document workflow initiated them.

## Evidence layers

Each completed run has an immutable history directory containing:
- `report.md`: readable coverage, execution status, per-file outcomes, and findings.
- `report.json`: structured evidence with execution metadata and original linter JSON payloads.

Each scope also maintains:
- `latest-lint-report.md` and `latest-lint-report.json`: latest completed report, including failures.
- `index.json`: compact run locator. Read it before opening historical reports.

The root `latest-lint-report.md` remains a compatibility copy for existing links. The scope-specific report is canonical.

## Review order

1. Read the relevant scope index.
2. Read the latest Markdown report.
3. Read JSON for exact finding data, fingerprints, and per-file source payloads.
4. Retrieve Actions logs/artifacts only when the report does not contain the needed runner-level evidence.

## Status and integrity

- `Passed`: all evaluated checks completed successfully.
- `Failed`: at least one evaluated check failed.
- `Incomplete`: evidence capture or execution did not complete.

A finding fingerprint is derived from the file path and stable diagnostic fields. It is a correlation key, not proof that two findings have identical meaning. Historical run directories are append-only. Latest pointers may advance only when a run completes report generation.

Reports preserve the commit SHA, run ID, attempt, baseline SHA where applicable, execution mode, exact evaluated paths, and original structured linter output. Do not infer repository-wide coverage from an incremental report.
