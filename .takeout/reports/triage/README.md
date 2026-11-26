# CI Ledger data and navigation

The CI Ledger tracks distinct findings from lint reports and GitHub Actions diagnostics. It stores active finding state, bounded evidence references, stable parent-task links, resolution history, and separate hosted-validation metadata. The Ledger does not execute remediation.

## Ownership

- **CI Ledger skill:** `.agent/skills/ci-ledger/SKILL.md` — finding governance, intake, identity, eligibility, evidence, task generation and linkage, lifecycle, resolution, recurrence retention, reset, and integrity.
- **The Worker:** task selection, authorization, batch orchestration, task records, board, progress, and closeout.
- **GitHub Actions skill:** technical CI diagnosis, remediation, recurrence prevention, workflow operations, and validation.
- **Data:** `ledger.json`.
- **Schema:** `ledger-schema.json` (version 1.5.0).
- **Generator:** `scripts/ledger.py`.
- **Regression tests:** `scripts/test_ledger.py`.

## Data contract

The data file stores:

- `schema_version` and `updated_at_utc`.
- `findings`: distinct finding records, including identity, source family, category, title, lifecycle status, severity, owner, first/last observation, cumulative occurrence count, bounded evidence, resolution, resolution history, duplicate relationship, accepted risk, task references, and task grouping.
- `ingestion_state`: processed report paths, lint baseline flags by scope, pending capture state, and other generator-managed ingestion metadata.

Finding IDs and report paths are stable references. Evidence rows retain the source report path, run URL, observation time, source-run identity, and concise note. The generator owns the structured format and schema validation.

## Report navigation

- [Report-family index](../README.md)
- [Lint reports](../lint_reports/README.md)
- [GitHub Actions diagnostics](../gh_ac_reports/README.md)
- [CI Ledger skill](../../../.agent/skills/ci-ledger/SKILL.md)
- [GitHub Actions skill](../../../.agent/skills/github-actions/SKILL.md)
- [The Worker](../../../.agent/skills/the-worker/SKILL.md)

## Operating boundary

Read the CI Ledger skill for all operational rules. Do not modify source reports or Ledger state outside the approved generator/publication flow. Do not scan historical report directories, backfill reports, or reset the Ledger without explicit authorization. Do not run scripts or tests locally.
