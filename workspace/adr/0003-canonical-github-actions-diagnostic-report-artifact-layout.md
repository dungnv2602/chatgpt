---
record_type: decision-record
template_version: "1.1"
id: "ADR-0003"
status: "accepted"
decision_date: "2026-11-26"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0004"
source_draft_revision: 1
approved_scope: "Option 3 only. Keep report.json, integrity.json, and captured job logs in each existing immutable history folder. Keep the repository-wide index.json as the only index and latest-report pointer. Render Markdown on demand. Remove per-run report.md files, root latest-report copies, and per-workflow indexes and latest copies. Preserve canonical report JSON bytes, captured log bytes, history paths, and Ledger/task evidence references. Regenerate integrity manifests as required so they cover the retained canonical JSON and logs. Do not change error-only retention, cancellation or propagation classification, Ledger finding identity, task generation, lint baseline rules, or the separate STE lint report layout."
related_adrs: []
supersedes: []
superseded_by: null
implementation_status: "not-started"
implementation_tasks: []
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
- The repository-wide index already stores a `latest_report` object with the canonical history path.

The Markdown report is a rendered view of the structured JSON report. The generator has a Markdown renderer and a canonical template. The Ledger links to report JSON paths. It does not require the Markdown copies.

The inventory at commit `f310d0921a6750caf40e7e314f0a7574bae120af` contains 29 retained history folders. The root contains two latest copies. Three workflow folders each contain an index and two latest copies. The inventory therefore contains 40 derived or redundant artifacts:

- 29 per-run Markdown renderings.
- Two root latest-report copies.
- Six per-workflow latest-report copies.
- Three per-workflow indexes.

This count excludes canonical JSON reports, integrity manifests, captured logs, and the repository-wide index. It is a file count, not a measured byte reduction.

A sample history folder contains `report.json` (7,058 bytes), `report.md` (4,167 bytes), and `integrity.json` (386 bytes), plus a logs directory. The root latest copies are 12,937 bytes for JSON and 6,565 bytes for Markdown. These sample sizes show duplicated content. They do not establish the total storage reduction for the full inventory.

The current layout increases commit size and creates several synchronization points. A generated Markdown report can be rendered again from its JSON source. A per-workflow index can be derived from the repository-wide index by filtering on workflow ID. The root index already identifies the latest report.

The user approved DRAFT-0004 revision 1, Option 3, on 2026-11-26. This ADR records that decision. Artifact-layout changes remain prohibited until this ADR reaches accepted status.

## Decision Drivers

- **Evidence durability and integrity — High:** Preserve original structured evidence, captured logs, and verifiable integrity data.
- **Repository size and commit noise — High:** Remove generated copies that can be recreated from canonical evidence.
- **Discoverability — High:** Retain a reliable way to locate the latest report and historical reports by workflow and run.
- **Ledger compatibility — High:** Preserve existing history paths and every report JSON reference used by findings and tasks.
- **Human readability — Medium:** Keep Markdown review available through an on-demand renderer.
- **Consistency and maintenance — High:** Maintain one report source and one repository-wide index.
- **Migration and rollback risk — High:** Do not rewrite or delete canonical evidence. Make derived views reproducible.

## Considered Options

### Option 1 — Keep the current layout

- **Description and operating model:** Keep per-run JSON and Markdown files, integrity manifests, logs, root latest copies, per-workflow indexes, and per-workflow latest copies.
- **Repository and environment fit:** This matches the current generator, report guide, and repository navigation.
- **Good — strengths:** No migration is required. Operators can open Markdown reports directly. Each workflow has a separate index and latest view.
- **Neutral — trade-offs:** The generator must keep several views synchronized. The root index remains the repository-wide source of report metadata.
- **Bad — weaknesses:** The 40 derived or redundant artifacts in the assessment snapshot remain. Markdown reports repeat information from JSON. Latest copies repeat history files. Per-workflow indexes repeat subsets of the root index. These copies can drift or create large commits.
- **Implementation and migration cost:** No implementation cost. Future report captures continue to write the same copies.
- **Dependencies and operational burden:** Retains all current scripts, templates, indexes, and documentation. Operators must understand which copy is canonical.
- **Risks and safeguards:** Copies can become stale. Rebuilding indexes mitigates drift but does not remove duplication.
- **Evidence and confidence:** The inventory at `f310d092` confirms the file types and counts. Confidence is high for that snapshot.
- **Limitations and unknowns:** The full byte cost was not measured. This option does not address repository growth.

