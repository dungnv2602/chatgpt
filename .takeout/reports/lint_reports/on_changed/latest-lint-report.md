# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#801](https://github.com/dungnv2602/chatgpt/actions/runs/45817273521)
- **Run ID / attempt:** 45817273521 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / d6ca2fc86a636c7da20fceefca01d1025644f4d9
- **Event:** push
- **Execution mode:** full-audit-fallback
- **Baseline SHA:** Not applicable
- **Linter source SHA:** d6ca2fc86a636c7da20fceefca01d1025644f4d9
- **Generated (UTC):** 2026-11-26T12:12:03.111590+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 89 |
| Files that failed | 34 |
| Files with findings | 64 |
| Total findings | 756 |
| Hard findings | 314 |
| Advisory findings | 442 |
| New findings | 0 |
| Recurring findings | 756 |
| Resolved findings | 1 |
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
- workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md
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
| .agent/skills/skill-creator/agents/grader.md | FAIL | 4 | 1 | 0 | 998 | 0.4 | 1 |
| .agent/skills/skill-creator/agents/analyzer.md | FAIL | 4 | 1 | 0 | 1147 | 0.3 | 1 |
| .agent/skills/the-worker/references/image-provenance-and-webp.md | FAIL | 15 | 7 | 0 | 1248 | 1.2 | 1 |
| .agent/skills/drawing/SKILL.md | PASS | 26 | 3 | 24 | 4899 | 0.5 | 0 |
| .agent/skills/doc-coauthoring/SKILL.md | FAIL | 28 | 9 | 0 | 2456 | 1.1 | 1 |
| .agent/skills/the-worker/assets/session-brief-template.md | PASS | 0 | 0 | 0 | 288 | 0.0 | 0 |
| .agent/INITIALIZATION_POLICY.md | PASS | 5 | 2 | 4 | 1551 | 0.3 | 0 |
| .agent/skills/internal-comms/SKILL.md | FAIL | 1 | 1 | 0 | 196 | 0.5 | 1 |
| .agent/skills/drawing/references/archive-and-delivery.md | PASS | 3 | 1 | 7 | 458 | 0.7 | 0 |
| .agent/skills/grilling/SKILL.md | FAIL | 6 | 4 | 0 | 289 | 2.1 | 1 |
| .agent/skills/internal-comms/examples/3p-updates.md | FAIL | 3 | 1 | 0 | 552 | 0.5 | 1 |
| .agent/skills/drawing/README.md | PASS | 0 | 0 | 0 | 406 | 0.0 | 0 |
| .agent/skills/theme-factory/themes/midnight-galaxy.md | PASS | 0 | 0 | 0 | 70 | 0.0 | 0 |
| .agent/skills/skill-creator/SKILL.md | FAIL | 49 | 43 | 0 | 4775 | 1.0 | 1 |
| workspace/adr/README.md | PASS | 0 | 0 | 0 | 523 | 0.0 | 0 |
| .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md | PASS | 8 | 0 | 7 | 2716 | 0.3 | 0 |
| .agent/skills/drawing/references/patterns/README.md | PASS | 1 | 0 | 0 | 795 | 0.1 | 0 |
| workspace/ADR_TEMPLATE.md | PASS | 0 | 0 | 0 | 349 | 0.0 | 0 |
| .agent/skills/xlsx/SKILL.md | FAIL | 34 | 25 | 0 | 1408 | 2.4 | 1 |
| .takeout/images/README-2.md | FAIL | 10 | 2 | 0 | 2048 | 0.5 | 1 |
| .agent/skills/theme-factory/themes/sunset-boulevard.md | PASS | 0 | 0 | 0 | 76 | 0.0 | 0 |
| .agent/skills/drawing/references/patterns/successful-patterns.md | PASS | 6 | 0 | 0 | 816 | 0.7 | 0 |
| workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | FAIL | 43 | 21 | 0 | 3304 | 1.3 | 1 |
| .agent/skills/define-goal/SKILL.md | FAIL | 11 | 9 | 0 | 857 | 1.3 | 1 |
| .agent/skills/drawing/references/generation-recovery-and-provenance.md | PASS | 19 | 0 | 17 | 2756 | 0.7 | 0 |
| .agent/skills/internal-comms/examples/faq-answers.md | FAIL | 7 | 4 | 0 | 403 | 1.7 | 1 |
| .agent/skills/README.md | PASS | 0 | 0 | 0 | 425 | 0.0 | 0 |
| .agent/skills/drawing/references/style-guide.md | PASS | 1 | 0 | 0 | 462 | 0.2 | 0 |
| .agent/skills/github-actions/SKILL.md | PASS | 3 | 0 | 0 | 2534 | 0.1 | 0 |
| .agent/skills/drawing/assets/attempt-template.md | PASS | 1 | 0 | 0 | 593 | 0.2 | 0 |
| .agent/skills/theme-factory/themes/ocean-depths.md | PASS | 0 | 0 | 0 | 76 | 0.0 | 0 |
| .agent/SESSION_START.md | FAIL | 10 | 3 | 0 | 2702 | 0.4 | 1 |
| .agent/skills/theme-factory/themes/modern-minimalist.md | PASS | 0 | 0 | 0 | 74 | 0.0 | 0 |
| .agent/skills/the-worker/assets/session-summary-template.md | PASS | 0 | 0 | 0 | 106 | 0.0 | 0 |
| .agent/skills/the-worker/SKILL.md | PASS | 0 | 0 | 0 | 5288 | 0.0 | 0 |
| .agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md | PASS | 0 | 0 | 0 | 166 | 0.0 | 0 |
| workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md | FAIL | 50 | 23 | 0 | 9822 | 0.5 | 1 |
| .agent/skills/philosophy-religion-asceticism/references/source-standards.md | PASS | 2 | 0 | 1 | 1467 | 0.1 | 0 |
| .agent/skills/philosophy-religion-asceticism/SKILL.md | PASS | 8 | 0 | 7 | 2387 | 0.3 | 0 |
| .agent/skills/internal-comms/examples/general-comms.md | PASS | 1 | 0 | 0 | 85 | 1.2 | 0 |
| .agent/skills/pdf/REFERENCE.md | PASS | 0 | 0 | 0 | 394 | 0.0 | 0 |
| .agent/skills/decision-governance/SKILL.md | FAIL | 9 | 5 | 0 | 2913 | 0.3 | 1 |
| .agent/skills/asd-ste100/references/writing-rules.md | PASS | 8 | 0 | 6 | 706 | 1.1 | 0 |
| .agent/skills/drawing/references/series-continuity-and-iteration.md | PASS | 9 | 0 | 9 | 3262 | 0.3 | 0 |
| .agent/skills/document-standards/references/document-type-catalog.md | FAIL | 7 | 4 | 0 | 4632 | 0.2 | 1 |
| .agent/skills/the-worker/references/archive-records-and-image-prompts.md | FAIL | 28 | 3 | 0 | 3538 | 0.8 | 1 |
| .agent/skills/drawing/references/image-editing-protocol.md | PASS | 2 | 1 | 4 | 474 | 0.4 | 0 |
| .agent/skills/agent-skill-authoring/SKILL.md | PASS | 15 | 0 | 6 | 2260 | 0.7 | 0 |
| .agent/skills/philosophy-religion-asceticism/README.md | PASS | 1 | 0 | 0 | 471 | 0.2 | 0 |
| .takeout/images/README-1.md | PASS | 1 | 0 | 0 | 314 | 0.3 | 0 |
| .agent/skills/theme-factory/themes/golden-hour.md | PASS | 0 | 0 | 0 | 71 | 0.0 | 0 |
| .agent/skills/the-worker/references/conversation-mode.md | FAIL | 19 | 2 | 0 | 3185 | 0.6 | 1 |
| .agent/skills/internal-comms/examples/company-newsletter.md | FAIL | 4 | 1 | 0 | 554 | 0.7 | 1 |
| .agent/skills/skill-creator/agents/comparator.md | FAIL | 6 | 1 | 0 | 735 | 0.8 | 1 |
| workspace/task_board.md | FAIL | 1 | 1 | 0 | 246 | 0.4 | 1 |
| .agent/skills/theme-factory/themes/desert-rose.md | PASS | 0 | 0 | 0 | 68 | 0.0 | 0 |
| workspace/analysis/README.md | PASS | 0 | 0 | 0 | 278 | 0.0 | 0 |
| .agent/skills/asd-ste100/README.md | PASS | 2 | 0 | 0 | 1573 | 0.1 | 0 |
| workspace/ANALYSIS_TEMPLATE.md | PASS | 1 | 0 | 0 | 384 | 0.3 | 0 |
| .agent/skills/the-worker/references/image-processing-scripts.md | PASS | 0 | 0 | 0 | 340 | 0.0 | 0 |
| .agent/skills/document-standards/SKILL.md | FAIL | 4 | 2 | 0 | 1044 | 0.4 | 1 |
| .agent/skills/migrate-to-rust/SKILL.md | FAIL | 21 | 15 | 0 | 1173 | 1.8 | 1 |
| .agent/skills/theme-factory/themes/forest-canopy.md | PASS | 0 | 0 | 0 | 68 | 0.0 | 0 |
| .agent/skills/skill-creator/references/schemas.md | PASS | 3 | 0 | 0 | 518 | 0.6 | 0 |
| workspace/draft/README.md | FAIL | 4 | 3 | 0 | 664 | 0.6 | 1 |
| workspace/TASK_TEMPLATE.md | PASS | 5 | 0 | 0 | 461 | 1.1 | 0 |
| .agent/skills/pdf/FORMS.md | FAIL | 13 | 8 | 0 | 1195 | 1.1 | 1 |
| .agent/skills/theme-factory/themes/arctic-frost.md | PASS | 0 | 0 | 0 | 73 | 0.0 | 0 |
| .agent/skills/pdf/SKILL.md | FAIL | 1 | 1 | 0 | 347 | 0.3 | 1 |
| .agent/skills/drawing/references/prompt-fidelity.md | PASS | 45 | 0 | 15 | 3676 | 1.2 | 0 |
| .agent/skills/theme-factory/themes/botanical-garden.md | PASS | 0 | 0 | 0 | 69 | 0.0 | 0 |
| .agent/skills/philosophy-religion-asceticism/references/research-method.md | PASS | 0 | 0 | 0 | 559 | 0.0 | 0 |
| .agent/skills/philosophy-religion-asceticism/CHANGELOG.md | PASS | 0 | 0 | 0 | 56 | 0.0 | 0 |
| .agent/skills/drawing/references/patterns/failure-patterns.md | PASS | 25 | 0 | 0 | 2146 | 1.2 | 0 |
| workspace/README.md | PASS | 0 | 0 | 0 | 883 | 0.0 | 0 |
| .agent/skills/drawing/assets/daily-index-template.md | PASS | 0 | 0 | 0 | 210 | 0.0 | 0 |
| .agent/skills/theme-factory/themes/tech-innovation.md | FAIL | 1 | 1 | 0 | 73 | 1.4 | 1 |
| .agent/skills/the-worker/references/drawing-session-closeout.md | PASS | 1 | 0 | 0 | 612 | 0.2 | 0 |
| .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md | PASS | 1 | 0 | 0 | 235 | 0.4 | 0 |
| .agent/skills/drawing/assets/pattern-entry-templates.md | PASS | 9 | 0 | 0 | 562 | 1.6 | 0 |
| .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md | FAIL | 13 | 10 | 0 | 1274 | 1.0 | 1 |
| .agent/skills/asd-ste100/SKILL.md | PASS | 20 | 12 | 31 | 2609 | 0.8 | 0 |
| .agent/skills/asd-ste100/assets/lint-report-template.md | PASS | 0 | 0 | 0 | 385 | 0.0 | 0 |
| workspace/DRAFT_TEMPLATE.md | FAIL | 9 | 4 | 0 | 1242 | 0.7 | 1 |
| .agent/skills/discernment-nudge/SKILL.md | FAIL | 26 | 24 | 0 | 1701 | 1.5 | 1 |
| workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md | FAIL | 75 | 53 | 0 | 8961 | 0.8 | 1 |
| .agent/skills/asd-ste100/references/repository-writing-policy.md | PASS | 1 | 0 | 0 | 570 | 0.2 | 0 |
| .agent/skills/theme-factory/SKILL.md | FAIL | 6 | 2 | 0 | 473 | 1.3 | 1 |
| .agent/skills/the-worker/assets/conversation-integrity-template.md | FAIL | 1 | 1 | 0 | 290 | 0.3 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 387 |
| long-sentence | 137 |
| semicolon | 110 |
| present-perfect | 55 |
| synonym-rotation | 54 |
| marketing-adjective | 6 |
| phrasal-verb | 5 |
| nominalization | 2 |

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
Ran 4 tests in 0.353s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.007s

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
Scanned 227 active Markdown files (303 available as link targets) and 341 local Markdown links.
Found 1 unresolved local Markdown targets or anchors.
workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md: missing Markdown file: ../../.archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

- **synonym-rotation** · .agent/skills/skill-creator/agents/grader.md:43:25 · **recurring** · fingerprint: 3ed0684ea12e354d46eea6bf
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · .agent/skills/skill-creator/agents/grader.md:50:34 · **recurring** · fingerprint: 6108d0ad8d8376fa45ce1bd8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were filled
- **passive-voice** · .agent/skills/skill-creator/agents/grader.md:55:53 · **recurring** · fingerprint: 08a61d6427184a2b733e6f62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · .agent/skills/skill-creator/agents/grader.md:204:30 · **recurring** · fingerprint: 54f29ef94b400956a5d9ef80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being verified
- **passive-voice** · .agent/skills/skill-creator/agents/analyzer.md:45:17 · **recurring** · fingerprint: 572d49165f68a06f3192f854
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were used
- **synonym-rotation** · .agent/skills/skill-creator/agents/analyzer.md:81:27 · **recurring** · fingerprint: 8618828539ad472e64245b5f
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modify
- **present-perfect** · .agent/skills/skill-creator/agents/analyzer.md:161:61 · **recurring** · fingerprint: f0e79378bd6b3ccceef251d9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have changed
- **passive-voice** · .agent/skills/skill-creator/agents/analyzer.md:200:37 · **recurring** · fingerprint: d37ba5ddd11156c4f02b3fb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being benchmarked
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:15:100 · **recurring** · fingerprint: 42ccfb93a745583fff3188b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:293 · **recurring** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:467 · **recurring** · fingerprint: caa7a81dbcbd2ca9a41f3f6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied
- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:592 · **recurring** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:29:579 · **recurring** · fingerprint: 327d345785066c739b823948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted
- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:29:621 · **recurring** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:40:4 · **recurring** · fingerprint: 691140761bb44de115fa7cff
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:43:106 · **recurring** · fingerprint: 6d33e304d616c2a0e3cf5f55
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated
- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:43:357 · **recurring** · fingerprint: 5e4c8482fd167c730eb47fe1
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:45:50 · **recurring** · fingerprint: cd327a2cb9681d781a088b3a
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:47:139 · **recurring** · fingerprint: 42ccfb93a745583fff3188b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:57:366 · **recurring** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:65 · **recurring** · fingerprint: eda9543144c60d68e835bcc2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **present-perfect** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:138 · **recurring** · fingerprint: 3e65c7310bbf6667184ee5cf
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been read
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:143 · **recurring** · fingerprint: 0b7ac6199463b1f46f7ddf4f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · .agent/skills/drawing/SKILL.md:107:69 · **recurring** · fingerprint: 878ab3b6dde18c0e7cecb1b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is requested
- **passive-voice** · .agent/skills/drawing/SKILL.md:180:77 · **recurring** · fingerprint: 70e71f064591705fb5f3c193
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed
- **passive-voice** · .agent/skills/drawing/SKILL.md:189:31 · **recurring** · fingerprint: 1ed5dffcee6e3b4ff82826e6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is packaged
- **passive-voice** · .agent/skills/drawing/SKILL.md:207:35 · **recurring** · fingerprint: af4c1dada33dd8c4ae145291
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · .agent/skills/drawing/SKILL.md:208:27 · **recurring** · fingerprint: af4c1dada33dd8c4ae145291
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · .agent/skills/drawing/SKILL.md:209:35 · **recurring** · fingerprint: 6e55a67e178c1b3912ead6ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded
- **passive-voice** · .agent/skills/drawing/SKILL.md:216:76 · **recurring** · fingerprint: 5b854191f0bd6325026a19b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **passive-voice** · .agent/skills/drawing/SKILL.md:255:21 · **recurring** · fingerprint: 2651d6044c8c968e365347e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are wanted
- **passive-voice** · .agent/skills/drawing/SKILL.md:259:15 · **recurring** · fingerprint: 7b7c5868ffded58b304476b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · .agent/skills/drawing/SKILL.md:290:382 · **recurring** · fingerprint: 7b7c5868ffded58b304476b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · .agent/skills/drawing/SKILL.md:290:557 · **recurring** · fingerprint: ea0cd474de27d7ba90f9b7fb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **synonym-rotation** · .agent/skills/drawing/SKILL.md:363:200 · **recurring** · fingerprint: 0cb5a57ca33c0b3b9c952ac3
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .agent/skills/drawing/SKILL.md:363:222 · **recurring** · fingerprint: d757e8ed6034e6ce6760ff48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was included
- **passive-voice** · .agent/skills/drawing/SKILL.md:363:300 · **recurring** · fingerprint: 7b7c5868ffded58b304476b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · .agent/skills/drawing/SKILL.md:371:238 · **recurring** · fingerprint: 07b4ec6dcfb61be8e9a2c72b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **passive-voice** · .agent/skills/drawing/SKILL.md:388:19 · **recurring** · fingerprint: 59195f4fed84f98241ef6837
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is refused
- **passive-voice** · .agent/skills/drawing/SKILL.md:420:42 · **recurring** · fingerprint: ea0cd474de27d7ba90f9b7fb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/drawing/SKILL.md:421:50 · **recurring** · fingerprint: 12868b6cbd963577744ae291
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was produced
- **passive-voice** · .agent/skills/drawing/SKILL.md:422:42 · **recurring** · fingerprint: 44599ec66070748c61d0019f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/skills/drawing/SKILL.md:426:11 · **recurring** · fingerprint: ae23dc4e6ea7f38ced45381f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/drawing/SKILL.md:438:58 · **recurring** · fingerprint: 5523d48c475ed4874a2175cb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is warranted
- **synonym-rotation** · .agent/skills/drawing/SKILL.md:459:47 · **recurring** · fingerprint: f80cb025f7c2a164b46dd70d
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modify
- **present-perfect** · .agent/skills/drawing/SKILL.md:462:77 · **recurring** · fingerprint: 4f907506abc94065c68b9303
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has specified
- **synonym-rotation** · .agent/skills/drawing/SKILL.md:464:46 · **recurring** · fingerprint: 3b58c82498a5ccdfc67852a1
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirmed
- **passive-voice** · .agent/skills/drawing/SKILL.md:480:24 · **recurring** · fingerprint: 2c7485ca908820b38aaade5e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are determined
- **passive-voice** · .agent/skills/drawing/SKILL.md:506:13 · **recurring** · fingerprint: 33a3fa0cff6f306a7a93ed80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed
- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:51:3 · **recurring** · fingerprint: b380e4795a1a535489af55a3
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:56:24 · **recurring** · fingerprint: e87615dcfea419143effe3a1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are answered
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:59:36 · **recurring** · fingerprint: 092e1440d84765a5998b315a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:65:53 · **recurring** · fingerprint: 785133e6de68fcf2ed362c2b
  - **Level:** advisory-free
  - **Message:** 'get' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** get
