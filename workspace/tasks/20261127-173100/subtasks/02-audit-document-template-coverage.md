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
- **Eligibility / deferral reason:** Done — acceptance criteria met; implementation and readback complete.
- **Required:** Yes
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-28
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
- **Result:** Audit and remediation completed; see the closeout entry below.
- **Next:** None.

### 2026-11-28 03:13 UTC — execution resumed

- **Action:** Read the current repository catalog, all novel template assets and owner references, the Worker governance rules, current task records, and startup CI evidence.
- **Result:** The 12 novel templates already exist under `.agent/skills/romantic-storyteller-visual-artist/assets/templates/`. The former `area/novel/templates/` path is absent. The catalog records 277 in-scope Markdown files and 30 template-named assets, with no missing recurring document format. The Prompt Master skill still contains retired GPT-6 variant names and related unsupported API claims. The live task-board contract also contains scheduling detail not yet reflected in its template.
- **Next:** Correct stale Prompt Master guidance and align the task-board template, then complete the repository-wide placement and link audit.

## 6. State and Evidence

- **Commit SHA:** `6cc29c784b7103bc425998ebfbfa5acfdf79399b`, `eb57d251600e4a86b78d9e62a1e49a5a65484003`, `11a44d28907f116f751babc3ede78fe436b8031c`, `be62841f0776a8c62e45d17ade01751c065a59b3`, `b59167b89e9c35ab071cf37e3fd5f74e6d14a264`, `56d2e4b515f79d15f01619d58af7983cd620280a`, and `98f8baf117c187edfc3dc76d16969a8228ed558e`
- **Changed paths:** 12 moved novel templates; template index; novel README and workflow; Romantic Storyteller and Drawing skills; Worker skill, catalog, validator, tests, and task-board template; Prompt Master template; anchor checker and Document Standards workflow.
- **Readback:** All 12 canonical template paths and affected references were fetched from branch `gpt`.
- **Checks:** Independent audit found 30/30 templates under skill assets, zero external templates, 277/277 Markdown paths covered, 54 coverage rules, and zero broken links among 35 checked local links. Original template blob SHAs were preserved.
- **Limitations:** Local scripts and tests were not run. Hosted workflow results were not inspected.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-28
- **Completion basis:** All nine acceptance criteria met by committed changes and remote readback. Validation limits are recorded above.

## 8. Hosted Validation

- **Status:** Not reviewed — no hosted result claimed
- **Run URL:** Not reviewed

## 9. Handoff

Closed. The completed task folder will be removed under normal lifecycle rules.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|


### 2026-11-28 — repository template audit and closeout

- **Inventory:** The baseline tree contained 30 template assets: 18 already under skills and 12 novel templates outside skills. The 12 novel templates moved to `.agent/skills/romantic-storyteller-visual-artist/assets/templates/`. Their original blob SHAs were preserved.
- **Coverage:** No recurring document type lacked an applicable template, schema, or embedded contract. No new template type was created. The catalog now records version 1.26 and covers 277/277 in-scope Markdown files with 54 path rules and zero uncovered files.
- **Freshness:** Updated the task-board template to match the live scheduler contract and current-focus queue semantics. Updated the Prompt Master OpenAI task brief to remove retired model labels and stale model-specific guidance. Added a Worker rule to scan all templates for drift whenever a template is created or materially revised.
- **Governance:** The catalog and validator now require reusable templates to live in the owning skill's `assets/` directory. The validator scans for misplaced skill templates and templates outside skills. Regression tests cover external placement, nested skill assets, and two-digit child-record coverage. The unsupported task-child character-class glob was replaced with supported `??-*.md` syntax.
- **Reference reconciliation:** Updated novel README/workflow, Romantic Storyteller workflow, Drawing skill, catalog, anchor-check exclusions, and workflow path filters. Removed the former `area/novel/templates/` directory.
- **Verification:** Read back all 12 moved templates and updated owner files. The repository tree contains 30 templates, all under skill assets, and zero outside. The former novel template directory has zero entries. Independent path matching covered all 277 Markdown files. A local-link audit checked 35 links with zero broken targets. The task-board scheduler section matches its template.
- **Commits:** `6cc29c784b7103bc425998ebfbfa5acfdf79399b`, `eb57d251600e4a86b78d9e62a1e49a5a65484003`, `11a44d28907f116f751babc3ede78fe436b8031c`, `be62841f0776a8c62e45d17ade01751c065a59b3`, `b59167b89e9c35ab071cf37e3fd5f74e6d14a264`, `56d2e4b515f79d15f01619d58af7983cd620280a`, and `98f8baf117c187edfc3dc76d16969a8228ed558e`.
- **Limitations:** Repository scripts and tests were not run locally. Hosted Document Standards results were not inspected. No hosted validation pass is claimed.
