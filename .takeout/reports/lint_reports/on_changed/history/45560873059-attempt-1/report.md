# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#696](https://github.com/dungnv2602/chatgpt/actions/runs/45560873059)
- **Run ID / attempt:** 45560873059 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 20e90a6b97317cb7c0c689dac9864baac3d64207
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 1b0d7bb58e734e64a7c3b1c778749f44cb097ac5
- **Linter source SHA:** 20e90a6b97317cb7c0c689dac9864baac3d64207
- **Generated (UTC):** 2026-11-25T06:29:23.019710+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 32 |
| Files that failed | 19 |
| Files with findings | 21 |
| Total findings | 242 |
| Hard findings | 161 |
| Advisory findings | 81 |
| New findings | 242 |
| Recurring findings | 0 |
| Resolved findings | 25 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- skills/skill-creator/agents/grader.md
- skills/theme-factory/themes/arctic-frost.md
- skills/internal-comms/examples/company-newsletter.md
- skills/pdf/FORMS.md
- skills/theme-factory/themes/tech-innovation.md
- skills/theme-factory/themes/modern-minimalist.md
- skills/theme-factory/themes/forest-canopy.md
- skills/internal-comms/examples/faq-answers.md
- skills/theme-factory/SKILL.md
- skills/grilling/SKILL.md
- skills/theme-factory/themes/midnight-galaxy.md
- skills/theme-factory/themes/botanical-garden.md
- skills/internal-comms/examples/3p-updates.md
- skills/theme-factory/themes/golden-hour.md
- workspace/task_board.md
- skills/theme-factory/themes/ocean-depths.md
- skills/discernment-nudge/SKILL.md
- skills/internal-comms/SKILL.md
- skills/skill-creator/agents/analyzer.md
- skills/pdf/SKILL.md
- skills/doc-coauthoring/SKILL.md
- skills/skill-creator/SKILL.md
- skills/theme-factory/themes/sunset-boulevard.md
- skills/define-goal/SKILL.md
- skills/skill-creator/references/schemas.md
- skills/migrate-to-rust/SKILL.md
- skills/theme-factory/themes/desert-rose.md
- skills/internal-comms/examples/general-comms.md
- skills/skill-creator/agents/comparator.md
- skills/migrate-to-rust/references/pgo_and_telemetry_guide.md
- skills/xlsx/SKILL.md
- skills/pdf/REFERENCE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| skills/skill-creator/agents/grader.md | FAIL | 4 | 1 | 0 | 998 | 0.4 | 1 |
| skills/theme-factory/themes/arctic-frost.md | PASS | 0 | 0 | 0 | 73 | 0.0 | 0 |
| skills/internal-comms/examples/company-newsletter.md | FAIL | 4 | 1 | 0 | 554 | 0.7 | 1 |
| skills/pdf/FORMS.md | FAIL | 13 | 8 | 0 | 1195 | 1.1 | 1 |
| skills/theme-factory/themes/tech-innovation.md | FAIL | 1 | 1 | 0 | 73 | 1.4 | 1 |
| skills/theme-factory/themes/modern-minimalist.md | PASS | 0 | 0 | 0 | 74 | 0.0 | 0 |
| skills/theme-factory/themes/forest-canopy.md | PASS | 0 | 0 | 0 | 68 | 0.0 | 0 |
| skills/internal-comms/examples/faq-answers.md | FAIL | 7 | 4 | 0 | 403 | 1.7 | 1 |
| skills/theme-factory/SKILL.md | FAIL | 6 | 2 | 0 | 473 | 1.3 | 1 |
| skills/grilling/SKILL.md | FAIL | 6 | 4 | 0 | 289 | 2.1 | 1 |
| skills/theme-factory/themes/midnight-galaxy.md | PASS | 0 | 0 | 0 | 70 | 0.0 | 0 |
| skills/theme-factory/themes/botanical-garden.md | PASS | 0 | 0 | 0 | 69 | 0.0 | 0 |
| skills/internal-comms/examples/3p-updates.md | FAIL | 3 | 1 | 0 | 552 | 0.5 | 1 |
| skills/theme-factory/themes/golden-hour.md | PASS | 0 | 0 | 0 | 71 | 0.0 | 0 |
| workspace/task_board.md | PASS | 0 | 0 | 0 | 1432 | 0.0 | 0 |
| skills/theme-factory/themes/ocean-depths.md | PASS | 0 | 0 | 0 | 76 | 0.0 | 0 |
| skills/discernment-nudge/SKILL.md | FAIL | 26 | 24 | 0 | 1701 | 1.5 | 1 |
| skills/internal-comms/SKILL.md | FAIL | 1 | 1 | 0 | 196 | 0.5 | 1 |
| skills/skill-creator/agents/analyzer.md | FAIL | 4 | 1 | 0 | 1147 | 0.3 | 1 |
| skills/pdf/SKILL.md | FAIL | 1 | 1 | 0 | 347 | 0.3 | 1 |
| skills/doc-coauthoring/SKILL.md | FAIL | 28 | 9 | 0 | 2456 | 1.1 | 1 |
| skills/skill-creator/SKILL.md | FAIL | 49 | 43 | 0 | 4775 | 1.0 | 1 |
| skills/theme-factory/themes/sunset-boulevard.md | PASS | 0 | 0 | 0 | 76 | 0.0 | 0 |
| skills/define-goal/SKILL.md | FAIL | 11 | 9 | 0 | 857 | 1.3 | 1 |
| skills/skill-creator/references/schemas.md | PASS | 3 | 0 | 0 | 518 | 0.6 | 0 |
| skills/migrate-to-rust/SKILL.md | FAIL | 21 | 15 | 0 | 1173 | 1.8 | 1 |
| skills/theme-factory/themes/desert-rose.md | PASS | 0 | 0 | 0 | 68 | 0.0 | 0 |
| skills/internal-comms/examples/general-comms.md | PASS | 1 | 0 | 0 | 85 | 1.2 | 0 |
| skills/skill-creator/agents/comparator.md | FAIL | 6 | 1 | 0 | 735 | 0.8 | 1 |
| skills/migrate-to-rust/references/pgo_and_telemetry_guide.md | FAIL | 13 | 10 | 0 | 1274 | 1.0 | 1 |
| skills/xlsx/SKILL.md | FAIL | 34 | 25 | 0 | 1408 | 2.4 | 1 |
| skills/pdf/REFERENCE.md | PASS | 0 | 0 | 0 | 394 | 0.0 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| long-sentence | 103 |
| passive-voice | 70 |
| semicolon | 29 |
| synonym-rotation | 28 |
| present-perfect | 11 |
| marketing-adjective | 1 |

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
Ran 4 tests in 0.342s

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

- **synonym-rotation** · skills/skill-creator/agents/grader.md:43:25 · **new** · fingerprint: f6b0cd4515b63f0d695cd984
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · skills/skill-creator/agents/grader.md:50:34 · **new** · fingerprint: eda68c8e5f0024bbf44478a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were filled
- **passive-voice** · skills/skill-creator/agents/grader.md:55:53 · **new** · fingerprint: 6d8513652396223c46db7c53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/skill-creator/agents/grader.md:204:30 · **new** · fingerprint: e47fae0d3214443b275d83bf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being verified
- **passive-voice** · skills/internal-comms/examples/company-newsletter.md:2:9 · **new** · fingerprint: 674f8c6b10c2692aba1d6872
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · skills/internal-comms/examples/company-newsletter.md:5:3 · **new** · fingerprint: 962ad33b16c74cce9136544c
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **present-perfect** · skills/internal-comms/examples/company-newsletter.md:5:245 · **new** · fingerprint: e21a631576722f4ba88c9a40
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have happened
- **passive-voice** · skills/internal-comms/examples/company-newsletter.md:21:418 · **new** · fingerprint: a5c77894421daf1d053502ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are highlighted
- **long-sentence** · skills/pdf/FORMS.md:53:3 · **new** · fingerprint: 633ed34d5a9f1f808fb3863d
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words
- **long-sentence** · skills/pdf/FORMS.md:74:3 · **new** · fingerprint: d1f4e4a17700e4fddf56e470
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **synonym-rotation** · skills/pdf/FORMS.md:76:18 · **new** · fingerprint: d0326226d8f30a067ce6965d
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **semicolon** · skills/pdf/FORMS.md:76:76 · **new** · fingerprint: d1786a470e3e35ea435e593b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/pdf/FORMS.md:92:179 · **new** · fingerprint: 3fe66375b59c3b0c8018b635
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned
- **passive-voice** · skills/pdf/FORMS.md:114:51 · **new** · fingerprint: bbe9290d6bdb305c9943d943
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected
- **long-sentence** · skills/pdf/FORMS.md:118:1 · **new** · fingerprint: 4df56657f6044a9e3d88ab1e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · skills/pdf/FORMS.md:163:10 · **new** · fingerprint: bc0b3a7638b2e3238d494397
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **synonym-rotation** · skills/pdf/FORMS.md:168:99 · **new** · fingerprint: 31453b7d73f9081ba7fc7aa1
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix
- **passive-voice** · skills/pdf/FORMS.md:174:23 · **new** · fingerprint: 3fe66375b59c3b0c8018b635
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned
- **synonym-rotation** · skills/pdf/FORMS.md:210:50 · **new** · fingerprint: d9abe8c3f4f7d6196dda74a6
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins
- **passive-voice** · skills/pdf/FORMS.md:260:39 · **new** · fingerprint: bcb3c4f45b7f95b1cf8ceddc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were detected
- **passive-voice** · skills/pdf/FORMS.md:291:9 · **new** · fingerprint: 1c58d1ff24fa595261572915
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is mispositioned
- **marketing-adjective** · skills/theme-factory/themes/tech-innovation.md:3:63 · **new** · fingerprint: 80634a765c13460d206a2ec7
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **passive-voice** · skills/internal-comms/examples/faq-answers.md:2:55 · **new** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · skills/internal-comms/examples/faq-answers.md:2:225 · **new** · fingerprint: 49cf594e46f6ead99fc2a24e
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · skills/internal-comms/examples/faq-answers.md:4:3 · **new** · fingerprint: 7982191c1f28db7fbe5c2969
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/internal-comms/examples/faq-answers.md:7:1 · **new** · fingerprint: 7982191c1f28db7fbe5c2969
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/internal-comms/examples/faq-answers.md:12:3 · **new** · fingerprint: 3a87e9c439a250becbc034ed
  - **Level:** advisory-free
  - **Message:** Sentence has 49 words (cap 25). Split it.
  - **Matched text:** 49 words