- **long-sentence** · .agent/skills/doc-coauthoring/SKILL.md:72:1 · **recurring** · fingerprint: 2a35f373caf351d2f1c207c4
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:72:22 · **recurring** · fingerprint: 7c6314612e64721268d82086
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:86:42 · **recurring** · fingerprint: d79f53a20eb266137f9d3a6b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being learned
- **long-sentence** · .agent/skills/doc-coauthoring/SKILL.md:94:1 · **recurring** · fingerprint: e83becde0a03b66c61fc8fee
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **present-perfect** · .agent/skills/doc-coauthoring/SKILL.md:97:20 · **recurring** · fingerprint: c43f81bd5eac082a83c3133a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been gathered
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:97:24 · **recurring** · fingerprint: 74f86169528f05b065c139b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been gathered
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:130:18 · **recurring** · fingerprint: f917bd3233f553bd15d7c0db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is agreed
- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:150:1 · **recurring** · fingerprint: 8d2d00522d8a837061c5ed1b
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **present-perfect** · .agent/skills/doc-coauthoring/SKILL.md:150:22 · **recurring** · fingerprint: c41f0a7ece739120265c01ab
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been created
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:150:26 · **recurring** · fingerprint: 94d4a5350ff0f65c87fcaed1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:156:20 · **recurring** · fingerprint: ed5186d0643ee8e5788c6553
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **present-perfect** · .agent/skills/doc-coauthoring/SKILL.md:200:40 · **recurring** · fingerprint: 7ddbdeee5e1488d5616700c5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been drafted
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:200:44 · **recurring** · fingerprint: a9cf321d719d8e5a4c878b43
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been drafted
- **long-sentence** · .agent/skills/doc-coauthoring/SKILL.md:202:1 · **recurring** · fingerprint: b97bc94bd9213a4c44e510b6
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/doc-coauthoring/SKILL.md:211:3 · **recurring** · fingerprint: 8ca3e39b1c98ae537285ec47
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:213:35 · **recurring** · fingerprint: 2160c31596b4f3fb5f40637c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:219:14 · **recurring** · fingerprint: e61aceb66bd95a2609f26a21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:233:21 · **recurring** · fingerprint: 36940177a105aa74789ecc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:234:23 · **recurring** · fingerprint: 36940177a105aa74789ecc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted
- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:312:30 · **recurring** · fingerprint: 602cc782aa5df3313fae814f
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct
- **present-perfect** · .agent/skills/doc-coauthoring/SKILL.md:336:18 · **recurring** · fingerprint: 700bd4a73778993f60baf63d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has passed
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:342:50 · **recurring** · fingerprint: e61aceb66bd95a2609f26a21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:346:84 · **recurring** · fingerprint: ca548ddaee5fc2417d9c9385
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was developed
- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:348:30 · **recurring** · fingerprint: 952ffdaac946082abede5a85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is received
- **present-perfect** · .agent/INITIALIZATION_POLICY.md:38:53 · **recurring** · fingerprint: a68d4b2091de8244b08b0984
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:38:57 · **recurring** · fingerprint: cc8f76f7786acf5d8492b443
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **long-sentence** · .agent/INITIALIZATION_POLICY.md:146:3 · **recurring** · fingerprint: 18db183bae30a8739132c97b
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:155:154 · **recurring** · fingerprint: 0bd04eaf142f6db0f46ab9bd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored
- **semicolon** · .agent/INITIALIZATION_POLICY.md:184:66 · **recurring** · fingerprint: 79226f1a409be7642928b566
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/internal-comms/SKILL.md:3:136 · **recurring** · fingerprint: 536e2e7ba4848c22f116b688
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **present-perfect** · .agent/skills/drawing/references/archive-and-delivery.md:11:167 · **recurring** · fingerprint: c5d02a5017b863230f3b252a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been verified
- **passive-voice** · .agent/skills/drawing/references/archive-and-delivery.md:11:172 · **recurring** · fingerprint: 6c7d74fe7edec2361ca15c24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **synonym-rotation** · .agent/skills/drawing/references/archive-and-delivery.md:45:13 · **recurring** · fingerprint: 8d54e05e87ff737f0d036438
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **long-sentence** · .agent/skills/grilling/SKILL.md:28:48 · **recurring** · fingerprint: bee2beaf2e1eb932b38195e7
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · .agent/skills/grilling/SKILL.md:28:193 · **recurring** · fingerprint: bf801ae5817722c54dd2a44b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/grilling/SKILL.md:28:255 · **recurring** · fingerprint: a1d366861065f2ff55895993
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · .agent/skills/grilling/SKILL.md:28:397 · **recurring** · fingerprint: bf801ae5817722c54dd2a44b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/grilling/SKILL.md:30:13 · **recurring** · fingerprint: 37bb72090ae983ecb14eb362
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **present-perfect** · .agent/skills/grilling/SKILL.md:30:166 · **recurring** · fingerprint: aec45cb5f1f28de5e7c0d37a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **passive-voice** · .agent/skills/internal-comms/examples/3p-updates.md:2:9 · **recurring** · fingerprint: 2fb37222a40a36ee64a89558
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · .agent/skills/internal-comms/examples/3p-updates.md:4:141 · **recurring** · fingerprint: f725d493718a8ba218869f2c
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **present-perfect** · .agent/skills/internal-comms/examples/3p-updates.md:7:28 · **recurring** · fingerprint: d8b362e021a14da1a7239b46
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has accomplished
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:3:100 · **recurring** · fingerprint: c0128c8cbc5de6229042e665
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:16:5 · **recurring** · fingerprint: b74a4ea33e6c64c04b84cd24
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:16:182 · **recurring** · fingerprint: 1ff41be9696d1a59f1840bb2
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:18:3 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:22:1 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:22:213 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:26:1 · **recurring** · fingerprint: 8effdf0ea562678b8a496c79
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:28:1 · **recurring** · fingerprint: b619282f2a5a1fd5e4b7bfbe
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · .agent/skills/skill-creator/SKILL.md:28:22 · **recurring** · fingerprint: c93247a38d888c7b3de90997
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:34:105 · **recurring** · fingerprint: a22ffb60a808d0d6b87d943d
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:39:3 · **recurring** · fingerprint: 0144c24eee82255498c96af9
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:41:1 · **recurring** · fingerprint: be024ce86df5418f04fe2f9a
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:54:35 · **recurring** · fingerprint: c08f6eef4e964b84145e106f
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:60:1 · **recurring** · fingerprint: 39093e7b1986c825d3ea89a1
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:67:398 · **recurring** · fingerprint: b2a04b8c675cc2a131a9420c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:67:467 · **recurring** · fingerprint: c5763365a63d688477d18164
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** display
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:67:592 · **recurring** · fingerprint: 7453e8516a384f818b51a5bb
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:96:3 · **recurring** · fingerprint: 7453e8516a384f818b51a5bb
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **semicolon** · .agent/skills/skill-creator/SKILL.md:96:32 · **recurring** · fingerprint: ffbd5dd7fe5b566a79c3f5ce
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:171:190 · **recurring** · fingerprint: d1d1f4eacd81ba68da187af9
  - **Level:** advisory-free
  - **Message:** 'launch' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** Launch
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:203:1 · **recurring** · fingerprint: be024ce86df5418f04fe2f9a
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/skill-creator/SKILL.md:223:15 · **recurring** · fingerprint: c641af7a17b87772a029e0ee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are done
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:225:386 · **recurring** · fingerprint: 063eab38cb8b453553940fb6
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:234:106 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · .agent/skills/skill-creator/SKILL.md:249:57 · **recurring** · fingerprint: ffbd5dd7fe5b566a79c3f5ce
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/skill-creator/SKILL.md:256:29 · **recurring** · fingerprint: cb5d2b8747a0ba90b3ee437b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was given
- **passive-voice** · .agent/skills/skill-creator/SKILL.md:259:33 · **recurring** · fingerprint: 9065f6de65e3a15641cce538
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run
- **present-perfect** · .agent/skills/skill-creator/SKILL.md:294:68 · **recurring** · fingerprint: 4d285f47dacf2b7c3b058584
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has reviewed
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:298:38 · **recurring** · fingerprint: b2a04b8c675cc2a131a9420c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:298:522 · **recurring** · fingerprint: 8effdf0ea562678b8a496c79
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:300:78 · **recurring** · fingerprint: 9e45bb53cb53b0272be7c185
  - **Level:** advisory-free
  - **Message:** Sentence has 52 words (cap 25). Split it.
  - **Matched text:** 52 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:302:255 · **recurring** · fingerprint: 02795ed552c2e6222c40b77d
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:302:485 · **recurring** · fingerprint: 6c92d547d198a40e19ee323d
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:304:50 · **recurring** · fingerprint: 0144c24eee82255498c96af9
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/skill-creator/SKILL.md:306:138 · **recurring** · fingerprint: ffbd5dd7fe5b566a79c3f5ce
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:313:214 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:327:1 · **recurring** · fingerprint: c10b33c4d79df51c6b9682af
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:348:429 · **recurring** · fingerprint: 063eab38cb8b453553940fb6
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:356:1 · **recurring** · fingerprint: 0144c24eee82255498c96af9
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:356:187 · **recurring** · fingerprint: b619282f2a5a1fd5e4b7bfbe
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:394:56 · **recurring** · fingerprint: c0128c8cbc5de6229042e665
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:394:362 · **recurring** · fingerprint: 8effdf0ea562678b8a496c79
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:398:228 · **recurring** · fingerprint: 28c50f5addd36eab74a135cb
  - **Level:** advisory-free
  - **Message:** Sentence has 47 words (cap 25). Split it.
  - **Matched text:** 47 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:424:206 · **recurring** · fingerprint: 7453e8516a384f818b51a5bb
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:426:264 · **recurring** · fingerprint: bb3182e438b02d99f7821313
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:451:3 · **recurring** · fingerprint: f0c41082c1096f144d45e58c
  - **Level:** advisory-free
  - **Message:** Sentence has 66 words (cap 25). Split it.
  - **Matched text:** 66 words
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:454:3 · **recurring** · fingerprint: b619282f2a5a1fd5e4b7bfbe
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · .agent/skills/skill-creator/SKILL.md:480:33 · **recurring** · fingerprint: 479ee2cb0da9e9d902d6bfb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **long-sentence** · .agent/skills/skill-creator/SKILL.md:483:93 · **recurring** · fingerprint: 0144c24eee82255498c96af9
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:7:89 · **recurring** · fingerprint: 164d4067e1e89a1f2ae2ca64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is designed
- **present-perfect** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:1 · **recurring** · fingerprint: 2ad598367272b6e37f11bb9f
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been completed
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:5 · **recurring** · fingerprint: a96bc88cfe9eb32ee5d37d49
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been completed
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:20:13 · **recurring** · fingerprint: 7be16217c093138da7f26077
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is built
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:37:47 · **recurring** · fingerprint: e6b31276bf3e3fe5b518d539
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:39:38 · **recurring** · fingerprint: e6b31276bf3e3fe5b518d539
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:57:65 · **recurring** · fingerprint: c4ef08a0a9dea42add5ac36c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:268:11 · **recurring** · fingerprint: c4ef08a0a9dea42add5ac36c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **passive-voice** · .agent/skills/drawing/references/patterns/README.md:34:143 · **recurring** · fingerprint: 8ea61fc966fb2cb721264549
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **long-sentence** · .agent/skills/xlsx/SKILL.md:3:90 · **recurring** · fingerprint: bc255bb6ff9d923c5f3753b7
  - **Level:** advisory-free
  - **Message:** Sentence has 50 words (cap 25). Split it.
  - **Matched text:** 50 words
- **semicolon** · .agent/skills/xlsx/SKILL.md:3:297 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/xlsx/SKILL.md:3:363 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/xlsx/SKILL.md:3:406 · **recurring** · fingerprint: a1017e69a4c1eaf91ce78914
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · .agent/skills/xlsx/SKILL.md:3:776 · **recurring** · fingerprint: 9e5463e9eb5bd2f364ef7820
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/xlsx/SKILL.md:3:953 · **recurring** · fingerprint: 9f552b549d8874f678a17d04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is involved
- **semicolon** · .agent/skills/xlsx/SKILL.md:13:80 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/xlsx/SKILL.md:16:42 · **recurring** · fingerprint: f40d0bf8e882628eef890729
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preinstalled
- **semicolon** · .agent/skills/xlsx/SKILL.md:16:91 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/xlsx/SKILL.md:23:79 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/xlsx/SKILL.md:26:246 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/xlsx/SKILL.md:27:3 · **recurring** · fingerprint: 9e5463e9eb5bd2f364ef7820
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/xlsx/SKILL.md:27:207 · **recurring** · fingerprint: 18a172b98eb69eb6ddd99c43
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were asked
- **long-sentence** · .agent/skills/xlsx/SKILL.md:40:1 · **recurring** · fingerprint: 0646b97517ca5d69236b9007
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **long-sentence** · .agent/skills/xlsx/SKILL.md:44:8 · **recurring** · fingerprint: 9e5463e9eb5bd2f364ef7820
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/xlsx/SKILL.md:44:71 · **recurring** · fingerprint: baad3877e021c564d5e1c82d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was recalculated
- **semicolon** · .agent/skills/xlsx/SKILL.md:55:40 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/xlsx/SKILL.md:58:80 · **recurring** · fingerprint: 685502200eabe22e68ffa6b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed
- **long-sentence** · .agent/skills/xlsx/SKILL.md:66:3 · **recurring** · fingerprint: 9e5463e9eb5bd2f364ef7820
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **long-sentence** · .agent/skills/xlsx/SKILL.md:67:81 · **recurring** · fingerprint: ea4acdb6652afd8c9eb38361
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/xlsx/SKILL.md:68:17 · **recurring** · fingerprint: f15854036a61bd943ceeea97
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reported
- **synonym-rotation** · .agent/skills/xlsx/SKILL.md:68:148 · **recurring** · fingerprint: 1f0dd672e3d5dfbde97b90fb
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **semicolon** · .agent/skills/xlsx/SKILL.md:72:100 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/xlsx/SKILL.md:75:116 · **recurring** · fingerprint: 55449c75856b6d1a3dc4263d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **semicolon** · .agent/skills/xlsx/SKILL.md:78:160 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/xlsx/SKILL.md:79:3 · **recurring** · fingerprint: 1b6abd36a2b499ad1787511b
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · .agent/skills/xlsx/SKILL.md:79:167 · **recurring** · fingerprint: 85c2fc0ec973eb11117dc903
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are saved
- **passive-voice** · .agent/skills/xlsx/SKILL.md:80:37 · **recurring** · fingerprint: bb17ecc485a14e6012fc6236
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is flattened
- **semicolon** · .agent/skills/xlsx/SKILL.md:80:90 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/xlsx/SKILL.md:82:3 · **recurring** · fingerprint: 3e44e64ba0811cfeb37369fa
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words
- **long-sentence** · .agent/skills/xlsx/SKILL.md:89:1 · **recurring** · fingerprint: ba2566fcf1c485f752996553
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **long-sentence** · .agent/skills/xlsx/SKILL.md:93:1 · **recurring** · fingerprint: a1017e69a4c1eaf91ce78914
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · .agent/skills/xlsx/SKILL.md:95:68 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/xlsx/SKILL.md:98:1 · **recurring** · fingerprint: 8045b4020231327ee7344fe3
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **passive-voice** · .takeout/images/README-2.md:26:255 · **recurring** · fingerprint: da41a5c6b07ad58b75b5ba18
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged
- **passive-voice** · .takeout/images/README-2.md:30:214 · **recurring** · fingerprint: 8b6c0e33f6a02796ddb94e33
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated
- **passive-voice** · .takeout/images/README-2.md:96:188 · **recurring** · fingerprint: 32c844d282b1c11074093437
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied
- **passive-voice** · .takeout/images/README-2.md:97:44 · **recurring** · fingerprint: 9f69f42d8f51f191d0d58188
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · .takeout/images/README-2.md:142:209 · **recurring** · fingerprint: 4df4cb023cf9d1ec7c96ddca
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recognized
- **semicolon** · .takeout/images/README-2.md:142:269 · **recurring** · fingerprint: f712923c6613939c83fbaec2
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .takeout/images/README-2.md:142:296 · **recurring** · fingerprint: a5ce13710f2822f72f96dc94
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rejected
- **passive-voice** · .takeout/images/README-2.md:144:203 · **recurring** · fingerprint: f1360185b073e84d28f1efb1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **semicolon** · .takeout/images/README-2.md:185:266 · **recurring** · fingerprint: f712923c6613939c83fbaec2
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .takeout/images/README-2.md:208:40 · **recurring** · fingerprint: 7b0b8a5e204fdc949021e113
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved
- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:3:121 · **recurring** · fingerprint: db01433d77ee17d96c56fcd6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **present-perfect** · .agent/skills/drawing/references/patterns/successful-patterns.md:25:23 · **recurring** · fingerprint: d2a1623a3515232827743a0f
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been tested
- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:25:27 · **recurring** · fingerprint: d31be00566b2fb6271a4c56f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:29:225 · **recurring** · fingerprint: 2c118b5809e6b19b18b6deff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were returned
- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:30:195 · **recurring** · fingerprint: 16c29dda93a863fa7f009a6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reused
- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:47:158 · **recurring** · fingerprint: 2cc2deaed296de61f4c7ac5e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being requested
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:66:61 · **recurring** · fingerprint: 3d753fd2c4828ff430fdb6c2
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:74:38 · **recurring** · fingerprint: 0642057a58aa1965274b9762
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:104 · **recurring** · fingerprint: f331458e480ad4445c592130
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:100:85 · **recurring** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:67 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:157 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:254 · **recurring** · fingerprint: c165f6e8824400b2723a92ab
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is controlled
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:106:205 · **recurring** · fingerprint: 0ee5ca333d00a4f63756c25b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is generated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:107:185 · **recurring** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:119:123 · **recurring** · fingerprint: 3a2d463bad961d4a2f26d082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was evaluated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:103 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:191 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:46 · **recurring** · fingerprint: 421ce0d953be11182d9e810a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stored
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:115 · **recurring** · fingerprint: 6937ea80a6afca82e7f414d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:133:54 · **recurring** · fingerprint: 2e0dfecf96eeb4735f44ac24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:143:183 · **recurring** · fingerprint: f8411801c3d8953cd8c2acbe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is identified
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:149:70 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:150:203 · **recurring** · fingerprint: a0bfc1f95f604fc3f864783e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is performed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:149 · **recurring** · fingerprint: 0da19e7aab04deb7911a62a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are unchanged
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:213 · **recurring** · fingerprint: fa6c012aa723a1be302eb24c
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:157:125 · **recurring** · fingerprint: 87a065e710f1792ecf1034fc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is migrated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:158:130 · **recurring** · fingerprint: 051c97c1441fc96df828d5f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:178:70 · **recurring** · fingerprint: 494f747b32f0b27099114e91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are filtered
- **long-sentence** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:190:3 · **recurring** · fingerprint: 0dc1b5fa54679407d060b44e
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:192:43 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:200:137 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:263 · **recurring** · fingerprint: ca82b6e19a6f4ef4347ae654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:293 · **recurring** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:216:263 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:139 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:162 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:188 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:219 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:222:62 · **recurring** · fingerprint: 6b4576cd5b0f0b9ac4699130
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was deleted
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:89 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:134 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:186 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:246 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:290 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:335 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:77 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:119 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:177 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/define-goal/SKILL.md:3:14 · **recurring** · fingerprint: 6e69702dd7b70f9e58a5b7d0
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **semicolon** · .agent/skills/define-goal/SKILL.md:3:303 · **recurring** · fingerprint: 64f46a5a0114f5419c00ca80
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/define-goal/SKILL.md:17:6 · **recurring** · fingerprint: 3f9fc482d99586da767ee8ca
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **synonym-rotation** · .agent/skills/define-goal/SKILL.md:31:41 · **recurring** · fingerprint: 3c0f0de82a3eb77b2f1b926d
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · .agent/skills/define-goal/SKILL.md:39:125 · **recurring** · fingerprint: cfda5ea15fb2c9e0c2cc445f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are sharpened
- **long-sentence** · .agent/skills/define-goal/SKILL.md:45:6 · **recurring** · fingerprint: 3f9fc482d99586da767ee8ca
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · .agent/skills/define-goal/SKILL.md:58:46 · **recurring** · fingerprint: f1c7de13906779a00f58730f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **long-sentence** · .agent/skills/define-goal/SKILL.md:66:3 · **recurring** · fingerprint: 6e69702dd7b70f9e58a5b7d0
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **synonym-rotation** · .agent/skills/define-goal/SKILL.md:66:130 · **recurring** · fingerprint: f5bebd30fc084be62b91ef54
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **long-sentence** · .agent/skills/define-goal/SKILL.md:70:3 · **recurring** · fingerprint: 61b81b0b3f3fa6a8612aac95
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **synonym-rotation** · .agent/skills/define-goal/SKILL.md:82:51 · **recurring** · fingerprint: de8e3efc53afc3d7e6a6854b
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:13:135 · **recurring** · fingerprint: a177e1fb8d855758e83b2fd3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:19:83 · **recurring** · fingerprint: 0a87489c591fb9a534219558
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disallowed
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:42:73 · **recurring** · fingerprint: 5845722ff39b083ac0f24c3c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:45:14 · **recurring** · fingerprint: 48a3cd39793032bad22fe180
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:47:74 · **recurring** · fingerprint: 48a3cd39793032bad22fe180
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:49:12 · **recurring** · fingerprint: 9f1e51594216eeb8d88ba38f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was included
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:86:20 · **recurring** · fingerprint: 2299f7304854c875ec35f372
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:97:52 · **recurring** · fingerprint: 7f9a0fe095243ed196597f7b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:119:29 · **recurring** · fingerprint: 0b4997f48c7f6654c29d6d42
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:123:77 · **recurring** · fingerprint: 2cee6ee6ee298d87860d2d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was approved
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:155:37 · **recurring** · fingerprint: 521c428794d37789264af034
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:159:37 · **recurring** · fingerprint: 295ce5dc4e797d6abdf84ff4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:181:62 · **recurring** · fingerprint: 8a2876168a6a0e61c7f3585a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:182:28 · **recurring** · fingerprint: 4a8888e0cc3de9ff35bb448b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:184:296 · **recurring** · fingerprint: 2ef0f783a815fbcc7919f6f8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:184:336 · **recurring** · fingerprint: ef7bd8ba29534123319befef
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been uploaded
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:185:31 · **recurring** · fingerprint: 4a8888e0cc3de9ff35bb448b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:186:26 · **recurring** · fingerprint: f3267cff8e89aa14f0508dcc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed
- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:205:20 · **recurring** · fingerprint: 7e02c138711b8a962490d168
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized
- **passive-voice** · .agent/skills/internal-comms/examples/faq-answers.md:2:55 · **recurring** · fingerprint: 9fe837ec91bfe0df1a9a74de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · .agent/skills/internal-comms/examples/faq-answers.md:2:225 · **recurring** · fingerprint: 3cde4b8a40b4b4e9d9003f98
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · .agent/skills/internal-comms/examples/faq-answers.md:4:3 · **recurring** · fingerprint: 9d88cb2e963737b24f2578f0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/internal-comms/examples/faq-answers.md:7:1 · **recurring** · fingerprint: 9d88cb2e963737b24f2578f0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/internal-comms/examples/faq-answers.md:12:3 · **recurring** · fingerprint: 771172c46821432e60b015b5
  - **Level:** advisory-free
  - **Message:** Sentence has 49 words (cap 25). Split it.
  - **Matched text:** 49 words
