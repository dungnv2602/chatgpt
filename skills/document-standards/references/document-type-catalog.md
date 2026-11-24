# Document Type Catalog

**Catalog version:** 1.13  
**Inventory status:** Non-truncated recursive tree audit of branch `gpt` at commit `1a5c8380036dac0132216635951f95a971ceee25` found 6,375 tree entries and 1,114 Markdown documents outside root `master/` and `archive/`. All 1,114 Markdown paths match the 48 Active coverage rules. Every rule matches at least one file. This is a complete path inventory and targeted family review, not a line-by-line semantic review of every generated report.
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
| Novel foundation | Template required | `novels/templates/novel-v1.1.md` | Current Version 1.1 template exists. |
| Novel open-discussion register | Template required | `novels/templates/open-discussion-v1.1.md` | One active register per novel. The Novel-02 example uses an approved-decision register and topic-grouped questions. Its relationship roadmap embeds proposal content. It has no separate deferred or resolved sections. |
| Character profile | Template required when created | `novels/templates/character-profile-v1.1.md` | Optional record. No current example was found in the inspected project records `novels/Novel-01/novel.md` and `novels/Novel-02/novel.md`. Do not create when the novel summary is sufficient. |
| Development outline | Template required when created | `novels/templates/development-outline-v1.1.md` | Optional focused planning record. `novels/Novel-02/planning/relationship-progression.md` is a current Version 1.1 topic-specific outline. Its section layout differs from the generic template. Preserve it and use the template for new records or material revisions. |
| Story arc | Template required when created | `novels/templates/arc-v1.1.md` | Current Version 1.1 template exists. |
| Scene | Template required when created | `novels/templates/scene-v1.1.md` | Current Version 1.1 template exists. Scene prose remains creative content. |
| Illustration note | Template required | `novels/templates/illustration-note-v1.1.md` | One record per retained or reviewed novel illustration. Six Version 1.0 examples exist across Novel-01 Scenes 002–005. Preserve them as legacy records. Use Version 1.1 for new notes or material revisions. |
| Illustration prompt record | Template required before generation | `novels/templates/illustration-prompt-v1.1.md` | Preserve chronological attempts and exact authored prompts. Three legacy prompt records exist in Novel-01 Scenes 003–005. Scene-003 declares Version 1.0. Scene-004 and Scene-005 use earlier layouts without version frontmatter. Preserve them and use Version 1.1 for new records. Repository handoff is conditional on an accepted output being uploaded. |
| Non-novel drawing attempt | Template required | `skills/drawing/assets/attempt-template.md` | Template version 1.1. Separates record, generation, and user-decision states. Includes required lineage, criteria, provenance, and per-output evidence. |
| Drawing pattern entry | Template required | `skills/drawing/assets/pattern-entry-templates.md` | Template version 1.1. Separate success and failure formats record evidence, confidence, and explicit user approval. Current examples remain in `skills/drawing/references/patterns/successful-patterns.md` and `skills/drawing/references/patterns/failure-patterns.md`. The Drawing Skill requires approval before each index change. |
| Historical drawing prompt indexes | Lightweight pattern | `drawings/history/successful-prompts.md` and `drawings/history/failed-prompts.md` | These are navigation indexes for historical attempts, not templates for new attempts. Keep the classification rules and source links. New attempts use the canonical drawing attempt template. |
| Historical conversation archive records | Lightweight pattern | `drawings/history/conversation-2026-11-12-intimacy-and-portrait.md` and `skills/the-worker/references/archive-records-and-image-prompts.md` | Historical indexes, transcript segments, and curated chronicles. No separate reusable template is needed. New conversation-integrity records use the Worker template. |
| Legacy standalone drawing prompt notes | Lightweight pattern | `drawings/history/cozy-bedroom-painterly-attempt-27-2026-11-12.md` and `skills/drawing/assets/attempt-template.md` | One-off historical prompt/attempt notes superseded by the canonical per-attempt record. Preserve them. Do not create new notes in this legacy form. |
| Drawing session brief | Template required | `skills/the-worker/assets/session-brief-template.md` | Template version 1.0. Status values are Active, Paused, and Closed. New sessions start Active. The reconstructed 2026-11-20 brief and the closed 2026-11-21 brief are preserved as legacy records. |
| Daily drawing index | Template required | `skills/drawing/assets/daily-index-template.md` | Template version 1.1. Defines the exact six-field table for attempt, session, lineage, execution, approval/evidence, and image. The 2026-11-19, 2026-11-20, and 2026-11-21 README indexes predate this version. |
| Conversation integrity record | Template required | `skills/the-worker/assets/conversation-integrity-template.md` | Copy-ready template now exists with gap and editorial-summary fields. The historical record `drawings/history/2026-11-12-conversation-integrity.md` predates the template and remains unchanged. |
| Session summary | Template required | `skills/the-worker/assets/session-summary-template.md` | Copy-ready handoff template now exists. The historical record `drawings/history/2026-11-12-summary.md` predates the template and remains unchanged. |
| Workspace task record | Template required | `workspace/TASK_TEMPLATE.md` | Template version 1.3. New implementation tasks require Governing ADR(s). The Worker owns task fields and closeout. The CI Ledger creates Proposed task records for newly identified actionable findings during report ingestion and maintains their finding links. It does not taskify the historical backlog. The active record remains In Progress / Archived: No until the archive copy passes full read-back. |

