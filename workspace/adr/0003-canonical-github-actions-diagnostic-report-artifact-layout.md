---
record_type: decision-record
template_version: "1.1"
id: "ADR-0003"
status: "superseded"
decision_date: "2026-11-26"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0004"
source_draft_revision: 1
approved_scope: "Option 3, as amended by the user on 2026-11-27: consolidate STE lint and GitHub Actions evidence under one .takeout/reports root, one index.json, one history directory, one latest-lint-report.json, one ledger.json, and one README.md. Do not persist Markdown report copies. Preserve the original Actions eligibility, cancellation, classification, Ledger identity, task generation, and lint baseline rules."
related_adrs: []
supersedes: []
superseded_by: "ADR-0008"
implementation_status: "superseded"
implementation_tasks:
review_triggers:
  - "A required external consumer is found to depend on a removed report path."
  - "The on-demand Markdown renderer or canonical integrity verification fails."
  - "The central index cannot reliably identify the latest retained report."
  - "Diagnostic evidence-retention requirements change."
---

<!-- Accepted on 2026-11-26 after the approved Draft and provisional ADR passed the completeness and read-back gates. -->

# Canonical GitHub Actions Diagnostic Report Artifact Layout

## Context and Problem Statement

The GitHub Actions diagnostic reporter stores several views of the same report.

- Each retained history folder contains `report.json`, `report.md`, `integrity.json`, and captured job logs.
- The repository root contains `index.json`, `latest-gh-ac-report.json`, and `latest-gh-ac-report.md`.
- Each workflow folder under `by_workflow/` contains an index and two latest-report copies.
- The repository-wide index already stores a `latest_report` object that points to the canonical history path.

The generator renders Markdown from structured JSON and uses a canonical template. The Ledger links to report JSON paths, not the Markdown copies.

The inventory at commit `f310d0921a6750caf40e7e314f0a7574bae120af` contains 29 retained history folders. The root contains two latest copies. Three workflow folders each contain an index and two latest copies. The inventory therefore contains 40 derived or redundant artifacts:

- 29 per-run Markdown renderings.
- Two root latest-report copies.
- Six per-workflow latest-report copies.
- Three per-workflow indexes.

This count excludes canonical JSON reports, integrity manifests, captured logs, and the repository-wide index. It counts files, not measured byte reduction.

A sample history folder contains `report.json` (7,058 bytes), `report.md` (4,167 bytes), and `integrity.json` (386 bytes), plus a logs directory. The root latest copies measured 12,937 bytes for JSON and 6,565 bytes for Markdown. These sample sizes show duplicated content. They do not establish the total storage reduction for the full inventory.

The current layout increases commit size and introduces several synchronization points. A generated Markdown report can be rendered again from its JSON source. Operators can derive a per-workflow index by filtering the repository-wide index on workflow ID. The root index already identifies the latest report.

The user approved DRAFT-0004 revision 1, Option 3, on 2026-11-26. This ADR records that decision. Artifact-layout changes remain prohibited until this ADR reaches accepted status.

## Decision Drivers

- **Evidence durability and integrity — High:** Preserve original structured evidence, captured logs, and verifiable integrity data.
- **Repository size and commit noise — High:** Remove generated copies that can be recreated from canonical evidence.
- **Discoverability — High:** Retain a reliable way to locate the latest report and historical reports by workflow and run.
- **Ledger compatibility — High:** Preserve existing history paths and every report JSON reference used by findings and tasks.
- **Human readability — Medium:** Keep Markdown review available through an on-demand renderer.
- **Consistency and maintenance — High:** Maintain one report source and one repository-wide index.
- **Migration and rollback risk — High:** Keep canonical evidence unchanged, including replacement or removal. Ensure that the generator can reproduce derived views.

## Considered Options

### Option 1 — Keep the current layout