- **passive-voice** · .agent/skills/internal-comms/examples/faq-answers.md:12:20 · **recurring** · fingerprint: 9fe837ec91bfe0df1a9a74de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · .agent/skills/internal-comms/examples/faq-answers.md:12:130 · **recurring** · fingerprint: 9fe837ec91bfe0df1a9a74de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · .agent/skills/drawing/references/style-guide.md:60:31 · **recurring** · fingerprint: 92028f1dabfce4a5dc9d32b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was classified
- **passive-voice** · .agent/skills/github-actions/SKILL.md:21:206 · **recurring** · fingerprint: ce5c879312639d5e4a37c1f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · .agent/skills/github-actions/SKILL.md:23:59 · **recurring** · fingerprint: 5ef6ce13baf5600a1694be8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **present-perfect** · .agent/skills/github-actions/SKILL.md:33:40 · **recurring** · fingerprint: e8019ef8bf6c31ab6be19a58
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **passive-voice** · .agent/skills/drawing/assets/attempt-template.md:61:53 · **recurring** · fingerprint: fe7c9e1555e50fd0d3ead59c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/SESSION_START.md:28:36 · **recurring** · fingerprint: dc938b5856f3e903edbd297a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was retrieved
- **semicolon** · .agent/SESSION_START.md:31:179 · **recurring** · fingerprint: 499417ab68edb8c596a98f0f
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · .agent/SESSION_START.md:35:114 · **recurring** · fingerprint: 7e401b80fb2469d88b8b16c6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved
- **passive-voice** · .agent/SESSION_START.md:35:119 · **recurring** · fingerprint: 65e01e8ee980bec2c691cd07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **synonym-rotation** · .agent/SESSION_START.md:74:4 · **recurring** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/SESSION_START.md:75:161 · **recurring** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:76:63 · **recurring** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · .agent/SESSION_START.md:220:167 · **recurring** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · .agent/SESSION_START.md:236:210 · **recurring** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · .agent/SESSION_START.md:260:1 · **recurring** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:36:10 · **recurring** · fingerprint: a737104c50ceb40f303a4a01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:332 · **recurring** · fingerprint: 63b66afb8b84b4750380eace
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:388 · **recurring** · fingerprint: e18acfaf818e2c30f6ca30e9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:158:1 · **recurring** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:169:21 · **recurring** · fingerprint: 34fd4b4fc86f7c4829f49935
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validated
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:179:143 · **recurring** · fingerprint: 8fab87c9578c4937b0124edf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:181:62 · **recurring** · fingerprint: 7c3c1ace5ec3d5c53c98a4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are observed
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:183:69 · **recurring** · fingerprint: 1614dc41c4b7be8e66e6f0d4
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:120 · **recurring** · fingerprint: 2e23d59621877db75c28ce78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:223 · **recurring** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:206:177 · **recurring** · fingerprint: ff8dedd324f39ede5ee75f82
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:208:43 · **recurring** · fingerprint: ae6b75fe50ddf475f002c2af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is fragmented
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:210:53 · **recurring** · fingerprint: e6a0a6a3cb10281e485f4ced
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been measured
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:235:53 · **recurring** · fingerprint: e0805effa50f8c2d06788a7e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:261:171 · **recurring** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:292:60 · **recurring** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:295:388 · **recurring** · fingerprint: 84a34fb70b809525fcff26b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been piloted
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:296:52 · **recurring** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:313:90 · **recurring** · fingerprint: cd8c27dadbc8cbf2ffa0ea4b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unsupported
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:325:178 · **recurring** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:346:218 · **recurring** · fingerprint: a27c714d52cff462c278171d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:458:36 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:482:251 · **recurring** · fingerprint: a484bb1a5b40074d480f3f91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is configured
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:502:30 · **recurring** · fingerprint: 0de287d1c4eae57b62d477b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:503:52 · **recurring** · fingerprint: cbf03a5bdfbefc8d301bac6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are resolved
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:504:22 · **recurring** · fingerprint: ba2af3047b1dbc7bfdba2dd0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are classified
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:541:4 · **recurring** · fingerprint: 93b3c8314ad783839cf934a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:585:23 · **recurring** · fingerprint: ebe3a0eaf57219e6e13da654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is treated
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:586:94 · **recurring** · fingerprint: b1897a649c20569be1ac0618
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:598:63 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:610:53 · **recurring** · fingerprint: 1e8f06c794753d0da4c374f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are supported
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:611:217 · **recurring** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:613:256 · **recurring** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:640:93 · **recurring** · fingerprint: 316a7cc78530dc52ed55aeb6
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:670:104 · **recurring** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:4 · **recurring** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:107 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:166 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:212 · **recurring** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:680:4 · **recurring** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:48 · **recurring** · fingerprint: 5c278ad2f255230faa055f76
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:90 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:122 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:700:45 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:707:246 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:708:194 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:155 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:240 · **recurring** · fingerprint: dd5a9425158b41b001c9b936
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:712:91 · **recurring** · fingerprint: c6bfceae059912f8aadd9e2e
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fixed
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:718:1 · **recurring** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/source-standards.md:99:19 · **recurring** · fingerprint: 31b1c652f1950eb652c297b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/source-standards.md:194:41 · **recurring** · fingerprint: 3cf3d888bb09d615bc5ecf6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being cited
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:53:21 · **recurring** · fingerprint: 636319e0f7c3b3cd746ca815
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:94:11 · **recurring** · fingerprint: 0213e8215e33b96f40b0cceb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disputed
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:144:43 · **recurring** · fingerprint: 9a59a040c9cc2c665d08de61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are related
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:167:67 · **recurring** · fingerprint: 744c323ac844ab9c1885a174
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:178:68 · **recurring** · fingerprint: 1ecb948b37f33ea375b33a87
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supported
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:179:43 · **recurring** · fingerprint: 467eea53004536ffbc6f6f83
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:291:3 · **recurring** · fingerprint: 61cfd4a2dc271720d2c83a22
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been excluded
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:292:52 · **recurring** · fingerprint: 85c8f8886cfc0e70af2fa91e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been kept
- **passive-voice** · .agent/skills/internal-comms/examples/general-comms.md:2:11 · **recurring** · fingerprint: ccc63107771e2eb7ec53a4e4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **semicolon** · .agent/skills/decision-governance/SKILL.md:84:206 · **recurring** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:103:283 · **recurring** · fingerprint: 7c881c753a4078cb6de1c860
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:107:38 · **recurring** · fingerprint: 7e15f02585cf13c74c4d9066
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:109:34 · **recurring** · fingerprint: ed925553639766f753b1e47c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:47 · **recurring** · fingerprint: c6fdcf445b99331b3955a823
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated
- **semicolon** · .agent/skills/decision-governance/SKILL.md:115:57 · **recurring** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:102 · **recurring** · fingerprint: c5cbda1d2fcdc95906e3b0f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:117:86 · **recurring** · fingerprint: 9248adb057e0be913c820595
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed
- **semicolon** · .agent/skills/decision-governance/SKILL.md:131:65 · **recurring** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · .agent/skills/asd-ste100/references/writing-rules.md:7:511 · **recurring** · fingerprint: f07d3c84432af463c7f72518
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been
- **present-perfect** · .agent/skills/asd-ste100/references/writing-rules.md:26:84 · **recurring** · fingerprint: 52fb0410311ad16756b7bfe3
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:26:129 · **recurring** · fingerprint: 9c80fb1e6e5000284a29137e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed
- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:27:16 · **recurring** · fingerprint: fcfbdbdcf23b08e64d0f93c8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:30:16 · **recurring** · fingerprint: b35ca4ac1ff82c9bf3fc1e3d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:31:17 · **recurring** · fingerprint: 9c80fb1e6e5000284a29137e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed
- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:37:58 · **recurring** · fingerprint: c6fc29287cb5e7f548957604
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are capped
- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:50:5 · **recurring** · fingerprint: 02478fa831f501fa3dd2ba3d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was designed
- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:44:40 · **recurring** · fingerprint: 3c65876301fed0b3c507542f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is inferred
- **present-perfect** · .agent/skills/drawing/references/series-continuity-and-iteration.md:50:245 · **recurring** · fingerprint: 532631bc6b42b9ef571cc030
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has declared
- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:78:42 · **recurring** · fingerprint: d9528dbaf4bbc041cf2ae3ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is ordered
- **present-perfect** · .agent/skills/drawing/references/series-continuity-and-iteration.md:82:259 · **recurring** · fingerprint: 2ad2d875e478e9ef55228ab2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has established
- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:94:27 · **recurring** · fingerprint: 1a1b591ca9810210a11e3bb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are locked
- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:134:15 · **recurring** · fingerprint: 0e03aa3ca8bee4298b54aa2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:140:14 · **recurring** · fingerprint: 0e03aa3ca8bee4298b54aa2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:164:73 · **recurring** · fingerprint: 45565ae1723777f3f799c982
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being edited
- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:177:79 · **recurring** · fingerprint: e9f8f5370d87e09abc939413
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **long-sentence** · .agent/skills/document-standards/references/document-type-catalog.md:45:121 · **recurring** · fingerprint: 2dd7b3784611553473e6528c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:45:212 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:45:458 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:191 · **recurring** · fingerprint: 3ae524e22114a03c0ab4422a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:228 · **recurring** · fingerprint: 2115664c682d98befee7c6f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is tracked
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:126:145 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:143 · **recurring** · fingerprint: d54e065531122bd43e42b93b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are allocated
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:13:64 · **recurring** · fingerprint: e5525626c1967e0a340ca6a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is curated
- **semicolon** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:19:336 · **recurring** · fingerprint: e1fd3f41b42938a1e8507bbb
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:21:109 · **recurring** · fingerprint: 69ced9ce37a5222737761146
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:33:8 · **recurring** · fingerprint: f63bb7a71c949cd73ccbef9b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was completed
- **synonym-rotation** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:52:20 · **recurring** · fingerprint: 03fe26b802d24bd62ff0a202
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:87:21 · **recurring** · fingerprint: 0612acc3ded54049ec675ae4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:96:11 · **recurring** · fingerprint: 2c1da6bfaf483087ef9327af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:124:164 · **recurring** · fingerprint: 94e51011211d6fc251cabb65
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:127:130 · **recurring** · fingerprint: 783ad4a07e61c15afad1e585
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:131:343 · **recurring** · fingerprint: d164c6cd28e0ab9df8f188d9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:188:170 · **recurring** · fingerprint: 433dafd5d692277cca6a4c24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was supplied
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:191:23 · **recurring** · fingerprint: 46d08da660ad9f0d48a138b0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being tested
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:229:65 · **recurring** · fingerprint: fbe839b26aecd31e753f74ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:240:24 · **recurring** · fingerprint: 3d87aa3e3e05414a6fc20859
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:246:176 · **recurring** · fingerprint: bac7b5e46fbea597ad4dbea1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:260:44 · **recurring** · fingerprint: 5d36f6e71392c533b3845506
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:270:68 · **recurring** · fingerprint: d012538c491cfde62ff1fdd9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:271:36 · **recurring** · fingerprint: fbe839b26aecd31e753f74ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:271:58 · **recurring** · fingerprint: 7c258b1c239930b3450bf575
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unverified
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:274:4 · **recurring** · fingerprint: a703317ebbefd56b39b629a9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:275:78 · **recurring** · fingerprint: ce5982a1a9d2565e0ee20170
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:276:48 · **recurring** · fingerprint: fa512a90594737a041e9d5c6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:277:75 · **recurring** · fingerprint: fbe839b26aecd31e753f74ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:278:68 · **recurring** · fingerprint: c88aa7cca35223c0301d1ceb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:288:20 · **recurring** · fingerprint: c330a30e67f8d2c28b084e65
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:292:53 · **recurring** · fingerprint: ffdcdc602458d6c9905129c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is renamed
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:316:69 · **recurring** · fingerprint: b2681466028c0f48c36959c5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based
- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:320:84 · **recurring** · fingerprint: ec91177483cac13de5f77a8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is authorized
- **semicolon** · .agent/skills/drawing/references/image-editing-protocol.md:9:82 · **recurring** · fingerprint: 4d3cb40fdfeb08c154a785f9
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/drawing/references/image-editing-protocol.md:33:34 · **recurring** · fingerprint: a58c92304a5ac7957912b9b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is confirmed
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:14:79 · **recurring** · fingerprint: 02b57d3b2df16eb3468595dc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:159:29 · **recurring** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:166:23 · **recurring** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:172:149 · **recurring** · fingerprint: ba8e0ed371140388669d2100
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:172:153 · **recurring** · fingerprint: 1b62b1b2e8581f74a08af948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:185:36 · **recurring** · fingerprint: 97f02ce3bcf5b6ef7653d521
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:223:38 · **recurring** · fingerprint: 6791e38cdf43e2f4c45df46b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:245:28 · **recurring** · fingerprint: eb4ac5866a5a9ae0a950a472
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:246:65 · **recurring** · fingerprint: 301135338f19f01e083e45ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:246:70 · **recurring** · fingerprint: e6c88a755850e4cbcab58fa8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:253:17 · **recurring** · fingerprint: bbeb4b1299f984862be3ce2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:255:37 · **recurring** · fingerprint: 6d4fd87d7c04e6106995412e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been made
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:255:41 · **recurring** · fingerprint: 5b69fb1b48037b85a2f02a19
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been made
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:257:32 · **recurring** · fingerprint: 19df0784fbab3f590bc978f2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:257:36 · **recurring** · fingerprint: 9124dbf071fc471856835398
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/README.md:17:11 · **recurring** · fingerprint: 1583b8690f42ec1e396bc38a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are enabled
- **passive-voice** · .takeout/images/README-1.md:17:543 · **recurring** · fingerprint: d62fd2f70644184cc4c5011d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted
- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:68:60 · **recurring** · fingerprint: d6fb83cbafb61644c729d606
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:68:162 · **recurring** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:84:157 · **recurring** · fingerprint: 50194bcb1c09593a6b8df74f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:96:72 · **recurring** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:101:41 · **recurring** · fingerprint: 01c59b00a54bee35fe1936cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:129:88 · **recurring** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:78 · **recurring** · fingerprint: 13168d32e5aeb357a6f05047
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:108 · **recurring** · fingerprint: 2d62a35466a8134401aac697
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:61 · **recurring** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:272 · **recurring** · fingerprint: a49119a4bb942d7711bad4ec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:146:63 · **recurring** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:151:36 · **recurring** · fingerprint: 3ca196dd83b56964e6c9c511
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:153:106 · **recurring** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:162:180 · **recurring** · fingerprint: 8b93e6445dd13d5345069497
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:260 · **recurring** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:205:94 · **recurring** · fingerprint: b8c8647d519418bedc546521
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:232:126 · **recurring** · fingerprint: f70f53510f186a20aefa39a5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:232:130 · **recurring** · fingerprint: 9c5f95ce73981d93b428a229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:253:75 · **recurring** · fingerprint: d3280be9a8e338d6afc3f804
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed
- **passive-voice** · .agent/skills/internal-comms/examples/company-newsletter.md:2:9 · **recurring** · fingerprint: d119f69401fb0d7940bb4b07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · .agent/skills/internal-comms/examples/company-newsletter.md:5:3 · **recurring** · fingerprint: e62dcc8049fb6bc6e436685c
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **present-perfect** · .agent/skills/internal-comms/examples/company-newsletter.md:5:245 · **recurring** · fingerprint: 848d2cddd8fb8ca620a9897a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have happened
- **passive-voice** · .agent/skills/internal-comms/examples/company-newsletter.md:21:418 · **recurring** · fingerprint: 0e81d23f4e8c8bea0003125d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are highlighted
- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:9:15 · **recurring** · fingerprint: 25f76deeafca430fb8355765
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based
- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:17:50 · **recurring** · fingerprint: dc78ab72e0948a2fb497356c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was executed
- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:48:38 · **recurring** · fingerprint: bc935daa91ef2a6b57226d04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is organized
- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:70:17 · **recurring** · fingerprint: f1d96c0b5d4b34b9c1ea0024
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are provided
- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:172:20 · **recurring** · fingerprint: 8499b8cbe16dca6dbedd1c00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were provided
- **semicolon** · .agent/skills/skill-creator/agents/comparator.md:200:67 · **recurring** · fingerprint: 5338d6f6a882c8070470752c
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/task_board.md:32:21 · **recurring** · fingerprint: 6d69ad27d49d36813c14b275
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Repair
- **passive-voice** · .agent/skills/asd-ste100/README.md:26:35 · **recurring** · fingerprint: f592f42318251b648dd03dcb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · .agent/skills/asd-ste100/README.md:40:109 · **recurring** · fingerprint: 04c8a0d348a66e7c3e456046
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · workspace/ANALYSIS_TEMPLATE.md:53:50 · **recurring** · fingerprint: 6065ee744d87e9ee28f540f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **synonym-rotation** · .agent/skills/document-standards/SKILL.md:22:21 · **recurring** · fingerprint: 59f9b3021fb92ba38c2f3aa0
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **passive-voice** · .agent/skills/document-standards/SKILL.md:39:46 · **recurring** · fingerprint: 6f736d87b623b41483378e01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **semicolon** · .agent/skills/document-standards/SKILL.md:39:137 · **recurring** · fingerprint: 908066259786706e521f34bf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/SKILL.md:107:229 · **recurring** · fingerprint: 49c041bef5326bd7d5361137
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:7:3 · **recurring** · fingerprint: 2051275b3344d8d1e90bb20c
  - **Level:** advisory-free
  - **Message:** Sentence has 55 words (cap 25). Split it.
  - **Matched text:** 55 words
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:12:57 · **recurring** · fingerprint: 0732cf54040416dcdb048e67
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:31:5 · **recurring** · fingerprint: ab1cd670db5255dba49ba1b0
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:36:5 · **recurring** · fingerprint: cc232b6cfb14b97181d99159
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is granted
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:37:5 · **recurring** · fingerprint: d3858f29af32d8e94293d0b0
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:42:5 · **recurring** · fingerprint: 25e51d985e9ed0edb6b1ce6c
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **synonym-rotation** · .agent/skills/migrate-to-rust/SKILL.md:43:26 · **recurring** · fingerprint: 4793da617ba3f4720177981a
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:46:45 · **recurring** · fingerprint: be06c683fb6cc7f7e8897691
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:47:22 · **recurring** · fingerprint: 85dac0b16ea5ca9c2b0033ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exhausted
- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:56:40 · **recurring** · fingerprint: 04d4c46e1b90de89a9b92bd8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:60:20 · **recurring** · fingerprint: f762c34776138fd607c76ea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are measured
- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:62:73 · **recurring** · fingerprint: 5b08b51f4a7b5fb8f192e23e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:102:58 · **recurring** · fingerprint: 51d97ec877597fa8ccf4f775
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:107:5 · **recurring** · fingerprint: 08a1774af47912b4ea612719
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **synonym-rotation** · .agent/skills/migrate-to-rust/SKILL.md:107:7 · **recurring** · fingerprint: a15b0b4bbc30e4751af5dbf6
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:110:19 · **recurring** · fingerprint: be06c683fb6cc7f7e8897691
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:119:1 · **recurring** · fingerprint: ca900c973726b0f821b797cc
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:155:5 · **recurring** · fingerprint: 8f605ea680fa9caf195b3943
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:159:24 · **recurring** · fingerprint: dcb436816632865387b30390
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reached
- **synonym-rotation** · .agent/skills/migrate-to-rust/SKILL.md:169:68 · **recurring** · fingerprint: 0f9a40808850989ecafd2544
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:176:5 · **recurring** · fingerprint: ca900c973726b0f821b797cc
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/skill-creator/references/schemas.md:76:35 · **recurring** · fingerprint: 17f5d80e88f7a58d4d55d5cc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being improved
- **passive-voice** · .agent/skills/skill-creator/references/schemas.md:79:46 · **recurring** · fingerprint: 7d978a01acd6c2742f13d662
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was derived
- **passive-voice** · .agent/skills/skill-creator/references/schemas.md:291:37 · **recurring** · fingerprint: 854bbcd9398ee87735892c01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run
- **semicolon** · workspace/draft/README.md:7:96 · **recurring** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/README.md:19:4 · **recurring** · fingerprint: fa0ad26c0f4696b24c6e471f
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · workspace/draft/README.md:21:305 · **recurring** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/README.md:23:136 · **recurring** · fingerprint: 23958065d6cbd83c298c65e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been assessed
- **passive-voice** · workspace/TASK_TEMPLATE.md:20:108 · **recurring** · fingerprint: 5275280719ed16d2a5b7ad67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is written
- **passive-voice** · workspace/TASK_TEMPLATE.md:48:21 · **recurring** · fingerprint: fdc561df7864672b424ed481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was inspected
- **passive-voice** · workspace/TASK_TEMPLATE.md:75:20 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:76:23 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:86:150 · **recurring** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **long-sentence** · .agent/skills/pdf/FORMS.md:53:3 · **recurring** · fingerprint: aa35eeeb7b54e03661f78104
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words
- **long-sentence** · .agent/skills/pdf/FORMS.md:74:3 · **recurring** · fingerprint: 12ef9957ae8fa3f2d1431f0a
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **synonym-rotation** · .agent/skills/pdf/FORMS.md:76:18 · **recurring** · fingerprint: 4d00c94cbb2ee5a3549d25f5
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **semicolon** · .agent/skills/pdf/FORMS.md:76:76 · **recurring** · fingerprint: eadb2528a436236ee54581d7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/pdf/FORMS.md:92:179 · **recurring** · fingerprint: 02b908f6e44af3aef97442d9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned
- **passive-voice** · .agent/skills/pdf/FORMS.md:114:51 · **recurring** · fingerprint: 89502e06609861db50e55419
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected
- **long-sentence** · .agent/skills/pdf/FORMS.md:118:1 · **recurring** · fingerprint: 6003a455c1f4c264a40e7c06
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · .agent/skills/pdf/FORMS.md:163:10 · **recurring** · fingerprint: 3d6807b222eb69b5b87dc658
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **synonym-rotation** · .agent/skills/pdf/FORMS.md:168:99 · **recurring** · fingerprint: 8f0ad7582380f0363e5c59c6
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix
- **passive-voice** · .agent/skills/pdf/FORMS.md:174:23 · **recurring** · fingerprint: 02b908f6e44af3aef97442d9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned
- **synonym-rotation** · .agent/skills/pdf/FORMS.md:210:50 · **recurring** · fingerprint: 5958fa7a24c9e3a09bf92349
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins
- **passive-voice** · .agent/skills/pdf/FORMS.md:260:39 · **recurring** · fingerprint: 4b9cfede2f3072d88c040579
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were detected
- **passive-voice** · .agent/skills/pdf/FORMS.md:291:9 · **recurring** · fingerprint: c1bdeae5f6d49be66f3dc77f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is mispositioned
- **long-sentence** · .agent/skills/pdf/SKILL.md:3:84 · **recurring** · fingerprint: 7c271799320bb3fa32a3db32
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:13:215 · **recurring** · fingerprint: 3d9cd8606c71744cd549b794
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is measured
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:15:69 · **recurring** · fingerprint: d5f82029b13df7171b934277
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:46:115 · **recurring** · fingerprint: 8cc9271efa91b21a28df106f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is phrased
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:56:24 · **recurring** · fingerprint: 811cd72c913b73297c41df31
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:62:24 · **recurring** · fingerprint: dc36d4218894c718c5cae3a8
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:74:32 · **recurring** · fingerprint: a0d9fae2ecfc97b1d4a4f353
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are prohibited
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:80:35 · **recurring** · fingerprint: bc92abe865806f83163486f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being limited
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:89:141 · **recurring** · fingerprint: fbf25669bed6707f20b54638
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been established
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:91:171 · **recurring** · fingerprint: 106e56d434926ee31ff1490e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:116:33 · **recurring** · fingerprint: 3bce599aec03b94f1f1acdf1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has specified
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:119:41 · **recurring** · fingerprint: 49a02aeb8c516b96480c0200
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is depicted
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:127:120 · **recurring** · fingerprint: af1fe0da78db75f1afca7e12
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unspecified
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:127:168 · **recurring** · fingerprint: 5fae82b579f91a91fce6afd1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:151:163 · **recurring** · fingerprint: 5fae82b579f91a91fce6afd1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:198:141 · **recurring** · fingerprint: 42bc7f65a0321b20b4ebe6eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:225:75 · **recurring** · fingerprint: dc36d4218894c718c5cae3a8
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:244:41 · **recurring** · fingerprint: cc38a206710d5124e674cb13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:245:103 · **recurring** · fingerprint: 88970a2b0d7687b4903bc248
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:246:33 · **recurring** · fingerprint: 0a1ccaa9e582c0e89cd78104
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been paraphrased
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:247:123 · **recurring** · fingerprint: e8b85db64c57be8defba2b0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:248:42 · **recurring** · fingerprint: 7d0ffc2028c0b5c0e00573ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been preserved
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:249:26 · **recurring** · fingerprint: d70b4cf5c12886fee4bae585
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been limited
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:250:23 · **recurring** · fingerprint: 07efb79fa4e7a754a4df6331
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been converted
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:265:66 · **recurring** · fingerprint: 1f850b5c9410689c68878d1b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being submitted
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:268:30 · **recurring** · fingerprint: 8c4e6e357e0de615dd8ee971
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been archived
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:268:34 · **recurring** · fingerprint: 0aacc915f68736f69d97bcd7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been archived
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:270:46 · **recurring** · fingerprint: bbc2b8452f1e9c60a3400849
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exposed
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:272:98 · **recurring** · fingerprint: 5ef443839fa3154ef240274c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was submitted
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:272:197 · **recurring** · fingerprint: cde682dbdf090ea0d1abbaf2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was authorized
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:289:87 · **recurring** · fingerprint: 5fae82b579f91a91fce6afd1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:300:57 · **recurring** · fingerprint: 4016f59fa6583b3fe4ac2a03
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been checked
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:300:62 · **recurring** · fingerprint: cc4bbc272970240397e9337b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been checked
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:301:99 · **recurring** · fingerprint: 8e9eceec4ee17012c246262d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:302:41 · **recurring** · fingerprint: 20b7a70989c653847d75e449
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:302:46 · **recurring** · fingerprint: e8b85db64c57be8defba2b0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:303:106 · **recurring** · fingerprint: 6aae20a911c952490fc2b8fd
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been added
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:303:111 · **recurring** · fingerprint: 88970a2b0d7687b4903bc248
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:304:31 · **recurring** · fingerprint: 98c704fe9c1c3900a44e37e0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been restored
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:304:35 · **recurring** · fingerprint: cc38a206710d5124e674cb13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:306:58 · **recurring** · fingerprint: c35b7f77d08cfe4ad18f5647
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been audited
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:306:62 · **recurring** · fingerprint: cfb684542126ef90917c1893
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been audited
- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:307:27 · **recurring** · fingerprint: d44b601f4e06693644fb00e7
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been removed
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:307:31 · **recurring** · fingerprint: 103b143264e3231c2f628df4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been removed
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:309:42 · **recurring** · fingerprint: e690cece4fd6dbd89977d838
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is assigned
- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:309:73 · **recurring** · fingerprint: 4b1c8a395c52a0749f8ce4a1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was copied
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:3:126 · **recurring** · fingerprint: 0656ffda7585e034eaeb0422
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:5:65 · **recurring** · fingerprint: 05ca10f52e76fee19176307e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are kept
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:19:163 · **recurring** · fingerprint: 22988deb64559045c494003e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reversed
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:22:89 · **recurring** · fingerprint: af251391824b3261c959e38f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:37:14 · **recurring** · fingerprint: 11ea98a026244f24cb19aa65
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is concentrated
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:48:20 · **recurring** · fingerprint: 3b45a129d4c0838326049ff7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were described
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:51:37 · **recurring** · fingerprint: 633eb4103528f878e2b3a9e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:61:197 · **recurring** · fingerprint: cc2fb2a172ba0f953ae0dfb4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:61:226 · **recurring** · fingerprint: 6de85062a6003e7358ec5c63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:85:19 · **recurring** · fingerprint: 183cb5a94112bdc23b770e5e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:91:264 · **recurring** · fingerprint: 29405619a2c91e6718f44773
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:120:233 · **recurring** · fingerprint: ec024dbf98259c151baea3a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was identified
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:136:66 · **recurring** · fingerprint: e7d0389b66176dff655137ba
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:154:172 · **recurring** · fingerprint: 0fca0464d15d439571aa29f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:165:92 · **recurring** · fingerprint: e0c2a92699e4acd4b0538ccc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:168:20 · **recurring** · fingerprint: 29405619a2c91e6718f44773
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:183:164 · **recurring** · fingerprint: 183cb5a94112bdc23b770e5e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **present-perfect** · .agent/skills/drawing/references/patterns/failure-patterns.md:194:52 · **recurring** · fingerprint: 8742abb9a4f8d39f2ac9b892
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has corrected
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:209:235 · **recurring** · fingerprint: 059552d8427fa19158b19e99
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was removed
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:209:273 · **recurring** · fingerprint: c0db69a5c995509e4eb77cff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was preserved
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:210:249 · **recurring** · fingerprint: 5332f45bf55aaf0434b21be1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was adopted
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:214:32 · **recurring** · fingerprint: 966afd25d1a5cb24ede20924
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **present-perfect** · .agent/skills/drawing/references/patterns/failure-patterns.md:218:179 · **recurring** · fingerprint: c16ece4a46c94b44b00a5fe8
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:224:30 · **recurring** · fingerprint: 42baa51e06c4f52b0c0c18b5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:250:20 · **recurring** · fingerprint: 966afd25d1a5cb24ede20924
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **marketing-adjective** · .agent/skills/theme-factory/themes/tech-innovation.md:3:63 · **recurring** · fingerprint: f11de535868101ba92b23305
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **passive-voice** · .agent/skills/the-worker/references/drawing-session-closeout.md:17:227 · **recurring** · fingerprint: 65adcc690f1e819c5e11e9d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed
- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md:29:14 · **recurring** · fingerprint: d20eaeb4d39ab36d89018d79
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested
- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:20:40 · **recurring** · fingerprint: ab9436f2b5ed3e06585afd03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired
- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:21:125 · **recurring** · fingerprint: a70edfc93adc8937d630930d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified
- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:25:67 · **recurring** · fingerprint: 7f22912dfdbb21318247d4b3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · .agent/skills/drawing/assets/pattern-entry-templates.md:107:246 · **recurring** · fingerprint: 8fab2ea58ed063963328af68
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested
- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:116:51 · **recurring** · fingerprint: ac66d4a7e8457dcc712ea9d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:117:16 · **recurring** · fingerprint: 524acb2777c80b2c40f2312b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was assigned
- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:121:20 · **recurring** · fingerprint: 9f497620b35e45191797af3b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are separated
- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:123:15 · **recurring** · fingerprint: 66a6cf2a8d964826d67af7b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are described
- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:125:19 · **recurring** · fingerprint: ac66d4a7e8457dcc712ea9d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:3:1 · **recurring** · fingerprint: b2b4aaa5b80db580f641bc21
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:49:49 · **recurring** · fingerprint: 5efbda4d1f757c605b1da5a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is isolated
- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:72:5 · **recurring** · fingerprint: cbf47abcc8791070f58ba425
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:86:5 · **recurring** · fingerprint: e81e6adfd11cb872fd2c800e
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:96:26 · **recurring** · fingerprint: ec08c47bfb79374766082383
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **synonym-rotation** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:97:34 · **recurring** · fingerprint: 146d695ea92d0b8d4fa5a564
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **synonym-rotation** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:98:5 · **recurring** · fingerprint: 242d6a5058ac23a1dd770c30
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:112:9 · **recurring** · fingerprint: ec08c47bfb79374766082383
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **semicolon** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:102 · **recurring** · fingerprint: 48ceae5f0f72eac5e3b2c143
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:129 · **recurring** · fingerprint: 48ceae5f0f72eac5e3b2c143
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:147:28 · **recurring** · fingerprint: 976f180d206c7bf876f46fd7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grounded
- **synonym-rotation** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:170:7 · **recurring** · fingerprint: 130f0ce7248726f1d9dbb390
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirming
- **passive-voice** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:220:22 · **recurring** · fingerprint: b6e95df7029eb4462c9ecbcc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is enforced
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:21:69 · **recurring** · fingerprint: 170e10c67c5ddb4ac54ea4b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was violated
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:49:227 · **recurring** · fingerprint: cb0ac7a2c5dda8b0dbd1051d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are defined
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:57:60 · **recurring** · fingerprint: 8a011f6518e4f647accaa107
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:58:99 · **recurring** · fingerprint: 70281f9b33028652f7a1daae
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** Spin up
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:73:118 · **recurring** · fingerprint: 28ef39a3cb8b2ca848f4ec97
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **nominalization** · .agent/skills/asd-ste100/SKILL.md:74:53 · **recurring** · fingerprint: 7e86fc5d602e4865ed4a0ff6
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:79:203 · **recurring** · fingerprint: 7a15da17f8212acf9cbcd80a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:81:140 · **recurring** · fingerprint: 320768d857c6a3e84654f3f5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed
- **nominalization** · .agent/skills/asd-ste100/SKILL.md:89:56 · **recurring** · fingerprint: fa833ca0d8a25be575faf6e0
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:79 · **recurring** · fingerprint: 12a9fb2640f958cc7e75f621
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:89 · **recurring** · fingerprint: c50be8a609eda6ecc738029b
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:107 · **recurring** · fingerprint: d7e2c69987f9328ac247ac53
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:121 · **recurring** · fingerprint: 0d5ed7f9257c40733f5c321d
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:133 · **recurring** · fingerprint: 2673e9a5ae5dd03778f880c9
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:29 · **recurring** · fingerprint: d272642fbbf9daaca0e0f89b
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** spin up
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:38 · **recurring** · fingerprint: 0069ef4a67380240203a7d96
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** reach out
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:49 · **recurring** · fingerprint: a00e46d5c1d01ed73aeb5e48
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** dive into
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:60 · **recurring** · fingerprint: 186eeebc10bfa90b61b9f168
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** kick off
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:113:134 · **recurring** · fingerprint: 361fe239198e1c7837a878ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:146:58 · **recurring** · fingerprint: 9efba8ed23b805f9a79bdc62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:25:119 · **recurring** · fingerprint: f64bf1ef9acc14ca64a7b985
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:51:26 · **recurring** · fingerprint: 211b66e79e230bc550635a4f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were identified
- **semicolon** · workspace/DRAFT_TEMPLATE.md:53:58 · **recurring** · fingerprint: 3b682280b9ab9bb9d337e5a7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/DRAFT_TEMPLATE.md:63:103 · **recurring** · fingerprint: 3b682280b9ab9bb9d337e5a7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:78:47 · **recurring** · fingerprint: 3027ddebf5aa8173af033457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:91:47 · **recurring** · fingerprint: 3027ddebf5aa8173af033457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **long-sentence** · workspace/DRAFT_TEMPLATE.md:111:75 · **recurring** · fingerprint: 1068d0f64079905a096f3f87
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:124:55 · **recurring** · fingerprint: fe3d0313172da8b3bd40c574
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **synonym-rotation** · workspace/DRAFT_TEMPLATE.md:166:28 · **recurring** · fingerprint: fcd884bb6124b09c0acad1a2
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:4:3 · **recurring** · fingerprint: dd75187d1582eb7d2b491ad4
  - **Level:** advisory-free
  - **Message:** Sentence has 88 words (cap 25). Split it.
  - **Matched text:** 88 words
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:12:59 · **recurring** · fingerprint: 122ed7fb2cb96e1ca4b4eb09
  - **Level:** advisory-free
  - **Message:** Sentence has 64 words (cap 25). Split it.
  - **Matched text:** 64 words
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:27:42 · **recurring** · fingerprint: d7e37d0e4b2dd92bcc8046ca
  - **Level:** advisory-free
  - **Message:** Sentence has 46 words (cap 25). Split it.
  - **Matched text:** 46 words
