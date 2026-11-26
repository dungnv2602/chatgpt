---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0004"
revision: 1
status: "in-review"
created: "2026-11-26"
updated: "2026-11-26"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs: []
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# Canonical GitHub Actions Diagnostic Report Artifact Layout

## Proposal Summary

Choose one canonical storage layout for retained GitHub Actions error reports. Keep `report.json`, `integrity.json`, and captured job logs in each immutable history folder. Keep one repository-wide `index.json` with the latest-report pointer.

Render Markdown on demand. Remove committed per-run Markdown renderings, root latest-report copies, and per-workflow indexes and latest copies. This proposal changes artifact storage only. It does not change the approved error-only retention policy or Ledger task eligibility.

## Context and Problem Statement

The current report layout stores several views of the same report.

- Each retained history folder contains `report.json`, `report.md`, `integrity.json`, and captured logs.
- The repository root contains `index.json`, `latest-gh-ac-report.json`, and `latest-gh-ac-report.md`.
- Each workflow folder under `by_workflow/` contains an index and two latest-report copies.
- The repository-wide index already stores a `latest_report` object with the canonical history path.

The Markdown report is a rendered view of the structured JSON report. The report generator has a Markdown renderer and a canonical template. The Ledger links to report JSON paths. It does not require the Markdown copies.

The current inventory at commit `f310d0921a6750caf40e7e314f0a7574bae120af` contains 29 retained history folders. The README describes four files or groups in each folder. The root contains two latest copies. Three workflow folders each contain an index and two latest copies.

This produces 40 derived or redundant artifacts:

- 29 per-run Markdown renderings.
- Two root latest-report copies.
- Six per-workflow latest-report copies.
- Three per-workflow indexes.

The count does not include canonical JSON reports, integrity manifests, captured logs, or the repository-wide index. It is an artifact count, not a measured byte reduction.

The current layout increases commit size and creates multiple places that must stay in sync. A generated Markdown report can be rendered again from its JSON source. A per-workflow index can be derived from the repository-wide index by filtering on workflow ID. The root index already identifies the latest report.

The user approved a smaller report layout in the conversation on 2026-11-26. This Draft records the exact proposal and migration boundary. No artifact-layout changes are authorized until the user approves this revision and the resulting ADR reaches accepted status.

## Goals and Non-Goals

### Goals

- Preserve every genuine retained error report and its original JSON evidence.
- Preserve every captured job log.
- Preserve integrity checks for the canonical JSON report and logs.
- Keep one repository-wide index with a latest-report pointer.
- Remove generated copies that can be recreated from canonical evidence.
- Keep existing history paths stable so Ledger and task references remain valid.
- Provide an on-demand Markdown rendering path.
- Reduce generated file count and report publication noise.

### Non-Goals

- Do not change which source runs qualify as error reports.
- Do not change the handling of cancellation-only or propagation-only runs.
- Do not change Ledger finding identity, task generation, or baseline rules.
- Do not move diagnostic evidence to an external service.
- Do not delete canonical JSON reports, integrity manifests, or captured logs.
- Do not rewrite source-run metadata or historical error findings.
- Do not change the separate STE lint report layout.

## Decision Drivers

| Criterion | Why it matters | Relative importance |
|---|---|---|
| Evidence durability and integrity | The repository must retain enough evidence to investigate and audit each error. | High. Loss of original logs or JSON is unacceptable. |
| Repository size and commit noise | Generated duplicate files increase commit size and make report updates harder to review. | High. This is the user's stated concern. |
| Discoverability | Operators must find the latest report and locate older reports by workflow and run. | High. |
| Compatibility with Ledger references | Task records and findings must keep valid links to immutable evidence. | High. |
| Human readability | Operators need a practical way to review a report without parsing JSON manually. | Medium. An on-demand renderer can meet this need. |
| Consistency and maintenance | The generator should have one source of truth for each report and its index. | High. |
| Migration and rollback risk | The change must not delete original evidence or break existing task references. | High. |

## Assessment Basis and Evidence Limits

- **Scope of comparison:** Four options. They range from the current layout to a canonical JSON layout and external artifact storage.
- **Assessment method:** Qualitative comparison of repository structure, generator behavior, index contents, evidence paths, and existing task references.
- **Evidence boundary:** The inventory was read from branch `gpt` at commit `f310d0921a6750caf40e7e314f0a7574bae120af`. It covered all three active workflow history directories, the three `by_workflow` directories, the repository root, the report index, the report guide, and one sample history folder.
- **Key assumptions:** The repository remains the durable source of truth for diagnostic evidence. The on-demand renderer remains available in the report generator.
- **Unresolved evidence gaps:** No byte-level total was measured for all 40 derived artifacts. No external consumer inventory was run outside this repository. The migration must search the repository for references to files that this proposal removes.

