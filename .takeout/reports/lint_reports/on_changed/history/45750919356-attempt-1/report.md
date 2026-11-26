# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#749](https://github.com/dungnv2602/chatgpt/actions/runs/45750919356)
- **Run ID / attempt:** 45750919356 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / e9a158a10a15f5c865da4feff79e68564b91bab7
- **Event:** push
- **Execution mode:** full-audit-fallback
- **Baseline SHA:** Not applicable
- **Linter source SHA:** e9a158a10a15f5c865da4feff79e68564b91bab7
- **Generated (UTC):** 2026-11-26T03:47:31.750655+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 88 |
| Files that failed | 88 |
| Files with findings | 0 |
| Total findings | 0 |
| Hard findings | 0 |
| Advisory findings | 0 |
| New findings | 0 |
| Recurring findings | 0 |
| Resolved findings | 0 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/skill-creator/agents/grader.md
- .agent/skills/skill-creator/agents/analyzer.md
- .agent/skills/the-worker/references/image-provenance-and-webp.md
- .agent/skills/drawing/SKILL.md
- .agent/skills/doc-coauthoring/SKILL.md
- .agent/skills/the-worker/assets/session-brief-template.md
- .agent/INITIALIZATION_POLICY.md
- .agent/skills/internal-comms/SKILL.md
- .agent/skills/drawing/references/archive-and-delivery.md
- .agent/skills/grilling/SKILL.md
- .agent/skills/internal-comms/examples/3p-updates.md
- .agent/skills/drawing/README.md
- .agent/skills/theme-factory/themes/midnight-galaxy.md
- .agent/skills/skill-creator/SKILL.md
- workspace/adr/README.md
- .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md
- .agent/skills/drawing/references/patterns/README.md
- workspace/ADR_TEMPLATE.md
- .agent/skills/xlsx/SKILL.md
- .takeout/images/README-2.md
- .agent/skills/theme-factory/themes/sunset-boulevard.md
- .agent/skills/drawing/references/patterns/successful-patterns.md
- .agent/skills/define-goal/SKILL.md
- .agent/skills/drawing/references/generation-recovery-and-provenance.md
- .agent/skills/internal-comms/examples/faq-answers.md
- .agent/skills/README.md
- .agent/skills/drawing/references/style-guide.md
- .agent/skills/github-actions/SKILL.md
- .agent/skills/drawing/assets/attempt-template.md
- .agent/skills/theme-factory/themes/ocean-depths.md
- .agent/SESSION_START.md
- .agent/skills/theme-factory/themes/modern-minimalist.md
- .agent/skills/the-worker/assets/session-summary-template.md
- .agent/skills/the-worker/SKILL.md
- .agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md
- workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md
- .agent/skills/philosophy-religion-asceticism/references/source-standards.md
- .agent/skills/philosophy-religion-asceticism/SKILL.md
- .agent/skills/internal-comms/examples/general-comms.md
- .agent/skills/pdf/REFERENCE.md
- .agent/skills/decision-governance/SKILL.md
- .agent/skills/asd-ste100/references/writing-rules.md
- .agent/skills/drawing/references/series-continuity-and-iteration.md
- .agent/skills/document-standards/references/document-type-catalog.md
- .agent/skills/the-worker/references/archive-records-and-image-prompts.md
- .agent/skills/drawing/references/image-editing-protocol.md
- .agent/skills/agent-skill-authoring/SKILL.md
- .agent/skills/philosophy-religion-asceticism/README.md
- .takeout/images/README-1.md
- .agent/skills/theme-factory/themes/golden-hour.md
- .agent/skills/the-worker/references/conversation-mode.md
- .agent/skills/internal-comms/examples/company-newsletter.md
- .agent/skills/skill-creator/agents/comparator.md
- workspace/task_board.md
- .agent/skills/theme-factory/themes/desert-rose.md
- workspace/analysis/README.md
- .agent/skills/asd-ste100/README.md
- workspace/ANALYSIS_TEMPLATE.md
- .agent/skills/the-worker/references/image-processing-scripts.md
- .agent/skills/document-standards/SKILL.md
- .agent/skills/migrate-to-rust/SKILL.md
- .agent/skills/theme-factory/themes/forest-canopy.md
- .agent/skills/skill-creator/references/schemas.md
- workspace/draft/README.md
- workspace/TASK_TEMPLATE.md
- .agent/skills/pdf/FORMS.md
- .agent/skills/theme-factory/themes/arctic-frost.md
- .agent/skills/pdf/SKILL.md
- .agent/skills/drawing/references/prompt-fidelity.md
- .agent/skills/theme-factory/themes/botanical-garden.md
- .agent/skills/philosophy-religion-asceticism/references/research-method.md
- .agent/skills/philosophy-religion-asceticism/CHANGELOG.md
- .agent/skills/drawing/references/patterns/failure-patterns.md
- workspace/README.md
- .agent/skills/drawing/assets/daily-index-template.md
- .agent/skills/theme-factory/themes/tech-innovation.md
- .agent/skills/the-worker/references/drawing-session-closeout.md
- .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md
- .agent/skills/drawing/assets/pattern-entry-templates.md
- .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md
- .agent/skills/asd-ste100/SKILL.md
- .agent/skills/asd-ste100/assets/lint-report-template.md
- workspace/DRAFT_TEMPLATE.md
- .agent/skills/discernment-nudge/SKILL.md
- workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md
- .agent/skills/asd-ste100/references/repository-writing-policy.md
- .agent/skills/theme-factory/SKILL.md
- .agent/skills/the-worker/assets/conversation-integrity-template.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/skill-creator/agents/grader.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/skill-creator/agents/analyzer.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/references/image-provenance-and-webp.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/doc-coauthoring/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/assets/session-brief-template.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/INITIALIZATION_POLICY.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/internal-comms/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/archive-and-delivery.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/grilling/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/internal-comms/examples/3p-updates.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/midnight-galaxy.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/skill-creator/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/adr/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/patterns/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/ADR_TEMPLATE.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/xlsx/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .takeout/images/README-2.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/sunset-boulevard.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/patterns/successful-patterns.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/define-goal/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/generation-recovery-and-provenance.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/internal-comms/examples/faq-answers.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/style-guide.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/github-actions/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/assets/attempt-template.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/ocean-depths.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/SESSION_START.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/modern-minimalist.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/assets/session-summary-template.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/references/source-standards.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/internal-comms/examples/general-comms.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/pdf/REFERENCE.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/decision-governance/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/asd-ste100/references/writing-rules.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/series-continuity-and-iteration.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/document-standards/references/document-type-catalog.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/references/archive-records-and-image-prompts.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/image-editing-protocol.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/agent-skill-authoring/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .takeout/images/README-1.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/golden-hour.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/references/conversation-mode.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/internal-comms/examples/company-newsletter.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/skill-creator/agents/comparator.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/task_board.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/desert-rose.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/analysis/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/asd-ste100/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/ANALYSIS_TEMPLATE.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/references/image-processing-scripts.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/document-standards/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/migrate-to-rust/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/forest-canopy.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/skill-creator/references/schemas.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/draft/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/TASK_TEMPLATE.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/pdf/FORMS.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/arctic-frost.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/pdf/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/prompt-fidelity.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/botanical-garden.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/references/research-method.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/CHANGELOG.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/patterns/failure-patterns.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/assets/daily-index-template.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/tech-innovation.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/references/drawing-session-closeout.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/assets/pattern-entry-templates.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/asd-ste100/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/asd-ste100/assets/lint-report-template.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/DRAFT_TEMPLATE.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/discernment-nudge/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/asd-ste100/references/repository-writing-policy.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/assets/conversation-integrity-template.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |

## 5. Findings by rule

Counts include hard and advisory findings.

No findings.

## 6. Workflow and validation checks

Each check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.

### Wrapper shell syntax

- **Result:** Passed
- **Exit code:** 0

~~~text
No output captured.
~~~

### Python report tooling compilation

- **Result:** Passed
- **Exit code:** 0

~~~text
No output captured.
~~~

### Lint report regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
....
----------------------------------------------------------------------
Ran 4 tests in 0.367s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
~~~

### STE linter self-test

- **Result:** Passed
- **Exit code:** 0

~~~text
selftest OK
~~~

### Markdown links and heading anchors

- **Result:** Failed
- **Exit code:** 1

~~~text
Scanned 246 active Markdown files (255 available as link targets) and 635 local Markdown links.
Found 193 unresolved local Markdown targets or anchors.
.agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md: missing heading anchor: #step-d-log-every-test-run--self-healing-fix-test_heal-bucket
.agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md: missing heading anchor: #4-profile-guided-optimization-pgo-workflow-pgo_bench-bucket
.agent/skills/prompt-master/assets/prompt-templates.md: missing heading anchor: #template-h--react--stop-conditions
.archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md: missing Markdown file: ../tasks/20261124-103354-establish-draft-adr-governance-and-repo-analysis-workflow.md
.archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md: missing Markdown file: ../tasks/20261124-103354-establish-draft-adr-governance-and-repo-analysis-workflow.md
area/drawing/history/2026-11-12-conversation-integrity.md: missing Markdown file: ../images/webp/README.md
area/drawing/history/2026-11-12-conversation-integrity.md: missing Markdown file: ../skills/drawing/SKILL.md
area/drawing/history/2026-11-12-conversation-integrity.md: missing Markdown file: ../skills/session-archiving/SKILL.md
area/drawing/history/2026-11-12-image-prompts.md: missing Markdown file: ../skills/session-archiving/SKILL.md
area/drawing/history/2026-11-12-summary.md: missing Markdown file: ../skills/session-archiving/SKILL.md
area/drawing/history/2026-11-12-summary.md: missing Markdown file: ../skills/session-archiving/SKILL.md
area/drawing/history/2026-11-12-summary.md: missing Markdown file: ../images/webp/
area/drawing/history/2026-11-12-summary.md: missing Markdown file: ../images/webp/README.md
area/drawing/history/2026-11-12-summary.md: missing Markdown file: ../skills/session-archiving/SKILL.md
area/drawing/history/2026-11-12-summary.md: missing Markdown file: ../skills/drawing/SKILL.md
area/drawing/history/2026-11-16-image-prompts.md: missing Markdown file: ../novel/Novel-01/Arc-01/Scene-001/scene.md
area/drawing/history/2026-11-16-image-prompts.md: missing Markdown file: ../novel/Novel-01/Arc-01/Scene-002/scene.md
area/drawing/history/2026-11-16-image-prompts.md: missing Markdown file: ../novel/Novel-01/Arc-01/Scene-002/scene.md
area/drawing/history/2026-11-16-image-prompts.md: missing Markdown file: ../novel/Novel-01/Arc-01/Scene-002/scene.md
area/drawing/history/conversation-2026-11-11-sams-origin-and-wonderhome.md: missing Markdown file: image-generation-attempt-history-2026-11-11.md
area/drawing/history/conversation-2026-11-11-sams-origin-and-wonderhome.md: missing Markdown file: our_glossary.md
area/drawing/history/conversation-2026-11-12-intimacy-and-portrait.md: missing Markdown file: image-generation-attempt-history-2026-11-12.md
area/drawing/history/conversation-2026-11-12-verbatim-available-record.md: missing Markdown file: image-generation-attempt-history-2026-11-12.md
area/novel/Novel-01/Arc-01/Scene-001/scene.md: missing Markdown file: ../../../../drawings/history/2026-11-16-image-prompts.md
area/novel/Novel-01/Arc-01/Scene-002/illustrations/illustration-01.md: missing Markdown file: ../../../../../drawings/history/2026-11-16-image-prompts.md#attempt-04--maya-listens-across-the-book
area/novel/Novel-01/Arc-01/Scene-002/illustrations/illustration-02.md: missing Markdown file: ../../../../../drawings/history/2026-11-16-image-prompts.md#attempt-05--a-closer-listening-moment
area/novel/Novel-01/Arc-01/Scene-002/illustrations/illustration-03.md: missing Markdown file: ../../../../../drawings/history/2026-11-16-image-prompts.md#attempt-06--maya-across-the-café-table
area/novel/Novel-01/Arc-01/Scene-002/scene.md: missing Markdown file: ../../../../drawings/history/2026-11-16-image-prompts.md#attempt-04--maya-listens-across-the-book
area/novel/Novel-01/Arc-01/Scene-002/scene.md: missing Markdown file: ../../../../drawings/history/2026-11-16-image-prompts.md#attempt-05--a-closer-listening-moment
area/novel/Novel-01/Arc-01/Scene-002/scene.md: missing Markdown file: ../../../../drawings/history/2026-11-16-image-prompts.md#attempt-06--maya-across-the-café-table
area/novel/WORKFLOW.md: missing Markdown file: ../skills/romantic-storyteller-visual-artist/SKILL.md
area/novel/WORKFLOW.md: missing Markdown file: ../skills/asd-ste100/references/repository-writing-policy.md
area/novel/templates/scene-v1.md: missing Markdown file: relative-path
workspace/adr/README.md: missing Markdown file: ../../archive/adr/0002-retire-source-drafts-after-verified-adr-promotion.md
workspace/adr/README.md: missing Markdown file: ../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md
workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md: missing Markdown file: ../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md
workspace/task_board.md: missing Markdown file: tasks/20261125-071328-04-review-semicolon-findings-in-workspace-draft-draft-0003-area-pro.md
workspace/task_board.md: missing Markdown file: tasks/20261125-071328-03-review-synonym-rotation-findings-in-workspace-draft-draft-0003-a.md
workspace/task_board.md: missing Markdown file: tasks/20261125-071328-02-review-long-sentence-findings-in-workspace-draft-draft-0003-area.md
workspace/task_board.md: missing Markdown file: tasks/20261125-071328-01-review-present-perfect-findings-in-workspace-draft-draft-0003-ar.md
workspace/task_board.md: missing Markdown file: tasks/20261125-071328-review-passive-voice-findings-in-workspace-draft-draft-0003-area.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-59-review-synonym-rotation-findings-in-skills-xlsx-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-58-review-passive-voice-findings-in-skills-xlsx-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-57-review-semicolon-findings-in-skills-xlsx-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-56-review-long-sentence-findings-in-skills-xlsx-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-55-review-semicolon-findings-in-skills-migrate-to-rust-references-p.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-54-review-synonym-rotation-findings-in-skills-migrate-to-rust-refer.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-53-review-passive-voice-findings-in-skills-migrate-to-rust-referenc.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-52-review-long-sentence-findings-in-skills-migrate-to-rust-referenc.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-51-review-semicolon-findings-in-skills-skill-creator-agents-compara.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-50-review-passive-voice-findings-in-skills-skill-creator-agents-com.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-49-review-passive-voice-findings-in-skills-internal-comms-examples.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-48-review-synonym-rotation-findings-in-skills-migrate-to-rust-skill.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-47-review-passive-voice-findings-in-skills-migrate-to-rust-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-46-review-long-sentence-findings-in-skills-migrate-to-rust-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-45-review-passive-voice-findings-in-skills-skill-creator-references.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-44-review-passive-voice-findings-in-skills-define-goal-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-43-review-synonym-rotation-findings-in-skills-define-goal-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-42-review-semicolon-findings-in-skills-define-goal-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-41-review-long-sentence-findings-in-skills-define-goal-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-40-review-present-perfect-findings-in-skills-skill-creator-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-39-review-semicolon-findings-in-skills-skill-creator-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-38-review-passive-voice-findings-in-skills-skill-creator-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-37-review-synonym-rotation-findings-in-skills-skill-creator-skill-m.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-36-review-long-sentence-findings-in-skills-skill-creator-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-35-review-present-perfect-findings-in-skills-doc-coauthoring-skill.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-34-review-long-sentence-findings-in-skills-doc-coauthoring-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-33-review-passive-voice-findings-in-skills-doc-coauthoring-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-32-review-synonym-rotation-findings-in-skills-doc-coauthoring-skill.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-31-review-long-sentence-findings-in-skills-pdf-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-30-review-present-perfect-findings-in-skills-skill-creator-agents-a.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-29-review-synonym-rotation-findings-in-skills-skill-creator-agents.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-28-review-passive-voice-findings-in-skills-skill-creator-agents-ana.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-27-review-long-sentence-findings-in-skills-internal-comms-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-26-review-passive-voice-findings-in-skills-discernment-nudge-skill.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-25-review-semicolon-findings-in-skills-discernment-nudge-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-24-review-synonym-rotation-findings-in-skills-discernment-nudge-ski.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-23-review-long-sentence-findings-in-skills-discernment-nudge-skill.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-22-review-present-perfect-findings-in-skills-internal-comms-example.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-21-review-long-sentence-findings-in-skills-internal-comms-examples.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-20-review-passive-voice-findings-in-skills-internal-comms-examples.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-19-review-present-perfect-findings-in-skills-grilling-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-18-review-passive-voice-findings-in-skills-grilling-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-17-review-semicolon-findings-in-skills-grilling-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-16-review-long-sentence-findings-in-skills-grilling-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-15-review-passive-voice-findings-in-skills-theme-factory-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-14-review-semicolon-findings-in-skills-theme-factory-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-13-review-synonym-rotation-findings-in-skills-theme-factory-skill-m.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-12-review-present-perfect-findings-in-skills-theme-factory-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-11-review-long-sentence-findings-in-skills-internal-comms-examples.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-10-review-passive-voice-findings-in-skills-internal-comms-examples.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-09-review-marketing-adjective-findings-in-skills-theme-factory-them.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-08-review-passive-voice-findings-in-skills-pdf-forms-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-07-review-semicolon-findings-in-skills-pdf-forms-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-06-review-synonym-rotation-findings-in-skills-pdf-forms-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-05-review-long-sentence-findings-in-skills-pdf-forms-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-04-review-present-perfect-findings-in-skills-internal-comms-example.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-03-review-long-sentence-findings-in-skills-internal-comms-examples.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-02-review-passive-voice-findings-in-skills-internal-comms-examples.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-01-review-passive-voice-findings-in-skills-skill-creator-agents-gra.md
workspace/task_board.md: missing Markdown file: tasks/20261125-062941-review-synonym-rotation-findings-in-skills-skill-creator-agents.md
workspace/task_board.md: missing Markdown file: tasks/20261125-023945-05-review-synonym-rotation-findings-in-workspace-draft-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-023945-04-review-long-sentence-findings-in-workspace-draft-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-023945-03-review-semicolon-findings-in-workspace-draft-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-023945-02-review-passive-voice-findings-in-workspace-draft-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-023945-01-review-long-sentence-findings-in-workspace-draft-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261125-023945-review-semicolon-findings-in-skills-decision-governance-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-182215-review-present-perfect-findings-in-workspace-adr-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-164450-review-synonym-rotation-findings-in-workspace-task-board-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-162814-review-synonym-rotation-findings-in-workspace-draft-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-161334-07-review-passive-voice-findings-in-workspace-draft-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-161334-06-review-present-perfect-findings-in-workspace-draft-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-161334-review-semicolon-findings-in-workspace-adr-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-155748-05-review-semicolon-findings-in-workspace-draft-draft-0003-retire-s.md
workspace/task_board.md: missing Markdown file: tasks/20261124-155748-04-review-passive-voice-findings-in-workspace-draft-draft-0003-reti.md
workspace/task_board.md: missing Markdown file: tasks/20261124-155748-03-review-present-perfect-findings-in-workspace-draft-draft-0003-re.md
workspace/task_board.md: missing Markdown file: tasks/20261124-155748-02-review-long-sentence-findings-in-workspace-draft-draft-0003-reti.md
workspace/task_board.md: missing Markdown file: tasks/20261124-155748-01-review-synonym-rotation-findings-in-workspace-draft-draft-0003-r.md
workspace/task_board.md: missing Markdown file: tasks/20261124-155748-review-semicolon-findings-in-workspace-draft-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-153825-01-review-semicolon-findings-in-workspace-draft-draft-0002-phase-aw.md
workspace/task_board.md: missing Markdown file: tasks/20261124-153825-review-long-sentence-findings-in-workspace-draft-draft-0002-phas.md
workspace/task_board.md: missing Markdown file: tasks/20261124-150717-review-publication-or-push-failures-in-ste-lint-changed-document.md
workspace/task_board.md: missing Markdown file: tasks/20261124-141534-review-synonym-rotation-findings-in-workspace-adr-0001-establish.md
workspace/task_board.md: missing Markdown file: tasks/20261124-134225-review-validation-or-test-failures-in-validate-document-standard.md
workspace/task_board.md: missing Markdown file: tasks/20261124-132754-02-review-present-perfect-findings-in-workspace-draft-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-132754-01-review-passive-voice-findings-in-workspace-analysis-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-132754-review-passive-voice-findings-in-workspace-adr-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-125956-06-review-passive-voice-findings-in-workspace-analysis-analysis-tem.md
workspace/task_board.md: missing Markdown file: tasks/20261124-125956-05-review-passive-voice-findings-in-workspace-task-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-125956-04-review-long-sentence-findings-in-workspace-analysis-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-125956-03-review-present-perfect-findings-in-skills-decision-governance-sk.md
workspace/task_board.md: missing Markdown file: tasks/20261124-125956-02-review-long-sentence-findings-in-skills-decision-governance-skil.md
workspace/task_board.md: missing Markdown file: tasks/20261124-125956-01-review-passive-voice-findings-in-skills-decision-governance-skil.md
workspace/task_board.md: missing Markdown file: tasks/20261124-125956-review-synonym-rotation-findings-in-skills-decision-governance-s.md
workspace/task_board.md: missing Markdown file: tasks/20261124-123847-review-passive-voice-findings-in-workspace-adr-0001-establish-dr.md
workspace/task_board.md: missing Markdown file: tasks/20261124-114048-02-review-present-perfect-findings-in-workspace-draft-draft-0002-ph.md
workspace/task_board.md: missing Markdown file: tasks/20261124-114048-01-review-synonym-rotation-findings-in-workspace-draft-draft-0002-p.md
workspace/task_board.md: missing Markdown file: tasks/20261124-114048-review-passive-voice-findings-in-workspace-draft-draft-0002-phas.md
workspace/task_board.md: missing Markdown file: tasks/20261124-111733-04-review-present-perfect-findings-in-skills-the-worker-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-111733-03-review-synonym-rotation-findings-in-skills-the-worker-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-111733-02-review-passive-voice-findings-in-skills-the-worker-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-111733-01-review-semicolon-findings-in-skills-the-worker-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-111733-review-long-sentence-findings-in-skills-the-worker-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104408-03-review-long-sentence-findings-in-workspace-draft-draft-0001-repo.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104408-02-review-synonym-rotation-findings-in-workspace-draft-draft-0001-r.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104408-01-review-present-perfect-findings-in-workspace-draft-draft-0001-repo.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104408-review-passive-voice-findings-in-workspace-draft-draft-0001-repo.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104329-review-validation-or-test-failures-in-validate-document-standard.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-09-review-synonym-rotation-findings-in-workspace-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-08-review-long-sentence-findings-in-workspace-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-07-review-semicolon-findings-in-workspace-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-06-review-passive-voice-findings-in-workspace-adr-adr-template-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-05-review-passive-voice-findings-in-workspace-adr-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-04-review-present-perfect-findings-in-workspace-draft-draft-templat.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-03-review-present-perfect-findings-in-skills-the-worker-references.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-02-review-passive-voice-findings-in-skills-the-worker-references-co.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-01-review-semicolon-findings-in-skills-the-worker-references-conver.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104204-review-long-sentence-findings-in-skills-the-worker-references-co.md
workspace/task_board.md: missing Markdown file: tasks/20261124-094047-07-review-passive-voice-findings-in-skills-drawing-references-patte.md
workspace/task_board.md: missing Markdown file: tasks/20261124-094047-06-review-passive-voice-findings-in-workspace-task-board-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-094047-05-review-synonym-rotation-findings-in-skills-document-standards-re.md
workspace/task_board.md: missing Markdown file: tasks/20261124-094047-04-review-present-perfect-findings-in-skills-drawing-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-094047-03-review-synonym-rotation-findings-in-skills-drawing-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-094047-02-review-passive-voice-findings-in-skills-drawing-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-094047-01-review-present-perfect-findings-in-skills-drawing-assets-pattern.md
workspace/task_board.md: missing Markdown file: tasks/20261124-094047-review-passive-voice-findings-in-skills-drawing-assets-pattern-e.md
workspace/task_board.md: missing Markdown file: tasks/20261124-061933-02-review-publication-or-push-failures-in-process-image-takeout-and.md
workspace/task_board.md: missing Markdown file: tasks/20261124-061933-01-review-checkout-or-action-download-failures-in-process-image-tak.md
workspace/task_board.md: missing Markdown file: tasks/20261124-061933-review-checkout-or-action-download-failures-in-validate-document.md
workspace/task_board.md: missing Markdown file: tasks/20261124-045935-02-review-long-sentence-findings-in-workspace-task-board-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-050735-02-review-long-sentence-findings-in-skills-document-standards-refer.md
workspace/task_board.md: missing Markdown file: tasks/20261124-050735-01-review-semicolon-findings-in-skills-document-standards-reference.md
workspace/task_board.md: missing Markdown file: tasks/20261124-045935-04-review-semicolon-findings-in-images-takeout-history-2026-11-20-0.md
workspace/task_board.md: missing Markdown file: tasks/20261124-045935-03-review-semicolon-findings-in-images-takeout-history-2026-11-20-0.md
workspace/task_board.md: missing Markdown file: tasks/20261124-045935-01-review-semicolon-findings-in-images-takeout-history-2026-11-20-0.md
workspace/task_board.md: missing Markdown file: tasks/20261124-045935-review-synonym-rotation-findings-in-skills-the-worker-references.md
workspace/task_board.md: missing Markdown file: tasks/20261124-050735-review-synonym-rotation-findings-in-skills-asd-ste100-skill-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-08-review-passive-voice-findings-in-workspace-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-07-review-present-perfect-findings-in-skills-document-standards-ref.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-06-review-passive-voice-findings-in-skills-document-standards-refer.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-05-review-passive-voice-findings-in-images-takeout-history-2026-11.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-04-review-passive-voice-findings-in-images-takeout-history-2026-11.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-03-review-passive-voice-findings-in-images-takeout-history-2026-11.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-02-review-passive-voice-findings-in-skills-the-worker-references-im.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-01-review-passive-voice-findings-in-images-readme-md.md
workspace/task_board.md: missing Markdown file: tasks/20261124-080232-review-passive-voice-findings-in-images-takeout-readme-md.md
workspace/task_board.md: missing Markdown file: ../.archive/task/20261125-023508-standardize-detailed-option-assessments-in-future-drafts.md
workspace/task_board.md: missing Markdown file: ../.archive/task/20261124-183017-repair-adr-catalog-rule-and-ci-follow-through.md
workspace/task_board.md: missing Markdown file: ../.archive/task/20261124-181746-reconcile-final-adr-0002-ledger-finding.md
workspace/task_board.md: missing Markdown file: ../.archive/task/20261124-161334-01-review-present-perfect-findings-in-workspace-adr-0002-retire-sou.md
workspace/task_board.md: missing Markdown file: ../.archive/task/20261124-161334-02-review-passive-voice-findings-in-workspace-adr-0002-retire-sourc.md
workspace/task_board.md: missing Markdown file: ../.archive/task/20261124-161334-03-review-semicolon-findings-in-workspace-adr-0002-retire-source-dr.md
workspace/task_board.md: missing Markdown file: ../.archive/task/20261124-161334-04-review-long-sentence-findings-in-workspace-adr-0002-retire-sourc.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