- **synonym-rotation** · .agent/skills/discernment-nudge/SKILL.md:38:9 · **recurring** · fingerprint: 166248501fb9f2ce64dbbda2
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verifying
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:52:3 · **recurring** · fingerprint: 8e8b4d5dcd6b9b3a95ebd340
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:55:3 · **recurring** · fingerprint: 791a6d81408bdac17b771d91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:58:42 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:59:39 · **recurring** · fingerprint: 791a6d81408bdac17b771d91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:66:3 · **recurring** · fingerprint: b056eeb37b6762f4cace445e
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:75:47 · **recurring** · fingerprint: 03e560e6a34affc3f3b3ce36
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:76:8 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:81:15 · **recurring** · fingerprint: 72a58961141ef493db231920
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **passive-voice** · .agent/skills/discernment-nudge/SKILL.md:83:24 · **recurring** · fingerprint: 7666a76a64fdc00c8e9909af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been invited
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:84:34 · **recurring** · fingerprint: 791a6d81408bdac17b771d91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:89:51 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:101:54 · **recurring** · fingerprint: 16b708bb219c5c5ddf4b8d4f
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:106:27 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:117:35 · **recurring** · fingerprint: b056eeb37b6762f4cace445e
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:121:65 · **recurring** · fingerprint: 72a58961141ef493db231920
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:130:36 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:136:16 · **recurring** · fingerprint: 79f0398563d7f9f20fe6c295
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:141:39 · **recurring** · fingerprint: 03e560e6a34affc3f3b3ce36
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/discernment-nudge/SKILL.md:156:9 · **recurring** · fingerprint: c16c15ec163e1f3c17879996
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are weighed
- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:167:1 · **recurring** · fingerprint: 4f3ace9d5db454f882ac45fe
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:171:34 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:205:17 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:25:10 · **recurring** · fingerprint: a2ab275c6b77dd5fee04cc69
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:25:236 · **recurring** · fingerprint: f361f0da8e025b2ad8e4e144
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:27:293 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:43:292 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:43:342 · **recurring** · fingerprint: a909a403a059d36f26caf607
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are unchanged
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:45:452 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:118:13 · **recurring** · fingerprint: 2622327c5814c036cce375d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are assessed
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:127:277 · **recurring** · fingerprint: 5fbc17194b22ffad4280c0ef
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supported
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:131:1 · **recurring** · fingerprint: fef6e60a628c50ea5557879f
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:135:123 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:141:432 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:149:130 · **recurring** · fingerprint: 5acc357959587a68b0f951b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:151:133 · **recurring** · fingerprint: ff6c3acd0c014dc4e61c466a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:154:130 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:3 · **recurring** · fingerprint: f7dc64f1259416e941602253
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:153 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:195 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:216 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:172:17 · **recurring** · fingerprint: 6e0df3ac815fc5850205b430
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has evolved
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:177:5 · **recurring** · fingerprint: 88aeab811894156e381b6f38
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:181:259 · **recurring** · fingerprint: 5c822b17641bfca685187467
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validate
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:45 · **recurring** · fingerprint: e8137e2bbd27eeeebe09cefe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are gitignored
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:72 · **recurring** · fingerprint: f82bfd9e6673b647a6d8fc2d
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:278 · **recurring** · fingerprint: 2879617005bdf3d23fcdebce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:186:131 · **recurring** · fingerprint: 88aeab811894156e381b6f38
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:186:552 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:187:3 · **recurring** · fingerprint: 0f7475f061de95d077b1bfe9
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:195:90 · **recurring** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:206:112 · **recurring** · fingerprint: d322aeaf54a910f1b652245b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is missed
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:207:165 · **recurring** · fingerprint: f0d61be6ac280ec407b4f93b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reconciled
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:209:5 · **recurring** · fingerprint: fef6e60a628c50ea5557879f
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:211:311 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:211:342 · **recurring** · fingerprint: 77adbdbc0fe812d1b67b5e05
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are intended
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:223:85 · **recurring** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:231:5 · **recurring** · fingerprint: f82bfd9e6673b647a6d8fc2d
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:232:3 · **recurring** · fingerprint: 3dd65725c765cdc8c75ee04a
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:241:81 · **recurring** · fingerprint: a7bf89e39efdb719560ebf21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is redesigned
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:244:107 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:267:114 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:268:69 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:281:139 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:283:84 · **recurring** · fingerprint: ff6c3acd0c014dc4e61c466a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:320:246 · **recurring** · fingerprint: 89ce3d95585eee314fa93cfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:326:391 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:338:117 · **recurring** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:338:187 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:383:179 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:463:1 · **recurring** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:469:245 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:515:142 · **recurring** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:516:107 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:517:145 · **recurring** · fingerprint: e4c84bbce7e4e015e5f82803
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:528:134 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:528:168 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:530:11 · **recurring** · fingerprint: f0baecd36560346eb7c99c71
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:18 · **recurring** · fingerprint: e7603e373d761a7c9ff25aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:104 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:126 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:157 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:537:20 · **recurring** · fingerprint: e796b5d39f657c7dbfca408d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is treated
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:539:30 · **recurring** · fingerprint: 45700ec28d246ad5f6098f6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are treated
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:554:32 · **recurring** · fingerprint: 70781a8fa973c1554931c214
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:612:52 · **recurring** · fingerprint: 331ead622bd8b63c3dc8ec78
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:615:4 · **recurring** · fingerprint: 26959e3895827a98ea573e44
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:632:4 · **recurring** · fingerprint: cb5ac6fb2c2c270ac73b57e0
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:633:145 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:634:4 · **recurring** · fingerprint: c3aa5dc7d8225bd81a86e1b5
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:649:20 · **recurring** · fingerprint: 33dd6d895441c53e43bd10a2
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:20 · **recurring** · fingerprint: 0f7475f061de95d077b1bfe9
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:56 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:112 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:152 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:204 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:250 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:665:90 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/asd-ste100/references/repository-writing-policy.md:18:36 · **recurring** · fingerprint: fa71e22a78d6e4ce44e3a977
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **present-perfect** · .agent/skills/theme-factory/SKILL.md:3:218 · **recurring** · fingerprint: f588ce6668825b2c639b420e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been
- **synonym-rotation** · .agent/skills/theme-factory/SKILL.md:23:33 · **recurring** · fingerprint: c4e3b3a464edfeee7fc7bcc3
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** Display
- **semicolon** · .agent/skills/theme-factory/SKILL.md:23:159 · **recurring** · fingerprint: b09339406bea0fa2e1afd49f
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · .agent/skills/theme-factory/SKILL.md:26:38 · **recurring** · fingerprint: 8ec8403e57aec198db5ad83e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been chosen
- **passive-voice** · .agent/skills/theme-factory/SKILL.md:45:12 · **recurring** · fingerprint: ec5648e4b37ff6b0ffe90c1f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is defined
- **passive-voice** · .agent/skills/theme-factory/SKILL.md:52:25 · **recurring** · fingerprint: c7a1a2c629a0f37d6575c485
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected
- **semicolon** · .agent/skills/the-worker/assets/conversation-integrity-template.md:41:315 · **recurring** · fingerprint: f4b4f08dfca80fb5e43ae4e6
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Resolved findings

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:190:37 · **resolved** · fingerprint: 5776176caba0a90604144fef
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is linked

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/skill-creator/agents/grader.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 998
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/skill-creator/agents/grader.md:43:25 · **recurring** · fingerprint: 3ed0684ea12e354d46eea6bf
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **passive-voice** · .agent/skills/skill-creator/agents/grader.md:50:34 · **recurring** · fingerprint: 6108d0ad8d8376fa45ce1bd8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were filled