- **Description and operating model:** Keep per-run JSON and Markdown files, integrity manifests, logs, root latest copies, per-workflow indexes, and per-workflow latest copies.
- **Repository and environment fit:** The current generator, report guide, and repository navigation support this layout.
- **Good — strengths:** Operators can skip migration and open Markdown reports directly. Each workflow has a separate index and latest view.
- **Neutral — trade-offs:** The generator must keep several views synchronized. The root index remains the repository-wide source of report metadata.
- **Bad — weaknesses:** The assessment snapshot contains all 40 derived or redundant artifacts. Markdown reports repeat information from JSON. Latest copies repeat history files. Per-workflow indexes repeat subsets of the root index. These copies can drift or create large commits.
- **Implementation and migration cost:** No implementation cost. Future report captures continue to write the same copies.
- **Dependencies and operational burden:** Retain all current scripts, templates, indexes, and documentation. Operators must understand which copy is canonical.
- **Risks and safeguards:** Copies can become stale. Rebuilding indexes reduces drift but retains duplication.
- **Evidence and confidence:** The inventory at `f310d092` confirms the file types and counts. This inventory has high confidence for that snapshot.
- **Limitations and unknowns:** The review did not measure the full byte cost. This option leaves repository growth unaddressed.

### Option 2 — Remove latest copies only

- **Description and operating model:** Keep per-run Markdown and JSON, integrity manifests, logs, the central index, and per-workflow indexes. Remove the root and per-workflow latest-report copies.
- **Repository and environment fit:** This option makes a limited change to the existing layout. It retains stored Markdown and workflow-specific navigation.
- **Good — strengths:** Removes eight latest-report copies while retaining stored Markdown and workflow navigation.
- **Neutral — trade-offs:** Operators use the central index for the latest report. Workflow indexes remain available.
- **Bad — weaknesses:** The assessment snapshot retains 29 per-run Markdown renderings and three per-workflow indexes. The layout still keeps several views of the same report data.
- **Implementation and migration cost:** Update latest-copy generation, tests, and the report guide. Remove the existing eight latest copies.
- **Dependencies and operational burden:** The central and workflow indexes remain. The generator still maintains several indexes.
- **Risks and safeguards:** Existing references may rely on latest-copy paths. Search references and review Ledger links before migration.
- **Evidence and confidence:** The root and workflow directory inventory confirms the eight latest copies. The evidence has high confidence for the inspected snapshot.
- **Limitations and unknowns:** This approach removes some duplication but retains most derived report artifacts.

### Option 3 — Keep canonical JSON, integrity, logs, and one central index

- **Description and operating model:** Retain `report.json`, `integrity.json`, and captured logs in each existing history folder. Use the repository-wide `index.json` as the sole index and latest-report pointer. Render Markdown from canonical JSON on demand. Delete per-run `report.md` files, root latest-report copies, and per-workflow indexes and latest copies.
- **Repository and environment fit:** The Ledger already links to report JSON paths. The root index lists workflow IDs and the latest-report path. The report generator has a Markdown renderer and template.
- **Good — strengths:** Retains the original structured evidence, logs, and integrity checks. It removes all 40 derived or redundant artifacts in the assessment snapshot. Report JSON remains canonical. The root index remains the sole index and latest pointer. Operators can filter workflow views from the root index.
- **Neutral — trade-offs:** Operators use the root index to find reports. A Markdown view requires an on-demand render step. The generator must rebuild the index correctly.
- **Bad — weaknesses:** Direct links to stored Markdown reports and per-workflow indexes will break. Update the report guide and repository references. JSON is less convenient for casual reading.
- **Implementation and migration cost:** Update the writer, integrity manifest generation, index builder, on-demand rendering interface, tests, and report guide. Remove only derived files from existing history folders. Regenerate integrity manifests for the retained JSON and logs. Keep all report JSON and captured log bytes unchanged.
- **Dependencies and operational burden:** Retain the report generator and template. The generator renders Markdown on demand and rebuilds the central index. It no longer maintains per-workflow copies.
- **Risks and safeguards:** A missing renderer reduces readability. The team must maintain and test it. A faulty migration could break task links or remove evidence. Preserve paths, compare hashes, and review every Ledger/task reference. Regression tests for index ordering and pruning help prevent stale latest pointers.
- **Evidence and confidence:** The root index contains the latest pointer and workflow metadata. Ledger evidence paths target report JSON. The report guide and sample history folder show that the generator creates Markdown alongside JSON. These repository facts have high confidence. The team has moderate confidence in migration effort.
- **Limitations and unknowns:** The assessment did not complete a repository reference search or external-consumer inventory. It did not measure a migration prototype or total bytes. External consumers remain unknown.

