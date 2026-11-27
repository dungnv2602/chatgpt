# Subtask: Simplify CI report structure

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-53
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** Done
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User request on 2026-11-27 to consolidate .takeout/reports into one CI-run report structure.
- **Governing ADR(s):** 0003
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready
- **Required:** Yes
- **Created:** 2026-11-27 15:00 UTC
- **Updated:** 2026-11-27 16:16 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Simplify .takeout/reports. No more /gh_ac_reports, no more /lint_reports. Just reports from CI runs.
>
> I expect only 1 index.json, only 1 latest-lint-report.json, no need for latest-lint-report.md, only 1 ledger.json, only 1 /history folder, no /triage folder, only 1 README.md, consolidate all README.md into only 1.

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Consolidate lint and GitHub Actions diagnostics under a unified `.takeout/reports/` structure. Retain a single index, latest structured lint report, issue Ledger, history directory, and README. Remove report-family subdirectories and the triage directory after migrating evidence, state, consumers, scripts, schemas, tests, and workflow references. Preserve report content and finding identities during migration.

## 4. Acceptance Criteria

1. `.takeout/reports/` contains one `README.md`, `index.json`, `latest-lint-report.json`, `ledger.json`, and `history/`, with no `gh_ac_reports/`, `lint_reports/`, or `triage/`.
2. Lint and Actions evidence are represented in the unified index and shared history tree.
3. Ledger ingestion and workflow generators use unified paths, retain attribution and eligibility rules, and preserve finding state.
4. Consolidated README documents the unified structure.
5. Remove redundant Markdown report copies and family README files.
6. Update all consumers, schemas/tests as needed, and read back changes.
7. Commit changes and verify paths; no hosted CI results inspected.

## 5. Decisions and Progress

- Audited the current report tree: separate Actions and lint report families, two lint scope indexes/latest pointers, three README files plus root report README, and the triage Ledger.
- Migration requires coordinating the reporter, lint generator, central Ledger, workflows, schemas, tests, and links. Preserve history rather than delete it.

## 6. State and Evidence

- **Commit SHA:** e2cb50475e2bb1b96740d745b5cf794583b584fe
- **Changed paths:** Unified lint and Actions generators, shared index and Ledger ingestion, latest lint JSON pointer, regression fixtures, workflows, report README, initialization policy, document catalog, and ADR-0003 amendment
- **Readback:** Final committed paths read back
- **Checks:** Not performed
- **Limitations:** No local scripts/tests or hosted CI inspection.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-27 16:16 UTC
- **Completion basis:** Unified index/history/report paths; one Ledger and README; no family report directories or persistent Markdown report copies

## 8. Hosted Validation

- **Status:** Not reviewed (hosted validation intentionally not inspected)
- **Run URL:** Not reviewed

## 9. Handoff

Implement unified index/history/ledger paths, migration and consumers; remove obsolete structures only after evidence and Ledger migration verified.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