### Option 2 — Remove latest copies only

- **Description and operating model:** Keep per-run Markdown and JSON, integrity manifests, logs, the central index, and per-workflow indexes. Remove the root and per-workflow latest-report copies.
- **Repository and environment fit:** This is a small change to the existing layout. It keeps stored Markdown and workflow-specific navigation.
- **Good — strengths:** Removes eight latest-report copies while retaining stored Markdown and workflow navigation.
- **Neutral — trade-offs:** Operators use the central index for the latest report. Workflow indexes remain available.
- **Bad — weaknesses:** The 29 per-run Markdown renderings and three per-workflow indexes remain in the assessment snapshot. The layout still stores several views of the same report data.
- **Implementation and migration cost:** Update latest-copy generation, tests, and the report guide. Remove the existing eight latest copies.
- **Dependencies and operational burden:** The central and workflow indexes remain. The generator still maintains multiple indexes.
- **Risks and safeguards:** Existing references may depend on latest-copy paths. Search references and verify Ledger links before migration.
- **Evidence and confidence:** The root and workflow directory inventory confirms the eight latest copies. Confidence is high for the inspected snapshot.
- **Limitations and unknowns:** This removes some duplication but leaves most derived report artifacts.

### Option 3 — Keep canonical JSON, integrity, logs, and one central index

- **Description and operating model:** Keep `report.json`, `integrity.json`, and captured logs in each existing history folder. Keep the repository-wide `index.json` as the only index and latest-report pointer. Render Markdown from canonical JSON on demand. Remove per-run `report.md` files, root latest-report copies, and per-workflow indexes and latest copies.
- **Repository and environment fit:** The Ledger already links to report JSON paths. The root index already contains workflow IDs and the latest-report path. The report generator already has a Markdown renderer and template.
- **Good — strengths:** Keeps the original structured evidence, logs, and integrity checks. Removes all 40 derived or redundant artifacts in the assessment snapshot. The report JSON remains the source of truth. The root index remains the only index and latest pointer. Workflow-specific views can be filtered from the root index.
- **Neutral — trade-offs:** Operators use the root index to find reports. A Markdown view requires an on-demand render step. The index remains a generated file and must be rebuilt correctly.
- **Bad — weaknesses:** Direct links to stored Markdown reports and per-workflow indexes stop working. The report guide and repository references must change. JSON is less convenient for casual reading.
- **Implementation and migration cost:** Update the writer, integrity manifest generation, index builder, on-demand rendering interface, tests, and report guide. Remove only derived files from existing history folders. Regenerate integrity manifests for the retained JSON and logs. Keep all report JSON and captured log bytes unchanged.
- **Dependencies and operational burden:** The report generator and template remain. The generator must render Markdown on demand and rebuild the central index. It no longer maintains per-workflow copies.
- **Risks and safeguards:** A missing renderer reduces readability; retain and test the renderer. A bad migration could break a task link or remove evidence; preserve paths, compare hashes, and verify every Ledger/task reference. A stale latest pointer is controlled by regression tests for index ordering and pruning.
- **Evidence and confidence:** The root index contains the latest pointer and workflow metadata. Ledger evidence paths target report JSON. The report guide and sample history folder confirm that Markdown is generated alongside JSON. Confidence is high for these repository facts and moderate for migration effort.
- **Limitations and unknowns:** A complete repository reference search and external-consumer inventory were not completed in the assessment. No migration prototype or byte-level total was measured. External consumers remain an unknown.

### Option 4 — Store reports and logs as GitHub workflow artifacts

