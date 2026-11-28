# Document Type Catalog

**Catalog version:** 1.23
**Previous tree inventory:** The last recursive audit at commit `315615e944ed55925a6aa72c59fd6401bdcc912b` counted 297 Markdown files outside root `master/` and `workspace/archive/`. That historical count predates the ADR-0004 task-folder migration. This task did not run a new recursive inventory, catalog simulation, validator, or tests.
**Source branch:** `gpt`

This catalog maps recurring document types to their canonical formats. It distinguishes standalone templates from embedded contracts and generated formats. Skill-owned copy-ready templates belong in the owning skill's `assets/` directory. Explanatory references belong in `references/`. Project-level templates may use the owning project's designated template directory.

Do not create a second template when an owning workflow already defines the required format.

## Classification

| Class | Meaning |
|---|---|
| Template required | Copy a canonical template when creating the record. |
| Schema required | Follow a defined field schema and validate its values. |
| Embedded contract | Follow the format defined by one canonical live file, owning skill, README, workflow, or script. |
| Generator-owned | The generating script and its tests define the output format. |
| Lightweight pattern | Use a small consistent structure for a one-off or low-risk note. |
| Exempt | Do not force a template where creative freedom or an external format controls the content. |

## Initial inventory

| Document type | Class | Current canonical format | Inventory finding / next action |
|---|---|---|---|
| Novel foundation | Template required | `area/novel/templates/novel-v1.1.md` | Current Version 1.1 template exists. |
| Novel open-discussion register | Template required | `area/novel/templates/open-discussion-v1.1.md` | One active register per novel. The Novel-02 example uses an approved-decision register and topic-grouped questions. Its relationship roadmap embeds proposal content. It has no separate deferred or resolved sections. |
| Character profile | Template required when created | `area/novel/templates/character-profile-v1.1.md` | Optional record. The inspected project records `area/novel/Novel-01/novel.md` and `area/novel/Novel-02/novel.md` contain no current example. Do not create when the novel summary is sufficient. |
| Development outline | Template required when created | `area/novel/templates/development-outline-v1.1.md` | Optional focused planning record. `area/novel/Novel-02/planning/relationship-progression.md` is a current Version 1.1 topic-specific outline. Its section layout differs from the generic template. Preserve it and use the template for new records or material revisions. |
| Story arc | Template required when created | `area/novel/templates/arc-v1.1.md` | Current Version 1.1 template exists. |
| Scene | Template required when created | `area/novel/templates/scene-v1.1.md` | Current Version 1.1 template exists. Scene prose remains creative content. |
| Illustration note | Template required | `area/novel/templates/illustration-note-v1.1.md` | One record per retained or reviewed novel illustration. Six Version 1.0 examples exist across Novel-01 Scenes 002–005. Preserve them as legacy records. Use Version 1.1 for new notes or material revisions. |
| Illustration prompt record | Template required before generation | `area/novel/templates/illustration-prompt-v1.1.md` | Preserve chronological attempts and exact authored prompts. Three legacy prompt records exist in Novel-01 Scenes 003–005. Scene-003 declares Version 1.0. Scene-004 and Scene-005 use earlier layouts without version frontmatter. Preserve them and use Version 1.1 for new records. Complete the repository handoff only after you upload an accepted output. |
| Non-novel drawing attempt | Template required | `.agent/skills/drawing/assets/attempt-template.md` | Template version 1.1. Separates record, generation, and user-decision states. Includes required lineage, criteria, provenance, and per-output evidence. |
| Drawing pattern entry | Template required | `.agent/skills/drawing/assets/pattern-entry-templates.md` | Template version 1.1. Separate success and failure formats record evidence, confidence, and explicit user approval. Current examples remain in `.agent/skills/drawing/references/patterns/successful-patterns.md` and `.agent/skills/drawing/references/patterns/failure-patterns.md`. The Drawing Skill requires approval before each index change. |
| Historical drawing prompt indexes | Lightweight pattern | `area/drawing/history/successful-prompts.md` and `area/drawing/history/failed-prompts.md` | These are navigation indexes for historical attempts, not templates for new attempts. Keep the classification rules and source links. New attempts use the canonical drawing attempt template. |
| Historical conversation archive records | Lightweight pattern | `area/drawing/history/conversation-2026-11-12-intimacy-and-portrait.md` and `.agent/skills/the-worker/references/archive-records-and-image-prompts.md` | Historical indexes, transcript segments, and curated chronicles. Do not create a separate reusable template. New conversation-integrity records use the Worker template. |
| Legacy standalone drawing prompt notes | Lightweight pattern | `area/drawing/history/cozy-bedroom-painterly-attempt-27-2026-11-12.md` and `.agent/skills/drawing/assets/attempt-template.md` | One-off historical prompt/attempt notes superseded by the canonical per-attempt record. Preserve them. Do not create new notes in this legacy form. |
| Drawing session brief | Template required | `.agent/skills/the-worker/assets/session-brief-template.md` | Template version 1.0. Status values are Active, Paused, and Closed. New sessions start Active. Retain the reconstructed 2026-11-20 brief and the closed 2026-11-21 brief as legacy records. |
| Daily drawing index | Template required | `.agent/skills/drawing/assets/daily-index-template.md` | Template version 1.1. Defines the exact six-field table for attempt, session, lineage, execution, approval/evidence, and image. The 2026-11-19, 2026-11-20, and 2026-11-21 README indexes predate this version. |
| Conversation integrity record | Template required | `.agent/skills/the-worker/assets/conversation-integrity-template.md` | Copy-ready template now exists with gap and editorial-summary fields. The historical record `area/drawing/history/2026-11-12-conversation-integrity.md` predates the template and remains unchanged. |
| Session summary | Template required | `.agent/skills/the-worker/assets/session-summary-template.md` | Copy-ready handoff template now exists. The historical record `area/drawing/history/2026-11-12-summary.md` predates the template and remains unchanged. |
| Workspace task folder | Template required | `.agent/skills/the-worker/assets/TASK_TEMPLATE.md` | Version 2.5. One actionable objective per parent task; preserve its original prompt and subsequent instructions verbatim. Each folder contains task.md and subtasks/README.md. |
| Workspace subtask record | Template required | `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md` | Version 1.4. Each substantive follow-up or CI remediation has its own child prompt, parent ID, acceptance criteria, evidence, and completion record. CI children default to P0, Approved, Ready; a real decision gate may make a child Proposed. |