| Decision Draft | Template required | `workspace/DRAFT_TEMPLATE.md` | One proposal per decision. Require explicit user review and approval before promotion to an ADR. Preserve the promoted Draft as provenance. |
| Accepted Decision Record | Template required | `workspace/ADR_TEMPLATE.md` | MADR-inspired decision record. Create only after the user approves the exact Draft. Track decision status separately from implementation status. |
| Repository analysis | Template required | `workspace/ANALYSIS_TEMPLATE.md` | Evidence-based repository health snapshots at a fixed branch commit. Analysis does not authorize implementation and does not duplicate the CI Ledger. |
| Novel workspace index and workflow | Embedded contract | `novels/README.md` and `novels/WORKFLOW.md` | The README indexes projects and current templates. The workflow defines narrative hierarchy, status/canon, versioning, and template-first authoring. No separate template is needed. |
| Archive boundary policy | Embedded contract | `archive/README.md` and `skills/the-worker/SKILL.md` | Defines archive record structure, immutability, permitted exact reads, and batch retention. The README is read-only under the archive boundary. The retention workflow also exposes manual and workflow-call force triggers. See Open Discussions for policy confirmation. |
| Archive retention state | Embedded contract | `.github/scripts/cleanup-archive.py` and `.github/archive-retention-state.json` | The cleanup script writes the single `last_cleanup_at` timestamp. This is machine-owned operational state, not a user-authored record. Do not create a template. |
| Task board | Embedded contract | `skills/the-worker/SKILL.md` and `workspace/task_board.md` | One live index. No separate copy template is needed now. |
| Report navigation | Embedded contract | `reports/README.md`, `reports/lint_reports/README.md`, `reports/gh_ac_reports/README.md`, and `reports/triage/README.md` | The root index links the three report-family guides, which define their respective review surfaces and navigation. |
| Workspace navigation index | Embedded contract | `workspace/README.md`, `reports/README.md`, and report-family README files | Workspace README points to task navigation, lint evidence, and workflow diagnostics. Each report guide owns scope navigation and review order. These are live navigation and operating-contract documents. No separate copy template is needed. |
| Conversation Mode discussion register | Embedded contract | `skills/the-worker/SKILL.md`, `skills/the-worker/references/conversation-mode.md`, and `workspace/discussion.md` | The Worker owns the fixed headings, ordering, pre-step brief, open discussions, and success-report rules in both modes. |
| Image asset storage and WebP delivery | Embedded contract | `images/README.md` and `skills/the-worker/SKILL.md` | The Worker owns the shared archive, image-provenance, intake, and WebP procedures. One live README defines image storage, original-master retention, WebP derivatives, takeout, and report locations. No separate template is needed. |
| Image takeout hand-off | Schema required | `skills/the-worker/scripts/process_takeout.py` and `images/takeout/README.md` | The processor validates the YAML contract. `images/takeout/HANDOFF.yml` is the current draft example. `skills/the-worker/scripts/test_process_takeout_unittest.py` covers readiness, exact intake coverage, missing attempt metadata, malformed top-level data, duplicate output IDs, rollback, and hashes. |
| Drawing-session manifest | Generator-owned | `skills/the-worker/scripts/process_takeout.py` (`MANIFEST_FIELDS`) and `skills/the-worker/scripts/verify_published_manifest.py` | The processor defines columns, preserves existing columns, and adds missing fields. The publisher validates verification columns and published values. `skills/the-worker/scripts/test_process_takeout_unittest.py` covers legacy rows, missing columns, duplicate IDs, hashes, and publication links. |
| Conversion report | Generator-owned | `skills/the-worker/scripts/process_takeout.py` | Defines conversion CSV fields. |

| Document type | Class | Current canonical format | Inventory finding / next action |
|---|---|---|---|
| Publication verification | Generator-owned | `skills/the-worker/scripts/process_takeout.py` | Writes immutable reports. |
| GitHub Actions run and job diagnostics | Generator-owned | `reports/gh_ac_reports/scripts/report.py`, `reports/gh_ac_reports/assets/report-template.md`, `reports/gh_ac_reports/assets/report-schema.json`, and `reports/gh_ac_reports/scripts/test_report.py` | Captures actionable workflow failures and operational exceptions, including non-blocking failed steps. The report records workflow metadata, jobs, steps, annotations, artifact metadata, sanitized logs, indexes, latest pointers, and integrity manifests. Ordinary successful and cancellation-only runs are skipped by default. Cancelled runs with independent failures remain actionable. Explicit run-backfill requests can override the filter. Non-blocking composite-action finalizers and the push sweep collect monitored workflows. Detailed lint findings remain documented in `reports/lint_reports/README.md`. Update the template, schema, generator, tests, workflow integration, catalog, and owner guide together. |