- **passive-voice** · skills/internal-comms/examples/faq-answers.md:12:20 · **new** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · skills/internal-comms/examples/faq-answers.md:12:130 · **new** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **present-perfect** · skills/theme-factory/SKILL.md:3:218 · **new** · fingerprint: 88d72e2d65542550249f0c15
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been
- **synonym-rotation** · skills/theme-factory/SKILL.md:23:33 · **new** · fingerprint: 90937deb6d9e203b4956d892
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** Display
- **semicolon** · skills/theme-factory/SKILL.md:23:159 · **new** · fingerprint: a9118ae923ba3eb2ca0eed95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/theme-factory/SKILL.md:26:38 · **new** · fingerprint: fc51630c87430edc3e5ee859
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been chosen
- **passive-voice** · skills/theme-factory/SKILL.md:45:12 · **new** · fingerprint: cc0e98e90677694b95ddacea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is defined
- **passive-voice** · skills/theme-factory/SKILL.md:52:25 · **new** · fingerprint: 9161559ebd704659b72aab24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected
- **long-sentence** · skills/grilling/SKILL.md:28:48 · **new** · fingerprint: 183863e52e0f6f06bf48dfcc
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · skills/grilling/SKILL.md:28:193 · **new** · fingerprint: ae6b7313f526901b623e262b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/grilling/SKILL.md:28:255 · **new** · fingerprint: 52a7f2689aea71be1612b603
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · skills/grilling/SKILL.md:28:397 · **new** · fingerprint: ae6b7313f526901b623e262b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/grilling/SKILL.md:30:13 · **new** · fingerprint: f0bdde4343f717a6d95280b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **present-perfect** · skills/grilling/SKILL.md:30:166 · **new** · fingerprint: 23f0857cbab27efe737d08c9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **passive-voice** · skills/internal-comms/examples/3p-updates.md:2:9 · **new** · fingerprint: 006084ecedd2b0f60f2a319e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **long-sentence** · skills/internal-comms/examples/3p-updates.md:4:141 · **new** · fingerprint: 0592d6c63ea607b94a7d508d
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **present-perfect** · skills/internal-comms/examples/3p-updates.md:7:28 · **new** · fingerprint: 1991d3b341dea71d1160d82e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has accomplished
- **long-sentence** · skills/discernment-nudge/SKILL.md:4:3 · **new** · fingerprint: 0a714b41c7716d9a6f1cab5e
  - **Level:** advisory-free
  - **Message:** Sentence has 88 words (cap 25). Split it.
  - **Matched text:** 88 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:12:59 · **new** · fingerprint: 66a0d61a227ac0548adbfcf7
  - **Level:** advisory-free
  - **Message:** Sentence has 64 words (cap 25). Split it.
  - **Matched text:** 64 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:27:42 · **new** · fingerprint: 09532e58e58d4dfe8bdc79d6
  - **Level:** advisory-free
  - **Message:** Sentence has 46 words (cap 25). Split it.
  - **Matched text:** 46 words
- **synonym-rotation** · skills/discernment-nudge/SKILL.md:38:9 · **new** · fingerprint: 8148fcf71c05d754866b31ae
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verifying
- **long-sentence** · skills/discernment-nudge/SKILL.md:52:3 · **new** · fingerprint: 7edd5e29457880d740b445be
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:55:3 · **new** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · skills/discernment-nudge/SKILL.md:58:42 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:59:39 · **new** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:66:3 · **new** · fingerprint: 0d46bb8bc736d2592d84c9ee
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:75:47 · **new** · fingerprint: 2732bbda68c4918a25cee5d7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · skills/discernment-nudge/SKILL.md:76:8 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:81:15 · **new** · fingerprint: bc449f6a09bfcee41f17a7e1
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **passive-voice** · skills/discernment-nudge/SKILL.md:83:24 · **new** · fingerprint: ef2a5302c79e63f003738349
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been invited
- **long-sentence** · skills/discernment-nudge/SKILL.md:84:34 · **new** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · skills/discernment-nudge/SKILL.md:89:51 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:101:54 · **new** · fingerprint: d4a15d9b253d6b8336214e0f
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **semicolon** · skills/discernment-nudge/SKILL.md:106:27 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:117:35 · **new** · fingerprint: 0d46bb8bc736d2592d84c9ee
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:121:65 · **new** · fingerprint: bc449f6a09bfcee41f17a7e1
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **semicolon** · skills/discernment-nudge/SKILL.md:130:36 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/discernment-nudge/SKILL.md:136:16 · **new** · fingerprint: fb1aa964536ca9c2e2071ce0
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **long-sentence** · skills/discernment-nudge/SKILL.md:141:39 · **new** · fingerprint: 2732bbda68c4918a25cee5d7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · skills/discernment-nudge/SKILL.md:156:9 · **new** · fingerprint: 09860b573750eb72110a818f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are weighed
- **long-sentence** · skills/discernment-nudge/SKILL.md:167:1 · **new** · fingerprint: b8df8fc4deef715436cbed14
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **semicolon** · skills/discernment-nudge/SKILL.md:171:34 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/discernment-nudge/SKILL.md:205:17 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/internal-comms/SKILL.md:3:136 · **new** · fingerprint: 6fb7073d863c9fbc89ee070c
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · skills/skill-creator/agents/analyzer.md:45:17 · **new** · fingerprint: 963c77d99b7e75e0a3bf0b37
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were used
- **synonym-rotation** · skills/skill-creator/agents/analyzer.md:81:27 · **new** · fingerprint: 73a20e38cbfda82326a10620
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modify
- **present-perfect** · skills/skill-creator/agents/analyzer.md:161:61 · **new** · fingerprint: a070d81ff2293e36967921ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have changed
- **passive-voice** · skills/skill-creator/agents/analyzer.md:200:37 · **new** · fingerprint: 8a779742e2e23efbc4881142
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being benchmarked
- **long-sentence** · skills/pdf/SKILL.md:3:84 · **new** · fingerprint: 80f948c0d409822bd1502a79
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:51:3 · **new** · fingerprint: c9464aa336f93a9a8d49a570
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · skills/doc-coauthoring/SKILL.md:56:24 · **new** · fingerprint: f058f8435b29176017e90d21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are answered
- **passive-voice** · skills/doc-coauthoring/SKILL.md:59:36 · **new** · fingerprint: e10d64cbb238674d2f93ba0f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:65:53 · **new** · fingerprint: c09611be7b0f6df8558b3632
  - **Level:** advisory-free
  - **Message:** 'get' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** get
