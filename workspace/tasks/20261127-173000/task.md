# Task: Refactor Skills

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173000
- **Created:** 2026-11-27 17:30 UTC
- **Updated:** 2026-11-27 15:20 UTC
- **Priority:** P0
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to create the Refactor Skills task and place workspace/tasks/20261127-102301 beneath it.
- **Governing ADR(s):** None
- **Current execution:** Yes
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready; approved, no dependencies. Selected as current execution by user's explicit priority instruction.
- **Related tasks:** None

## 1. Original Request

> Create a task named "refactor skills" and put workspace/tasks/20261127-102301 as subtask into it.

## 2. Subsequent Instructions

### 2026-11-27 18:27 UTC

> workspace/tasks/20261127-173000/task.md Make this task P0, we focus on this task from now on.

- **Action:** Set parent priority to P0 and select it as Current Execution.
- **Approval:** Explicit authorization to prioritize and focus execution on this task.

## 3. Objective and Acceptance Criteria

Serve as the persistent, open parent task and coordination point for skills refactoring in the repository, including the current consolidation work and future refactoring initiatives. This is an explicitly authorized standing parent for skills-refactoring work; it is not a finite deliverable and must not be retired or closed merely because its current children are complete.

1. Keep this parent task open as the enduring skills-refactoring workstream.
2. Capture each distinct current or future skills-refactoring deliverable as its own subtask under this parent, after confirming it genuinely concerns refactoring the repository's skills.
3. Preserve original prompts, approvals, dependencies, progress, evidence, and history in each child record.
4. Keep the subtask index and task board reconciled as children are created, activated, paused, completed, or removed at closeout.
5. Never mark this parent Done, Cancelled, or delete its task folder as ordinary child closeout. Only a new explicit user instruction may change this standing lifecycle rule.

## 4. Decisions

- The existing task is reparented as a subtask rather than duplicated as an independent parent.
- This is a persistent skills-refactoring parent, not a finite project task. Completed children may be closed and deleted under normal closeout, but the parent and its folder remain open indefinitely unless the user explicitly instructs otherwise.

### 2026-11-27 18:40 UTC

> This task acts as a placeholder for refractoring skills now and in the future. You do not retire this task, only creat subtasks under it.

- **Decision:** Preserve this task as the standing parent for current and future skills-refactoring work. Create follow-up deliverables as child subtasks; do not create replacement parents for work within this defined scope or close/delete this parent at child closeout.

## 5. Progress

### 2026-11-27T16:50:00Z — startup P0 child 26 closeout

- **Action:** Split the remaining long sentence in `.agent/SESSION_START.md` into four sentences. The earlier closeout had not changed this sentence.
- **Result:** Read back the corrected passage. Resolved `lint-85322c6fe1ce661af2777338` in the Ledger. Closed and removed the completed child record.
- **Evidence:** Commit pending. Changed path: `.agent/SESSION_START.md`.
- **Validation:** Not run. No hosted CI results were inspected.


### 2026-11-27T16:42:00Z — startup P0 child 52 closeout

- **Action:** Rewrote the passive-voice statements in the Actions report template to name the capture process as the actor.
- **Result:** Read back the template. The two finding IDs in child 52 are not present in the current Ledger, so no Ledger finding status was changed. Closed and removed the completed child record.
- **Evidence:** Commit pending. Changed path: `.agent/skills/the-worker/assets/actions-report-template.md`.
- **Validation:** No local tests or hosted CI results were inspected.


### 2026-11-27T13:36:52Z — startup P0 child 24 closeout

- **Action:** Rewrote the ADR status and completed-task deletion descriptions in the document-type catalog to name the repository or Worker as the actor. Verified the target file and resolved all three linked findings in the central Ledger.
- **Result:** Closed and deleted child 24. Activated child 26, the next indexed P0 remediation.
- **Evidence:** Commit `80440b3c6a81e440826071a66dd9f9c3a3e38747`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:35:02Z — startup P0 child 23 closeout

- **Action:** Split the five long-sentence constructions in the Worker skill into shorter sentences. Verified the target file and resolved all five linked findings in the central Ledger.
- **Result:** Closed and deleted child 23. Activated child 24, the next P0 remediation.
- **Evidence:** Commit `239b1acd74e87bfc96a9b6f4ab5d8216603a9789`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:32:13Z — startup P0 child 22 closeout

