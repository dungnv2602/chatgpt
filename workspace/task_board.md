# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](TASK_BOARD_TEMPLATE.md). Preserve its structure and scheduler contract.

## Scheduler contract

The Worker is the sole scheduler. This board publishes its current selection and ordered eligible queue. It is not a second scheduler. Compare the board with task records and child indexes before declaring the queue empty.

Check eligibility before priority or age. Dependencies must be satisfied, execution must be authorized, and status must be Ready. Rank eligible tasks by priority (P0 first), then age within the same priority unless a documented dependency or material constraint changes the order. Keep ineligible tasks out of the queue. List them in the appropriate deferred section with the exact reason.

**Approval:** Approved records explicit authorization for the documented scope or applicable standing authorization. Pending means the user has not authorized execution. Declined means the user rejected the proposal. Approval does not depend on status or eligibility.

This is the sole index of active task parents. Each parent folder contains `task.md` and `subtasks/README.md`. The parent index lists substantive children. Board links point to parents, except Current Execution may link to the selected child. Keep a parent open while a required child remains open. The Worker owns status, selection, and deletion at closeout.

## Current Execution

[20261127-173000-05: CI remediation — Review present-perfect findings in .agent/skills/agent-skill-authoring/SKILL.md](tasks/20261127-173000/subtasks/05-ci-remediation-review-present-perfect-findings-in-agent-skills-agent-skill-auth.md). This P0 child is active under the persistent Refactor Skills parent.

## Ordered Eligible Execution Queue

