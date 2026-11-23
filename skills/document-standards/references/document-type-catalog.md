# Document Type Catalog

**Catalog version:** 1.2  
**Inventory status:** The initial recursive tree review enumerated 417 files (483 entries). The final read-back enumerated 420 files (488 entries). Neither tree was truncated. Candidate template/schema files, all skill reference files, and their owners were inspected. The user-authorized audit included read-only review of the two archived task records. This is a complete path inventory and a targeted content audit, not a line-by-line review of every repository file.  
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
| Novel open-discussion register | Template required | `novels/templates/open-discussion-v1.1.md` | One active register per novel. The Novel-02 example uses an approved-decision register and topic-grouped questions; its relationship roadmap embeds proposal content, with no separate deferred or resolved sections. |
| Character profile | Template required when created | `novels/templates/character-profile-v1.1.md` | Optional record. No current example was found in the inspected project records `novels/Novel-01/novel.md` and `novels/Novel-02/novel.md`. Do not create when the novel summary is sufficient. |
| Development outline | Template required when created | `novels/templates/development-outline-v1.1.md` | Optional focused planning record. `novels/Novel-02/planning/relationship-progression.md` is a current Version 1.1, topic-specific outline whose section layout differs from the generic template; preserve it and use the template for new records or material revisions. |
| Story arc | Template required when created | `novels/templates/arc-v1.1.md` | Current Version 1.1 template exists. |
| Scene | Template required when created | `novels/templates/scene-v1.1.md` | Current Version 1.1 template exists. Scene prose remains creative content. |
| Illustration note | Template required | `novels/templates/illustration-note-v1.1.md` | One record per retained or reviewed novel illustration. Six Version 1.0 examples exist across Novel-01 Scenes 002–005; preserve them as legacy records and use Version 1.1 for new notes or material revisions. |
| Illustration prompt record | Template required before generation | `novels/templates/illustration-prompt-v1.1.md` | Preserve chronological attempts and exact authored prompts. Three legacy prompt records exist in Novel-01 Scenes 003–005; Scene-003 declares Version 1.0, while Scene-004 and Scene-005 use earlier layouts without version frontmatter. Preserve them and use Version 1.1 for new records. Repository handoff is conditional on an accepted output being uploaded. |
| Non-novel drawing attempt | Template required | `skills/drawing/assets/attempt-template.md` | Template version 1.1. Separates record, generation, and user-decision states. Includes required lineage, criteria, provenance, and per-output evidence. |
| Drawing pattern entry | Template required | `skills/drawing/assets/pattern-entry-templates.md` | Template version 1.0. Separate copy-ready formats cover successful and failure patterns, evidence, and confidence rules. Current examples remain in `skills/drawing/references/patterns/successful-patterns.md` and `skills/drawing/references/patterns/failure-patterns.md`. |
| Historical drawing prompt indexes | Lightweight pattern | `drawings/history/successful-prompts.md` and `drawings/history/failed-prompts.md` | These are navigation indexes for historical attempts, not templates for new attempts. Keep the classification rules and source links; new attempts use the canonical drawing attempt template. |
| Drawing session brief | Template required | `skills/session-archiving/assets/session-brief-template.md` | Template version 1.0. Status values are Active, Paused, and Closed. New sessions start Active. |
| Daily drawing index | Template required | `skills/drawing/assets/daily-index-template.md` | Template version 1.1. Defines the exact six-field table for attempt, session, lineage, execution, approval/evidence, and image. |
| Conversation integrity record | Template required | `skills/session-archiving/assets/conversation-integrity-template.md` | Copy-ready template now exists with gap and editorial-summary fields. The historical record `drawings/history/2026-11-12-conversation-integrity.md` predates the template and remains unchanged. |
| Session summary | Template required | `skills/session-archiving/assets/session-summary-template.md` | Copy-ready handoff template now exists. The historical record `drawings/history/2026-11-12-summary.md` predates the template and remains unchanged. |
| Workspace task record | Template required | `workspace/TASK_TEMPLATE.md` | Template version 1.1. The Worker owns task fields and closeout. The active record remains In Progress / Archived: No until the archive copy passes full read-back. |
| Novel workspace index and workflow | Embedded contract | `novels/README.md` and `novels/WORKFLOW.md` | The README indexes projects and current templates; the workflow defines narrative hierarchy, status/canon, versioning, and template-first authoring. No separate template is needed. |
| Archive boundary policy | Embedded contract | `archive/README.md` and `skills/session-archiving/SKILL.md` | Defines archive record structure, immutability, permitted exact reads, and batch retention. The README is read-only under the archive boundary. The retention workflow also exposes manual and workflow-call force triggers; see Open Discussions for policy confirmation. |
| Archive retention state | Embedded contract | `.github/scripts/cleanup-archive.py` and `.github/archive-retention-state.json` | The cleanup script writes the single `last_cleanup_at` timestamp. This is machine-owned operational state, not a user-authored record; do not create a template. |
| Task board | Embedded contract | `skills/the-worker/SKILL.md` and `workspace/task_board.md` | One live index. No separate copy template is needed now. |
| Report navigation | Embedded contract | `reports/README.md`, `reports/lint_reports/README.md`, `reports/gh_ac_reports/README.md`, and `reports/triage/README.md` | The root index links the three report-family guides, which define their respective review surfaces and navigation. |
| Workspace navigation index | Embedded contract | `workspace/README.md`, `reports/README.md`, and report-family README files | Workspace README points to task navigation, lint evidence, and workflow diagnostics. Each report guide owns scope navigation and review order. These are live navigation and operating-contract documents; no separate copy template is needed. |
| Conversation Mode discussion register | Embedded contract | `skills/conversation-mode/SKILL.md` and `workspace/discussion.md` | Fixed headings, ordering, and entry rules. The register applies in Default Mode and Condensed Mode. |
| Image asset storage and WebP delivery | Embedded contract | `images/README.md` and `skills/session-archiving/SKILL.md` | The session-archiving skill owns the workflow; one live README defines image storage, original-master retention, WebP derivatives, takeout, and report locations. No separate template is needed. |
| Image takeout hand-off | Schema required | `skills/session-archiving/scripts/process_takeout.py` and `images/takeout/README.md` | The processor validates the YAML contract; `images/takeout/HANDOFF.yml` is the current draft example. `skills/session-archiving/scripts/test_process_takeout_unittest.py` covers readiness, exact intake coverage, missing attempt metadata, malformed top-level data, duplicate output IDs, rollback, and hashes. |
| Drawing-session manifest | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`MANIFEST_FIELDS`) and `skills/session-archiving/scripts/verify_published_manifest.py` | The processor defines columns, preserves existing columns, and adds missing fields. The publisher checks verification columns and published values. `skills/session-archiving/scripts/test_process_takeout_unittest.py` covers legacy rows, missing columns, duplicate IDs, hashes, and publication links. |
| Conversion report CSV | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`FIELDS`) | The processor defines the output columns and writes one report row per input image. `skills/session-archiving/scripts/test_process_takeout_unittest.py` checks report creation and source, staging, and final paths. |
| Publication verification report | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`write_reports`) and `skills/session-archiving/scripts/verify_published_manifest.py` | The report generator writes fixed sections for checks and errors. `skills/session-archiving/scripts/test_process_takeout_unittest.py` covers published asset, URL, README, and attempt-link outcomes. |
| Repository-wide and changed-document STE lint reports | Generator-owned | `skills/asd-ste100/scripts/generate_lint_report.py`, `skills/asd-ste100/assets/lint-report-template.md`, `skills/asd-ste100/assets/lint-report-schema.json`, and `skills/asd-ste100/scripts/test_generate_lint_report.py` | Both workflows use one generator and one schema. The generator owns exact coverage, complete per-file diagnostics, check evidence, baseline comparisons, indexes, latest pointers, and integrity manifests for both scopes. Tests cover both scopes and report history. Update the template, schema, generator, tests, catalog, and owner documentation together. |
| Central report triage ledger | Generator-owned | `reports/triage/scripts/ledger.py`, `reports/triage/ledger-schema.json`, and `reports/triage/scripts/test_ledger.py` | The generator validates and updates the machine-readable ledger from indexed immutable lint and GitHub Actions reports. The schema defines the record contract, and regression tests cover identity, lifecycle, idempotency, and safe publication. The operator guide is `reports/triage/README.md`. |
| GitHub Actions run and job diagnostics | Generator-owned | `reports/gh_ac_reports/scripts/report.py`, `reports/gh_ac_reports/assets/report-template.md`, `reports/gh_ac_reports/assets/report-schema.json`, and `reports/gh_ac_reports/scripts/test_report.py` | Captures workflow metadata, jobs, steps, check annotations, artifact metadata, sanitized logs, failure classifications, pre-finalizer and post-run evidence, indexes, latest pointers, and integrity manifests. Non-blocking composite-action finalizers and the push sweep collect monitored workflows. Detailed lint findings remain documented in `reports/lint_reports/README.md`. Update the template, schema, generator, tests, workflow integration, catalog, and owner guide together. |

