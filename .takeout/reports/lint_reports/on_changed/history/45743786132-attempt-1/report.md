# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#709](https://github.com/dungnv2602/chatgpt/actions/runs/45743786132)
- **Run ID / attempt:** 45743786132 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / c91c7dedd734c09c21ab765c169aadc83dc408e9
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** c259604f5c331c12fa98215f244df66a5dc3fc6c
- **Linter source SHA:** c91c7dedd734c09c21ab765c169aadc83dc408e9
- **Generated (UTC):** 2026-11-26T02:40:09.213897+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 78 |
| Files that failed | 78 |
| Files with findings | 0 |
| Total findings | 0 |
| Hard findings | 0 |
| Advisory findings | 0 |
| New findings | 0 |
| Recurring findings | 0 |
| Resolved findings | 54 |
| Failed workflow checks | 0 |

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
- .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md
- .agent/skills/drawing/references/patterns/README.md
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
- .agent/skills/asd-ste100/README.md
- .agent/skills/the-worker/references/image-processing-scripts.md
- .agent/skills/document-standards/SKILL.md
- .agent/skills/migrate-to-rust/SKILL.md
- .agent/skills/theme-factory/themes/forest-canopy.md
- .agent/skills/skill-creator/references/schemas.md
- .agent/skills/pdf/FORMS.md
- .agent/skills/theme-factory/themes/arctic-frost.md
- .agent/skills/pdf/SKILL.md
- .agent/skills/drawing/references/prompt-fidelity.md
- .agent/skills/theme-factory/themes/botanical-garden.md
- .agent/skills/philosophy-religion-asceticism/references/research-method.md
- .agent/skills/philosophy-religion-asceticism/CHANGELOG.md
- .agent/skills/drawing/references/patterns/failure-patterns.md
- .agent/skills/drawing/assets/daily-index-template.md
- .agent/skills/theme-factory/themes/tech-innovation.md
- .agent/skills/the-worker/references/drawing-session-closeout.md
- .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md
- .agent/skills/drawing/assets/pattern-entry-templates.md
- .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md
- .agent/skills/asd-ste100/SKILL.md
- .agent/skills/asd-ste100/assets/lint-report-template.md
- .agent/skills/discernment-nudge/SKILL.md
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
| .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/patterns/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
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
| .agent/skills/asd-ste100/README.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/references/image-processing-scripts.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/document-standards/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/migrate-to-rust/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/forest-canopy.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/skill-creator/references/schemas.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/pdf/FORMS.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/arctic-frost.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/pdf/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/prompt-fidelity.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/botanical-garden.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/references/research-method.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/CHANGELOG.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/patterns/failure-patterns.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/assets/daily-index-template.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/theme-factory/themes/tech-innovation.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/the-worker/references/drawing-session-closeout.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/philosophy-religion-asceticism/references/answer-patterns.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/assets/pattern-entry-templates.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/migrate-to-rust/references/pgo_and_telemetry_guide.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/asd-ste100/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/asd-ste100/assets/lint-report-template.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/discernment-nudge/SKILL.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
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
Ran 4 tests in 0.255s

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

- **Result:** Skipped
- **Exit code:** Unknown

~~~text
Not required for this incremental run.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

None.

### Resolved findings

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:36:10 · **resolved** · fingerprint: a737104c50ceb40f303a4a01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:332 · **resolved** · fingerprint: 63b66afb8b84b4750380eace
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:388 · **resolved** · fingerprint: e18acfaf818e2c30f6ca30e9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:158:1 · **resolved** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:169:21 · **resolved** · fingerprint: 34fd4b4fc86f7c4829f49935
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validated
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:179:143 · **resolved** · fingerprint: 8fab87c9578c4937b0124edf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:181:62 · **resolved** · fingerprint: 7c3c1ace5ec3d5c53c98a4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are observed
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:183:69 · **resolved** · fingerprint: 1614dc41c4b7be8e66e6f0d4
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:120 · **resolved** · fingerprint: 2e23d59621877db75c28ce78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:223 · **resolved** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:206:177 · **resolved** · fingerprint: ff8dedd324f39ede5ee75f82
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:208:43 · **resolved** · fingerprint: ae6b75fe50ddf475f002c2af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is fragmented
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:210:53 · **resolved** · fingerprint: e6a0a6a3cb10281e485f4ced
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been measured
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:235:53 · **resolved** · fingerprint: e0805effa50f8c2d06788a7e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:261:171 · **resolved** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:292:60 · **resolved** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:295:388 · **resolved** · fingerprint: 84a34fb70b809525fcff26b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been piloted
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:296:52 · **resolved** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:313:90 · **resolved** · fingerprint: cd8c27dadbc8cbf2ffa0ea4b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unsupported
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:325:178 · **resolved** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:346:218 · **resolved** · fingerprint: a27c714d52cff462c278171d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:458:36 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:482:251 · **resolved** · fingerprint: a484bb1a5b40074d480f3f91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is configured
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:502:30 · **resolved** · fingerprint: 0de287d1c4eae57b62d477b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:503:52 · **resolved** · fingerprint: cbf03a5bdfbefc8d301bac6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are resolved
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:504:22 · **resolved** · fingerprint: ba2af3047b1dbc7bfdba2dd0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are classified
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:541:4 · **resolved** · fingerprint: 93b3c8314ad783839cf934a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:585:23 · **resolved** · fingerprint: ebe3a0eaf57219e6e13da654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is treated
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:586:94 · **resolved** · fingerprint: b1897a649c20569be1ac0618
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:598:63 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:610:53 · **resolved** · fingerprint: 1e8f06c794753d0da4c374f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are supported
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:611:217 · **resolved** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:613:256 · **resolved** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:640:93 · **resolved** · fingerprint: 316a7cc78530dc52ed55aeb6
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:670:104 · **resolved** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:4 · **resolved** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:107 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:166 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:212 · **resolved** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:680:4 · **resolved** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:48 · **resolved** · fingerprint: 5c278ad2f255230faa055f76
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:90 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:122 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:700:45 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:707:246 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:708:194 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:155 · **resolved** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:240 · **resolved** · fingerprint: dd5a9425158b41b001c9b936
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:712:91 · **resolved** · fingerprint: c6bfceae059912f8aadd9e2e
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fixed
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:718:1 · **resolved** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **semicolon** · workspace/draft/README.md:7:96 · **resolved** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/README.md:19:4 · **resolved** · fingerprint: fa0ad26c0f4696b24c6e471f
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · workspace/draft/README.md:21:305 · **resolved** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/README.md:23:136 · **resolved** · fingerprint: 23958065d6cbd83c298c65e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been assessed

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
