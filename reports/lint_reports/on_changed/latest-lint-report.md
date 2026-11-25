# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#699](https://github.com/dungnv2602/chatgpt/actions/runs/45566151970)
- **Run ID / attempt:** 45566151970 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / c259604f5c331c12fa98215f244df66a5dc3fc6c
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 20e90a6b97317cb7c0c689dac9864baac3d64207
- **Linter source SHA:** c259604f5c331c12fa98215f244df66a5dc3fc6c
- **Generated (UTC):** 2026-11-25T07:13:06.911788+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 54 |
| Hard findings | 26 |
| Advisory findings | 28 |
| New findings | 54 |
| Recurring findings | 0 |
| Resolved findings | 242 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md
- workspace/task_board.md
- workspace/draft/README.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md | FAIL | 50 | 23 | 0 | 9822 | 0.5 | 1 |
| workspace/task_board.md | PASS | 0 | 0 | 0 | 2212 | 0.0 | 0 |
| workspace/draft/README.md | FAIL | 4 | 3 | 0 | 665 | 0.6 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 25 |
| semicolon | 12 |
| long-sentence | 9 |
| synonym-rotation | 5 |
| present-perfect | 3 |

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
Ran 4 tests in 0.293s

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

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:36:10 · **new** · fingerprint: a737104c50ceb40f303a4a01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:332 · **new** · fingerprint: 63b66afb8b84b4750380eace
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:388 · **new** · fingerprint: e18acfaf818e2c30f6ca30e9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:158:1 · **new** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:169:21 · **new** · fingerprint: 34fd4b4fc86f7c4829f49935
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validated
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:179:143 · **new** · fingerprint: 8fab87c9578c4937b0124edf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:181:62 · **new** · fingerprint: 7c3c1ace5ec3d5c53c98a4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are observed
- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:183:69 · **new** · fingerprint: 1614dc41c4b7be8e66e6f0d4
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:120 · **new** · fingerprint: 2e23d59621877db75c28ce78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:223 · **new** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:206:177 · **new** · fingerprint: ff8dedd324f39ede5ee75f82
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:208:43 · **new** · fingerprint: ae6b75fe50ddf475f002c2af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is fragmented
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:210:53 · **new** · fingerprint: e6a0a6a3cb10281e485f4ced
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been measured
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:235:53 · **new** · fingerprint: e0805effa50f8c2d06788a7e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:261:171 · **new** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:292:60 · **new** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:295:388 · **new** · fingerprint: 84a34fb70b809525fcff26b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been piloted
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:296:52 · **new** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:313:90 · **new** · fingerprint: cd8c27dadbc8cbf2ffa0ea4b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unsupported
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:325:178 · **new** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:346:218 · **new** · fingerprint: a27c714d52cff462c278171d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:458:36 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:482:251 · **new** · fingerprint: a484bb1a5b40074d480f3f91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is configured
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:502:30 · **new** · fingerprint: 0de287d1c4eae57b62d477b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:503:52 · **new** · fingerprint: cbf03a5bdfbefc8d301bac6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are resolved
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:504:22 · **new** · fingerprint: ba2af3047b1dbc7bfdba2dd0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are classified
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:541:4 · **new** · fingerprint: 93b3c8314ad783839cf934a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:585:23 · **new** · fingerprint: ebe3a0eaf57219e6e13da654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is treated
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:586:94 · **new** · fingerprint: b1897a649c20569be1ac0618
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:598:63 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:610:53 · **new** · fingerprint: 1e8f06c794753d0da4c374f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are supported
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:611:217 · **new** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:613:256 · **new** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:640:93 · **new** · fingerprint: 316a7cc78530dc52ed55aeb6
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:670:104 · **new** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:4 · **new** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:107 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:166 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:212 · **new** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:680:4 · **new** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:48 · **new** · fingerprint: 5c278ad2f255230faa055f76
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:90 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:122 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:700:45 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:707:246 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:708:194 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:155 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:240 · **new** · fingerprint: dd5a9425158b41b001c9b936
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:712:91 · **new** · fingerprint: c6bfceae059912f8aadd9e2e
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fixed
- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:718:1 · **new** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **semicolon** · workspace/draft/README.md:7:96 · **new** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/README.md:19:4 · **new** · fingerprint: fa0ad26c0f4696b24c6e471f
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · workspace/draft/README.md:21:305 · **new** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/README.md:23:136 · **new** · fingerprint: 23958065d6cbd83c298c65e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been assessed

### Recurring findings

None.

### Resolved findings

