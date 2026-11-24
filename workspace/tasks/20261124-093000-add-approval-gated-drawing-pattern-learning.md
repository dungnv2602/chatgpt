# Task: Add approval-gated drawing pattern learning

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-093000
- **Created:** 2026-11-24 09:30 UTC
- **Updated:** 2026-11-24 09:39 UTC
- **Priority:** P2
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved for the Drawing workflow change. Each pattern creation, revision, confidence change, or retirement still requires separate explicit user approval.
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** None
- **Ledger group:** None
- **Archived:** No

<!-- Lifecycle invariant: keep the active record In Progress and Archived: No until the final archive copy is written and read back. Set Done/Cancelled and Archived: Yes only in the initial archive copy. Check its complete content and commit metadata before deleting the active path. After creation, treat the archive copy as immutable. Delete the active record only after archive verification. Move the board row to Historical only after the active path is absent and the board can link the exact archive path and archive commit. If any step fails, keep the task open and reconcile the partial state without rewriting the archive. -->

## 1. Original Request

Update drawing workflow to automatically extract and update successful patterns when image generated successfully, and automatically extract and update failure patterns when image generated failed. But you must bring them up and discuss with me first, then only update after my approval.

## 2. Subsequent Instructions

- **2026-11-24:** The user selected Condensed Mode and explicitly started a session.
- **2026-11-24:** Do not update a successful-pattern or failure-pattern index until the user has reviewed and explicitly approved the proposed change.

## 3. Objective

Add a required post-generation pattern-learning step to the Drawing workflow. Extract reusable success and failure pattern candidates from verified attempt outcomes. Present each candidate to the user for discussion. Update the canonical pattern indexes only after explicit approval.

## 4. Requirements

1. Assess every returned image separately against the attempt's recorded acceptance criteria and active session brief before pattern extraction.
2. Distinguish a successful image-tool call from a successful visual result. A returned image is not a successful pattern unless the relevant requirements were met or the user explicitly accepts the result.
3. Extract success candidates only when evidence shows that a technique contributed to a meaningful improvement or reliably protected an important requirement.
4. Inspect failed, refused, output-less, partial, off-target, and source-linkage outcomes for reusable failure lessons. Do not turn every isolated failure into a global pattern. Follow the existing rule for recurring failures or a single incident that reveals an important reusable risk.
5. Separate observed facts from suspected causes. Do not infer internal image-model causes. Record countermeasures as tested only when an actual attempt tested them.
6. Compare each candidate with existing patterns. Propose a new entry, evidence update, confidence change, scope/limitation change, or retirement when the new evidence supports that action. Do not create duplicates.
7. After each attempt assessment, present each proposed pattern change to the user. Include its type, proposed principle or observed failure, scope, evidence, confidence, hypotheses, tested countermeasures, and limitations as applicable.
8. Require explicit user approval for each pattern creation or change. Workflow approval does not pre-approve future pattern entries. Silence, image delivery, prompt approval, or approval of a different candidate does not count.
9. Do not write an unapproved candidate to either canonical pattern index. If the user requests changes, revise the proposal and discuss it again. If the user rejects or defers it, record that decision in the attempt record and do not update the index.
10. Assign the next unused permanent pattern ID only after approval. Never reuse an ID.
11. On approval, update only the relevant pattern index. Link exact attempt evidence. Record the user's approval date and approved scope in the pattern entry.
12. If no reusable lesson exists, record that no pattern candidate was identified. Do not create a weak entry or ask for approval without a concrete candidate.
13. Handle mixed outcomes and multiple outputs independently. A single attempt may support a success candidate for one output and a failure candidate for another.
14. Keep the active session brief and latest user instructions above all pattern guidance. A pattern must never authorize a creative change or restriction.
15. This is an assistant-driven post-attempt workflow step. It does not run as a background watcher and does not authorize automatic writes.

## 5. Decisions

