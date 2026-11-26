# On Repo STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#196](https://github.com/dungnv2602/chatgpt/actions/runs/45743066143)
- **Run ID / attempt:** 45743066143 / 1
- **Workflow:** STE Lint Full Technical Documentation
- **Branch / commit:** gpt / a17a908918f887fa7ce1e4aceccb11225d7eeee0
- **Event:** push
- **Execution mode:** repository-wide
- **Baseline SHA:** Not applicable
- **Linter source SHA:** 01d8ebcfa2fa92cd887c992abb01d81baf52bf61
- **Generated (UTC):** 2026-11-26T02:34:45.232275+00:00

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
| Resolved findings | 454 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43
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
Ran 4 tests in 0.226s

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
Scanned 596 active Markdown files (753 available as link targets) and 655 local Markdown links.
Found 106 unresolved local Markdown targets or anchors.
.agent/SESSION_START.md: missing Markdown file: .agent/skills/asd-ste100/references/repository-writing-policy.md
.agent/skills/README.md: missing Markdown file: SESSION_START.md
.agent/skills/README.md: missing Markdown file: SESSION_START.md
.agent/skills/drawing/references/patterns/README.md: missing Markdown file: ../../../../drawings/history/successful-prompts.md
.agent/skills/drawing/references/patterns/README.md: missing Markdown file: ../../../../drawings/history/failed-prompts.md
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/failed-prompts.md
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/failed-prompts.md#fp-05--repeated-reversed-resting-roles-in-the-cozy-bedroom-sequence
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-12-image-prompts.md#20--concise-reuse-of-successful-after-work-pose
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-12-image-prompts.md#21--reference-guided-reconstruction-of-the-correct-after-work-pose
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/failed-prompts.md#fp-07--style-transfer-and-source-preservation-attempts
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-13-image-prompts.md#attempt-01--source-guided-silk-wrap-portrait
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-13-image-prompts.md#attempt-02--reference-attached-silk-wrap-portrait
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/failed-prompts.md#fp-07--style-transfer-and-source-preservation-attempts
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-16-image-prompts.md#attempt-03--the-book-handoff-single-scene
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-13-image-prompts.md#attempt-02--reference-attached-silk-wrap-portrait
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-13-image-prompts.md#attempt-03--modest-editorial-silk-wrap-portrait-safety-aware-revision
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/failed-prompts.md#fp-08--generic-safety-refusals-during-portrait-retries
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-16-image-prompts.md#attempt-06--maya-across-the-café-table
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-12-image-prompts.md#13--fresh-generation-in-the-preferred-cream-cardigan
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/2026-11-19/attempt-46.md
.agent/skills/drawing/references/patterns/failure-patterns.md: missing Markdown file: ../../../../drawings/2026-11-19/attempt-45.md
.agent/skills/drawing/references/patterns/successful-patterns.md: missing Markdown file: ../../../../drawings/history/successful-prompts.md
.agent/skills/drawing/references/patterns/successful-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-12-image-prompts.md#33--historical-silk-wrap-portrait-direction-realistic-mode
.agent/skills/drawing/references/patterns/successful-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-13-image-prompts.md#attempt-04--direct-reuse-of-the-proven-silk-wrap-portrait-direction
.agent/skills/drawing/references/patterns/successful-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-12-image-prompts.md#33--historical-silk-wrap-portrait-direction-realistic-mode
.agent/skills/drawing/references/patterns/successful-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-13-image-prompts.md#attempt-04--direct-reuse-of-the-proven-silk-wrap-portrait-direction
.agent/skills/drawing/references/patterns/successful-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-12-image-prompts.md#04--comfort-after-a-long-workday
.agent/skills/drawing/references/patterns/successful-patterns.md: missing Markdown file: ../../../../drawings/history/2026-11-12-image-prompts.md#14--mistaken-tea-scene-interpretation-cream-cardigan-and-navy-polo
.agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md: missing heading anchor: #step-d-log-every-test-run--self-healing-fix-test_heal-bucket
.agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md: missing heading anchor: #4-profile-guided-optimization-pgo-workflow-pgo_bench-bucket
.agent/skills/prompt-master/assets/prompt-templates.md: missing heading anchor: #template-h--react--stop-conditions
.agent/skills/romantic-storyteller-visual-artist/SKILL.md: missing Markdown file: ../SESSION_START.md#novelist-role-initialization
.agent/skills/romantic-storyteller-visual-artist/references/novel-production-workflow.md: missing Markdown file: ../../../novels/WORKFLOW.md
.agent/skills/romantic-storyteller-visual-artist/references/novel-production-workflow.md: missing Markdown file: ../../../novels/README.md
.agent/skills/romantic-storyteller-visual-artist/references/novel-production-workflow.md: missing Markdown file: ../../../novels/WORKFLOW.md
.agent/skills/the-worker/references/image-provenance-and-webp.md: missing Markdown file: ../../../images/takeout/README.md
.archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md: missing Markdown file: ../tasks/20261124-103354-establish-draft-adr-governance-and-repo-analysis-workflow.md
.archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md: missing Markdown file: ../tasks/20261124-103354-establish-draft-adr-governance-and-repo-analysis-workflow.md
.archive/task/20261120-120302-condensed-mode-discussion-register.md: missing Markdown file: ../../skills/conversation-mode/SKILL.md
.archive/task/20261120-120302-condensed-mode-discussion-register.md: missing Markdown file: ../../skills/the-worker/SKILL.md
.archive/task/20261120-123400-condensed-mode-task-gates-and-reporting.md: missing Markdown file: ../conversation-mode/SKILL.md
.archive/task/20261120-123400-condensed-mode-task-gates-and-reporting.md: missing Markdown file: ../task_board.md
.archive/task/20261120-123400-condensed-mode-task-gates-and-reporting.md: missing Markdown file: ../discussion.md
.archive/task/20261124-160500-implement-verified-source-draft-retirement.md: missing Markdown file: ../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md
.archive/task/20261124-161334-01-review-present-perfect-findings-in-workspace-adr-0002-retire-sou.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45456236271-attempt-1/report.md
.archive/task/20261124-161334-02-review-passive-voice-findings-in-workspace-adr-0002-retire-sourc.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45456236271-attempt-1/report.md
.archive/task/20261124-161334-03-review-semicolon-findings-in-workspace-adr-0002-retire-source-dr.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45456236271-attempt-1/report.md
.archive/task/20261124-161334-04-review-long-sentence-findings-in-workspace-adr-0002-retire-sourc.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45456236271-attempt-1/report.md
.archive/task/20261124-161334-05-review-synonym-rotation-findings-in-workspace-adr-0002-retire-so.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45456236271-attempt-1/report.md
.archive/task/20261124-181746-reconcile-final-adr-0002-ledger-finding.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45456236271-attempt-1/report.md
.archive/task/20261124-181746-reconcile-final-adr-0002-ledger-finding.md: missing Markdown file: ../../archive/tasks/20261124-161334-05-review-synonym-rotation-findings-in-workspace-adr-0002-retire-so.md
.archive/task/20261124-181746-reconcile-final-adr-0002-ledger-finding.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45456236271-attempt-1/report.md
.archive/task/20261124-183017-repair-adr-catalog-rule-and-ci-follow-through.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45460721790-attempt-1/report.md
.archive/task/20261124-183017-repair-adr-catalog-rule-and-ci-follow-through.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45461327872-attempt-1/report.md
.archive/task/20261124-183017-repair-adr-catalog-rule-and-ci-follow-through.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45461706916-attempt-1/report.md
.archive/task/20261124-183017-repair-adr-catalog-rule-and-ci-follow-through.md: missing Markdown file: ../../reports/lint_reports/on_changed/history/45461706916-attempt-1/report.md
.takeout/images/README-1.md: missing Markdown file: takeout/README.md
.takeout/images/README-1.md: missing Markdown file: ../skills/drawing/references/archive-and-delivery.md
.takeout/images/README-1.md: missing Markdown file: ../skills/asd-ste100/references/repository-writing-policy.md
.takeout/images/README-2.md: missing Markdown file: ../../skills/asd-ste100/references/repository-writing-policy.md
.takeout/reports/README.md: missing Markdown file: ../archive/README.md
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
area/novel/README.md: missing Markdown file: ../images/takeout/README.md
area/novel/README.md: missing Markdown file: ../skills/drawing/references/archive-and-delivery.md
area/novel/README.md: missing Markdown file: ../skills/drawing/references/image-editing-protocol.md
area/novel/README.md: missing Markdown file: ../skills/asd-ste100/references/repository-writing-policy.md
area/novel/WORKFLOW.md: missing Markdown file: ../skills/romantic-storyteller-visual-artist/SKILL.md
area/novel/WORKFLOW.md: missing Markdown file: ../skills/asd-ste100/references/repository-writing-policy.md
area/novel/templates/scene-v1.md: missing Markdown file: relative-path
workspace/README.md: missing Markdown file: ../reports/README.md
workspace/README.md: missing Markdown file: ../archive/README.md
workspace/adr/README.md: missing Markdown file: ../../archive/adr/0002-retire-source-drafts-after-verified-adr-promotion.md
workspace/adr/README.md: missing Markdown file: ../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md
workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md: missing Markdown file: ../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md
workspace/task_board.md: missing Markdown file: tasks/20261124-104408-01-review-present-perfect-findings-in-workspace-draft-draft-0001-repo.md
workspace/task_board.md: missing Markdown file: ../archive/tasks/20261125-023508-standardize-detailed-option-assessments-in-future-drafts.md
workspace/task_board.md: missing Markdown file: ../archive/tasks/20261124-183017-repair-adr-catalog-rule-and-ci-follow-through.md
workspace/task_board.md: missing Markdown file: ../archive/tasks/20261124-181746-reconcile-final-adr-0002-ledger-finding.md
workspace/task_board.md: missing Markdown file: ../archive/tasks/20261124-161334-01-review-present-perfect-findings-in-workspace-adr-0002-retire-sou.md
workspace/task_board.md: missing Markdown file: ../archive/tasks/20261124-161334-02-review-passive-voice-findings-in-workspace-adr-0002-retire-sourc.md
workspace/task_board.md: missing Markdown file: ../archive/tasks/20261124-161334-03-review-semicolon-findings-in-workspace-adr-0002-retire-source-dr.md
workspace/task_board.md: missing Markdown file: ../archive/tasks/20261124-161334-04-review-long-sentence-findings-in-workspace-adr-0002-retire-sourc.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