| Decision Draft | Template required | `.agent/skills/the-worker/assets/DRAFT_TEMPLATE.md` | Template version 1.2. One proposal per decision. Assess each materially viable option against explicit decision drivers. Include no-change when viable. For multiple viable options, use a qualitative comparative matrix and recommend one option against the strongest alternative. Record evidence provenance, source versions, dates, commits, confidence, and limitations. Distinguish facts, external claims, tests, inferences, and hypotheses. Do not invent scores or estimates. Require explicit user review and approval. After the Worker completes the completeness and read-back review for an accepted ADR, delete the source Draft. Keep its ID and revision as ADR provenance. Retain the source temporarily only when deletion fails, under Promotion Cleanup Pending. |
| Accepted Decision Record | Template required | `.agent/skills/the-worker/assets/ADR_TEMPLATE.md` | MADR-inspired decision record. Use promotion-pending only for the provisional promotion transaction. It is not accepted, must not appear in the accepted-decision index, and cannot govern a task. Change it to accepted only after the full rationale review and read-back both pass. Track decision status separately from implementation status. |
| Repository analysis | Template required | `.agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md` | Evidence-based repository health snapshots at a fixed branch commit. Analysis does not authorize implementation and does not duplicate the CI Ledger. |
| Novel workspace index and workflow | Embedded contract | `area/novel/README.md` and `area/novel/WORKFLOW.md` | The README indexes projects and current templates. The workflow defines narrative hierarchy, status/canon, versioning, and template-first authoring. Do not create a separate template. |
| Task board | Template required | `.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md` | The live board is the current schedule. Create or revise it from the canonical asset template. |
| Report navigation | Embedded contract | `.takeout/reports/README.md` | One guide defines the unified index, latest lint report, Ledger, history layout, and on-demand rendering. |
| Workspace navigation index | Embedded contract | `workspace/README.md` and `.takeout/reports/README.md` | Workspace README points to task navigation and unified CI evidence. The single report guide owns navigation and review order. |
| Conversation discussion register | Template required | `.agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md` | Register structure only. The Worker defines its operational contract and interaction rules. |
| Image asset storage and WebP delivery | Embedded contract | `.takeout/images/README.md` and `.agent/skills/the-worker/SKILL.md` | The Worker owns the shared archive, image-provenance, intake, and WebP procedures. One live README defines image storage, original-master retention, WebP derivatives, takeout, and report locations. Do not create a separate template. |
| Image takeout hand-off | Schema required | `.agent/skills/the-worker/scripts/process_takeout.py` and `.takeout/images/README.md` | The processor validates the YAML contract during batch preparation. The reconstructed tree contains no active hand-off file. The regression suite covers readiness, exact intake coverage, missing attempt metadata, malformed top-level data, duplicate output IDs, rollback, and hashes. |
| Drawing-session manifest | Generator-owned | `.agent/skills/the-worker/scripts/process_takeout.py` (`MANIFEST_FIELDS`) and `.agent/skills/the-worker/scripts/verify_published_manifest.py` | The processor defines columns, preserves existing columns, and adds missing fields. The publisher validates verification columns and published values. `.agent/skills/the-worker/scripts/test_process_takeout_unittest.py` covers legacy rows, missing columns, duplicate IDs, hashes, and publication links. |
| Conversion report | Generator-owned | `.agent/skills/the-worker/scripts/process_takeout.py` | Defines conversion CSV fields. |

