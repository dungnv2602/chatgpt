# Subtask: Consolidate specialist skills into The Worker

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-02
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit user instruction to consolidate .agent/skills/github-actions, ci-ledger, decision-governance, and document-standards into The Worker and remove those separate skills.
- **Governing ADR(s):** None
- **Dependencies:** None — child 01 is complete and the mandatory startup P0 batch is complete
- **Eligibility / deferral reason:** Eligible — Ready, approved, dependencies satisfied
- **Required:** Yes
- **Created:** 2026-11-27 18:00 UTC
- **Updated:** 2026-11-27 11:42 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

Confirm the parent before creating this child: it must directly advance the parent's objective or acceptance criteria. Do not choose the active parent solely because it is active, or because the work shares a repository, files, or broad theme. If the relationship is uncertain, leave parentage unassigned until resolved.

## 1. Original Prompt

> Consolidate these into worker skill 
>
> .agent/skills/github-actions 
>
> .agent/skills/ci-ledger 
>
> .agent/skills/decision-governance 
>
> .agent/skills/document-standards 
>
> I want them gone, now the worker handle those.

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Move all necessary operational rules and responsibilities from the four specialist skills into the Worker skill so The Worker is the sole skill owner for these functions, then remove the four specialist skill directories and reconcile activation references, indexes, templates, schemas, supporting assets, and documentation so no dangling references or duplicate activation paths remain.

## 4. Acceptance Criteria

1. The Worker skill includes all required GitHub Actions workflow design, CI remediation, Ledger intake/attribution/finding lifecycle/integrity, decision governance/ADR lifecycle/analysis, and document governance/format coverage procedures.
2. Consolidation preserves critical safeguards, ownership boundaries, execution restrictions, and integrity rules without conflicting or duplicated instructions.
3. The four separate skill directories are removed, unless a necessary non-skill supporting asset is deliberately relocated and justified.
4. Skill index, session-start procedures, catalogs, scripts, references, and related callers are reconciled and read back; no activation references or dead links remain.
5. Worker is the sole activation/governance entry point for these responsibilities; task-specific rules are integrated in Worker and not split into skill activation.
6. Changes are committed on branch gpt, all changed paths are read back, and acceptance evidence is recorded.

## 5. Decisions and Progress

### 2026-11-27 11:42 UTC — execution started

- **Action:** Began the approved consolidation after the user said “Proceed”. Fast-forwarded `gpt` to the merged `main` commit. Read the skill template, Worker skill, session-start procedure, initialization policy, catalog, and affected indexes.
- **Result:** The three specialist directories contain only `SKILL.md`. Their procedures will move into Worker-owned references. Document governance remains in The Worker.
- **References:** Merge commit `ff863c96e0c64cd6aef2ee8ff60242af288deb00`; `.agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`.
- **Next:** Finish the reference migration and reconcile every active caller before deleting the specialist skill files.

### 2026-11-27 18:00 UTC

- **Action:** Captured the requested consolidation as a subtask of Refactor Skills.
- **Result:** Approved scope recorded; execution deferred behind mandatory P0 queue.
- **References:** The four skill paths named in the original prompt.
- **Next:** Compare each specialist skill and its referenced assets/callers against The Worker. Consolidate carefully, then delete redundant skill folders and reconcile references.

### 2026-11-27 11:08 UTC — startup P0 batch complete

- **Action:** Reconciled all currently indexed CI-generated P0 children. The P0 remediation work is committed and its task records have been closed and deleted under the normal lifecycle.
- **Result:** This child’s prerequisites are satisfied. It is now Ready under the persistent Refactor Skills parent.
- **Next:** Begin the approved specialist-skill consolidation when selected for execution.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Task record and task indexes/board
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** Consolidation and deletion have not been performed.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

The Worker marks the child Done only after its acceptance criteria pass and the intended-branch commit is read back. For CI remediation, commit-based completion is separate from hosted validation.

## 8. Hosted Validation

Conditional: CI remediation only.

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

Resume after the mandatory P0 queue. First inspect all four skill folders, their referenced assets, session-start/index/catalog references and applicable contracts. Before modifying documents, read the applicable templates/contracts. Consolidate content into The Worker, remove obsolete specialist skill directories and reconcile every caller.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