- **long-sentence** · skills/doc-coauthoring/SKILL.md:72:1 · **new** · fingerprint: 9319ee289b0fe44d84643a21
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **passive-voice** · skills/doc-coauthoring/SKILL.md:72:22 · **new** · fingerprint: aacb3f77deb9a088671cd4ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected
- **passive-voice** · skills/doc-coauthoring/SKILL.md:86:42 · **new** · fingerprint: cee3981022d4e3499944c77e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being learned
- **long-sentence** · skills/doc-coauthoring/SKILL.md:94:1 · **new** · fingerprint: 70b1172296ab0a28aeb9fe21
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **present-perfect** · skills/doc-coauthoring/SKILL.md:97:20 · **new** · fingerprint: 63238be79dd0f680047ad702
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been gathered
- **passive-voice** · skills/doc-coauthoring/SKILL.md:97:24 · **new** · fingerprint: f3183f25b8780ed21113c300
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been gathered
- **passive-voice** · skills/doc-coauthoring/SKILL.md:130:18 · **new** · fingerprint: 65720f031e47f176970ebc0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is agreed
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:150:1 · **new** · fingerprint: 6a6fbd0d92479d7d01d8ae93
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **present-perfect** · skills/doc-coauthoring/SKILL.md:150:22 · **new** · fingerprint: 8cdb21ea190546014c9be542
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been created
- **passive-voice** · skills/doc-coauthoring/SKILL.md:150:26 · **new** · fingerprint: 27597883b1f70487be501033
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:156:20 · **new** · fingerprint: 9cc2456ea1ec0364078faf6b
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **present-perfect** · skills/doc-coauthoring/SKILL.md:200:40 · **new** · fingerprint: 97ebea75b5ec66e6e650944b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been drafted
- **passive-voice** · skills/doc-coauthoring/SKILL.md:200:44 · **new** · fingerprint: 8c0e9f5d680b69e4b6921173
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been drafted
- **long-sentence** · skills/doc-coauthoring/SKILL.md:202:1 · **new** · fingerprint: 295b724e21d2dc85c8f7ce1f
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/doc-coauthoring/SKILL.md:211:3 · **new** · fingerprint: 37fccb416c5a2c73a2b08580
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · skills/doc-coauthoring/SKILL.md:213:35 · **new** · fingerprint: 3c0ab4824ebf0184fa850617
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied
- **passive-voice** · skills/doc-coauthoring/SKILL.md:219:14 · **new** · fingerprint: a369cd14e91a6c55c8078a9e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **passive-voice** · skills/doc-coauthoring/SKILL.md:233:21 · **new** · fingerprint: f849879f47683f3042f9aa04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted
- **passive-voice** · skills/doc-coauthoring/SKILL.md:234:23 · **new** · fingerprint: f849879f47683f3042f9aa04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted
- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:312:30 · **new** · fingerprint: 1ee1d09f44673180016e2f67
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct
- **present-perfect** · skills/doc-coauthoring/SKILL.md:336:18 · **new** · fingerprint: 19bc6ba8838ee66ff59dc7b6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has passed
- **passive-voice** · skills/doc-coauthoring/SKILL.md:342:50 · **new** · fingerprint: a369cd14e91a6c55c8078a9e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **passive-voice** · skills/doc-coauthoring/SKILL.md:346:84 · **new** · fingerprint: 5f77ec29406067038b3f0fbd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was developed
- **passive-voice** · skills/doc-coauthoring/SKILL.md:348:30 · **new** · fingerprint: 6de4f19737e8127fa123c9f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is received
- **long-sentence** · skills/skill-creator/SKILL.md:3:100 · **new** · fingerprint: cfd51398e7020a0fbdafe7ba
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **long-sentence** · skills/skill-creator/SKILL.md:16:5 · **new** · fingerprint: 67edb283ba2426229ffbdd5b
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **synonym-rotation** · skills/skill-creator/SKILL.md:16:182 · **new** · fingerprint: 6089f9e6b2cd3054930b07d3
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change
- **long-sentence** · skills/skill-creator/SKILL.md:18:3 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/skill-creator/SKILL.md:22:1 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/skill-creator/SKILL.md:22:213 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/skill-creator/SKILL.md:26:1 · **new** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/skill-creator/SKILL.md:28:1 · **new** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/skill-creator/SKILL.md:28:22 · **new** · fingerprint: 7638fc0a5fbb6cceca5a3ffd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **long-sentence** · skills/skill-creator/SKILL.md:34:105 · **new** · fingerprint: 90b7c0eac3e2ee5b205b348c
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **long-sentence** · skills/skill-creator/SKILL.md:39:3 · **new** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/skill-creator/SKILL.md:41:1 · **new** · fingerprint: b3b51b275e9ef2296ec3dd01
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **synonym-rotation** · skills/skill-creator/SKILL.md:54:35 · **new** · fingerprint: 7a3d7648e3a631037e76cf6d
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · skills/skill-creator/SKILL.md:60:1 · **new** · fingerprint: bd108e08bd9bf096790dc153
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **long-sentence** · skills/skill-creator/SKILL.md:67:398 · **new** · fingerprint: 0a0fc1886c1048efdc236f0b
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **synonym-rotation** · skills/skill-creator/SKILL.md:67:467 · **new** · fingerprint: b5b2e581ff9ad306cac93f39
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** display
- **long-sentence** · skills/skill-creator/SKILL.md:67:592 · **new** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · skills/skill-creator/SKILL.md:96:3 · **new** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **semicolon** · skills/skill-creator/SKILL.md:96:32 · **new** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · skills/skill-creator/SKILL.md:171:190 · **new** · fingerprint: c8837f28e78344d9ce3dae88
  - **Level:** advisory-free
  - **Message:** 'launch' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** Launch
- **long-sentence** · skills/skill-creator/SKILL.md:203:1 · **new** · fingerprint: b3b51b275e9ef2296ec3dd01
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · skills/skill-creator/SKILL.md:223:15 · **new** · fingerprint: aa754f9c434238c7ca7024d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are done
- **long-sentence** · skills/skill-creator/SKILL.md:225:386 · **new** · fingerprint: 81a0eb0a3166d8b6ad5e3282
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/skill-creator/SKILL.md:234:106 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · skills/skill-creator/SKILL.md:249:57 · **new** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/skill-creator/SKILL.md:256:29 · **new** · fingerprint: 7f9cc5be406601f9334d0a9f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was given
- **passive-voice** · skills/skill-creator/SKILL.md:259:33 · **new** · fingerprint: 073227ab82a9e051ae64eb07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run
- **present-perfect** · skills/skill-creator/SKILL.md:294:68 · **new** · fingerprint: 39027c43abde57eb08780deb
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has reviewed
- **long-sentence** · skills/skill-creator/SKILL.md:298:38 · **new** · fingerprint: 0a0fc1886c1048efdc236f0b
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **long-sentence** · skills/skill-creator/SKILL.md:298:522 · **new** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/skill-creator/SKILL.md:300:78 · **new** · fingerprint: 5442f1f21a2b76c5f0d49f1a
  - **Level:** advisory-free
  - **Message:** Sentence has 52 words (cap 25). Split it.
  - **Matched text:** 52 words
- **long-sentence** · skills/skill-creator/SKILL.md:302:255 · **new** · fingerprint: 2e7431350f9b2729b3a6b971
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **long-sentence** · skills/skill-creator/SKILL.md:302:485 · **new** · fingerprint: bc0db0a6aca974542651f79d
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **long-sentence** · skills/skill-creator/SKILL.md:304:50 · **new** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · skills/skill-creator/SKILL.md:306:138 · **new** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/skill-creator/SKILL.md:313:214 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/skill-creator/SKILL.md:327:1 · **new** · fingerprint: 285c7910fd39a83bb1401a2b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/skill-creator/SKILL.md:348:429 · **new** · fingerprint: 81a0eb0a3166d8b6ad5e3282
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/skill-creator/SKILL.md:356:1 · **new** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/skill-creator/SKILL.md:356:187 · **new** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · skills/skill-creator/SKILL.md:394:56 · **new** · fingerprint: cfd51398e7020a0fbdafe7ba
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **long-sentence** · skills/skill-creator/SKILL.md:394:362 · **new** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/skill-creator/SKILL.md:398:228 · **new** · fingerprint: 4ba45f4babc708e638969a97
  - **Level:** advisory-free
  - **Message:** Sentence has 47 words (cap 25). Split it.
  - **Matched text:** 47 words
- **long-sentence** · skills/skill-creator/SKILL.md:424:206 · **new** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · skills/skill-creator/SKILL.md:426:264 · **new** · fingerprint: cccbdcfa7cc6ce04982ee106
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **long-sentence** · skills/skill-creator/SKILL.md:451:3 · **new** · fingerprint: b13f3ee36e07d9b3e730917b
  - **Level:** advisory-free
  - **Message:** Sentence has 66 words (cap 25). Split it.
  - **Matched text:** 66 words