- **Action:** Standardized the deletion verb in the GitHub Actions reference. Verified the target file and resolved the linked Ledger finding.
- **Result:** Closed and deleted child 22. Activated child 23, the next P0 remediation.
- **Evidence:** Commit `5305c1b39030c5057eacb1251867ce4fc96d0064`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:30:31Z — startup P0 child 21 closeout

- **Action:** Split all four semicolon constructions in `workspace/README.md` into separate sentences. Verified the target file and resolved the linked Ledger finding.
- **Result:** Closed and deleted child 21. Activated child 22, the next P0 remediation.
- **Evidence:** Commit `50b029374102b3a593c5e63dd38f54586158ac8e`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:27:38Z — startup P0 child 20 closeout

- **Action:** Rewrote both passive constructions in the CI Ledger reference to name the user and the Ledger as actors. Verified the target file and resolved both linked findings in the central Ledger.
- **Result:** Closed and deleted child 20. Activated child 21, the next P0 remediation.
- **Evidence:** Commit `d2e5abb40b6df969d74a748df90a135c47b34f59`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:24:24Z — startup P0 child 19 closeout

- **Action:** Rewrote the five passive constructions in the ASD-STE100 skill to name the actor or state the action directly. Verified the target file and resolved all five linked findings in the central Ledger.
- **Result:** Closed and deleted child 19. Activated child 20, the next P0 remediation.
- **Evidence:** Commit `67c3549c9c7106eddfdf5f90ccab563cc0720775`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:22:44Z — startup P0 child 18 closeout

- **Action:** Rewrote the passive constructions in the initialization procedure to name the user as the actor. Verified both cue occurrences and the reference-verification instruction. Resolved both linked findings in the central Ledger.
- **Result:** Closed and deleted child 18. Activated child 19, the next P0 remediation.
- **Evidence:** Commits `6f6b9431e93ed833611fefcf1eda03cae25499f0` and `f63fb0023e2c2c4fe78cf71fa7edc50ad0aa2b17`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:20:56Z — startup P0 child 17 closeout

- **Action:** Standardized the six action-term groups in the Worker skill. Verified the exact target file and resolved all six linked findings in the central Ledger.
- **Result:** Closed and deleted child 17. Activated child 18, the next P0 remediation.
- **Evidence:** Commit `a3603c9582a13695e52730d8b5f6d8911d7b5b03`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:18:10Z — startup P0 child 16 closeout

- **Action:** Split the two remaining semicolon constructions in the decision-governance reference into separate sentences. Verified the target file and resolved the linked Ledger finding.
- **Result:** Closed and deleted child 16. Activated child 17, the next P0 remediation.
- **Evidence:** Commit `ecf0a00796997d7ca6c76e96232632680e6268af`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:15:50Z — startup P0 child 15 closeout

- **Action:** Rewrote the seven passive constructions in the Worker skill as active instructions. Verified the target file and resolved all seven linked findings in the central Ledger.
- **Result:** Closed and deleted child 15. Activated child 16, the next P0 remediation.
- **Evidence:** Commit `958b18f9878db02cc9cbf3e788b27d54dbbb4a87`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:12:54Z — startup P0 child 14 closeout

- **Action:** Replaced the flagged phrasal-verb examples in the ASD-STE100 skill with plain-language descriptions and single-word alternatives. Verified the target file and resolved all five linked findings in the central Ledger.
- **Result:** Closed and deleted child 14. Activated child 15, the next P0 remediation.
- **Evidence:** Commit `7b682727a140dae6135471a694aca2148fdbff2c`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:10:46Z — startup P0 child 13 closeout

- **Action:** Standardized the initialization procedure on `fetch` for file retrieval and `verify` for confirmation. Verified the exact file and resolved both linked synonym-rotation findings in the central Ledger.
- **Result:** Closed and deleted child 13. Activated child 14, the next P0 remediation.
- **Evidence:** Commit `86ef132fb4948487f7f8aefe324ca1b74e19db0f`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:08:03Z — startup P0 child 12 closeout

- **Action:** Split all six semicolon constructions in the Worker skill into separate sentences. Verified the target file and resolved the linked Ledger finding.
- **Result:** Closed and deleted child 12. Activated child 13, the next P0 remediation.
- **Evidence:** Commit `f62d4cc6692f764cad57f1a291066c8af0966ca0`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:05:55Z — startup P0 child 11 closeout