The current report index contains 29 runs. The history directories contain 26 reports for workflow ID `427313089`, two for workflow ID `424743410`, and one for workflow ID `424715662`. The root index contains a `latest_report` pointer.

A sample history folder contains `report.json` (7,058 bytes), `report.md` (4,167 bytes), and `integrity.json` (386 bytes), plus a logs directory. The root latest copies are 12,937 bytes for JSON and 6,565 bytes for Markdown. These sample sizes demonstrate duplication. They do not establish the total size reduction for the full inventory.

## Considered Options

### Option 1 — Keep the current layout

- **Description and operating model:** Keep per-run JSON and Markdown files, integrity manifests, logs, root latest copies, per-workflow indexes, and per-workflow latest copies.
- **Repository and environment fit:** This matches the current generator, report guide, and repository navigation.
- **Good — strengths:** No migration is required. Operators can open Markdown reports directly. Each workflow has a separate index and latest view.
- **Neutral — trade-offs:** The generator must keep several views synchronized. The root index remains the repository-wide source of report metadata.
- **Bad — weaknesses:** The layout stores 40 derived or redundant artifacts in the current inventory. Markdown reports repeat information from JSON. Latest copies repeat history files. Per-workflow indexes repeat subsets of the root index. These copies can drift or create large commits.
- **Implementation and migration cost:** No implementation cost. Future report captures continue to write the same copies.
- **Dependencies and operational burden:** Retains all current scripts, templates, indexes, and documentation. Operators must understand which copy is canonical.
- **Risks and safeguards:** Duplicate files can become stale. The current index rebuild reduces this risk but does not remove the duplicated storage.
- **Evidence and confidence:** Repository inspection confirms the current files and counts. Confidence is high for the artifact count and current layout.
- **Limitations and unknowns:** The full byte cost was not measured. This option does not address the user's repository-size concern.

### Option 2 — Remove latest copies only

- **Description and operating model:** Keep per-run Markdown reports, JSON reports, integrity manifests, logs, the root index, and per-workflow indexes. Remove the root and per-workflow latest-report copies. Use the index paths to locate the newest report.
- **Repository and environment fit:** This is a small change to the existing layout. It keeps the current human-readable per-run reports and workflow-specific indexes.
- **Good — strengths:** Removes eight latest-report copies. It reduces some commit noise without changing the per-run report format. The root index remains the main index.
- **Neutral — trade-offs:** Operators must open the index to find the latest report. Workflow-specific navigation remains available.
- **Bad — weaknesses:** The 29 per-run Markdown renderings remain. The three per-workflow indexes remain derived copies of the root index. The layout still has multiple views of the same report data.
- **Implementation and migration cost:** Moderate. Update latest-copy generation, tests, and the report guide. Delete the existing eight latest copies.
- **Dependencies and operational burden:** The root index and per-workflow indexes remain. The generator still maintains multiple index files.
- **Risks and safeguards:** Existing documentation or scripts may expect latest-copy paths. Search for these references before migration. Keep the root index pointer and verify all task links.
- **Evidence and confidence:** The root and workflow directories contain the eight latest copies. Confidence is high.
- **Limitations and unknowns:** This option reduces duplication but does not remove the largest repeated report view, the per-run Markdown file.

### Option 3 — Keep canonical JSON, integrity, logs, and one central index