1. **P0** — [20261127-173000-05: CI remediation — Review present-perfect findings in .agent/skills/agent-skill-authoring/SKILL.md](tasks/20261127-173000/subtasks/05-ci-remediation-review-present-perfect-findings-in-agent-skills-agent-skill-auth.md) — Approved, Ready, no dependencies.
2. **P0** — [20261127-173000-06: CI remediation — Review synonym-rotation findings in .agent/INITIALIZATION\\\_POLICY.md](tasks/20261127-173000/subtasks/06-ci-remediation-review-synonym-rotation-findings-in-agent-initialization-policy.md) — Approved, Ready, no dependencies.
3. **P0** — [20261127-173000-07: CI remediation — Review synonym-rotation findings in .agent/skills/the-worker/references/document-type-catalog.md](tasks/20261127-173000/subtasks/07-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-refe.md) — Approved, Ready, no dependencies.
4. **P0** — [20261127-173000-08: CI remediation — Review synonym-rotation findings in .agent/skills/the-worker/references/decision-governance.md](tasks/20261127-173000/subtasks/08-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-refe.md) — Approved, Ready, no dependencies.
5. **P0** — [20261127-173000-09: CI remediation — Review synonym-rotation findings in .agent/skills/the-worker/references/ci-ledger.md](tasks/20261127-173000/subtasks/09-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-refe.md) — Approved, Ready, no dependencies.
6. **P0** — [20261127-173000-10: CI remediation — Review passive-voice findings in .agent/skills/the-worker/references/decision-governance.md](tasks/20261127-173000/subtasks/10-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md) — Approved, Ready, no dependencies.
7. **P0** — [20261127-173000-11: CI remediation — Review passive-voice findings in .agent/skills/agent-skill-authoring/SKILL.md](tasks/20261127-173000/subtasks/11-ci-remediation-review-passive-voice-findings-in-agent-skills-agent-skill-author.md) — Approved, Ready, no dependencies.
8. **P0** — [20261127-173000-12: CI remediation — Review semicolon findings in .agent/skills/the-worker/SKILL.md](tasks/20261127-173000/subtasks/12-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-skill-md.md) — Approved, Ready, no dependencies.
9. **P0** — [20261127-173000-13: CI remediation — Review synonym-rotation findings in .agent/SESSION\\\_START.md](tasks/20261127-173000/subtasks/13-ci-remediation-review-synonym-rotation-findings-in-agent-session-start-md.md) — Approved, Ready, no dependencies.
10. **P0** — [20261127-173000-14: CI remediation — Review phrasal-verb findings in .agent/skills/asd-ste100/SKILL.md](tasks/20261127-173000/subtasks/14-ci-remediation-review-phrasal-verb-findings-in-agent-skills-asd-ste100-skill-md.md) — Approved, Ready, no dependencies.
11. **P0** — [20261127-173000-15: CI remediation — Review passive-voice findings in .agent/skills/the-worker/SKILL.md](tasks/20261127-173000/subtasks/15-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-skill-m.md) — Approved, Ready, no dependencies.
12. **P0** — [20261127-173000-16: CI remediation — Review semicolon findings in .agent/skills/the-worker/references/decision-governance.md](tasks/20261127-173000/subtasks/16-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-references.md) — Approved, Ready, no dependencies.
13. **P0** — [20261127-173000-17: CI remediation — Review synonym-rotation findings in .agent/skills/the-worker/SKILL.md](tasks/20261127-173000/subtasks/17-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-skil.md) — Approved, Ready, no dependencies.
14. **P0** — [20261127-173000-18: CI remediation — Review passive-voice findings in .agent/SESSION\\\_START.md](tasks/20261127-173000/subtasks/18-ci-remediation-review-passive-voice-findings-in-agent-session-start-md.md) — Approved, Ready, no dependencies.
15. **P0** — [20261127-173000-19: CI remediation — Review passive-voice findings in .agent/skills/asd-ste100/SKILL.md](tasks/20261127-173000/subtasks/19-ci-remediation-review-passive-voice-findings-in-agent-skills-asd-ste100-skill-m.md) — Approved, Ready, no dependencies.
16. **P0** — [20261127-173000-20: CI remediation — Review passive-voice findings in .agent/skills/the-worker/references/ci-ledger.md](tasks/20261127-173000/subtasks/20-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md) — Approved, Ready, no dependencies.
17. **P0** — [20261127-173000-21: CI remediation — Review semicolon findings in workspace/README.md](tasks/20261127-173000/subtasks/21-ci-remediation-review-semicolon-findings-in-workspace-readme-md.md) — Approved, Ready, no dependencies.
18. **P0** — [20261127-173000-22: CI remediation — Review synonym-rotation findings in .agent/skills/the-worker/references/github-actions.md](tasks/20261127-173000/subtasks/22-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-refe.md) — Approved, Ready, no dependencies.
19. **P0** — [20261127-173000-23: CI remediation — Review long-sentence findings in .agent/skills/the-worker/SKILL.md](tasks/20261127-173000/subtasks/23-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-skill-m.md) — Approved, Ready, no dependencies.
20. **P0** — [20261127-173000-24: CI remediation — Review passive-voice findings in .agent/skills/the-worker/references/document-type-catalog.md](tasks/20261127-173000/subtasks/24-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md) — Approved, Ready, no dependencies.
21. **P0** — [20261127-173000-26: CI remediation — Review long-sentence findings in .agent/SESSION\\\_START.md](tasks/20261127-173000/subtasks/26-ci-remediation-review-long-sentence-findings-in-agent-session-start-md.md) — Approved, Ready, no dependencies.
22. **P0** — [20261127-173000-27: CI remediation — Review passive-voice findings in workspace/README.md](tasks/20261127-173000/subtasks/27-ci-remediation-review-passive-voice-findings-in-workspace-readme-md.md) — Approved, Ready, no dependencies.
23. **P0** — [20261127-173000-28: CI remediation — Review marketing-adjective findings in .agent/skills/asd-ste100/SKILL.md](tasks/20261127-173000/subtasks/28-ci-remediation-review-marketing-adjective-findings-in-agent-skills-asd-ste100-s.md) — Approved, Ready, no dependencies.
24. **P0** — [20261127-173000-29: CI remediation — Review nominalization findings in .agent/skills/asd-ste100/SKILL.md](tasks/20261127-173000/subtasks/29-ci-remediation-review-nominalization-findings-in-agent-skills-asd-ste100-skill.md) — Approved, Ready, no dependencies.
25. **P0** — [20261127-173000-30: CI remediation — Review present-perfect findings in .agent/skills/asd-ste100/SKILL.md](tasks/20261127-173000/subtasks/30-ci-remediation-review-present-perfect-findings-in-agent-skills-asd-ste100-skill.md) — Approved, Ready, no dependencies.
26. **P0** — [20261127-173000-31: CI remediation — Review semicolon findings in .agent/skills/the-worker/references/document-type-catalog.md](tasks/20261127-173000/subtasks/31-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-references.md) — Approved, Ready, no dependencies.
27. **P0** — [20261127-173000-32: CI remediation — Review long-sentence findings in .agent/skills/the-worker/references/github-actions.md](tasks/20261127-173000/subtasks/32-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-referen.md) — Approved, Ready, no dependencies.
28. **P0** — [20261127-173000-33: CI remediation — Review present-perfect findings in .agent/SESSION\\\_START.md](tasks/20261127-173000/subtasks/33-ci-remediation-review-present-perfect-findings-in-agent-session-start-md.md) — Approved, Ready, no dependencies.
29. **P0** — [20261127-173000-34: CI remediation — Review synonym-rotation findings in workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md](tasks/20261127-173000/subtasks/34-ci-remediation-review-synonym-rotation-findings-in-workspace-adr-0003-canonical.md) — Approved, Ready, no dependencies.
30. **P0** — [20261127-173000-35: CI remediation — Review semicolon findings in workspace/TASK\\\_TEMPLATE.md](tasks/20261127-173000/subtasks/35-ci-remediation-review-semicolon-findings-in-workspace-task-template-md.md) — Approved, Ready, no dependencies.
31. **P0** — [20261127-173000-36: CI remediation — Review passive-voice findings in workspace/SUBTASK\\\_TEMPLATE.md](tasks/20261127-173000/subtasks/36-ci-remediation-review-passive-voice-findings-in-workspace-subtask-template-md.md) — Approved, Ready, no dependencies.
32. **P0** — [20261127-173000-37: CI remediation — Review semicolon findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md](tasks/20261127-173000/subtasks/37-ci-remediation-review-semicolon-findings-in-workspace-adr-0004-task-folders-sub.md) — Approved, Ready, no dependencies.
33. **P0** — [20261127-173000-38: CI remediation — Review passive-voice findings in workspace/TASK\\\_TEMPLATE.md](tasks/20261127-173000/subtasks/38-ci-remediation-review-passive-voice-findings-in-workspace-task-template-md.md) — Approved, Ready, no dependencies.
34. **P0** — [20261127-173000-39: CI remediation — Review synonym-rotation findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md](tasks/20261127-173000/subtasks/39-ci-remediation-review-synonym-rotation-findings-in-workspace-adr-0004-task-fold.md) — Approved, Ready, no dependencies.
35. **P0** — [20261127-173000-40: CI remediation — Review passive-voice findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md](tasks/20261127-173000/subtasks/40-ci-remediation-review-passive-voice-findings-in-workspace-adr-0004-task-folders.md) — Approved, Ready, no dependencies.
36. **P0** — [20261127-173000-41: CI remediation — Review long-sentence findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md](tasks/20261127-173000/subtasks/41-ci-remediation-review-long-sentence-findings-in-workspace-adr-0004-task-folders.md) — Approved, Ready, no dependencies.
37. **P0** — [20261127-173000-42: CI remediation — Review passive-voice findings in workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md](tasks/20261127-173000/subtasks/42-ci-remediation-review-passive-voice-findings-in-workspace-adr-0001-establish-dr.md) — Approved, Ready, no dependencies.
38. **P0** — [20261127-173000-43: CI remediation — Review semicolon findings in workspace/SUBTASK\\\_TEMPLATE.md](tasks/20261127-173000/subtasks/43-ci-remediation-review-semicolon-findings-in-workspace-subtask-template-md.md) — Approved, Ready, no dependencies.
39. **P0** — [20261127-173000-44: CI remediation — Review semicolon findings in workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md](tasks/20261127-173000/subtasks/44-ci-remediation-review-semicolon-findings-in-workspace-adr-0001-establish-draft.md) — Approved, Ready, no dependencies.
40. **P0** — [20261127-173000-45: CI remediation — Review semicolon findings in workspace/adr/README.md](tasks/20261127-173000/subtasks/45-ci-remediation-review-semicolon-findings-in-workspace-adr-readme-md.md) — Approved, Ready, no dependencies.
41. **P0** — [20261127-173000-46: CI remediation — Review passive-voice findings in .agent/skills/the-worker/references/conversation-mode.md](tasks/20261127-173000/subtasks/46-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md) — Approved, Ready, no dependencies.
42. **P1** — [20261127-173100-02: Audit document template coverage and create missing templates](tasks/20261127-173100/subtasks/02-audit-document-template-coverage.md) — Approved, Ready, no dependencies.
43. **P1** — [20261127-173000-04: Enforce template-first document editing](tasks/20261127-173000/subtasks/04-enforce-template-first-document-editing.md) — Approved, Ready, no dependencies.

## Next Task

[20261127-173000-05](tasks/20261127-173000/subtasks/05-ci-remediation-review-present-perfect-findings-in-agent-skills-agent-skill-auth.md) is next after the active P0 remediation child.

## Deferred Work

### Blocked

_No blocked tasks._

### Proposed — decision pending

_No proposed tasks._

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261127-173000-03 | Correct objective-based task parent selection | P1 | Paused | Approved | Remaining audit is deferred behind the current Refactor Skills consolidation. | [subtask](tasks/20261127-173000/subtasks/03-correct-objective-based-task-parent-selection.md) |

### Dependency-waiting

_No dependency-waiting tasks._