- **Action:** Rewrote the remaining passive constructions in the Agent Skill Authoring skill as active instructions. Verified the exact target file and resolved all ten linked findings in the central Ledger.
- **Result:** Closed and deleted child 11. Activated child 12, the next P0 remediation.
- **Evidence:** Commit `eb780b92aa048fdaf2c9bc6a1e1783c8bc2adceb`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:02:43Z — startup P0 child 10 closeout

- **Action:** Rewrote the four linked passive-voice constructions in the decision-governance reference as direct instructions. Verified the source file and resolved all four findings in the central Ledger.
- **Result:** Closed and deleted child 10. Activated child 11, the next P0 remediation.
- **Evidence:** Commit `8324ee76f6ba30cbe04ca8b82414b2d51e98cdd0`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T13:00:05Z — startup P0 child 09 closeout

- **Action:** Standardized the remaining synonym-rotation wording in the CI Ledger reference. Verified the earlier `alter`/`modify` correction and the new `changes`/`modify` correction by remote readback. Resolved both findings in the central Ledger.
- **Result:** Closed and deleted child 09. Activated child 10, the next P0 remediation.
- **Evidence:** Commit `d83971693d6f268f7c52abe117ea00b22cbcd56d` corrected `alter` to `modify`. Commit `1a82e58b4d88cd86fd9f5c120f17ac22ca23d7a0` standardized `report-index changes` to `report-index modifications`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27T12:57:07Z — startup P0 child 07 and 08 closeout

- **Result:** Closed and deleted child records 07 and 08 after source readback and Ledger reconciliation. Child 09 is now the current P0 execution.
- **Evidence:** Child 07 commit `a5521f4c244720dcb49bfcc92fba1df657160566`. Child 08 commit `e1658a2dc41dffffe10d6563c5a7158f580c4918`. Ledger blob recovered from `b8f592ac62d41b92d0f5cbc71895fbc5870ed8f5`.
- **Validation:** Hosted validation remains pending. No hosted CI results were inspected.


### 2026-11-27 12:01 UTC

- **Action:** Closed P0 child 06 after readback. Started P0 child 07.
- **Result:** Child 06 standardized the active initialization instructions on `fetch`. The catalog now uses `closeout validation` instead of `closeout checks` for consistent terminology.
- **Evidence:** Commit `1ac4a9545ec7edf0b1369a3a1ba55c21dce915d7`. Child 06 record removed at closeout.
- **Next:** Commit and read back child 07, then continue the ordered P0 queue.


### 2026-11-27 11:59 UTC

- **Action:** Closed P0 child 05 after readback. Started P0 child 06.
- **Result:** Child 05 corrected four present-perfect constructions in the Agent Skill Authoring skill. The source file and task state were read back. The current eligible P0 child is 06.
- **Evidence:** Commit `b7de07d9138d3095e8b590f19a1a22da24595361`. Child 05 record removed at closeout.
- **Next:** Standardize the initialization policy's use of `fetch` and continue the ordered P0 queue.


### 2026-11-27 11:56 UTC

- **Action:** Closed Subtask 02 after completing the specialist-skill consolidation. Resolved the related P0 link finding in child 25. Started the first remaining P0 remediation child, 05.
- **Result:** The Worker now owns document governance, GitHub Actions, CI Ledger, and decision governance. The three specialist skill files are removed. The active callers and navigation paths now point to Worker-owned references. The one repository-wide broken link now points to the Worker reference.
- **Evidence:** Consolidation commit `80819ac6f8d3640671dd3b550ac2008cf3a0acc5`; Ledger path correction `8a00ccfe91f0acfea20bb03a0a01d7203ac3836a`; broken-link repair `75d4f66e0e9f665ddf913e1f9c8c4a44e21e5064`.
- **Readback:** Read back all changed files. Confirmed the three deleted specialist skill paths return not found. Checked local Markdown links in the changed navigation and reference files. Confirmed the repaired target exists.
- **Checks:** No local tests or linter run. No hosted run pages or logs inspected. Repository-published reports were read.
- **Queue:** The Ledger generated P0 remediation children 05–46. Child 25 is resolved. Child 05 is now active. The remaining P0 children precede the P1 queue.


### 2026-11-27 11:42 UTC