- **synonym-rotation** · skills/skill-creator/agents/grader.md:43:25 · **resolved** · fingerprint: f6b0cd4515b63f0d695cd984
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · skills/skill-creator/agents/grader.md:50:34 · **resolved** · fingerprint: eda68c8e5f0024bbf44478a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were filled
- **passive-voice** · skills/skill-creator/agents/grader.md:55:53 · **resolved** · fingerprint: 6d8513652396223c46db7c53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/skill-creator/agents/grader.md:204:30 · **resolved** · fingerprint: e47fae0d3214443b275d83bf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being verified
- **passive-voice** · skills/internal-comms/examples/company-newsletter.md:2:9 · **resolved** · fingerprint: 674f8c6b10c2692aba1d6872
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · skills/internal-comms/examples/company-newsletter.md:5:3 · **resolved** · fingerprint: 962ad33b16c74cce9136544c
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **present-perfect** · skills/internal-comms/examples/company-newsletter.md:5:245 · **resolved** · fingerprint: e21a631576722f4ba88c9a40
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have happened
- **passive-voice** · skills/internal-comms/examples/company-newsletter.md:21:418 · **resolved** · fingerprint: a5c77894421daf1d053502ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are highlighted
- **long-sentence** · skills/pdf/FORMS.md:53:3 · **resolved** · fingerprint: 633ed34d5a9f1f808fb3863d
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words
- **long-sentence** · skills/pdf/FORMS.md:74:3 · **resolved** · fingerprint: d1f4e4a17700e4fddf56e470
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **synonym-rotation** · skills/pdf/FORMS.md:76:18 · **resolved** · fingerprint: d0326226d8f30a067ce6965d
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **semicolon** · skills/pdf/FORMS.md:76:76 · **resolved** · fingerprint: d1786a470e3e35ea435e593b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/pdf/FORMS.md:92:179 · **resolved** · fingerprint: 3fe66375b59c3b0c8018b635
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned
- **passive-voice** · skills/pdf/FORMS.md:114:51 · **resolved** · fingerprint: bbe9290d6bdb305c9943d943
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected
- **long-sentence** · skills/pdf/FORMS.md:118:1 · **resolved** · fingerprint: 4df56657f6044a9e3d88ab1e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · skills/pdf/FORMS.md:163:10 · **resolved** · fingerprint: bc0b3a7638b2e3238d494397
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **synonym-rotation** · skills/pdf/FORMS.md:168:99 · **resolved** · fingerprint: 31453b7d73f9081ba7fc7aa1
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix
- **passive-voice** · skills/pdf/FORMS.md:174:23 · **resolved** · fingerprint: 3fe66375b59c3b0c8018b635
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned
- **synonym-rotation** · skills/pdf/FORMS.md:210:50 · **resolved** · fingerprint: d9abe8c3f4f7d6196dda74a6
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins
- **passive-voice** · skills/pdf/FORMS.md:260:39 · **resolved** · fingerprint: bcb3c4f45b7f95b1cf8ceddc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were detected
- **passive-voice** · skills/pdf/FORMS.md:291:9 · **resolved** · fingerprint: 1c58d1ff24fa595261572915
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is mispositioned
- **marketing-adjective** · skills/theme-factory/themes/tech-innovation.md:3:63 · **resolved** · fingerprint: 80634a765c13460d206a2ec7
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **passive-voice** · skills/internal-comms/examples/faq-answers.md:2:55 · **resolved** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · skills/internal-comms/examples/faq-answers.md:2:225 · **resolved** · fingerprint: 49cf594e46f6ead99fc2a24e
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · skills/internal-comms/examples/faq-answers.md:4:3 · **resolved** · fingerprint: 7982191c1f28db7fbe5c2969
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/internal-comms/examples/faq-answers.md:7:1 · **resolved** · fingerprint: 7982191c1f28db7fbe5c2969
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/internal-comms/examples/faq-answers.md:12:3 · **resolved** · fingerprint: 3a87e9c439a250becbc034ed
  - **Level:** advisory-free
  - **Message:** Sentence has 49 words (cap 25). Split it.
  - **Matched text:** 49 words
