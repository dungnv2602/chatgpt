# Task: Audit template placement and enforce template-first authoring

## Metadata

- **Template version:** 1.1
- **ID:** 20261123043747
- **Created:** 2026-11-23 04:37 UTC
- **Updated:** 2026-11-23 04:58 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261122-233900
- **Archived:** No

## 1. Original Request

> Scan entire repo to look for inappropriate templates positions, consult your standards to relocate them accordingly. Double check if current workflow enforces templates standard, what we aggred on, to prevent drifts from future. I would expect you follow our agreed workflow, creating or modifying templates before directly work with the file. Update your workflow accordingly if needed.

## 2. Subsequent Instructions

- The repository `dungnv2602/chatgpt`, branch `gpt`, is the sole source of truth. Do not use Library.
- Use remote GitHub operations only.
- Keep `workspace/discussion.md` updated in both Default Mode and Condensed Mode. Only chat verbosity differs.
- Follow Document Standards and Agent Skill Authoring. Create or update canonical templates before editing governed documents.
- Do not modify `.github/workflows/*` without separate explicit authorization.
- The user's request to check and update template-standard enforcement authorized path-filter changes only to `.github/workflows/validate-document-standards.yml`. No other workflow was modified.
- Archived records are immutable after their initial archive write. Do not edit, move, replace, or manually delete them. Do not broadly inspect archive contents unless necessary.

## 3. Objective

Audit the repository's template and schema placement, classify each recurring document format, correct misplaced or duplicate canonical assets where safe, and make template-first authoring an enforceable Worker workflow.

## 4. Requirements

1. Inventory the repository tree and identify all templates, schemas, examples, generators, and recurring document types.
2. Apply `skills/document-standards/SKILL.md`, its catalog, and `skills/agent-skill-authoring/SKILL.md`.
3. Check template placement against ownership and resource-type standards.
4. Relocate templates only when the canonical owner and all references can be updated safely. Preserve content and avoid duplicate sources of truth.
5. Identify recurring document types without canonical templates or schemas.
6. Create or update templates before editing governed documents.
7. Strengthen The Worker so it must retrieve and use the canonical template or embedded contract before document creation or material revision. If missing, create the template and catalog entry first, then author the governed document.
8. Add enforceable validation or CI coverage only within existing authorization. Do not modify workflow files without separate authorization.
9. Update the Document Type Catalog, indexes, and references as required.
10. Read back every changed path. Report exact verification and CI limitations.
11. Do not mass-migrate historical documents or touch immutable archive records.

## 5. Decisions

- Use `gpt` only.
- Treat `archive/` as immutable. The user's explicit full-repository audit request authorized read-only review of the two archived task records. No archived record was modified.
- Prefer canonical ownership by skill: templates and supporting assets live under the owning skill's `assets/`; explanatory standards and inventories live under `references/`; executable generators and validators live under `scripts/`.
- A document type may use a template, schema, embedded contract, generator-owned format, lightweight pattern, or justified exemption. Do not create redundant templates.

## 6. Progress Log

### 2026-11-23 04:37 UTC

- **Action:** Read the current discussion register, Document Standards skill and catalog, The Worker, Session Archiving, Session Start, Agent Skill Authoring, task template, task board, and workspace README. Recorded the audit in the shared discussion register.
- **Result:** The current standards define template-first authoring, but The Worker only says to retrieve and use the canonical format. It does not explicitly require creating a missing template and catalog entry before authoring, and the catalog's existing inventory is marked as representative rather than exhaustive. Session Archiving also restricts broad repository listings, so this user-authorized whole-repository audit needs a scoped exception that preserves archive immutability.
- **References:** `workspace/discussion.md`, `skills/document-standards/SKILL.md`, `skills/document-standards/references/document-type-catalog.md`, `skills/the-worker/SKILL.md`, `skills/session-archiving/SKILL.md`, `skills/agent-skill-authoring/SKILL.md`, `workspace/TASK_TEMPLATE.md`, `workspace/task_board.md`.
- **Next:** Enumerate the repository tree, then build a complete template/schema placement inventory before making any governed document changes.