- **Action:** Started the approved specialist-skill consolidation after the user said “Proceed”. Fast-forwarded `gpt` to the merged `main` commit before implementation.
- **Result:** Confirmed the canonical skill template and relevant task templates. Mapped the three remaining specialist skills and their active activation/navigation references. The Worker will own their detailed procedures through references, not separate skills.
- **References:** Subtask `20261127-173000-02`; commit `ff863c96e0c64cd6aef2ee8ff60242af288deb00`; `.agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`.
- **Next:** Consolidate procedures, update activation and navigation references, remove the specialist skill files, then read back every changed path.

### 2026-11-27 18:29 UTC

- **Action:** Set this parent to P0 and selected it as Current Execution. Activated child 01 and reconciled the board and child index.
- **Result:** Readback confirmed parent, child, index, and board state. Child 02 (consolidate specialist skills into The Worker) is Ready after the mandatory startup P0 batch. Child 03 (objective-based task-parent selection) remains Paused. Child 04 (enforce template-first document editing) is Ready; it was created after no existing task covering the rule was found.
- **References:** Commit `1e6800f40e4c1bf1e15263f0a479a54afe81468a`; child `24f697da8a75972ff7f6a0dca7302a125e63499c`; index `3f0101796d08a5eba78dfe2fd4120b7445bf5c62`; board `91ca878a4c151aeb65d3f5ff78b438af8e437aa3`.
- **Next:** Execute child 01.

### 2026-11-27 17:30 UTC

- **Action:** Created Refactor Skills parent and began reparenting existing document-governance consolidation.
- **Result:** Parent record and child structure created.
- **References:** Existing task ID 20261127-102301.
- **Next:** Reconcile hierarchy and board.

### 2026-11-27 11:02 UTC — startup P0 child 04 remediation

- **Action:** Completed CI remediation child `20261127-173000-04`. Updated the two stale Markdown assertions in `.agent/skills/asd-ste100/scripts/test_generate_lint_report.py` to match the canonical `- **Source task:**` template label.
- **Result:** Commit `1e697f0e5167e9c0778cadef69d7cf084249be27` contains the test correction. Remote readback confirmed both assertions and the unchanged report template. No tests or scripts were run. Hosted CI results were not inspected.
- **References:** Child diagnostic/progress commit `418d2e0d1a1e845bf834799f915984983da68fa0`; implementation commit `1e697f0e5167e9c0778cadef69d7cf084249be27`; child completion/evidence commits `c27098af28f5581feb16b784fa67184b19256920` and `531e52bd0ce6239484a553a5d31209cbe13a290b`; child index commit `3f9867a5bc0e42df2828b361468aa2c2eb0e1e59`; board selection commit `40cbc1c4354d3c61dd5ff0d7df2c20c5b5b15b5a`.
- **Next:** Complete child-record deletion and index reconciliation. Continue the startup P0 batch with the remaining eligible and newly unblocked Ledger children.
 
### 2026-11-27 11:08 UTC — repository report handoff to child 05

- **Action:** Read the newest indexed on_repo report `.takeout/reports/lint_reports/on_repo/history/45987814713-attempt-1/report.json` for commit `1e697f0e5167e9c0778cadef69d7cf084249be27`.
- **Result:** All six lint-report regression tests passed. The Markdown link check still found four missing targets across `.takeout/reports/README.md`, ADR-0001, and DRAFT-0002. The Ledger created P0 child `20261127-173000-05` under this persistent parent.
- **Evidence:** `.takeout/reports/lint_reports/on_repo/history/45987814713-attempt-1/report.json`; child `20261127-173000-05`; report index run `45987814713`. No hosted Actions results were inspected.
- **Next:** Close and delete completed child 04. Execute child 05 by correcting the four stale local links after checking current canonical paths.

### 2026-11-27 11:08 UTC — startup P0 child 05 remediation