- **passive-voice** · skills/internal-comms/examples/faq-answers.md:12:20 · **resolved** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · skills/internal-comms/examples/faq-answers.md:12:130 · **resolved** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **present-perfect** · skills/theme-factory/SKILL.md:3:218 · **resolved** · fingerprint: 88d72e2d65542550249f0c15
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been
- **synonym-rotation** · skills/theme-factory/SKILL.md:23:33 · **resolved** · fingerprint: 90937deb6d9e203b4956d892
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** Display
- **semicolon** · skills/theme-factory/SKILL.md:23:159 · **resolved** · fingerprint: a9118ae923ba3eb2ca0eed95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/theme-factory/SKILL.md:26:38 · **resolved** · fingerprint: fc51630c87430edc3e5ee859
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been chosen
- **passive-voice** · skills/theme-factory/SKILL.md:45:12 · **resolved** · fingerprint: cc0e98e90677694b95ddacea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is defined
- **passive-voice** · skills/theme-factory/SKILL.md:52:25 · **resolved** · fingerprint: 9161559ebd704659b72aab24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected
- **long-sentence** · skills/grilling/SKILL.md:28:48 · **resolved** · fingerprint: 183863e52e0f6f06bf48dfcc
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · skills/grilling/SKILL.md:28:193 · **resolved** · fingerprint: ae6b7313f526901b623e262b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/grilling/SKILL.md:28:255 · **resolved** · fingerprint: 52a7f2689aea71be1612b603
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · skills/grilling/SKILL.md:28:397 · **resolved** · fingerprint: ae6b7313f526901b623e262b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/grilling/SKILL.md:30:13 · **resolved** · fingerprint: f0bdde4343f717a6d95280b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **present-perfect** · skills/grilling/SKILL.md:30:166 · **resolved** · fingerprint: 23f0857cbab27efe737d08c9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **passive-voice** · skills/internal-comms/examples/3p-updates.md:2:9 · **resolved** · fingerprint: 006084ecedd2b0f60f2a319e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · skills/internal-comms/examples/3p-updates.md:4:141 · **resolved** · fingerprint: 0592d6c63ea607b94a7d508d
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **present-perfect** · skills/internal-comms/examples/3p-updates.md:7:28 · **resolved** · fingerprint: 1991d3b341dea71d1160d82e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has accomplished
- **long-sentence** · skills/discernment-nudge/SKILL.md:4:3 · **resolved** · fingerprint: 0a714b41c7716d9a6f1cab5e
  - **Level:** advisory-free
  - **Message:** Sentence has 88 words (cap 25). Split it.
  - **Matched text:** 88 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:12:59 · **resolved** · fingerprint: 66a0d61a227ac0548adbfcf7
  - **Level:** advisory-free
  - **Message:** Sentence has 64 words (cap 25). Split it.
  - **Matched text:** 64 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:27:42 · **resolved** · fingerprint: 09532e58e58d4dfe8bdc79d6
  - **Level:** advisory-free
  - **Message:** Sentence has 46 words (cap 25). Split it.
  - **Matched text:** 46 words
- **synonym-rotation** · skills/discernment-nudge/SKILL.md:38:9 · **resolved** · fingerprint: 8148fcf71c05d754866b31ae
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verifying
- **long-sentence** · skills/discernment-nudge/SKILL.md:52:3 · **resolved** · fingerprint: 7edd5e29457880d740b445be
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:55:3 · **resolved** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · skills/discernment-nudge/SKILL.md:58:42 · **resolved** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:59:39 · **resolved** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:66:3 · **resolved** · fingerprint: 0d46bb8bc736d2592d84c9ee
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:75:47 · **resolved** · fingerprint: 2732bbda68c4918a25cee5d7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · skills/discernment-nudge/SKILL.md:76:8 · **resolved** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:81:15 · **resolved** · fingerprint: bc449f6a09bfcee41f17a7e1
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **passive-voice** · skills/discernment-nudge/SKILL.md:83:24 · **resolved** · fingerprint: ef2a5302c79e63f003738349
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been invited
- **long-sentence** · skills/discernment-nudge/SKILL.md:84:34 · **resolved** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · skills/discernment-nudge/SKILL.md:89:51 · **resolved** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:101:54 · **resolved** · fingerprint: d4a15d9b253d6b8336214e0f
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **semicolon** · skills/discernment-nudge/SKILL.md:106:27 · **resolved** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:117:35 · **resolved** · fingerprint: 0d46bb8bc736d2592d84c9ee
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:121:65 · **resolved** · fingerprint: bc449f6a09bfcee41f17a7e1
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **semicolon** · skills/discernment-nudge/SKILL.md:130:36 · **resolved** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:136:16 · **resolved** · fingerprint: fb1aa964536ca9c2e2071ce0
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:141:39 · **resolved** · fingerprint: 2732bbda68c4918a25cee5d7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · skills/discernment-nudge/SKILL.md:156:9 · **resolved** · fingerprint: 09860b573750eb72110a818f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are weighed
- **long-sentence** · skills/discernment-nudge/SKILL.md:167:1 · **resolved** · fingerprint: b8df8fc4deef715436cbed14
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **semicolon** · skills/discernment-nudge/SKILL.md:171:34 · **resolved** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/discernment-nudge/SKILL.md:205:17 · **resolved** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/internal-comms/SKILL.md:3:136 · **resolved** · fingerprint: 6fb7073d863c9fbc89ee070c
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · skills/skill-creator/agents/analyzer.md:45:17 · **resolved** · fingerprint: 963c77d99b7e75e0a3bf0b37
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were used
- **synonym-rotation** · skills/skill-creator/agents/analyzer.md:81:27 · **resolved** · fingerprint: 73a20e38cbfda82326a10620
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modify
- **present-perfect** · skills/skill-creator/agents/analyzer.md:161:61 · **resolved** · fingerprint: a070d81ff2293e36967921ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have changed
- **passive-voice** · skills/skill-creator/agents/analyzer.md:200:37 · **resolved** · fingerprint: 8a779742e2e23efbc4881142
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being benchmarked
- **long-sentence** · skills/pdf/SKILL.md:3:84 · **resolved** · fingerprint: 80f948c0d409822bd1502a79
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:51:3 · **resolved** · fingerprint: c9464aa336f93a9a8d49a570
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · skills/doc-coauthoring/SKILL.md:56:24 · **resolved** · fingerprint: f058f8435b29176017e90d21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are answered
- **passive-voice** · skills/doc-coauthoring/SKILL.md:59:36 · **resolved** · fingerprint: e10d64cbb238674d2f93ba0f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:65:53 · **resolved** · fingerprint: c09611be7b0f6df8558b3632
  - **Level:** advisory-free
  - **Message:** 'get' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** get