- **long-sentence** · skills/skill-creator/SKILL.md:454:3 · **new** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/skill-creator/SKILL.md:480:33 · **new** · fingerprint: 9b5eb6649d3441bc6d4564c7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **long-sentence** · skills/skill-creator/SKILL.md:483:93 · **new** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/define-goal/SKILL.md:3:14 · **new** · fingerprint: 3c3b8526ec42c8236337ec34
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **semicolon** · skills/define-goal/SKILL.md:3:303 · **new** · fingerprint: 4b3d24f9aed9b98b70670a67
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/define-goal/SKILL.md:17:6 · **new** · fingerprint: 36d1e3a66695e9ccae667cb7
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **synonym-rotation** · skills/define-goal/SKILL.md:31:41 · **new** · fingerprint: 7ffb6feff2099d48d0f7cbae
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · skills/define-goal/SKILL.md:39:125 · **new** · fingerprint: 53fe342999b284bfb8bd5229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are sharpened
- **long-sentence** · skills/define-goal/SKILL.md:45:6 · **new** · fingerprint: 36d1e3a66695e9ccae667cb7
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · skills/define-goal/SKILL.md:58:46 · **new** · fingerprint: 95854f6562674ce44ac99933
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done
- **long-sentence** · skills/define-goal/SKILL.md:66:3 · **new** · fingerprint: 3c3b8526ec42c8236337ec34
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **synonym-rotation** · skills/define-goal/SKILL.md:66:130 · **new** · fingerprint: d5e7ea11f84d519e58dae002
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **long-sentence** · skills/define-goal/SKILL.md:70:3 · **new** · fingerprint: 02027dda3d9662b4af3db321
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **synonym-rotation** · skills/define-goal/SKILL.md:82:51 · **new** · fingerprint: d10340e745766e580d758131
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **passive-voice** · skills/skill-creator/references/schemas.md:76:35 · **new** · fingerprint: b2f957f961ac90f2b5e25347
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being improved
- **passive-voice** · skills/skill-creator/references/schemas.md:79:46 · **new** · fingerprint: fc77b5ae02889cc12a032af8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was derived
- **passive-voice** · skills/skill-creator/references/schemas.md:291:37 · **new** · fingerprint: 07fb28aa8827a903ec8ce46f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run
- **long-sentence** · skills/migrate-to-rust/SKILL.md:7:3 · **new** · fingerprint: a662b736df433f7da92e66fc
  - **Level:** advisory-free
  - **Message:** Sentence has 55 words (cap 25). Split it.
  - **Matched text:** 55 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:12:57 · **new** · fingerprint: e2295110305762ff8e335a91
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:31:5 · **new** · fingerprint: 7028a07f9a3fb5f858d31275
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **passive-voice** · skills/migrate-to-rust/SKILL.md:36:5 · **new** · fingerprint: d383e306464baf7b95b09904
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is granted
- **long-sentence** · skills/migrate-to-rust/SKILL.md:37:5 · **new** · fingerprint: b88d92a5c0e5e167cff4ad82
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:42:5 · **new** · fingerprint: 78e0abedeafeb317479e2a5b
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:43:26 · **new** · fingerprint: 57d64593c4bd12d2d0efd0ce
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · skills/migrate-to-rust/SKILL.md:46:45 · **new** · fingerprint: 0d7124ea47427cfe3b990b70
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · skills/migrate-to-rust/SKILL.md:47:22 · **new** · fingerprint: 467939dfbb29b044552a4f11
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exhausted
- **passive-voice** · skills/migrate-to-rust/SKILL.md:56:40 · **new** · fingerprint: 0bb9a329b75fa24f68895375
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/migrate-to-rust/SKILL.md:60:20 · **new** · fingerprint: 95972905cbdd013afe6ad4d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are measured
- **passive-voice** · skills/migrate-to-rust/SKILL.md:62:73 · **new** · fingerprint: 4f992062ac109aed75870bc0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered
- **long-sentence** · skills/migrate-to-rust/SKILL.md:102:58 · **new** · fingerprint: 4c2241f7419e1cf7fc294279
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:107:5 · **new** · fingerprint: 3f2ed706861e681ceff6a9f4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:107:7 · **new** · fingerprint: 1f3f76c2dc2193679fdec0b3
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **long-sentence** · skills/migrate-to-rust/SKILL.md:110:19 · **new** · fingerprint: 0d7124ea47427cfe3b990b70
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:119:1 · **new** · fingerprint: fbc4aa5d66dc3fafe7ac3cde
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · skills/migrate-to-rust/SKILL.md:155:5 · **new** · fingerprint: 252237a4f0aa1d04ceb61fc9
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · skills/migrate-to-rust/SKILL.md:159:24 · **new** · fingerprint: 88add639cbc69b3d060a35f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reached
- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:169:68 · **new** · fingerprint: 2f192b17ca60a110bed2f049
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **long-sentence** · skills/migrate-to-rust/SKILL.md:176:5 · **new** · fingerprint: fbc4aa5d66dc3fafe7ac3cde
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/internal-comms/examples/general-comms.md:2:11 · **new** · fingerprint: f5182f6e401a8e0cd0a281d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · skills/skill-creator/agents/comparator.md:9:15 · **new** · fingerprint: 6c4d2de7a2ac7b8671c78576
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based
- **passive-voice** · skills/skill-creator/agents/comparator.md:17:50 · **new** · fingerprint: fc725ae1310f6770f082b7d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was executed
- **passive-voice** · skills/skill-creator/agents/comparator.md:48:38 · **new** · fingerprint: 1a4e8dde9b444c0c6a259329
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is organized
- **passive-voice** · skills/skill-creator/agents/comparator.md:70:17 · **new** · fingerprint: 06e2447aaf67b0f70bd1d6f4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are provided
- **passive-voice** · skills/skill-creator/agents/comparator.md:172:20 · **new** · fingerprint: 2b87728a994a74cda45b6f17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were provided
- **semicolon** · skills/skill-creator/agents/comparator.md:200:67 · **new** · fingerprint: c0fa64514011ccf40bcaa205
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:3:1 · **new** · fingerprint: 8941f6e0f48e87a46cae1089
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:49:49 · **new** · fingerprint: 97b200de091b786e8d3ac8e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is isolated
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:72:5 · **new** · fingerprint: 88e99411d9c8e38d261735a0
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:86:5 · **new** · fingerprint: 4dcee79a954a878bd5a8ea33
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:96:26 · **new** · fingerprint: e95dbe9e5215964e3cded5ab
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:97:34 · **new** · fingerprint: c51b0ce42e3586600dd045b8
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:98:5 · **new** · fingerprint: 613ef8f7b5298e0c6db14dc0
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:112:9 · **new** · fingerprint: e95dbe9e5215964e3cded5ab
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **semicolon** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:102 · **new** · fingerprint: 0ec9ec46610bc293be0f4026
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:129 · **new** · fingerprint: 0ec9ec46610bc293be0f4026
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:147:28 · **new** · fingerprint: f44a8b2b9d31a4c738017b9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grounded
- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:170:7 · **new** · fingerprint: 48f91bb35f25b0197e2d1854
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirming
- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:220:22 · **new** · fingerprint: c40e0a110415686139157e67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is enforced
- **long-sentence** · skills/xlsx/SKILL.md:3:90 · **new** · fingerprint: f01d015c0294a320ea718e21
  - **Level:** advisory-free
  - **Message:** Sentence has 50 words (cap 25). Split it.
  - **Matched text:** 50 words
- **semicolon** · skills/xlsx/SKILL.md:3:297 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/xlsx/SKILL.md:3:363 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:3:406 · **new** · fingerprint: ccb49c9369554c45dc85cff9
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · skills/xlsx/SKILL.md:3:776 · **new** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · skills/xlsx/SKILL.md:3:953 · **new** · fingerprint: d7c3da4cab34766bbeb18c4a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is involved
- **semicolon** · skills/xlsx/SKILL.md:13:80 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/xlsx/SKILL.md:16:42 · **new** · fingerprint: 2c1023f6d06e7f043fe8aae6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preinstalled
- **semicolon** · skills/xlsx/SKILL.md:16:91 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/xlsx/SKILL.md:23:79 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/xlsx/SKILL.md:26:246 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:27:3 · **new** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · skills/xlsx/SKILL.md:27:207 · **new** · fingerprint: f3aa2c4d7e06ebf371e77816
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were asked
- **long-sentence** · skills/xlsx/SKILL.md:40:1 · **new** · fingerprint: 011da665a0c2ff74a6b74755
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **long-sentence** · skills/xlsx/SKILL.md:44:8 · **new** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · skills/xlsx/SKILL.md:44:71 · **new** · fingerprint: 189dece9ba87f307d9a452d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was recalculated
- **semicolon** · skills/xlsx/SKILL.md:55:40 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/xlsx/SKILL.md:58:80 · **new** · fingerprint: 036f999f6b29928b3dbfe0a2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed
- **long-sentence** · skills/xlsx/SKILL.md:66:3 · **new** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **long-sentence** · skills/xlsx/SKILL.md:67:81 · **new** · fingerprint: eaf247ebd4907c600853b68a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · skills/xlsx/SKILL.md:68:17 · **new** · fingerprint: afb595bdfd38499714786a9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reported
- **synonym-rotation** · skills/xlsx/SKILL.md:68:148 · **new** · fingerprint: 78a832da081777bd2e464819
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **semicolon** · skills/xlsx/SKILL.md:72:100 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/xlsx/SKILL.md:75:116 · **new** · fingerprint: f474913920113893681a698c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **semicolon** · skills/xlsx/SKILL.md:78:160 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:79:3 · **new** · fingerprint: aad8f9ccd5b6288ae3de1a6f
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/xlsx/SKILL.md:79:167 · **new** · fingerprint: ef7c6ddf0f899365fab978af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are saved
- **passive-voice** · skills/xlsx/SKILL.md:80:37 · **new** · fingerprint: 115b0065fd7574ef88e08839
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is flattened
- **semicolon** · skills/xlsx/SKILL.md:80:90 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:82:3 · **new** · fingerprint: dad26d2d8ae1bd2000776a97
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words
- **long-sentence** · skills/xlsx/SKILL.md:89:1 · **new** · fingerprint: 34d7440bbd271044262654bf
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **long-sentence** · skills/xlsx/SKILL.md:93:1 · **new** · fingerprint: ccb49c9369554c45dc85cff9
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · skills/xlsx/SKILL.md:95:68 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/xlsx/SKILL.md:98:1 · **new** · fingerprint: 3c6294d2724d449d03904c6d
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

### Recurring findings

None.

### Resolved findings

