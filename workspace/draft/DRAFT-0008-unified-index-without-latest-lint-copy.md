---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0008"
revision: 2
status: "approved-for-adr"
created: "2026-11-27"
updated: "2026-11-28"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs:
  - "ADR-0003"
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# Use the unified CI report index without a standalone latest lint copy

## Proposal Summary

Administrative provenance correction: this proposal previously reused ID DRAFT-0005, which is already recorded as the source of accepted ADR-0004. Its ID is now DRAFT-0008. Revision 2 changes only this ID, status normalization, and the approval/provenance references. The approved proposal content and scope are unchanged, so the revision-1 approval remains applicable.

Remove `.takeout/reports/latest-lint-report.json`. Use `.takeout/reports/index.json` as the only locator for the latest lint report. The index already records each report's family, scope, run identity, status, and repository-relative history path.

This proposal changes the accepted storage decision in ADR-0003. It does not authorize implementation until the user approves this exact Draft revision and the resulting ADR reaches accepted status.

## Context and Problem Statement

ADR-0003 currently requires one `latest-lint-report.json` file in addition to the shared index. The user has now requested its removal. The current implementation writes the latest report JSON to both its immutable history directory and the root latest file.

The shared index already records lint entries with a `history_path`. It sorts report entries by generated time, run number, and attempt. A consumer can select the newest eligible lint entry for its scope and read `report.json` from that history path.

The generator and both lint workflows still refer to the standalone file. The changed-document workflow also uses the standalone report as its baseline source. The full-document workflow passes the same path to the generator. These consumers must change together.

The current shared index has no run entries because the user directed the report history reset. The current latest JSON file contains only an empty baseline marker. The repository has not run local tests or reviewed hosted CI results for this proposal.

## Goals and Non-Goals

### Goals

- Remove the standalone latest lint JSON copy.
- Make the shared index the only locator for latest lint reports.
- Preserve baseline comparison and resolved-finding detection.
- Keep immutable report JSON in the shared history directory.
- Remove active code, workflow, test, and guide dependencies on the standalone path.

### Non-Goals

- Change lint eligibility, finding identity, or report schemas.
- Change Actions report retention or classification.
- Change Ledger ingestion or task attribution.
- Delete immutable report JSON or captured logs.
- Inspect hosted CI results or run tests locally.

## Decision Drivers

| Criterion | Why it matters | Relative importance |
|---|---|---|
| One source of truth | Avoid a second latest-report copy that can become stale. | High |
| Baseline correctness | Preserve the current comparison and resolved-finding behavior. | High |
| Evidence durability | Keep immutable report JSON and integrity data in history. | High |
| Safe path resolution | Reject missing, malformed, or unsafe index paths and fall back to a full audit. | High |
| Maintenance cost | Keep the generator and workflows aligned with one index contract. | Medium |
| Migration compatibility | Update every active consumer before removing the file. | High |

## Assessment Basis and Evidence Limits

- **Scope of comparison:** Keep the current standalone latest JSON file, or remove it and derive the latest report path from the unified index.
- **Assessment method:** Compare current repository code, workflows, report index structure, and accepted ADR-0003. No tests or prototypes were run.
- **Evidence boundary:** The repository confirms that the index stores lint history paths and that the generator writes a latest JSON copy. It does not establish external consumers.
- **Key assumptions:** The index remains committed with each complete report. Its entries remain sorted newest first. Each referenced history directory contains the canonical report JSON.
- **Unresolved evidence gaps:** No hosted validation was inspected. No external consumer inventory is available. The history is empty after the user-directed reset.

## Considered Options

### Option 1 — Keep the standalone latest lint JSON

- **Description and operating model:** Retain `latest-lint-report.json` as a duplicate of the newest lint report. The generator writes the immutable history report and updates the root copy. Workflows use the root copy for baseline comparisons.
- **Repository and environment fit:** This matches the current accepted ADR-0003 and existing workflow arguments.
- **Good — strengths:** Consumers can read one fixed path. They do not need to parse the shared index or resolve a history path.
- **Neutral — trade-offs:** The root file duplicates data that already exists in immutable history. The generator must keep both copies synchronized.
- **Bad — weaknesses:** The root copy can become stale if a write fails or a consumer updates the index without updating the copy. It creates another file that must be committed and reviewed.
- **Implementation and migration cost:** No migration is required. Future changes must preserve the root copy and its ordering logic.
- **Dependencies and operational burden:** The generator and workflows depend on the latest-file contract. Maintainers must keep the root copy synchronized with the index.
- **Risks and safeguards:** A stale copy can cause incorrect baseline comparisons. Keep the existing ordering checks and add coverage for concurrent publication and recovery.
- **Evidence and confidence:** The current generator writes the report JSON to history and the root latest path. Both workflows pass the root path to the generator. High confidence from current repository source.
- **Limitations and unknowns:** No evidence establishes that an external consumer requires the fixed path. Tests and hosted workflows were not run for this review.

