# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#604](https://github.com/dungnv2602/chatgpt/actions/runs/45395353908)
- **Run ID / attempt:** 45395353908 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 241ba8ad5e4aa7cff683ecf49df31c0ad11945ef
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 31bb58dfe0d7acd5914b7b34ee8b41464f0658ee
- **Linter source SHA:** 241ba8ad5e4aa7cff683ecf49df31c0ad11945ef
- **Generated (UTC):** 2026-11-24T12:38:26.660336+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 6 |
| Files that failed | 3 |
| Files with findings | 5 |
| Total findings | 37 |
| Hard findings | 14 |
| Advisory findings | 23 |
| New findings | 34 |
| Recurring findings | 3 |
| Resolved findings | 15 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/README.md
- workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md
- workspace/task_board.md
- workspace/draft/README.md
- workspace/README.md
- workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/README.md | PASS | 1 | 0 | 0 | 387 | 0.3 | 0 |
| workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md | FAIL | 19 | 7 | 0 | 3360 | 0.6 | 1 |
| workspace/task_board.md | FAIL | 5 | 2 | 0 | 1570 | 0.3 | 1 |
| workspace/draft/README.md | PASS | 0 | 0 | 0 | 333 | 0.0 | 0 |
| workspace/README.md | FAIL | 9 | 5 | 0 | 750 | 1.2 | 1 |
| workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md | PASS | 3 | 0 | 0 | 1129 | 0.3 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 21 |
| synonym-rotation | 7 |
| long-sentence | 5 |
| present-perfect | 2 |
| semicolon | 2 |

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
Ran 4 tests in 0.225s

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

- **passive-voice** · workspace/adr/README.md:54:38 · **new** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:40:64 · **new** · fingerprint: 04ec4f5fbb130c1324f44f00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:81:41 · **new** · fingerprint: 5d7ba294a41810bbc4f7a8fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made
- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:177:31 · **new** · fingerprint: 015ecb389e532dd8875c1837
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has presented
- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:178:34 · **new** · fingerprint: 0f4521e8c2b440c5ef392f4b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has requested
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:180:23 · **new** · fingerprint: 852ed94029abbea4e6fab0f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:201:14 · **new** · fingerprint: 8d81ddd804dfe2c99c883b3e
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:217:237 · **new** · fingerprint: 4c95c42ba0a8e33df95da64d
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:269:158 · **new** · fingerprint: a317f5b19e2ab5d770d78d2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grandfathered
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:275:55 · **new** · fingerprint: 54ced16a4522c38f24c053a6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was implemented
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:277:21 · **new** · fingerprint: 469e1521575230ced366ea79
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:279:38 · **new** · fingerprint: 21fa99cd9adb2127f01fc204
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:281:132 · **new** · fingerprint: 101211397f76806715447ab0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:285:85 · **new** · fingerprint: befabfa16e1d11b4cc317bc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:295:42 · **new** · fingerprint: 063bc6652b2f8cba7e22ed0d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:303:59 · **new** · fingerprint: 8ab2123627f631a8c49701db
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fixed
- **long-sentence** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:333:3 · **new** · fingerprint: 8bf6c58f1f0bd3c79519cfd1
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:355:45 · **new** · fingerprint: 7a97a9361b4bcc774d6f0ab9
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:372:95 · **new** · fingerprint: e1b81119b147b4cb2485bf75
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:402:17 · **new** · fingerprint: 396aabeca89bdc013b3dc544
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **long-sentence** · workspace/task_board.md:33:1 · **new** · fingerprint: 92ec83b350b615bdf683ddd6
  - **Level:** advisory-free
  - **Message:** Sentence has 646 words (cap 25). Split it.
  - **Matched text:** 646 words
- **long-sentence** · workspace/task_board.md:94:1 · **new** · fingerprint: 57773ee1e8cfcfbc4aa600df
  - **Level:** advisory-free
  - **Message:** Sentence has 128 words (cap 25). Split it.
  - **Matched text:** 128 words
- **semicolon** · workspace/README.md:33:113 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/README.md:37:4 · **new** · fingerprint: 850ad36627f5885d916de296
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · workspace/README.md:37:64 · **new** · fingerprint: f9374751a535ad58835e814f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **passive-voice** · workspace/README.md:37:110 · **new** · fingerprint: 28231427e3d00c582576f2b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is updated
- **passive-voice** · workspace/README.md:37:140 · **new** · fingerprint: 6e067aa5c3c536cd323a5c6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **passive-voice** · workspace/README.md:49:108 · **new** · fingerprint: 4a500644b11ea45e7a256ac0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **synonym-rotation** · workspace/README.md:49:364 · **new** · fingerprint: 01eb48b1e6acd03619987cff
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **long-sentence** · workspace/README.md:53:139 · **new** · fingerprint: a222143dea70fba6ab12863a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/README.md:53:223 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:34:64 · **new** · fingerprint: fbe6150d9b5e8dab3b1e43a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:47:41 · **new** · fingerprint: 8d3ad3a1e3838d879ee9b85a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:111:44 · **new** · fingerprint: e871aaaf906a610ac0db5605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are implemented

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

- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:119:62 · **resolved** · fingerprint: 5acc357959587a68b0f951b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are required
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:223:48 · **resolved** · fingerprint: 3c71bd1ac16f45619f5466ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preferred
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:227:233 · **resolved** · fingerprint: 89ce3d95585eee314fa93cfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:296:167 · **resolved** · fingerprint: 3a3155bef6ccfb4a15af4609
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:306:67 · **resolved** · fingerprint: f9a394a8cb93eb454dfa7f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are displaced
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:344:71 · **resolved** · fingerprint: e73135d93a51902c9fd106d5
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:364:16 · **resolved** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:365:8 · **resolved** · fingerprint: 7d8c8c30ca8b7156c5fd20d6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been learned
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:365:12 · **resolved** · fingerprint: 5edc8896dd1191aed01bae09
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been learned
- **present-perfect** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:366:13 · **resolved** · fingerprint: e0f4e715b1c053931ad979c7
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has occurred
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:446:99 · **resolved** · fingerprint: bbc02b6745dfaa6a298be3af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:461:87 · **resolved** · fingerprint: 2de665cea398a7c3f0984efd
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:469:11 · **resolved** · fingerprint: f0baecd36560346eb7c99c71
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:507:112 · **resolved** · fingerprint: bb1c50eaa631694d123a7701
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:524:116 · **resolved** · fingerprint: f361f0da8e025b2ad8e4e144
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 387
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/adr/README.md:54:38 · **new** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done


### workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 19
- **Hard findings:** 7
- **Baseline:** 0
- **Words:** 3360
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:40:64 · **new** · fingerprint: 04ec4f5fbb130c1324f44f00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:81:41 · **new** · fingerprint: 5d7ba294a41810bbc4f7a8fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made

- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:177:31 · **new** · fingerprint: 015ecb389e532dd8875c1837
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has presented

- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:178:34 · **new** · fingerprint: 0f4521e8c2b440c5ef392f4b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has requested

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:180:23 · **new** · fingerprint: 852ed94029abbea4e6fab0f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:201:14 · **new** · fingerprint: 8d81ddd804dfe2c99c883b3e
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:217:237 · **new** · fingerprint: 4c95c42ba0a8e33df95da64d
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:269:158 · **new** · fingerprint: a317f5b19e2ab5d770d78d2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grandfathered

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:275:55 · **new** · fingerprint: 54ced16a4522c38f24c053a6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was implemented

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:277:21 · **new** · fingerprint: 469e1521575230ced366ea79
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:279:38 · **new** · fingerprint: 21fa99cd9adb2127f01fc204
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:281:132 · **new** · fingerprint: 101211397f76806715447ab0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:285:85 · **new** · fingerprint: befabfa16e1d11b4cc317bc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:295:42 · **new** · fingerprint: 063bc6652b2f8cba7e22ed0d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:303:59 · **new** · fingerprint: 8ab2123627f631a8c49701db
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fixed

- **long-sentence** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:333:3 · **new** · fingerprint: 8bf6c58f1f0bd3c79519cfd1
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:355:45 · **new** · fingerprint: 7a97a9361b4bcc774d6f0ab9
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:372:95 · **new** · fingerprint: e1b81119b147b4cb2485bf75
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:402:17 · **new** · fingerprint: 396aabeca89bdc013b3dc544
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 5
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1570
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

- **long-sentence** · workspace/task_board.md:33:1 · **new** · fingerprint: 92ec83b350b615bdf683ddd6
  - **Level:** advisory-free
  - **Message:** Sentence has 646 words (cap 25). Split it.
  - **Matched text:** 646 words

- **long-sentence** · workspace/task_board.md:94:1 · **new** · fingerprint: 57773ee1e8cfcfbc4aa600df
  - **Level:** advisory-free
  - **Message:** Sentence has 128 words (cap 25). Split it.
  - **Matched text:** 128 words


### workspace/draft/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 333
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 750
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **semicolon** · workspace/README.md:33:113 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/README.md:37:4 · **new** · fingerprint: 850ad36627f5885d916de296
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **passive-voice** · workspace/README.md:37:64 · **new** · fingerprint: f9374751a535ad58835e814f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **passive-voice** · workspace/README.md:37:110 · **new** · fingerprint: 28231427e3d00c582576f2b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is updated

- **passive-voice** · workspace/README.md:37:140 · **new** · fingerprint: 6e067aa5c3c536cd323a5c6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed

- **passive-voice** · workspace/README.md:49:108 · **new** · fingerprint: 4a500644b11ea45e7a256ac0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **synonym-rotation** · workspace/README.md:49:364 · **new** · fingerprint: 01eb48b1e6acd03619987cff
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

- **long-sentence** · workspace/README.md:53:139 · **new** · fingerprint: a222143dea70fba6ab12863a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/README.md:53:223 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1129
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:34:64 · **new** · fingerprint: fbe6150d9b5e8dab3b1e43a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:47:41 · **new** · fingerprint: 8d3ad3a1e3838d879ee9b85a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:111:44 · **new** · fingerprint: e871aaaf906a610ac0db5605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are implemented

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
