# Reports

Single entry point for generated repository reports.

- [lint_reports/](lint_reports/README.md): STE lint findings, per-scope baselines, and fingerprints.
- [gh_ac_reports/](gh_ac_reports/README.md): GitHub Actions workflow, job, step, log, annotation, and artifact diagnostics.
- [triage/](triage/README.md): shared cross-family issue Ledger and event-driven Worker task handoff.

## Normal operation

CI owns generated report files. Do not edit report payloads manually. The family indexes identify active reports; the Ledger ingests only indexed report paths. Report payloads needed by a completed task move to `workspace/archive/reports/` with their exact paths registered in `.github/archive-retention-index.json`. The shared scheduled retention workflow deletes each indexed task/report archive file after 90 days.

## Clean-start reset

A full reset is destructive and requires explicit user authorization. It clears generated active reports, latest pointers, request queues, all prior `workspace/archive/reports/**` snapshots, report indexes, and active Ledger findings/processing state. It preserves report scripts, schemas, templates, workflow definitions, assets, operating guides, task archives, and unrelated active tasks. Both lint scopes restart with unseeded baselines; their first complete tooling-valid full audits seed the new period without creating findings or tasks.

Normal reporting-period rollover is not a full reset. It preserves open-finding evidence and processed state. See [the Ledger guide](triage/README.md) and [archive guide](../../workspace/archive/README.md) for exact lifecycle rules.

A clean-start reset affects the current branch tree only. It does not rewrite Git commit history or delete GitHub Actions run records; prior report blobs remain available in earlier commits unless a separate history-rewrite operation is explicitly authorized.