| Document type | Class | Current canonical format | Inventory finding / next action |
|---|---|---|---|
| Publication verification | Generator-owned | `.agent/skills/the-worker/scripts/process_takeout.py` | Writes immutable reports. |
| GitHub Actions run and job diagnostics | Generator-owned | `.agent/skills/the-worker/scripts/actions-report.py`, `.agent/skills/the-worker/assets/actions-report-template.md`, `.agent/skills/the-worker/assets/actions-report-schema.json`, and `.agent/skills/the-worker/scripts/test_actions-report.py` | Captures actionable workflow failures and operational exceptions. The generator stores canonical JSON and sanitized logs under the shared history root, updates the unified index, and renders Markdown on demand. It preserves error-only eligibility, cancellation handling, explicit backfill rules, and independent failure classification. Detailed lint findings use the same index and history root. |

| Agent Skill definition | Template required | `.agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Copy-ready `SKILL.md` template now exists. |
| Prompt framework templates | Template required when needed | `.agent/skills/prompt-master/assets/prompt-templates.md` | Copy-ready prompt architectures for specific AI tools. Load only the relevant template. |
| Skill index and activation files | Embedded contract | `.agent/skills/README.md`, `.agent/SESSION_START.md`, `.agent/INITIALIZATION_POLICY.md` | Each has a distinct ownership role. Do not force one generic index template. |
| PDF processing guides | Lightweight pattern | `.agent/skills/pdf/FORMS.md` and `.agent/skills/pdf/REFERENCE.md` | The PDF Skill links these focused form-filling and advanced processing references. Preserve their subject-specific structures. |
| Skill Creator agent instructions | Embedded contract | `.agent/skills/skill-creator/SKILL.md` and `.agent/skills/agent-skill-authoring/SKILL.md` | Specialized role prompts support the Skill Creator workflow. Preserve each agent's bounded responsibilities. |
| Theme definitions | Lightweight pattern | `.agent/skills/theme-factory/themes/arctic-frost.md` | Theme files define named palettes and font pairings. Preserve each theme's values and structure. |
| GitHub Actions workflows | Exempt | `.github/workflows/validate-document-standards.yml` | Follow GitHub's workflow schema. |

| Document type | Class | Current canonical format | Inventory finding / next action |
|---|---|---|---|
| Master catalogues | Lightweight pattern | `master/Images.md` | Keep their project forms. |
| One-off creative, educational, and exploratory content | Exempt | `area/drawing/2026-11-19/TODO.md`, `area/drawing/2026-11-20/samantha-visual-drive.md`, `area/drawing/2026-11-20/scenario-direction.md`, `area/drawing/history/conversation-2026-11-11-sams-origin-and-wonderhome.md`, and `.agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md` | These are one-off exploratory notes, a curated narrative chronicle, and a standalone study curriculum, not recurring record types. Preserve their content-specific structures. |

## Markdown inventory coverage

This register classifies every Markdown file outside root `master/`. The validator scans the repository tree but excludes that directory and Git metadata. Every in-scope Markdown path must match a rule below. Active rules must match a current file. Optional rules may match zero or more generated outputs. Reserved rules must match no current file before its first record appears. Add a narrow rule before creating a new document family. Do not add a broad catch-all to silence an uncovered-path error. The class describes the document family. The canonical authority identifies its template, schema, embedded contract, or generator.

Coverage status has three values. `Active` rules must match at least one in-scope Markdown file. `Reserved` rules must match no current file. Change a Reserved rule to Active in the commit that creates its first record. `Optional` rules apply only to `Generator-owned` outputs. They may match zero or more files, including after a clean reset or during a report period with no generated Markdown. The validator rejects Active rules with no matches. It also rejects Reserved rules that already match a document and Optional rules on any other class.

| Path pattern | Class | Coverage status | Canonical authority | Coverage rationale |
|---|---|---|---|---|
| `area/drawing/history/20??-??-??-conversation-integrity.md` | Template required | Active | `.agent/skills/the-worker/assets/conversation-integrity-template.md` | Historical conversation-integrity records. New records use the current template. Preserve old content without mass migration. |
| `area/drawing/history/20??-??-??-summary.md` | Template required | Active | `.agent/skills/the-worker/assets/session-summary-template.md` | Historical session summaries. New records use the current template. Preserve old content without mass migration. |
| `area/drawing/history/20??-??-??-image-prompts.md` | Lightweight pattern | Active | `.agent/skills/the-worker/references/archive-records-and-image-prompts.md` and `.agent/skills/drawing/assets/attempt-template.md` | Legacy chronological prompt logs. Do not create new logs. New attempts use one canonical attempt record each. |
| `area/drawing/history/conversation-*.md` | Lightweight pattern | Active | `.agent/skills/the-worker/references/archive-records-and-image-prompts.md` and `.agent/skills/the-worker/assets/conversation-integrity-template.md` | Historical archive indexes, transcript segments, and curated chronicles. They are legacy navigation/source records, not a new recurring document type. New session archives use the conversation-integrity template. |
| `area/drawing/history/cozy-bedroom-*.md` | Lightweight pattern | Active | `.agent/skills/the-worker/references/archive-records-and-image-prompts.md` and `.agent/skills/drawing/assets/attempt-template.md` | Legacy standalone prompt and attempt notes. Preserve as historical records. New drawing work uses the current attempt template. |
| `area/drawing/history/failed-prompts.md` | Lightweight pattern | Active | `.agent/skills/drawing/SKILL.md` and `.agent/skills/drawing/references/patterns/README.md` | Historical navigation index only. Not a template for new attempts. |
| `area/drawing/history/successful-prompts.md` | Lightweight pattern | Active | `.agent/skills/drawing/SKILL.md` and `.agent/skills/drawing/references/patterns/README.md` | Historical navigation index only. Not a template for new attempts. |
| `area/drawing/20??-??-??/README.md` | Template required | Active | `.agent/skills/drawing/assets/daily-index-template.md` | Daily drawing indexes. Use the canonical six-field index for new dates and material revisions. |
| `area/drawing/20??-??-??/attempt-*.md` | Template required | Active | `.agent/skills/drawing/assets/attempt-template.md` | One record per drawing attempt. Preserve legacy attempts without mass migration. |
| `area/drawing/20??-??-??/session-*-brief.md` | Template required | Active | `.agent/skills/the-worker/assets/session-brief-template.md` | One opening brief per distinct drawing session. |
| `area/drawing/2026-11-19/TODO.md` | Exempt | Active | `.agent/skills/drawing/SKILL.md` | One-off project TODO. Not a recurring record type. |
| `area/drawing/2026-11-20/samantha-visual-drive.md` | Exempt | Active | `.agent/skills/drawing/SKILL.md` | One-off creative visual reference. Preserve its project-specific form. |
| `area/drawing/2026-11-20/scenario-direction.md` | Exempt | Active | `.agent/skills/drawing/SKILL.md` | One-off film-grounded creative direction. Do not constrain it with a reusable template. |
| `.takeout/images/README.md` | Embedded contract | Active | `.takeout/images/README.md`, `.agent/skills/the-worker/SKILL.md`, and `.agent/skills/the-worker/scripts/process_takeout.py` | Image storage, original-master retention, WebP derivatives, intake and processing procedure. The processor owns the YAML/CSV field contract. |
| `.takeout/images/history/**/*.md` | Generator-owned | Optional | `.agent/skills/the-worker/scripts/process_takeout.py` and `.agent/skills/the-worker/scripts/test_process_takeout_unittest.py` | Generated per-attempt Takeout verification reports. History may remain empty until a batch runs. |
| `area/novel/*.md` | Embedded contract | Active | `area/novel/README.md` and `area/novel/WORKFLOW.md` | Novel root navigation and project-wide narrative, canon, status, and versioning rules. |
| `area/novel/templates/*.md` | Exempt | Active | `area/novel/templates/scene-v1.1.md` | Canonical template source files, not authored novel records. The catalog lists individual document types separately. |
| `area/novel/*/novel.md` | Template required | Active | `area/novel/templates/novel-v1.1.md` | Novel foundation records. |
| `area/novel/*/open-discussion.md` | Template required | Active | `area/novel/templates/open-discussion-v1.1.md` | Per-novel open-discussion and approved-decision register. |
| `area/novel/*/planning/*.md` | Template required | Active | `area/novel/templates/development-outline-v1.1.md` | Focused novel planning and development outlines. Preserve existing topic-specific legacy structures until material revision. |
| `area/novel/*/*/arc.md` | Template required | Active | `area/novel/templates/arc-v1.1.md` | Story arc records. |
| `area/novel/*/*/Scene-*/scene.md` | Template required | Active | `area/novel/templates/scene-v1.1.md` | Scene records. Creative prose remains unconstrained by prose-style templates. |
| `area/novel/*/*/Scene-*/illustrations/illustration-*.md` | Template required | Active | `area/novel/templates/illustration-note-v1.1.md` and `area/novel/templates/illustration-prompt-v1.1.md` | Novel illustration notes and scene-local prompt/attempt records. Choose the matching type-specific template. |
| `.takeout/reports/README.md` | Embedded contract | Active | `.takeout/reports/README.md` | Sole CI report navigation and operating guide. |

| `.agent/skills/README.md` | Embedded contract | Active | `.agent/skills/README.md` and `.agent/SESSION_START.md` | Skill index and activation hierarchy. |
| `.agent/INITIALIZATION_POLICY.md` | Embedded contract | Active | `.agent/INITIALIZATION_POLICY.md` and `.agent/SESSION_START.md` | Initialization source hierarchy and conditional loading rules. |
| `.agent/SESSION_START.md` | Embedded contract | Active | `.agent/SESSION_START.md` and `.agent/INITIALIZATION_POLICY.md` | Explicit initialization cues and foundational load sequence. |
| `.agent/skills/pdf/FORMS.md` | Lightweight pattern | Active | `.agent/skills/pdf/SKILL.md` | PDF form-filling instructions for the PDF skill. |
| `.agent/skills/pdf/REFERENCE.md` | Lightweight pattern | Active | `.agent/skills/pdf/SKILL.md` | Extended PDF library and command reference. |
| `.agent/skills/skill-creator/agents/*.md` | Embedded contract | Active | `.agent/skills/skill-creator/SKILL.md` and `.agent/skills/agent-skill-authoring/SKILL.md` | Role-specific agent instructions used by the Skill Creator workflow. |
| `.agent/skills/theme-factory/themes/*.md` | Lightweight pattern | Active | `.agent/skills/theme-factory/SKILL.md` | Named theme specifications. Preserve their color palettes and typography pairings. |
| `.agent/skills/*/SKILL.md` | Template required | Active | `.agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Every Agent Skill definition uses the canonical skill template for new definitions and material rewrites. |
| `.agent/skills/*/README.md` | Lightweight pattern | Active | `.agent/skills/README.md` and `.agent/skills/asd-ste100/references/repository-writing-policy.md` | Skill-specific navigation and technical documentation. Use type-specific headings. No universal README template. |
| `.agent/skills/*/CHANGELOG.md` | Lightweight pattern | Active | `.agent/skills/philosophy-religion-asceticism/CHANGELOG.md` | Concise version headings and change bullets. |
| `.agent/skills/*/assets/*.md` | Exempt | Active | `.agent/skills/the-worker/SKILL.md` and `.agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Canonical template/prompt assets themselves. They do not represent governed records. The main inventory covers their document types. |
| `.agent/skills/*/references/*.md` | Lightweight pattern | Active | `.agent/skills/the-worker/SKILL.md` and `.agent/skills/asd-ste100/references/repository-writing-policy.md` | Technical references, policies, research notes, and workflow guidance. Use subject-specific structure. |
| `.agent/skills/*/references/**/*.md` | Lightweight pattern | Active | `.agent/skills/the-worker/SKILL.md` and `.agent/skills/drawing/references/patterns/README.md` | Nested technical references and drawing-pattern documentation. |
| `.agent/skills/*/examples/*.md` | Exempt | Active | `.agent/skills/asd-ste100/SKILL.md` | Worked examples and edge-case fixtures. Preserve their example-specific form. |
| `workspace/README.md` | Embedded contract | Active | `workspace/README.md` and `.agent/skills/the-worker/SKILL.md` | Workspace navigation and operating rules. |
| `workspace/task_board.md` | Embedded contract | Active | `workspace/task_board.md` and `.agent/skills/the-worker/SKILL.md` | One live scheduler view: Current Execution, ranked eligible queue, Next Task, and deferred categories. Its ADR(s) column links implementation tasks to accepted decisions; the Worker remains sole scheduler. |
| `workspace/discussion.md` | Embedded contract | Active | `workspace/discussion.md` and `.agent/skills/the-worker/references/conversation-mode.md` | Shared current-step, open-discussion, and verified-report register. |
| `.agent/skills/the-worker/assets/TASK_TEMPLATE.md` | Exempt | Active | `.agent/skills/the-worker/assets/TASK_TEMPLATE.md` and `.agent/skills/the-worker/SKILL.md` | Canonical task template source, not a task instance. |
| `.agent/skills/the-worker/assets/ADR_TEMPLATE.md` | Exempt | Active | `.agent/skills/the-worker/assets/ADR_TEMPLATE.md` | Canonical accepted decision template source, not a decision record. |
| `.agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md` | Exempt | Active | `.agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md` | Canonical analysis template source, not an analysis record. |
| `.agent/skills/the-worker/assets/DRAFT_TEMPLATE.md` | Exempt | Active | `.agent/skills/the-worker/assets/DRAFT_TEMPLATE.md` | Canonical Draft template source, not a proposal record. |
| `workspace/tasks/*/task.md` | Template required | Active | `.agent/skills/the-worker/assets/TASK_TEMPLATE.md` v2.4 | Authoritative parent record. Every task folder also contains `subtasks/README.md`. Parent Done requires every required child Done. |
| `workspace/tasks/*/subtasks/README.md` | Embedded contract | Active | `workspace/tasks/*/subtasks/README.md` and `.agent/skills/the-worker/SKILL.md` | Required child index. Link the parent task and list every child subtask. |
| `workspace/tasks/*/subtasks/[0-9][0-9]-*.md` | Template required | Active | `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md` v1.3 | Child subtask records. Each record has a stable ID, parent ID, type, status, acceptance criteria, evidence, and completion record. |
| `workspace/analysis/README.md` | Embedded contract | Active | `.agent/skills/the-worker/references/decision-governance.md` and `workspace/analysis/README.md` | Repository-analysis navigation, review cadence, evidence requirements, and boundaries. |
| `workspace/analysis/ANALYSIS-20??Q?*.md` | Template required | Reserved | `.agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md` | Quarterly and event-triggered repository analysis snapshots. Activate this rule with the first real analysis record. |
| `workspace/draft/README.md` | Embedded contract | Active | `.agent/skills/the-worker/references/decision-governance.md` and `workspace/draft/README.md` | Draft folder navigation, status transitions, and promotion rules. |
| `workspace/draft/DRAFT-*.md` | Template required | Active | `.agent/skills/the-worker/assets/DRAFT_TEMPLATE.md` | One proposal record per decision. Delete the source after verified ADR promotion. Use Promotion Cleanup Pending only when deletion fails after acceptance. The first Draft is DRAFT-0001. |
| `workspace/adr/README.md` | Embedded contract | Active | `.agent/skills/the-worker/references/decision-governance.md` and `workspace/adr/README.md` | Accepted ADR navigation, status, and implementation rules. |
| `workspace/adr/????-*.md` | Template required | Active | `.agent/skills/the-worker/assets/ADR_TEMPLATE.md` | Global four-digit ADR records. The repository retains ADR-0001 and ADR-0002 as completed historical records in this flat folder. ADR-0003 and ADR-0004 record accepted decisions. Their implementation work or confirmation remains in progress. Provisional promotion-pending records are non-authoritative and must pass the completeness/read-back gate before acceptance. Only accepted records govern implementation tasks. |

## Validation coverage limits

The processor validates the hand-off when it processes a ready batch. Its regression suite covers important success and failure paths. Field-level tests cover invalid asset IDs, generation hashes, internal IDs, native IDs, approval values, and mapping evidence. A drawing-session upload test also asserts that provenance metadata reaches the generated manifest. Existing tests cover manifest backfill, custom-column preservation, published hashes, URLs, and attempt links.

The suite does not test every invalid value or every interaction between fields. Do not claim exhaustive schema coverage. The processor and its tests remain the schema authority. Do not create a second hand-off or manifest schema.

The processor and its tests remain the authority for the current YAML and CSV formats. A separate schema file is not required unless another consumer needs it or the processor adopts it.

## Existing versioned templates

The novel workspace has Version 1.1 templates for eight document types. It retains Version 1.0 templates for historical compatibility.

Do not mass-migrate untouched legacy novel records. Use the current template for new records and material revisions.

### Novel template field-contract audit

This review covers the eight Version 1.1 templates below and their required, conditional, optional, and repeatable content. Unless a field or subsection is explicitly marked Optional or Conditional, treat it as required under the Worker's document-governance procedure. Apply the shared `Unknown` and `Not applicable` conventions when evidence is missing or a field does not apply. Use each template's own enumerations for status and other controlled values.

| Template | Required baseline | Conditional content | Optional content | Repeatable structures / rules |
|---|---|---|---|---|
| `novel-v1.1.md` | Sections 1–14 and all unmarked fields | None | Chapter grouping within Structural Approach, Detailed Character Profile, Visual Reference, Detailed Development Outline, Detailed World References, Detailed Chronology Link, and Approved Decisions summary | Main Characters (use `None recorded` until established), Story Arc Directory rows (use `None recorded` until an arc exists), and dated events and revision entries |
| `open-discussion-v1.1.md` | Sections 1, 2, 4, and 7. Retain the Approved Decisions Register when it contains no decisions. | Keep only Open Questions subject headings that contain questions | Active Proposals (when they need a separate decision), Deferred Questions (when deliberately deferred), and Resolved or Superseded Items (when retention helps) | Decision rows, proposal blocks, and question entries. Use `None recorded` when the register contains no approved decision. |
| `character-profile-v1.1.md` | Sections 1–11 and all unmarked fields | None | None | Relationship rows (use `None recorded` when the profile lists no relationships). Use the shared missing/inapplicable-value convention for unknown or inapplicable details. |
| `development-outline-v1.1.md` | Sections 1–9 and all unmarked fields | None | None | Repeat the Progression / Components block for each stage. Use `None recorded` if no progression is ready. Component Status is separate from overall outline Status. |
| `arc-v1.1.md` | Sections 1–10 and all unmarked fields | None | None | Character Development blocks (use `None recorded` if the arc defines none). Scene Directory rows (use `None planned` before the author plans a scene). Retain the five narrative-progression subsections. |
| `scene-v1.1.md` | Sections 1–11 and all unmarked fields, including the complete Scene Prose section | None | None | Character entries and illustration rows (use `None recorded` when the scene has no planned or retained illustration). Illustration assets must link to both the central-library master and WebP files. |
| `illustration-note-v1.1.md` | Sections 1–10 and all unmarked fields | Takeout filename/batch, stored master/WebP paths, hashes, and conversion/verification report links depend on the asset's intake and storage history. Use the field-specific `Not applicable` or `Not available` value shown in the template. | User Acceptance | Visual observations, continuity assessments, and review findings must reflect the actual returned asset |
| `illustration-prompt-v1.1.md` | Sections 1–5 and all unmarked fields. Record every attempt before submission and update it after the result. | Source Image for Edit applies only to a direct edit. Repository Asset Handoff applies only after the user uploads an accepted output to the novel asset library. | None | Append one complete chronological Attempt block per attempt. Never overwrite earlier attempts. |

This is a field-contract index, not a second copy of the templates. Exact field names, status enumerations, and section order remain authoritative in each linked template. Do not duplicate those definitions here or create a second schema.

## Representative records reviewed

| Document type | Representative record or inspected scope | Finding | Handling |
|---|---|---|---|
| Novel open-discussion register | `area/novel/Novel-02/open-discussion.md` | The Version 1.1 register has an approved-decision table, topic-grouped questions, and a current-status summary. Its relationship roadmap embeds proposal content rather than duplicating it in a separate proposal section. It has no separate deferred or resolved sections. | Preserve the active record. The canonical template now allows embedded proposals and marks separate proposal, deferred, and resolved sections as conditional. |
| Development outline | `area/novel/Novel-02/planning/relationship-progression.md` | Current Version 1.1 focused outline. It separates the approved broad direction from proposed dramatic beats and open questions, but its section layout is specific to this relationship progression. | Preserve the active record. Use the canonical template for new outlines and material revisions. |
| Master catalogues | `master/Images.md`, `master/Poses.md`, and `master/Prompts.md` | Images uses standalone prompt blocks, Poses mixes bullets and prose, and Prompts groups scene-specific prompt records. These collections do not justify a common entry schema. | Keep these as lightweight reference collections. Do not impose a uniform template. |
| Image asset directory contract | `.takeout/images/README-1.md` | Defines storage, original-master retention, WebP delivery, intake, and report locations. | Keep the single live README as the embedded contract. |
| One-off creative references | `area/drawing/2026-11-19/TODO.md`, `area/drawing/2026-11-20/samantha-visual-drive.md`, and `area/drawing/2026-11-20/scenario-direction.md` | These are one-off exploratory or creative direction notes, not recurring record types. | Keep them exempt from rigid templates. |
| Novel workspace index and workflow | `area/novel/README.md` and `area/novel/WORKFLOW.md` | The README points to the current Version 1.1 standard. The workflow governs hierarchy, canon, status, versioning, and template use. | Keep both as the embedded contract. Do not create a generic README template. |
| Skill changelog | `.agent/skills/philosophy-religion-asceticism/CHANGELOG.md` | Uses version headings and concise change bullets. | Keep as a lightweight pattern. |
| Historical drawing prompt indexes | `area/drawing/history/successful-prompts.md` and `area/drawing/history/failed-prompts.md` | These indexes classify historical outcomes and link to source records. They are not templates for new attempts. | Preserve as historical navigation indexes. |
| One-off study curriculum | `.agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md` | A standalone course plan with a flexible weekly sequence and assessment checkpoints. | Keep exempt from a recurring document template. |
| Drawing pattern entries | `.agent/skills/drawing/references/patterns/successful-patterns.md` and `.agent/skills/drawing/references/patterns/failure-patterns.md` | Current examples use separate success and failure structures. They distinguish observed results, hypotheses, evidence, confidence, and limitations. | Keep the indexes. Use the matching copy-ready pattern in `.agent/skills/drawing/assets/pattern-entry-templates.md`. |
| Character profile | Inspected `area/novel/Novel-01/novel.md` and `area/novel/Novel-02/novel.md` | The review found no current character-profile record. | Keep this type optional. Do not create a profile only to populate the catalog. |
| Novel illustration prompt record | `area/novel/Novel-01/Arc-01/Scene-003/illustrations/illustration-01-prompt.md`, `area/novel/Novel-01/Arc-01/Scene-004/illustrations/illustration-01-prompt.md`, and `area/novel/Novel-01/Arc-01/Scene-005/illustrations/illustration-01-prompt.md` | Three legacy prompt records exist. Scene-003 declares Version 1.0. Scene-004 and Scene-005 have no version frontmatter and use earlier layouts. Scene-002 has no standalone prompt record. | Preserve existing records. Use the canonical Version 1.1 prompt template for new records and material revisions. |

## Legacy examples reviewed

The following records predate the current templates. Preserve them as historical records. Do not migrate them only to match a newer template.

| Document type | Representative records | Finding | Handling |
|---|---|---|---|
| Novel foundation, arc, and scene | `area/novel/Novel-01/novel.md`, `area/novel/Novel-01/Arc-01/arc.md`, `area/novel/Novel-01/Arc-01/Scene-001/scene.md` | These records declare format Version 1.0. The current templates use Version 1.1. | Keep untouched records at Version 1.0. Use Version 1.1 for new records and material revisions. |
| Non-novel drawing attempt | `area/drawing/2026-11-20/attempt-01.md`, `area/drawing/2026-11-21/attempt-17.md` | The older notes use earlier field layouts. Attempt 17 combines prompt-archive and generation-pending states in one status value. | Preserve existing notes. Use the Version 1.1 template with separate record, generation, and user-decision states for new records and material revisions. |
| Daily drawing index | `area/drawing/2026-11-19/README.md`, `area/drawing/2026-11-20/README.md`, and `area/drawing/2026-11-21/README.md` | These indexes predate the Version 1.1 six-field template. The 2026-11-21 index also uses a shorter legacy table. | Preserve existing indexes. Use the six-field template for new daily indexes and material revisions. |
| Drawing session brief | `area/drawing/2026-11-20/session-01-brief.md` and `area/drawing/2026-11-21/session-01-brief.md` | The 2026-11-20 brief uses a reconstruction from earlier notes. The 2026-11-21 brief records a closed session. Both preserve legacy structure. | Preserve them. New briefs use the canonical template and status values Active, Paused, and Closed. |
| Novel illustration notes | `area/novel/Novel-01/Arc-01/Scene-002/illustrations/illustration-01.md`, `area/novel/Novel-01/Arc-01/Scene-002/illustrations/illustration-02.md`, `area/novel/Novel-01/Arc-01/Scene-002/illustrations/illustration-03.md`, `area/novel/Novel-01/Arc-01/Scene-003/illustrations/illustration-01.md`, `area/novel/Novel-01/Arc-01/Scene-004/illustrations/illustration-01.md`, and `area/novel/Novel-01/Arc-01/Scene-005/illustrations/illustration-01.md` | All six records declare format Version 1.0 and predate the current Version 1.1 template. | Preserve the records. Use Version 1.1 for new notes and material revisions. |
| Session integrity and summary | `area/drawing/history/2026-11-12-conversation-integrity.md`, `area/drawing/history/2026-11-13-conversation-integrity.md`, `area/drawing/history/2026-11-12-summary.md`, and `area/drawing/history/2026-11-13-summary.md` | These historical records predate the standalone templates and use project-specific chronological and handoff structures. | Preserve them. Use the canonical templates for new records. |
| Historical novel templates | `area/novel/templates/novel-v1.md`, `area/novel/templates/arc-v1.md`, `area/novel/templates/scene-v1.md`, and `area/novel/templates/illustration-note-v1.md` | The current Version 1.1 templates replace these Version 1.0 templates. | Preserve as historical references. New documents and material revisions use the current templates. |
| Early drawing attempt | `area/drawing/2026-11-19/attempt-01.md` | This record predates the Version 1.1 attempt template and uses an earlier free-form structure. | Preserve it. Use Version 1.1 for new attempts and material revisions. |
| Historical image-prompt logs | `area/drawing/history/2026-11-12-image-prompts.md`, `area/drawing/history/2026-11-13-image-prompts.md`, and `area/drawing/history/2026-11-16-image-prompts.md` | These chronological logs predate the current drawing-attempt template and preserve historical prompts and outcomes. | Preserve them as historical records. New attempts use the canonical attempt template. |
| Historical conversation indexes and transcript segments | `area/drawing/history/conversation-2026-11-12-intimacy-and-portrait.md`, `area/drawing/history/conversation-2026-11-12-starry-night-verbatim-available.md`, and `area/drawing/history/conversation-2026-11-12-verbatim-available-record.md` | These are legacy navigation/source records for past conversations, not a new recurring authoring type. | Preserve them. New conversation archive records use the conversation-integrity template and do not require separate index or transcript templates. |
| Legacy standalone drawing prompt notes | `area/drawing/history/cozy-bedroom-painterly-attempt-27-2026-11-12.md` and `area/drawing/history/cozy-bedroom-cream-cardigan-navy-polo-2026-11-12.md` | These standalone prompt notes predate the one-record-per-attempt workflow. | Preserve them. New drawing attempts use the canonical attempt template. |
| Novel illustration prompt records | `area/novel/Novel-01/Arc-01/Scene-003/illustrations/illustration-01-prompt.md`, `area/novel/Novel-01/Arc-01/Scene-004/illustrations/illustration-01-prompt.md`, and `area/novel/Novel-01/Arc-01/Scene-005/illustrations/illustration-01-prompt.md` | Scene-003 declares Version 1.0. Scene-004 and Scene-005 lack version frontmatter and use earlier custom layouts. | Preserve the historical records. Use the canonical Version 1.1 template for new prompt records and material revisions. |
| Legacy workspace task record | No retained active flat record. The Worker deletes completed task records at closeout. | Active task records now use ID folders. The Worker deletes completed task records after closeout validation. | Do not restore or create active flat task notes. New active task records use `.agent/skills/the-worker/assets/TASK_TEMPLATE.md` Version 2.0. |
| Agent Skill definitions | Existing skill files under `.agent/skills/` | Many skills predate the reusable Agent Skill template. | Do not mass-convert existing skills. Use the canonical template for new skills and material rewrites. |

This review did not require a new session summary or conversation-integrity record. Their templates remain available for future sessions.

## Audit outcome

The full in-scope Markdown inventory has no recurring document family without a canonical template, schema, embedded contract, or generator-owned format. The review found no reason to add another standalone template. Existing canonical assets cover the recurring novel, drawing, session, conversation, task, skill, unified CI report and CI-ledger record types.

Historical daily indexes, reconstructed session briefs, chronological prompt logs, transcript/index records, and standalone legacy prompt notes remain unchanged. They are not new document types and must not be mass-migrated. One-off creative direction notes remain exempt. Generated report files remain generator-owned.

The validator enforces path-family coverage for Markdown. Machine-readable JSON, YAML, and CSV records remain governed by their exact schema, processor, generator, and regression-test entries in the Initial inventory. This Markdown path audit does not replace those validations.

## Catalog maintenance

When you add or change a recurring document type:

1. Identify its owning skill or workflow.
2. Define its canonical template, schema, or embedded contract.
3. Add or update one document-type row and, for Markdown, one narrow path-coverage rule.
4. Link the canonical format from its owner index.
5. Define structural validation and migration rules.
6. Read back all changed paths.
7. Run the catalog validator and regression tests through the hosted Document Standards workflow. The validator enforces catalog integrity, exact references, template placement, and Markdown path coverage. It does not prove semantic document conformance. Do not run repository scripts locally.