### Option 4 — Store reports and logs as GitHub workflow artifacts

- **Description and operating model:** Keep a small repository index and upload JSON reports and logs as workflow artifacts.
- **Repository and environment fit:** GitHub Actions supports workflow artifacts. This option would reduce the size of commits that publish diagnostic evidence.
- **Good — strengths:** Reduces repository storage. Workflow artifacts provide a direct link from a run to its captured files.
- **Neutral — trade-offs:** Operators retrieve evidence through the Actions interface or API. The index needs artifact identifiers or URLs.
- **Bad — weaknesses:** Evidence availability depends on artifact retention, permissions, and platform access. Expired artifacts can leave the repository without complete diagnostic evidence.
- **Implementation and migration cost:** Change capture and publication workflows, artifact upload/retrieval, index schema, permissions, retention, and recovery procedures. Define a durable evidence-recovery path.
- **Dependencies and operational burden:** Requires artifact permissions, retention settings, and an operational process to retrieve expired or inaccessible evidence.
- **Risks and safeguards:** Evidence may become unavailable after retention expiry or permission changes. A second durable store would be necessary to meet the current evidence-retention requirement.
- **Evidence and confidence:** GitHub Actions supports workflow artifacts. The assessment did not evaluate retention or permissions.
- **Limitations and unknowns:** The assessment did not test retention periods or access behavior. This option does not fit the repository's current role as the durable source of diagnostic evidence.

## Comparative Assessment

The matrix compares all materially viable options against the same six decision drivers. The detailed assessments above describe each option's operating model, costs, dependencies, risks, evidence, and limits.

| Criterion | Option 1: Current layout | Option 2: Remove latest copies | Option 3: Canonical JSON | Option 4: Workflow artifacts |
|---|---|---|---|---|
| Evidence durability and integrity | Strong. All evidence remains in the repository. | Strong. Canonical reports and logs remain. | Strong. Canonical reports, logs, and regenerated integrity manifests remain. | Weak. Evidence depends on artifact retention and access. |
| Repository size and commit noise | Weak. All derived copies remain. | Moderate. Option 2 removes eight latest copies. | Strong. Option 3 removes all 40 derived or redundant artifacts from the assessment snapshot. | Strong. Most evidence leaves the repository. |
| Discoverability | Strong. Several navigation views exist. | Strong. The root and workflow indexes remain. | Strong. The root index lists workflow IDs and provides the latest pointer. | Moderate. The index links to external artifacts. |
| Human readability | Strong. Markdown files remain in the repository. | Strong. Option 2 retains per-run Markdown. | Moderate. Operators can render Markdown on demand. | Moderate. Operators retrieve artifacts. |
| Consistency and maintenance | Weak. Several copies must stay synchronized. | Moderate. Workflow indexes still duplicate the root index. | Strong. One report source and one index remain. | Weak. Repository metadata and external artifact state must stay synchronized. |
| Migration and rollback risk | Strong. Operators need no migration. | Moderate. Remove latest copies and update references. | Moderate. The team removes derived files and regenerates integrity manifests. | Weak. Change storage, access, retention, and recovery. |

## Decision Outcome

Chosen option: **Option 3 — Keep canonical JSON, integrity, logs, and one central index.**

This option meets the evidence durability, Ledger compatibility, discoverability, and repository-size decision drivers. It removes generated copies while retaining the report JSON and captured logs required for investigation. The central index already provides the latest pointer and workflow metadata. The existing renderer can provide a human-readable Markdown view without storing another copy.

Option 2 is the strongest conservative changenative. It is less disruptive and preserves direct access to per-run Markdown and workflow indexes, but it leaves most derived artifacts in the repository. It would be preferable only if direct stored Markdown or workflow-specific index paths are a hard operational requirement. Option 4 reduces repository storage further but weakens evidence durability through artifact expiry and access dependencies. Option 1 avoids migration but leaves the duplication problem unchanged.

The decision assumes that no required external consumer relies on removed paths. Before migration, search the repository for references. If the search identifies an external consumer, document the dependency and reassess the migration before removing the affected path.