- **passive-voice** · .agent/skills/skill-creator/agents/grader.md:55:53 · **recurring** · fingerprint: 08a61d6427184a2b733e6f62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified

- **passive-voice** · .agent/skills/skill-creator/agents/grader.md:204:30 · **recurring** · fingerprint: 54f29ef94b400956a5d9ef80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being verified


### .agent/skills/skill-creator/agents/analyzer.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1147
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · .agent/skills/skill-creator/agents/analyzer.md:45:17 · **recurring** · fingerprint: 572d49165f68a06f3192f854
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were used

- **synonym-rotation** · .agent/skills/skill-creator/agents/analyzer.md:81:27 · **recurring** · fingerprint: 8618828539ad472e64245b5f
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modify

- **present-perfect** · .agent/skills/skill-creator/agents/analyzer.md:161:61 · **recurring** · fingerprint: f0e79378bd6b3ccceef251d9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have changed

- **passive-voice** · .agent/skills/skill-creator/agents/analyzer.md:200:37 · **recurring** · fingerprint: d37ba5ddd11156c4f02b3fb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being benchmarked


### .agent/skills/the-worker/references/image-provenance-and-webp.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 15
- **Hard findings:** 7
- **Baseline:** 0
- **Words:** 1248
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:15:100 · **recurring** · fingerprint: 42ccfb93a745583fff3188b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:293 · **recurring** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:467 · **recurring** · fingerprint: caa7a81dbcbd2ca9a41f3f6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied

- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:592 · **recurring** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:29:579 · **recurring** · fingerprint: 327d345785066c739b823948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted

- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:29:621 · **recurring** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:40:4 · **recurring** · fingerprint: 691140761bb44de115fa7cff
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:43:106 · **recurring** · fingerprint: 6d33e304d616c2a0e3cf5f55
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated

- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:43:357 · **recurring** · fingerprint: 5e4c8482fd167c730eb47fe1
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms

- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:45:50 · **recurring** · fingerprint: cd327a2cb9681d781a088b3a
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validates

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:47:139 · **recurring** · fingerprint: 42ccfb93a745583fff3188b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:57:366 · **recurring** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:65 · **recurring** · fingerprint: eda9543144c60d68e835bcc2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed

- **present-perfect** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:138 · **recurring** · fingerprint: 3e65c7310bbf6667184ee5cf
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been read

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:143 · **recurring** · fingerprint: 0b7ac6199463b1f46f7ddf4f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read


### .agent/skills/drawing/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 26
- **Hard findings:** 3
- **Baseline:** 24
- **Words:** 4899
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/SKILL.md:107:69 · **recurring** · fingerprint: 878ab3b6dde18c0e7cecb1b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is requested

- **passive-voice** · .agent/skills/drawing/SKILL.md:180:77 · **recurring** · fingerprint: 70e71f064591705fb5f3c193
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed

- **passive-voice** · .agent/skills/drawing/SKILL.md:189:31 · **recurring** · fingerprint: 1ed5dffcee6e3b4ff82826e6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is packaged

- **passive-voice** · .agent/skills/drawing/SKILL.md:207:35 · **recurring** · fingerprint: af4c1dada33dd8c4ae145291
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · .agent/skills/drawing/SKILL.md:208:27 · **recurring** · fingerprint: af4c1dada33dd8c4ae145291
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · .agent/skills/drawing/SKILL.md:209:35 · **recurring** · fingerprint: 6e55a67e178c1b3912ead6ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded

- **passive-voice** · .agent/skills/drawing/SKILL.md:216:76 · **recurring** · fingerprint: 5b854191f0bd6325026a19b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained

- **passive-voice** · .agent/skills/drawing/SKILL.md:255:21 · **recurring** · fingerprint: 2651d6044c8c968e365347e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are wanted

- **passive-voice** · .agent/skills/drawing/SKILL.md:259:15 · **recurring** · fingerprint: 7b7c5868ffded58b304476b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **passive-voice** · .agent/skills/drawing/SKILL.md:290:382 · **recurring** · fingerprint: 7b7c5868ffded58b304476b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **passive-voice** · .agent/skills/drawing/SKILL.md:290:557 · **recurring** · fingerprint: ea0cd474de27d7ba90f9b7fb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **synonym-rotation** · .agent/skills/drawing/SKILL.md:363:200 · **recurring** · fingerprint: 0cb5a57ca33c0b3b9c952ac3
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **passive-voice** · .agent/skills/drawing/SKILL.md:363:222 · **recurring** · fingerprint: d757e8ed6034e6ce6760ff48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was included

- **passive-voice** · .agent/skills/drawing/SKILL.md:363:300 · **recurring** · fingerprint: 7b7c5868ffded58b304476b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **passive-voice** · .agent/skills/drawing/SKILL.md:371:238 · **recurring** · fingerprint: 07b4ec6dcfb61be8e9a2c72b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **passive-voice** · .agent/skills/drawing/SKILL.md:388:19 · **recurring** · fingerprint: 59195f4fed84f98241ef6837
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is refused

- **passive-voice** · .agent/skills/drawing/SKILL.md:420:42 · **recurring** · fingerprint: ea0cd474de27d7ba90f9b7fb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/drawing/SKILL.md:421:50 · **recurring** · fingerprint: 12868b6cbd963577744ae291
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was produced

- **passive-voice** · .agent/skills/drawing/SKILL.md:422:42 · **recurring** · fingerprint: 44599ec66070748c61d0019f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · .agent/skills/drawing/SKILL.md:426:11 · **recurring** · fingerprint: ae23dc4e6ea7f38ced45381f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/drawing/SKILL.md:438:58 · **recurring** · fingerprint: 5523d48c475ed4874a2175cb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is warranted

- **synonym-rotation** · .agent/skills/drawing/SKILL.md:459:47 · **recurring** · fingerprint: f80cb025f7c2a164b46dd70d
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modify

- **present-perfect** · .agent/skills/drawing/SKILL.md:462:77 · **recurring** · fingerprint: 4f907506abc94065c68b9303
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has specified

- **synonym-rotation** · .agent/skills/drawing/SKILL.md:464:46 · **recurring** · fingerprint: 3b58c82498a5ccdfc67852a1
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirmed

- **passive-voice** · .agent/skills/drawing/SKILL.md:480:24 · **recurring** · fingerprint: 2c7485ca908820b38aaade5e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are determined

- **passive-voice** · .agent/skills/drawing/SKILL.md:506:13 · **recurring** · fingerprint: 33a3fa0cff6f306a7a93ed80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed


### .agent/skills/doc-coauthoring/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 28
- **Hard findings:** 9
- **Baseline:** 0
- **Words:** 2456
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:51:3 · **recurring** · fingerprint: b380e4795a1a535489af55a3
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:56:24 · **recurring** · fingerprint: e87615dcfea419143effe3a1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are answered

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:59:36 · **recurring** · fingerprint: 092e1440d84765a5998b315a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used

- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:65:53 · **recurring** · fingerprint: 785133e6de68fcf2ed362c2b
  - **Level:** advisory-free
  - **Message:** 'get' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** get

- **long-sentence** · .agent/skills/doc-coauthoring/SKILL.md:72:1 · **recurring** · fingerprint: 2a35f373caf351d2f1c207c4
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:72:22 · **recurring** · fingerprint: 7c6314612e64721268d82086
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:86:42 · **recurring** · fingerprint: d79f53a20eb266137f9d3a6b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being learned

- **long-sentence** · .agent/skills/doc-coauthoring/SKILL.md:94:1 · **recurring** · fingerprint: e83becde0a03b66c61fc8fee
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **present-perfect** · .agent/skills/doc-coauthoring/SKILL.md:97:20 · **recurring** · fingerprint: c43f81bd5eac082a83c3133a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been gathered

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:97:24 · **recurring** · fingerprint: 74f86169528f05b065c139b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been gathered

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:130:18 · **recurring** · fingerprint: f917bd3233f553bd15d7c0db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is agreed

- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:150:1 · **recurring** · fingerprint: 8d2d00522d8a837061c5ed1b
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **present-perfect** · .agent/skills/doc-coauthoring/SKILL.md:150:22 · **recurring** · fingerprint: c41f0a7ece739120265c01ab
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been created

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:150:26 · **recurring** · fingerprint: 94d4a5350ff0f65c87fcaed1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created

- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:156:20 · **recurring** · fingerprint: ed5186d0643ee8e5788c6553
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin

- **present-perfect** · .agent/skills/doc-coauthoring/SKILL.md:200:40 · **recurring** · fingerprint: 7ddbdeee5e1488d5616700c5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been drafted

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:200:44 · **recurring** · fingerprint: a9cf321d719d8e5a4c878b43
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been drafted

- **long-sentence** · .agent/skills/doc-coauthoring/SKILL.md:202:1 · **recurring** · fingerprint: b97bc94bd9213a4c44e510b6
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · .agent/skills/doc-coauthoring/SKILL.md:211:3 · **recurring** · fingerprint: 8ca3e39b1c98ae537285ec47
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:213:35 · **recurring** · fingerprint: 2160c31596b4f3fb5f40637c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:219:14 · **recurring** · fingerprint: e61aceb66bd95a2609f26a21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:233:21 · **recurring** · fingerprint: 36940177a105aa74789ecc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:234:23 · **recurring** · fingerprint: 36940177a105aa74789ecc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted

- **synonym-rotation** · .agent/skills/doc-coauthoring/SKILL.md:312:30 · **recurring** · fingerprint: 602cc782aa5df3313fae814f
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct

- **present-perfect** · .agent/skills/doc-coauthoring/SKILL.md:336:18 · **recurring** · fingerprint: 700bd4a73778993f60baf63d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has passed

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:342:50 · **recurring** · fingerprint: e61aceb66bd95a2609f26a21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:346:84 · **recurring** · fingerprint: ca548ddaee5fc2417d9c9385
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was developed

- **passive-voice** · .agent/skills/doc-coauthoring/SKILL.md:348:30 · **recurring** · fingerprint: 952ffdaac946082abede5a85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is received


### .agent/skills/the-worker/assets/session-brief-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 288
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/INITIALIZATION_POLICY.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 5
- **Hard findings:** 2
- **Baseline:** 4
- **Words:** 1551
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **present-perfect** · .agent/INITIALIZATION_POLICY.md:38:53 · **recurring** · fingerprint: a68d4b2091de8244b08b0984
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved

- **passive-voice** · .agent/INITIALIZATION_POLICY.md:38:57 · **recurring** · fingerprint: cc8f76f7786acf5d8492b443
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved

- **long-sentence** · .agent/INITIALIZATION_POLICY.md:146:3 · **recurring** · fingerprint: 18db183bae30a8739132c97b
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · .agent/INITIALIZATION_POLICY.md:155:154 · **recurring** · fingerprint: 0bd04eaf142f6db0f46ab9bd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored

- **semicolon** · .agent/INITIALIZATION_POLICY.md:184:66 · **recurring** · fingerprint: 79226f1a409be7642928b566
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/internal-comms/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 196
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **long-sentence** · .agent/skills/internal-comms/SKILL.md:3:136 · **recurring** · fingerprint: 536e2e7ba4848c22f116b688
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words


### .agent/skills/drawing/references/archive-and-delivery.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 7
- **Words:** 458
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **present-perfect** · .agent/skills/drawing/references/archive-and-delivery.md:11:167 · **recurring** · fingerprint: c5d02a5017b863230f3b252a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been verified

- **passive-voice** · .agent/skills/drawing/references/archive-and-delivery.md:11:172 · **recurring** · fingerprint: 6c7d74fe7edec2361ca15c24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **synonym-rotation** · .agent/skills/drawing/references/archive-and-delivery.md:45:13 · **recurring** · fingerprint: 8d54e05e87ff737f0d036438
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify


### .agent/skills/grilling/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 289
- **Findings per 100 words:** 2.1

#### Complete diagnostics

- **long-sentence** · .agent/skills/grilling/SKILL.md:28:48 · **recurring** · fingerprint: bee2beaf2e1eb932b38195e7
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · .agent/skills/grilling/SKILL.md:28:193 · **recurring** · fingerprint: bf801ae5817722c54dd2a44b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/grilling/SKILL.md:28:255 · **recurring** · fingerprint: a1d366861065f2ff55895993
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **semicolon** · .agent/skills/grilling/SKILL.md:28:397 · **recurring** · fingerprint: bf801ae5817722c54dd2a44b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/grilling/SKILL.md:30:13 · **recurring** · fingerprint: 37bb72090ae983ecb14eb362
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **present-perfect** · .agent/skills/grilling/SKILL.md:30:166 · **recurring** · fingerprint: aec45cb5f1f28de5e7c0d37a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached


### .agent/skills/internal-comms/examples/3p-updates.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 552
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · .agent/skills/internal-comms/examples/3p-updates.md:2:9 · **recurring** · fingerprint: 2fb37222a40a36ee64a89558
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **long-sentence** · .agent/skills/internal-comms/examples/3p-updates.md:4:141 · **recurring** · fingerprint: f725d493718a8ba218869f2c
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **present-perfect** · .agent/skills/internal-comms/examples/3p-updates.md:7:28 · **recurring** · fingerprint: d8b362e021a14da1a7239b46
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has accomplished


### .agent/skills/drawing/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 406
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/midnight-galaxy.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 70
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/skill-creator/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 49
- **Hard findings:** 43
- **Baseline:** 0
- **Words:** 4775
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:3:100 · **recurring** · fingerprint: c0128c8cbc5de6229042e665
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:16:5 · **recurring** · fingerprint: b74a4ea33e6c64c04b84cd24
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:16:182 · **recurring** · fingerprint: 1ff41be9696d1a59f1840bb2
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:18:3 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:22:1 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:22:213 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:26:1 · **recurring** · fingerprint: 8effdf0ea562678b8a496c79
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:28:1 · **recurring** · fingerprint: b619282f2a5a1fd5e4b7bfbe
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **passive-voice** · .agent/skills/skill-creator/SKILL.md:28:22 · **recurring** · fingerprint: c93247a38d888c7b3de90997
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:34:105 · **recurring** · fingerprint: a22ffb60a808d0d6b87d943d
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:39:3 · **recurring** · fingerprint: 0144c24eee82255498c96af9
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:41:1 · **recurring** · fingerprint: be024ce86df5418f04fe2f9a
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:54:35 · **recurring** · fingerprint: c08f6eef4e964b84145e106f
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:60:1 · **recurring** · fingerprint: 39093e7b1986c825d3ea89a1
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:67:398 · **recurring** · fingerprint: b2a04b8c675cc2a131a9420c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:67:467 · **recurring** · fingerprint: c5763365a63d688477d18164
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** display

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:67:592 · **recurring** · fingerprint: 7453e8516a384f818b51a5bb
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:96:3 · **recurring** · fingerprint: 7453e8516a384f818b51a5bb
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **semicolon** · .agent/skills/skill-creator/SKILL.md:96:32 · **recurring** · fingerprint: ffbd5dd7fe5b566a79c3f5ce
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/skill-creator/SKILL.md:171:190 · **recurring** · fingerprint: d1d1f4eacd81ba68da187af9
  - **Level:** advisory-free
  - **Message:** 'launch' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** Launch

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:203:1 · **recurring** · fingerprint: be024ce86df5418f04fe2f9a
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/skill-creator/SKILL.md:223:15 · **recurring** · fingerprint: c641af7a17b87772a029e0ee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are done

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:225:386 · **recurring** · fingerprint: 063eab38cb8b453553940fb6
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:234:106 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **semicolon** · .agent/skills/skill-creator/SKILL.md:249:57 · **recurring** · fingerprint: ffbd5dd7fe5b566a79c3f5ce
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/skill-creator/SKILL.md:256:29 · **recurring** · fingerprint: cb5d2b8747a0ba90b3ee437b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was given

- **passive-voice** · .agent/skills/skill-creator/SKILL.md:259:33 · **recurring** · fingerprint: 9065f6de65e3a15641cce538
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run

- **present-perfect** · .agent/skills/skill-creator/SKILL.md:294:68 · **recurring** · fingerprint: 4d285f47dacf2b7c3b058584
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has reviewed

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:298:38 · **recurring** · fingerprint: b2a04b8c675cc2a131a9420c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:298:522 · **recurring** · fingerprint: 8effdf0ea562678b8a496c79
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:300:78 · **recurring** · fingerprint: 9e45bb53cb53b0272be7c185
  - **Level:** advisory-free
  - **Message:** Sentence has 52 words (cap 25). Split it.
  - **Matched text:** 52 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:302:255 · **recurring** · fingerprint: 02795ed552c2e6222c40b77d
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:302:485 · **recurring** · fingerprint: 6c92d547d198a40e19ee323d
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:304:50 · **recurring** · fingerprint: 0144c24eee82255498c96af9
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/skill-creator/SKILL.md:306:138 · **recurring** · fingerprint: ffbd5dd7fe5b566a79c3f5ce
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:313:214 · **recurring** · fingerprint: 12e0ce731b8ac8fd76d18fc8
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:327:1 · **recurring** · fingerprint: c10b33c4d79df51c6b9682af
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:348:429 · **recurring** · fingerprint: 063eab38cb8b453553940fb6
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:356:1 · **recurring** · fingerprint: 0144c24eee82255498c96af9
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:356:187 · **recurring** · fingerprint: b619282f2a5a1fd5e4b7bfbe
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:394:56 · **recurring** · fingerprint: c0128c8cbc5de6229042e665
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:394:362 · **recurring** · fingerprint: 8effdf0ea562678b8a496c79
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:398:228 · **recurring** · fingerprint: 28c50f5addd36eab74a135cb
  - **Level:** advisory-free
  - **Message:** Sentence has 47 words (cap 25). Split it.
  - **Matched text:** 47 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:424:206 · **recurring** · fingerprint: 7453e8516a384f818b51a5bb
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:426:264 · **recurring** · fingerprint: bb3182e438b02d99f7821313
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:451:3 · **recurring** · fingerprint: f0c41082c1096f144d45e58c
  - **Level:** advisory-free
  - **Message:** Sentence has 66 words (cap 25). Split it.
  - **Matched text:** 66 words

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:454:3 · **recurring** · fingerprint: b619282f2a5a1fd5e4b7bfbe
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **passive-voice** · .agent/skills/skill-creator/SKILL.md:480:33 · **recurring** · fingerprint: 479ee2cb0da9e9d902d6bfb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **long-sentence** · .agent/skills/skill-creator/SKILL.md:483:93 · **recurring** · fingerprint: 0144c24eee82255498c96af9
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words


### workspace/adr/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 523
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 8
- **Hard findings:** 0
- **Baseline:** 7
- **Words:** 2716
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:7:89 · **recurring** · fingerprint: 164d4067e1e89a1f2ae2ca64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is designed

- **present-perfect** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:1 · **recurring** · fingerprint: 2ad598367272b6e37f11bb9f
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been completed

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:5 · **recurring** · fingerprint: a96bc88cfe9eb32ee5d37d49
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been completed

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:20:13 · **recurring** · fingerprint: 7be16217c093138da7f26077
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is built

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:37:47 · **recurring** · fingerprint: e6b31276bf3e3fe5b518d539
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:39:38 · **recurring** · fingerprint: e6b31276bf3e3fe5b518d539
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:57:65 · **recurring** · fingerprint: c4ef08a0a9dea42add5ac36c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:268:11 · **recurring** · fingerprint: c4ef08a0a9dea42add5ac36c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used


