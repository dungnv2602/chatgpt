# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#645](https://github.com/dungnv2602/chatgpt/actions/runs/45431116555)
- **Run ID / attempt:** 45431116555 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / f3ffc8590cd01ca6eaf26ff25f7f08d32f2b4c76
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** f3d11e25cdcc4335102725e51a5e4a20d1921753
- **Linter source SHA:** f3ffc8590cd01ca6eaf26ff25f7f08d32f2b4c76
- **Generated (UTC):** 2026-11-24T15:57:19.215118+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 2 |
| Files with findings | 3 |
| Total findings | 41 |
| Hard findings | 16 |
| Advisory findings | 25 |
| New findings | 41 |
| Recurring findings | 0 |
| Resolved findings | 5 |
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
- workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/task_board.md | PASS | 4 | 0 | 0 | 1210 | 0.3 | 0 |
| workspace/draft/README.md | FAIL | 1 | 1 | 0 | 345 | 0.3 | 1 |
| workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md | FAIL | 36 | 15 | 0 | 3082 | 1.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 22 |
| semicolon | 8 |
| long-sentence | 4 |
| synonym-rotation | 4 |
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
Ran 4 tests in 0.252s

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

- **passive-voice** · workspace/task_board.md:7:110 · **new** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/task_board.md:7:137 · **new** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · workspace/task_board.md:7:162 · **new** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/task_board.md:11:31 · **new** · fingerprint: ed2247bc287f94142d470682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected
- **semicolon** · workspace/draft/README.md:13:213 · **new** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:23:255 · **new** · fingerprint: b2db79571b0fd793f16cfc6e
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:23:261 · **new** · fingerprint: f33785399ee477f140c53be5
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:27:74 · **new** · fingerprint: 682e7a3c6258df9314cac8ab
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:38:154 · **new** · fingerprint: 417028a1c6ce0cd86f44b467
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has clarified
- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:40:229 · **new** · fingerprint: 8a7eac590ca1275b3cbb1898
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:42:64 · **new** · fingerprint: e393f743a72abc7c888f6cec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:55:41 · **new** · fingerprint: c447d529f7b20b4590b587f7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:86:39 · **new** · fingerprint: 0b579768d40496de9c52eb18
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:90:52 · **new** · fingerprint: c447d529f7b20b4590b587f7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:99:16 · **new** · fingerprint: dd3e21d877e9a2d231775f40
  - **Level:** advisory-free
  - **Message:** 'verify' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:138:90 · **new** · fingerprint: 74b25e7a1f97c63191134119
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has passed
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:151:27 · **new** · fingerprint: b9a84ebe6dcce03f0dc6bba8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were considered
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:168:50 · **new** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:170:3 · **new** · fingerprint: 88383bbb9edb4a64f57b4f5d
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:176:127 · **new** · fingerprint: 60f3249b1cd98b7bfc324e27
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:179:14 · **new** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:179:85 · **new** · fingerprint: e3f45e1c3ad0739bdf1dd4df
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:197:19 · **new** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:205:21 · **new** · fingerprint: e393f743a72abc7c888f6cec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:206:58 · **new** · fingerprint: dbf3d2cb4647779b785af24a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:208:51 · **new** · fingerprint: 9ddf121d6af934b7f894ee93
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:217:77 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:217:122 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:220:83 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:222:91 · **new** · fingerprint: 5adb2f8b4d0fd44cce39c150
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retired
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:223:80 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:234:102 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:237:63 · **new** · fingerprint: 4d6943b3cf48f72f6c117611
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scheduled
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:243:24 · **new** · fingerprint: d7ce4a873457263c7e94b520
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:262:9 · **new** · fingerprint: 98c2fc965a4ebb8e335136f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:264:97 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:265:13 · **new** · fingerprint: ce34144ae929301d185371c6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:266:33 · **new** · fingerprint: 98c2fc965a4ebb8e335136f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:287:4 · **new** · fingerprint: 12e588d9bbad646077be3159
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:301:285 · **new** · fingerprint: 3d55bac6a43511c9d51dfea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was prepared
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:302:159 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Recurring findings

None.

### Resolved findings

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:353:4 · **resolved** · fingerprint: b12cf7b98114051a3ef4ed4e
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:550:52 · **resolved** · fingerprint: 331ead622bd8b63c3dc8ec78
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:553:4 · **resolved** · fingerprint: 26959e3895827a98ea573e44
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:587:20 · **resolved** · fingerprint: 33dd6d895441c53e43bd10a2
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:602:90 · **resolved** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 4
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1210
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:7:110 · **new** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/task_board.md:7:137 · **new** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded

- **passive-voice** · workspace/task_board.md:7:162 · **new** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · workspace/task_board.md:11:31 · **new** · fingerprint: ed2247bc287f94142d470682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected


### workspace/draft/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 345
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · workspace/draft/README.md:13:213 · **new** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 36
- **Hard findings:** 15
- **Baseline:** 0
- **Words:** 3082
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:23:255 · **new** · fingerprint: b2db79571b0fd793f16cfc6e
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:23:261 · **new** · fingerprint: f33785399ee477f140c53be5
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** confirms

- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:27:74 · **new** · fingerprint: 682e7a3c6258df9314cac8ab
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:38:154 · **new** · fingerprint: 417028a1c6ce0cd86f44b467
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has clarified

- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:40:229 · **new** · fingerprint: 8a7eac590ca1275b3cbb1898
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:42:64 · **new** · fingerprint: e393f743a72abc7c888f6cec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:55:41 · **new** · fingerprint: c447d529f7b20b4590b587f7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:86:39 · **new** · fingerprint: 0b579768d40496de9c52eb18
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:90:52 · **new** · fingerprint: c447d529f7b20b4590b587f7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:99:16 · **new** · fingerprint: dd3e21d877e9a2d231775f40
  - **Level:** advisory-free
  - **Message:** 'verify' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:138:90 · **new** · fingerprint: 74b25e7a1f97c63191134119
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has passed

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:151:27 · **new** · fingerprint: b9a84ebe6dcce03f0dc6bba8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were considered

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:168:50 · **new** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:170:3 · **new** · fingerprint: 88383bbb9edb4a64f57b4f5d
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:176:127 · **new** · fingerprint: 60f3249b1cd98b7bfc324e27
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:179:14 · **new** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:179:85 · **new** · fingerprint: e3f45e1c3ad0739bdf1dd4df
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:197:19 · **new** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:205:21 · **new** · fingerprint: e393f743a72abc7c888f6cec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:206:58 · **new** · fingerprint: dbf3d2cb4647779b785af24a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:208:51 · **new** · fingerprint: 9ddf121d6af934b7f894ee93
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed

- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:217:77 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:217:122 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:220:83 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:222:91 · **new** · fingerprint: 5adb2f8b4d0fd44cce39c150
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retired

- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:223:80 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:234:102 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:237:63 · **new** · fingerprint: 4d6943b3cf48f72f6c117611
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scheduled

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:243:24 · **new** · fingerprint: d7ce4a873457263c7e94b520
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:262:9 · **new** · fingerprint: 98c2fc965a4ebb8e335136f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:264:97 · **new** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:265:13 · **new** · fingerprint: ce34144ae929301d185371c6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:266:33 · **new** · fingerprint: 98c2fc965a4ebb8e335136f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:287:4 · **new** · fingerprint: 12e588d9bbad646077be3159
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:301:285 · **new** · fingerprint: 3d55bac6a43511c9d51dfea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was prepared

- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:302:159 · **new** · fingerprint: 04c9ac442f56ef3b58400722
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
