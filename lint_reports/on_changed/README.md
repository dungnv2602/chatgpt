# Changed-document Lint Reports

Canonical reports for the changed-document STE workflow. Incremental runs and full-audit fallbacks both belong here. The execution mode field distinguishes them.

- Latest report: `latest-lint-report.md` and `latest-lint-report.json`.
- Historical evidence: `history/<run-id>-attempt-<attempt>/`.
- Each run includes `report.md`, `report.json`, and `integrity.json`.

The shared generator records the exact changed or fallback-audit file set, per-file metrics and complete diagnostics, report-tooling checks, anchor-check output when run, baseline comparisons, and run provenance. JSON retains the complete original per-file linter payload. The scope index and latest pointers include successful and failed completed reports.

Do not edit generated reports. Update the canonical template, schema, generator, regression tests, Document Type Catalog, workflows, and owner documentation together when the format changes.