### 2026-11-23 04:45 UTC

- **Action:** Enumerated the recursive Git tree and reviewed every filename-matched template/schema candidate outside archive contents. Inspected the novel workflow, Prompt Master references, Drawing pattern index, skill asset conventions, Document Type Catalog, validator, tests, and current validation workflow.
- **Result:** The tree contains 483 entries (417 files) and was not truncated. Two copy-ready template resources are misplaced in `references/`: Prompt Master’s template library and Drawing’s pattern-entry templates. Other named templates are in appropriate locations: project-owned novel templates under `novels/templates/`, skill-owned assets under their owning `assets/` folders, and the shared task template under `workspace/`. The catalog currently misclassifies Prompt Master’s template library as a lightweight technical reference. The validator checks catalog rows, paths, class references, and tests, but it does not enforce template placement or content use. The Actions workflow only watches the catalog, validator, tests, and novel templates. It will not trigger for most skill-template changes.
- **References:** Recursive tree for `gpt`; `skills/document-standards/scripts/validate_catalog.py`; `skills/document-standards/scripts/test_validate_catalog.py`; `.github/workflows/validate-document-standards.yml`; `skills/prompt-master/references/templates.md`; `skills/drawing/references/patterns/PATTERN-TEMPLATES.md`; `skills/document-standards/references/document-type-catalog.md`.
- **Next:** Create and verify the two correctly placed canonical assets. Then update all references and catalog classifications. Do not edit governed documents before the target assets exist and pass read-back.



### 2026-11-23 04:55 UTC