- **Description and operating model:** Keep a small repository index and upload JSON reports and logs as workflow artifacts.
- **Repository and environment fit:** GitHub Actions supports workflow artifacts. This would reduce the size of commits that publish diagnostic evidence.
- **Good — strengths:** Reduces repository storage. Workflow artifacts provide a direct link from a run to its captured files.
- **Neutral — trade-offs:** Operators retrieve evidence through the Actions interface or API. The index must store artifact identifiers or URLs.
- **Bad — weaknesses:** Evidence availability depends on artifact retention, permissions, and platform access. Expired artifacts can leave the repository without complete diagnostic evidence.
- **Implementation and migration cost:** Update capture and publication workflows, artifact upload/retrieval, index schema, permissions, retention, and recovery procedures. Define a durable evidence-recovery path.
- **Dependencies and operational burden:** Requires artifact permissions, retention settings, and an operational process to retrieve expired or inaccessible evidence.
- **Risks and safeguards:** Evidence may become unavailable after retention expiry or permission changes. A second durable store would be required to meet the current evidence-retention requirement.
- **Evidence and confidence:** GitHub Actions supports workflow artifacts, but no retention prototype or permission model was evaluated.
- **Limitations and unknowns:** Retention periods and access behavior were not tested. This option does not fit the repository's current role as the durable source of diagnostic evidence.

## Comparative Assessment

The matrix summarizes the same six decision drivers for all materially viable options. The detailed assessments above define each option's operating model, costs, dependencies, risks, evidence, and limits.

| Criterion | Option 1: Current layout | Option 2: Remove latest copies | Option 3: Canonical JSON | Option 4: Workflow artifacts |
|---|---|---|---|---|
| Evidence durability and integrity | Strong. All evidence remains in the repository. | Strong. Canonical reports and logs remain. | Strong. Canonical reports, logs, and regenerated integrity manifests remain. | Weak. Evidence depends on artifact retention and access. |
| Repository size and commit noise | Weak. All derived copies remain. | Moderate. Eight latest copies are removed. | Strong. All 40 derived or redundant artifacts in the assessment snapshot are removed. | Strong. Most evidence leaves the repository. |
| Discoverability | Strong. Several navigation views exist. | Strong. The root and workflow indexes remain. | Strong. The root index has workflow IDs and the latest pointer. | Moderate. The index links to external artifacts. |
| Human readability | Strong. Markdown files are stored. | Strong. Per-run Markdown remains. | Moderate. Markdown is rendered on demand. | Moderate. Operators retrieve artifacts. |
| Consistency and maintenance | Weak. Several copies must stay synchronized. | Moderate. Workflow indexes still duplicate the root index. | Strong. One report source and one index remain. | Weak. Repository metadata and external artifact state must stay synchronized. |
| Migration and rollback risk | Strong. No migration is needed. | Moderate. Remove latest copies and update references. | Moderate. Remove derived files and regenerate integrity manifests. | Weak. Change storage, access, retention, and recovery. |

## Decision Outcome

Chosen option: **Option 3 — Keep canonical JSON, integrity, logs, and one central index.**

This option meets the evidence durability, Ledger compatibility, discoverability, and repository-size decision drivers. It removes generated copies while retaining the report JSON and captured logs required for investigation. The central index already provides the latest pointer and workflow metadata. The existing renderer can provide a human-readable Markdown view without storing another copy.

Option 2 is the strongest conservative alternative. It is less disruptive and preserves direct access to per-run Markdown and workflow indexes, but it leaves most derived artifacts in the repository. It would be preferable only if direct stored Markdown or workflow-specific index paths are a hard operational requirement. Option 4 reduces repository storage further but weakens evidence durability through artifact expiry and access dependencies. Option 1 avoids migration but leaves the duplication problem unchanged.

The decision depends on the assumption that no required external consumer relies on removed paths. Search the repository for all references before migration. If an external consumer is identified, document the dependency and reassess the migration before deleting the affected path.

### Consequences