- **semicolon** · skills/decision-governance/SKILL.md:84:206 · **resolved** · fingerprint: 0c1945d1be17968236b3ecd9
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · skills/decision-governance/SKILL.md:103:283 · **resolved** · fingerprint: 745fe2084d6ac713461ff51a
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · skills/decision-governance/SKILL.md:107:38 · **resolved** · fingerprint: d06e7bd96064cab3016a0461
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · skills/decision-governance/SKILL.md:109:34 · **resolved** · fingerprint: c36782537305a07bdb58d06c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · skills/decision-governance/SKILL.md:115:47 · **resolved** · fingerprint: 1cb7ea75d4eb018776bb77e4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated
- **semicolon** · skills/decision-governance/SKILL.md:115:57 · **resolved** · fingerprint: 0c1945d1be17968236b3ecd9
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/decision-governance/SKILL.md:115:102 · **resolved** · fingerprint: ca3d08a0a95c039f5e31b693
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied
- **passive-voice** · skills/decision-governance/SKILL.md:117:86 · **resolved** · fingerprint: dda122e1893dc39b76ae7e74
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed
- **semicolon** · skills/decision-governance/SKILL.md:131:65 · **resolved** · fingerprint: 0c1945d1be17968236b3ecd9
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:45:121 · **resolved** · fingerprint: 18a6b0b7a0486b637074b006
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **semicolon** · skills/document-standards/references/document-type-catalog.md:45:212 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:45:458 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/README.md:7:96 · **resolved** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/README.md:18:4 · **resolved** · fingerprint: fa0ad26c0f4696b24c6e471f
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · workspace/draft/README.md:20:305 · **resolved** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/README.md:22:136 · **resolved** · fingerprint: 23958065d6cbd83c298c65e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been assessed
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:25:119 · **resolved** · fingerprint: f64bf1ef9acc14ca64a7b985
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:51:26 · **resolved** · fingerprint: 211b66e79e230bc550635a4f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were identified
- **semicolon** · workspace/DRAFT_TEMPLATE.md:53:58 · **resolved** · fingerprint: 3b682280b9ab9bb9d337e5a7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/DRAFT_TEMPLATE.md:63:103 · **resolved** · fingerprint: 3b682280b9ab9bb9d337e5a7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:78:47 · **resolved** · fingerprint: 3027ddebf5aa8173af033457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:91:47 · **resolved** · fingerprint: 3027ddebf5aa8173af033457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **long-sentence** · workspace/DRAFT_TEMPLATE.md:111:75 · **resolved** · fingerprint: 1068d0f64079905a096f3f87
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/DRAFT_TEMPLATE.md:124:55 · **resolved** · fingerprint: fe3d0313172da8b3bd40c574
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **synonym-rotation** · workspace/DRAFT_TEMPLATE.md:166:28 · **resolved** · fingerprint: fcd884bb6124b09c0acad1a2
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### skills/skill-creator/agents/grader.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 998
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **synonym-rotation** · skills/skill-creator/agents/grader.md:43:25 · **new** · fingerprint: f6b0cd4515b63f0d695cd984
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **passive-voice** · skills/skill-creator/agents/grader.md:50:34 · **new** · fingerprint: eda68c8e5f0024bbf44478a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were filled

- **passive-voice** · skills/skill-creator/agents/grader.md:55:53 · **new** · fingerprint: 6d8513652396223c46db7c53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified

- **passive-voice** · skills/skill-creator/agents/grader.md:204:30 · **new** · fingerprint: e47fae0d3214443b275d83bf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being verified


### skills/theme-factory/themes/arctic-frost.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 73
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/internal-comms/examples/company-newsletter.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 554
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · skills/internal-comms/examples/company-newsletter.md:2:9 · **new** · fingerprint: 674f8c6b10c2692aba1d6872
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **long-sentence** · skills/internal-comms/examples/company-newsletter.md:5:3 · **new** · fingerprint: 962ad33b16c74cce9136544c
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **present-perfect** · skills/internal-comms/examples/company-newsletter.md:5:245 · **new** · fingerprint: e21a631576722f4ba88c9a40
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have happened

- **passive-voice** · skills/internal-comms/examples/company-newsletter.md:21:418 · **new** · fingerprint: a5c77894421daf1d053502ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are highlighted


### skills/pdf/FORMS.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 13
- **Hard findings:** 8
- **Baseline:** 0
- **Words:** 1195
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **long-sentence** · skills/pdf/FORMS.md:53:3 · **new** · fingerprint: 633ed34d5a9f1f808fb3863d
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words

- **long-sentence** · skills/pdf/FORMS.md:74:3 · **new** · fingerprint: d1f4e4a17700e4fddf56e470
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **synonym-rotation** · skills/pdf/FORMS.md:76:18 · **new** · fingerprint: d0326226d8f30a067ce6965d
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **semicolon** · skills/pdf/FORMS.md:76:76 · **new** · fingerprint: d1786a470e3e35ea435e593b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/pdf/FORMS.md:92:179 · **new** · fingerprint: 3fe66375b59c3b0c8018b635
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned

- **passive-voice** · skills/pdf/FORMS.md:114:51 · **new** · fingerprint: bbe9290d6bdb305c9943d943
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected

- **long-sentence** · skills/pdf/FORMS.md:118:1 · **new** · fingerprint: 4df56657f6044a9e3d88ab1e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · skills/pdf/FORMS.md:163:10 · **new** · fingerprint: bc0b3a7638b2e3238d494397
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

- **synonym-rotation** · skills/pdf/FORMS.md:168:99 · **new** · fingerprint: 31453b7d73f9081ba7fc7aa1
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix

- **passive-voice** · skills/pdf/FORMS.md:174:23 · **new** · fingerprint: 3fe66375b59c3b0c8018b635
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scanned

- **synonym-rotation** · skills/pdf/FORMS.md:210:50 · **new** · fingerprint: d9abe8c3f4f7d6196dda74a6
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins

- **passive-voice** · skills/pdf/FORMS.md:260:39 · **new** · fingerprint: bcb3c4f45b7f95b1cf8ceddc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were detected

- **passive-voice** · skills/pdf/FORMS.md:291:9 · **new** · fingerprint: 1c58d1ff24fa595261572915
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is mispositioned


### skills/theme-factory/themes/tech-innovation.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 73
- **Findings per 100 words:** 1.4

#### Complete diagnostics

- **marketing-adjective** · skills/theme-factory/themes/tech-innovation.md:3:63 · **new** · fingerprint: 80634a765c13460d206a2ec7
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge


### skills/theme-factory/themes/modern-minimalist.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 74
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/theme-factory/themes/forest-canopy.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 68
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/internal-comms/examples/faq-answers.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 403
- **Findings per 100 words:** 1.7

#### Complete diagnostics

- **passive-voice** · skills/internal-comms/examples/faq-answers.md:2:55 · **new** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **long-sentence** · skills/internal-comms/examples/faq-answers.md:2:225 · **new** · fingerprint: 49cf594e46f6ead99fc2a24e
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **long-sentence** · skills/internal-comms/examples/faq-answers.md:4:3 · **new** · fingerprint: 7982191c1f28db7fbe5c2969
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · skills/internal-comms/examples/faq-answers.md:7:1 · **new** · fingerprint: 7982191c1f28db7fbe5c2969
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · skills/internal-comms/examples/faq-answers.md:12:3 · **new** · fingerprint: 3a87e9c439a250becbc034ed
  - **Level:** advisory-free
  - **Message:** Sentence has 49 words (cap 25). Split it.
  - **Matched text:** 49 words

- **passive-voice** · skills/internal-comms/examples/faq-answers.md:12:20 · **new** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **passive-voice** · skills/internal-comms/examples/faq-answers.md:12:130 · **new** · fingerprint: 9a56fa884d51cd2867afa899
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked


### skills/theme-factory/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 473
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **present-perfect** · skills/theme-factory/SKILL.md:3:218 · **new** · fingerprint: 88d72e2d65542550249f0c15
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been

- **synonym-rotation** · skills/theme-factory/SKILL.md:23:33 · **new** · fingerprint: 90937deb6d9e203b4956d892
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** Display

- **semicolon** · skills/theme-factory/SKILL.md:23:159 · **new** · fingerprint: a9118ae923ba3eb2ca0eed95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · skills/theme-factory/SKILL.md:26:38 · **new** · fingerprint: fc51630c87430edc3e5ee859
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been chosen

- **passive-voice** · skills/theme-factory/SKILL.md:45:12 · **new** · fingerprint: cc0e98e90677694b95ddacea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is defined

- **passive-voice** · skills/theme-factory/SKILL.md:52:25 · **new** · fingerprint: 9161559ebd704659b72aab24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected


### skills/grilling/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 289
- **Findings per 100 words:** 2.1

#### Complete diagnostics

- **long-sentence** · skills/grilling/SKILL.md:28:48 · **new** · fingerprint: 183863e52e0f6f06bf48dfcc
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · skills/grilling/SKILL.md:28:193 · **new** · fingerprint: ae6b7313f526901b623e262b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/grilling/SKILL.md:28:255 · **new** · fingerprint: 52a7f2689aea71be1612b603
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **semicolon** · skills/grilling/SKILL.md:28:397 · **new** · fingerprint: ae6b7313f526901b623e262b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/grilling/SKILL.md:30:13 · **new** · fingerprint: f0bdde4343f717a6d95280b9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **present-perfect** · skills/grilling/SKILL.md:30:166 · **new** · fingerprint: 23f0857cbab27efe737d08c9
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached


### skills/theme-factory/themes/midnight-galaxy.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 70
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/theme-factory/themes/botanical-garden.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 69
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/internal-comms/examples/3p-updates.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 552
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · skills/internal-comms/examples/3p-updates.md:2:9 · **new** · fingerprint: 006084ecedd2b0f60f2a319e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **long-sentence** · skills/internal-comms/examples/3p-updates.md:4:141 · **new** · fingerprint: 0592d6c63ea607b94a7d508d
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **present-perfect** · skills/internal-comms/examples/3p-updates.md:7:28 · **new** · fingerprint: 1991d3b341dea71d1160d82e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has accomplished


