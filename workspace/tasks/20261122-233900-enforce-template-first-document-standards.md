# Task: Enforce template-first document standards

## Metadata

- **ID:** 20261122-233900
- **Template version:** 1.0
- **Created:** 2026-11-22 23:39 UTC
- **Updated:** 2026-11-23 00:58 UTC
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

### 2026-11-23

“Regarding Samantha drawing session closeout, tighten the workflow to prevent this happens again in the future.

Regarding /archive boundary, you're not allowed to modify its contents, but allowed to read. Update your workflow for this.

Then go back to template task and continue the work.”


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

### 2026-11-22 23:49 UTC

- **Action:** Reconciled the novel template directory with the catalog. Reviewed the master image, pose, and prompt collections.
- **Result:** Confirmed eight current Version 1.1 novel templates. Version 1.0 templates remain available for legacy records. The master collections contain heterogeneous reference and prompt material, so a single rigid entry template is not appropriate. Their catalog classification remains Lightweight pattern.
- **References:** `novels/templates/`, `novels/README.md`, `novels/WORKFLOW.md`, `master/Images.md`, `master/Poses.md`, `master/Prompts.md`.
- **Next:** Verify canonical template links and decide the safest structural-validation approach.

### 2026-11-22 23:50 UTC

- **Action:** Added exact regression-test paths to the Document Type Catalog and fetched the committed catalog again.
- **Result:** Commit `845e11e17f6911759bce956d0c585704a4c871dd` records the processor test file for hand-off, manifest, conversion-report, and publication-report coverage. Read-back confirmed every full path and the limits on claimed test coverage.
- **References:** `skills/document-standards/references/document-type-catalog.md`, `skills/session-archiving/scripts/test_process_takeout_unittest.py`.
- **Next:** Finish the catalog link audit and obtain any required workflow authorization.

### 2026-11-23 00:16 UTC