- **long-sentence** · skills/doc-coauthoring/SKILL.md:72:1 · **resolved** · fingerprint: 9319ee289b0fe44d84643a21
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **passive-voice** · skills/doc-coauthoring/SKILL.md:72:22 · **resolved** · fingerprint: aacb3f77deb9a088671cd4ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected
- **passive-voice** · skills/doc-coauthoring/SKILL.md:86:42 · **resolved** · fingerprint: cee3981022d4e3499944c77e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being learned
- **long-sentence** · skills/doc-coauthoring/SKILL.md:94:1 · **resolved** · fingerprint: 70b1172296ab0a28aeb9fe21
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **present-perfect** · skills/doc-coauthoring/SKILL.md:97:20 · **resolved** · fingerprint: 63238be79dd0f680047ad702
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been gathered
- **passive-voice** · skills/doc-coauthoring/SKILL.md:97:24 · **resolved** · fingerprint: f3183f25b8780ed21113c300
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been gathered
- **passive-voice** · skills/doc-coauthoring/SKILL.md:130:18 · **resolved** · fingerprint: 65720f031e47f176970ebc0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is agreed
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:150:1 · **resolved** · fingerprint: 6a6fbd0d92479d7d01d8ae93
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **present-perfect** · skills/doc-coauthoring/SKILL.md:150:22 · **resolved** · fingerprint: 8cdb21ea190546014c9be542
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been created
- **passive-voice** · skills/doc-coauthoring/SKILL.md:150:26 · **resolved** · fingerprint: 27597883b1f70487be501033
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:156:20 · **resolved** · fingerprint: 9cc2456ea1ec0364078faf6b
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **present-perfect** · skills/doc-coauthoring/SKILL.md:200:40 · **resolved** · fingerprint: 97ebea75b5ec66e6e650944b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been drafted
- **passive-voice** · skills/doc-coauthoring/SKILL.md:200:44 · **resolved** · fingerprint: 8c0e9f5d680b69e4b6921173
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been drafted
- **long-sentence** · skills/doc-coauthoring/SKILL.md:202:1 · **resolved** · fingerprint: 295b724e21d2dc85c8f7ce1f
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/doc-coauthoring/SKILL.md:211:3 · **resolved** · fingerprint: 37fccb416c5a2c73a2b08580
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · skills/doc-coauthoring/SKILL.md:213:35 · **resolved** · fingerprint: 3c0ab4824ebf0184fa850617
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied
- **passive-voice** · skills/doc-coauthoring/SKILL.md:219:14 · **resolved** · fingerprint: a369cd14e91a6c55c8078a9e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **passive-voice** · skills/doc-coauthoring/SKILL.md:233:21 · **resolved** · fingerprint: f849879f47683f3042f9aa04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted
- **passive-voice** · skills/doc-coauthoring/SKILL.md:234:23 · **resolved** · fingerprint: f849879f47683f3042f9aa04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:312:30 · **resolved** · fingerprint: 1ee1d09f44673180016e2f67
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct
- **present-perfect** · skills/doc-coauthoring/SKILL.md:336:18 · **resolved** · fingerprint: 19bc6ba8838ee66ff59dc7b6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has passed
- **passive-voice** · skills/doc-coauthoring/SKILL.md:342:50 · **resolved** · fingerprint: a369cd14e91a6c55c8078a9e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **passive-voice** · skills/doc-coauthoring/SKILL.md:346:84 · **resolved** · fingerprint: 5f77ec29406067038b3f0fbd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was developed
- **passive-voice** · skills/doc-coauthoring/SKILL.md:348:30 · **resolved** · fingerprint: 6de4f19737e8127fa123c9f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is received
- **long-sentence** · skills/skill-creator/SKILL.md:3:100 · **resolved** · fingerprint: cfd51398e7020a0fbdafe7ba
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **long-sentence** · skills/skill-creator/SKILL.md:16:5 · **resolved** · fingerprint: 67edb283ba2426229ffbdd5b
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **synonym-rotation** · skills/skill-creator/SKILL.md:16:182 · **resolved** · fingerprint: 6089f9e6b2cd3054930b07d3
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change
- **long-sentence** · skills/skill-creator/SKILL.md:18:3 · **resolved** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/skill-creator/SKILL.md:22:1 · **resolved** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/skill-creator/SKILL.md:22:213 · **resolved** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/skill-creator/SKILL.md:26:1 · **resolved** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/skill-creator/SKILL.md:28:1 · **resolved** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/skill-creator/SKILL.md:28:22 · **resolved** · fingerprint: 7638fc0a5fbb6cceca5a3ffd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **long-sentence** · skills/skill-creator/SKILL.md:34:105 · **resolved** · fingerprint: 90b7c0eac3e2ee5b205b348c
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **long-sentence** · skills/skill-creator/SKILL.md:39:3 · **resolved** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/skill-creator/SKILL.md:41:1 · **resolved** · fingerprint: b3b51b275e9ef2296ec3dd01
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **synonym-rotation** · skills/skill-creator/SKILL.md:54:35 · **resolved** · fingerprint: 7a3d7648e3a631037e76cf6d
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · skills/skill-creator/SKILL.md:60:1 · **resolved** · fingerprint: bd108e08bd9bf096790dc153
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **long-sentence** · skills/skill-creator/SKILL.md:67:398 · **resolved** · fingerprint: 0a0fc1886c1048efdc236f0b
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **synonym-rotation** · skills/skill-creator/SKILL.md:67:467 · **resolved** · fingerprint: b5b2e581ff9ad306cac93f39
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** display
- **long-sentence** · skills/skill-creator/SKILL.md:67:592 · **resolved** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · skills/skill-creator/SKILL.md:96:3 · **resolved** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **semicolon** · skills/skill-creator/SKILL.md:96:32 · **resolved** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · skills/skill-creator/SKILL.md:171:190 · **resolved** · fingerprint: c8837f28e78344d9ce3dae88
  - **Level:** advisory-free
  - **Message:** 'launch' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** Launch
