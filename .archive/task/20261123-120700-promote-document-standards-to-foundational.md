# Task: Promote Document Standards to Foundational Status

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-120700
- **Created:** 2026-11-23 12:07 UTC
- **Updated:** 2026-11-23 12:09 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Approved
- **Current execution:** No
- **Dependencies:** None
- **Related tasks:** 20261123-115700 — Consolidate Session Archiving into The Worker
- **Archived:** Yes

## 1. Original Request

Promote Document Standards to foundational status while keeping it as an independent skill. Leave the archived Session Archiving consolidation record unchanged.

## 2. Subsequent Instructions

- **2026-11-23 12:07 UTC:** User approved all proposed changes. Do not edit, annotate, or otherwise change the archived Session Archiving consolidation record.

## 3. Objective

Make Document Standards a foundational skill loaded during explicit session initialization, while preserving its independent ownership of document governance, catalog, templates, and validation.

## 4. Requirements

1. Add Document Standards to the foundational loading sequence in `skills/SESSION_START.md`.
2. Update `skills/INITIALIZATION_POLICY.md` and `skills/README.md` to match.
3. Change Document Standards metadata to foundational.
4. Update The Worker so it treats Document Standards as a foundational dependency while continuing to load the catalog and specific templates only when needed.
5. Correct stale Session Archiving references in initialization policy.
6. Remove the discussion-register question about the archived task correction. Do not change the archived task record.
7. Read back every changed path. Do not run local scripts or CI.

## 5. Decisions

- Document Standards is foundational because its template-first gate applies to repository document creation and material revision across project workflows.
- Keep Document Standards independent from The Worker. The Worker owns execution and task continuity; Document Standards owns document classification, canonical formats, catalog integrity, and structural validation.
- Load `document-standards/SKILL.md` during explicit foundational initialization. Load its catalog entries, templates, schemas, and validator details only when the task requires them.
- Leave the archived Session Archiving consolidation record unchanged, including its historical metadata.

## 6. Progress Log

### 2026-11-23 12:07 UTC

- **Action:** Reviewed the current session-start procedure, initialization policy, skills index, Document Standards metadata and operating rules, and The Worker's template-first gate.
- **Result:** Document Standards is currently classified as on-demand in all three activation documents and marked `task-specific` in its metadata. The Worker already mandates Document Standards for repository document creation and material revision. The initialization policy also contains a stale Session Archiving skill path.
- **References:** `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md`, `skills/README.md`, `skills/document-standards/SKILL.md`, `skills/the-worker/SKILL.md`, `workspace/discussion.md`.
- **Next:** Update activation hierarchy and metadata, correct the stale dependency path, and remove the correction question from the discussion register without modifying the archived record.

### 2026-11-23 12:09 UTC

- **Action:** Promoted Document Standards to foundational loading. Updated the explicit session-start sequence, foundational dependency hierarchy, initialization policy, skills index, Document Standards metadata, and The Worker's dependency statement. Removed the archived-record correction question from the open discussion register.
- **Result:** All seven affected paths were retrieved after writing. Document Standards is listed as foundational in session-start, initialization policy, and the skills index; its metadata is `project-role: foundational`. The Worker identifies it as an independent foundational dependency. The catalog and specific templates/schemas/validator details remain task-triggered. The stale active Session Archiving path is absent from the initialization policy. The archived Session Archiving task record was not modified.
- **References:** `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md`, `skills/README.md`, `skills/document-standards/SKILL.md`, `skills/the-worker/SKILL.md`, `workspace/discussion.md`, `workspace/task_board.md`.
- **Next:** Archive this task record and reconcile the task board.

## 7. Current State

The approved promotion is implemented and read back. Document Standards is foundational and remains an independent skill. Its catalog and specific canonical assets remain task-triggered.

## 8. Remaining Work

- None. All approved changes are implemented and read back.

## 9. Next Actions

- None. The task is complete and archived.

## 10. References

- `skills/SESSION_START.md`
- `skills/INITIALIZATION_POLICY.md`
- `skills/README.md`
- `skills/document-standards/SKILL.md`
- `skills/the-worker/SKILL.md`
- `workspace/discussion.md`

## 11. Verification

- **Check:** Foundational loading, classification, dependency hierarchy, stale-path removal, and preservation of archived record.
- **Method:** Retrieve every changed file from branch `gpt` after update and inspect exact content. Confirm archived record is unchanged.
- **Result:** Passed. All seven changed paths were retrieved after writing. Foundational classification and loading rules are consistent. The archived Session Archiving task record was not modified.
- **Limitations:** No local scripts, tests, or CI runs were performed. This change updates activation policy; it does not execute the next session's initialization sequence.

## 12. Handoff Instructions

Implement the approved promotion on branch `gpt`. Keep Document Standards independent from The Worker. Do not modify the archived Session Archiving consolidation record. Do not report completion until every changed path is read back.


**Archive timestamp:** `2026-11-23T12:09:00Z`.
