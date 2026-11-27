# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#811](https://github.com/dungnv2602/chatgpt/actions/runs/45840589283)
- **Run ID / attempt:** 45840589283 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 03cd9983a483d8763eae98269e6c22c210b94898
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 6499c1ec65de33e1376671531ea770c5098e53b3
- **Linter source SHA:** 03cd9983a483d8763eae98269e6c22c210b94898
- **Generated (UTC):** 2026-11-26T14:37:29.792977+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 3 |
| Files with findings | 3 |
| Total findings | 6 |
| Hard findings | 5 |
| Advisory findings | 1 |
| New findings | 5 |
| Recurring findings | 1 |
| Resolved findings | 74 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
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
| workspace/task_board.md | FAIL | 1 | 1 | 0 | 362 | 0.3 | 1 |
| workspace/draft/README.md | FAIL | 4 | 3 | 0 | 666 | 0.6 | 1 |
| workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md | FAIL | 1 | 1 | 0 | 9080 | 0.0 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| semicolon | 2 |
| synonym-rotation | 2 |
| long-sentence | 1 |
| passive-voice | 1 |

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
Ran 4 tests in 0.317s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.016s

OK
~~~

### STE linter self-test

- **Result:** Passed
- **Exit code:** 0

~~~text
selftest OK
~~~

### Markdown links and heading anchors

- **Result:** Passed
- **Exit code:** 0

~~~text
Scanned 3 changed Markdown sources (321 available as link targets) and 18 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · workspace/task_board.md:26:61 · **new** · fingerprint: fe0043dd1c2c55650b8f76ae
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
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

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:216:73 · **recurring** · fingerprint: 5c822b17641bfca685187467
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validate

### Resolved findings

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:25:10 · **resolved** · fingerprint: a2ab275c6b77dd5fee04cc69
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:25:236 · **resolved** · fingerprint: f361f0da8e025b2ad8e4e144
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:27:293 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:43:292 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:43:342 · **resolved** · fingerprint: a909a403a059d36f26caf607
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are unchanged
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:45:452 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:118:13 · **resolved** · fingerprint: 2622327c5814c036cce375d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are assessed
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:127:277 · **resolved** · fingerprint: 5fbc17194b22ffad4280c0ef
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supported
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:131:1 · **resolved** · fingerprint: fef6e60a628c50ea5557879f
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:135:123 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:141:432 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:149:130 · **resolved** · fingerprint: 5acc357959587a68b0f951b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:151:133 · **resolved** · fingerprint: ff6c3acd0c014dc4e61c466a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:154:130 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:3 · **resolved** · fingerprint: f7dc64f1259416e941602253
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:153 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:195 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:166:216 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:172:17 · **resolved** · fingerprint: 6e0df3ac815fc5850205b430
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has evolved
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:177:5 · **resolved** · fingerprint: 88aeab811894156e381b6f38
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:45 · **resolved** · fingerprint: e8137e2bbd27eeeebe09cefe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are gitignored
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:72 · **resolved** · fingerprint: f82bfd9e6673b647a6d8fc2d
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:182:278 · **resolved** · fingerprint: 2879617005bdf3d23fcdebce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:186:131 · **resolved** · fingerprint: 88aeab811894156e381b6f38
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:186:552 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:187:3 · **resolved** · fingerprint: 0f7475f061de95d077b1bfe9
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:195:90 · **resolved** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:206:112 · **resolved** · fingerprint: d322aeaf54a910f1b652245b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is missed
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:207:165 · **resolved** · fingerprint: f0d61be6ac280ec407b4f93b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reconciled
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:209:5 · **resolved** · fingerprint: fef6e60a628c50ea5557879f
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:211:311 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:211:342 · **resolved** · fingerprint: 77adbdbc0fe812d1b67b5e05
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are intended
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:223:85 · **resolved** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:231:5 · **resolved** · fingerprint: f82bfd9e6673b647a6d8fc2d
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:232:3 · **resolved** · fingerprint: 3dd65725c765cdc8c75ee04a
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:241:81 · **resolved** · fingerprint: a7bf89e39efdb719560ebf21
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is redesigned
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:244:107 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:267:114 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:268:69 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:281:139 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:283:84 · **resolved** · fingerprint: ff6c3acd0c014dc4e61c466a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:320:246 · **resolved** · fingerprint: 89ce3d95585eee314fa93cfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:326:391 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:338:117 · **resolved** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:338:187 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:383:179 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:463:1 · **resolved** · fingerprint: 2b8b751eaf86badac01b9e00
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:469:245 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:515:142 · **resolved** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:516:107 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:517:145 · **resolved** · fingerprint: e4c84bbce7e4e015e5f82803
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:528:134 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:528:168 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:530:11 · **resolved** · fingerprint: f0baecd36560346eb7c99c71
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:18 · **resolved** · fingerprint: e7603e373d761a7c9ff25aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:104 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:126 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:533:157 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:537:20 · **resolved** · fingerprint: e796b5d39f657c7dbfca408d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is treated
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:539:30 · **resolved** · fingerprint: 45700ec28d246ad5f6098f6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are treated
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:554:32 · **resolved** · fingerprint: 70781a8fa973c1554931c214
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:612:52 · **resolved** · fingerprint: 331ead622bd8b63c3dc8ec78
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:615:4 · **resolved** · fingerprint: 26959e3895827a98ea573e44
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:632:4 · **resolved** · fingerprint: cb5ac6fb2c2c270ac73b57e0
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:633:145 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:634:4 · **resolved** · fingerprint: c3aa5dc7d8225bd81a86e1b5
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:649:20 · **resolved** · fingerprint: 33dd6d895441c53e43bd10a2
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:20 · **resolved** · fingerprint: 0f7475f061de95d077b1bfe9
  - **Level:** advisory-free
  - **Message:** Sentence has 38 words (cap 25). Split it.
  - **Matched text:** 38 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:56 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:112 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:152 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:204 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:650:250 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:665:90 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 362
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:26:61 · **new** · fingerprint: fe0043dd1c2c55650b8f76ae
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate


### workspace/draft/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 666
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


### workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 9080
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:216:73 · **recurring** · fingerprint: 5c822b17641bfca685187467
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validate

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