- **Approved by the user:** Add automatic post-attempt extraction and a user discussion/approval gate before any global pattern-index write.
- **Approved by the user:** Preserve user control over each future pattern addition or revision.
- **Implementation detail:** Use the existing Drawing skill, pattern governance, and canonical attempt template. Do not add a separate pattern queue or duplicate pattern catalogue unless inspection shows a concrete need.
- **Not authorized:** Writing any new or revised successful/failure pattern entry without separate approval for that specific proposal.

## 6. Progress Log

### 2026-11-24 09:39 UTC — Implement and verify approval-gated pattern learning

- **Action:** Updated the Drawing Skill, pattern governance, pattern-entry template, and Document Type Catalog. Added a mandatory review after every image generation or edit attempt, including refusals and no-output failures.
- **Result:** The workflow now assesses each output, extracts reusable success/failure candidates, checks existing entries, presents proposed changes, and waits for explicit approval before assigning IDs or changing indexes. Success candidates require meaningful evidence. Failure candidates require a recurring problem or important reusable risk. New and existing entries require per-change approval. The pattern-entry template is Version 1.1 and records the last approval date and approved change. The Document Type Catalog is Version 1.10.
- **Commits:** Workflow and governance [81ec641](https://github.com/dungnv2602/chatgpt/commit/81ec641145c2d9b74d38256f07bef02f05deb70b); approval metadata [849808d](https://github.com/dungnv2602/chatgpt/commit/849808d5b9a8bf53307c420b911c7086bd2c2df3); review timing [e2509c8](https://github.com/dungnv2602/chatgpt/commit/e2509c8bfa03aa8f3200eda0822563deeac5ed68).
- **Read-back:** All four changed files passed targeted content checks. The successful-pattern index SHA remains `d06dff83c57e03dddff5bfeb18b303f58b765997`. The failure-pattern index SHA remains `250768f6f3172a493a681df8951ce8d6fcf46ad1`. No pattern entry was added or changed.
- **Limitations:** No image was generated in this workflow-maintenance turn, so no new pattern candidate was available for user review. No local lint or test was run. No hosted validation result was checked or claimed.
- **Next:** Prepare the Done archive copy, register its exact path and timestamp, then delete the active record and reconcile the task board.

### 2026-11-24 09:30 UTC — Confirm scope for attempt-record formats

- **Action:** Checked the novel illustration prompt template, Novel README and workflow, Document Type Catalog, and Drawing attempt template.
- **Result:** A new durable review field in attempt records would require a broader versioned change to novel templates and their owner workflow. The existing attempt records already preserve the evidence needed for pattern proposals. The post-attempt conversation will carry each proposal. Approved pattern entries will record the approval date and exact attempt evidence. No attempt-template or novel-template migration is needed.
- **References:** `novels/templates/illustration-prompt-v1.1.md`; `novels/README.md`; `novels/WORKFLOW.md`; `skills/drawing/assets/attempt-template.md`; `skills/document-standards/references/document-type-catalog.md`.
- **Next:** Revise the Drawing skill, pattern README, pattern-entry template, and catalog. Leave both pattern indexes unchanged.

### 2026-11-24 09:30 UTC — Inspect current pattern governance and task continuity

- **Action:** Read the foundational session skills, Drawing skill, required Drawing references, current pattern indexes, pattern-entry templates, attempt template, workspace README, task board, and active CI task.
- **Result:** The Drawing skill already requires pattern consultation before prompt drafting and classifies each returned image after generation. The pattern indexes contain three successful patterns (S-001 to S-003) and eight failure patterns (F-001 to F-008). Existing governance requires traceable evidence, separates observations from hypotheses, and limits failure entries to recurring failures or important reusable risks. No mandatory post-attempt extraction, discussion, or user-approval gate exists. The current CI task remains In Progress and is no longer the current execution task.
- **References:** `skills/drawing/SKILL.md`; `skills/drawing/references/patterns/README.md`; `skills/drawing/references/patterns/successful-patterns.md`; `skills/drawing/references/patterns/failure-patterns.md`; `skills/drawing/assets/pattern-entry-templates.md`; `skills/drawing/assets/attempt-template.md`; `skills/drawing/references/generation-recovery-and-provenance.md`; `skills/drawing/references/prompt-fidelity.md`; `workspace/task_board.md`; prior task `20261123-225745`.
- **Next:** Load Agent Skill Authoring and the repository writing policy. Then update the Drawing workflow and its canonical review templates. Keep the success and failure indexes unchanged until a future candidate receives explicit user approval.

## 7. Current State

The Drawing workflow now requires post-attempt pattern review after every image generation or edit attempt. This includes refusals, tool failures, and no-output results.

The assistant assesses every returned output separately. It extracts success candidates only when evidence shows meaningful improvement or protection of an important requirement. It extracts failure candidates only for recurring problems or important reusable risks. It checks existing entries before proposing new patterns or updates.

The assistant presents each candidate to the user and discusses its exact scope and content. It does not assign an ID or change either global pattern index before explicit approval. Approval applies only to the candidate or candidates the user identifies. The pattern-entry template records the last approval date and approved change.

The Drawing Skill, pattern README, pattern-entry template, and Document Type Catalog are committed and read back. The successful-pattern and failure-pattern indexes remain unchanged. No image was generated during this maintenance task, so no pattern candidate was created.

## 8. Remaining Work

No implementation work remains. Future pattern proposals must follow the new per-candidate discussion and approval gate.

## 9. Next Actions

1. Create the immutable Done archive copy with its UTC archive timestamp.
2. Read back the complete archive copy and verify its commit.
3. Register the exact archive path and timestamp in `.github/archive-retention-index.json`.
4. Delete the active task record and update the task board.
5. Restore the CI Ledger task as current execution.

## 10. References

- `skills/drawing/SKILL.md`
- `skills/drawing/references/patterns/README.md`
- `skills/drawing/references/patterns/successful-patterns.md`
- `skills/drawing/references/patterns/failure-patterns.md`
- `skills/drawing/assets/pattern-entry-templates.md`
- `skills/document-standards/references/document-type-catalog.md`
- `workspace/task_board.md`
- Commits: [81ec641](https://github.com/dungnv2602/chatgpt/commit/81ec641145c2d9b74d38256f07bef02f05deb70b), [849808d](https://github.com/dungnv2602/chatgpt/commit/849808d5b9a8bf53307c420b911c7086bd2c2df3), [e2509c8](https://github.com/dungnv2602/chatgpt/commit/e2509c8bfa03aa8f3200eda0822563deeac5ed68).

## 11. Verification

- **Check:** Drawing workflow rules, pattern approval governance, entry-template fields, catalog version, unchanged pattern indexes, task state, and board selection.
- **Method:** Retrieved the exact files from branch `gpt` and checked the expected content and blob SHAs.
- **Result:** All four changed files passed targeted read-back checks. Both pattern indexes retain their original blob SHAs. The new Drawing task is current execution. The previous CI task remains In Progress and is checkpointed.
- **Limitations:** No image generation occurred, so no pattern proposal was available. No local linter or test was run. No hosted validation result was checked. This task makes documentation and workflow-instruction changes only.

## 12. Handoff Instructions

The Drawing workflow now extracts reusable success and failure candidates after every generation or edit attempt. Present each candidate to the user and discuss its exact proposed change. Do not create, revise, promote, change confidence, or retire a pattern without explicit approval of that specific proposal. Do not treat image approval, prompt approval, workflow approval, or silence as pattern approval. If no reusable lesson exists, do not create a candidate.

Keep the current session brief as the creative authority. Do not let pattern guidance override it. Both global pattern indexes remain unchanged after this task.

After closeout, resume the previous current-execution task `20261123-225745` from its existing Next Actions. Do not dispatch or poll CI.

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
