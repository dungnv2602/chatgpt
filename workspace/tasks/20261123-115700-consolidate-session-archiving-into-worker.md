# Task: Consolidate Session Archiving into The Worker

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-115700
- **Created:** 2026-11-23 11:57 UTC
- **Updated:** 2026-11-23 11:57 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261123-112100 — Consolidate foundational collaboration skills into The Worker
- **Archived:** No

## 1. Original Request

Consolidate conversation-mode into the-worker.

Since we had the-worker, I'm seeing duplications of roles in the-worker and session-archiving. I mean, the-worker can handle what session-archiving does. We've been using the-worker and /workspace as our working session. You should consolidate session-archiving into the-worker and then delete it. 

Regarding document-standards, explain why we shouldn't consolidate it into the-worker. We always working with documents. Isn't it foundational enough?

## 2. Subsequent Instructions

- **2026-11-23 11:57 UTC:** Treat the request as a full ownership transfer. Preserve Session Archiving's templates, references, and processing scripts under The Worker. Update dependent paths and activation rules. Remove the standalone Session Archiving and Conversation Mode skill entry points.

## 3. Objective

Make The Worker the sole owner of collaboration modes, task/session continuity, conversation and drawing-session archives, image provenance, WebP delivery, and image takeout processing. Remove the standalone `session-archiving` and `conversation-mode` skill directories without losing their operational content or assets.

## 4. Requirements

1. Preserve Conversation Mode's complete rules in The Worker and remove its standalone compatibility skill.
2. Move all Session Archiving templates, references, and scripts into The Worker.
3. Integrate Session Archiving's operational responsibilities into The Worker without duplicating its existing task archival and discussion-register rules.
4. Update workflow script paths, image documentation, Drawing dependencies, session-start procedures, the Document Type Catalog, and skill indexes.
5. Remove the standalone `skills/session-archiving/` and `skills/conversation-mode/` directories after all required content and references are migrated.
6. Preserve the explicit `start session` initialization cue and keep The Worker as the only foundational owner of these responsibilities.
7. Keep Document Standards separate from The Worker. Explain its architectural role and recommend whether its activation status should change.
8. Use branch `gpt` only. Preserve existing user-approved scope and workspace boundaries.
9. Read back every changed path. Do not run local scripts or tests. Do not wait for CI.

## 5. Decisions

- The Worker absorbs the complete Session Archiving capability, not only its entry-point instructions.
- Existing task archival remains owned by The Worker. Do not create a second task-archival procedure.
- Conversation Mode remains a mandatory component of The Worker, but no separate skill path remains.
- Document Standards remains a separate policy/validator package because it owns document-type classification, canonical templates, catalog integrity, and structural validation. The Worker invokes it as a governed authoring dependency.
- Document Standards is a candidate for foundational activation because its gate applies to repository document creation and material revision. Its large catalog and validator details should remain separately maintained rather than being copied into The Worker.

## 6. Progress Log

### 2026-11-23 11:57 UTC

- **Action:** Reviewed the existing Worker, Conversation Mode, Session Archiving, Document Standards, session-start procedure, skill index, workspace board, discussion register, archive policy, and prior foundational-skill consolidation record.
- **Result:** Conversation Mode already exists in The Worker as a mandatory reference, while its standalone skill is only a compatibility pointer. The Worker already owns task archival and workspace continuity. Session Archiving still owns conversation/drawing records, image provenance, WebP procedures, takeout scripts, and their supporting templates. The prior task's on-demand classification is superseded by this request.
- **References:** `skills/the-worker/SKILL.md`, `skills/the-worker/references/conversation-mode.md`, `skills/session-archiving/SKILL.md`, `skills/conversation-mode/SKILL.md`, `skills/document-standards/SKILL.md`, `skills/document-standards/references/document-type-catalog.md`, `skills/SESSION_START.md`, `skills/README.md`, `workspace/README.md`, `workspace/task_board.md`, `workspace/discussion.md`, `archive/README.md`, `archive/tasks/20261123-112100-consolidate-foundational-skills-into-worker.md`.
- **Next:** Transfer supporting assets and procedures into The Worker, then update all dependent references and remove the two standalone skill directories.

### 2026-11-23 11:58 UTC

- **Action:** Copied all three canonical templates, all four operational references, and all three image-processing scripts from Session Archiving into The Worker.
- **Result:** All ten destination files were retrieved from branch `gpt`. Their blob IDs match the original source blob IDs, confirming exact copies. The original files remain until dependent paths are updated.
- **References:** `skills/the-worker/assets/`, `skills/the-worker/references/`, and `skills/the-worker/scripts/`.
- **Next:** Integrate archive/media ownership into The Worker and update workflow, Drawing, session-start, image README, and catalog references.

### 2026-11-23 12:00 UTC

- **Action:** Integrated archive/media ownership into The Worker. Updated its purpose and procedures, moved image-processing script ownership, and redirected the workflow, Drawing skill, session-start procedure, image README, Document Type Catalog, and skill index to Worker-owned paths.
- **Result:** The Worker now owns the complete archive/media domain. The workflow calls the moved scripts under `skills/the-worker/scripts/`. Session-start retains the explicit `start session` cue and loads archive/media references only for relevant specialist work. The Document Type Catalog now points to Worker-owned templates and processors. An obsolete compatibility heading was removed.
- **References:** `skills/the-worker/SKILL.md`, `skills/the-worker/references/`, `skills/the-worker/assets/`, `skills/the-worker/scripts/`, `.github/workflows/convert-images-to-webp.yml`, `skills/drawing/SKILL.md`, `skills/SESSION_START.md`, `skills/README.md`, `skills/document-standards/references/document-type-catalog.md`, and `images/README.md`.
- **Next:** Check all migrated destinations and dependent references. Then delete the two absorbed standalone skill directories and read back the final paths.

## 7. Current State

The task is approved and in progress. All ten supporting files have been copied and read back under The Worker. Owner instructions, activation paths, workflow script paths, Drawing dependencies, image documentation, the Document Type Catalog, and skill indexes have been updated. Original standalone skill files remain until final stale-reference checks and deletion.

## 8. Remaining Work

- Move the Session Archiving assets, references, and scripts.
- Update The Worker and all dependent activation, workflow, image, Drawing, and catalog paths.
- Delete the two absorbed skill directories.
- Read back every changed path and reconcile task closeout.

## 9. Next Actions

1. Transfer Session Archiving supporting files into The Worker.
2. Update owner instructions and all exact dependent paths.
3. Delete the absorbed skill files and verify no stale references remain.
4. Archive this task and reconcile the task board.

## 10. References

- `skills/the-worker/`
- `skills/session-archiving/`
- `skills/conversation-mode/`
- `skills/SESSION_START.md`
- `skills/README.md`
- `skills/document-standards/references/document-type-catalog.md`
- `skills/drawing/SKILL.md`
- `images/README.md`
- `.github/workflows/convert-images-to-webp.yml`

## 11. Verification

- **Check:** Required content transfer, owner and dependency references, workflow paths, deletion of absorbed skill directories, and branch read-back.
- **Method:** Fetch every source file, create its Worker-owned destination, update exact references, delete source files only after destination verification, and retrieve all changed paths from branch `gpt`.
- **Result:** Not performed.
- **Limitations:** No local script execution or CI run is authorized or required by this task.

## 12. Handoff Instructions

Continue the approved migration on branch `gpt`. Preserve all Session Archiving content under The Worker. Do not alter Document Standards' implementation in this task. Keep the explicit session-start cue. Do not report completion until all migrated paths and cross-references pass remote read-back.