### skills/theme-factory/themes/golden-hour.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 71
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1432
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/theme-factory/themes/ocean-depths.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 76
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/discernment-nudge/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 26
- **Hard findings:** 24
- **Baseline:** 0
- **Words:** 1701
- **Findings per 100 words:** 1.5

#### Complete diagnostics

- **long-sentence** · skills/discernment-nudge/SKILL.md:4:3 · **new** · fingerprint: 0a714b41c7716d9a6f1cab5e
  - **Level:** advisory-free
  - **Message:** Sentence has 88 words (cap 25). Split it.
  - **Matched text:** 88 words

- **long-sentence** · skills/discernment-nudge/SKILL.md:12:59 · **new** · fingerprint: 66a0d61a227ac0548adbfcf7
  - **Level:** advisory-free
  - **Message:** Sentence has 64 words (cap 25). Split it.
  - **Matched text:** 64 words

- **long-sentence** · skills/discernment-nudge/SKILL.md:27:42 · **new** · fingerprint: 09532e58e58d4dfe8bdc79d6
  - **Level:** advisory-free
  - **Message:** Sentence has 46 words (cap 25). Split it.
  - **Matched text:** 46 words

- **synonym-rotation** · skills/discernment-nudge/SKILL.md:38:9 · **new** · fingerprint: 8148fcf71c05d754866b31ae
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verifying

- **long-sentence** · skills/discernment-nudge/SKILL.md:52:3 · **new** · fingerprint: 7edd5e29457880d740b445be
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · skills/discernment-nudge/SKILL.md:55:3 · **new** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · skills/discernment-nudge/SKILL.md:58:42 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/discernment-nudge/SKILL.md:59:39 · **new** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · skills/discernment-nudge/SKILL.md:66:3 · **new** · fingerprint: 0d46bb8bc736d2592d84c9ee
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · skills/discernment-nudge/SKILL.md:75:47 · **new** · fingerprint: 2732bbda68c4918a25cee5d7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · skills/discernment-nudge/SKILL.md:76:8 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/discernment-nudge/SKILL.md:81:15 · **new** · fingerprint: bc449f6a09bfcee41f17a7e1
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **passive-voice** · skills/discernment-nudge/SKILL.md:83:24 · **new** · fingerprint: ef2a5302c79e63f003738349
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been invited

- **long-sentence** · skills/discernment-nudge/SKILL.md:84:34 · **new** · fingerprint: edaa7ec5be833cea16777df0
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · skills/discernment-nudge/SKILL.md:89:51 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/discernment-nudge/SKILL.md:101:54 · **new** · fingerprint: d4a15d9b253d6b8336214e0f
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words

- **semicolon** · skills/discernment-nudge/SKILL.md:106:27 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/discernment-nudge/SKILL.md:117:35 · **new** · fingerprint: 0d46bb8bc736d2592d84c9ee
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · skills/discernment-nudge/SKILL.md:121:65 · **new** · fingerprint: bc449f6a09bfcee41f17a7e1
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **semicolon** · skills/discernment-nudge/SKILL.md:130:36 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/discernment-nudge/SKILL.md:136:16 · **new** · fingerprint: fb1aa964536ca9c2e2071ce0
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **long-sentence** · skills/discernment-nudge/SKILL.md:141:39 · **new** · fingerprint: 2732bbda68c4918a25cee5d7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · skills/discernment-nudge/SKILL.md:156:9 · **new** · fingerprint: 09860b573750eb72110a818f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are weighed

- **long-sentence** · skills/discernment-nudge/SKILL.md:167:1 · **new** · fingerprint: b8df8fc4deef715436cbed14
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **semicolon** · skills/discernment-nudge/SKILL.md:171:34 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/discernment-nudge/SKILL.md:205:17 · **new** · fingerprint: 50d12d368bab862dde7d9298
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### skills/internal-comms/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 196
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **long-sentence** · skills/internal-comms/SKILL.md:3:136 · **new** · fingerprint: 6fb7073d863c9fbc89ee070c
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words


### skills/skill-creator/agents/analyzer.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1147
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · skills/skill-creator/agents/analyzer.md:45:17 · **new** · fingerprint: 963c77d99b7e75e0a3bf0b37
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were used

- **synonym-rotation** · skills/skill-creator/agents/analyzer.md:81:27 · **new** · fingerprint: 73a20e38cbfda82326a10620
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modify

- **present-perfect** · skills/skill-creator/agents/analyzer.md:161:61 · **new** · fingerprint: a070d81ff2293e36967921ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have changed

- **passive-voice** · skills/skill-creator/agents/analyzer.md:200:37 · **new** · fingerprint: 8a779742e2e23efbc4881142
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being benchmarked


### skills/pdf/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 347
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **long-sentence** · skills/pdf/SKILL.md:3:84 · **new** · fingerprint: 80f948c0d409822bd1502a79
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words


### skills/doc-coauthoring/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 28
- **Hard findings:** 9
- **Baseline:** 0
- **Words:** 2456
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:51:3 · **new** · fingerprint: c9464aa336f93a9a8d49a570
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · skills/doc-coauthoring/SKILL.md:56:24 · **new** · fingerprint: f058f8435b29176017e90d21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are answered

- **passive-voice** · skills/doc-coauthoring/SKILL.md:59:36 · **new** · fingerprint: e10d64cbb238674d2f93ba0f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used

- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:65:53 · **new** · fingerprint: c09611be7b0f6df8558b3632
  - **Level:** advisory-free
  - **Message:** 'get' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** get

- **long-sentence** · skills/doc-coauthoring/SKILL.md:72:1 · **new** · fingerprint: 9319ee289b0fe44d84643a21
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **passive-voice** · skills/doc-coauthoring/SKILL.md:72:22 · **new** · fingerprint: aacb3f77deb9a088671cd4ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are detected

- **passive-voice** · skills/doc-coauthoring/SKILL.md:86:42 · **new** · fingerprint: cee3981022d4e3499944c77e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being learned

- **long-sentence** · skills/doc-coauthoring/SKILL.md:94:1 · **new** · fingerprint: 70b1172296ab0a28aeb9fe21
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **present-perfect** · skills/doc-coauthoring/SKILL.md:97:20 · **new** · fingerprint: 63238be79dd0f680047ad702
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been gathered

- **passive-voice** · skills/doc-coauthoring/SKILL.md:97:24 · **new** · fingerprint: f3183f25b8780ed21113c300
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been gathered

- **passive-voice** · skills/doc-coauthoring/SKILL.md:130:18 · **new** · fingerprint: 65720f031e47f176970ebc0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is agreed

- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:150:1 · **new** · fingerprint: 6a6fbd0d92479d7d01d8ae93
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **present-perfect** · skills/doc-coauthoring/SKILL.md:150:22 · **new** · fingerprint: 8cdb21ea190546014c9be542
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been created

- **passive-voice** · skills/doc-coauthoring/SKILL.md:150:26 · **new** · fingerprint: 27597883b1f70487be501033
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created

- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:156:20 · **new** · fingerprint: 9cc2456ea1ec0364078faf6b
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin

- **present-perfect** · skills/doc-coauthoring/SKILL.md:200:40 · **new** · fingerprint: 97ebea75b5ec66e6e650944b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been drafted

- **passive-voice** · skills/doc-coauthoring/SKILL.md:200:44 · **new** · fingerprint: 8c0e9f5d680b69e4b6921173
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been drafted

- **long-sentence** · skills/doc-coauthoring/SKILL.md:202:1 · **new** · fingerprint: 295b724e21d2dc85c8f7ce1f
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · skills/doc-coauthoring/SKILL.md:211:3 · **new** · fingerprint: 37fccb416c5a2c73a2b08580
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · skills/doc-coauthoring/SKILL.md:213:35 · **new** · fingerprint: 3c0ab4824ebf0184fa850617
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied

- **passive-voice** · skills/doc-coauthoring/SKILL.md:219:14 · **new** · fingerprint: a369cd14e91a6c55c8078a9e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **passive-voice** · skills/doc-coauthoring/SKILL.md:233:21 · **new** · fingerprint: f849879f47683f3042f9aa04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted

- **passive-voice** · skills/doc-coauthoring/SKILL.md:234:23 · **new** · fingerprint: f849879f47683f3042f9aa04
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are drafted

- **synonym-rotation** · skills/doc-coauthoring/SKILL.md:312:30 · **new** · fingerprint: 1ee1d09f44673180016e2f67
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct

- **present-perfect** · skills/doc-coauthoring/SKILL.md:336:18 · **new** · fingerprint: 19bc6ba8838ee66ff59dc7b6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has passed

- **passive-voice** · skills/doc-coauthoring/SKILL.md:342:50 · **new** · fingerprint: a369cd14e91a6c55c8078a9e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **passive-voice** · skills/doc-coauthoring/SKILL.md:346:84 · **new** · fingerprint: 5f77ec29406067038b3f0fbd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was developed

- **passive-voice** · skills/doc-coauthoring/SKILL.md:348:30 · **new** · fingerprint: 6de4f19737e8127fa123c9f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is received


### skills/skill-creator/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 49
- **Hard findings:** 43
- **Baseline:** 0
- **Words:** 4775
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **long-sentence** · skills/skill-creator/SKILL.md:3:100 · **new** · fingerprint: cfd51398e7020a0fbdafe7ba
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words