### Consequences

- **Good:** The repository keeps one structured report source per run, original logs, integrity data, and one repository-wide index. The generator no longer publishes redundant Markdown and latest or workflow-index copies.
- **Neutral:** Operators use the central index and an on-demand render command. Workflow-specific navigation is derived by filtering the central index.
- **Bad:** The migration will break stored Markdown links and per-workflow index/latest paths. The team must update the report guide and repository references.
- **Conditional:** Human-readable reports remain available only while the team supports the renderer and template. The repository has no quantified storage-savings estimate until someone measures bytes.

### Confirmation

- [x] Every retained history folder contains canonical `report.json`, `integrity.json`, and captured logs. The migration preserved report JSON and log content hashes. Each regenerated integrity manifest matches the retained files. Diagnostics run 45858706596 confirmed all 28 manifests. The task copied 12 report folders and read back their JSON, manifest, and log files byte-for-byte.
- [x] The generator no longer writes per-run Markdown, root latest-report copies, or per-workflow indexes/latest copies. The central index remains valid, and its latest pointer selects the correct report after capture, pruning, and backfill. The active index now contains 16 reports, and its latest pointer resolves to the canonical report JSON. Diagnostics run 45858706596 passed the hosted reporter tests.
- [x] The on-demand Markdown renderer produces a readable report from canonical JSON, with regression tests for representative reports and missing or invalid input. Diagnostics run 45858706596 passed the end-to-end renderer tests and the missing or invalid input tests.
- [ ] Search the entire repository for required references to removed paths and migrate any remaining consumers. Check that Ledger and task evidence paths still resolve to unchanged report JSON history paths. The Worker reviewed the report guide, generator, tests, Ledger, diagnostics workflow, Document Type Catalog, and task evidence as targeted consumers. The Worker still needed to complete a repository-wide reference search.
- [x] The migration removes only derived artifacts. The changed-path review confirms that the migration did not change or remove canonical report JSON or captured logs. Git blob comparisons confirm that all 57 pre-migration report JSON and log files were byte-identical. Later task evidence archival copied files exactly and retained the original integrity manifests.
- [x] The relevant naturally triggered hosted validation workflows passed on the implementation commit. Diagnostics runs 45858706596 and 45861355013, Confirm Document Standards runs 45858726101 and 45861354992, and STE Lint Changed run 45859253550 all passed. The Worker did not manually dispatch them.

## Pros and Cons of the Options

### Option 1 — Keep the current layout

- **Good:** No migration. Direct Markdown and workflow-specific navigation remain.
- **Neutral:** Existing generator and index behavior continue.
- **Bad:** Duplicated views, larger publication commits, and multiple synchronization points remain.

### Option 2 — Remove latest copies only

- **Good:** Removes eight latest copies in the assessment snapshot and preserves direct Markdown.
- **Neutral:** The central and workflow indexes remain.
- **Bad:** Per-run Markdown and duplicate workflow indexes remain.

### Option 3 — Canonical JSON and one index

- **Good:** Retains original evidence and integrity while removing all derived copies in the assessment snapshot. Maintains stable JSON paths for the Ledger.
- **Neutral:** Markdown requires an on-demand render. Operators filter workflow views from the central index.
- **Bad:** Existing links to stored Markdown and per-workflow indexes must be updated.

### Option 4 — GitHub workflow artifacts

- **Good:** Minimizes repository storage for reports.
- **Neutral:** Evidence retrieval moves to the Actions interface/API.
- **Bad:** Retention and permissions can make historical evidence unavailable. A second durable store would be needed.

## Implementation Scope