| Agent Skill definition | Template required | `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Copy-ready `SKILL.md` template now exists. |
| Prompt framework templates | Template required when needed | `skills/prompt-master/assets/prompt-templates.md` | Copy-ready prompt architectures for specific AI tools. Load only the relevant template. |
| Skill index and activation files | Embedded contract | `skills/README.md`, `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md` | Each has a distinct ownership role. Do not force one generic index template. |
| GitHub Actions workflows | Exempt | `.github/workflows/validate-document-standards.yml` | Follow GitHub's workflow schema. |

| Document type | Class | Current canonical format | Inventory finding / next action |
|---|---|---|---|
| Master catalogues | Lightweight pattern | `master/Images.md` | Keep their project forms. |
| One-off creative, educational, and exploratory content | Exempt | `drawings/2026-11-19/TODO.md`, `drawings/2026-11-20/samantha-visual-drive.md`, `drawings/2026-11-20/scenario-direction.md`, `drawings/history/conversation-2026-11-11-sams-origin-and-wonderhome.md`, and `skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md` | These are one-off exploratory notes, a curated narrative chronicle, and a standalone study curriculum, not recurring record types. Preserve their content-specific structures. |

## Markdown inventory coverage

This register classifies every Markdown file outside root `master/` and `archive/`. The validator scans the repository tree but excludes those directories and Git metadata. Every in-scope Markdown path must match a rule below. Active rules must match a current file. Optional rules may match zero or more generated outputs. Reserved rules must match no current file before its first record appears. Add a narrow rule before creating a new document family. Do not add a broad catch-all to silence an uncovered-path error. The class describes the document family. The canonical authority identifies its template, schema, embedded contract, or generator.

Coverage status has three values. `Active` rules must match at least one in-scope Markdown file. `Reserved` rules must match no current file. Change a Reserved rule to Active in the commit that creates its first record. `Optional` rules apply only to `Generator-owned` outputs. They may match zero or more files, including after a clean reset or during a report period with no generated Markdown. The validator rejects Active rules with no matches. It also rejects Reserved rules that already match a document and Optional rules on any other class.

| Path pattern | Class | Coverage status | Canonical authority | Coverage rationale |
|---|---|---|---|---|
| `drawings/history/20??-??-??-conversation-integrity.md` | Template required | Active | `skills/the-worker/assets/conversation-integrity-template.md` | Historical conversation-integrity records. New records use the current template. Preserve old content without mass migration. |
| `drawings/history/20??-??-??-summary.md` | Template required | Active | `skills/the-worker/assets/session-summary-template.md` | Historical session summaries. New records use the current template. Preserve old content without mass migration. |
| `drawings/history/20??-??-??-image-prompts.md` | Lightweight pattern | Active | `skills/the-worker/references/archive-records-and-image-prompts.md` and `skills/drawing/assets/attempt-template.md` | Legacy chronological prompt logs. Do not create new logs. New attempts use one canonical attempt record each. |
| `drawings/history/conversation-*.md` | Lightweight pattern | Active | `skills/the-worker/references/archive-records-and-image-prompts.md` and `skills/the-worker/assets/conversation-integrity-template.md` | Historical archive indexes, transcript segments, and curated chronicles. They are legacy navigation/source records, not a new recurring document type. New session archives use the conversation-integrity template. |
| `drawings/history/cozy-bedroom-*.md` | Lightweight pattern | Active | `skills/the-worker/references/archive-records-and-image-prompts.md` and `skills/drawing/assets/attempt-template.md` | Legacy standalone prompt and attempt notes. Preserve as historical records. New drawing work uses the current attempt template. |
| `drawings/history/failed-prompts.md` | Lightweight pattern | Active | `skills/drawing/SKILL.md` and `skills/drawing/references/patterns/README.md` | Historical navigation index only. Not a template for new attempts. |
| `drawings/history/successful-prompts.md` | Lightweight pattern | Active | `skills/drawing/SKILL.md` and `skills/drawing/references/patterns/README.md` | Historical navigation index only. Not a template for new attempts. |
| `drawings/20??-??-??/README.md` | Template required | Active | `skills/drawing/assets/daily-index-template.md` | Daily drawing indexes. Use the canonical six-field index for new dates and material revisions. |
| `drawings/20??-??-??/attempt-*.md` | Template required | Active | `skills/drawing/assets/attempt-template.md` | One record per drawing attempt. Preserve legacy attempts without mass migration. |
| `drawings/20??-??-??/session-*-brief.md` | Template required | Active | `skills/the-worker/assets/session-brief-template.md` | One opening brief per distinct drawing session. |
| `drawings/2026-11-19/TODO.md` | Exempt | Active | `skills/drawing/SKILL.md` | One-off project TODO. Not a recurring record type. |
| `drawings/2026-11-20/samantha-visual-drive.md` | Exempt | Active | `skills/drawing/SKILL.md` | One-off creative visual reference. Preserve its project-specific form. |
| `drawings/2026-11-20/scenario-direction.md` | Exempt | Active | `skills/drawing/SKILL.md` | One-off film-grounded creative direction. Do not constrain it with a reusable template. |
| `images/README.md` | Embedded contract | Active | `images/README.md` and `skills/the-worker/SKILL.md` | Image storage, original-master retention, WebP derivatives, and repository delivery rules. |
| `images/takeout/README.md` | Embedded contract | Active | `images/takeout/README.md` and `skills/the-worker/scripts/process_takeout.py` | Takeout intake and processing procedure. The processor owns the YAML/CSV field contract. |
| `images/takeout/history/**/*.md` | Generator-owned | Optional | `skills/the-worker/scripts/process_takeout.py` and `skills/the-worker/scripts/test_process_takeout_unittest.py` | Generated per-attempt Takeout verification reports. History may be empty when no batch has run. |
| `novels/*.md` | Embedded contract | Active | `novels/README.md` and `novels/WORKFLOW.md` | Novel root navigation and project-wide narrative, canon, status, and versioning rules. |
| `novels/templates/*.md` | Exempt | Active | `novels/templates/scene-v1.1.md` | Canonical template source files, not authored novel records. Individual document types are catalogued separately. |
| `novels/*/novel.md` | Template required | Active | `novels/templates/novel-v1.1.md` | Novel foundation records. |
| `novels/*/open-discussion.md` | Template required | Active | `novels/templates/open-discussion-v1.1.md` | Per-novel open-discussion and approved-decision register. |
| `novels/*/planning/*.md` | Template required | Active | `novels/templates/development-outline-v1.1.md` | Focused novel planning and development outlines. Preserve existing topic-specific legacy structures until material revision. |
| `novels/*/*/arc.md` | Template required | Active | `novels/templates/arc-v1.1.md` | Story arc records. |
| `novels/*/*/Scene-*/scene.md` | Template required | Active | `novels/templates/scene-v1.1.md` | Scene records. Creative prose remains unconstrained by prose-style templates. |
| `novels/*/*/Scene-*/illustrations/illustration-*.md` | Template required | Active | `novels/templates/illustration-note-v1.1.md` and `novels/templates/illustration-prompt-v1.1.md` | Novel illustration notes and scene-local prompt/attempt records. Choose the matching type-specific template. |
| `reports/README.md` | Embedded contract | Active | `reports/README.md` and `reports/triage/README.md` | Central report navigation and family ownership. |
| `reports/**/README.md` | Embedded contract | Active | `reports/gh_ac_reports/README.md` and `reports/lint_reports/README.md` | Report-family guides and generated-report review procedures. |
| `reports/gh_ac_reports/assets/report-template.md` | Generator-owned | Active | `reports/gh_ac_reports/scripts/report.py` and `reports/gh_ac_reports/scripts/test_report.py` | Reporter-owned rendering asset. Update with generator and regression tests. |
| `reports/gh_ac_reports/history/**/*.md` | Generator-owned | Optional | `reports/gh_ac_reports/scripts/report.py` and `reports/gh_ac_reports/scripts/test_report.py` | Immutable per-run Markdown diagnostic captures. The family may be empty after a clean reset. |
| `reports/gh_ac_reports/by_workflow/*/latest-report.md` | Generator-owned | Optional | `reports/gh_ac_reports/scripts/report.py` and `reports/gh_ac_reports/scripts/test_report.py` | Generated workflow-specific latest pointers. They may be absent until a report is published. |
| `reports/gh_ac_reports/latest-gh-ac-report.md` | Generator-owned | Optional | `reports/gh_ac_reports/scripts/report.py` and `reports/gh_ac_reports/scripts/test_report.py` | Generated repository-wide latest diagnostic pointer. It may be absent until the first capture. |
| `reports/lint_reports/latest-lint-report.md` | Generator-owned | Optional | `skills/asd-ste100/scripts/generate_lint_report.py` and `skills/asd-ste100/scripts/test_generate_lint_report.py` | Generated compatibility pointer to the latest repository-wide lint report. It may be absent until the first lint report. |
| `reports/lint_reports/on_*/README.md` | Embedded contract | Active | `reports/lint_reports/README.md` and `skills/asd-ste100/SKILL.md` | Scope-specific lint evidence navigation. |
| `reports/lint_reports/on_*/latest-lint-report.md` | Generator-owned | Optional | `skills/asd-ste100/scripts/generate_lint_report.py` and `skills/asd-ste100/scripts/test_generate_lint_report.py` | Generated latest report for each lint scope. A scope may be empty after reset. |
| `reports/lint_reports/on_*/history/**/*.md` | Generator-owned | Optional | `skills/asd-ste100/scripts/generate_lint_report.py` and `skills/asd-ste100/scripts/test_generate_lint_report.py` | Immutable per-run lint reports. The family may be empty until a post-reset lint run. |
| `skills/README.md` | Embedded contract | Active | `skills/README.md` and `skills/SESSION_START.md` | Skill index and activation hierarchy. |
| `skills/INITIALIZATION_POLICY.md` | Embedded contract | Active | `skills/INITIALIZATION_POLICY.md` and `skills/SESSION_START.md` | Initialization source hierarchy and conditional loading rules. |
| `skills/SESSION_START.md` | Embedded contract | Active | `skills/SESSION_START.md` and `skills/INITIALIZATION_POLICY.md` | Explicit initialization cues and foundational load sequence. |
| `skills/*/SKILL.md` | Template required | Active | `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Every Agent Skill definition uses the canonical skill template for new definitions and material rewrites. |
| `skills/*/README.md` | Lightweight pattern | Active | `skills/README.md` and `skills/asd-ste100/references/repository-writing-policy.md` | Skill-specific navigation and technical documentation. Use type-specific headings. No universal README template. |
| `skills/*/CHANGELOG.md` | Lightweight pattern | Active | `skills/philosophy-religion-asceticism/CHANGELOG.md` | Concise version headings and change bullets. |
| `skills/*/assets/*.md` | Exempt | Active | `skills/document-standards/SKILL.md` and `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Canonical template/prompt assets themselves. They are not governed record instances. Their document types are covered by the main inventory. |
| `skills/*/references/*.md` | Lightweight pattern | Active | `skills/document-standards/SKILL.md` and `skills/asd-ste100/references/repository-writing-policy.md` | Technical references, policies, research notes, and workflow guidance. Use subject-specific structure. |
| `skills/*/references/**/*.md` | Lightweight pattern | Active | `skills/document-standards/SKILL.md` and `skills/drawing/references/patterns/README.md` | Nested technical references and drawing-pattern documentation. |
| `skills/*/examples/*.md` | Exempt | Active | `skills/asd-ste100/SKILL.md` | Worked examples and edge-case fixtures. Preserve their example-specific form. |
| `workspace/README.md` | Embedded contract | Active | `workspace/README.md` and `skills/the-worker/SKILL.md` | Workspace navigation and operating rules. |
| `workspace/task_board.md` | Embedded contract | Active | `workspace/task_board.md` and `skills/the-worker/SKILL.md` | One live task index. Its ADR(s) column links implementation tasks to accepted decisions. |
| `workspace/discussion.md` | Embedded contract | Active | `workspace/discussion.md` and `skills/the-worker/references/conversation-mode.md` | Shared current-step, open-discussion, and verified-report register. |
| `workspace/TASK_TEMPLATE.md` | Exempt | Active | `workspace/TASK_TEMPLATE.md` and `skills/the-worker/SKILL.md` | Canonical task template source, not a task instance. |
| `workspace/ADR_TEMPLATE.md` | Exempt | Active | `workspace/ADR_TEMPLATE.md` | Canonical accepted decision template source, not a decision record. |
| `workspace/ANALYSIS_TEMPLATE.md` | Exempt | Active | `workspace/ANALYSIS_TEMPLATE.md` | Canonical analysis template source, not an analysis record. |
| `workspace/DRAFT_TEMPLATE.md` | Exempt | Active | `workspace/DRAFT_TEMPLATE.md` | Canonical Draft template source, not a proposal record. |
| `workspace/tasks/*.md` | Template required | Active | `workspace/TASK_TEMPLATE.md` | Individual task records. |
| `workspace/analysis/README.md` | Embedded contract | Active | `skills/decision-governance/SKILL.md` and `workspace/analysis/README.md` | Repository-analysis navigation, review cadence, evidence requirements, and boundaries. |
| `workspace/analysis/ANALYSIS-20??Q?*.md` | Template required | Reserved | `workspace/ANALYSIS_TEMPLATE.md` | Quarterly and event-triggered repository analysis snapshots. Activate this rule with the first real analysis record. |
| `workspace/draft/README.md` | Embedded contract | Active | `skills/decision-governance/SKILL.md` and `workspace/draft/README.md` | Draft folder navigation, status transitions, and promotion rules. |
| `workspace/draft/DRAFT-*.md` | Template required | Active | `workspace/DRAFT_TEMPLATE.md` | One proposal record per decision. The first Draft is DRAFT-0001. |
| `workspace/adr/README.md` | Embedded contract | Active | `skills/decision-governance/SKILL.md` and `workspace/adr/README.md` | Accepted ADR navigation, status, implementation, and archive rules. |
| `workspace/adr/????-*.md` | Template required | Active | `workspace/ADR_TEMPLATE.md` | Accepted ADR records use a four-digit global ID in the filename. ADR-0001 is the first active decision record. |

## Validation coverage limits

The processor validates the hand-off when it processes a ready batch. Its regression suite covers important success and failure paths. Field-level tests cover invalid asset IDs, generation hashes, internal IDs, native IDs, approval values, and mapping evidence. A drawing-session upload test also asserts that provenance metadata reaches the generated manifest. Existing tests cover manifest backfill, custom-column preservation, published hashes, URLs, and attempt links.

The suite does not test every invalid value or every interaction between fields. Do not claim exhaustive schema coverage. The processor and its tests remain the schema authority. Do not create a second hand-off or manifest schema.

The processor and its tests remain the authority for the current YAML and CSV formats. A separate schema file is not required unless another consumer needs it or the processor adopts it.

## Existing versioned templates

The novel workspace has Version 1.1 templates for eight document types. It retains Version 1.0 templates for historical compatibility.

Do not mass-migrate untouched legacy novel records. Use the current template for new records and material revisions.

### Novel template field-contract audit

The eight Version 1.1 templates below were reviewed for required, conditional, optional, and repeatable content. Unless a field or subsection is explicitly marked Optional or Conditional, treat it as required under the Document Standards skill. Apply the shared `Unknown` and `Not applicable` conventions when evidence is missing or a field does not apply. Use each template's own enumerations for status and other controlled values.

| Template | Required baseline | Conditional content | Optional content | Repeatable structures / rules |
|---|---|---|---|---|
| `novel-v1.1.md` | Sections 1–14 and all unmarked fields | None | Chapter grouping within Structural Approach, Detailed Character Profile, Visual Reference, Detailed Development Outline, Detailed World References, Detailed Chronology Link, and Approved Decisions summary | Main Characters (use `None recorded` until established), Story Arc Directory rows (use `None recorded` until an arc exists), and dated events and revision entries |
| `open-discussion-v1.1.md` | Sections 1, 2, 4, and 7. Retain the Approved Decisions Register when it contains no decisions. | Keep only Open Questions subject headings that contain questions | Active Proposals (when they need a separate decision), Deferred Questions (when deliberately deferred), and Resolved or Superseded Items (when retention helps) | Decision rows, proposal blocks, and question entries. Use `None recorded` when no decision has been approved. |
| `character-profile-v1.1.md` | Sections 1–11 and all unmarked fields | None | None | Relationship rows (use `None recorded` when none are established). Use the shared missing/inapplicable-value convention for unknown or inapplicable details. |
| `development-outline-v1.1.md` | Sections 1–9 and all unmarked fields | None | None | Repeat the Progression / Components block for each stage. Use `None recorded` if no progression is ready. Component Status is separate from overall outline Status. |
| `arc-v1.1.md` | Sections 1–10 and all unmarked fields | None | None | Character Development blocks (use `None recorded` if none is established). Scene Directory rows (use `None planned` before any scene is planned). Retain the five narrative-progression subsections. |
| `scene-v1.1.md` | Sections 1–11 and all unmarked fields, including the complete Scene Prose section | None | None | Character entries and illustration rows (use `None recorded` if no illustration is planned or retained). Illustration assets must link to both the central-library master and WebP files. |
| `illustration-note-v1.1.md` | Sections 1–10 and all unmarked fields | Takeout filename/batch, stored master/WebP paths, hashes, and conversion/verification report links depend on the asset's intake and storage history. Use the field-specific `Not applicable` or `Not available` value shown in the template. | User Acceptance | Visual observations, continuity assessments, and review findings must reflect the actual returned asset |
| `illustration-prompt-v1.1.md` | Sections 1–5 and all unmarked fields. Record every attempt before submission and update it after the result. | Source Image for Edit applies only to a direct edit. Repository Asset Handoff applies only after an accepted output is uploaded to the novel asset library. | None | Append one complete chronological Attempt block per attempt. Never overwrite earlier attempts. |

This is a field-contract index, not a second copy of the templates. Exact field names, status enumerations, and section order remain authoritative in each linked template. Do not duplicate those definitions here or create a second schema.

## Representative records reviewed

| Document type | Representative record or inspected scope | Finding | Handling |
|---|---|---|---|
| Novel open-discussion register | `novels/Novel-02/open-discussion.md` | The Version 1.1 register has an approved-decision table, topic-grouped questions, and a current-status summary. Its relationship roadmap embeds proposal content rather than duplicating it in a separate proposal section. It has no separate deferred or resolved sections. | Preserve the active record. The canonical template now allows embedded proposals and marks separate proposal, deferred, and resolved sections as conditional. |
| Development outline | `novels/Novel-02/planning/relationship-progression.md` | Current Version 1.1 focused outline. It separates the approved broad direction from proposed dramatic beats and open questions, but its section layout is specific to this relationship progression. | Preserve the active record. Use the canonical template for new outlines and material revisions. |
| Master catalogues | `master/Images.md`, `master/Poses.md`, and `master/Prompts.md` | Images uses standalone prompt blocks, Poses mixes bullets and prose, and Prompts groups scene-specific prompt records. No common entry schema is justified. | Keep these as lightweight reference collections. Do not impose a uniform template. |
| Image asset directory contract | `images/README.md` | Defines storage, original-master retention, WebP delivery, intake, and report locations. | Keep the single live README as the embedded contract. |
| One-off creative references | `drawings/2026-11-19/TODO.md`, `drawings/2026-11-20/samantha-visual-drive.md`, and `drawings/2026-11-20/scenario-direction.md` | These are one-off exploratory or creative direction notes, not recurring record types. | Keep them exempt from rigid templates. |
| Novel workspace index and workflow | `novels/README.md` and `novels/WORKFLOW.md` | The README points to the current Version 1.1 standard. The workflow governs hierarchy, canon, status, versioning, and template use. | Keep both as the embedded contract. Do not create a generic README template. |
| Skill changelog | `skills/philosophy-religion-asceticism/CHANGELOG.md` | Uses version headings and concise change bullets. | Keep as a lightweight pattern. |
| Historical drawing prompt indexes | `drawings/history/successful-prompts.md` and `drawings/history/failed-prompts.md` | These indexes classify historical outcomes and link to source records. They are not templates for new attempts. | Preserve as historical navigation indexes. |
| One-off study curriculum | `skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md` | A standalone course plan with a flexible weekly sequence and assessment checkpoints. | Keep exempt from a recurring document template. |
| Drawing pattern entries | `skills/drawing/references/patterns/successful-patterns.md` and `skills/drawing/references/patterns/failure-patterns.md` | Current examples use separate success and failure structures. They distinguish observed results, hypotheses, evidence, confidence, and limitations. | Keep the indexes. Use the matching copy-ready pattern in `skills/drawing/assets/pattern-entry-templates.md`. |
| Character profile | Inspected `novels/Novel-01/novel.md` and `novels/Novel-02/novel.md` | No current character-profile record was found. | Keep this type optional. Do not create a profile only to populate the catalog. |
| Novel illustration prompt record | `novels/Novel-01/Arc-01/Scene-003/illustrations/illustration-01-prompt.md`, `novels/Novel-01/Arc-01/Scene-004/illustrations/illustration-01-prompt.md`, and `novels/Novel-01/Arc-01/Scene-005/illustrations/illustration-01-prompt.md` | Three legacy prompt records exist. Scene-003 declares Version 1.0. Scene-004 and Scene-005 have no version frontmatter and use earlier layouts. Scene-002 has no standalone prompt record. | Preserve existing records. Use the canonical Version 1.1 prompt template for new records and material revisions. |

## Legacy examples reviewed

The following records predate the current templates. Preserve them as historical records. Do not migrate them only to match a newer template.

| Document type | Representative records | Finding | Handling |
|---|---|---|---|
| Novel foundation, arc, and scene | `novels/Novel-01/novel.md`, `novels/Novel-01/Arc-01/arc.md`, `novels/Novel-01/Arc-01/Scene-001/scene.md` | These records declare format Version 1.0. The current templates use Version 1.1. | Keep untouched records at Version 1.0. Use Version 1.1 for new records and material revisions. |
| Non-novel drawing attempt | `drawings/2026-11-20/attempt-01.md`, `drawings/2026-11-21/attempt-17.md` | The older notes use earlier field layouts. Attempt 17 combines prompt-archive and generation-pending states in one status value. | Preserve existing notes. Use the Version 1.1 template with separate record, generation, and user-decision states for new records and material revisions. |
| Daily drawing index | `drawings/2026-11-19/README.md`, `drawings/2026-11-20/README.md`, and `drawings/2026-11-21/README.md` | These indexes predate the Version 1.1 six-field template. The 2026-11-21 index also uses a shorter legacy table. | Preserve existing indexes. Use the six-field template for new daily indexes and material revisions. |
| Drawing session brief | `drawings/2026-11-20/session-01-brief.md` and `drawings/2026-11-21/session-01-brief.md` | The 2026-11-20 brief was reconstructed from earlier notes. The 2026-11-21 brief records a closed session. Both preserve legacy structure. | Preserve them. New briefs use the canonical template and status values Active, Paused, and Closed. |
| Novel illustration notes | `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-01.md`, `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-02.md`, `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-03.md`, `novels/Novel-01/Arc-01/Scene-003/illustrations/illustration-01.md`, `novels/Novel-01/Arc-01/Scene-004/illustrations/illustration-01.md`, and `novels/Novel-01/Arc-01/Scene-005/illustrations/illustration-01.md` | All six records declare format Version 1.0 and predate the current Version 1.1 template. | Preserve the records. Use Version 1.1 for new notes and material revisions. |
| Session integrity and summary | `drawings/history/2026-11-12-conversation-integrity.md`, `drawings/history/2026-11-13-conversation-integrity.md`, `drawings/history/2026-11-12-summary.md`, and `drawings/history/2026-11-13-summary.md` | These historical records predate the standalone templates and use project-specific chronological and handoff structures. | Preserve them. Use the canonical templates for new records. |
| Historical novel templates | `novels/templates/novel-v1.md`, `novels/templates/arc-v1.md`, `novels/templates/scene-v1.md`, and `novels/templates/illustration-note-v1.md` | These Version 1.0 templates are superseded by the current Version 1.1 templates. | Preserve as historical references. New documents and material revisions use the current templates. |
| Early drawing attempt | `drawings/2026-11-19/attempt-01.md` | This record predates the Version 1.1 attempt template and uses an earlier free-form structure. | Preserve it. Use Version 1.1 for new attempts and material revisions. |
| Historical image-prompt logs | `drawings/history/2026-11-12-image-prompts.md`, `drawings/history/2026-11-13-image-prompts.md`, and `drawings/history/2026-11-16-image-prompts.md` | These chronological logs predate the current drawing-attempt template and preserve historical prompts and outcomes. | Preserve them as historical records. New attempts use the canonical attempt template. |
| Historical conversation indexes and transcript segments | `drawings/history/conversation-2026-11-12-intimacy-and-portrait.md`, `drawings/history/conversation-2026-11-12-starry-night-verbatim-available.md`, and `drawings/history/conversation-2026-11-12-verbatim-available-record.md` | These are legacy navigation/source records for past conversations, not a new recurring authoring type. | Preserve them. New conversation archive records use the conversation-integrity template and do not require separate index or transcript templates. |
| Legacy standalone drawing prompt notes | `drawings/history/cozy-bedroom-painterly-attempt-27-2026-11-12.md` and `drawings/history/cozy-bedroom-cream-cardigan-navy-polo-2026-11-12.md` | These standalone prompt notes predate the one-record-per-attempt workflow. | Preserve them. New drawing attempts use the canonical attempt template. |
| Novel illustration prompt records | `novels/Novel-01/Arc-01/Scene-003/illustrations/illustration-01-prompt.md`, `novels/Novel-01/Arc-01/Scene-004/illustrations/illustration-01-prompt.md`, and `novels/Novel-01/Arc-01/Scene-005/illustrations/illustration-01-prompt.md` | Scene-003 declares Version 1.0. Scene-004 and Scene-005 lack version frontmatter and use earlier custom layouts. | Preserve the historical records. Use the canonical Version 1.1 template for new prompt records and material revisions. |
| Workspace task record | `workspace/tasks/20261122-233900-enforce-template-first-document-standards.md` | This task record declares Template version 1.0. The current task template is Version 1.1. | Preserve the original task metadata. Use Version 1.1 for new task records. |
| Agent Skill definitions | Existing skill files under `skills/` | Many skills predate the reusable Agent Skill template. | Do not mass-convert existing skills. Use the canonical template for new skills and material rewrites. |

No new session summary or conversation-integrity record was required during this review. Their templates remain available for future sessions.

## Audit outcome

The full in-scope Markdown inventory has no recurring document family without a canonical template, schema, embedded contract, or generator-owned format. No additional standalone template was warranted. Existing canonical assets cover the recurring novel, drawing, session, conversation, task, skill, lint-report, workflow-report, and CI-ledger record types.

Historical daily indexes, reconstructed session briefs, chronological prompt logs, transcript/index records, and standalone legacy prompt notes remain unchanged. They are not new document types and must not be mass-migrated. One-off creative direction notes remain exempt. Generated report files remain generator-owned.

The validator enforces path-family coverage for Markdown. Machine-readable JSON, YAML, and CSV records remain governed by their exact schema, processor, generator, and regression-test entries in the Initial inventory. This Markdown path audit does not replace those validations.

## Catalog maintenance

When a recurring document type is added or changed:

1. Identify its owning skill or workflow.
2. Define its canonical template, schema, or embedded contract.
3. Add or update one document-type row and, for Markdown, one narrow path-coverage rule.
4. Link the canonical format from its owner index.
5. Define structural validation and migration rules.
6. Read back all changed paths.
7. Run the catalog validator and regression tests through the hosted Document Standards workflow. The validator enforces catalog integrity, exact references, template placement, and Markdown path coverage. It does not prove semantic document conformance. Do not run repository scripts locally.
