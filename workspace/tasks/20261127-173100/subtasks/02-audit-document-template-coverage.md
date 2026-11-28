# Subtask: Audit document template coverage and create missing templates

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173100-02
- **Parent Task ID:** 20261127-173100
- **Type:** Audit / Implementation
- **Status:** Done
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User-authorized subtask under Template Fix, expanded by the user's 2026-11-28 instruction to audit stale templates and relocate templates outside skills into appropriate skill locations.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Completed — all acceptance criteria satisfied; ready for parent closeout.
- **Required:** Yes
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-28 03:45 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Scan repo if any document still haven't have its template, then create its template.

## 2. Subsequent Instructions

> When templates are created, scan the repository to update stale templates compared to the current workflow/repository. Then relocate all templates outside of skills into skills at appropriate places, respecting the skill standard.

## 3. Objective and Scope

Systematically scan the entire repository for document types or documents that lack an applicable canonical template, schema, or embedded contract. In the same audit, inventory all existing templates and compare them with the current workflow, repository structure, governance contracts, and skill standards. Identify genuine coverage gaps and stale content, update stale templates, create appropriate missing templates, and relocate every template outside skill directories into the appropriate owning skill. Maintain a clear mapping from each template to its skill/document owner and reconcile all references and catalogs.

## 4. Acceptance Criteria

1. Define and execute a scoped, reproducible repository-wide scan for template coverage, freshness, and placement.
2. Inventory document types and all existing templates, recording their locations, owners, applicable contracts/standards, freshness findings, and coverage gaps with evidence.
3. Read existing canonical templates, relevant governance contracts, and the current skill standard before modifying, creating, or relocating templates.
4. Compare existing templates against current workflow and repository reality; update every confirmed stale template and its affected references.
5. Relocate every template found outside skill directories into the appropriate owning skill location. Preserve required content/history as appropriate, follow the skill standard, and avoid arbitrary dumping of unrelated templates into a generic skill.
6. Create templates only for confirmed gaps; avoid redundant templates where schemas or embedded contracts already govern.
7. Update catalogs, coverage records, owner metadata, indexes, links, and other inbound references for created, updated, and relocated templates.
8. Remove obsolete duplicate/original copies only after all references have been reconciled and the canonical destination has been verified.
9. Commit and remotely read back results. Verify paths, references, and applicable skill-standard requirements; make no validation beyond observed evidence claims.

## 5. Decisions and Progress

- **Action:** Completed the repository-wide template coverage, freshness, and placement audit; corrected stale assets and owner guidance; integrated the placement-aware validator into the hosted document-standards workflow; reconciled catalog and inbound references.
- **Result:** Verified all 30 canonical template assets under owning skills. The 12 novel templates are under the Romantic Storyteller skill's `assets/templates/`; the former project-local directory and workspace-root task templates are absent. The recorded scan baseline covers 277 Markdown documents and 30 template assets and reports no missing recurring document family, so no redundant template was created.
- **Next:** Close the parent and remove completed task records under the normal lifecycle.

### 2026-11-28 03:39 UTC — task recovered and resumed

- **Action:** Recovered the active child record from the last known in-progress commit after the current branch deleted it. Reconciled the remaining acceptance criteria against the current files.
- **Result:** The 12 novel templates are already skill-owned and the project-local directory is absent. The catalog records a 277-Markdown / 30-template audit baseline but inaccurately claims stale assets were updated. Prompt Master still contains retired GPT-6 variant names and unsupported API claims; Template N lacks explicit scope and approval boundaries; the task-board template duplicates Worker scheduling rules; and CI still runs the older validator rather than the placement-aware validator.
- **Next:** Fix those stale assets and owner references, integrate and correct the placement-aware validator, then verify the full canonical path map.

- **Action:** Created child record.
- **Result:** Audit and remediation pending.
- **Next:** Begin the full coverage, freshness, and placement audit after task-board-template child as ordered by parent.

## 6. State and Evidence

- **Final commit:** `a4d42b9f8bde7ff1ff4a52fe7b510bd6627e0433`
- **Supporting commits:** `babd4863ea5517b94f5f3a2e93326fca34ac3da6` (Task Board template); `695cdd4174986c99633caa6f5c3a3d5e9d6ad8f7` (OpenAI task brief); `501bc09bbc646a54c8c422de23a4c5a60efb8298` (placement validator); `81cbb0d1220fa0165dfa8d06b67b97fda71ca84d` (regression tests); `9d9ac2e31187aa07076d081f436bcdb5f55fd51a` (workflow); `8eb9d12a5c151111ad424520d7b20b1b1737286a` (catalog).
- **Changed paths:** Task Board template and live board; Prompt Master Template N, SKILL.md, and README.md; document catalog validator and regression tests; document-standards workflow; catalog; workspace README; legacy validator and test removal.
- **Readback:** All changed files were fetched after commit. All 30 canonical template asset paths were verified. The old `area/novel/templates/` and workspace-root template paths are absent. Novel README, workflow, drawing skill, and Romantic Storyteller references point to the skill-owned assets.
- **Checks:** The recorded repository scan baseline covers 277 Markdown documents and 30 template assets, with no missing recurring document family. Regression cases now cover external template files/directories, misplaced skill assets, task-record exclusions, and historical archive exclusions. The hosted workflow is configured to run the new suite and validator.
- **Limitations:** No local scripts or tests were run. No hosted CI results were inspected; no pass claim is made.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-28 03:45 UTC
- **Completion basis:** All acceptance criteria satisfied by repository readback. No new template type was needed; two stale templates and their owner guidance were updated; all 30 canonical template assets are skill-owned; placement and coverage validation is wired into the hosted workflow.

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed. The workflow is configured; hosted results were not inspected.

## 9. Handoff

No further work remains in this child. The parent is ready for closeout. Completed task records will be removed under the Worker lifecycle rules.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
