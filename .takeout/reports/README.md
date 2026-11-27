# Reports

Single entry point for generated repository reports.

- [lint_reports/](lint_reports/README.md): STE lint findings, per-scope baselines, and fingerprints.
- [gh_ac_reports/](gh_ac_reports/README.md): GitHub Actions workflow, job, step, log, annotation, and artifact diagnostics.
- [triage/](triage/README.md): shared cross-family issue Ledger and event-driven Worker task handoff.

## Normal operation

CI owns generated report files. Do not edit report payloads manually. The family indexes identify active reports. The Ledger ingests only indexed report paths. Keep each report in its immutable family history path. Do not move report payloads into task folders, create report archives or retention copies, or add cleanup schedules.

## Clean-start reset

A full reset is destructive and requires explicit user authorization. It clears generated active reports, latest pointers, request queues, report indexes, and active Ledger findings/processing state. It preserves report scripts, schemas, templates, workflow definitions, assets, operating guides, and unrelated active tasks. Both lint scopes restart with unseeded baselines. Their first complete tooling-valid full audits seed the new period without creating findings or tasks.

Normal reporting-period rollover is not a full reset. It preserves open-finding evidence and processed state. See [the Ledger guide](triage/README.md) for report intake and [the workspace guide](../../workspace/README.md) for task capture and closeout rules.

A clean-start reset affects the current branch tree only. It does not rewrite Git commit history or delete GitHub Actions run records; prior report blobs remain available in earlier commits unless a separate history-rewrite operation is explicitly authorized.