- **Action:** Relocated the two misplaced template assets, updated all identified active references and the catalog, strengthened Document Standards and The Worker, added validator placement checks and regression tests, clarified the full-repository audit exception, and expanded the Document Standards Actions path filters.
- **Result:** The Prompt Master template library now lives at `skills/prompt-master/assets/prompt-templates.md`. Drawing pattern-entry templates now live at `skills/drawing/assets/pattern-entry-templates.md`. New blobs match their original source content exactly. The old paths return 404. All active consumers and the catalog use the new paths. Document Standards requires the format and catalog to be committed and read back before target-document edits. The Worker now has a mandatory stop condition. The validator rejects skill templates outside `assets/` and detects named templates in skill `references/` directories. Hosted run [45114001584](https://github.com/dungnv2602/chatgpt/actions/runs/45114001584) passed 16 tests and catalog validation (36 types, 80 exact references). The validation workflow now triggers on all `skills/**` changes and known project/workspace template paths. Its new path-filter commit has not yet been validated by a subsequent hosted run.
- **References:** `skills/prompt-master/assets/prompt-templates.md`, `skills/drawing/assets/pattern-entry-templates.md`, `skills/document-standards/SKILL.md`, `skills/document-standards/references/document-type-catalog.md`, `skills/document-standards/scripts/validate_catalog.py`, `skills/document-standards/scripts/test_validate_catalog.py`, `skills/the-worker/SKILL.md`, `skills/session-archiving/SKILL.md`, `.github/workflows/validate-document-standards.yml`, `skills/prompt-master/SKILL.md`, `skills/drawing/SKILL.md`, `skills/drawing/README.md`, `skills/drawing/references/patterns/README.md`.
- **Next:** Complete final read-back and branch-head verification. Record the separate changed-document lint workflow defect without modifying that workflow. Then archive this task and reconcile the board.



### 2026-11-23 04:57 UTC

- **Action:** Completed the final repository tree scan, content/reference review, and read-back of all changed paths.
- **Result:** The final recursive tree contains 420 files and 488 entries, with no truncation. No named template or schema remains under a skill `references/` directory. The two relocated assets retain the exact original blob contents. All active references resolve to the new asset paths. Every changed skill, standard, catalog, validator, test, workflow, task-board, and discussion path was fetched again. Branch `gpt` HEAD at final verification was `9490c00f31eeee7a674e64ba02be8c983b51fc89`. Hosted run [45114001584](https://github.com/dungnv2602/chatgpt/actions/runs/45114001584) passed 16 validator tests and catalog validation (36 document types, 80 exact references). The later workflow path-filter change has not yet received a verified hosted result. The latest changed-document lint run [45113875454](https://github.com/dungnv2602/chatgpt/actions/runs/45113875454) still has a separate shell defect: the report command receives a literal trailing backslash from `.github/workflows/ste-lint-changed.yml`. The stale `resolved_findings` test assertion was corrected, but hosted confirmation is not yet observed. That workflow was not modified.
- **References:** Final branch head `9490c00f31eeee7a674e64ba02be8c983b51fc89`; catalog validation run `45114001584`; changed lint run `45113875454`; full-document lint run `45111202565`.
- **Next:** Archive this completed task, register the exact path and timestamp in the retention index, remove the active task record, and reconcile the task board. No further template-placement implementation work remains.

## 7. Current State

The task record was created from `workspace/TASK_TEMPLATE.md`. The full repository tree and template/schema candidate inventory were reviewed. Two misplaced skill-owned template files were relocated into their owning `assets/` directories. All active references and catalog entries were updated. Document Standards and The Worker now require the canonical format and its catalog/owner references to be committed and read back before target-document edits. The catalog validator enforces template placement and detects named templates under skill `references/`. The validation workflow now triggers on all skill changes and known project/workspace template locations.

## 8. Remaining Work

- Create and verify the immutable archive copy.
- Register the exact archive path and UTC timestamp in the retention index.
- Remove the active record and reconcile the task board.
- The changed-document lint workflow shell defect and unverified hosted result remain separate open CI issues.

## 9. Next Actions

1. Archive this completed task and reconcile the task board.

## 10. References

- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `skills/the-worker/SKILL.md`
- `skills/agent-skill-authoring/SKILL.md`
- `skills/session-archiving/SKILL.md`
- `workspace/TASK_TEMPLATE.md`
- Related task: `archive/tasks/20261122-233900-enforce-template-first-document-standards.md`

## 11. Verification

- **Check:** Repository template placement, authoring workflow, catalog, validator, and changed paths.
- **Method:** Enumerated the recursive Git tree; inspected all filename-matched template/schema candidates and all skill reference files; read the two archived task records under the explicit audit scope; fetched every changed path; checked the branch head.
- **Result:** Final tree: 420 files and 488 entries, not truncated. No named template or schema remains under a skill `references/` directory. The two relocated asset blobs match their original source blobs exactly. Hosted run [45114001584](https://github.com/dungnv2602/chatgpt/actions/runs/45114001584) passed 16 validator tests and catalog validation (36 document types, 80 exact references). Final branch head at read-back: `9490c00f31eeee7a674e64ba02be8c983b51fc89`.
- **Limitations:** The updated validation-workflow path filters have not yet received a verified hosted run. Changed-document lint run [45113875454](https://github.com/dungnv2602/chatgpt/actions/runs/45113875454) also exposed a separate literal-backslash shell defect in `.github/workflows/ste-lint-changed.yml`. The stale report-test assertion was corrected, but hosted confirmation is not yet observed. That workflow was not modified.

## 12. Handoff Instructions

The task is complete. For every future document creation or material revision, load Document Standards and the catalog, retrieve the canonical template or contract, and verify its owner location. If the format is missing, create and register it first, commit and read it back, and only then edit the target document. Apply this gate in Default Mode and Condensed Mode. Keep `workspace/discussion.md` current in both modes. Do not modify unrelated workflows without separate authorization. Do not claim hosted CI validation unless a run is verified.
