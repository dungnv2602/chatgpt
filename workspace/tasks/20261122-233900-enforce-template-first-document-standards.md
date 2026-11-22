# Task: Enforce template-first document standards

## Metadata

- **ID:** 20261122-233900
- **Created:** 2026-11-22 23:39 UTC
- **Updated:** 2026-11-22 23:39 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** None
- **Archived:** No

## 1. Original Request

“Do you think every document should have a template? This prevents you from drifting from the standard.”

## 2. Subsequent Instructions

### 2026-11-22

“Approve. Now we want to enforce the standard right? 

How should we proceed from this?”

Approval: The user approved the template-first document policy and authorized implementation.

## 3. Objective

Establish and enforce a repository-wide template-first policy for recurring document types. Prevent structural drift, omitted fields, inconsistent labels, and undocumented formats.

## 4. Requirements

1. Inventory recurring document types in the approved project directories.
2. Identify existing canonical templates, schemas, and examples for each type.
3. Classify each type as template-required, schema-required, lightweight-standard, or exempt.
4. Define one authoritative template or schema for each recurring type that requires one.
5. Specify required, conditional, and optional sections. Define field names, order, formats, allowed values, and missing-value rules.
6. Define a document-creation procedure that requires template retrieval before drafting.
7. Define a completion check that compares each new or revised document with its canonical template.
8. Add automated structural validation where machine-checkable rules provide value. Integrate relevant checks into the existing GitHub Actions workflows without weakening current coverage.
9. Migrate or reconcile existing recurring document types in a controlled order. Preserve historical and creative content.
10. Document explicit exceptions. Do not force rigid templates onto creative prose, one-off notes, or externally controlled formats when a template would reduce clarity or conflict with their governing format.
11. Update indexes and references when canonical templates or schemas change.
12. Read back and verify all changed files. Commit all repository changes to branch `gpt`.

## 5. Decisions

- **Approved:** Adopt a template-first policy for recurring document types.
- A template applies to a document type, not automatically to every individual file.
- Use canonical templates for recurring records and structured schemas for machine-readable data.
- Keep required, conditional, and optional content distinct.
- Do not invent a new structure when an approved template exists.
- When no template exists, identify the gap and define the standard before producing repeated documents.
- Preserve flexibility for creative writing, one-off exploratory notes, and externally governed formats.
- Prefer automated validation for structural rules that can be checked reliably. Do not claim that structure validation proves factual correctness.

## 6. Progress Log

### 2026-11-22 23:36 UTC