| Agent Skill definition | Template required | `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Copy-ready `SKILL.md` template now exists. |
| Prompt framework templates | Template required when needed | `skills/prompt-master/assets/prompt-templates.md` | Copy-ready prompt architectures for specific AI tools. Load only the relevant template. |
| Skill index and activation files | Embedded contract | `skills/README.md`, `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md` | Each has a distinct ownership role. Do not force one generic index template. |
| GitHub Actions workflow definitions | Exempt | `.github/workflows/archive-retention.yml`, `.github/workflows/convert-images-to-webp.yml`, `.github/workflows/notification.yml`, `.github/workflows/ste-lint-changed.yml`, `.github/workflows/ste-lint-full-docs.yml`, `.github/workflows/gh-actions-diagnostics.yml` | Workflow YAML follows GitHub Actions' external schema. Use workflow-specific validation and the GitHub Actions skill; do not invent a project template. |
| Master image, pose, and prompt catalogues | Lightweight pattern | `master/Images.md`, `master/Poses.md`, `master/Prompts.md` | Reviewed. Images contains standalone prompt blocks, Poses mixes bullet ideas and prose, and Prompts groups scene-specific prompt records. Their structures are heterogeneous; do not impose one shared entry schema. |
| Technical skill references | Lightweight pattern | `skills/asd-ste100/SKILL.md`, `skills/asd-ste100/README.md`, `skills/asd-ste100/references/repository-writing-policy.md`, `skills/drawing/README.md`, `skills/philosophy-religion-asceticism/README.md`, `skills/prompt-master/README.md`, and owning-skill references | Also includes `skills/prompt-master/references/patterns.md`. Use type-specific headings; no universal section layout is appropriate. |
| Skill changelog | Lightweight pattern | `skills/philosophy-religion-asceticism/CHANGELOG.md` | Keep version headings and concise change bullets. No full template is needed for this single skill changelog. |
| One-off creative, educational, and exploratory content | Exempt | `drawings/2026-11-19/TODO.md`, `drawings/2026-11-20/samantha-visual-drive.md`, `drawings/2026-11-20/scenario-direction.md`, `drawings/history/conversation-2026-11-11-sams-origin-and-wonderhome.md`, and `skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md` | These are one-off exploratory notes, a curated narrative chronicle, and a standalone study curriculum, not recurring record types. Preserve their content-specific structures. |

## Validation coverage limits

The processor validates the hand-off when it processes a ready batch. Its regression suite covers important success and failure paths. Field-level cases now check invalid asset IDs, generation hashes, internal IDs, native IDs, approval values, and mapping evidence. A drawing-session upload test also checks that provenance metadata reaches the generated manifest. Existing tests cover manifest backfill, custom-column preservation, published hashes, URLs, and attempt links.

The suite does not test every invalid value or every interaction between fields. Do not claim exhaustive schema coverage. The processor and its tests remain the schema authority. Do not create a second hand-off or manifest schema.

The processor and its tests remain the authority for the current YAML and CSV formats. A separate schema file is not required unless another consumer needs it or the processor adopts it.

## Existing versioned templates

The novel workspace has Version 1.1 templates for eight document types. It retains Version 1.0 templates for historical compatibility.

Do not mass-migrate untouched legacy novel records. Use the current template for new records and material revisions.

### Novel template field-contract audit

The eight Version 1.1 templates below were reviewed for required, conditional, optional, and repeatable content. Unless a field or subsection is explicitly marked Optional or Conditional, treat it as required under the Document Standards skill. Apply the shared `Unknown` and `Not applicable` conventions when evidence is missing or a field does not apply. Use each template's own enumerations for status and other controlled values.

| Template | Required baseline | Conditional content | Optional content | Repeatable structures / rules |
|---|---|---|---|---|
| `novel-v1.1.md` | Sections 1–14 and all unmarked fields | None | Chapter grouping within Structural Approach; Detailed Character Profile; Visual Reference; Detailed Development Outline; Detailed World References; Detailed Chronology Link; Approved Decisions summary | Main Characters (use `None recorded` until established); Story Arc Directory rows (use `None recorded` until an arc exists); dated events and revision entries |
| `open-discussion-v1.1.md` | Sections 1, 2, 4, and 7; retain the Approved Decisions Register even when it contains no decisions | Keep only Open Questions subject headings that contain questions | Active Proposals (only when a proposal needs a separate decision); Deferred Questions (only when deliberately deferred); Resolved or Superseded Items (only when retention is useful) | Decision rows, proposal blocks, and question entries; use `None recorded` when no decision has been approved |
| `character-profile-v1.1.md` | Sections 1–11 and all unmarked fields | None | None | Relationship rows (use `None recorded` when none are established); use the shared missing/inapplicable-value convention for unknown or inapplicable details |
| `development-outline-v1.1.md` | Sections 1–9 and all unmarked fields | None | None | Repeat the Progression / Components block for each stage; use `None recorded` if no progression is ready; component Status is separate from overall outline Status |
| `arc-v1.1.md` | Sections 1–10 and all unmarked fields | None | None | Character Development blocks (use `None recorded` if none is established); Scene Directory rows (use `None planned` before any scene is planned); retain the five narrative-progression subsections |
| `scene-v1.1.md` | Sections 1–11 and all unmarked fields, including the complete Scene Prose section | None | None | Character entries and illustration rows (use `None recorded` if no illustration is planned or retained); illustration assets must link to both the central-library master and WebP files |
| `illustration-note-v1.1.md` | Sections 1–10 and all unmarked fields | Takeout filename/batch, stored master/WebP paths, hashes, and conversion/verification report links depend on the asset's intake and storage history; use the field-specific `Not applicable` or `Not available` value shown in the template | User Acceptance | Visual observations, continuity assessments, and review findings must reflect the actual returned asset |
| `illustration-prompt-v1.1.md` | Sections 1–5 and all unmarked fields; record every attempt before submission and update it after the result | Source Image for Edit applies only to a direct edit; Repository Asset Handoff applies only after an accepted output is uploaded to the novel asset library | None | Append one complete chronological Attempt block per attempt; never overwrite earlier attempts |

This is a field-contract index, not a second copy of the templates. Exact field names, status enumerations, and section order remain authoritative in each linked template. Do not duplicate those definitions here or create a second schema.

## Representative records reviewed

| Document type | Representative record or inspected scope | Finding | Handling |
|---|---|---|---|
| Novel open-discussion register | `novels/Novel-02/open-discussion.md` | The Version 1.1 register has an approved-decision table, topic-grouped questions, and a current-status summary. Its relationship roadmap embeds proposal content rather than duplicating it in a separate proposal section; no separate deferred or resolved sections are present. | Preserve the active record. The canonical template now allows embedded proposals and marks separate proposal, deferred, and resolved sections as conditional. |
| Development outline | `novels/Novel-02/planning/relationship-progression.md` | Current Version 1.1 focused outline. It separates the approved broad direction from proposed dramatic beats and open questions, but its section layout is specific to this relationship progression. | Preserve the active record. Use the canonical template for new outlines and material revisions. |
| Master catalogues | `master/Images.md`; `master/Poses.md`; `master/Prompts.md` | Images uses standalone prompt blocks, Poses mixes bullets and prose, and Prompts groups scene-specific prompt records. No common entry schema is justified. | Keep these as lightweight reference collections. Do not impose a uniform template. |
| Image asset directory contract | `images/README.md` | Defines storage, original-master retention, WebP delivery, intake, and report locations. | Keep the single live README as the embedded contract. |
| One-off creative references | `drawings/2026-11-19/TODO.md`; `drawings/2026-11-20/samantha-visual-drive.md`; `drawings/2026-11-20/scenario-direction.md` | These are one-off exploratory or creative direction notes, not recurring record types. | Keep them exempt from rigid templates. |
| Novel workspace index and workflow | `novels/README.md`; `novels/WORKFLOW.md` | The README points to the current Version 1.1 standard; the workflow governs hierarchy, canon, status, versioning, and template use. | Keep both as the embedded contract; do not create a generic README template. |
| Skill changelog | `skills/philosophy-religion-asceticism/CHANGELOG.md` | Uses version headings and concise change bullets. | Keep as a lightweight pattern. |
| Historical drawing prompt indexes | `drawings/history/successful-prompts.md`; `drawings/history/failed-prompts.md` | These indexes classify historical outcomes and link to source records; they are not templates for new attempts. | Preserve as historical navigation indexes. |
| One-off study curriculum | `skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md` | A standalone course plan with a flexible weekly sequence and assessment checkpoints. | Keep exempt from a recurring document template. |
| Drawing pattern entries | `skills/drawing/references/patterns/successful-patterns.md`; `skills/drawing/references/patterns/failure-patterns.md` | Current examples use separate success and failure structures. They distinguish observed results, hypotheses, evidence, confidence, and limitations. | Keep the indexes. Use the matching copy-ready pattern in `skills/drawing/assets/pattern-entry-templates.md`. |
| Character profile | Inspected `novels/Novel-01/novel.md` and `novels/Novel-02/novel.md` | No current character-profile record was found. | Keep this type optional. Do not create a profile only to populate the catalog. |
| Novel illustration prompt record | `novels/Novel-01/Arc-01/Scene-003/illustrations/illustration-01-prompt.md`; `novels/Novel-01/Arc-01/Scene-004/illustrations/illustration-01-prompt.md`; `novels/Novel-01/Arc-01/Scene-005/illustrations/illustration-01-prompt.md` | Three legacy prompt records exist. Scene-003 declares Version 1.0; Scene-004 and Scene-005 have no version frontmatter and use earlier layouts. Scene-002 has no standalone prompt record. | Preserve existing records. Use the canonical Version 1.1 prompt template for new records and material revisions. |

## Legacy examples reviewed

The following records predate the current templates. Preserve them as historical records. Do not migrate them only to match a newer template.

| Document type | Representative records | Finding | Handling |
|---|---|---|---|
| Novel foundation, arc, and scene | `novels/Novel-01/novel.md`, `novels/Novel-01/Arc-01/arc.md`, `novels/Novel-01/Arc-01/Scene-001/scene.md` | These records declare format Version 1.0. The current templates use Version 1.1. | Keep untouched records at Version 1.0. Use Version 1.1 for new records and material revisions. |
| Non-novel drawing attempt | `drawings/2026-11-20/attempt-01.md`, `drawings/2026-11-21/attempt-17.md` | The older notes use earlier field layouts. Attempt 17 combines prompt-archive and generation-pending states in one status value. | Preserve existing notes. Use the Version 1.1 template with separate record, generation, and user-decision states for new records and material revisions. |
| Daily drawing index | `drawings/2026-11-20/README.md`, `drawings/2026-11-21/README.md` | These indexes predate the Version 1.1 six-field template. | Preserve existing indexes. Use the six-field template for new daily indexes and material revisions. |
| Drawing session brief | `drawings/2026-11-21/session-01-brief.md` | This brief predates the canonical template and records a closed session. | Preserve it. New briefs use the canonical status values Active, Paused, and Closed. |
| Novel illustration notes | `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-01.md`; `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-02.md`; `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-03.md`; `novels/Novel-01/Arc-01/Scene-003/illustrations/illustration-01.md`; `novels/Novel-01/Arc-01/Scene-004/illustrations/illustration-01.md`; `novels/Novel-01/Arc-01/Scene-005/illustrations/illustration-01.md` | All six records declare format Version 1.0 and predate the current Version 1.1 template. | Preserve the records. Use Version 1.1 for new notes and material revisions. |
| Session integrity and summary | `drawings/history/2026-11-12-conversation-integrity.md`; `drawings/history/2026-11-12-summary.md` | These historical records predate the standalone templates and use project-specific chronological and handoff structures. | Preserve them. Use the canonical templates for new records. |
| Historical novel templates | `novels/templates/novel-v1.md`; `novels/templates/arc-v1.md`; `novels/templates/scene-v1.md`; `novels/templates/illustration-note-v1.md` | These Version 1.0 templates are superseded by the current Version 1.1 templates. | Preserve as historical references; new documents and material revisions use the current templates. |
| Early drawing attempt | `drawings/2026-11-19/attempt-01.md` | This record predates the Version 1.1 attempt template and uses an earlier free-form structure. | Preserve it; use Version 1.1 for new attempts and material revisions. |
| Historical image-prompt logs | `drawings/history/2026-11-12-image-prompts.md`; `drawings/history/2026-11-13-image-prompts.md`; `drawings/history/2026-11-16-image-prompts.md` | These chronological logs predate the current drawing-attempt template and preserve historical prompts and outcomes. | Preserve them as historical records; new attempts use the canonical attempt template. |
| Novel illustration prompt records | `novels/Novel-01/Arc-01/Scene-003/illustrations/illustration-01-prompt.md`; `novels/Novel-01/Arc-01/Scene-004/illustrations/illustration-01-prompt.md`; `novels/Novel-01/Arc-01/Scene-005/illustrations/illustration-01-prompt.md` | Scene-003 declares Version 1.0; Scene-004 and Scene-005 lack version frontmatter and use earlier custom layouts. | Preserve the historical records. Use the canonical Version 1.1 template for new prompt records and material revisions. |
| Workspace task record | `workspace/tasks/20261122-233900-enforce-template-first-document-standards.md` | This task record declares Template version 1.0. The current task template is Version 1.1. | Preserve the original task metadata. Use Version 1.1 for new task records. |
| Agent Skill definitions | Existing skill files under `skills/` | Many skills predate the reusable Agent Skill template. | Do not mass-convert existing skills. Use the canonical template for new skills and material rewrites. |

No new session summary or conversation-integrity record was required during this review. Their templates remain available for future sessions.

## Priority gaps

1. Obtain separate user approval to add a dedicated GitHub Actions workflow for the catalog validator and its regression tests.
2. After approval, run the validator and tests on a hosted runner, then repair any failures.
3. Keep archive-retention trigger scope unresolved until the user confirms whether manual and workflow-call force triggers are permitted.

## Catalog maintenance

When a recurring document type is added or changed:

1. Identify its owning skill or workflow.
2. Define its canonical template, schema, or embedded contract.
3. Add or update one catalog row.
4. Link the template from its owner index.
5. Define structural validation and migration rules.
6. Read back all changed paths.
7. Run `skills/document-standards/scripts/validate_catalog.py` and its tests through an authorized GitHub Actions workflow. This validator checks catalog integrity and exact references; it does not validate document content. Do not run it locally.
