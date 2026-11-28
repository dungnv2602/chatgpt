# Workflow Map

**Purpose:** A navigable overview of current repository workflows. This map routes to canonical owners; it does not replace their procedures. Read it during `/start` before loading task-specific references. The `/map` cue displays this file without initializing the session.

## Session and repository work

```mermaid
flowchart TD
 A[Conversation] --> B{Cue or task activation}
 B -->|/start| C[Session Start guard] --> D[Read Workflow Map] --> E[The Worker] --> F[Conversation Mode: presentation only] --> G[Repository/task baseline and progressive loading] --> H[Workspace P0 and task reconciliation] --> I[Task / queue reconciliation] --> J[Authorized work to quiescence] --> K[Commit, readback and tracking] --> L[Closeout and queue continuation] --> M[Quiescence report]
 B -->|/map| N[Display map only]
 B -->|execute| O[Authorize prepared eligible batch]
 B -->|approve| P[Log decision only]
 B -->|Next| Q[Decision navigation only]
```

- Cue guard: `.agent/SESSION_START.md`; operating authority: `.agent/skills/the-worker/SKILL.md`.
- Presentation settings: `.agent/skills/the-worker/references/conversation-mode.md`.
- `/map` displays this map only; it does not initialize or execute.
- Standalone case-insensitive `execute` is the execution cue; approval and `Next` are log/navigation only.

## Task lifecycle and scheduling

```mermaid
flowchart TD
 A[Capture request and decisions] --> B[Objective-based parent]
 B --> C[Task / child from canonical template]
 C --> D[Reconcile parentage, dependencies, indexes and board]
 D --> E{Eligible and authorized?}
 E -->|No| F[Proposed / blocked / paused / dependency-waiting]
 E -->|Yes| G[Worker schedules within focus]
 G --> H[Autonomous implementation]
 H --> I[Commit with Task-ID trailer]
 I --> J[Readback and evidence]
 J --> K[Reconcile records and board]
 K --> L{Another eligible task?}
 L -->|Yes| G
 L -->|No| M[Quiescence and consolidated blocker brief]
```

- Task templates, subtask templates and board template: `.agent/skills/the-worker/assets/`.
- Board: `workspace/task_board.md`; records and indexes: `workspace/tasks/`.
- Drafts, analyses, ADRs and discussion registers: `workspace/decisions/`, governed by Worker decision-governance reference.
- Worker owns task capture, hierarchy, selection, blockers, commit evidence and closeout.

## Document and skill governance

```mermaid
flowchart TD
 A[Create or materially revise document] --> B[Document Type Catalog]
 B --> C[Identify type and canonical format]
 C --> D[Template / schema / embedded contract / generator]
 D --> E[Assess freshness; update canonical format first if needed]
 E --> F[Revise target and reconcile links/indexes]
 F --> G[Readback and permitted validation]
 G --> H[Commit; maintain map when workflow changes]
 I[Skill creation or revision] --> J[Skill template and skill index]
 J --> K[Owner references and activation boundaries]
```

- Catalog: `.agent/skills/the-worker/references/document-type-catalog.md`; reusable templates are in skill-owned `assets/`.
- Skill index: `.agent/skills/README.md`; skill authoring: `.agent/skills/agent-skill-authoring/`; Skill Creator has its specialized workflow.
- Novel/story: `.agent/skills/romantic-storyteller-visual-artist/` and `area/novel/`.
- Drawing: `.agent/skills/drawing/` (attempts, continuity, patterns, image editing, archive and delivery).
- Specialist skill activation is conditional and routed through the skill index and Worker gates.

## CI, reports and remediation

```mermaid
flowchart TD
 A[Workflow or report producer] --> B[Worker scripts and capture workflow]
 B --> C[Unified report index]
 C --> D[Published report and diagnostics]
 D --> E[CI Ledger: evidence, identity, attribution, state]
 E --> F[Attributed genuine task]
 F --> G[Remediation child and eligibility]
 G --> H[Worker scheduling and closeout]
 C --> I[On-demand report navigation]
```

- Activation: CI work is handled only for an assigned, selected task under `workspace/tasks/` and within its authorized scope. It is not part of general session initialization.
- Procedures: `.agent/skills/the-worker/references/ci-ledger.md` and `github-actions.md`, loaded only when the assigned CI task requires them.
- Canonical implementation: `.agent/skills/the-worker/scripts/`; capture workflow: `.github/workflows/gh-actions-capture.yml`.
- Report index and data: `.takeout/reports/`; navigation guide: `.takeout/reports/README.md`.
- No automatic startup CI baseline, report scan, or Ledger reconciliation. Do not access `.takeout/reports/` for general setup or unrelated tasks.
- Attribution is source-task-based, not guessed. The Ledger does not schedule or create parents.
- Historical backfill and hosted CI access remain governed; this map grants no permission.

## Image, drawing and takeout

```mermaid
flowchart TD
 A[Drawing session and attempt] --> B[Prompt, generation or edit]
 B --> C[User decision and accepted asset]
 C --> D[Archive and provenance]
 D --> E[WebP derivative and manifest]
 E --> F[Takeout preparation and validation]
 F --> G[Publication and verification reports]
 G --> H[Session index and closeout]
```

- Worker image procedures and focused drawing references own processing, provenance, storage and WebP.
- Drawing skill: `.agent/skills/drawing/`; image processing and verification scripts are routed from The Worker.

## Specialist routing

| Workflow | Entry / owner | Scope |
|---|---|---|
| Repository sessions, tasks, documents, decisions, CI | The Worker | Cross-cutting canonical operating authority |
| Skill creation / authoring | Agent Skill Authoring; Skill Creator | Creation, structure and bounded activation |
| Drawing / image iteration | Drawing | Attempt records, continuity, editing, patterns and delivery |
| Narrative / novel | Romantic Storyteller Visual Artist | Story hierarchy, arcs, scenes and illustration records |
| PDF | PDF skill | Form and reference procedures |
| Prompt design | Prompt Master | Prompt framework, templates and patterns |
| STE-100 writing / lint | ASD-STE100 | Writing rules and lint tooling |
| Visual themes | Theme Factory | Theme definitions and assets |
| Other specialist skills | `.agent/skills/README.md` | Activation requirements and scope |

## Map maintenance

Whenever a workflow, cue, owner boundary, activation prerequisite, or operational route changes, update this map in the same governed change cycle. Review it against owner files, read back both map and owners, and include the map in the commit. The map summarizes and routes; it does not duplicate detailed procedures or become a competing authority.