- **In scope:** Maintain `.agent/skills/the-worker/scripts/actions-report.py`, `.agent/skills/the-worker/scripts/ledger.py`, `.agent/skills/asd-ste100/scripts/generate_lint_report.py`, their regression tests, the CI workflows, and one `.takeout/reports/README.md`. Store lint and Actions evidence under `.takeout/reports/history/`. Keep `.takeout/reports/index.json` as the shared index, `.takeout/reports/latest-lint-report.json` as the only latest-report file, and `.takeout/reports/ledger.json` as the sole Ledger. Render Markdown only when requested; do not persist `report.md` or `latest-lint-report.md`.
- **Out of scope:** Changes to error-only retention, cancellation or propagation classification, Ledger finding identity, task generation, and lint baseline rules. Do not move evidence to an external artifact store.
- **Tasks:** 20261126-090154 (cancelled and deleted) implements the artifact-layout portion of this ADR. Its acceptance criteria map to all six Confirmation criteria. The task's separately approved error-only retention and Ledger remediation remains outside this ADR's scope.
- **Dependencies:** Acceptance of this ADR and the existing report generator, canonical Markdown template, central index, and Ledger JSON evidence references.
- **Migration / rollback:** Search all repository references to removed paths and check for external consumers. Update generation and rendering behavior, then migrate derived files only. Compare canonical JSON and log hashes before and after. Regenerate and check integrity manifests and the central index. Check every Ledger/task evidence path. Roll back by regenerating Markdown and derived index/latest views from canonical JSON and the central index. Never restore by rewriting canonical report JSON or logs.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence and rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| An external consumer uses a removed path. | Unknown / High | The repository inventory does not cover external integrations. | Search all repository references. Ask the user about any known external consumer before migration. | External use may remain unknown. |
| The Markdown renderer fails. | Low / Medium | The current generator already has a renderer and template. The assessment did not test an on-demand CLI command. | Keep the template. Add regression tests that render representative reports from JSON and cover missing or invalid input. | A future template change can still break rendering. |
| An integrity manifest no longer matches retained files. | Medium / High | Current manifests include the Markdown file. | Regenerate each manifest for canonical JSON and logs. Confirm every hash after migration. | A faulty migration could still omit a file. |
| A task or Ledger link targets a removed Markdown file. | Low / High | Current Ledger evidence links target report JSON. The assessment did not search all other references. | Search task, Ledger, README, and workflow references before removal. Preserve all JSON history paths. | External links may remain. |
| The root latest pointer becomes stale. | Low / High | The index is rebuilt from retained reports. | Test latest-pointer ordering after capture, pruning, and backfill. | A future index bug could select the wrong report. |
| A migration removes original evidence by mistake. | Low / Critical | The cleanup affects many history folders. | Remove only derived files. Compare report JSON and log hashes before and after. Review changed-path metadata. | A human must still review the changes. |

## More Information
### Evidence Register

| ID | Source and exact locator | Version, date, or commit | Evidence type | Supports | Limitations |
|---|---|---|---|---|---|
| E1 | Repository branch `gpt`, commit `f310d0921a6750caf40e7e314f0a7574bae120af` | 2026-11-26 | Repository fact | Inventory snapshot and source version. | Later task and discussion commits did not change the report layout. |
| E2 | `.takeout/reports/gh_ac_reports/index.json` | Commit `f310d092`, 29 runs | Repository fact | The root index contains the run list and latest-report pointer. | This is a snapshot of the active index. |
| E3 | `.takeout/reports/gh_ac_reports/history/427313089/45798838831-attempt-1-post_run/` | Commit `f310d092` | Repository fact | A history folder contains JSON, Markdown, integrity, and logs. | One folder sample. The report guide defines the same layout for each capture. |
| E4 | `.takeout/reports/gh_ac_reports/` and `.takeout/reports/gh_ac_reports/by_workflow/` directory listings | Commit `f310d092`, three workflow folders | Repository fact | Root latest copies and per-workflow indexes/latest copies. | The review inspected directory names and counts. No one measured the byte total for every file. |
| E5 | `.takeout/reports/gh_ac_reports/README.md`, sections "Evidence layout", "Integrity and history", and "Review order" | Commit `f310d092` | Repository fact | The documented current layout and integrity coverage. | The guide describes current behavior. It does not prove external consumer use. |
| E6 | `.takeout/reports/gh_ac_reports/scripts/report.py` and `.takeout/reports/gh_ac_reports/assets/report-template.md` | Commit `f310d092` | Repository fact | The report generator renders Markdown from structured report data. | The review did not test a new on-demand CLI command. |
| E7 | `.takeout/reports/triage/scripts/ledger.py`, function `finding_row` | Commit `f310d092` | Repository fact | Ledger evidence links target report paths in history, not latest Markdown copies. | Other consumers still require a repository search. |
| E8 | Sample history folder and root latest-copy file sizes | Commit `f310d092` | Repository fact | Sample sizes: report.json 7,058 bytes. report.md 4,167 bytes. integrity.json 386 bytes. root latest JSON 12,937 bytes. root latest Markdown 6,565 bytes. | Samples do not establish total byte savings. |
| E9 | User instruction in this conversation | 2026-11-26 | User instruction | Approval of DRAFT-0004 revision 1, Option 3 and its stated migration scope. | Decision approval does not replace the ADR completeness gate or task execution and hosted-validation requirements. |