- **long-sentence** · skills/skill-creator/SKILL.md:203:1 · **resolved** · fingerprint: b3b51b275e9ef2296ec3dd01
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · skills/skill-creator/SKILL.md:223:15 · **resolved** · fingerprint: aa754f9c434238c7ca7024d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are done
- **long-sentence** · skills/skill-creator/SKILL.md:225:386 · **resolved** · fingerprint: 81a0eb0a3166d8b6ad5e3282
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/skill-creator/SKILL.md:234:106 · **resolved** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · skills/skill-creator/SKILL.md:249:57 · **resolved** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/skill-creator/SKILL.md:256:29 · **resolved** · fingerprint: 7f9cc5be406601f9334d0a9f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was given
- **passive-voice** · skills/skill-creator/SKILL.md:259:33 · **resolved** · fingerprint: 073227ab82a9e051ae64eb07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run
- **present-perfect** · skills/skill-creator/SKILL.md:294:68 · **resolved** · fingerprint: 39027c43abde57eb08780deb
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has reviewed
- **long-sentence** · skills/skill-creator/SKILL.md:298:38 · **resolved** · fingerprint: 0a0fc1886c1048efdc236f0b
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **long-sentence** · skills/skill-creator/SKILL.md:298:522 · **resolved** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/skill-creator/SKILL.md:300:78 · **resolved** · fingerprint: 5442f1f21a2b76c5f0d49f1a
  - **Level:** advisory-free
  - **Message:** Sentence has 52 words (cap 25). Split it.
  - **Matched text:** 52 words
- **long-sentence** · skills/skill-creator/SKILL.md:302:255 · **resolved** · fingerprint: 2e7431350f9b2729b3a6b971
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **long-sentence** · skills/skill-creator/SKILL.md:302:485 · **resolved** · fingerprint: bc0db0a6aca974542651f79d
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **long-sentence** · skills/skill-creator/SKILL.md:304:50 · **resolved** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · skills/skill-creator/SKILL.md:306:138 · **resolved** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/skill-creator/SKILL.md:313:214 · **resolved** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/skill-creator/SKILL.md:327:1 · **resolved** · fingerprint: 285c7910fd39a83bb1401a2b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/skill-creator/SKILL.md:348:429 · **resolved** · fingerprint: 81a0eb0a3166d8b6ad5e3282
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/skill-creator/SKILL.md:356:1 · **resolved** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/skill-creator/SKILL.md:356:187 · **resolved** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · skills/skill-creator/SKILL.md:394:56 · **resolved** · fingerprint: cfd51398e7020a0fbdafe7ba
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **long-sentence** · skills/skill-creator/SKILL.md:394:362 · **resolved** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/skill-creator/SKILL.md:398:228 · **resolved** · fingerprint: 4ba45f4babc708e638969a97
  - **Level:** advisory-free
  - **Message:** Sentence has 47 words (cap 25). Split it.
  - **Matched text:** 47 words
- **long-sentence** · skills/skill-creator/SKILL.md:424:206 · **resolved** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · skills/skill-creator/SKILL.md:426:264 · **resolved** · fingerprint: cccbdcfa7cc6ce04982ee106
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · skills/skill-creator/SKILL.md:451:3 · **resolved** · fingerprint: b13f3ee36e07d9b3e730917b
  - **Level:** advisory-free
  - **Message:** Sentence has 66 words (cap 25). Split it.
  - **Matched text:** 66 words