- **Action:** Ran the required CI preflight for the current branch head.
- **Result:** The newest changed-document lint run failed on two findings in `skills/the-worker/SKILL.md`. The job log identified the exact lines.
- **References:** Commit `bf6434ddf5432ef2adacc9d3a4cac3e10b1b6670`, run [45084133413](https://github.com/dungnv2602/chatgpt/actions/runs/45084133413).
- **Next:** Repair the findings on branch `gpt`. Do not wait for a new CI run.

### 2026-11-22 23:37 UTC

- **Action:** Repaired the two Worker skill lint findings and committed the change.
- **Result:** Commit `a8c327fc9136c172e5be599aad83461f71de1db7` updated `skills/the-worker/SKILL.md`. A read-back confirmed both corrected passages.
- **References:** `skills/the-worker/SKILL.md`, commit `a8c327fc9136c172e5be599aad83461f71de1db7`.
- **Next:** Create this task record and begin the document-type inventory.

### 2026-11-22 23:39 UTC

- **Action:** Reviewed workspace navigation, the task board, the task template, and the remaining active task record.
- **Result:** No task is marked Current Execution or In Progress on the board. The prior Samantha task record is marked Done and Archived. This task is a separate objective.
- **References:** `workspace/README.md`, `workspace/task_board.md`, `workspace/TASK_TEMPLATE.md`, `workspace/tasks/20261120-183600-continue-samantha-drawing-session.md`.
- **Next:** Create this task as the sole Current Execution task and inspect the repository's existing template inventory.

### 2026-11-22 23:44 UTC

- **Action:** Inspected top-level project indexes and directory inventories in the approved project directories.
- **Result:** Identified existing novel templates, the drawing-attempt template, session and archive record structures, task templates, discussion-register rules, and the image hand-off contract. Several recurring formats use instructions embedded in skills rather than standalone template files.
- **References:** `novels/README.md`, `novels/WORKFLOW.md`, `novels/templates/`, `skills/drawing/assets/attempt-template.md`, `skills/session-archiving/references/archive-records-and-image-prompts.md`, `workspace/TASK_TEMPLATE.md`, `images/takeout/README.md`, `skills/agent-skill-authoring/SKILL.md`.
- **Next:** Complete the inventory and distinguish standalone templates from embedded contracts and data schemas.

### 2026-11-22 23:46 UTC

- **Action:** Added the central Document Standards skill, its initial catalog, and a reusable Agent Skill template. Integrated the on-demand gate into The Worker and indexed the new skill.
- **Result:** Commit `884fbfacd026a17ddcdbc161d20d83206fb7f167` created the policy and catalog. Read-back checks passed for all five changed paths.
- **References:** `skills/document-standards/SKILL.md`, `skills/document-standards/references/document-type-catalog.md`, `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`, `skills/the-worker/SKILL.md`, `skills/README.md`.
- **Next:** Add standalone templates for the recurring session and drawing record types.

### 2026-11-22 23:49 UTC

- **Action:** Added session brief, conversation-integrity, session-summary, and daily drawing-index templates. Updated the owning workflow instructions and catalog.
- **Result:** Commit `c8d26d3417fc9a14a95da888795c29e42e928a50` created four templates and updated four owner or catalog files. All eight paths were fetched again. Their required content and template links were confirmed.
- **References:** `skills/session-archiving/assets/`, `skills/drawing/assets/daily-index-template.md`, `skills/session-archiving/references/archive-records-and-image-prompts.md`, `skills/drawing/SKILL.md`, `skills/agent-skill-authoring/SKILL.md`, `skills/document-standards/references/document-type-catalog.md`.
- **Next:** Inspect the takeout processor and manifest format before designing machine-readable schema validation.

### 2026-11-22 23:48 UTC

- **Action:** Inspected the takeout processor, publication verifier, and regression test index. Compared documented formats with parser, field constants, generator functions, and tests.
- **Result:** The processor validates the hand-off and defines conversion-report and manifest columns. The publisher checks required verification columns and remote assets. Tests cover readiness, exact intake coverage, missing attempt metadata, malformed top-level YAML, duplicate output IDs, rollback, hash behavior, manifest updates, and published links. They do not establish exhaustive field-by-field coverage.
- **References:** `skills/session-archiving/scripts/process_takeout.py`, `skills/session-archiving/scripts/test_process_takeout_unittest.py`, `skills/session-archiving/scripts/verify_published_manifest.py`, `skills/session-archiving/references/image-processing-scripts.md`.
- **Next:** Complete the document-type catalog audit and reconcile existing record types without rewriting historical content.

## 7. Current State

- The user approved the template-first policy.
- The task is the sole Current Execution task.
- The novel workspace has a mature Version 1.1 template set for eight document types. Version 1.0 templates remain historical references.
- Non-novel drawing attempts use the versioned template at `skills/drawing/assets/attempt-template.md`.
- Drawing-session briefs, daily drawing indexes, conversation-integrity records, and session summaries now have standalone Version 1.0 templates.
- Agent Skill definitions have a copy-ready template at `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`.
- Drawing pattern entries have separate successful and failure templates in `skills/drawing/references/patterns/PATTERN-TEMPLATES.md`.
- Workspace task records use the versioned template at `workspace/TASK_TEMPLATE.md`.
- Task boards and the Condensed Mode discussion register remain embedded contracts for single live files.
- Novel documents use the current Version 1.1 template set. Do not mass-migrate untouched Version 1.0 records.
- The image takeout hand-off is validated by `skills/session-archiving/scripts/process_takeout.py`. The same script defines conversion-report and manifest columns. `verify_published_manifest.py` checks published data and links.
- The processor test suite covers important intake and publication paths. It does not yet establish exhaustive field-by-field validation coverage.
- Master image, pose, and prompt catalogues remain classified as lightweight collections. A single shared template may not improve them.
- The catalog covers the main recurring document types identified across `images/`, `master/`, `novels/`, `drawings/`, `skills/`, and `workspace/`. Full file-by-file reconciliation remains incomplete.
- The latest CI failure was repaired. The post-repair CI result has not been checked.

## 8. Remaining Work

- Complete the catalog audit for every recurring document type discovered in the approved project directories.
- Review the master catalogues and decide whether a lightweight shared pattern improves consistency.
- Compare existing recurring records with canonical formats. Record legacy exceptions without rewriting historical records.
- Review whether the processor test suite needs additional field-level validation cases.
- Decide how to integrate structural document checks with CI. Workflow changes require fresh authorization.
- Read back and verify all changed paths and record the final result.

## 9. Next Actions

1. Complete the type-level catalog audit for recurring document types in all approved project directories.
2. Review the master image, pose, and prompt catalogues and assign their final lightweight or exempt classifications.
3. Compare existing recurring records with canonical formats. Record legacy exceptions without rewriting historical records.
4. Decide whether additional processor tests are needed for hand-off and manifest field validation.
5. Request fresh authorization before editing GitHub workflow files.

## 10. References

- `skills/SESSION_START.md`
- `skills/session-archiving/SKILL.md`
- `skills/the-worker/SKILL.md`
- `skills/agent-skill-authoring/SKILL.md`
- `skills/asd-ste100/SKILL.md`
- `skills/asd-ste100/references/repository-writing-policy.md`
- `skills/github-actions/SKILL.md`
- `workspace/README.md`
- `workspace/task_board.md`
- `workspace/TASK_TEMPLATE.md`
- `skills/drawing/assets/attempt-template.md`

## 11. Verification

- **Check:** User approval and scope.
- **Method:** Current conversation.
- **Result:** Approved. The implementation scope covers recurring repository document types and their templates or schemas.
- **Limitations:** No repository-wide inventory or automated validation has been completed.

- **Check:** CI preflight repair.
- **Method:** Retrieved the newest applicable run, inspected its job log, updated the exact affected file, and fetched it again.
- **Result:** The two reported Worker skill findings were corrected and the file read-back matched the update.
- **Limitations:** A new CI result has not been checked.

## 12. Handoff Instructions

Continue this task on branch `gpt`. Do not switch to another branch.

Start with a systematic inventory of recurring document types and existing templates in the approved project directories. Use directory indexes and exact-path reads. Do not scan or inspect `archive/` contents.

Keep the distinction between document types and individual documents. Prefer one canonical template per recurring type, with schemas for structured data. Record exceptions where a rigid template is unsuitable.

Do not make broad migrations until the inventory identifies the affected files and the authoritative standard for each type. Preserve user prompts, historical records, and creative content.

After each important write, fetch the exact path and verify it. Commit completed changes to `gpt`. Never change `main`.
