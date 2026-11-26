# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#603](https://github.com/dungnv2602/chatgpt/actions/runs/45386030748)
- **Run ID / attempt:** 45386030748 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 31bb58dfe0d7acd5914b7b34ee8b41464f0658ee
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 8adc48d1be4d4d659fba028d7cea8e76ddd9c9d9
- **Linter source SHA:** 31bb58dfe0d7acd5914b7b34ee8b41464f0658ee
- **Generated (UTC):** 2026-11-24T11:40:26.558806+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 1 |
| Files with findings | 2 |
| Total findings | 18 |
| Hard findings | 2 |
| Advisory findings | 16 |
| New findings | 15 |
| Recurring findings | 3 |
| Resolved findings | 28 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/task_board.md
- workspace/draft/README.md
- workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/task_board.md | PASS | 3 | 0 | 0 | 890 | 0.3 | 0 |
| workspace/draft/README.md | PASS | 0 | 0 | 0 | 321 | 0.0 | 0 |
| workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md | FAIL | 15 | 2 | 0 | 4727 | 0.3 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 14 |
| present-perfect | 2 |
| synonym-rotation | 2 |

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
Ran 4 tests in 0.234s

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

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:119:62 · **new** · fingerprint: 5acc357959587a68b0f951b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:223:48 · **new** · fingerprint: 3c71bd1ac16f45619f5466ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preferred
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:227:233 · **new** · fingerprint: 89ce3d95585eee314fa93cfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:296:167 · **new** · fingerprint: 3a3155bef6ccfb4a15af4609
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:306:67 · **new** · fingerprint: f9a394a8cb93eb454dfa7f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are displaced
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:344:71 · **new** · fingerprint: e73135d93a51902c9fd106d5
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:364:16 · **new** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:365:8 · **new** · fingerprint: 7d8c8c30ca8b7156c5fd20d6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been learned
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:365:12 · **new** · fingerprint: 5edc8896dd1191aed01bae09
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been learned
- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:366:13 · **new** · fingerprint: e0f4e715b1c053931ad979c7
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has occurred
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:446:99 · **new** · fingerprint: bbc02b6745dfaa6a298be3af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:461:87 · **new** · fingerprint: 2de665cea398a7c3f0984efd
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:469:11 · **new** · fingerprint: f0baecd36560346eb7c99c71
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:507:112 · **new** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:524:116 · **new** · fingerprint: f361f0da8e025b2ad8e4e144
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

### Recurring findings

- **passive-voice** · workspace/task_board.md:7:110 · **recurring** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/task_board.md:7:137 · **recurring** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · workspace/task_board.md:7:162 · **recurring** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

### Resolved findings

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
- **synonym-rotation** · skills/the-worker/SKILL.md:360:182 · **resolved** · fingerprint: 0564bcc241576c15bb1f3427
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 890
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:7:110 · **recurring** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/task_board.md:7:137 · **recurring** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded

- **passive-voice** · workspace/task_board.md:7:162 · **recurring** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved


### workspace/draft/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 321
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 15
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 4727
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:119:62 · **new** · fingerprint: 5acc357959587a68b0f951b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:223:48 · **new** · fingerprint: 3c71bd1ac16f45619f5466ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preferred

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:227:233 · **new** · fingerprint: 89ce3d95585eee314fa93cfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:296:167 · **new** · fingerprint: 3a3155bef6ccfb4a15af4609
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:306:67 · **new** · fingerprint: f9a394a8cb93eb454dfa7f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are displaced

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:344:71 · **new** · fingerprint: e73135d93a51902c9fd106d5
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:364:16 · **new** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:365:8 · **new** · fingerprint: 7d8c8c30ca8b7156c5fd20d6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been learned

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:365:12 · **new** · fingerprint: 5edc8896dd1191aed01bae09
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been learned

- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:366:13 · **new** · fingerprint: e0f4e715b1c053931ad979c7
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has occurred

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:446:99 · **new** · fingerprint: bbc02b6745dfaa6a298be3af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:461:87 · **new** · fingerprint: 2de665cea398a7c3f0984efd
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:469:11 · **new** · fingerprint: f0baecd36560346eb7c99c71
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:507:112 · **new** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:524:116 · **new** · fingerprint: f361f0da8e025b2ad8e4e144
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