- **Description and operating model:** Keep `report.json`, `integrity.json`, and captured logs in each immutable history folder. Keep the repository-wide `index.json` as the only index and latest-report pointer. Render Markdown from the canonical JSON report when an operator requests it. Remove per-run `report.md` files, root latest copies, and all per-workflow indexes and latest copies.
- **Repository and environment fit:** The Ledger already links to report JSON paths. The root index already contains workflow IDs and the latest-report path. The report generator already has a Markdown renderer and template.
- **Good — strengths:** Keeps the original structured evidence, logs, and integrity checks. Removes all 40 derived or redundant artifacts from the current inventory. The report JSON remains the source of truth. The root index remains the only index and latest pointer. Workflow-specific views can be filtered from the root index.
- **Neutral — trade-offs:** Operators use the root index to find reports. A Markdown view requires an on-demand render step. The index remains a generated file and must be rebuilt correctly.
- **Bad — weaknesses:** Direct links to stored Markdown reports and per-workflow indexes will stop working. The report guide and any repository references must change. JSON is less convenient for casual reading.
- **Implementation and migration cost:** Moderate. Update the writer, integrity manifest, index builder, CLI or rendering interface, tests, and report guide. Remove derived files from existing history folders. Rebuild integrity manifests for the retained JSON and logs. Keep all report JSON and logs unchanged.
- **Dependencies and operational burden:** The report generator and template remain. The generator must render Markdown on demand and rebuild the central index. It no longer maintains per-workflow copies.
- **Risks and safeguards:** A missing renderer would reduce readability. Keep the renderer and test its output. A bad migration could remove a task link. Preserve all history paths and report JSON files. Verify every Ledger evidence path after migration.
- **Evidence and confidence:** The root index contains the latest pointer and workflow IDs. The Ledger links to JSON paths. The report README and sample history folder confirm that Markdown is generated alongside JSON. Confidence is high for the current repository structure and moderate for migration effort.
- **Limitations and unknowns:** The repository has not yet been searched for every consumer of the latest-copy paths. No migration test or byte-level size measurement has been run.

### Option 4 — Store logs and reports as GitHub workflow artifacts

- **Description and operating model:** Keep a small report index in the repository and upload JSON reports and logs as GitHub workflow artifacts. Operators download artifacts to inspect full evidence.
- **Repository and environment fit:** GitHub Actions supports workflow artifacts. This would reduce the size of commits that publish diagnostic evidence.
- **Good — strengths:** The repository would store less report data. Workflow artifacts provide a direct link from a run to its captured files.
- **Neutral — trade-offs:** Operators would use the Actions interface or an API to retrieve evidence. The repository index would need to store artifact identifiers and URLs.
- **Bad — weaknesses:** Artifact retention is separate from repository history. Evidence can expire under artifact retention rules. Access depends on GitHub permissions and artifact availability. The repository would no longer contain the complete diagnostic evidence.
- **Implementation and migration cost:** High. Update capture and publication workflows, artifact upload and retrieval, index schema, access handling, and tests. Define a retention policy and recovery path.
- **Dependencies and operational burden:** Requires artifact permissions, retention settings, and an operational process to retrieve expired or inaccessible evidence.
- **Risks and safeguards:** Evidence may become unavailable after retention expiry or permission changes. A second durable store would be required to meet the current audit requirement.
- **Evidence and confidence:** This assessment uses the repository's current evidence-retention requirement and the existing GitHub Actions workflow model. No artifact-retention prototype was tested.
- **Limitations and unknowns:** No artifact retention period or permission model was evaluated. This option does not fit the repository's current role as the durable source of report evidence.

## Comparative Assessment

| Criterion | Option 1: Current layout | Option 2: Remove latest copies | Option 3: Canonical JSON | Option 4: Workflow artifacts |
|---|---|---|---|---|
| Evidence durability and integrity | Strong. All evidence remains in the repository. | Strong. Canonical reports and logs remain. | Strong. Canonical reports, logs, and integrity remain. | Weak. Evidence depends on artifact retention and access. |
| Repository size and commit noise | Weak. All derived copies remain. | Moderate. Eight latest copies are removed. | Strong. All 40 derived or redundant artifacts are removed. | Strong. Most evidence leaves the repository. |
| Discoverability | Strong. Several navigation views exist. | Strong. The root and workflow indexes remain. | Strong. The root index has workflow IDs and latest pointer. | Moderate. The index links to external artifacts. |
| Human readability | Strong. Markdown files are stored. | Strong. Per-run Markdown remains. | Moderate. Markdown is rendered on demand. | Moderate. Operators must retrieve artifacts. |
| Consistency and maintenance | Weak. Several copies must stay synchronized. | Moderate. Workflow indexes still duplicate the root index. | Strong. One report source and one index remain. | Weak. Repository metadata and external artifact state must stay synchronized. |
| Migration and rollback risk | Strong. No migration is needed. | Moderate. Remove latest copies and update references. | Moderate. Remove derived files and rebuild integrity manifests. | Weak. Change storage, access, retention, and recovery. |

### Overall comparison

Option 1 has the lowest migration risk. It does not reduce repository growth or duplication.