- **long-sentence** · skills/skill-creator/SKILL.md:454:3 · **resolved** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/skill-creator/SKILL.md:480:33 · **resolved** · fingerprint: 9b5eb6649d3441bc6d4564c7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **long-sentence** · skills/skill-creator/SKILL.md:483:93 · **resolved** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/define-goal/SKILL.md:3:14 · **resolved** · fingerprint: 3c3b8526ec42c8236337ec34
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **semicolon** · skills/define-goal/SKILL.md:3:303 · **resolved** · fingerprint: 4b3d24f9aed9b98b70670a67
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/define-goal/SKILL.md:17:6 · **resolved** · fingerprint: 36d1e3a66695e9ccae667cb7
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **synonym-rotation** · skills/define-goal/SKILL.md:31:41 · **resolved** · fingerprint: 7ffb6feff2099d48d0f7cbae
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · skills/define-goal/SKILL.md:39:125 · **resolved** · fingerprint: 53fe342999b284bfb8bd5229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are sharpened
- **long-sentence** · skills/define-goal/SKILL.md:45:6 · **resolved** · fingerprint: 36d1e3a66695e9ccae667cb7
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · skills/define-goal/SKILL.md:58:46 · **resolved** · fingerprint: 95854f6562674ce44ac99933
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **long-sentence** · skills/define-goal/SKILL.md:66:3 · **resolved** · fingerprint: 3c3b8526ec42c8236337ec34
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **synonym-rotation** · skills/define-goal/SKILL.md:66:130 · **resolved** · fingerprint: d5e7ea11f84d519e58dae002
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **long-sentence** · skills/define-goal/SKILL.md:70:3 · **resolved** · fingerprint: 02027dda3d9662b4af3db321
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **synonym-rotation** · skills/define-goal/SKILL.md:82:51 · **resolved** · fingerprint: d10340e745766e580d758131
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **passive-voice** · skills/skill-creator/references/schemas.md:76:35 · **resolved** · fingerprint: b2f957f961ac90f2b5e25347
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being improved
- **passive-voice** · skills/skill-creator/references/schemas.md:79:46 · **resolved** · fingerprint: fc77b5ae02889cc12a032af8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was derived
- **passive-voice** · skills/skill-creator/references/schemas.md:291:37 · **resolved** · fingerprint: 07fb28aa8827a903ec8ce46f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run
- **long-sentence** · skills/migrate-to-rust/SKILL.md:7:3 · **resolved** · fingerprint: a662b736df433f7da92e66fc
  - **Level:** advisory-free
  - **Message:** Sentence has 55 words (cap 25). Split it.
  - **Matched text:** 55 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:12:57 · **resolved** · fingerprint: e2295110305762ff8e335a91
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:31:5 · **resolved** · fingerprint: 7028a07f9a3fb5f858d31275
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **passive-voice** · skills/migrate-to-rust/SKILL.md:36:5 · **resolved** · fingerprint: d383e306464baf7b95b09904
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is granted
- **long-sentence** · skills/migrate-to-rust/SKILL.md:37:5 · **resolved** · fingerprint: b88d92a5c0e5e167cff4ad82
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:42:5 · **resolved** · fingerprint: 78e0abedeafeb317479e2a5b
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:43:26 · **resolved** · fingerprint: 57d64593c4bd12d2d0efd0ce
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · skills/migrate-to-rust/SKILL.md:46:45 · **resolved** · fingerprint: 0d7124ea47427cfe3b990b70
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · skills/migrate-to-rust/SKILL.md:47:22 · **resolved** · fingerprint: 467939dfbb29b044552a4f11
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exhausted
- **passive-voice** · skills/migrate-to-rust/SKILL.md:56:40 · **resolved** · fingerprint: 0bb9a329b75fa24f68895375
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/migrate-to-rust/SKILL.md:60:20 · **resolved** · fingerprint: 95972905cbdd013afe6ad4d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are measured
- **passive-voice** · skills/migrate-to-rust/SKILL.md:62:73 · **resolved** · fingerprint: 4f992062ac109aed75870bc0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered
- **long-sentence** · skills/migrate-to-rust/SKILL.md:102:58 · **resolved** · fingerprint: 4c2241f7419e1cf7fc294279
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:107:5 · **resolved** · fingerprint: 3f2ed706861e681ceff6a9f4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:107:7 · **resolved** · fingerprint: 1f3f76c2dc2193679fdec0b3
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **long-sentence** · skills/migrate-to-rust/SKILL.md:110:19 · **resolved** · fingerprint: 0d7124ea47427cfe3b990b70
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:119:1 · **resolved** · fingerprint: fbc4aa5d66dc3fafe7ac3cde
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:155:5 · **resolved** · fingerprint: 252237a4f0aa1d04ceb61fc9
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · skills/migrate-to-rust/SKILL.md:159:24 · **resolved** · fingerprint: 88add639cbc69b3d060a35f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reached
- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:169:68 · **resolved** · fingerprint: 2f192b17ca60a110bed2f049
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **long-sentence** · skills/migrate-to-rust/SKILL.md:176:5 · **resolved** · fingerprint: fbc4aa5d66dc3fafe7ac3cde
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/internal-comms/examples/general-comms.md:2:11 · **resolved** · fingerprint: f5182f6e401a8e0cd0a281d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · skills/skill-creator/agents/comparator.md:9:15 · **resolved** · fingerprint: 6c4d2de7a2ac7b8671c78576
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based
- **passive-voice** · skills/skill-creator/agents/comparator.md:17:50 · **resolved** · fingerprint: fc725ae1310f6770f082b7d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was executed
- **passive-voice** · skills/skill-creator/agents/comparator.md:48:38 · **resolved** · fingerprint: 1a4e8dde9b444c0c6a259329
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is organized
- **passive-voice** · skills/skill-creator/agents/comparator.md:70:17 · **resolved** · fingerprint: 06e2447aaf67b0f70bd1d6f4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are provided
- **passive-voice** · skills/skill-creator/agents/comparator.md:172:20 · **resolved** · fingerprint: 2b87728a994a74cda45b6f17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were provided
- **semicolon** · skills/skill-creator/agents/comparator.md:200:67 · **resolved** · fingerprint: c0fa64514011ccf40bcaa205
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:3:1 · **resolved** · fingerprint: 8941f6e0f48e87a46cae1089
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:49:49 · **resolved** · fingerprint: 97b200de091b786e8d3ac8e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is isolated
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:72:5 · **resolved** · fingerprint: 88e99411d9c8e38d261735a0
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:86:5 · **resolved** · fingerprint: 4dcee79a954a878bd5a8ea33
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:96:26 · **resolved** · fingerprint: e95dbe9e5215964e3cded5ab
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:97:34 · **resolved** · fingerprint: c51b0ce42e3586600dd045b8
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:98:5 · **resolved** · fingerprint: 613ef8f7b5298e0c6db14dc0
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:112:9 · **resolved** · fingerprint: e95dbe9e5215964e3cded5ab
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **semicolon** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:102 · **resolved** · fingerprint: 0ec9ec46610bc293be0f4026
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:129 · **resolved** · fingerprint: 0ec9ec46610bc293be0f4026
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:147:28 · **resolved** · fingerprint: f44a8b2b9d31a4c738017b9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grounded
- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:170:7 · **resolved** · fingerprint: 48f91bb35f25b0197e2d1854
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirming
- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:220:22 · **resolved** · fingerprint: c40e0a110415686139157e67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is enforced
- **long-sentence** · skills/xlsx/SKILL.md:3:90 · **resolved** · fingerprint: f01d015c0294a320ea718e21
  - **Level:** advisory-free
  - **Message:** Sentence has 50 words (cap 25). Split it.
  - **Matched text:** 50 words