### .agent/skills/drawing/references/patterns/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 795
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/references/patterns/README.md:34:143 · **recurring** · fingerprint: 8ea61fc966fb2cb721264549
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded


### workspace/ADR_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 349
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/xlsx/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 34
- **Hard findings:** 25
- **Baseline:** 0
- **Words:** 1408
- **Findings per 100 words:** 2.4

#### Complete diagnostics

- **long-sentence** · .agent/skills/xlsx/SKILL.md:3:90 · **recurring** · fingerprint: bc255bb6ff9d923c5f3753b7
  - **Level:** advisory-free
  - **Message:** Sentence has 50 words (cap 25). Split it.
  - **Matched text:** 50 words

- **semicolon** · .agent/skills/xlsx/SKILL.md:3:297 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/xlsx/SKILL.md:3:363 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/xlsx/SKILL.md:3:406 · **recurring** · fingerprint: a1017e69a4c1eaf91ce78914
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · .agent/skills/xlsx/SKILL.md:3:776 · **recurring** · fingerprint: 9e5463e9eb5bd2f364ef7820
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/xlsx/SKILL.md:3:953 · **recurring** · fingerprint: 9f552b549d8874f678a17d04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is involved

- **semicolon** · .agent/skills/xlsx/SKILL.md:13:80 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/xlsx/SKILL.md:16:42 · **recurring** · fingerprint: f40d0bf8e882628eef890729
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preinstalled

- **semicolon** · .agent/skills/xlsx/SKILL.md:16:91 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/xlsx/SKILL.md:23:79 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/xlsx/SKILL.md:26:246 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/xlsx/SKILL.md:27:3 · **recurring** · fingerprint: 9e5463e9eb5bd2f364ef7820
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/xlsx/SKILL.md:27:207 · **recurring** · fingerprint: 18a172b98eb69eb6ddd99c43
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were asked

- **long-sentence** · .agent/skills/xlsx/SKILL.md:40:1 · **recurring** · fingerprint: 0646b97517ca5d69236b9007
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **long-sentence** · .agent/skills/xlsx/SKILL.md:44:8 · **recurring** · fingerprint: 9e5463e9eb5bd2f364ef7820
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/xlsx/SKILL.md:44:71 · **recurring** · fingerprint: baad3877e021c564d5e1c82d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was recalculated

- **semicolon** · .agent/skills/xlsx/SKILL.md:55:40 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/xlsx/SKILL.md:58:80 · **recurring** · fingerprint: 685502200eabe22e68ffa6b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed

- **long-sentence** · .agent/skills/xlsx/SKILL.md:66:3 · **recurring** · fingerprint: 9e5463e9eb5bd2f364ef7820
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **long-sentence** · .agent/skills/xlsx/SKILL.md:67:81 · **recurring** · fingerprint: ea4acdb6652afd8c9eb38361
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · .agent/skills/xlsx/SKILL.md:68:17 · **recurring** · fingerprint: f15854036a61bd943ceeea97
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reported

- **synonym-rotation** · .agent/skills/xlsx/SKILL.md:68:148 · **recurring** · fingerprint: 1f0dd672e3d5dfbde97b90fb
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **semicolon** · .agent/skills/xlsx/SKILL.md:72:100 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/xlsx/SKILL.md:75:116 · **recurring** · fingerprint: 55449c75856b6d1a3dc4263d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **semicolon** · .agent/skills/xlsx/SKILL.md:78:160 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/xlsx/SKILL.md:79:3 · **recurring** · fingerprint: 1b6abd36a2b499ad1787511b
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **passive-voice** · .agent/skills/xlsx/SKILL.md:79:167 · **recurring** · fingerprint: 85c2fc0ec973eb11117dc903
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are saved

- **passive-voice** · .agent/skills/xlsx/SKILL.md:80:37 · **recurring** · fingerprint: bb17ecc485a14e6012fc6236
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is flattened

- **semicolon** · .agent/skills/xlsx/SKILL.md:80:90 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/xlsx/SKILL.md:82:3 · **recurring** · fingerprint: 3e44e64ba0811cfeb37369fa
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words

- **long-sentence** · .agent/skills/xlsx/SKILL.md:89:1 · **recurring** · fingerprint: ba2566fcf1c485f752996553
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **long-sentence** · .agent/skills/xlsx/SKILL.md:93:1 · **recurring** · fingerprint: a1017e69a4c1eaf91ce78914
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **semicolon** · .agent/skills/xlsx/SKILL.md:95:68 · **recurring** · fingerprint: 44f2460db5baff6e34d85fbf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/xlsx/SKILL.md:98:1 · **recurring** · fingerprint: 8045b4020231327ee7344fe3
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words


### .takeout/images/README-2.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 10
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 2048
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · .takeout/images/README-2.md:26:255 · **recurring** · fingerprint: da41a5c6b07ad58b75b5ba18
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged

- **passive-voice** · .takeout/images/README-2.md:30:214 · **recurring** · fingerprint: 8b6c0e33f6a02796ddb94e33
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated

- **passive-voice** · .takeout/images/README-2.md:96:188 · **recurring** · fingerprint: 32c844d282b1c11074093437
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied

- **passive-voice** · .takeout/images/README-2.md:97:44 · **recurring** · fingerprint: 9f69f42d8f51f191d0d58188
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **passive-voice** · .takeout/images/README-2.md:142:209 · **recurring** · fingerprint: 4df4cb023cf9d1ec7c96ddca
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recognized

- **semicolon** · .takeout/images/README-2.md:142:269 · **recurring** · fingerprint: f712923c6613939c83fbaec2
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .takeout/images/README-2.md:142:296 · **recurring** · fingerprint: a5ce13710f2822f72f96dc94
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rejected

- **passive-voice** · .takeout/images/README-2.md:144:203 · **recurring** · fingerprint: f1360185b073e84d28f1efb1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

- **semicolon** · .takeout/images/README-2.md:185:266 · **recurring** · fingerprint: f712923c6613939c83fbaec2
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .takeout/images/README-2.md:208:40 · **recurring** · fingerprint: 7b0b8a5e204fdc949021e113
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved


### .agent/skills/theme-factory/themes/sunset-boulevard.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 76
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/drawing/references/patterns/successful-patterns.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 6
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 816
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:3:121 · **recurring** · fingerprint: db01433d77ee17d96c56fcd6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed

- **present-perfect** · .agent/skills/drawing/references/patterns/successful-patterns.md:25:23 · **recurring** · fingerprint: d2a1623a3515232827743a0f
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been tested

- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:25:27 · **recurring** · fingerprint: d31be00566b2fb6271a4c56f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:29:225 · **recurring** · fingerprint: 2c118b5809e6b19b18b6deff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were returned

- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:30:195 · **recurring** · fingerprint: 16c29dda93a863fa7f009a6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reused

- **passive-voice** · .agent/skills/drawing/references/patterns/successful-patterns.md:47:158 · **recurring** · fingerprint: 2cc2deaed296de61f4c7ac5e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being requested


### workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 43
- **Hard findings:** 21
- **Baseline:** 0
- **Words:** 3304
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:66:61 · **recurring** · fingerprint: 3d753fd2c4828ff430fdb6c2
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:74:38 · **recurring** · fingerprint: 0642057a58aa1965274b9762
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:104 · **recurring** · fingerprint: f331458e480ad4445c592130
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:100:85 · **recurring** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:67 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:157 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:254 · **recurring** · fingerprint: c165f6e8824400b2723a92ab
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is controlled

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:106:205 · **recurring** · fingerprint: 0ee5ca333d00a4f63756c25b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is generated

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:107:185 · **recurring** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:119:123 · **recurring** · fingerprint: 3a2d463bad961d4a2f26d082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was evaluated

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:103 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:191 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:46 · **recurring** · fingerprint: 421ce0d953be11182d9e810a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stored

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:115 · **recurring** · fingerprint: 6937ea80a6afca82e7f414d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:133:54 · **recurring** · fingerprint: 2e0dfecf96eeb4735f44ac24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:143:183 · **recurring** · fingerprint: f8411801c3d8953cd8c2acbe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is identified

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:149:70 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:150:203 · **recurring** · fingerprint: a0bfc1f95f604fc3f864783e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is performed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:149 · **recurring** · fingerprint: 0da19e7aab04deb7911a62a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are unchanged

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:213 · **recurring** · fingerprint: fa6c012aa723a1be302eb24c
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validates

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:157:125 · **recurring** · fingerprint: 87a065e710f1792ecf1034fc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is migrated

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:158:130 · **recurring** · fingerprint: 051c97c1441fc96df828d5f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:178:70 · **recurring** · fingerprint: 494f747b32f0b27099114e91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are filtered

- **long-sentence** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:190:3 · **recurring** · fingerprint: 0dc1b5fa54679407d060b44e
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:192:43 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:200:137 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:263 · **recurring** · fingerprint: ca82b6e19a6f4ef4347ae654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:293 · **recurring** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:216:263 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:139 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:162 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:188 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:219 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:222:62 · **recurring** · fingerprint: 6b4576cd5b0f0b9ac4699130
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was deleted

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:89 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:134 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:186 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:246 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:290 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:335 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:77 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:119 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:177 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/define-goal/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 11
- **Hard findings:** 9
- **Baseline:** 0
- **Words:** 857
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **long-sentence** · .agent/skills/define-goal/SKILL.md:3:14 · **recurring** · fingerprint: 6e69702dd7b70f9e58a5b7d0
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **semicolon** · .agent/skills/define-goal/SKILL.md:3:303 · **recurring** · fingerprint: 64f46a5a0114f5419c00ca80
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/define-goal/SKILL.md:17:6 · **recurring** · fingerprint: 3f9fc482d99586da767ee8ca
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **synonym-rotation** · .agent/skills/define-goal/SKILL.md:31:41 · **recurring** · fingerprint: 3c0f0de82a3eb77b2f1b926d
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **passive-voice** · .agent/skills/define-goal/SKILL.md:39:125 · **recurring** · fingerprint: cfda5ea15fb2c9e0c2cc445f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are sharpened

- **long-sentence** · .agent/skills/define-goal/SKILL.md:45:6 · **recurring** · fingerprint: 3f9fc482d99586da767ee8ca
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **passive-voice** · .agent/skills/define-goal/SKILL.md:58:46 · **recurring** · fingerprint: f1c7de13906779a00f58730f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **long-sentence** · .agent/skills/define-goal/SKILL.md:66:3 · **recurring** · fingerprint: 6e69702dd7b70f9e58a5b7d0
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **synonym-rotation** · .agent/skills/define-goal/SKILL.md:66:130 · **recurring** · fingerprint: f5bebd30fc084be62b91ef54
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **long-sentence** · .agent/skills/define-goal/SKILL.md:70:3 · **recurring** · fingerprint: 61b81b0b3f3fa6a8612aac95
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **synonym-rotation** · .agent/skills/define-goal/SKILL.md:82:51 · **recurring** · fingerprint: de8e3efc53afc3d7e6a6854b
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix


### .agent/skills/drawing/references/generation-recovery-and-provenance.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 19
- **Hard findings:** 0
- **Baseline:** 17
- **Words:** 2756
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:13:135 · **recurring** · fingerprint: a177e1fb8d855758e83b2fd3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:19:83 · **recurring** · fingerprint: 0a87489c591fb9a534219558
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disallowed

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:42:73 · **recurring** · fingerprint: 5845722ff39b083ac0f24c3c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:45:14 · **recurring** · fingerprint: 48a3cd39793032bad22fe180
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:47:74 · **recurring** · fingerprint: 48a3cd39793032bad22fe180
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:49:12 · **recurring** · fingerprint: 9f1e51594216eeb8d88ba38f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was included

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:86:20 · **recurring** · fingerprint: 2299f7304854c875ec35f372
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:97:52 · **recurring** · fingerprint: 7f9a0fe095243ed196597f7b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:119:29 · **recurring** · fingerprint: 0b4997f48c7f6654c29d6d42
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:123:77 · **recurring** · fingerprint: 2cee6ee6ee298d87860d2d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was approved

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:155:37 · **recurring** · fingerprint: 521c428794d37789264af034
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:159:37 · **recurring** · fingerprint: 295ce5dc4e797d6abdf84ff4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:181:62 · **recurring** · fingerprint: 8a2876168a6a0e61c7f3585a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:182:28 · **recurring** · fingerprint: 4a8888e0cc3de9ff35bb448b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:184:296 · **recurring** · fingerprint: 2ef0f783a815fbcc7919f6f8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:184:336 · **recurring** · fingerprint: ef7bd8ba29534123319befef
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been uploaded

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:185:31 · **recurring** · fingerprint: 4a8888e0cc3de9ff35bb448b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:186:26 · **recurring** · fingerprint: f3267cff8e89aa14f0508dcc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed

- **passive-voice** · .agent/skills/drawing/references/generation-recovery-and-provenance.md:205:20 · **recurring** · fingerprint: 7e02c138711b8a962490d168
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized


### .agent/skills/internal-comms/examples/faq-answers.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 403
- **Findings per 100 words:** 1.7

#### Complete diagnostics

- **passive-voice** · .agent/skills/internal-comms/examples/faq-answers.md:2:55 · **recurring** · fingerprint: 9fe837ec91bfe0df1a9a74de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **long-sentence** · .agent/skills/internal-comms/examples/faq-answers.md:2:225 · **recurring** · fingerprint: 3cde4b8a40b4b4e9d9003f98
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **long-sentence** · .agent/skills/internal-comms/examples/faq-answers.md:4:3 · **recurring** · fingerprint: 9d88cb2e963737b24f2578f0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · .agent/skills/internal-comms/examples/faq-answers.md:7:1 · **recurring** · fingerprint: 9d88cb2e963737b24f2578f0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · .agent/skills/internal-comms/examples/faq-answers.md:12:3 · **recurring** · fingerprint: 771172c46821432e60b015b5
  - **Level:** advisory-free
  - **Message:** Sentence has 49 words (cap 25). Split it.
  - **Matched text:** 49 words

- **passive-voice** · .agent/skills/internal-comms/examples/faq-answers.md:12:20 · **recurring** · fingerprint: 9fe837ec91bfe0df1a9a74de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **passive-voice** · .agent/skills/internal-comms/examples/faq-answers.md:12:130 · **recurring** · fingerprint: 9fe837ec91bfe0df1a9a74de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked


### .agent/skills/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 425
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/drawing/references/style-guide.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 462
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/references/style-guide.md:60:31 · **recurring** · fingerprint: 92028f1dabfce4a5dc9d32b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was classified


### .agent/skills/github-actions/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 2534
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · .agent/skills/github-actions/SKILL.md:21:206 · **recurring** · fingerprint: ce5c879312639d5e4a37c1f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted

- **passive-voice** · .agent/skills/github-actions/SKILL.md:23:59 · **recurring** · fingerprint: 5ef6ce13baf5600a1694be8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided

- **present-perfect** · .agent/skills/github-actions/SKILL.md:33:40 · **recurring** · fingerprint: e8019ef8bf6c31ab6be19a58
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached


### .agent/skills/drawing/assets/attempt-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 593
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/assets/attempt-template.md:61:53 · **recurring** · fingerprint: fe7c9e1555e50fd0d3ead59c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned


### .agent/skills/theme-factory/themes/ocean-depths.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 76
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 10
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 2702
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **passive-voice** · .agent/SESSION_START.md:28:36 · **recurring** · fingerprint: dc938b5856f3e903edbd297a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was retrieved

- **semicolon** · .agent/SESSION_START.md:31:179 · **recurring** · fingerprint: 499417ab68edb8c596a98f0f
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · .agent/SESSION_START.md:35:114 · **recurring** · fingerprint: 7e401b80fb2469d88b8b16c6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved

- **passive-voice** · .agent/SESSION_START.md:35:119 · **recurring** · fingerprint: 65e01e8ee980bec2c691cd07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved

- **synonym-rotation** · .agent/SESSION_START.md:74:4 · **recurring** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · .agent/SESSION_START.md:75:161 · **recurring** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/SESSION_START.md:76:63 · **recurring** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **passive-voice** · .agent/SESSION_START.md:220:167 · **recurring** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **present-perfect** · .agent/SESSION_START.md:236:210 · **recurring** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed

- **long-sentence** · .agent/SESSION_START.md:260:1 · **recurring** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words


### .agent/skills/theme-factory/themes/modern-minimalist.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 74
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/the-worker/assets/session-summary-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 106
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/the-worker/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 5288
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 166
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 50
- **Hard findings:** 23
- **Baseline:** 0
- **Words:** 9822
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:36:10 · **recurring** · fingerprint: a737104c50ceb40f303a4a01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended

- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:332 · **recurring** · fingerprint: 63b66afb8b84b4750380eace
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:388 · **recurring** · fingerprint: e18acfaf818e2c30f6ca30e9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:158:1 · **recurring** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:169:21 · **recurring** · fingerprint: 34fd4b4fc86f7c4829f49935
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validated

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:179:143 · **recurring** · fingerprint: 8fab87c9578c4937b0124edf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:181:62 · **recurring** · fingerprint: 7c3c1ace5ec3d5c53c98a4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are observed

- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:183:69 · **recurring** · fingerprint: 1614dc41c4b7be8e66e6f0d4
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:120 · **recurring** · fingerprint: 2e23d59621877db75c28ce78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:223 · **recurring** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:206:177 · **recurring** · fingerprint: ff8dedd324f39ede5ee75f82
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:208:43 · **recurring** · fingerprint: ae6b75fe50ddf475f002c2af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is fragmented

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:210:53 · **recurring** · fingerprint: e6a0a6a3cb10281e485f4ced
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been measured

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:235:53 · **recurring** · fingerprint: e0805effa50f8c2d06788a7e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:261:171 · **recurring** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:292:60 · **recurring** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:295:388 · **recurring** · fingerprint: 84a34fb70b809525fcff26b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been piloted

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:296:52 · **recurring** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:313:90 · **recurring** · fingerprint: cd8c27dadbc8cbf2ffa0ea4b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unsupported

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:325:178 · **recurring** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:346:218 · **recurring** · fingerprint: a27c714d52cff462c278171d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:458:36 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:482:251 · **recurring** · fingerprint: a484bb1a5b40074d480f3f91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is configured

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:502:30 · **recurring** · fingerprint: 0de287d1c4eae57b62d477b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:503:52 · **recurring** · fingerprint: cbf03a5bdfbefc8d301bac6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are resolved

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:504:22 · **recurring** · fingerprint: ba2af3047b1dbc7bfdba2dd0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are classified

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:541:4 · **recurring** · fingerprint: 93b3c8314ad783839cf934a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:585:23 · **recurring** · fingerprint: ebe3a0eaf57219e6e13da654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is treated

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:586:94 · **recurring** · fingerprint: b1897a649c20569be1ac0618
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:598:63 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:610:53 · **recurring** · fingerprint: 1e8f06c794753d0da4c374f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are supported

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:611:217 · **recurring** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:613:256 · **recurring** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:640:93 · **recurring** · fingerprint: 316a7cc78530dc52ed55aeb6
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:670:104 · **recurring** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:4 · **recurring** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:107 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:166 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:212 · **recurring** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:680:4 · **recurring** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:48 · **recurring** · fingerprint: 5c278ad2f255230faa055f76
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:90 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:122 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:700:45 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:707:246 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:708:194 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:155 · **recurring** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:240 · **recurring** · fingerprint: dd5a9425158b41b001c9b936
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:712:91 · **recurring** · fingerprint: c6bfceae059912f8aadd9e2e
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fixed

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:718:1 · **recurring** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words


### .agent/skills/philosophy-religion-asceticism/references/source-standards.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 1
- **Words:** 1467
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/source-standards.md:99:19 · **recurring** · fingerprint: 31b1c652f1950eb652c297b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/source-standards.md:194:41 · **recurring** · fingerprint: 3cf3d888bb09d615bc5ecf6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being cited


### .agent/skills/philosophy-religion-asceticism/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 8
- **Hard findings:** 0
- **Baseline:** 7
- **Words:** 2387
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:53:21 · **recurring** · fingerprint: 636319e0f7c3b3cd746ca815
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:94:11 · **recurring** · fingerprint: 0213e8215e33b96f40b0cceb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disputed

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:144:43 · **recurring** · fingerprint: 9a59a040c9cc2c665d08de61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are related

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:167:67 · **recurring** · fingerprint: 744c323ac844ab9c1885a174
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:178:68 · **recurring** · fingerprint: 1ecb948b37f33ea375b33a87
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supported

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:179:43 · **recurring** · fingerprint: 467eea53004536ffbc6f6f83
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:291:3 · **recurring** · fingerprint: 61cfd4a2dc271720d2c83a22
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been excluded

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/SKILL.md:292:52 · **recurring** · fingerprint: 85c8f8886cfc0e70af2fa91e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been kept