Option 2 is the strongest conservative alternative. It removes eight latest copies and keeps the current navigation model. It leaves 29 per-run Markdown renderings and three per-workflow indexes.

Option 3 keeps the original evidence and integrity checks. It removes all 40 derived or redundant artifacts. The root index already provides the required latest pointer and workflow metadata. The report renderer can provide Markdown when needed. This option best meets the user's repository-size and single-source-of-truth requirements.

Option 4 reduces repository size further. It does not meet the current requirement to keep diagnostic evidence in the repository. Artifact expiry and access rules add operational risk.

## Proposed Recommendation

Recommend Option 3.

Keep one canonical `report.json`, one `integrity.json`, and the captured logs in each immutable history folder. Keep the repository-wide `index.json` as the only index and latest-report pointer. Render Markdown from JSON on demand.

This option preserves the evidence that tasks and the Ledger need. It removes the derived files that make report commits large. It also reduces the number of generated indexes and latest copies that must stay synchronized.

Option 2 is the strongest alternative. It is less disruptive, but it leaves most derived artifacts in the repository. Choose Option 2 instead if direct access to stored Markdown reports or per-workflow indexes is a hard operational requirement.

The recommendation depends on one assumption: no required consumer outside the inspected repository depends on the removed file paths. Search the repository for all such references before implementation. If an external consumer exists, document it and reassess the migration.

## Consequences and Trade-Offs

- **Positive:** The repository stores one structured report source and the original logs. The central index provides the latest pointer. The report commit contains fewer generated files.
- **Negative:** Operators cannot open a stored Markdown report directly. They must use the on-demand renderer.
- **Neutral:** The repository-wide index remains. Its size depends on the number of retained reports.
- **Conditional:** A Markdown view remains available if the renderer and template stay supported.
- **Conditional:** Workflow-specific navigation remains available if consumers filter the central index by workflow ID.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| An external consumer uses a removed path. | Unknown / High | The repository inventory does not cover external integrations. | Search all repository references. Ask the user about any external consumer before migration. | External use may remain unknown. |
| The Markdown renderer fails. | Low / Medium | The current generator already has a renderer and template. | Keep the template. Add a regression test that renders a representative report from JSON. | A future template change can still break rendering. |
| The integrity manifest no longer matches the stored files. | Medium / High | Current manifests include the Markdown file. | Rebuild each manifest for JSON and logs. Verify every hash after migration. | A faulty migration could still omit a file. |
| A task or Ledger link points to a removed Markdown file. | Low / High | The current Ledger links to report JSON paths. Other references have not been fully searched. | Search all task, Ledger, README, and workflow references before deleting files. | External links may remain. |
| The root latest pointer becomes stale. | Low / High | The index is rebuilt from retained reports. | Test latest-pointer ordering after pruning and backfill. | A future index bug could select the wrong report. |
| A migration commit deletes original evidence by mistake. | Low / Critical | The cleanup touches many history folders. | Limit deletion to derived files. Compare report JSON and log hashes before and after migration. | Human review remains necessary. |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Report generator | Write canonical JSON and integrity data. Do not write stored Markdown or latest copies. Render Markdown on demand. | `.takeout/reports/gh_ac_reports/scripts/report.py` | Accepted ADR from DRAFT-0004 |
| Reporter tests | Verify canonical files, integrity hashes, rendering, and index pointers. | `.takeout/reports/gh_ac_reports/scripts/test_report.py` | Accepted ADR from DRAFT-0004 |
| Report guide | Document the canonical layout and on-demand rendering path. | `.takeout/reports/gh_ac_reports/README.md` | Accepted ADR from DRAFT-0004 |
| Historical report data | Remove per-run Markdown files, root latest copies, and per-workflow indexes and latest copies. Keep JSON, integrity, and logs. | `.takeout/reports/gh_ac_reports/history/`, `.takeout/reports/gh_ac_reports/by_workflow/`, `.takeout/reports/gh_ac_reports/latest-gh-ac-report.*` | Accepted ADR from DRAFT-0004 |
| Central index | Keep one repository-wide index and its latest-report pointer. | `.takeout/reports/gh_ac_reports/index.json` | Accepted ADR from DRAFT-0004 |
| Ledger and tasks | Preserve report JSON evidence paths. Do not change finding or task identity under this Draft. | `.takeout/reports/triage/ledger.json`, `workspace/tasks/` | No change proposed |
| Document standards | Update the catalog only if the report layout contract changes. | `.agent/skills/document-standards/references/document-type-catalog.md` | Accepted ADR from DRAFT-0004 |