- **Action:** Completed child `20261127-173000-05`. Corrected the report navigation/lifecycle guidance, removed two stale links to the deleted task record from ADR-0001 while preserving task ID `20261124-103354`, and corrected DRAFT-0002's ADR link.
- **Result:** The four unresolved local targets from report `45987814713` now resolve to current repository paths or no longer appear as links. Remote readback confirmed all three changed files and both new link targets. No linter or tests were run.
- **References:** Report README commit `f514ad0dfc46bca10ab5d9cae95d609d26b8a704`; ADR-0001 commit `60ec079dbb8aaa6db97d8b717af9fc3b95962826`; DRAFT-0002 commit `22907d4bfb9905ee155d0d16164982c96d415762`; child completion commit `f6359e9507f8b383b1000488da06ee233c9c514b`; report `.takeout/reports/lint_reports/on_repo/history/45987814713-attempt-1/report.json`.
- **Next:** Close and delete child 05. Reconcile duplicate P0 remediation children under their other genuine parents. Then resume the approved Refactor Skills workstream.

### 2026-11-27 11:08 UTC — startup P0 batch completed

- **Action:** Processed every eligible CI-generated P0 child in the currently published task indexes. Closed the duplicate P0 children under the CI workflow and Template Fix parents using the shared verified remediation commits.
- **Result:** No eligible CI-generated P0 tasks remain in the inspected active parent indexes. The completed P0 remediation records were removed after parent/index reconciliation. No local tests were run and no hosted CI results were inspected.
- **Next:** Child `20261127-173000-02` is Ready as the next Refactor Skills deliverable. Child `20261127-173000-03` remains Paused.

### 2026-11-27 11:26 UTC — template-first editing governance

- **Action:** Created child `20261127-173000-04` to make template-first document editing a durable Worker-owned rule.
- **Result:** No existing active task covering this requirement was found. The child requires reading the applicable template before edits and raising a proposed template to the user before modifying a document when no applicable template exists. It explicitly avoids introducing a separate skill.
- **References:** Child `subtasks/04-enforce-template-first-document-editing.md`; child index commit `52a1c9080cc19ebe26bbd0999c68cbbd5e0cc247`; task creation commit `2980a1f77e5968f4e2fe5a1e6e83e9c66e57d921`.
- **Next:** Execute the already approved specialist-skill consolidation child `20261127-173000-02`; then address this new governance child.

## 6. Current State and Remaining Work

This parent remains open as the persistent skills-refactoring workstream. Child 01 (document governance consolidation) has been completed and closed. Child 04 (the lint report regression-test remediation) is complete by commit `1e697f0e5167e9c0778cadef69d7cf084249be27` and its child record is closed. Child 05 (Markdown links and heading anchors) is complete and closed after commits `f514ad0dfc46bca10ab5d9cae95d609d26b8a704`, `60ec079dbb8aaa6db97d8b717af9fc3b95962826`, and `22907d4bfb9905ee155d0d16164982c96d415762`. Child 02 (consolidate specialist skills into The Worker) is Ready after the mandatory startup P0 batch. Child 03 (objective-based task-parent selection) remains Paused. Future skills-refactoring requests that fit this scope must be captured as new child subtasks under this parent. Do not retire this parent when the current children are complete.

## 7. Verification and Evidence

- **Commit SHA:** `1e6800f40e4c1bf1e15263f0a479a54afe81468a` (parent priority/current-execution); `24f697da8a75972ff7f6a0dca7302a125e63499c` (child 01 activation); `3f0101796d08a5eba78dfe2fd4120b7445bf5c62` (subtask index); `91ca878a4c151aeb65d3f5ff78b438af8e437aa3` (board)
- **Changed paths:** `workspace/tasks/20261127-173000/task.md`; `workspace/tasks/20261127-173000/subtasks/01-consolidate-document-standards-into-worker.md`; `workspace/tasks/20261127-173000/subtasks/README.md`; `workspace/task_board.md`
- **Readback:** Verified all four paths on branch `gpt`.
- **Checks:** Not performed
- **Limitations:** No tests performed.

## 8. Handoff