- **long-sentence** · skills/skill-creator/SKILL.md:16:5 · **new** · fingerprint: 67edb283ba2426229ffbdd5b
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **synonym-rotation** · skills/skill-creator/SKILL.md:16:182 · **new** · fingerprint: 6089f9e6b2cd3054930b07d3
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change

- **long-sentence** · skills/skill-creator/SKILL.md:18:3 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · skills/skill-creator/SKILL.md:22:1 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · skills/skill-creator/SKILL.md:22:213 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · skills/skill-creator/SKILL.md:26:1 · **new** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · skills/skill-creator/SKILL.md:28:1 · **new** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **passive-voice** · skills/skill-creator/SKILL.md:28:22 · **new** · fingerprint: 7638fc0a5fbb6cceca5a3ffd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **long-sentence** · skills/skill-creator/SKILL.md:34:105 · **new** · fingerprint: 90b7c0eac3e2ee5b205b348c
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words

- **long-sentence** · skills/skill-creator/SKILL.md:39:3 · **new** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · skills/skill-creator/SKILL.md:41:1 · **new** · fingerprint: b3b51b275e9ef2296ec3dd01
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **synonym-rotation** · skills/skill-creator/SKILL.md:54:35 · **new** · fingerprint: 7a3d7648e3a631037e76cf6d
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · skills/skill-creator/SKILL.md:60:1 · **new** · fingerprint: bd108e08bd9bf096790dc153
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **long-sentence** · skills/skill-creator/SKILL.md:67:398 · **new** · fingerprint: 0a0fc1886c1048efdc236f0b
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **synonym-rotation** · skills/skill-creator/SKILL.md:67:467 · **new** · fingerprint: b5b2e581ff9ad306cac93f39
  - **Level:** advisory-free
  - **Message:** 'display' and 'show' name the same action. Pick one and use it every time.
  - **Matched text:** display

- **long-sentence** · skills/skill-creator/SKILL.md:67:592 · **new** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **long-sentence** · skills/skill-creator/SKILL.md:96:3 · **new** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **semicolon** · skills/skill-creator/SKILL.md:96:32 · **new** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · skills/skill-creator/SKILL.md:171:190 · **new** · fingerprint: c8837f28e78344d9ce3dae88
  - **Level:** advisory-free
  - **Message:** 'launch' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** Launch

- **long-sentence** · skills/skill-creator/SKILL.md:203:1 · **new** · fingerprint: b3b51b275e9ef2296ec3dd01
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · skills/skill-creator/SKILL.md:223:15 · **new** · fingerprint: aa754f9c434238c7ca7024d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are done

- **long-sentence** · skills/skill-creator/SKILL.md:225:386 · **new** · fingerprint: 81a0eb0a3166d8b6ad5e3282
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · skills/skill-creator/SKILL.md:234:106 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **semicolon** · skills/skill-creator/SKILL.md:249:57 · **new** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/skill-creator/SKILL.md:256:29 · **new** · fingerprint: 7f9cc5be406601f9334d0a9f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was given

- **passive-voice** · skills/skill-creator/SKILL.md:259:33 · **new** · fingerprint: 073227ab82a9e051ae64eb07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run

- **present-perfect** · skills/skill-creator/SKILL.md:294:68 · **new** · fingerprint: 39027c43abde57eb08780deb
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has reviewed

- **long-sentence** · skills/skill-creator/SKILL.md:298:38 · **new** · fingerprint: 0a0fc1886c1048efdc236f0b
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **long-sentence** · skills/skill-creator/SKILL.md:298:522 · **new** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · skills/skill-creator/SKILL.md:300:78 · **new** · fingerprint: 5442f1f21a2b76c5f0d49f1a
  - **Level:** advisory-free
  - **Message:** Sentence has 52 words (cap 25). Split it.
  - **Matched text:** 52 words

- **long-sentence** · skills/skill-creator/SKILL.md:302:255 · **new** · fingerprint: 2e7431350f9b2729b3a6b971
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

- **long-sentence** · skills/skill-creator/SKILL.md:302:485 · **new** · fingerprint: bc0db0a6aca974542651f79d
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **long-sentence** · skills/skill-creator/SKILL.md:304:50 · **new** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · skills/skill-creator/SKILL.md:306:138 · **new** · fingerprint: b26e853d0378999b28835ede
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/skill-creator/SKILL.md:313:214 · **new** · fingerprint: 83321e7be691a44356abf397
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · skills/skill-creator/SKILL.md:327:1 · **new** · fingerprint: 285c7910fd39a83bb1401a2b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · skills/skill-creator/SKILL.md:348:429 · **new** · fingerprint: 81a0eb0a3166d8b6ad5e3282
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · skills/skill-creator/SKILL.md:356:1 · **new** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · skills/skill-creator/SKILL.md:356:187 · **new** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **long-sentence** · skills/skill-creator/SKILL.md:394:56 · **new** · fingerprint: cfd51398e7020a0fbdafe7ba
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words

- **long-sentence** · skills/skill-creator/SKILL.md:394:362 · **new** · fingerprint: 50e95484d402557c91868acc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · skills/skill-creator/SKILL.md:398:228 · **new** · fingerprint: 4ba45f4babc708e638969a97
  - **Level:** advisory-free
  - **Message:** Sentence has 47 words (cap 25). Split it.
  - **Matched text:** 47 words

- **long-sentence** · skills/skill-creator/SKILL.md:424:206 · **new** · fingerprint: b7656fbcfb79ae5ac950a8de
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **long-sentence** · skills/skill-creator/SKILL.md:426:264 · **new** · fingerprint: cccbdcfa7cc6ce04982ee106
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **long-sentence** · skills/skill-creator/SKILL.md:451:3 · **new** · fingerprint: b13f3ee36e07d9b3e730917b
  - **Level:** advisory-free
  - **Message:** Sentence has 66 words (cap 25). Split it.
  - **Matched text:** 66 words

- **long-sentence** · skills/skill-creator/SKILL.md:454:3 · **new** · fingerprint: 1a4238764ac29c270955f2ad
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **passive-voice** · skills/skill-creator/SKILL.md:480:33 · **new** · fingerprint: 9b5eb6649d3441bc6d4564c7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **long-sentence** · skills/skill-creator/SKILL.md:483:93 · **new** · fingerprint: 931b8db7add7b3535eb82fe4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words


### skills/theme-factory/themes/sunset-boulevard.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 76
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/define-goal/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 11
- **Hard findings:** 9
- **Baseline:** 0
- **Words:** 857
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **long-sentence** · skills/define-goal/SKILL.md:3:14 · **new** · fingerprint: 3c3b8526ec42c8236337ec34
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **semicolon** · skills/define-goal/SKILL.md:3:303 · **new** · fingerprint: 4b3d24f9aed9b98b70670a67
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/define-goal/SKILL.md:17:6 · **new** · fingerprint: 36d1e3a66695e9ccae667cb7
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **synonym-rotation** · skills/define-goal/SKILL.md:31:41 · **new** · fingerprint: 7ffb6feff2099d48d0f7cbae
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **passive-voice** · skills/define-goal/SKILL.md:39:125 · **new** · fingerprint: 53fe342999b284bfb8bd5229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are sharpened

- **long-sentence** · skills/define-goal/SKILL.md:45:6 · **new** · fingerprint: 36d1e3a66695e9ccae667cb7
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **passive-voice** · skills/define-goal/SKILL.md:58:46 · **new** · fingerprint: 95854f6562674ce44ac99933
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is done

- **long-sentence** · skills/define-goal/SKILL.md:66:3 · **new** · fingerprint: 3c3b8526ec42c8236337ec34
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words

- **synonym-rotation** · skills/define-goal/SKILL.md:66:130 · **new** · fingerprint: d5e7ea11f84d519e58dae002
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **long-sentence** · skills/define-goal/SKILL.md:70:3 · **new** · fingerprint: 02027dda3d9662b4af3db321
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **synonym-rotation** · skills/define-goal/SKILL.md:82:51 · **new** · fingerprint: d10340e745766e580d758131
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix


### skills/skill-creator/references/schemas.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 518
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · skills/skill-creator/references/schemas.md:76:35 · **new** · fingerprint: b2f957f961ac90f2b5e25347
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being improved

- **passive-voice** · skills/skill-creator/references/schemas.md:79:46 · **new** · fingerprint: fc77b5ae02889cc12a032af8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was derived

- **passive-voice** · skills/skill-creator/references/schemas.md:291:37 · **new** · fingerprint: 07fb28aa8827a903ec8ce46f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was run


### skills/migrate-to-rust/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 21
- **Hard findings:** 15
- **Baseline:** 0
- **Words:** 1173
- **Findings per 100 words:** 1.8

#### Complete diagnostics

- **long-sentence** · skills/migrate-to-rust/SKILL.md:7:3 · **new** · fingerprint: a662b736df433f7da92e66fc
  - **Level:** advisory-free
  - **Message:** Sentence has 55 words (cap 25). Split it.
  - **Matched text:** 55 words

- **long-sentence** · skills/migrate-to-rust/SKILL.md:12:57 · **new** · fingerprint: e2295110305762ff8e335a91
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **long-sentence** · skills/migrate-to-rust/SKILL.md:31:5 · **new** · fingerprint: 7028a07f9a3fb5f858d31275
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