None.

### Resolved findings

None.

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/skill-creator/agents/grader.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/skill-creator/agents/analyzer.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/references/image-provenance-and-webp.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/doc-coauthoring/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/assets/session-brief-template.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/INITIALIZATION_POLICY.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/internal-comms/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/archive-and-delivery.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/grilling/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/internal-comms/examples/3p-updates.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/midnight-galaxy.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/skill-creator/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/adr/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/patterns/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/ADR_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/xlsx/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .takeout/images/README-2.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/sunset-boulevard.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/patterns/successful-patterns.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/define-goal/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/generation-recovery-and-provenance.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/internal-comms/examples/faq-answers.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/style-guide.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/assets/attempt-template.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/ocean-depths.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/modern-minimalist.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/assets/session-summary-template.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/references/source-standards.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/internal-comms/examples/general-comms.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/pdf/REFERENCE.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/decision-governance/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/asd-ste100/references/writing-rules.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/series-continuity-and-iteration.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/references/archive-records-and-image-prompts.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/image-editing-protocol.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/agent-skill-authoring/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .takeout/images/README-1.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/golden-hour.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/references/conversation-mode.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/internal-comms/examples/company-newsletter.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/skill-creator/agents/comparator.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/desert-rose.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/analysis/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/asd-ste100/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/ANALYSIS_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/references/image-processing-scripts.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/document-standards/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/migrate-to-rust/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/forest-canopy.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/skill-creator/references/schemas.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/draft/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/TASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/pdf/FORMS.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/arctic-frost.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/pdf/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/prompt-fidelity.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/botanical-garden.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/references/research-method.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/CHANGELOG.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/patterns/failure-patterns.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/assets/daily-index-template.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/tech-innovation.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/references/drawing-session-closeout.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/assets/pattern-entry-templates.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/asd-ste100/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/asd-ste100/assets/lint-report-template.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/DRAFT_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/discernment-nudge/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/asd-ste100/references/repository-writing-policy.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/theme-factory/SKILL.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/the-worker/assets/conversation-integrity-template.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