Keep this persistent P0 Refactor Skills parent open. Create and execute child subtasks for current and future skills-refactoring deliverables. Do not close or delete the parent task unless the user explicitly changes this instruction.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| `lint-tooling-fd63ee164167664baaa97d9b` | high | Lint tooling check failed: Lint report regression tests | [report](../../../.takeout/reports/lint_reports/on_changed/history/45979960470-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45979960470) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45984083069-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45984083069) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985300823-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985300823) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985475477-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985475477) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45986815109-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45986815109) |
| `lint-tooling-2c26d8bc14fd4d4bbe314234` | high | Lint tooling check failed: Markdown links and heading anchors | [report](../../../.takeout/reports/lint_reports/on_changed/history/45911866106-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911866106) · [report](../../../.takeout/reports/lint_reports/on_changed/history/46019304454-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46019304454) · [report](../../../.takeout/reports/lint_reports/on_changed/history/46020530596-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46020530596) · [report](../../../.takeout/reports/lint_reports/on_repo/history/46023746666-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46023746666) · [report](../../../.takeout/reports/lint_reports/on_changed/history/46023746732-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46023746732) |
| `lint-89880d1a1650656e6b26d226` | low | present-perfect: Compound tense. Use simple past/present unless current relevance is the point \(then keep and flag\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45904670122-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45904670122) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45942426065-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45942426065) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) · [report](../../../.takeout/reports/lint_reports/on_changed/history/46012838586-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46012838586) |
| `lint-85322c6fe1ce661af2777338` | medium | long-sentence: Sentence has 27 words \(cap 25\). Split it. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45904670122-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45904670122) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45906789462-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45906789462) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45942426065-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45942426065) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-bdeb2ff1622490b994e19f76` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45921789448-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45921789448) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45974724264-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45974724264) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-66ac36e2cdb3db3683c0c8f2` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45921789448-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45921789448) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45974724264-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45974724264) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-4e20a50af596bd1c8120efea` | medium | synonym-rotation: 'retrieve' and 'fetch' name the same action. Pick one and use it every time. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45942426065-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45942426065) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-e7ff64fedb3eddf5ee3c1564` | medium | semicolon: STE bans the semicolon \(Rule 8.1\). Split into separate sentences. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45995191222-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45995191222) |
| `lint-933a579fb10c54b6f0b0201a` | medium | long-sentence: Sentence has 26 words \(cap 25\). Split it. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-ba8e0ed371140388669d2100` | low | present-perfect: Compound tense. Use simple past/present unless current relevance is the point \(then keep and flag\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-301135338f19f01e083e45ee` | low | present-perfect: Compound tense. Use simple past/present unless current relevance is the point \(then keep and flag\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-6d4fd87d7c04e6106995412e` | low | present-perfect: Compound tense. Use simple past/present unless current relevance is the point \(then keep and flag\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-19df0784fbab3f590bc978f2` | low | present-perfect: Compound tense. Use simple past/present unless current relevance is the point \(then keep and flag\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-7e86fc5d602e4865ed4a0ff6` | medium | nominalization: Action frozen into a noun. Use the verb \(analyze, not perform an analysis of\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-fa833ca0d8a25be575faf6e0` | medium | nominalization: Action frozen into a noun. Use the verb \(analyze, not perform an analysis of\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-7a15da17f8212acf9cbcd80a` | low | present-perfect: Compound tense. Use simple past/present unless current relevance is the point \(then keep and flag\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-320768d857c6a3e84654f3f5` | low | present-perfect: Compound tense. Use simple past/present unless current relevance is the point \(then keep and flag\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-361fe239198e1c7837a878ba` | low | present-perfect: Compound tense. Use simple past/present unless current relevance is the point \(then keep and flag\). | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-12a9fb2640f958cc7e75f621` | medium | marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-c50be8a609eda6ecc738029b` | medium | marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-d7e2c69987f9328ac247ac53` | medium | marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-0d5ed7f9257c40733f5c321d` | medium | marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-2673e9a5ae5dd03778f880c9` | medium | marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45992769255-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-869c8495109dea6f34af871c` | medium | synonym-rotation: 'check' and 'confirm' name the same action. Pick one and use it every time. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45864180906-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45864180906) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45901511879-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45901511879) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45902843717-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45902843717) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-e65e3922aa38293af2adc5e0` | medium | synonym-rotation: 'delete' and 'remove' name the same action. Pick one and use it every time. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45903174690-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45903174690) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-4012e882a41727aa31e45e80` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45906789462-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45906789462) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45935162405-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45935162405) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45977120769-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45977120769) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-23ba89c188bd721485225ac0` | medium | long-sentence: Sentence has 30 words \(cap 25\). Split it. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-8d237e4d80507b6e1ceceb31` | medium | long-sentence: Sentence has 28 words \(cap 25\). Split it. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-b29e4df2ee98e11a4663446d` | medium | long-sentence: Sentence has 34 words \(cap 25\). Split it. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-911fad1e156f4210f836f36c` | medium | long-sentence: Sentence has 36 words \(cap 25\). Split it. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-95b3ae27d255dd6d3908c02c` | medium | long-sentence: Sentence has 26 words \(cap 25\). Split it. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45911174533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911174533) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-71fd369fd4ce87f3145d3f61` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-0b78e160768da5f8fc81245e` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-b6f783768f9aa08d96bf979c` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-9997ef7899ffcdb243897741` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-9943dcb3a220dcbe0a08ff17` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-3d99cf816793019bd73c4f70` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-579e397c39954135265f1d98` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-14114c25a67a248bad384f1b` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-298a9b83f5adba5f46527b78` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45911174533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911174533) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-f85e8d2b3bb15312e48006c0` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45911174533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911174533) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-3c01363d8fccb6632309a933` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45911174533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911174533) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-0a8fdd51c323d7e6c5184e93` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45911174533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911174533) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-0ce56fdfcbc85adb0c649e73` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-235b8a3528fa8a066c7b86a4` | medium | semicolon: STE bans the semicolon \(Rule 8.1\). Split into separate sentences. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-6ecaad7e08b08c8dc23c4ac5` | medium | synonym-rotation: 'delete' and 'remove' name the same action. Pick one and use it every time. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911611855-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45929248916-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45929248916) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45970411285-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-0927b4ce823c0e0c8d5570fa` | medium | semicolon: STE bans the semicolon \(Rule 8.1\). Split into separate sentences. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45910973837-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45911174533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911174533) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45940913773-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45940913773) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-77496caee1aa1b14090beb02` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45935299170-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45935299170) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-ae777a92ddc5d2c5149411bc` | medium | semicolon: STE bans the semicolon \(Rule 8.1\). Split into separate sentences. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45935299170-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45935299170) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-1d091436eb9c47dd7a5b55d1` | medium | semicolon: STE bans the semicolon \(Rule 8.1\). Split into separate sentences. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45947839170-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45947839170) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45974724264-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45974724264) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-f89fcc99c66cd06012ce7d5a` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45947839170-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45947839170) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45974724264-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45974724264) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-174cb92f03c94b341eec0955` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45974724264-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45974724264) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-fbe6150d9b5e8dab3b1e43a3` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45988691008-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45988691008) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-8d3ad3a1e3838d879ee9b85a` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45988691008-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45988691008) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-e871aaaf906a610ac0db5605` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45988691008-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45988691008) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-e56053c3ddae76d3a0704b63` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45988691008-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45988691008) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-2eafa78f211213b12b14d4d5` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45988691008-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45988691008) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-cb29534f35d8d330ae1e06be` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45988691008-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45988691008) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-9a23cba48e9d5ffca1df4cc7` | medium | semicolon: STE bans the semicolon \(Rule 8.1\). Split into separate sentences. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45988691008-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45988691008) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45993945279-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45993945279) |
| `lint-78a70aacc34addace6e797ec` | medium | synonym-rotation: 'verify' and 'check' name the same action. Pick one and use it every time. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45994577533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45994577533) |
| `lint-9db0ccdc5f344a34e6b09777` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45994577533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45994577533) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45994942334-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45994942334) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45995191222-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45995191222) |
| `lint-fa71e22a78d6e4ce44e3a977` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/45994577533-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45994577533) |
| `lint-c4694e88f04cd654220cc23d` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/46015025342-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46015025342) |
| `lint-4d345e231ac14cad2ca77be0` | low | passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. | [report](../../../.takeout/reports/lint_reports/on_changed/history/46015025342-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46015025342) |

### 2026-11-27 — CI Ledger and GitHub Actions consolidation closeout

- Completed child 51. Consolidated scripts, regression tests, shared eligibility policy, schemas, and report template under `.agent/skills/the-worker/scripts/` and `.agent/skills/the-worker/assets/`.
- Updated the composite capture action and Worker references. Removed duplicate report-family implementations. Kept report indexes, immutable reports, and Ledger state in their data paths.
- Read back canonical scripts, regression tests, schemas, template, and capture action. Tests, lint, and hosted CI inspection were not performed, as required.
- **Commits:** `7744b9f`, `36a6ecc`, `578207a`, `4d86b34`, `6f8adc0`, `e75cf10`, `9b8a88e`, `e5c48e2`.