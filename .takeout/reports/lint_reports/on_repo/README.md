# Repository-wide Lint Reports

Canonical reports for full technical-document audits. The shared generator in `skills/asd-ste100/scripts/generate_lint_report.py` owns the report format for both lint scopes.

- Latest report: `latest-lint-report.md` and `latest-lint-report.json`.
- Historical evidence: `history/<run-id>-attempt-<attempt>/`.
- Each run includes a detailed `report.md`, structured `report.json`, and `integrity.json`.

The Markdown report lists every evaluated file, per-file status and metrics, all STE diagnostics, rule totals, report-tooling and anchor-check output, and run provenance. The JSON retains the original per-file linter payloads, fingerprints, and normalized findings. The repository root `lint_reports/latest-lint-report.md` remains a compatibility copy.

The report records lint findings and workflow-check failures separately. A generated report can have status Failed and still be a complete evidence capture. Do not edit generated reports.