- **passive-voice** · skills/migrate-to-rust/SKILL.md:36:5 · **new** · fingerprint: d383e306464baf7b95b09904
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is granted

- **long-sentence** · skills/migrate-to-rust/SKILL.md:37:5 · **new** · fingerprint: b88d92a5c0e5e167cff4ad82
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words

- **long-sentence** · skills/migrate-to-rust/SKILL.md:42:5 · **new** · fingerprint: 78e0abedeafeb317479e2a5b
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:43:26 · **new** · fingerprint: 57d64593c4bd12d2d0efd0ce
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **long-sentence** · skills/migrate-to-rust/SKILL.md:46:45 · **new** · fingerprint: 0d7124ea47427cfe3b990b70
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **passive-voice** · skills/migrate-to-rust/SKILL.md:47:22 · **new** · fingerprint: 467939dfbb29b044552a4f11
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exhausted

- **passive-voice** · skills/migrate-to-rust/SKILL.md:56:40 · **new** · fingerprint: 0bb9a329b75fa24f68895375
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · skills/migrate-to-rust/SKILL.md:60:20 · **new** · fingerprint: 95972905cbdd013afe6ad4d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are measured

- **passive-voice** · skills/migrate-to-rust/SKILL.md:62:73 · **new** · fingerprint: 4f992062ac109aed75870bc0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered

- **long-sentence** · skills/migrate-to-rust/SKILL.md:102:58 · **new** · fingerprint: 4c2241f7419e1cf7fc294279
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · skills/migrate-to-rust/SKILL.md:107:5 · **new** · fingerprint: 3f2ed706861e681ceff6a9f4
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:107:7 · **new** · fingerprint: 1f3f76c2dc2193679fdec0b3
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **long-sentence** · skills/migrate-to-rust/SKILL.md:110:19 · **new** · fingerprint: 0d7124ea47427cfe3b990b70
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · skills/migrate-to-rust/SKILL.md:119:1 · **new** · fingerprint: fbc4aa5d66dc3fafe7ac3cde
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · skills/migrate-to-rust/SKILL.md:155:5 · **new** · fingerprint: 252237a4f0aa1d04ceb61fc9
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · skills/migrate-to-rust/SKILL.md:159:24 · **new** · fingerprint: 88add639cbc69b3d060a35f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reached

- **synonym-rotation** · skills/migrate-to-rust/SKILL.md:169:68 · **new** · fingerprint: 2f192b17ca60a110bed2f049
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **long-sentence** · skills/migrate-to-rust/SKILL.md:176:5 · **new** · fingerprint: fbc4aa5d66dc3fafe7ac3cde
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words


### skills/theme-factory/themes/desert-rose.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 68
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/internal-comms/examples/general-comms.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 85
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **passive-voice** · skills/internal-comms/examples/general-comms.md:2:11 · **new** · fingerprint: f5182f6e401a8e0cd0a281d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked


### skills/skill-creator/agents/comparator.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 735
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · skills/skill-creator/agents/comparator.md:9:15 · **new** · fingerprint: 6c4d2de7a2ac7b8671c78576
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based

- **passive-voice** · skills/skill-creator/agents/comparator.md:17:50 · **new** · fingerprint: fc725ae1310f6770f082b7d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was executed

- **passive-voice** · skills/skill-creator/agents/comparator.md:48:38 · **new** · fingerprint: 1a4e8dde9b444c0c6a259329
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is organized

- **passive-voice** · skills/skill-creator/agents/comparator.md:70:17 · **new** · fingerprint: 06e2447aaf67b0f70bd1d6f4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are provided

- **passive-voice** · skills/skill-creator/agents/comparator.md:172:20 · **new** · fingerprint: 2b87728a994a74cda45b6f17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were provided

- **semicolon** · skills/skill-creator/agents/comparator.md:200:67 · **new** · fingerprint: c0fa64514011ccf40bcaa205
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### skills/migrate-to-rust/references/pgo_and_telemetry_guide.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 13
- **Hard findings:** 10
- **Baseline:** 0
- **Words:** 1274
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:3:1 · **new** · fingerprint: 8941f6e0f48e87a46cae1089
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:49:49 · **new** · fingerprint: 97b200de091b786e8d3ac8e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is isolated

- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:72:5 · **new** · fingerprint: 88e99411d9c8e38d261735a0
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:86:5 · **new** · fingerprint: 4dcee79a954a878bd5a8ea33
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:96:26 · **new** · fingerprint: e95dbe9e5215964e3cded5ab
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:97:34 · **new** · fingerprint: c51b0ce42e3586600dd045b8
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:98:5 · **new** · fingerprint: 613ef8f7b5298e0c6db14dc0
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **long-sentence** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:112:9 · **new** · fingerprint: e95dbe9e5215964e3cded5ab
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **semicolon** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:102 · **new** · fingerprint: 0ec9ec46610bc293be0f4026
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:124:129 · **new** · fingerprint: 0ec9ec46610bc293be0f4026
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:147:28 · **new** · fingerprint: f44a8b2b9d31a4c738017b9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grounded

- **synonym-rotation** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:170:7 · **new** · fingerprint: 48f91bb35f25b0197e2d1854
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirming

- **passive-voice** · skills/migrate-to-rust/references/pgo_and_telemetry_guide.md:220:22 · **new** · fingerprint: c40e0a110415686139157e67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is enforced


### skills/xlsx/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 34
- **Hard findings:** 25
- **Baseline:** 0
- **Words:** 1408
- **Findings per 100 words:** 2.4

#### Complete diagnostics

- **long-sentence** · skills/xlsx/SKILL.md:3:90 · **new** · fingerprint: f01d015c0294a320ea718e21
  - **Level:** advisory-free
  - **Message:** Sentence has 50 words (cap 25). Split it.
  - **Matched text:** 50 words

- **semicolon** · skills/xlsx/SKILL.md:3:297 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/xlsx/SKILL.md:3:363 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/xlsx/SKILL.md:3:406 · **new** · fingerprint: ccb49c9369554c45dc85cff9
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · skills/xlsx/SKILL.md:3:776 · **new** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · skills/xlsx/SKILL.md:3:953 · **new** · fingerprint: d7c3da4cab34766bbeb18c4a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is involved

- **semicolon** · skills/xlsx/SKILL.md:13:80 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/xlsx/SKILL.md:16:42 · **new** · fingerprint: 2c1023f6d06e7f043fe8aae6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preinstalled

- **semicolon** · skills/xlsx/SKILL.md:16:91 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/xlsx/SKILL.md:23:79 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/xlsx/SKILL.md:26:246 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/xlsx/SKILL.md:27:3 · **new** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · skills/xlsx/SKILL.md:27:207 · **new** · fingerprint: f3aa2c4d7e06ebf371e77816
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were asked

- **long-sentence** · skills/xlsx/SKILL.md:40:1 · **new** · fingerprint: 011da665a0c2ff74a6b74755
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words

- **long-sentence** · skills/xlsx/SKILL.md:44:8 · **new** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · skills/xlsx/SKILL.md:44:71 · **new** · fingerprint: 189dece9ba87f307d9a452d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was recalculated

- **semicolon** · skills/xlsx/SKILL.md:55:40 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/xlsx/SKILL.md:58:80 · **new** · fingerprint: 036f999f6b29928b3dbfe0a2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed

- **long-sentence** · skills/xlsx/SKILL.md:66:3 · **new** · fingerprint: 2c5761d0e7f57eb14fa5f2f4
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **long-sentence** · skills/xlsx/SKILL.md:67:81 · **new** · fingerprint: eaf247ebd4907c600853b68a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · skills/xlsx/SKILL.md:68:17 · **new** · fingerprint: afb595bdfd38499714786a9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reported

- **synonym-rotation** · skills/xlsx/SKILL.md:68:148 · **new** · fingerprint: 78a832da081777bd2e464819
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **semicolon** · skills/xlsx/SKILL.md:72:100 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/xlsx/SKILL.md:75:116 · **new** · fingerprint: f474913920113893681a698c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **semicolon** · skills/xlsx/SKILL.md:78:160 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/xlsx/SKILL.md:79:3 · **new** · fingerprint: aad8f9ccd5b6288ae3de1a6f
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **passive-voice** · skills/xlsx/SKILL.md:79:167 · **new** · fingerprint: ef7c6ddf0f899365fab978af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are saved

- **passive-voice** · skills/xlsx/SKILL.md:80:37 · **new** · fingerprint: 115b0065fd7574ef88e08839
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is flattened

- **semicolon** · skills/xlsx/SKILL.md:80:90 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/xlsx/SKILL.md:82:3 · **new** · fingerprint: dad26d2d8ae1bd2000776a97
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words

- **long-sentence** · skills/xlsx/SKILL.md:89:1 · **new** · fingerprint: 34d7440bbd271044262654bf
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **long-sentence** · skills/xlsx/SKILL.md:93:1 · **new** · fingerprint: ccb49c9369554c45dc85cff9
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **semicolon** · skills/xlsx/SKILL.md:95:68 · **new** · fingerprint: 809718d1498aea4fb5551b4b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/xlsx/SKILL.md:98:1 · **new** · fingerprint: 3c6294d2724d449d03904c6d
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words


### skills/pdf/REFERENCE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 394
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