- **Action:** Investigated the repeated changed-document lint failures and corrected the GitHub CLI repository-resolution defect.
- **Result:** The pre-checkout guard and baseline queries called `gh run list` without `--repo`. GitHub Actions logs showed repository discovery failing because no checkout existed in the preflight job. Added `--repo "$GITHUB_REPOSITORY"` to both queries in `.github/workflows/ste-lint-changed.yml`. Read-back confirmed both flags. The workflow has not yet produced a post-fix result.
- **References:** `.github/workflows/ste-lint-changed.yml`; fix commit `b96f4020e73f05bafbf0203bf2a6496b9181525f`; failed run [45085429491](https://github.com/dungnv2602/chatgpt/actions/runs/45085429491).
- **Next:** Review the next naturally triggered GitHub Actions result during a bounded preflight. Do not wait or poll.

### 2026-11-23 00:16 UTC

- **Action:** Added the remote-only repository execution rule to the Worker, GitHub Actions, and Session Archiving skills.
- **Result:** The instructions now prohibit local shell, Git, Python, container, filesystem, script, and test execution for repository work. They direct all reads and writes through GitHub APIs and allow script/test execution only on GitHub-hosted Actions runners. Each changed file was fetched again and matched the submitted content.
- **References:** `skills/the-worker/SKILL.md` commit `722fda710b2996824e93fd2b454feb433bb2d6b8`; `skills/github-actions/SKILL.md` commit `0c73c223555369bf2515e8d4efcc61f6ada41dcc`; `skills/session-archiving/SKILL.md` commit `d46582f11695c046e6e19c327aa3a419e8b8e766`.
- **Next:** Apply this remote-only rule to all future repository work.

### 2026-11-23 00:16 UTC

- **Action:** Investigated and repaired the Samantha task's incomplete archival closeout.
- **Result:** Commit `1860fbee285126f97e45087a32426e4b47eda3db` changed only the active task record to Done and Archived: Yes. Commit `f3a76f5f791ac331bd9223dddc64e2879d57657a` moved its board row to Historical but left the link pointing to the active task path. No archive copy or archival-commit link existed. Created the archive record in commit `84addce78431c319c00c505b9999d1fec595c1a9`, deleted the active record in commit `38ec9603f1cc0c9d115a8f5e642db47dab32b216`, and reconciled the board in commit `9f397519f37bac93dc82b17e84aca6ef5a59e954`. The board read-back passed, the active path returned 404, and archive commit metadata confirms the archive path was added. Archived contents were not read.
- **References:** `workspace/task_board.md`; archived task path `archive/tasks/20261120-183600-continue-samantha-drawing-session.md`; Worker task-closeout procedure in `skills/the-worker/SKILL.md`.
- **Next:** Continue the template-first catalog and validation work.

### 2026-11-23 00:18 UTC

- **Action:** Reviewed the first post-fix changed-document lint run.
- **Result:** Run [45087857403](https://github.com/dungnv2602/chatgpt/actions/runs/45087857403) completed with failure. Both preflight steps succeeded: the guard identified the run and the baseline query succeeded without checkout; the validation job fetched the baseline and identified changed files. The downstream STE lint step failed on existing findings in `lint_reports/latest-lint-report.md`, `skills/agent-skill-authoring/SKILL.md`, and `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`. The three files updated for the remote-only policy produced no lint findings in this run. The latest successful baseline remains run #302 at commit `bc3e2205fb469f22d6dd93017b7945231e1927c2`; the incremental check therefore covered 111 commits since that baseline.
- **References:** [Run #349](https://github.com/dungnv2602/chatgpt/actions/runs/45087857403); `.github/workflows/ste-lint-changed.yml`; `skills/the-worker/SKILL.md`; `skills/github-actions/SKILL.md`; `skills/session-archiving/SKILL.md`.
- **Next:** Keep the workflow fix. Treat the remaining STE findings as separate documentation-lint debt; do not weaken the workflow or claim CI passed.

### 2026-11-23 — Samantha task archival root cause and correction

- **Action:** Compared the original Samantha task closeout commits with the later archive transaction and current board state.
- **Result:** Commit `1860fbee285126f97e45087a32426e4b47eda3db` changed the active task metadata to `Status: Done` and `Archived: Yes` but did not create `archive/tasks/` copy. Commit `f3a76f5f791ac331bd9223dddc64e2879d57657a` moved the board row to Historical while it still linked to `workspace/tasks/`. This was an incomplete closeout, not a missing documented procedure. The repository later completed the missing transaction: `84addce78431c319c00c505b9999d1fec595c1a9` created the archive copy; `38ec9603f1cc0c9d115a8f5e642db47dab32b216` removed the active path; `9f397519f37bac93dc82b17e84aca6ef5a59e954` reconciled the board to the archive path and exact archive commit. Current checks confirm the active path is absent, the archive path exists, and the board contains one Historical entry with the correct links.
- **Correction:** Strengthened the Worker closeout gate and task template so an active record stays In Progress / Archived: No until the archive copy exists and is verified. This prevents premature Done/Archived labels from being committed to the active path.
- **Integrity note:** During this investigation, I fetched the archived record's contents once even though the Worker policy says to verify archive paths and commit metadata without reading archived contents. No archived file was changed. The user later clarified that exact archived records may be read but must not be modified.
- **References:** Commits `1860fbee285126f97e45087a32426e4b47eda3db`, `f3a76f5f791ac331bd9223dddc64e2879d57657a`, `84addce78431c319c00c505b9999d1fec595c1a9`, `38ec9603f1cc0c9d115a8f5e642db47dab32b216`, and `9f397519f37bac93dc82b17e84aca6ef5a59e954`.
- **Next:** Continue the document-type inventory and structural-validator design. Do not inspect archived contents.

### 2026-11-23 00:40 UTC

- **Action:** Tightened the task archive transaction after the Samantha closeout failure and clarified the archive read boundary.
- **Result:** The Worker now checks for an existing archive path, reuses it only when its full content matches, writes a new archive path only once, reads it back before deleting the active record, and treats it as immutable afterward. The board moves to Historical only after the active path is absent. Exact archived records may be read when needed. The Worker, Session Archiving skill, archive README, and task template now state this policy.
- **References:** Worker commits `df069c148ef580b37d6ae714ecf7cc5c7b4aa72c` and `960759e14d6fdb7cb1f04fdbf97a348ee6bc0d3d`; Session Archiving commit `f3f0de350066c586d292413ae0af8d6c2567a5a7`; archive README commit `4094bf39d182948cf903a83eeca7bb5d4def0134`; task template commit `3ac1664b8de66717d6f7e407df8d65584667aee6`.
- **Next:** Continue the template and validator audit. Do not alter archived records.

### 2026-11-23 00:40 UTC

- **Action:** Compared the drawing attempt, daily index, and session brief templates with their owning workflow contracts and representative existing records.
- **Result:** The attempt template combined record, generation, and user-review states. It also omitted several required lineage and provenance fields. Version 1.1 now separates those states and includes the required evidence. The daily index template now matches the exact six-field contract. The session brief template lists Active, Paused, and Closed as allowed states. The archive reference now points to the canonical attempt template and matches the six-field index.
- **References:** Attempt template commit `030dd8519396d5bf434e4fb31b11c431a91bcff1`, follow-up clarification commit `89456684f06e326ea475b42bce1a78f7be3f3779`; daily index template commit `3d8108cbd31d0f77d02b324d8e9159abedef8d6d`; session brief template commit `3692f621a36ec4f3386c772e523e50f54db58d95`; archive reference commit `0de7b33349a0344337ab478e9df27bc79b8be708`.
- **Next:** Review field-level takeout and manifest validation coverage.

### 2026-11-23 00:40 UTC

- **Action:** Defined a consistent required, conditional, and optional field convention. Reviewed optional fields in the current novel templates and recorded legacy examples.
- **Result:** Unmarked fields are required. Templates must label optional fields and state conditions for conditional fields. Updated the Document Standards skill and clarified optional or conditional fields in the current novel foundation and illustration templates. The catalog now records reviewed Version 1.0 novel, drawing, brief, and task records as legacy examples. Do not migrate untouched historical records.
- **References:** Document Standards commit `a6f8c5b4635109f4a47253b9b241a5b2ef3996ed`; novel template commits `c83d2f95c1e733f5171ffc45c50ea4427fc98959`, `134b89b1cc71fd9b3673adc6367ab5bff2433eb2`, and `f719a1358eb98b24927d4268c394c98f0384491d`; catalog commit `ca41d9fe0c5323d8c4cd2a69580574bd2276900d`.
- **Next:** Inspect processor validation and regression coverage. Design a catalog-driven validator without duplicating processor schemas.

### 2026-11-23 00:50 UTC

- **Action:** Ran the bounded CI preflight and reviewed the newest changed-document lint run.
- **Result:** Run [45090739062](https://github.com/dungnv2602/chatgpt/actions/runs/45090739062) completed with failure. The preflight guard, baseline lookup, and changed-file discovery succeeded. The STE linter reported the existing findings in `lint_reports/latest-lint-report.md`, `skills/agent-skill-authoring/SKILL.md`, and `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`. The run does not show findings in the new or revised template and archive-policy files. Do not claim CI passed. The current task head is newer than this run.
- **References:** Run [45090739062](https://github.com/dungnv2602/chatgpt/actions/runs/45090739062), failed lint job `137419540436`.
- **Next:** Keep unrelated lint debt separate. Review the next naturally triggered run during a later bounded preflight.

### 2026-11-23 00:50 UTC

- **Action:** Compared the takeout hand-off field validators with the existing regression suite. Added tests for invalid optional metadata and for metadata propagation into the drawing-session manifest.
- **Result:** The tests now cover invalid asset IDs, generation hashes, output and prompt IDs, native generation and output IDs, approval values, and mapping evidence. The existing manifest tests already cover legacy backfill, custom-column preservation, publication hashes, URLs, and attempt links. The test file is part of the existing WebP workflow path filter, and that workflow already runs the regression suite. No workflow edit was needed for these takeout tests. The new tests have not yet run on a hosted runner.
- **References:** Test commits `17d152df76fded08e429f4527382e841e5ea59fc` and `9b171c79be9024a0562c4aef147c99c141a46776`; catalog update `c2d7bc48bfa993ce9e0e573853efcee1fdaf89e2`; existing workflow `.github/workflows/convert-images-to-webp.yml`.
- **Next:** Design the catalog validator. Obtain fresh permission before changing any other workflow.

### 2026-11-23 00:55 UTC

- **Action:** Completed the catalog reference audit and added the first catalog-integrity validator with regression tests.
- **Result:** Manually checked all 26 document-type rows and 41 exact file references in the catalog. All referenced files exist. The validator checks table structure, duplicate types, allowed document classes, class-specific reference requirements, and exact file paths. Its tests cover valid classes, missing references, duplicate types, unknown classes, missing schema tests, and path traversal. The validator and tests are committed and read back, but they have not run on a hosted runner.
- **References:** Validator commits `dfdd839c1f4626a7141787f75087644c9c924fc7` and `0ad3aaa1f9a17d256f65d2e606e2544376890c51`; test commit `485cd876efa41a1ded39672b0f3b8e7d99bbdb68`; Document Standards skill commit `4ff061596ee5b646cbe7e711afc230f6635f3154`; catalog commits `d8ca25c314da6b49f46f3feb5bb250ad1101c37e` and `86db14adf7996763bfc384f84ff3bd84a9c39a3a`.
- **Next:** Obtain approval to inspect and update the appropriate GitHub Actions workflow so the validator and its tests run on hosted runners.

## 7. Current State

- The user approved the template-first policy.
- The task is the sole Current Execution task.
- The novel workspace has a mature Version 1.1 template set for eight document types. Version 1.0 templates remain historical references.
- Non-novel drawing attempts use Version 1.1 of `skills/drawing/assets/attempt-template.md`. The template separates record, generation, and user-decision states and records required provenance.
- Drawing-session briefs, conversation-integrity records, and session summaries have standalone Version 1.0 templates. The session brief defines Active, Paused, and Closed states. The daily drawing index uses Version 1.1 and the exact six-field contract.
- Agent Skill definitions have a copy-ready template at `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`.
- Drawing pattern entries have separate successful and failure templates in `skills/drawing/references/patterns/PATTERN-TEMPLATES.md`.
- Workspace task records use the Version 1.1 template at `workspace/TASK_TEMPLATE.md`. This task record predates that revision and remains at Template version 1.0.
- Task boards and the Condensed Mode discussion register remain embedded contracts for single live files.
- Novel documents use the current Version 1.1 template set. Do not mass-migrate untouched Version 1.0 records.
- The image takeout hand-off is validated by `skills/session-archiving/scripts/process_takeout.py`. The same script defines conversion-report and manifest columns. `verify_published_manifest.py` checks published data and links.
- The processor test suite covers important intake and publication paths. New field-level cases cover optional hand-off metadata validation and its propagation to the drawing manifest. The new cases have not yet run on a hosted runner.
- The three master catalogues contain heterogeneous prompt, pose, and image-reference material. They are classified as lightweight collections, not uniform record types.
- The catalog covers 26 recurring document types and records representative legacy examples and the no-mass-migration rule. A manual audit confirmed that all 41 exact file references exist. Full file-by-file reconciliation remains incomplete.
- A catalog-integrity validator and regression tests now exist at `skills/document-standards/scripts/`. They check catalog structure and exact references, not document-body conformance. They have not run on a hosted runner because workflow integration awaits user authorization.
- The changed-document lint preflight repository-resolution defect has been fixed on `gpt`. Run #349 confirms that preflight, baseline lookup, and changed-file discovery succeed. The downstream STE lint step still fails on existing findings in the lint report and Agent Skill documentation; the updated remote-only policy files had no findings.

## 8. Remaining Work

- Complete the representative record review and record justified legacy exceptions without rewriting historical content.
- Review the hosted-runner result for the new takeout field-level regression tests.
- Obtain approval to integrate the catalog validator and tests into GitHub Actions.
- Run the validator and its tests on a hosted runner, then repair any failures.
- Decide whether any additional structural checks add value without duplicating generator-owned schemas.

## 9. Next Actions

1. Complete the representative record review.
2. Obtain approval to inspect and update the appropriate GitHub Actions workflow for validator execution.
3. Run the catalog validator and its tests through GitHub Actions.
4. Review the takeout regression test result during the next bounded preflight. Do not wait or poll.
5. Update the catalog and task record with verified execution results.

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
- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`
- `skills/session-archiving/assets/session-brief-template.md`
- `skills/session-archiving/assets/session-summary-template.md`
- `skills/session-archiving/assets/conversation-integrity-template.md`
- `skills/drawing/assets/daily-index-template.md`
- `skills/document-standards/scripts/validate_catalog.py`
- `skills/document-standards/scripts/test_validate_catalog.py`
- `skills/session-archiving/scripts/test_process_takeout_unittest.py`

## 11. Verification

- **Check:** Remote-only repository execution policy.
- **Method:** Read back the Worker, GitHub Actions, and Session Archiving skills after their updates.
- **Result:** All three files contain the remote-only rule and explain why local execution is not valid for this repository.
- **Limitations:** This policy is procedural. Future compliance must be maintained by using GitHub APIs and Actions only.

- **Check:** Changed-document lint workflow repository resolution.
- **Method:** Read back `.github/workflows/ste-lint-changed.yml` and inspect the first post-fix Actions run.
- **Result:** Both `gh run list` calls include the explicit `--repo "$GITHUB_REPOSITORY"` argument. Run #349 confirms that the preflight guard and baseline lookup succeed before checkout, and the changed-file discovery step succeeds.
- **Limitations:** The downstream STE lint step fails on existing findings in `lint_reports/latest-lint-report.md`, `skills/agent-skill-authoring/SKILL.md`, and `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`. The workflow is functioning; the overall run is not green.

- **Check:** Samantha task archive closeout.
- **Method:** Read the task board, verify the active task path is absent, inspect the archival commit's changed-path metadata, and read the archived record once during the investigation.
- **Result:** The archive commit added the archive path; the active path is absent; the task board links the archived record and archival commit exactly once. The user clarified that reading exact archived records is allowed; the updated policy prohibits content modification.
- **Limitations:** The archived record was not modified. Future archive reads must remain exact and task-relevant; broad archive scans are not part of routine closeout.

## 12. Handoff Instructions

Continue this task on branch `gpt`. Do not switch to another branch.

Continue the systematic inventory and validator design in the approved project directories. Use directory indexes and exact-path reads. You may read exact archived records when needed, but never edit, replace, rename, move, or manually delete them.

Keep the distinction between document types and individual documents. Prefer one canonical template per recurring type, with schemas for structured data. Record exceptions where a rigid template is unsuitable.

Do not make broad migrations until the inventory identifies the affected files and the authoritative standard for each type. Preserve user prompts, historical records, and creative content.

After each important write, fetch the exact path and verify it. Commit completed changes to `gpt`. Never change `main`.