- **Good:** The repository keeps one structured report source per run, original logs, integrity data, and one repository-wide index. The generator no longer publishes redundant Markdown and latest/index copies.
- **Neutral:** Operators use the central index and an on-demand render command. Workflow-specific navigation is derived by filtering the central index.
- **Bad:** Stored Markdown links and per-workflow index/latest paths are removed. The report guide and repository references must change.
- **Conditional:** Human-readable reports remain available only while the renderer and template remain supported. The amount of repository storage saved is not quantified until a byte-level measurement is performed.

### Confirmation

- [ ] Every retained history folder contains canonical `report.json`, `integrity.json`, and captured logs. Their report JSON and log content hashes are unchanged by migration. Each regenerated integrity manifest validates against the retained files.
- [ ] The generator no longer writes per-run Markdown, root latest-report copies, or per-workflow indexes/latest copies. The central index remains valid and its latest pointer selects the correct report after capture, pruning, and backfill.
- [ ] The on-demand Markdown renderer produces a readable report from canonical JSON, with regression tests for representative reports and missing or invalid input.
- [ ] A repository-wide reference search finds no remaining required references to removed paths, or each required consumer is migrated. All Ledger and task evidence paths continue to resolve to unchanged report JSON history paths.
- [ ] The migration removes only derived artifacts. A changed-path review confirms that no canonical report JSON or captured log was modified or deleted.
- [ ] The relevant naturally triggered hosted validation workflows pass on the implementation commit. Do not use manual dispatch or polling as a substitute for event-driven validation.

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
- **Neutral:** Markdown requires an on-demand render. Workflow views are filtered from the central index.
- **Bad:** Existing links to stored Markdown and per-workflow indexes must be updated.

### Option 4 — GitHub workflow artifacts

- **Good:** Minimizes repository storage for reports.
- **Neutral:** Evidence retrieval moves to the Actions interface/API.
- **Bad:** Retention and permissions can make historical evidence unavailable. A second durable store would be needed.

## Implementation Scope

- **In scope:** Update `.takeout/reports/gh_ac_reports/scripts/report.py`, its regression tests, and the report guide. Keep `.takeout/reports/gh_ac_reports/index.json` as the only index. Update the writer and on-demand renderer. Migrate history folders by deleting only derived Markdown files and remove root latest copies and per-workflow indexes/latest copies. Keep canonical JSON, history paths, and captured log bytes stable. Regenerate integrity manifests so they cover the retained JSON and logs.
- **Out of scope:** Changes to error-only retention, cancellation or propagation classification, Ledger finding identity, task generation, lint baseline rules, report JSON content, captured log content, and the separate STE lint report layout. Do not move evidence to an external artifact store.
- **Tasks:** No implementation task is linked while this ADR is promotion-pending. After acceptance, link the approved artifact-layout work to an implementation task and map the applicable Confirmation criteria to its acceptance criteria.
- **Dependencies:** Acceptance of this ADR; the existing report generator, canonical Markdown template, central index, and Ledger JSON evidence references.
- **Migration / rollback:** Search all repository references to removed paths and check for external consumers. Update generation and rendering behavior, then migrate derived files only. Compare canonical JSON and log hashes before and after. Regenerate and verify integrity manifests and the central index. Verify every Ledger/task evidence path. Roll back by regenerating Markdown and derived index/latest views from canonical JSON and the central index. Never restore by rewriting canonical report JSON or logs.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence and rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| An external consumer uses a removed path. | Unknown / High | The repository inventory does not cover external integrations. | Search all repository references. Ask the user about any known external consumer before migration. | External use may remain unknown. |
| The Markdown renderer fails. | Low / Medium | The current generator already has a renderer and template, but no on-demand CLI command was tested. | Keep the template. Add regression tests that render representative reports from JSON and cover missing or invalid input. | A future template change can still break rendering. |
| An integrity manifest no longer matches retained files. | Medium / High | Current manifests include the Markdown file. | Regenerate each manifest for canonical JSON and logs. Verify every hash after migration. | A faulty migration could still omit a file. |
| A task or Ledger link points to a removed Markdown file. | Low / High | Current Ledger evidence links target report JSON. Other references were not fully searched in the assessment. | Search task, Ledger, README, and workflow references before deletion. Preserve all JSON history paths. | External links may remain. |
| The root latest pointer becomes stale. | Low / High | The index is rebuilt from retained reports. | Test latest-pointer ordering after capture, pruning, and backfill. | A future index bug could select the wrong report. |
| A migration deletes original evidence by mistake. | Low / Critical | The cleanup touches many history folders. | Delete only derived files. Compare report JSON and log hashes before and after. Review changed-path metadata. | Human review remains necessary. |

