# Subtask: Audit document template coverage and create missing templates

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173100-02
- **Parent Task ID:** 20261127-173100
- **Type:** Audit / Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User-authorized subtask under Template Fix, expanded by the user's 2026-11-28 instruction to audit stale templates and relocate templates outside skills into appropriate skill locations.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — selected under the user's current authorized focus.
- **Required:** Yes
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-28 03:39 UTC
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

- **Action:** Created child record.
- **Result:** Audit and remediation pending.
- **Next:** Begin the full coverage, freshness, and placement audit after task-board-template child as ordered by parent.

### 2026-11-28 03:39 UTC — task recovered and resumed

- **Action:** Recovered the active child record from the last known in-progress commit after the current branch deleted it. Reconciled the remaining acceptance criteria against the current files.
- **Result:** The 12 novel templates are already skill-owned and the project-local directory is absent. The catalog records a 277-Markdown / 30-template audit baseline but inaccurately claims stale assets were updated. Prompt Master still contains retired GPT-6 variant names and unsupported API claims; Template N lacks explicit scope and approval boundaries; the task-board template duplicates Worker scheduling rules; and CI still runs the older validator rather than the placement-aware validator.
- **Next:** Fix those stale assets and owner references, integrate and correct the placement-aware validator, then verify the full canonical path map.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Pending
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** Repository-wide audit not yet performed.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

Complete the template freshness corrections, integrate the placement-aware validator into the hosted document-standards workflow, reconcile catalog and inbound references, and verify all template assets are under their owning skills. Then close the parent and child under the normal lifecycle.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