None.

### Resolved findings

- **long-sentence** · skills/the-worker/references/conversation-mode.md:68:60 · **resolved** · fingerprint: a572f3dff82333ad7db50991
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · skills/the-worker/references/conversation-mode.md:68:162 · **resolved** · fingerprint: 09a34c4b31b88c0f364bd67e
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/references/conversation-mode.md:84:157 · **resolved** · fingerprint: bee2a996a437e18d996259cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered
- **passive-voice** · skills/the-worker/references/conversation-mode.md:95:72 · **resolved** · fingerprint: 2241e6bb50e2f15bfa24211b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **passive-voice** · skills/the-worker/references/conversation-mode.md:100:41 · **resolved** · fingerprint: d30ba0439a3d723f276eb4c5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · skills/the-worker/references/conversation-mode.md:127:88 · **resolved** · fingerprint: 2241e6bb50e2f15bfa24211b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **present-perfect** · skills/the-worker/references/conversation-mode.md:128:78 · **resolved** · fingerprint: cedfb1b9e8b08ba988f26ada
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **present-perfect** · skills/the-worker/references/conversation-mode.md:128:108 · **resolved** · fingerprint: 17842a0d207d59e3d6dfd995
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed
- **passive-voice** · skills/the-worker/references/conversation-mode.md:129:61 · **resolved** · fingerprint: bd2f7bbdff13e7e39ad308db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/the-worker/references/conversation-mode.md:129:272 · **resolved** · fingerprint: 843d844a7e11cf758d6cc899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved
- **passive-voice** · skills/the-worker/references/conversation-mode.md:144:63 · **resolved** · fingerprint: bd2f7bbdff13e7e39ad308db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/the-worker/references/conversation-mode.md:149:36 · **resolved** · fingerprint: 8e2161d80a5148d771a0f3ef
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered
- **passive-voice** · skills/the-worker/references/conversation-mode.md:151:106 · **resolved** · fingerprint: ff487ca595e84d2db113914a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · skills/the-worker/references/conversation-mode.md:160:180 · **resolved** · fingerprint: 308ed03edab7da5db41594ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · skills/the-worker/references/conversation-mode.md:186:260 · **resolved** · fingerprint: bd2f7bbdff13e7e39ad308db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · skills/the-worker/references/conversation-mode.md:201:94 · **resolved** · fingerprint: 04cc8860da7a5678f9593957
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · skills/the-worker/references/conversation-mode.md:228:126 · **resolved** · fingerprint: b415c4bf0547befb7d81674b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given
- **passive-voice** · skills/the-worker/references/conversation-mode.md:228:130 · **resolved** · fingerprint: b76b30e48b4f4ad0c86a4c75
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given
- **passive-voice** · skills/the-worker/references/conversation-mode.md:249:75 · **resolved** · fingerprint: c9dae4d4501881d9eacee582
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:53:21 · **resolved** · fingerprint: fc114dacae449b7519133918
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:94:11 · **resolved** · fingerprint: 01b04df4a4d61aa32756adf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disputed
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:144:43 · **resolved** · fingerprint: f05c498f9ee2269430ff8ada
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are related
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:167:67 · **resolved** · fingerprint: c645e65b81e4110faf6f2062
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:178:68 · **resolved** · fingerprint: b1d63c43c6349bc6f120ce18
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supported
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:179:43 · **resolved** · fingerprint: 671a7eda510ef040edd3be61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:291:3 · **resolved** · fingerprint: ac33fd0d35779883eb5af2cb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been excluded
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:292:52 · **resolved** · fingerprint: cd2a130c88bf1b1de364eda1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been kept
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:3:126 · **resolved** · fingerprint: ba15e2b13749f7aad6447fc1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:5:65 · **resolved** · fingerprint: fb05b158f323ac0a88758170
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are kept
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:19:163 · **resolved** · fingerprint: 7cb850c3e4335a13e7519ba0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reversed
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:22:89 · **resolved** · fingerprint: ce25d5ad6ba4826e11264f32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:37:14 · **resolved** · fingerprint: 32467609b8c42805cbf2c5ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is concentrated
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:48:20 · **resolved** · fingerprint: e1de4bab2e607823412ffbc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were described
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:51:37 · **resolved** · fingerprint: ac6348f1c31c27d904cb53b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:61:190 · **resolved** · fingerprint: b49561bafa5675d60cc907c5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:61:219 · **resolved** · fingerprint: 346827f54f442c607e8b24a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:85:19 · **resolved** · fingerprint: ede5e693c6707a81cfe3079a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:91:257 · **resolved** · fingerprint: 3c48312b0ae19adb3273832c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:120:226 · **resolved** · fingerprint: e0e662058459fdceb4c02481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was identified
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:136:66 · **resolved** · fingerprint: 715e2eee6cf5d1784b75c730
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:154:172 · **resolved** · fingerprint: c5308af1d2f63badad79bd66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:165:92 · **resolved** · fingerprint: 74cd4ed7e5ca2631c57c069b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:168:20 · **resolved** · fingerprint: 3c48312b0ae19adb3273832c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:183:164 · **resolved** · fingerprint: ede5e693c6707a81cfe3079a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **present-perfect** · skills/drawing/references/patterns/failure-patterns.md:194:52 · **resolved** · fingerprint: fca6bef2ba2e441b581fcc8d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has corrected
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:209:228 · **resolved** · fingerprint: 75eccc37cbac9985f7061f82
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was removed
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:209:266 · **resolved** · fingerprint: e56ece3c0f60be33dac72d05
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was preserved
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:210:242 · **resolved** · fingerprint: 5b28443dc965cf5ab3378e12
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was adopted
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:214:32 · **resolved** · fingerprint: b35900a9da7c000de2e26e70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **present-perfect** · skills/drawing/references/patterns/failure-patterns.md:218:179 · **resolved** · fingerprint: feb2d786d14c99b7e9fe9de0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:224:30 · **resolved** · fingerprint: 0cae9b0c6170006a0e67edc2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:250:20 · **resolved** · fingerprint: b35900a9da7c000de2e26e70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **passive-voice** · skills/the-worker/references/drawing-session-closeout.md:17:227 · **resolved** · fingerprint: 2d728b322e849133738368be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:14:79 · **resolved** · fingerprint: cf9a19441f150cbc6e394584
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:159:29 · **resolved** · fingerprint: 6ffc592c0b6322b443496f66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:166:23 · **resolved** · fingerprint: 6ffc592c0b6322b443496f66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **present-perfect** · skills/agent-skill-authoring/SKILL.md:172:149 · **resolved** · fingerprint: 2dddc1891d5710f75a1cc520
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been loaded
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:172:153 · **resolved** · fingerprint: f7fae0229a13471823102bb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:185:36 · **resolved** · fingerprint: 0be774910939027b005107b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:223:38 · **resolved** · fingerprint: 5eabd6169bec15a6fdfd2a80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:245:28 · **resolved** · fingerprint: 0f053c89c3267998b6edc9d6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused
- **present-perfect** · skills/agent-skill-authoring/SKILL.md:246:65 · **resolved** · fingerprint: 70dc63b30d658452239a6cbe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:246:70 · **resolved** · fingerprint: 2df378472bba68cfc7a25cbe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:253:17 · **resolved** · fingerprint: 8416fa6ec8b8068d6f7379c2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected
- **present-perfect** · skills/agent-skill-authoring/SKILL.md:255:37 · **resolved** · fingerprint: c26f9840d6188237d9689546
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been made
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:255:41 · **resolved** · fingerprint: 599292fe4dd9cfdbc4788ec9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been made
- **present-perfect** · skills/agent-skill-authoring/SKILL.md:257:32 · **resolved** · fingerprint: 4414015699cf2e3e269abe29
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:257:36 · **resolved** · fingerprint: 91d321a9405d06bea4b12487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · skills/asd-ste100/references/repository-writing-policy.md:18:36 · **resolved** · fingerprint: 3ae757460d9b3aa9399e9808
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/philosophy-religion-asceticism/references/source-standards.md:99:19 · **resolved** · fingerprint: ce4f5586a0c66bf136f1a181
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed
- **passive-voice** · skills/philosophy-religion-asceticism/references/source-standards.md:194:41 · **resolved** · fingerprint: 16921dc530cca16c2f4562e8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being cited
- **passive-voice** · skills/asd-ste100/README.md:26:35 · **resolved** · fingerprint: dc6fc135735cd3aa5f4246ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/asd-ste100/README.md:40:109 · **resolved** · fingerprint: bdbff79e00c0aca5352dcc38
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:17:40 · **resolved** · fingerprint: 80ff0d75ee9e57c63a759659
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:18:125 · **resolved** · fingerprint: e71b3a8ba6751987cf0fb966
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:22:67 · **resolved** · fingerprint: 4cca9a878a87bc55497611c8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · skills/drawing/assets/pattern-entry-templates.md:100:246 · **resolved** · fingerprint: ad46045395dc40b74a35f499
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:111:20 · **resolved** · fingerprint: 92485eeff29784dba3505b2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are separated
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:113:15 · **resolved** · fingerprint: 3f5048026fc0041e11f90db1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are described
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:115:19 · **resolved** · fingerprint: 9a512eba16db074bc582887d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · images/takeout/README.md:10:155 · **resolved** · fingerprint: 2a42254f52ec0603ee85a3a9
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/README.md:26:246 · **resolved** · fingerprint: df40b652ab5b159c04f41e56
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged
- **passive-voice** · images/takeout/README.md:30:214 · **resolved** · fingerprint: 1dd4e3f93bbd63b8ba0b2f3b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated
- **passive-voice** · images/takeout/README.md:96:188 · **resolved** · fingerprint: 2d2406b2dcc9afee713a40e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied
- **passive-voice** · images/takeout/README.md:97:44 · **resolved** · fingerprint: 52e38bd958f4a920f261f704
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · images/takeout/README.md:137:179 · **resolved** · fingerprint: 7e08a1b96836766cfc9ef94c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recognized
- **semicolon** · images/takeout/README.md:137:239 · **resolved** · fingerprint: 2a42254f52ec0603ee85a3a9
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/README.md:137:266 · **resolved** · fingerprint: 94d52ae57cd3b9cc39a3dbda
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rejected
- **passive-voice** · images/takeout/README.md:139:203 · **resolved** · fingerprint: 90c0f6ed37a3e9357ebf7580
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **semicolon** · images/takeout/README.md:180:266 · **resolved** · fingerprint: 2a42254f52ec0603ee85a3a9
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/README.md:203:40 · **resolved** · fingerprint: bf5f3ed6bfe52608af6f2cbb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:13:64 · **resolved** · fingerprint: f699d20c8970b5d1983db259
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is curated
- **semicolon** · skills/the-worker/references/archive-records-and-image-prompts.md:19:336 · **resolved** · fingerprint: 8e0bc452dce64863b8652cff
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/the-worker/references/archive-records-and-image-prompts.md:21:105 · **resolved** · fingerprint: e746242422de68b35229b9f1
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:33:8 · **resolved** · fingerprint: cc9ba4be2c27f329401729a2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was completed
- **synonym-rotation** · skills/the-worker/references/archive-records-and-image-prompts.md:52:20 · **resolved** · fingerprint: 1231d4c583bee759ca768857
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:87:21 · **resolved** · fingerprint: f3fec903703ee5f02784e5b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:96:11 · **resolved** · fingerprint: a8780077bedc79b1c8c2f758
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:124:164 · **resolved** · fingerprint: 26fb46186c78ffa8fc4b9cda
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:127:130 · **resolved** · fingerprint: ee1b84223aa1974ec2c266cc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:131:343 · **resolved** · fingerprint: c9f4691a4ae74067995898f8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:188:170 · **resolved** · fingerprint: 7004493f0380541a3c7f3930
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was supplied
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:191:23 · **resolved** · fingerprint: ca92034f0c45e9624487b338
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being tested
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:229:65 · **resolved** · fingerprint: 775b40787e9b3007554a0ec5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:240:24 · **resolved** · fingerprint: 2e9865ddbebafa08f9136623
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:246:176 · **resolved** · fingerprint: bb7ba68bed0f5ce8ed1acfa4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:260:44 · **resolved** · fingerprint: 080078c5d205e0780e807349
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:270:68 · **resolved** · fingerprint: d084f532a966087492331395
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:271:36 · **resolved** · fingerprint: 775b40787e9b3007554a0ec5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:271:58 · **resolved** · fingerprint: 3722d82669780cffed6aeec3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unverified
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:274:4 · **resolved** · fingerprint: 5a90765839e065feaea2c67f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:275:78 · **resolved** · fingerprint: 7b3ba7f2b54fbc6ca66fbc67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:276:48 · **resolved** · fingerprint: b53044cd6e868b63415369d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:277:75 · **resolved** · fingerprint: 775b40787e9b3007554a0ec5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:278:68 · **resolved** · fingerprint: b04fa2904d1f6ad6f275ec4c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:288:20 · **resolved** · fingerprint: 96841d15291a7c9a3b97989e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:292:53 · **resolved** · fingerprint: 3ad612336bdf6ad04df13169
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is renamed
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:316:69 · **resolved** · fingerprint: c791b4a9936caab1939af327
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based
- **passive-voice** · skills/the-worker/references/archive-records-and-image-prompts.md:320:84 · **resolved** · fingerprint: 1c8f9ddb3e42b7986914faf3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is authorized
- **semicolon** · skills/the-worker/assets/conversation-integrity-template.md:41:315 · **resolved** · fingerprint: 9767fc93c72cbc1b8b6be8b1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/README.md:17:534 · **resolved** · fingerprint: 73b4936551a1476f572649ed
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted
- **passive-voice** · skills/asd-ste100/SKILL.md:21:69 · **resolved** · fingerprint: 7266e62fe12e7cc92f88c06b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was violated
- **passive-voice** · skills/asd-ste100/SKILL.md:49:227 · **resolved** · fingerprint: 4e26f8ad5ee76bbe5f532dd1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are defined
- **passive-voice** · skills/asd-ste100/SKILL.md:57:60 · **resolved** · fingerprint: 0447fbf776081d483d4a8de4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **phrasal-verb** · skills/asd-ste100/SKILL.md:58:99 · **resolved** · fingerprint: bc3fa2e84f1094e34446f7f9
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** Spin up
- **passive-voice** · skills/asd-ste100/SKILL.md:73:118 · **resolved** · fingerprint: 081cea6a0061b9dd44d263e8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **nominalization** · skills/asd-ste100/SKILL.md:74:53 · **resolved** · fingerprint: f17e13a684f76bb434777eb7
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis
- **present-perfect** · skills/asd-ste100/SKILL.md:79:203 · **resolved** · fingerprint: 97b0da1333b1090e07b7b8c2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · skills/asd-ste100/SKILL.md:81:140 · **resolved** · fingerprint: 87ac5857a6a44a6085f99a33
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed
- **nominalization** · skills/asd-ste100/SKILL.md:89:56 · **resolved** · fingerprint: b0f99a99288209b64ca87fa8
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:79 · **resolved** · fingerprint: e376f8090861f51701cf8a19
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:89 · **resolved** · fingerprint: 0f33fa33abea44edf29a8632
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:107 · **resolved** · fingerprint: b483bbe719cbd32778da4137
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:121 · **resolved** · fingerprint: ea81b9a88d6189c3e9903c71
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:133 · **resolved** · fingerprint: c3ddafa9275694f20a349624
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast
- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:29 · **resolved** · fingerprint: 4b3269c887ff5c340b1876ec
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** spin up
- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:38 · **resolved** · fingerprint: b1d1a41a0e596b342bab207e
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** reach out
- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:49 · **resolved** · fingerprint: d9e6e08d672f564d722faa69
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** dive into
- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:60 · **resolved** · fingerprint: a17ca63c1abfe64d5e677484
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** kick off
- **present-perfect** · skills/asd-ste100/SKILL.md:113:134 · **resolved** · fingerprint: 95fa90f026478e1c3824ab91
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **passive-voice** · skills/asd-ste100/SKILL.md:146:58 · **resolved** · fingerprint: 8f0e185b12ebc8ed1b2a84fa
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized
- **passive-voice** · skills/philosophy-religion-asceticism/README.md:17:11 · **resolved** · fingerprint: 10fe19e3d918086368f3fe12
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are enabled
- **present-perfect** · skills/drawing/references/archive-and-delivery.md:11:167 · **resolved** · fingerprint: 964cabe631fed5dc94a42014
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been verified
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:11:172 · **resolved** · fingerprint: 9b691551f730fb0278640420
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **synonym-rotation** · skills/drawing/references/archive-and-delivery.md:45:13 · **resolved** · fingerprint: 9f0ae35295d64485e1c937b0
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · skills/github-actions/SKILL.md:21:206 · **resolved** · fingerprint: 0dc1e5055d6ed33dfbc9b5d4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · skills/github-actions/SKILL.md:23:59 · **resolved** · fingerprint: f81ea4b00301347b2d2f1455
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **present-perfect** · skills/github-actions/SKILL.md:33:40 · **resolved** · fingerprint: 701a297d4776256937ee58f6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **passive-voice** · skills/drawing/assets/attempt-template.md:61:53 · **resolved** · fingerprint: 54bc3060d325ed44b8a62ae3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:3:121 · **resolved** · fingerprint: 5e242a061496f40752e20b1c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **present-perfect** · skills/drawing/references/patterns/successful-patterns.md:25:23 · **resolved** · fingerprint: 0c43c9aefcafc776120c4656
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been tested
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:25:27 · **resolved** · fingerprint: ab5c52aeee06db5e4aedaddd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:29:218 · **resolved** · fingerprint: 34e6d8f4282135e9b79d9cf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were returned
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:30:188 · **resolved** · fingerprint: 637ad15324468536b31ecfe4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reused
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:47:158 · **resolved** · fingerprint: 2936d742ababd61bba5196c3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being requested
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:13:135 · **resolved** · fingerprint: 79b0a68b86133eedb422b851
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:19:83 · **resolved** · fingerprint: be7d514944589a18a9f9db9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disallowed
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:42:73 · **resolved** · fingerprint: 9f97b1e41f33db726c88c333
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:45:14 · **resolved** · fingerprint: f96d7c6c45b4119df93b13ed
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:47:74 · **resolved** · fingerprint: f96d7c6c45b4119df93b13ed
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:49:12 · **resolved** · fingerprint: 8defbd478033ef0db3a0b656
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was included
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:86:20 · **resolved** · fingerprint: f92adcede423eda0ec4d1115
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:97:52 · **resolved** · fingerprint: b63bcf77584105d5ad091e1c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:119:29 · **resolved** · fingerprint: 9e98e3f9c31cb275ce90f3ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:123:77 · **resolved** · fingerprint: 160e46128e327497aa2a3a64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was approved
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:155:37 · **resolved** · fingerprint: 746f4f3fe8422ec0ab0dde68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:159:37 · **resolved** · fingerprint: f47cc4296d9e8a5663c8308c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:181:62 · **resolved** · fingerprint: 9375e59fa41686a4eb0bad2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:182:28 · **resolved** · fingerprint: 4b6f194f46882ca644424605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:184:296 · **resolved** · fingerprint: 01d3ba03570b64cfafb32a81
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:184:336 · **resolved** · fingerprint: 88fe09b5c3b3525804ef713a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been uploaded
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:185:31 · **resolved** · fingerprint: 4b6f194f46882ca644424605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:186:26 · **resolved** · fingerprint: 5511c926d5a7460dc6f46cb9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:205:20 · **resolved** · fingerprint: 8f0edbc69c4e47b3297c86ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:7:89 · **resolved** · fingerprint: cd523ffc146c3f6901de60f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is designed
- **present-perfect** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:1 · **resolved** · fingerprint: d30efb69e80e577256521942
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been completed
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:5 · **resolved** · fingerprint: 6ff3e39160ad0dff0950e93f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been completed
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:20:13 · **resolved** · fingerprint: 50a2d483f4875f3fb2b04103
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is built
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:37:47 · **resolved** · fingerprint: 375845a698662aa8e2119fb5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:39:38 · **resolved** · fingerprint: 375845a698662aa8e2119fb5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:57:65 · **resolved** · fingerprint: 4b337153e373889fb349022d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:268:11 · **resolved** · fingerprint: 4b337153e373889fb349022d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **passive-voice** · skills/drawing/SKILL.md:107:69 · **resolved** · fingerprint: 64d3910316c7c02208869eec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is requested
- **passive-voice** · skills/drawing/SKILL.md:180:77 · **resolved** · fingerprint: 9a01e5392bd2f640fccc16f8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed
- **passive-voice** · skills/drawing/SKILL.md:189:31 · **resolved** · fingerprint: ae959494a55d88be42e4abf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is packaged
- **passive-voice** · skills/drawing/SKILL.md:207:35 · **resolved** · fingerprint: d87f3bdb2e4a5cd311e567e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/drawing/SKILL.md:208:27 · **resolved** · fingerprint: d87f3bdb2e4a5cd311e567e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/drawing/SKILL.md:209:35 · **resolved** · fingerprint: 4a1561330f4473854edf7d68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded
- **passive-voice** · skills/drawing/SKILL.md:216:76 · **resolved** · fingerprint: 83aca3a3f45f79d0190f037b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **passive-voice** · skills/drawing/SKILL.md:255:21 · **resolved** · fingerprint: 4adc0f726bafb883a943a4c7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are wanted
- **passive-voice** · skills/drawing/SKILL.md:259:15 · **resolved** · fingerprint: 182721976b7c74744cfa668b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · skills/drawing/SKILL.md:290:378 · **resolved** · fingerprint: 182721976b7c74744cfa668b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · skills/drawing/SKILL.md:290:553 · **resolved** · fingerprint: 108fef94cd85af0be9bae737
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **synonym-rotation** · skills/drawing/SKILL.md:363:200 · **resolved** · fingerprint: aa2b4a16cd7d5222231207e6
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · skills/drawing/SKILL.md:363:222 · **resolved** · fingerprint: f718531ecab4f80464bcfc7a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was included
- **passive-voice** · skills/drawing/SKILL.md:363:300 · **resolved** · fingerprint: 182721976b7c74744cfa668b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · skills/drawing/SKILL.md:371:238 · **resolved** · fingerprint: 856947d77008b1a8011c64b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **passive-voice** · skills/drawing/SKILL.md:388:19 · **resolved** · fingerprint: f7c61d976e048fc4d2187457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is refused
- **passive-voice** · skills/drawing/SKILL.md:420:42 · **resolved** · fingerprint: 108fef94cd85af0be9bae737
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/drawing/SKILL.md:421:50 · **resolved** · fingerprint: d518259c92d98a763deb57db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was produced
- **passive-voice** · skills/drawing/SKILL.md:422:42 · **resolved** · fingerprint: a9eeb0708efad4ad4ebac5a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/SKILL.md:426:11 · **resolved** · fingerprint: 2ebc7cf088303cbfd5592603
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **synonym-rotation** · skills/drawing/SKILL.md:444:47 · **resolved** · fingerprint: c41dfa89d8e1360fd85eac2a
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modify
- **present-perfect** · skills/drawing/SKILL.md:447:77 · **resolved** · fingerprint: 1fde6e149badf6f261b22219
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has specified
- **synonym-rotation** · skills/drawing/SKILL.md:449:46 · **resolved** · fingerprint: e9ab9c52b006f1c31b593715
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirmed
- **passive-voice** · skills/drawing/SKILL.md:465:24 · **resolved** · fingerprint: f6cfabada63cd4b942c2fdab
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are determined
- **passive-voice** · skills/drawing/SKILL.md:491:13 · **resolved** · fingerprint: 9ce13cb184b2103476d72b72
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed
- **semicolon** · skills/document-standards/references/document-type-catalog.md:4:279 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:28:139 · **resolved** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:33:453 · **resolved** · fingerprint: bcb83f45ddf38808e5512023
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:37:304 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **semicolon** · skills/document-standards/references/document-type-catalog.md:37:313 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:38:284 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:39:264 · **resolved** · fingerprint: bd13d200f2cd36d327625082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:44:276 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:45:207 · **resolved** · fingerprint: a41ef6bbf64045f943d2af47
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:47:139 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:49:358 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:51:336 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:54:250 · **resolved** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:57:171 · **resolved** · fingerprint: b6bdd9a4073c471e94b40acf
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:57:435 · **resolved** · fingerprint: 4213736a472e3b847e27d1ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived
- **semicolon** · skills/document-standards/references/document-type-catalog.md:57:653 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:58:260 · **resolved** · fingerprint: 33b66dbc6dc280ae7c9be6c8
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:58:546 · **resolved** · fingerprint: 199f2603ee3fb1c3abd18ce6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are skipped
- **semicolon** · skills/document-standards/references/document-type-catalog.md:58:568 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:66:165 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:66:176 · **resolved** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:71:257 · **resolved** · fingerprint: 6192a6cd4c83102388153572
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/document-standards/references/document-type-catalog.md:71:306 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:71:363 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:71:509 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:73:117 · **resolved** · fingerprint: 6192a6cd4c83102388153572
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/document-standards/references/document-type-catalog.md:73:219 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:73:316 · **resolved** · fingerprint: 4b99bc607f23d422ec3ca66d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited
- **semicolon** · skills/document-standards/references/document-type-catalog.md:77:233 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:78:198 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:79:257 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:81:265 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:82:184 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:83:188 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:87:101 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:88:131 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:89:135 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:91:180 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:92:231 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:92:268 · **resolved** · fingerprint: 028b84870f82ee2f98dcbf3b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has run
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:94:169 · **resolved** · fingerprint: bb8de6bc648079b20917fbff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are catalogued
- **semicolon** · skills/document-standards/references/document-type-catalog.md:103:207 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:104:215 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:105:227 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:105:263 · **resolved** · fingerprint: 305641bf283ed85e29efe674
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is published
- **semicolon** · skills/document-standards/references/document-type-catalog.md:106:227 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:107:267 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:109:242 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:110:223 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:115:223 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:117:188 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:117:251 · **resolved** · fingerprint: 195a2fd68103c17c8542eb26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **semicolon** · skills/document-standards/references/document-type-catalog.md:120:117 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:122:140 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:143:39 · **resolved** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:148:200 · **resolved** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:148:479 · **resolved** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:148:483 · **resolved** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:149:136 · **resolved** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:151:131 · **resolved** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:151:206 · **resolved** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:152:199 · **resolved** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:154:262 · **resolved** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:230 · **resolved** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:172:129 · **resolved** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **semicolon** · skills/document-standards/references/document-type-catalog.md:183:185 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:184:138 · **resolved** · fingerprint: d8738c991b456b6b6a7cdd80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconstructed
- **semicolon** · skills/document-standards/references/document-type-catalog.md:184:174 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:187:203 · **resolved** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:196:57 · **resolved** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:200:189 · **resolved** · fingerprint: 7e6ec02ac376dc4e638ffc6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was warranted
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:208:32 · **resolved** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **semicolon** · skills/document-standards/references/document-type-catalog.md:216:203 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-001/verification-report.md:10:34 · **resolved** · fingerprint: 503dc7bce1ba23b2d124a344
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-001/verification-report.md:10:44 · **resolved** · fingerprint: 42e1e6cee4dc601200c8b3a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-001/verification-report.md:10:89 · **resolved** · fingerprint: 59924aa7d58583d2f51d8af5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were retained
- **passive-voice** · workspace/task_board.md:7:110 · **resolved** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/task_board.md:7:137 · **resolved** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · workspace/task_board.md:7:162 · **resolved** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · skills/drawing/references/style-guide.md:60:31 · **resolved** · fingerprint: 581a2555fa37c98ab6bcfea3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was classified
- **present-perfect** · skills/INITIALIZATION_POLICY.md:38:53 · **resolved** · fingerprint: 4f9e87e44f34528956cbd2f3
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved
- **passive-voice** · skills/INITIALIZATION_POLICY.md:38:57 · **resolved** · fingerprint: 25393e4ca29211513c0ea122
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **long-sentence** · skills/INITIALIZATION_POLICY.md:146:3 · **resolved** · fingerprint: f40cb6e7d22052c296f243c7
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · skills/INITIALIZATION_POLICY.md:173:66 · **resolved** · fingerprint: b28796101e8a0d8165b3d79b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:19:108 · **resolved** · fingerprint: 5275280719ed16d2a5b7ad67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is written
- **passive-voice** · workspace/TASK_TEMPLATE.md:47:21 · **resolved** · fingerprint: fdc561df7864672b424ed481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was inspected
- **passive-voice** · workspace/TASK_TEMPLATE.md:74:20 · **resolved** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:75:23 · **resolved** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:85:150 · **resolved** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:44:40 · **resolved** · fingerprint: 1438a8fae83f4cef43ff111f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is inferred
- **present-perfect** · skills/drawing/references/series-continuity-and-iteration.md:50:245 · **resolved** · fingerprint: 8dcbbc229f60c870064ba1c1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has declared
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:78:42 · **resolved** · fingerprint: 37314d6abfb814d104e0fd33
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is ordered
- **present-perfect** · skills/drawing/references/series-continuity-and-iteration.md:82:259 · **resolved** · fingerprint: fd585a05866ee7a0cfc00d99
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has established
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:94:27 · **resolved** · fingerprint: eeef7c60d434b3d4f60ce329
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are locked
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:134:15 · **resolved** · fingerprint: 0854ae12d93b6bb158c85528
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:140:14 · **resolved** · fingerprint: 0854ae12d93b6bb158c85528
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:164:73 · **resolved** · fingerprint: 602406a24344ba12b85a3c26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being edited
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:177:79 · **resolved** · fingerprint: 6bead85653574df77128e560
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:11:24 · **resolved** · fingerprint: 54e6ea18964c8d07234eb34d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:11:46 · **resolved** · fingerprint: 0a843d6680fb0f980128abb5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:12:101 · **resolved** · fingerprint: 0a843d6680fb0f980128abb5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:13:71 · **resolved** · fingerprint: 0a843d6680fb0f980128abb5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:14:71 · **resolved** · fingerprint: 703b35745489e449d29a7979
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were identified
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:16:23 · **resolved** · fingerprint: dc62f6f1e462dc554039b7f1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are restricted
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:16:100 · **resolved** · fingerprint: 0a843d6680fb0f980128abb5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:16:131 · **resolved** · fingerprint: 53482677f474507283576d4c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are rejected
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:17:36 · **resolved** · fingerprint: d8e577514faf6130a4c72560
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were prevalidated
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:19:124 · **resolved** · fingerprint: 0a843d6680fb0f980128abb5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:20:24 · **resolved** · fingerprint: 4de91f2ed3faf88248b04182
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was relocated
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:20:51 · **resolved** · fingerprint: 0a843d6680fb0f980128abb5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:21:20 · **resolved** · fingerprint: 1874d1658204ba42a9b2a7c8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was moved
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-003/verification-report.md:22:57 · **resolved** · fingerprint: 914f4c6926cf8fdde32254dd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were prepared
- **passive-voice** · skills/the-worker/references/image-provenance-and-webp.md:15:100 · **resolved** · fingerprint: 8614398268bd51316f465e56
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · skills/the-worker/references/image-provenance-and-webp.md:27:289 · **resolved** · fingerprint: 93317464da1c1dbf0ae723f5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/references/image-provenance-and-webp.md:27:463 · **resolved** · fingerprint: 42bf16e8c39db9b8087ec2d0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied
- **semicolon** · skills/the-worker/references/image-provenance-and-webp.md:27:588 · **resolved** · fingerprint: 93317464da1c1dbf0ae723f5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/references/image-provenance-and-webp.md:29:418 · **resolved** · fingerprint: 8030ef41b062f29bdeeda991
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted
- **semicolon** · skills/the-worker/references/image-provenance-and-webp.md:29:460 · **resolved** · fingerprint: 93317464da1c1dbf0ae723f5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · skills/the-worker/references/image-provenance-and-webp.md:40:4 · **resolved** · fingerprint: 6621b8a44449ab3404408732
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · skills/the-worker/references/image-provenance-and-webp.md:43:106 · **resolved** · fingerprint: 82c969b497f70d9e180c2327
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated
- **synonym-rotation** · skills/the-worker/references/image-provenance-and-webp.md:43:357 · **resolved** · fingerprint: bfcd67821988f21f547ec19c
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **synonym-rotation** · skills/the-worker/references/image-provenance-and-webp.md:45:50 · **resolved** · fingerprint: 165228fd89d930749cfaa835
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · skills/the-worker/references/image-provenance-and-webp.md:47:139 · **resolved** · fingerprint: 8614398268bd51316f465e56
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · skills/the-worker/references/image-provenance-and-webp.md:57:366 · **resolved** · fingerprint: 93317464da1c1dbf0ae723f5
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/references/image-provenance-and-webp.md:61:65 · **resolved** · fingerprint: 678db87db1d222633995aa3f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **present-perfect** · skills/the-worker/references/image-provenance-and-webp.md:61:138 · **resolved** · fingerprint: 31fa6d94c05533c4e2f9d76a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been read
- **passive-voice** · skills/the-worker/references/image-provenance-and-webp.md:61:143 · **resolved** · fingerprint: fcc7dc911acbecb8434fffce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:11:24 · **resolved** · fingerprint: f0b97e3b799c71824583916b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:11:46 · **resolved** · fingerprint: cf34c78f3b75adc29ca74391
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:12:101 · **resolved** · fingerprint: cf34c78f3b75adc29ca74391
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:13:71 · **resolved** · fingerprint: cf34c78f3b75adc29ca74391
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:14:71 · **resolved** · fingerprint: edaae53fa50b283e635f02e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were identified
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:16:23 · **resolved** · fingerprint: 2c18de9543bceb1f6be63762
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are restricted
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:16:100 · **resolved** · fingerprint: cf34c78f3b75adc29ca74391
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:16:131 · **resolved** · fingerprint: 907d41550724d4ec03b29947
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are rejected
- **semicolon** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:17:34 · **resolved** · fingerprint: cf34c78f3b75adc29ca74391
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:17:44 · **resolved** · fingerprint: 4a029df4fea5d1e261864968
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored
- **passive-voice** · images/takeout/history/2026-11-20-001/attempt-002/verification-report.md:17:89 · **resolved** · fingerprint: bd17ec2b5ba3f1a01952c68c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were retained
- **present-perfect** · skills/asd-ste100/references/writing-rules.md:7:511 · **resolved** · fingerprint: b41b3daad40ce14cd376bd73
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been
- **present-perfect** · skills/asd-ste100/references/writing-rules.md:26:84 · **resolved** · fingerprint: 4b5ee50f1aff2b6dcc346552
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:26:129 · **resolved** · fingerprint: bb10a66696f9dabc2249dc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:27:16 · **resolved** · fingerprint: ac3ecaa3996b4c54c0d3e834
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:30:16 · **resolved** · fingerprint: 773da2a0fc01b2b8333a892c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:31:17 · **resolved** · fingerprint: bb10a66696f9dabc2249dc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:37:58 · **resolved** · fingerprint: 4905d0267d2de525570a8af5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are capped
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:50:5 · **resolved** · fingerprint: 2b19e1e9387f5374b63a7c1f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was designed
- **passive-voice** · skills/philosophy-religion-asceticism/references/answer-patterns.md:29:14 · **resolved** · fingerprint: c179db648027812a0a97ede9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested
- **semicolon** · workspace/README.md:18:113 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/README.md:22:4 · **resolved** · fingerprint: 850ad36627f5885d916de296
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · workspace/README.md:22:64 · **resolved** · fingerprint: f9374751a535ad58835e814f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **passive-voice** · workspace/README.md:22:110 · **resolved** · fingerprint: 28231427e3d00c582576f2b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is updated
- **passive-voice** · workspace/README.md:22:140 · **resolved** · fingerprint: 6e067aa5c3c536cd323a5c6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **passive-voice** · workspace/README.md:34:108 · **resolved** · fingerprint: 4a500644b11ea45e7a256ac0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **synonym-rotation** · workspace/README.md:34:364 · **resolved** · fingerprint: 01eb48b1e6acd03619987cff
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **long-sentence** · workspace/README.md:38:139 · **resolved** · fingerprint: a222143dea70fba6ab12863a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/README.md:38:223 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/the-worker/SKILL.md:15:1 · **resolved** · fingerprint: 8f5fb40f1456d6cdee279897
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · skills/the-worker/SKILL.md:19:127 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/SKILL.md:23:310 · **resolved** · fingerprint: 8df02bfe022ca25e5787bc55
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **long-sentence** · skills/the-worker/SKILL.md:37:38 · **resolved** · fingerprint: 43ee5fc4aa2ab0ab98097505
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · skills/the-worker/SKILL.md:61:61 · **resolved** · fingerprint: 0eebcb0484fe67c4e2017ecc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **passive-voice** · skills/the-worker/SKILL.md:115:111 · **resolved** · fingerprint: d226740cae172dd2e1c78d14
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/the-worker/SKILL.md:304:178 · **resolved** · fingerprint: 48c926404290adf5d27a8438
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked
- **long-sentence** · skills/the-worker/SKILL.md:304:237 · **resolved** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/the-worker/SKILL.md:304:362 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · skills/the-worker/SKILL.md:306:105 · **resolved** · fingerprint: 1ea159f708a07bb12899702f
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verifying
- **semicolon** · skills/the-worker/SKILL.md:307:251 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:309:108 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:310:277 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/SKILL.md:311:140 · **resolved** · fingerprint: f0690d035381adacbc37a83e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · skills/the-worker/SKILL.md:311:200 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:311:242 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/SKILL.md:312:54 · **resolved** · fingerprint: 0888728fc5c2a25c2caac0be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · skills/the-worker/SKILL.md:313:66 · **resolved** · fingerprint: 3003cdc6d38c0022f8be463c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **long-sentence** · skills/the-worker/SKILL.md:313:204 · **resolved** · fingerprint: ead8bfcb0c1049225be6ce1d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · skills/the-worker/SKILL.md:313:330 · **resolved** · fingerprint: 59e52367ff4fbe890c502667
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived
- **long-sentence** · skills/the-worker/SKILL.md:315:188 · **resolved** · fingerprint: 1ca5b3d7c683e38db0ecafeb
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · skills/the-worker/SKILL.md:323:3 · **resolved** · fingerprint: 6d31ffa74d22866fde26008b
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **passive-voice** · skills/the-worker/SKILL.md:325:90 · **resolved** · fingerprint: c2eadbfa652dd24c2decf4de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being removed
- **semicolon** · skills/the-worker/SKILL.md:325:103 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:328:120 · **resolved** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/the-worker/SKILL.md:339:168 · **resolved** · fingerprint: 0e07f428da579362c55d461b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been verified
- **passive-voice** · skills/the-worker/SKILL.md:339:172 · **resolved** · fingerprint: b6cbb5b662b7ac93ef3ba05e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **synonym-rotation** · skills/the-worker/SKILL.md:343:102 · **resolved** · fingerprint: b0d48c1fdb52aa58dc1b1908
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **long-sentence** · skills/the-worker/SKILL.md:344:4 · **resolved** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:13:215 · **resolved** · fingerprint: 404693192feb5c0a1bc279e9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is measured
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:15:69 · **resolved** · fingerprint: ccf5d0ae1e3ac5dfa3d81535
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:46:115 · **resolved** · fingerprint: 620b7d7fd1d18757b7cf5e84
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is phrased
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:56:24 · **resolved** · fingerprint: dbd3657662996413f5b3e09d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:62:24 · **resolved** · fingerprint: 0b65a30e1dc02ac864748bce
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:74:32 · **resolved** · fingerprint: f40577f4f87280d2bafbbb33
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are prohibited
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:80:35 · **resolved** · fingerprint: 1439db2c98d70c1af24c7cd4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being limited
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:89:141 · **resolved** · fingerprint: ca6cd5747867ae19c46def89
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been established
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:91:171 · **resolved** · fingerprint: f1f73777ecdc15c96cdcd383
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:116:33 · **resolved** · fingerprint: c31471d539e8aa39ed2d47c3
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has specified
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:119:41 · **resolved** · fingerprint: 3238ce4831a0652078d996e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is depicted
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:127:120 · **resolved** · fingerprint: 942e61ff7b0fb459a13ad0d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unspecified
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:127:168 · **resolved** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:151:163 · **resolved** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:198:141 · **resolved** · fingerprint: b7f3317fff8f1ff3b74412df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:225:75 · **resolved** · fingerprint: 0b65a30e1dc02ac864748bce
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:244:41 · **resolved** · fingerprint: 292fbd9b5ed50c5247cf2f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:245:103 · **resolved** · fingerprint: 5ea0ac18f64fc9ba3c3b6b6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:246:33 · **resolved** · fingerprint: 8233e35bff35faaf38a980b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been paraphrased
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:247:123 · **resolved** · fingerprint: 753e3e43156f685672332845
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:248:42 · **resolved** · fingerprint: 97a20fbdbe0577e454aefdc8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been preserved
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:249:26 · **resolved** · fingerprint: 13f4a5392eedebe0585ee245
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been limited
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:250:23 · **resolved** · fingerprint: b49d5e45b1b3b1c0140fab39
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been converted
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:265:66 · **resolved** · fingerprint: 278f5a301dede82f4c8ac412
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being submitted
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:268:30 · **resolved** · fingerprint: d88beccb64f34579d80979ff
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been archived
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:268:34 · **resolved** · fingerprint: 8e48ea2de3c2f37bc3a96546
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been archived
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:270:46 · **resolved** · fingerprint: 40f2dda08cf8d4e026bc1cf8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exposed
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:272:98 · **resolved** · fingerprint: 7166cf5d9d622916649b0f8d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was submitted
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:272:197 · **resolved** · fingerprint: 403d89805494afd57b827dee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was authorized
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:289:87 · **resolved** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:300:57 · **resolved** · fingerprint: 4e3b443eb033832d17dc8545
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been checked
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:300:62 · **resolved** · fingerprint: bdcbc53fefbff59427750156
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been checked
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:301:99 · **resolved** · fingerprint: 8854a5a70b9be9bbffa72e61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:302:41 · **resolved** · fingerprint: 83c2d80059f94672d8a71141
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:302:46 · **resolved** · fingerprint: 753e3e43156f685672332845
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:303:106 · **resolved** · fingerprint: 3115ca2ae7a235e7560a1cbc
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been added
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:303:111 · **resolved** · fingerprint: 5ea0ac18f64fc9ba3c3b6b6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:304:31 · **resolved** · fingerprint: c60448dfacfff81b45010545
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been restored
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:304:35 · **resolved** · fingerprint: 292fbd9b5ed50c5247cf2f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:306:58 · **resolved** · fingerprint: ebc3fe4b7983f2625cff09c5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been audited
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:306:62 · **resolved** · fingerprint: 847f9b53906e7b622acde414
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been audited
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:307:27 · **resolved** · fingerprint: 1f52364af2f7476db43a8cf5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been removed
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:307:31 · **resolved** · fingerprint: 4fa531795b4f48c712cb9b8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been removed
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:309:42 · **resolved** · fingerprint: dc5ac767caa168e0bfb3a0be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is assigned
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:309:73 · **resolved** · fingerprint: 2684dd7826880335bb93b3ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was copied
- **synonym-rotation** · skills/document-standards/SKILL.md:22:21 · **resolved** · fingerprint: b1e46093b290a3c3f0ad7363
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **passive-voice** · skills/document-standards/SKILL.md:39:46 · **resolved** · fingerprint: f02e1c27fdc79f6921bf2e16
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **semicolon** · skills/document-standards/SKILL.md:39:137 · **resolved** · fingerprint: 0a9f2f8f059737eb01876e1d
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/SKILL.md:107:229 · **resolved** · fingerprint: 988e824c418cdeb39523dd3c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **semicolon** · skills/drawing/references/image-editing-protocol.md:9:82 · **resolved** · fingerprint: d22425f617c43f7ddbcea655
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/drawing/references/image-editing-protocol.md:33:34 · **resolved** · fingerprint: 3e67ae90c3ab8a6c71da58c3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is confirmed
- **passive-voice** · skills/SESSION_START.md:28:36 · **resolved** · fingerprint: 1b7d224401886a9004746406
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was retrieved
- **semicolon** · skills/SESSION_START.md:31:179 · **resolved** · fingerprint: 8baa1c9f84886b197fcd6710
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/SESSION_START.md:35:114 · **resolved** · fingerprint: 9acf80e5a2b48047e9dd619f
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved
- **passive-voice** · skills/SESSION_START.md:35:119 · **resolved** · fingerprint: fec2fb4fa450910b68502f34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **synonym-rotation** · skills/SESSION_START.md:74:4 · **resolved** · fingerprint: 1fb1875ac91e733b353da2ae
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · skills/SESSION_START.md:75:168 · **resolved** · fingerprint: bafc7f56ccc1107f8e988e9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · skills/SESSION_START.md:76:63 · **resolved** · fingerprint: 6dd94c7c1b750dbf34848556
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · skills/SESSION_START.md:220:174 · **resolved** · fingerprint: bafc7f56ccc1107f8e988e9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · skills/SESSION_START.md:236:217 · **resolved** · fingerprint: ea47a38e16cc241e4c1d2a58
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · skills/SESSION_START.md:260:1 · **resolved** · fingerprint: 2f0f70014ccf6e650b884255
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/drawing/references/patterns/README.md:34:143 · **resolved** · fingerprint: f9d42240cfb6f779e60dcd02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded

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