## More Information
### Evidence Register

| ID | Source and exact locator | Version, date, or commit | Evidence type | Supports | Limitations |
|---|---|---|---|---|---|
| E1 | Repository branch `gpt`, commit `f310d0921a6750caf40e7e314f0a7574bae120af` | 2026-11-26 | Repository fact | Inventory snapshot and source version. | Later task and discussion commits did not change the report layout. |
| E2 | `.takeout/reports/gh_ac_reports/index.json` | Commit `f310d092`, 29 runs | Repository fact | The root index contains the run list and latest-report pointer. | This is a snapshot of the active index. |
| E3 | `.takeout/reports/gh_ac_reports/history/427313089/45798838831-attempt-1-post_run/` | Commit `f310d092` | Repository fact | A history folder contains JSON, Markdown, integrity, and logs. | One folder sample. The report guide defines the same layout for each capture. |
| E4 | `.takeout/reports/gh_ac_reports/` and `.takeout/reports/gh_ac_reports/by_workflow/` directory listings | Commit `f310d092`, three workflow folders | Repository fact | Root latest copies and per-workflow indexes/latest copies. | Directory names and counts were inspected. No byte total was measured for every file. |
| E5 | `.takeout/reports/gh_ac_reports/README.md`, sections "Evidence layout", "Integrity and history", and "Review order" | Commit `f310d092` | Repository fact | The documented current layout and integrity coverage. | The guide describes current behavior. It does not prove external consumer use. |
| E6 | `.takeout/reports/gh_ac_reports/scripts/report.py` and `.takeout/reports/gh_ac_reports/assets/report-template.md` | Commit `f310d092` | Repository fact | The report generator can render Markdown from structured report data. | No new on-demand CLI command was tested. |
| E7 | `.takeout/reports/triage/scripts/ledger.py`, function `finding_row` | Commit `f310d092` | Repository fact | Ledger evidence links target report paths in history, not latest Markdown copies. | Other consumers still require a repository search. |
| E8 | Sample history folder and root latest-copy file sizes | Commit `f310d092` | Repository fact | Sample sizes: report.json 7,058 bytes; report.md 4,167 bytes; integrity.json 386 bytes; root latest JSON 12,937 bytes; root latest Markdown 6,565 bytes. | Samples do not establish total byte savings. |
| E9 | User instruction in this conversation | 2026-11-26 | User instruction | Approval of DRAFT-0004 revision 1, Option 3 and its stated migration scope. | Decision approval does not replace the ADR completeness gate or task execution and hosted-validation requirements. |


- **Source Draft:** DRAFT-0004, revision 1. The source file is deleted after verified promotion. The Draft ID and revision remain as provenance.
- **Approved scope:** Option 3 only, as recorded in the metadata and approved by the user on 2026-11-26.
- **Related ADRs:** None.
- **Evidence:** Assessment snapshot at commit `f310d0921a6750caf40e7e314f0a7574bae120af`; `.takeout/reports/gh_ac_reports/index.json`; `.takeout/reports/gh_ac_reports/scripts/report.py`; `.takeout/reports/gh_ac_reports/assets/report-template.md`; `.takeout/reports/gh_ac_reports/README.md`; `.takeout/reports/triage/scripts/ledger.py`; sample history folder and directory inventory recorded in DRAFT-0004 revision 1.
- **Review trigger:** A required external consumer depends on a removed path; renderer or integrity verification fails; central-index latest-pointer behavior becomes unreliable; or evidence-retention requirements change.

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| 2026-11-26 | Accepted | User approved DRAFT-0004 revision 1, Option 3. The complete rationale comparison and provisional ADR read-back passed. |