### Option 2 — Use the unified index as the only latest-report locator

- **Description and operating model:** Remove the root latest JSON file. Select the newest eligible lint entry for the required scope from `index.json`. Resolve its `history_path` and read the immutable `report.json` from that directory.
- **Repository and environment fit:** The current index already stores `family`, `scope`, run identity, status, and `history_path`. The generator already sorts entries by report time, run number, and attempt.
- **Good — strengths:** Removes the duplicate copy. The index becomes the only source for report discovery. Consumers read the same immutable JSON that the Ledger and history review use.
- **Neutral — trade-offs:** Consumers must parse the index and resolve the path. The index and report JSON must both be available in the checked-out commit.
- **Bad — weaknesses:** A malformed or stale index can prevent baseline discovery. A missing history report can make the selected entry unusable.
- **Implementation and migration cost:** Update the lint generator, both lint workflows, regression tests, and the report guide. The changed workflow must retrieve the latest complete lint entry and validate its report before using it. The full workflow must resolve its previous report from the checked-out index.
- **Dependencies and operational burden:** Depends on the shared index schema and stable history paths. The generator and workflows remain responsible for atomic publication and safe path checks.
- **Risks and safeguards:** An invalid entry could select the wrong report or escape the report root. Require the `lint` family, exact scope, complete status, a `history/` path without traversal segments, and an existing JSON report. Fall back to a full audit when validation fails.
- **Evidence and confidence:** Current generator entries include `history_path` and the index sorts newest first. High confidence for the existing data contract. The updated workflow behavior remains untested.
- **Limitations and unknowns:** The repository does not identify external consumers. No tests or hosted validation were run. The index can be empty after a reset, in which case the workflow must perform a full audit.

## Comparative Assessment

| Criterion | Option 1: Keep latest JSON | Option 2: Index only |
|---|---|---|
| One source of truth | Weak. Maintains a duplicate report copy. | Strong. Uses one index and immutable history report. |
| Baseline correctness | Strong if both writes remain synchronized. | Strong if consumers validate the selected index entry and report path. |
| Evidence durability | Strong. The history report remains canonical. | Strong. The same history report remains canonical. |
| Safe path resolution | Strong. Fixed path, but content may be stale. | Moderate. Requires strict path and identity checks. |
| Maintenance cost | Moderate. Maintains two synchronized outputs. | Strong. Maintains one locator contract. |
| Migration compatibility | Strong. No consumer changes. | Moderate. Requires coordinated workflow and generator changes. |

### Overall comparison

Option 1 offers simpler fixed-path access. It also preserves the accepted ADR-0003 decision. Its main cost is the duplicate latest report and the synchronization logic that maintains it.

Option 2 removes that duplicate state. The index already contains the required path and run metadata. Strict validation and a full-audit fallback can manage path and index failures. Option 1 would be preferable only if a required external consumer depends on the fixed root path. No such consumer is established by the repository evidence.

## Proposed Recommendation

Recommend Option 2. Remove the standalone latest lint JSON and use the unified index as the only latest-report locator.

This recommendation follows the user's explicit request and the repository's existing index contract. It preserves the immutable report source and the lint baseline behavior. It also removes a duplicate state file.

The recommendation depends on the index retaining a stable `history_path` and the workflows validating the selected entry. Evidence that a required external consumer depends on the fixed root path could change the recommendation.

## Consequences and Trade-Offs