## Proposed Implementation Outline

1. Obtain user approval for this exact Draft revision.
2. Promote the Draft to an ADR and complete the required read-back before implementation.
3. Search the repository for all references to `report.md`, `latest-gh-ac-report.*`, and `by_workflow/`.
4. Update the generator to write only `report.json`, `integrity.json`, and logs in each history folder.
5. Keep `index.json` as the only index and latest-report pointer.
6. Add an on-demand Markdown renderer that reads the canonical JSON report and the existing template.
7. Update integrity generation to hash the JSON report and every captured log.
8. Add regression tests for rendering, report hashes, index ordering, backfill, and Ledger evidence links.
9. Migrate existing history folders. Delete only derived Markdown and index/latest copies. Do not change report JSON or captured logs.
10. Rebuild the central index and verify every Ledger and task evidence path.
11. Compare report JSON and log hashes before and after migration. Verify all integrity manifests.
12. Allow the normal hosted workflows to validate the changes. Do not dispatch or poll CI.

Rollback must restore the removed derived files from the canonical JSON reports and index. The original report JSON and logs must remain unchanged.

## Questions for the User

1. Approve Option 3 and its migration scope: keep per-run JSON, integrity, and logs. Keep the root index as the only latest pointer. Render Markdown on demand. Remove the 40 derived or redundant artifacts.

## Review and Approval

- **Revision presented:** 1
- **User decision:** Pending
- **Approved scope:** Not approved
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-26 | 1 | Initial proposal for a canonical JSON, integrity, logs, and central-index layout. | Pending |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | Repository branch `gpt`, commit `f310d0921a6750caf40e7e314f0a7574bae120af` | 2026-11-26 | Repository fact | Inventory snapshot and source version. | Later task and discussion commits do not change the report layout. |
| E2 | `.takeout/reports/gh_ac_reports/index.json` | Commit `f310d092`, 29 runs | Repository fact | The root index contains the run list and latest-report pointer. | This is a snapshot of the active index. |
| E3 | `.takeout/reports/gh_ac_reports/history/427313089/45798838831-attempt-1-post_run/` | Commit `f310d092` | Repository fact | A history folder contains JSON, Markdown, integrity, and logs. | One folder sample. The README defines the same layout for each capture. |
| E4 | `.takeout/reports/gh_ac_reports/` and `.takeout/reports/gh_ac_reports/by_workflow/` directory listings | Commit `f310d092`, three workflow folders | Repository fact | Root latest copies and per-workflow indexes/latest copies. | Directory names and counts were inspected. No byte total was measured for every file. |
| E5 | `.takeout/reports/gh_ac_reports/README.md`, sections "Evidence layout", "Integrity and history", and "Review order" | Commit `f310d092` | Repository fact | The documented current layout and integrity coverage. | The guide describes current behavior. It does not prove external consumer use. |
| E6 | `.takeout/reports/gh_ac_reports/scripts/report.py` and `.takeout/reports/gh_ac_reports/assets/report-template.md` | Commit `f310d092` | Repository fact | The report generator can render Markdown from structured report data. | No new on-demand CLI command was tested. |
| E7 | `.takeout/reports/triage/scripts/ledger.py`, function `finding_row` | Commit `f310d092` | Repository fact | Ledger evidence links target report paths in history, not the latest Markdown copies. | Other consumers still require a repository search. |
| E8 | Sample history folder file sizes and root latest-copy file sizes | Commit `f310d092` | Repository fact | Demonstrates that the latest files duplicate report content. | Samples do not establish total byte savings. |
| E9 | User approval in the current conversation | 2026-11-26 | User instruction | Confirms approval to prepare and execute the report cleanup recommendation. | This Draft still requires approval of its exact revision under repository governance. |

<!--
Draft lifecycle:
- Allowed statuses: draft, in-review, changes-requested, approved-for-adr, rejected, withdrawn, superseded.
- Do not use promoted as a Draft status.
- On successful promotion, delete this source file after the accepted ADR passes the completeness and read-back checks.
- If deletion fails after acceptance, keep this file temporarily. Set resulting_adr, promotion_cleanup_pending, and cleanup_reason. Add it to Promotion Cleanup Pending, not Current Drafts.
- Do not create an `.archive/draft/` folder or a Promoted Drafts index.
-->
