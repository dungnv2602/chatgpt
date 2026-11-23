# Task: Audit template placement and enforce template-first authoring

## Metadata

- **Template version:** 1.1
- **ID:** 20261123043747
- **Created:** 2026-11-23 04:37 UTC
- **Updated:** 2026-11-23 04:37 UTC
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
- Treat `archive/` as immutable. The audit may inventory top-level structure, but will not read archived record contents unless a specific dependency requires it.
- Prefer canonical ownership by skill: templates and supporting assets live under the owning skill's `assets/`; explanatory standards and inventories live under `references/`; executable generators and validators live under `scripts/`.
- A document type may use a template, schema, embedded contract, generator-owned format, lightweight pattern, or justified exemption. Do not create redundant templates.

## 6. Progress Log

### 2026-11-23 04:37 UTC

- **Action:** Read the current discussion register, Document Standards skill and catalog, The Worker, Session Archiving, Session Start, Agent Skill Authoring, task template, task board, and workspace README. Recorded the audit in the shared discussion register.
- **Result:** The current standards define template-first authoring, but The Worker only says to retrieve and use the canonical format. It does not explicitly require creating a missing template and catalog entry before authoring, and the catalog's existing inventory is marked as representative rather than exhaustive. Session Archiving also restricts broad repository listings, so this user-authorized whole-repository audit needs a scoped exception that preserves archive immutability.
- **References:** `workspace/discussion.md`, `skills/document-standards/SKILL.md`, `skills/document-standards/references/document-type-catalog.md`, `skills/the-worker/SKILL.md`, `skills/session-archiving/SKILL.md`, `skills/agent-skill-authoring/SKILL.md`, `workspace/TASK_TEMPLATE.md`, `workspace/task_board.md`.
- **Next:** Enumerate the repository tree, then build a complete template/schema placement inventory before making any governed document changes.

## 7. Current State

The task record was created from `workspace/TASK_TEMPLATE.md`. Initial standards review is complete. Full repository inventory and enforcement changes are pending.

## 8. Remaining Work

- Enumerate and classify the repository tree.
- Inspect template/schema asset placement and all references.
- Identify missing or duplicate canonical formats.
- Update templates and catalog before editing governed documents.
- Strengthen Worker and any non-workflow validators that can enforce template-first authoring.
- Verify all changes and reconcile the task board.

## 9. Next Actions

1. Fetch the recursive Git tree for branch `gpt`.
2. Inventory candidate templates, schemas, generators, examples, and repeated document types outside immutable archive content.
3. Compare every candidate with the standards and catalog.
4. Prepare the canonical template changes before changing governed documents.

## 10. References

- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `skills/the-worker/SKILL.md`
- `skills/agent-skill-authoring/SKILL.md`
- `skills/session-archiving/SKILL.md`
- `workspace/TASK_TEMPLATE.md`
- Related task: `archive/tasks/20261122-233900-enforce-template-first-document-standards.md`

## 11. Verification

- **Check:** Task-record format.
- **Method:** Copied the canonical task template and populated its required fields.
- **Result:** Created using Template version 1.1. Read-back and board registration pending.
- **Limitations:** This is an initial record. It does not yet establish audit completeness.

## 12. Handoff Instructions

Continue on branch `gpt`. Keep `workspace/discussion.md` current before each meaningful step. Complete the repository inventory before relocating or creating templates. Do not edit governed documents until their canonical templates or contracts are in place. Do not modify `.github/workflows/*` without separate explicit authorization. Do not inspect or modify archived record contents. Record exact paths, read back every write, and do not claim hosted CI validation unless a run is verified.