- **Positive:** One index locates the latest lint report. The generator no longer writes a duplicate JSON copy.
- **Negative:** The workflows need safe index parsing and history-path resolution.
- **Neutral:** The immutable report JSON remains under history. Baseline comparison still reads a previous report.
- **Conditional:** A full audit runs when the index has no eligible entry or the selected report fails validation.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| Index entry is missing or malformed. | Medium / High | The index is the only locator. | Validate structure, family, scope, status, and required fields. Fall back to a full audit. | A malformed index may still require manual repair. |
| History path is unsafe. | Low / High | The path comes from repository data. | Require a `history/` prefix and reject traversal segments. | A future schema change may need new validation. |
| Report JSON is missing. | Medium / High | The index can reference a removed or uncommitted path. | Check the file before baseline use. Fall back to a full audit. | Baseline comparison is unavailable until a complete report exists. |
| An external consumer needs the fixed path. | Unknown / High | No external consumer inventory is available. | Search repository references and ask about known external integrations before migration. | External use may remain unknown. |
| Baseline behavior changes. | Medium / High | The workflow changes its report lookup method. | Preserve existing eligibility checks and add regression coverage for index selection and fallback. | Hosted behavior remains unverified until normal CI runs. |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Lint generator | Stop writing the root latest JSON copy. Keep optional previous-report input. | `.agent/skills/asd-ste100/scripts/generate_lint_report.py` | This Draft and accepted ADR |
| Changed lint workflow | Select the latest complete `on_changed` report from the shared index. | `.github/workflows/ste-lint-changed.yml` | This Draft and accepted ADR |
| Full lint workflow | Resolve the previous `on_repo` report from the shared index. | `.github/workflows/ste-lint-full-docs.yml` | This Draft and accepted ADR |
| Regression tests | Verify that the generator does not create a root latest file and that index lookup preserves baseline behavior. | `.agent/skills/asd-ste100/scripts/test_generate_lint_report.py` and workflow-owned checks | This Draft and accepted ADR |
| Report guide | Document the index-only layout. | `.takeout/reports/README.md` | This Draft and accepted ADR |
| Report data | Delete the root latest JSON file. Preserve index, ledger, README, and history. | `.takeout/reports/latest-lint-report.json` | This Draft and accepted ADR |
| Decision record | Supersede only the latest-file requirement in ADR-0003. Preserve its other accepted requirements. | New ADR linked to ADR-0003 | User approval of this Draft |

## Proposed Implementation Outline

1. Obtain approval for this exact Draft revision and scope.
2. Promote the Draft to a new accepted ADR. Keep ADR-0003 immutable.
3. Update the generator and workflows in one coordinated implementation.
4. Update regression tests and the report guide.
5. Delete the root latest JSON file.
6. Read back all changed paths and confirm that active consumers use the unified index.
7. Leave hosted validation unreviewed unless the user requests review.

## Questions for the User

No further decision is required for the approved scope. Promote this exact approved content to an ADR after the ID/provenance reconciliation.

## Review and Approval

- **Revision presented:** Revision 2 (administrative ID correction; content unchanged)
- **User decision:** Approved Option 2 on revision 1; approval retained for unchanged proposal content
- **Approved scope:** DRAFT-0008 revision 2, carrying forward the unchanged approval of revision 1, Option 2: remove `.takeout/reports/latest-lint-report.json` and use `.takeout/reports/index.json` as the sole latest-lint-report locator, resolving validated immutable history reports; implementation remains separately gated.
- **Decision date:** 2026-11-28
- **Resulting ADR:** Pending promotion

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-27 | 1 | Initial proposal to remove the standalone latest lint JSON and use the unified index. | Approved on 2026-11-28: Option 2, exact revision 1. |\n| 2026-11-28 | 2 | Administrative ID correction from DRAFT-0005 to DRAFT-0008; status normalized to approved-for-adr. Proposal content and scope unchanged. | Approval of revision 1 retained; no new decision requested. |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | `.agent/skills/asd-ste100/scripts/generate_lint_report.py`, index writer and latest JSON writer | Branch `gpt`, current source read during this session | Repository fact | Both options' current behavior; index includes history paths and generator writes latest copy. | No local tests were run. |
| E2 | `.github/workflows/ste-lint-changed.yml`, baseline preflight and generator invocation | Branch `gpt`, current source read during this session | Repository fact | Current fixed-path consumer and required migration. | Hosted workflow behavior was not inspected. |
| E3 | `.github/workflows/ste-lint-full-docs.yml`, generator invocation and publication step | Branch `gpt`, current source read during this session | Repository fact | Current fixed-path consumer and required migration. | Hosted workflow behavior was not inspected. |
| E4 | `.takeout/reports/index.json` | Branch `gpt`, current committed state | Repository fact | Unified index is currently empty after the history reset. | Empty state does not demonstrate next-run behavior. |
| E5 | `workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md` | Branch `gpt`, current accepted ADR | Repository fact | The accepted decision currently requires one latest lint JSON file. | The ADR remains authoritative until a new ADR is accepted. |
| E6 | User instruction in this conversation | 2026-11-27 | User instruction | Requests deletion of the standalone latest lint JSON. | User approved Option 2, revision 1 on 2026-11-28; revision 2 is an administrative ID correction. |