### .agent/skills/internal-comms/examples/general-comms.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 85
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/internal-comms/examples/general-comms.md:2:11 · **recurring** · fingerprint: ccc63107771e2eb7ec53a4e4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked


### .agent/skills/pdf/REFERENCE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 394
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/decision-governance/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 2913
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · .agent/skills/decision-governance/SKILL.md:84:206 · **recurring** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:103:283 · **recurring** · fingerprint: 7c881c753a4078cb6de1c860
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:107:38 · **recurring** · fingerprint: 7e15f02585cf13c74c4d9066
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **passive-voice** · .agent/skills/decision-governance/SKILL.md:109:34 · **recurring** · fingerprint: ed925553639766f753b1e47c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included

- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:47 · **recurring** · fingerprint: c6fdcf445b99331b3955a823
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated

- **semicolon** · .agent/skills/decision-governance/SKILL.md:115:57 · **recurring** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:102 · **recurring** · fingerprint: c5cbda1d2fcdc95906e3b0f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied

- **passive-voice** · .agent/skills/decision-governance/SKILL.md:117:86 · **recurring** · fingerprint: 9248adb057e0be913c820595
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed

- **semicolon** · .agent/skills/decision-governance/SKILL.md:131:65 · **recurring** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/asd-ste100/references/writing-rules.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 8
- **Hard findings:** 0
- **Baseline:** 6
- **Words:** 706
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **present-perfect** · .agent/skills/asd-ste100/references/writing-rules.md:7:511 · **recurring** · fingerprint: f07d3c84432af463c7f72518
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been

- **present-perfect** · .agent/skills/asd-ste100/references/writing-rules.md:26:84 · **recurring** · fingerprint: 52fb0410311ad16756b7bfe3
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received

- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:26:129 · **recurring** · fingerprint: 9c80fb1e6e5000284a29137e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed

- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:27:16 · **recurring** · fingerprint: fcfbdbdcf23b08e64d0f93c8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted

- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:30:16 · **recurring** · fingerprint: b35ca4ac1ff82c9bf3fc1e3d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:31:17 · **recurring** · fingerprint: 9c80fb1e6e5000284a29137e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed

- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:37:58 · **recurring** · fingerprint: c6fc29287cb5e7f548957604
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are capped

- **passive-voice** · .agent/skills/asd-ste100/references/writing-rules.md:50:5 · **recurring** · fingerprint: 02478fa831f501fa3dd2ba3d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was designed


### .agent/skills/drawing/references/series-continuity-and-iteration.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 9
- **Hard findings:** 0
- **Baseline:** 9
- **Words:** 3262
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:44:40 · **recurring** · fingerprint: 3c65876301fed0b3c507542f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is inferred

- **present-perfect** · .agent/skills/drawing/references/series-continuity-and-iteration.md:50:245 · **recurring** · fingerprint: 532631bc6b42b9ef571cc030
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has declared

- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:78:42 · **recurring** · fingerprint: d9528dbaf4bbc041cf2ae3ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is ordered

- **present-perfect** · .agent/skills/drawing/references/series-continuity-and-iteration.md:82:259 · **recurring** · fingerprint: 2ad2d875e478e9ef55228ab2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has established

- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:94:27 · **recurring** · fingerprint: 1a1b591ca9810210a11e3bb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are locked

- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:134:15 · **recurring** · fingerprint: 0e03aa3ca8bee4298b54aa2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:140:14 · **recurring** · fingerprint: 0e03aa3ca8bee4298b54aa2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:164:73 · **recurring** · fingerprint: 45565ae1723777f3f799c982
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being edited

- **passive-voice** · .agent/skills/drawing/references/series-continuity-and-iteration.md:177:79 · **recurring** · fingerprint: e9f8f5370d87e09abc939413
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached


### .agent/skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 4632
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **long-sentence** · .agent/skills/document-standards/references/document-type-catalog.md:45:121 · **recurring** · fingerprint: 2dd7b3784611553473e6528c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:45:212 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:45:458 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:191 · **recurring** · fingerprint: 3ae524e22114a03c0ab4422a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:228 · **recurring** · fingerprint: 2115664c682d98befee7c6f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is tracked

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:126:145 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:143 · **recurring** · fingerprint: d54e065531122bd43e42b93b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are allocated


### .agent/skills/the-worker/references/archive-records-and-image-prompts.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 28
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 3538
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:13:64 · **recurring** · fingerprint: e5525626c1967e0a340ca6a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is curated

- **semicolon** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:19:336 · **recurring** · fingerprint: e1fd3f41b42938a1e8507bbb
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:21:109 · **recurring** · fingerprint: 69ced9ce37a5222737761146
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:33:8 · **recurring** · fingerprint: f63bb7a71c949cd73ccbef9b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was completed

- **synonym-rotation** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:52:20 · **recurring** · fingerprint: 03fe26b802d24bd62ff0a202
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:87:21 · **recurring** · fingerprint: 0612acc3ded54049ec675ae4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:96:11 · **recurring** · fingerprint: 2c1da6bfaf483087ef9327af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:124:164 · **recurring** · fingerprint: 94e51011211d6fc251cabb65
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:127:130 · **recurring** · fingerprint: 783ad4a07e61c15afad1e585
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:131:343 · **recurring** · fingerprint: d164c6cd28e0ab9df8f188d9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:188:170 · **recurring** · fingerprint: 433dafd5d692277cca6a4c24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was supplied

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:191:23 · **recurring** · fingerprint: 46d08da660ad9f0d48a138b0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being tested

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:229:65 · **recurring** · fingerprint: fbe839b26aecd31e753f74ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:240:24 · **recurring** · fingerprint: 3d87aa3e3e05414a6fc20859
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:246:176 · **recurring** · fingerprint: bac7b5e46fbea597ad4dbea1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:260:44 · **recurring** · fingerprint: 5d36f6e71392c533b3845506
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:270:68 · **recurring** · fingerprint: d012538c491cfde62ff1fdd9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:271:36 · **recurring** · fingerprint: fbe839b26aecd31e753f74ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:271:58 · **recurring** · fingerprint: 7c258b1c239930b3450bf575
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unverified

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:274:4 · **recurring** · fingerprint: a703317ebbefd56b39b629a9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:275:78 · **recurring** · fingerprint: ce5982a1a9d2565e0ee20170
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:276:48 · **recurring** · fingerprint: fa512a90594737a041e9d5c6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:277:75 · **recurring** · fingerprint: fbe839b26aecd31e753f74ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:278:68 · **recurring** · fingerprint: c88aa7cca35223c0301d1ceb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:288:20 · **recurring** · fingerprint: c330a30e67f8d2c28b084e65
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:292:53 · **recurring** · fingerprint: ffdcdc602458d6c9905129c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is renamed

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:316:69 · **recurring** · fingerprint: b2681466028c0f48c36959c5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based

- **passive-voice** · .agent/skills/the-worker/references/archive-records-and-image-prompts.md:320:84 · **recurring** · fingerprint: ec91177483cac13de5f77a8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is authorized


### .agent/skills/drawing/references/image-editing-protocol.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 1
- **Baseline:** 4
- **Words:** 474
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **semicolon** · .agent/skills/drawing/references/image-editing-protocol.md:9:82 · **recurring** · fingerprint: 4d3cb40fdfeb08c154a785f9
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/drawing/references/image-editing-protocol.md:33:34 · **recurring** · fingerprint: a58c92304a5ac7957912b9b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is confirmed


### .agent/skills/agent-skill-authoring/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 15
- **Hard findings:** 0
- **Baseline:** 6
- **Words:** 2260
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:14:79 · **recurring** · fingerprint: 02b57d3b2df16eb3468595dc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:159:29 · **recurring** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:166:23 · **recurring** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:172:149 · **recurring** · fingerprint: ba8e0ed371140388669d2100
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been loaded

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:172:153 · **recurring** · fingerprint: 1b62b1b2e8581f74a08af948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:185:36 · **recurring** · fingerprint: 97f02ce3bcf5b6ef7653d521
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:223:38 · **recurring** · fingerprint: 6791e38cdf43e2f4c45df46b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:245:28 · **recurring** · fingerprint: eb4ac5866a5a9ae0a950a472
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused

- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:246:65 · **recurring** · fingerprint: 301135338f19f01e083e45ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:246:70 · **recurring** · fingerprint: e6c88a755850e4cbcab58fa8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:253:17 · **recurring** · fingerprint: bbeb4b1299f984862be3ce2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected

- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:255:37 · **recurring** · fingerprint: 6d4fd87d7c04e6106995412e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been made

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:255:41 · **recurring** · fingerprint: 5b69fb1b48037b85a2f02a19
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been made

- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:257:32 · **recurring** · fingerprint: 19df0784fbab3f590bc978f2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:257:36 · **recurring** · fingerprint: 9124dbf071fc471856835398
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read


### .agent/skills/philosophy-religion-asceticism/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 471
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/README.md:17:11 · **recurring** · fingerprint: 1583b8690f42ec1e396bc38a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are enabled


### .takeout/images/README-1.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 314
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · .takeout/images/README-1.md:17:543 · **recurring** · fingerprint: d62fd2f70644184cc4c5011d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted


### .agent/skills/theme-factory/themes/golden-hour.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 71
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/the-worker/references/conversation-mode.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 19
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 3185
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:68:60 · **recurring** · fingerprint: d6fb83cbafb61644c729d606
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:68:162 · **recurring** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:84:157 · **recurring** · fingerprint: 50194bcb1c09593a6b8df74f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:96:72 · **recurring** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:101:41 · **recurring** · fingerprint: 01c59b00a54bee35fe1936cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:129:88 · **recurring** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:78 · **recurring** · fingerprint: 13168d32e5aeb357a6f05047
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:108 · **recurring** · fingerprint: 2d62a35466a8134401aac697
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:61 · **recurring** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:272 · **recurring** · fingerprint: a49119a4bb942d7711bad4ec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:146:63 · **recurring** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:151:36 · **recurring** · fingerprint: 3ca196dd83b56964e6c9c511
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:153:106 · **recurring** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:162:180 · **recurring** · fingerprint: 8b93e6445dd13d5345069497
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:260 · **recurring** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:205:94 · **recurring** · fingerprint: b8c8647d519418bedc546521
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:232:126 · **recurring** · fingerprint: f70f53510f186a20aefa39a5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:232:130 · **recurring** · fingerprint: 9c5f95ce73981d93b428a229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:253:75 · **recurring** · fingerprint: d3280be9a8e338d6afc3f804
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed


### .agent/skills/internal-comms/examples/company-newsletter.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 554
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · .agent/skills/internal-comms/examples/company-newsletter.md:2:9 · **recurring** · fingerprint: d119f69401fb0d7940bb4b07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **long-sentence** · .agent/skills/internal-comms/examples/company-newsletter.md:5:3 · **recurring** · fingerprint: e62dcc8049fb6bc6e436685c
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **present-perfect** · .agent/skills/internal-comms/examples/company-newsletter.md:5:245 · **recurring** · fingerprint: 848d2cddd8fb8ca620a9897a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have happened

- **passive-voice** · .agent/skills/internal-comms/examples/company-newsletter.md:21:418 · **recurring** · fingerprint: 0e81d23f4e8c8bea0003125d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are highlighted


### .agent/skills/skill-creator/agents/comparator.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 735
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:9:15 · **recurring** · fingerprint: 25f76deeafca430fb8355765
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based

- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:17:50 · **recurring** · fingerprint: dc78ab72e0948a2fb497356c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was executed

- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:48:38 · **recurring** · fingerprint: bc935daa91ef2a6b57226d04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is organized

- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:70:17 · **recurring** · fingerprint: f1d96c0b5d4b34b9c1ea0024
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are provided

- **passive-voice** · .agent/skills/skill-creator/agents/comparator.md:172:20 · **recurring** · fingerprint: 8499b8cbe16dca6dbedd1c00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were provided

- **semicolon** · .agent/skills/skill-creator/agents/comparator.md:200:67 · **recurring** · fingerprint: 5338d6f6a882c8070470752c
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 246
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:32:21 · **recurring** · fingerprint: 6d69ad27d49d36813c14b275
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Repair


### .agent/skills/theme-factory/themes/desert-rose.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 68
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/analysis/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 278
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/asd-ste100/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1573
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · .agent/skills/asd-ste100/README.md:26:35 · **recurring** · fingerprint: f592f42318251b648dd03dcb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · .agent/skills/asd-ste100/README.md:40:109 · **recurring** · fingerprint: 04c8a0d348a66e7c3e456046
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved


### workspace/ANALYSIS_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 384
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/ANALYSIS_TEMPLATE.md:53:50 · **recurring** · fingerprint: 6065ee744d87e9ee28f540f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified


### .agent/skills/the-worker/references/image-processing-scripts.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 340
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/document-standards/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1044
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/document-standards/SKILL.md:22:21 · **recurring** · fingerprint: 59f9b3021fb92ba38c2f3aa0
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

- **passive-voice** · .agent/skills/document-standards/SKILL.md:39:46 · **recurring** · fingerprint: 6f736d87b623b41483378e01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **semicolon** · .agent/skills/document-standards/SKILL.md:39:137 · **recurring** · fingerprint: 908066259786706e521f34bf
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/document-standards/SKILL.md:107:229 · **recurring** · fingerprint: 49c041bef5326bd7d5361137
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed


### .agent/skills/migrate-to-rust/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 21
- **Hard findings:** 15
- **Baseline:** 0
- **Words:** 1173
- **Findings per 100 words:** 1.8

#### Complete diagnostics

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:7:3 · **recurring** · fingerprint: 2051275b3344d8d1e90bb20c
  - **Level:** advisory-free
  - **Message:** Sentence has 55 words (cap 25). Split it.
  - **Matched text:** 55 words

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:12:57 · **recurring** · fingerprint: 0732cf54040416dcdb048e67
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:31:5 · **recurring** · fingerprint: ab1cd670db5255dba49ba1b0
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:36:5 · **recurring** · fingerprint: cc232b6cfb14b97181d99159
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is granted

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:37:5 · **recurring** · fingerprint: d3858f29af32d8e94293d0b0
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:42:5 · **recurring** · fingerprint: 25e51d985e9ed0edb6b1ce6c
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **synonym-rotation** · .agent/skills/migrate-to-rust/SKILL.md:43:26 · **recurring** · fingerprint: 4793da617ba3f4720177981a
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:46:45 · **recurring** · fingerprint: be06c683fb6cc7f7e8897691
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:47:22 · **recurring** · fingerprint: 85dac0b16ea5ca9c2b0033ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exhausted

- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:56:40 · **recurring** · fingerprint: 04d4c46e1b90de89a9b92bd8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:60:20 · **recurring** · fingerprint: f762c34776138fd607c76ea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are measured

- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:62:73 · **recurring** · fingerprint: 5b08b51f4a7b5fb8f192e23e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:102:58 · **recurring** · fingerprint: 51d97ec877597fa8ccf4f775
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:107:5 · **recurring** · fingerprint: 08a1774af47912b4ea612719
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **synonym-rotation** · .agent/skills/migrate-to-rust/SKILL.md:107:7 · **recurring** · fingerprint: a15b0b4bbc30e4751af5dbf6
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:110:19 · **recurring** · fingerprint: be06c683fb6cc7f7e8897691
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:119:1 · **recurring** · fingerprint: ca900c973726b0f821b797cc
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:155:5 · **recurring** · fingerprint: 8f605ea680fa9caf195b3943
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · .agent/skills/migrate-to-rust/SKILL.md:159:24 · **recurring** · fingerprint: dcb436816632865387b30390
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reached

- **synonym-rotation** · .agent/skills/migrate-to-rust/SKILL.md:169:68 · **recurring** · fingerprint: 0f9a40808850989ecafd2544
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **long-sentence** · .agent/skills/migrate-to-rust/SKILL.md:176:5 · **recurring** · fingerprint: ca900c973726b0f821b797cc
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words


### .agent/skills/theme-factory/themes/forest-canopy.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 68
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/skill-creator/references/schemas.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 518
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/skill-creator/references/schemas.md:76:35 · **recurring** · fingerprint: 17f5d80e88f7a58d4d55d5cc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being improved

- **passive-voice** · .agent/skills/skill-creator/references/schemas.md:79:46 · **recurring** · fingerprint: 7d978a01acd6c2742f13d662
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was derived

- **passive-voice** · .agent/skills/skill-creator/references/schemas.md:291:37 · **recurring** · fingerprint: 854bbcd9398ee87735892c01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run


### workspace/draft/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 664
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **semicolon** · workspace/draft/README.md:7:96 · **recurring** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/README.md:19:4 · **recurring** · fingerprint: fa0ad26c0f4696b24c6e471f
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **semicolon** · workspace/draft/README.md:21:305 · **recurring** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/README.md:23:136 · **recurring** · fingerprint: 23958065d6cbd83c298c65e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been assessed


### workspace/TASK_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 5
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 461
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **passive-voice** · workspace/TASK_TEMPLATE.md:20:108 · **recurring** · fingerprint: 5275280719ed16d2a5b7ad67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is written

- **passive-voice** · workspace/TASK_TEMPLATE.md:48:21 · **recurring** · fingerprint: fdc561df7864672b424ed481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was inspected

- **passive-voice** · workspace/TASK_TEMPLATE.md:75:20 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **passive-voice** · workspace/TASK_TEMPLATE.md:76:23 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **passive-voice** · workspace/TASK_TEMPLATE.md:86:150 · **recurring** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted


### .agent/skills/pdf/FORMS.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 13
- **Hard findings:** 8
- **Baseline:** 0
- **Words:** 1195
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **long-sentence** · .agent/skills/pdf/FORMS.md:53:3 · **recurring** · fingerprint: aa35eeeb7b54e03661f78104
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words

- **long-sentence** · .agent/skills/pdf/FORMS.md:74:3 · **recurring** · fingerprint: 12ef9957ae8fa3f2d1431f0a
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **synonym-rotation** · .agent/skills/pdf/FORMS.md:76:18 · **recurring** · fingerprint: 4d00c94cbb2ee5a3549d25f5
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **semicolon** · .agent/skills/pdf/FORMS.md:76:76 · **recurring** · fingerprint: eadb2528a436236ee54581d7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/pdf/FORMS.md:92:179 · **recurring** · fingerprint: 02b908f6e44af3aef97442d9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned

- **passive-voice** · .agent/skills/pdf/FORMS.md:114:51 · **recurring** · fingerprint: 89502e06609861db50e55419
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected

- **long-sentence** · .agent/skills/pdf/FORMS.md:118:1 · **recurring** · fingerprint: 6003a455c1f4c264a40e7c06
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · .agent/skills/pdf/FORMS.md:163:10 · **recurring** · fingerprint: 3d6807b222eb69b5b87dc658
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

- **synonym-rotation** · .agent/skills/pdf/FORMS.md:168:99 · **recurring** · fingerprint: 8f0ad7582380f0363e5c59c6
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix

- **passive-voice** · .agent/skills/pdf/FORMS.md:174:23 · **recurring** · fingerprint: 02b908f6e44af3aef97442d9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned

- **synonym-rotation** · .agent/skills/pdf/FORMS.md:210:50 · **recurring** · fingerprint: 5958fa7a24c9e3a09bf92349
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins

- **passive-voice** · .agent/skills/pdf/FORMS.md:260:39 · **recurring** · fingerprint: 4b9cfede2f3072d88c040579
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were detected

- **passive-voice** · .agent/skills/pdf/FORMS.md:291:9 · **recurring** · fingerprint: c1bdeae5f6d49be66f3dc77f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is mispositioned


### .agent/skills/theme-factory/themes/arctic-frost.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 73
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/pdf/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 347
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **long-sentence** · .agent/skills/pdf/SKILL.md:3:84 · **recurring** · fingerprint: 7c271799320bb3fa32a3db32
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words