- **semicolon** · skills/xlsx/SKILL.md:3:297 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/xlsx/SKILL.md:3:363 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:3:406 · **resolved** · fingerprint: ccb49c9369554c45dc85cff9
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/xlsx/SKILL.md:3:776 · **resolved** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · skills/xlsx/SKILL.md:3:953 · **resolved** · fingerprint: d7c3da4cab34766bbeb18c4a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is involved
- **semicolon** · skills/xlsx/SKILL.md:13:80 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/xlsx/SKILL.md:16:42 · **resolved** · fingerprint: 2c1023f6d06e7f043fe8aae6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preinstalled
- **semicolon** · skills/xlsx/SKILL.md:16:91 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/xlsx/SKILL.md:23:79 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/xlsx/SKILL.md:26:246 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:27:3 · **resolved** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · skills/xlsx/SKILL.md:27:207 · **resolved** · fingerprint: f3aa2c4d7e06ebf371e77816
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were asked
- **long-sentence** · skills/xlsx/SKILL.md:40:1 · **resolved** · fingerprint: 011da665a0c2ff74a6b74755
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **long-sentence** · skills/xlsx/SKILL.md:44:8 · **resolved** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · skills/xlsx/SKILL.md:44:71 · **resolved** · fingerprint: 189dece9ba87f307d9a452d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was recalculated
- **semicolon** · skills/xlsx/SKILL.md:55:40 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/xlsx/SKILL.md:58:80 · **resolved** · fingerprint: 036f999f6b29928b3dbfe0a2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed
- **long-sentence** · skills/xlsx/SKILL.md:66:3 · **resolved** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **long-sentence** · skills/xlsx/SKILL.md:67:81 · **resolved** · fingerprint: eaf247ebd4907c600853b68a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · skills/xlsx/SKILL.md:68:17 · **resolved** · fingerprint: afb595bdfd38499714786a9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reported
- **synonym-rotation** · skills/xlsx/SKILL.md:68:148 · **resolved** · fingerprint: 78a832da081777bd2e464819
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **semicolon** · skills/xlsx/SKILL.md:72:100 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/xlsx/SKILL.md:75:116 · **resolved** · fingerprint: f474913920113893681a698c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **semicolon** · skills/xlsx/SKILL.md:78:160 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:79:3 · **resolved** · fingerprint: aad8f9ccd5b6288ae3de1a6f
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/xlsx/SKILL.md:79:167 · **resolved** · fingerprint: ef7c6ddf0f899365fab978af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are saved
- **passive-voice** · skills/xlsx/SKILL.md:80:37 · **resolved** · fingerprint: 115b0065fd7574ef88e08839
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is flattened
- **semicolon** · skills/xlsx/SKILL.md:80:90 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:82:3 · **resolved** · fingerprint: dad26d2d8ae1bd2000776a97
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words
- **long-sentence** · skills/xlsx/SKILL.md:89:1 · **resolved** · fingerprint: 34d7440bbd271044262654bf
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **long-sentence** · skills/xlsx/SKILL.md:93:1 · **resolved** · fingerprint: ccb49c9369554c45dc85cff9
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · skills/xlsx/SKILL.md:95:68 · **resolved** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:98:1 · **resolved** · fingerprint: 3c6294d2724d449d03904c6d
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 50
- **Hard findings:** 23
- **Baseline:** 0
- **Words:** 9822
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:36:10 · **new** · fingerprint: a737104c50ceb40f303a4a01
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended

- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:332 · **new** · fingerprint: 63b66afb8b84b4750380eace
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:38:388 · **new** · fingerprint: e18acfaf818e2c30f6ca30e9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:158:1 · **new** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:169:21 · **new** · fingerprint: 34fd4b4fc86f7c4829f49935
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validated

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:179:143 · **new** · fingerprint: 8fab87c9578c4937b0124edf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:181:62 · **new** · fingerprint: 7c3c1ace5ec3d5c53c98a4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are observed

- **present-perfect** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:183:69 · **new** · fingerprint: 1614dc41c4b7be8e66e6f0d4
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:120 · **new** · fingerprint: 2e23d59621877db75c28ce78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:184:223 · **new** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:206:177 · **new** · fingerprint: ff8dedd324f39ede5ee75f82
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:208:43 · **new** · fingerprint: ae6b75fe50ddf475f002c2af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is fragmented

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:210:53 · **new** · fingerprint: e6a0a6a3cb10281e485f4ced
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been measured

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:235:53 · **new** · fingerprint: e0805effa50f8c2d06788a7e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:261:171 · **new** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:292:60 · **new** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:295:388 · **new** · fingerprint: 84a34fb70b809525fcff26b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been piloted

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:296:52 · **new** · fingerprint: 2bc5f6f2f61d2bd47030e11b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:313:90 · **new** · fingerprint: cd8c27dadbc8cbf2ffa0ea4b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unsupported

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:325:178 · **new** · fingerprint: 8e84e07883201687e9d6dbbf
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:346:218 · **new** · fingerprint: a27c714d52cff462c278171d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:458:36 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:482:251 · **new** · fingerprint: a484bb1a5b40074d480f3f91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is configured

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:502:30 · **new** · fingerprint: 0de287d1c4eae57b62d477b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:503:52 · **new** · fingerprint: cbf03a5bdfbefc8d301bac6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are resolved

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:504:22 · **new** · fingerprint: ba2af3047b1dbc7bfdba2dd0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are classified

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:541:4 · **new** · fingerprint: 93b3c8314ad783839cf934a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:585:23 · **new** · fingerprint: ebe3a0eaf57219e6e13da654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is treated

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:586:94 · **new** · fingerprint: b1897a649c20569be1ac0618
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:598:63 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:610:53 · **new** · fingerprint: 1e8f06c794753d0da4c374f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are supported

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:611:217 · **new** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:613:256 · **new** · fingerprint: deb50ff287f5e69a8ed3d45a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:640:93 · **new** · fingerprint: 316a7cc78530dc52ed55aeb6
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:670:104 · **new** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:4 · **new** · fingerprint: 2a27149bc363daa6f4a3a38e
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:107 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:166 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:678:212 · **new** · fingerprint: cda7ec14df291f440000a085
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:680:4 · **new** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:48 · **new** · fingerprint: 5c278ad2f255230faa055f76
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:90 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:694:122 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:700:45 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:707:246 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:708:194 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:155 · **new** · fingerprint: 28ee61d5eaadf9744f6bf805
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:711:240 · **new** · fingerprint: dd5a9425158b41b001c9b936
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created

- **synonym-rotation** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:712:91 · **new** · fingerprint: c6bfceae059912f8aadd9e2e
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fixed

- **long-sentence** · workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md:718:1 · **new** · fingerprint: ee090e362481d6ce86016eb8
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 2212
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/draft/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 665
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **semicolon** · workspace/draft/README.md:7:96 · **new** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/README.md:19:4 · **new** · fingerprint: fa0ad26c0f4696b24c6e471f
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **semicolon** · workspace/draft/README.md:21:305 · **new** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/README.md:23:136 · **new** · fingerprint: 23958065d6cbd83c298c65e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been assessed

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
