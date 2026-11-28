---
record_type: decision-record
template_version: "1.1"
id: "ADR-0007"
status: "accepted"
decision_date: "2026-11-28"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0008"
source_draft_revision: 1
approved_scope: "Option 2: remove .takeout/reports/latest-lint-report.json and use .takeout/reports/index.json as the sole locator for latest lint reports, resolving validated immutable history reports."
related_adrs:
  - "ADR-0003"
supersedes: []
superseded_by: null
implementation_status: "in-progress"
implementation_tasks:
  - "20261127-173500"
review_triggers:
  - "A required external consumer is found to depend on the removed path."
  - "Index lookup fails to preserve baseline comparison or resolved-finding behavior."
---

# Unified index as the sole latest lint report locator

## Decision

Use `.takeout/reports/index.json` as the sole locator for the latest lint report. Remove `.takeout/reports/latest-lint-report.json`. Consumers must select an eligible lint entry for the exact scope, validate its status and path, and read the immutable JSON report from its history directory.

## Scope

Supersede only the latest-file requirement in ADR-0003. Preserve ADR-0003's other accepted requirements, report schemas, finding identity, baseline behavior, evidence retention, and Ledger integration.

## Safeguards

- Validate index structure and selected entry identity, family, scope, status, and safe history path.
- Reject path traversal and require the report to exist.
- Fall back to a full audit if the index or selected report is unusable.
- Keep immutable history report JSON. Update generator, workflows, regression tests, and guide together.
- Preserve report history, Ledger and index. Do not inspect hosted CI or execute tests for this task.

## Approval and implementation

DRAFT-0005 revision 1, Option 2 was approved by the user on 2026-11-28. The source reference was corrected administratively to DRAFT-0008 after DRAFT-0005 was found to collide with ADR-0004 provenance. This correction changes no approved decision content or scope. Execution began after the user's explicit `execute` cue on 2026-11-28. ADR-0003 remains immutable.
