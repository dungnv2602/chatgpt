# Subtask: Workflow Map and Cue Registry

## Metadata
- **ID:** 20261127-173000-69
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit prior approval for workflow map, cue registry, map-first startup, and same-cycle maintenance; current execution cue and scoped startup P0 override.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / execution override:** User explicitly directed “Don't bother P0 CI, my order supersede, execute”. This skips startup P0 CI reconciliation for this deliverable only. No historical backfill, CI modification or hosted inspection authorized.
- **Required:** Yes
- **Created:** 2026-11-28
- **Updated:** 2026-11-28

## 1. Original Prompt
> My new cue: "/map" - you show me the map
> Create a map represents the current state of repo workflows. It must have everything in it. Use mermaid to draw the map. Every time you update the workflow, you must also update this map. Update your initiation to require you to read this map for workflow overview before reading related skills. Where do you place this map?

## 2. Subsequent Instructions
> Approve
> For your workflow, relocate then appropriately.
> Execute
> Don't bother P0 CI, my order supersede, execute

## 3. Objective and Acceptance Criteria
- Create canonical map at `.agent/WORKFLOW_MAP.md`.
- Define `/map` as display without initialization.
- Require `/start` to read map before related skill/reference loading.
- Require same-cycle map updates whenever workflows change.
- Readback changed files and commit on `gpt` with task trailer.

## 4. Progress
The user explicitly superseded the startup P0 CI reconciliation gate for this task only. No Ledger history was scanned/backfilled and hosted CI was not inspected.

## 5. Evidence
Readback and commit evidence will be recorded at closeout. No local scripts, tests or lint.

## 6. Handoff
Finish implementation, readback and tracking reconciliation. Leave the CI baseline discrepancy as separate deferred state.