### .agent/skills/drawing/references/prompt-fidelity.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 45
- **Hard findings:** 0
- **Baseline:** 15
- **Words:** 3676
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:13:215 · **recurring** · fingerprint: 3d9cd8606c71744cd549b794
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is measured

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:15:69 · **recurring** · fingerprint: d5f82029b13df7171b934277
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:46:115 · **recurring** · fingerprint: 8cc9271efa91b21a28df106f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is phrased

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:56:24 · **recurring** · fingerprint: 811cd72c913b73297c41df31
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:62:24 · **recurring** · fingerprint: dc36d4218894c718c5cae3a8
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:74:32 · **recurring** · fingerprint: a0d9fae2ecfc97b1d4a4f353
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are prohibited

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:80:35 · **recurring** · fingerprint: bc92abe865806f83163486f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being limited

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:89:141 · **recurring** · fingerprint: fbf25669bed6707f20b54638
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been established

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:91:171 · **recurring** · fingerprint: 106e56d434926ee31ff1490e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:116:33 · **recurring** · fingerprint: 3bce599aec03b94f1f1acdf1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has specified

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:119:41 · **recurring** · fingerprint: 49a02aeb8c516b96480c0200
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is depicted

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:127:120 · **recurring** · fingerprint: af1fe0da78db75f1afca7e12
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unspecified

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:127:168 · **recurring** · fingerprint: 5fae82b579f91a91fce6afd1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:151:163 · **recurring** · fingerprint: 5fae82b579f91a91fce6afd1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:198:141 · **recurring** · fingerprint: 42bc7f65a0321b20b4ebe6eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:225:75 · **recurring** · fingerprint: dc36d4218894c718c5cae3a8
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:244:41 · **recurring** · fingerprint: cc38a206710d5124e674cb13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:245:103 · **recurring** · fingerprint: 88970a2b0d7687b4903bc248
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:246:33 · **recurring** · fingerprint: 0a1ccaa9e582c0e89cd78104
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been paraphrased

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:247:123 · **recurring** · fingerprint: e8b85db64c57be8defba2b0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:248:42 · **recurring** · fingerprint: 7d0ffc2028c0b5c0e00573ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been preserved

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:249:26 · **recurring** · fingerprint: d70b4cf5c12886fee4bae585
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been limited

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:250:23 · **recurring** · fingerprint: 07efb79fa4e7a754a4df6331
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been converted

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:265:66 · **recurring** · fingerprint: 1f850b5c9410689c68878d1b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being submitted

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:268:30 · **recurring** · fingerprint: 8c4e6e357e0de615dd8ee971
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been archived

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:268:34 · **recurring** · fingerprint: 0aacc915f68736f69d97bcd7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been archived

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:270:46 · **recurring** · fingerprint: bbc2b8452f1e9c60a3400849
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exposed

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:272:98 · **recurring** · fingerprint: 5ef443839fa3154ef240274c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was submitted

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:272:197 · **recurring** · fingerprint: cde682dbdf090ea0d1abbaf2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was authorized

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:289:87 · **recurring** · fingerprint: 5fae82b579f91a91fce6afd1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:300:57 · **recurring** · fingerprint: 4016f59fa6583b3fe4ac2a03
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been checked

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:300:62 · **recurring** · fingerprint: cc4bbc272970240397e9337b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been checked

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:301:99 · **recurring** · fingerprint: 8e9eceec4ee17012c246262d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:302:41 · **recurring** · fingerprint: 20b7a70989c653847d75e449
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:302:46 · **recurring** · fingerprint: e8b85db64c57be8defba2b0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:303:106 · **recurring** · fingerprint: 6aae20a911c952490fc2b8fd
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been added

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:303:111 · **recurring** · fingerprint: 88970a2b0d7687b4903bc248
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:304:31 · **recurring** · fingerprint: 98c704fe9c1c3900a44e37e0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been restored

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:304:35 · **recurring** · fingerprint: cc38a206710d5124e674cb13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:306:58 · **recurring** · fingerprint: c35b7f77d08cfe4ad18f5647
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been audited

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:306:62 · **recurring** · fingerprint: cfb684542126ef90917c1893
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been audited

- **present-perfect** · .agent/skills/drawing/references/prompt-fidelity.md:307:27 · **recurring** · fingerprint: d44b601f4e06693644fb00e7
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been removed

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:307:31 · **recurring** · fingerprint: 103b143264e3231c2f628df4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been removed

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:309:42 · **recurring** · fingerprint: e690cece4fd6dbd89977d838
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is assigned

- **passive-voice** · .agent/skills/drawing/references/prompt-fidelity.md:309:73 · **recurring** · fingerprint: 4b1c8a395c52a0749f8ce4a1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was copied


### .agent/skills/theme-factory/themes/botanical-garden.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 69
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/references/research-method.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 559
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/philosophy-religion-asceticism/CHANGELOG.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 56
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/drawing/references/patterns/failure-patterns.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 25
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 2146
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:3:126 · **recurring** · fingerprint: 0656ffda7585e034eaeb0422
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:5:65 · **recurring** · fingerprint: 05ca10f52e76fee19176307e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are kept

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:19:163 · **recurring** · fingerprint: 22988deb64559045c494003e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reversed

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:22:89 · **recurring** · fingerprint: af251391824b3261c959e38f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:37:14 · **recurring** · fingerprint: 11ea98a026244f24cb19aa65
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is concentrated

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:48:20 · **recurring** · fingerprint: 3b45a129d4c0838326049ff7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were described

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:51:37 · **recurring** · fingerprint: 633eb4103528f878e2b3a9e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:61:197 · **recurring** · fingerprint: cc2fb2a172ba0f953ae0dfb4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:61:226 · **recurring** · fingerprint: 6de85062a6003e7358ec5c63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:85:19 · **recurring** · fingerprint: 183cb5a94112bdc23b770e5e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:91:264 · **recurring** · fingerprint: 29405619a2c91e6718f44773
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:120:233 · **recurring** · fingerprint: ec024dbf98259c151baea3a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was identified

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:136:66 · **recurring** · fingerprint: e7d0389b66176dff655137ba
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:154:172 · **recurring** · fingerprint: 0fca0464d15d439571aa29f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:165:92 · **recurring** · fingerprint: e0c2a92699e4acd4b0538ccc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:168:20 · **recurring** · fingerprint: 29405619a2c91e6718f44773
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:183:164 · **recurring** · fingerprint: 183cb5a94112bdc23b770e5e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **present-perfect** · .agent/skills/drawing/references/patterns/failure-patterns.md:194:52 · **recurring** · fingerprint: 8742abb9a4f8d39f2ac9b892
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has corrected

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:209:235 · **recurring** · fingerprint: 059552d8427fa19158b19e99
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was removed

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:209:273 · **recurring** · fingerprint: c0db69a5c995509e4eb77cff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was preserved

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:210:249 · **recurring** · fingerprint: 5332f45bf55aaf0434b21be1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was adopted

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:214:32 · **recurring** · fingerprint: 966afd25d1a5cb24ede20924
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained

- **present-perfect** · .agent/skills/drawing/references/patterns/failure-patterns.md:218:179 · **recurring** · fingerprint: c16ece4a46c94b44b00a5fe8
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:224:30 · **recurring** · fingerprint: 42baa51e06c4f52b0c0c18b5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included

- **passive-voice** · .agent/skills/drawing/references/patterns/failure-patterns.md:250:20 · **recurring** · fingerprint: 966afd25d1a5cb24ede20924
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained


### workspace/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 883
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/drawing/assets/daily-index-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 210
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/theme-factory/themes/tech-innovation.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 73
- **Findings per 100 words:** 1.4

#### Complete diagnostics

- **marketing-adjective** · .agent/skills/theme-factory/themes/tech-innovation.md:3:63 · **recurring** · fingerprint: f11de535868101ba92b23305
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge


### .agent/skills/the-worker/references/drawing-session-closeout.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 612
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/references/drawing-session-closeout.md:17:227 · **recurring** · fingerprint: 65adcc690f1e819c5e11e9d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed


### .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 235
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **passive-voice** · .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md:29:14 · **recurring** · fingerprint: d20eaeb4d39ab36d89018d79
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested


### .agent/skills/drawing/assets/pattern-entry-templates.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 9
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 562
- **Findings per 100 words:** 1.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:20:40 · **recurring** · fingerprint: ab9436f2b5ed3e06585afd03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired

- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:21:125 · **recurring** · fingerprint: a70edfc93adc8937d630930d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified

- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:25:67 · **recurring** · fingerprint: 7f22912dfdbb21318247d4b3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **present-perfect** · .agent/skills/drawing/assets/pattern-entry-templates.md:107:246 · **recurring** · fingerprint: 8fab2ea58ed063963328af68
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested

- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:116:51 · **recurring** · fingerprint: ac66d4a7e8457dcc712ea9d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:117:16 · **recurring** · fingerprint: 524acb2777c80b2c40f2312b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was assigned

- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:121:20 · **recurring** · fingerprint: 9f497620b35e45191797af3b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are separated

- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:123:15 · **recurring** · fingerprint: 66a6cf2a8d964826d67af7b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are described

- **passive-voice** · .agent/skills/drawing/assets/pattern-entry-templates.md:125:19 · **recurring** · fingerprint: ac66d4a7e8457dcc712ea9d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded


### .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 13
- **Hard findings:** 10
- **Baseline:** 0
- **Words:** 1274
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:3:1 · **recurring** · fingerprint: b2b4aaa5b80db580f641bc21
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:49:49 · **recurring** · fingerprint: 5efbda4d1f757c605b1da5a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is isolated

- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:72:5 · **recurring** · fingerprint: cbf47abcc8791070f58ba425
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:86:5 · **recurring** · fingerprint: e81e6adfd11cb872fd2c800e
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:96:26 · **recurring** · fingerprint: ec08c47bfb79374766082383
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **synonym-rotation** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:97:34 · **recurring** · fingerprint: 146d695ea92d0b8d4fa5a564
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **synonym-rotation** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:98:5 · **recurring** · fingerprint: 242d6a5058ac23a1dd770c30
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **long-sentence** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:112:9 · **recurring** · fingerprint: ec08c47bfb79374766082383
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **semicolon** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:102 · **recurring** · fingerprint: 48ceae5f0f72eac5e3b2c143
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:129 · **recurring** · fingerprint: 48ceae5f0f72eac5e3b2c143
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:147:28 · **recurring** · fingerprint: 976f180d206c7bf876f46fd7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grounded

- **synonym-rotation** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:170:7 · **recurring** · fingerprint: 130f0ce7248726f1d9dbb390
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirming

- **passive-voice** · .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:220:22 · **recurring** · fingerprint: b6e95df7029eb4462c9ecbcc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is enforced


### .agent/skills/asd-ste100/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 20
- **Hard findings:** 12
- **Baseline:** 31
- **Words:** 2609
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:21:69 · **recurring** · fingerprint: 170e10c67c5ddb4ac54ea4b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was violated

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:49:227 · **recurring** · fingerprint: cb0ac7a2c5dda8b0dbd1051d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are defined

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:57:60 · **recurring** · fingerprint: 8a011f6518e4f647accaa107
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:58:99 · **recurring** · fingerprint: 70281f9b33028652f7a1daae
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** Spin up

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:73:118 · **recurring** · fingerprint: 28ef39a3cb8b2ca848f4ec97
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved

- **nominalization** · .agent/skills/asd-ste100/SKILL.md:74:53 · **recurring** · fingerprint: 7e86fc5d602e4865ed4a0ff6
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis

- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:79:203 · **recurring** · fingerprint: 7a15da17f8212acf9cbcd80a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received

- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:81:140 · **recurring** · fingerprint: 320768d857c6a3e84654f3f5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed

- **nominalization** · .agent/skills/asd-ste100/SKILL.md:89:56 · **recurring** · fingerprint: fa833ca0d8a25be575faf6e0
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:79 · **recurring** · fingerprint: 12a9fb2640f958cc7e75f621
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:89 · **recurring** · fingerprint: c50be8a609eda6ecc738029b
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:107 · **recurring** · fingerprint: d7e2c69987f9328ac247ac53
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:121 · **recurring** · fingerprint: 0d5ed7f9257c40733f5c321d
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:133 · **recurring** · fingerprint: 2673e9a5ae5dd03778f880c9
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:29 · **recurring** · fingerprint: d272642fbbf9daaca0e0f89b
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** spin up

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:38 · **recurring** · fingerprint: 0069ef4a67380240203a7d96
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** reach out

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:49 · **recurring** · fingerprint: a00e46d5c1d01ed73aeb5e48
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** dive into

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:60 · **recurring** · fingerprint: 186eeebc10bfa90b61b9f168
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** kick off

- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:113:134 · **recurring** · fingerprint: 361fe239198e1c7837a878ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:146:58 · **recurring** · fingerprint: 9efba8ed23b805f9a79bdc62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized


### .agent/skills/asd-ste100/assets/lint-report-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 385
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/DRAFT_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 1242
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · workspace/DRAFT_TEMPLATE.md:25:119 · **recurring** · fingerprint: f64bf1ef9acc14ca64a7b985
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **passive-voice** · workspace/DRAFT_TEMPLATE.md:51:26 · **recurring** · fingerprint: 211b66e79e230bc550635a4f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were identified

- **semicolon** · workspace/DRAFT_TEMPLATE.md:53:58 · **recurring** · fingerprint: 3b682280b9ab9bb9d337e5a7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/DRAFT_TEMPLATE.md:63:103 · **recurring** · fingerprint: 3b682280b9ab9bb9d337e5a7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/DRAFT_TEMPLATE.md:78:47 · **recurring** · fingerprint: 3027ddebf5aa8173af033457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **passive-voice** · workspace/DRAFT_TEMPLATE.md:91:47 · **recurring** · fingerprint: 3027ddebf5aa8173af033457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **long-sentence** · workspace/DRAFT_TEMPLATE.md:111:75 · **recurring** · fingerprint: 1068d0f64079905a096f3f87
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/DRAFT_TEMPLATE.md:124:55 · **recurring** · fingerprint: fe3d0313172da8b3bd40c574
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified

- **synonym-rotation** · workspace/DRAFT_TEMPLATE.md:166:28 · **recurring** · fingerprint: fcd884bb6124b09c0acad1a2
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete


### .agent/skills/discernment-nudge/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 26
- **Hard findings:** 24
- **Baseline:** 0
- **Words:** 1701
- **Findings per 100 words:** 1.5

#### Complete diagnostics

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:4:3 · **recurring** · fingerprint: dd75187d1582eb7d2b491ad4
  - **Level:** advisory-free
  - **Message:** Sentence has 88 words (cap 25). Split it.
  - **Matched text:** 88 words

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:12:59 · **recurring** · fingerprint: 122ed7fb2cb96e1ca4b4eb09
  - **Level:** advisory-free
  - **Message:** Sentence has 64 words (cap 25). Split it.
  - **Matched text:** 64 words

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:27:42 · **recurring** · fingerprint: d7e37d0e4b2dd92bcc8046ca
  - **Level:** advisory-free
  - **Message:** Sentence has 46 words (cap 25). Split it.
  - **Matched text:** 46 words

- **synonym-rotation** · .agent/skills/discernment-nudge/SKILL.md:38:9 · **recurring** · fingerprint: 166248501fb9f2ce64dbbda2
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verifying

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:52:3 · **recurring** · fingerprint: 8e8b4d5dcd6b9b3a95ebd340
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:55:3 · **recurring** · fingerprint: 791a6d81408bdac17b771d91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:58:42 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:59:39 · **recurring** · fingerprint: 791a6d81408bdac17b771d91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:66:3 · **recurring** · fingerprint: b056eeb37b6762f4cace445e
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:75:47 · **recurring** · fingerprint: 03e560e6a34affc3f3b3ce36
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:76:8 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:81:15 · **recurring** · fingerprint: 72a58961141ef493db231920
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **passive-voice** · .agent/skills/discernment-nudge/SKILL.md:83:24 · **recurring** · fingerprint: 7666a76a64fdc00c8e9909af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been invited

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:84:34 · **recurring** · fingerprint: 791a6d81408bdac17b771d91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:89:51 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:101:54 · **recurring** · fingerprint: 16b708bb219c5c5ddf4b8d4f
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words

- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:106:27 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:117:35 · **recurring** · fingerprint: b056eeb37b6762f4cace445e
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:121:65 · **recurring** · fingerprint: 72a58961141ef493db231920
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:130:36 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:136:16 · **recurring** · fingerprint: 79f0398563d7f9f20fe6c295
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:141:39 · **recurring** · fingerprint: 03e560e6a34affc3f3b3ce36
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · .agent/skills/discernment-nudge/SKILL.md:156:9 · **recurring** · fingerprint: c16c15ec163e1f3c17879996
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are weighed

- **long-sentence** · .agent/skills/discernment-nudge/SKILL.md:167:1 · **recurring** · fingerprint: 4f3ace9d5db454f882ac45fe
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:171:34 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/discernment-nudge/SKILL.md:205:17 · **recurring** · fingerprint: 4a420c825c6d96305cf9ad30
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 75
- **Hard findings:** 53
- **Baseline:** 0
- **Words:** 8961
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:25:10 · **recurring** · fingerprint: a2ab275c6b77dd5fee04cc69
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:25:236 · **recurring** · fingerprint: f361f0da8e025b2ad8e4e144
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:27:293 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:43:292 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:43:342 · **recurring** · fingerprint: a909a403a059d36f26caf607
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are unchanged

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:45:452 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:118:13 · **recurring** · fingerprint: 2622327c5814c036cce375d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are assessed

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:127:277 · **recurring** · fingerprint: 5fbc17194b22ffad4280c0ef
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supported

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:131:1 · **recurring** · fingerprint: fef6e60a628c50ea5557879f
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:135:123 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:141:432 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:149:130 · **recurring** · fingerprint: 5acc357959587a68b0f951b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:151:133 · **recurring** · fingerprint: ff6c3acd0c014dc4e61c466a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:154:130 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:3 · **recurring** · fingerprint: f7dc64f1259416e941602253
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:153 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:195 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:216 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:172:17 · **recurring** · fingerprint: 6e0df3ac815fc5850205b430
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has evolved

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:177:5 · **recurring** · fingerprint: 88aeab811894156e381b6f38
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:181:259 · **recurring** · fingerprint: 5c822b17641bfca685187467
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validate

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:45 · **recurring** · fingerprint: e8137e2bbd27eeeebe09cefe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are gitignored

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:72 · **recurring** · fingerprint: f82bfd9e6673b647a6d8fc2d
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:278 · **recurring** · fingerprint: 2879617005bdf3d23fcdebce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:186:131 · **recurring** · fingerprint: 88aeab811894156e381b6f38
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:186:552 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:187:3 · **recurring** · fingerprint: 0f7475f061de95d077b1bfe9
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:195:90 · **recurring** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:206:112 · **recurring** · fingerprint: d322aeaf54a910f1b652245b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is missed

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:207:165 · **recurring** · fingerprint: f0d61be6ac280ec407b4f93b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reconciled

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:209:5 · **recurring** · fingerprint: fef6e60a628c50ea5557879f
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:211:311 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:211:342 · **recurring** · fingerprint: 77adbdbc0fe812d1b67b5e05
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are intended

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:223:85 · **recurring** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:231:5 · **recurring** · fingerprint: f82bfd9e6673b647a6d8fc2d
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:232:3 · **recurring** · fingerprint: 3dd65725c765cdc8c75ee04a
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:241:81 · **recurring** · fingerprint: a7bf89e39efdb719560ebf21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is redesigned

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:244:107 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:267:114 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:268:69 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:281:139 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:283:84 · **recurring** · fingerprint: ff6c3acd0c014dc4e61c466a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:320:246 · **recurring** · fingerprint: 89ce3d95585eee314fa93cfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:326:391 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:338:117 · **recurring** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:338:187 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:383:179 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:463:1 · **recurring** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:469:245 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:515:142 · **recurring** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:516:107 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:517:145 · **recurring** · fingerprint: e4c84bbce7e4e015e5f82803
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:528:134 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:528:168 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:530:11 · **recurring** · fingerprint: f0baecd36560346eb7c99c71
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:18 · **recurring** · fingerprint: e7603e373d761a7c9ff25aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:104 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:126 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:157 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:537:20 · **recurring** · fingerprint: e796b5d39f657c7dbfca408d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is treated

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:539:30 · **recurring** · fingerprint: 45700ec28d246ad5f6098f6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are treated

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:554:32 · **recurring** · fingerprint: 70781a8fa973c1554931c214
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:612:52 · **recurring** · fingerprint: 331ead622bd8b63c3dc8ec78
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:615:4 · **recurring** · fingerprint: 26959e3895827a98ea573e44
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:632:4 · **recurring** · fingerprint: cb5ac6fb2c2c270ac73b57e0
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:633:145 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:634:4 · **recurring** · fingerprint: c3aa5dc7d8225bd81a86e1b5
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:649:20 · **recurring** · fingerprint: 33dd6d895441c53e43bd10a2
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:20 · **recurring** · fingerprint: 0f7475f061de95d077b1bfe9
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:56 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:112 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:152 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:204 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:250 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:665:90 · **recurring** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/asd-ste100/references/repository-writing-policy.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 570
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/asd-ste100/references/repository-writing-policy.md:18:36 · **recurring** · fingerprint: fa71e22a78d6e4ce44e3a977
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known


### .agent/skills/theme-factory/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 473
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **present-perfect** · .agent/skills/theme-factory/SKILL.md:3:218 · **recurring** · fingerprint: f588ce6668825b2c639b420e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been

- **synonym-rotation** · .agent/skills/theme-factory/SKILL.md:23:33 · **recurring** · fingerprint: c4e3b3a464edfeee7fc7bcc3
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** Display

- **semicolon** · .agent/skills/theme-factory/SKILL.md:23:159 · **recurring** · fingerprint: b09339406bea0fa2e1afd49f
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · .agent/skills/theme-factory/SKILL.md:26:38 · **recurring** · fingerprint: 8ec8403e57aec198db5ad83e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been chosen

- **passive-voice** · .agent/skills/theme-factory/SKILL.md:45:12 · **recurring** · fingerprint: ec5648e4b37ff6b0ffe90c1f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is defined

- **passive-voice** · .agent/skills/theme-factory/SKILL.md:52:25 · **recurring** · fingerprint: c7a1a2c629a0f37d6575c485
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected


### .agent/skills/the-worker/assets/conversation-integrity-template.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 290
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/assets/conversation-integrity-template.md:41:315 · **recurring** · fingerprint: f4b4f08dfca80fb5e43ae4e6
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