- **Source Draft:** DRAFT-0004, revision 1. The team removed the source Draft after the accepted ADR passed its read-back check. The Draft ID and revision remain as provenance.
- **Approved scope:** Option 3 only, as recorded in the metadata and approved by the user on 2026-11-26.
- **Related ADRs:** None.
- **Evidence:** Assessment snapshot at commit `f310d0921a6750caf40e7e314f0a7574bae120af`. `.takeout/reports/gh_ac_reports/index.json`. `.takeout/reports/gh_ac_reports/scripts/report.py`. `.takeout/reports/gh_ac_reports/assets/report-template.md`. `.takeout/reports/gh_ac_reports/README.md`. `.takeout/reports/triage/scripts/ledger.py`. sample history folder and directory inventory recorded in DRAFT-0004 revision 1.
- **Review trigger:** A required external consumer depends on a removed path. The renderer or integrity verification fails. The central index cannot reliably identify the latest report. Evidence-retention requirements change.

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| 2026-11-26 | Accepted | User approved DRAFT-0004 revision 1, Option 3. The complete rationale comparison and provisional ADR read-back passed. |
| 2026-11-26 | Option 3 implementation complete. The team verified five of six confirmation criteria | Reporter migration, central index, on-demand renderer, evidence preservation, and naturally triggered hosted validation passed. The repository-wide reference search remains pending. |


## User-directed amendment — 2026-11-27

The user expanded the accepted Option 3 layout to include both STE lint and GitHub Actions evidence. This amendment supersedes the original exclusion of the separate STE lint report layout and the original family-specific path references.

The canonical report structure is now:

- `.takeout/reports/README.md`
- `.takeout/reports/index.json`
- `.takeout/reports/latest-lint-report.json`
- `.takeout/reports/ledger.json`
- `.takeout/reports/history/`

Both report families write to the shared index and history root. Lint index entries carry their `family`, `scope`, and repository-relative `history_path`. Actions entries carry their `family`, capture stage, source status, workflow identity, and `history_path`. The Ledger reads the shared index once and resolves each family from its history path. Lint updates replace only matching lint entries, so an Actions capture for the same workflow run and attempt remains in the index.

The user also directed that all content inside the report history directory be cleared. The migration therefore retains the 312-finding Ledger and its historical archived evidence references, clears stale run-index entries whose source history was removed, and initializes the single latest lint JSON pointer as an empty baseline until the next lint run. No hosted CI results or local tests were inspected or executed for this amendment.

Implementation: Task `20261127-173000-53`, commits `0cdaf24593e2193a31382dd3aec54283c30c6e5e`, `f1efd131ff3236027d2d23a922ac52fde294ebbb`, `c153f4904df1bcf36e454725911a07d0a6cb2904`, `1499bac37d2f53f57bf747c1af19eb4b8c49e56e`, `6c9fdfe78f7d8560ef72f780a9f54acb5937fbe8`, `47d90bc2f110bd41de8d1c399d4700820ea314fb`, `e2cb50475e2bb1b96740d745b5cf794583b584fe`, and `30fbb5ee5334ec282d378d86c5bd855f80b3c9b8`.


## Supersession — ADR-0008 (2026-11-28)

ADR-0008 supersedes this report-artifact layout decision. The repository will retire the complete `.takeout/reports/` tree only after the replacement coordinator, verifier, status index, publisher, recovery sweep, and review-task flow are operational and every producer and consumer has migrated. Preserve unrelated lint, test, workflow coverage, and baselines. Do not retain this report layout or a parallel findings archive after migration. ADR-0008 is the governing decision for the replacement.
