# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#667](https://github.com/dungnv2602/chatgpt/actions/runs/45442492124)
- **Run ID / attempt:** 45442492124 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / b4f01ecb336fdc3174039a9c014229e44f7aad6d
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 80e67808c0b97fbd4f1e69896c806b2145316d7c
- **Linter source SHA:** b4f01ecb336fdc3174039a9c014229e44f7aad6d
- **Generated (UTC):** 2026-11-24T16:57:00.938432+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 4 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 2 |
| Hard findings | 2 |
| Advisory findings | 0 |
| New findings | 1 |
| Recurring findings | 1 |
| Resolved findings | 49 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- skills/decision-governance/SKILL.md
- skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md
- workspace/README.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| skills/decision-governance/SKILL.md | FAIL | 1 | 1 | 0 | 2203 | 0.0 | 1 |
| skills/document-standards/references/document-type-catalog.md | PASS | 0 | 0 | 0 | 4373 | 0.0 | 0 |
| workspace/task_board.md | PASS | 0 | 0 | 0 | 1448 | 0.0 | 0 |
| workspace/README.md | FAIL | 1 | 1 | 0 | 886 | 0.1 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
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
Ran 4 tests in 0.243s

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

- **synonym-rotation** · skills/decision-governance/SKILL.md:95:35 · **new** · fingerprint: a894730c426b5a08cb0d4e4c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check

### Recurring findings

- **synonym-rotation** · workspace/README.md:58:376 · **recurring** · fingerprint: 3659e4816d32f3f6e196b772
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

### Resolved findings

- **synonym-rotation** · skills/decision-governance/SKILL.md:63:90 · **resolved** · fingerprint: 2624698c9e0a949a01e1c0be
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **synonym-rotation** · skills/decision-governance/SKILL.md:142:28 · **resolved** · fingerprint: 4b2ab07116317a3363e3cd06
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:45:159 · **resolved** · fingerprint: ee3dcb468a833bb24e5822bc
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:46:331 · **resolved** · fingerprint: 7de3890b6aa2dea92c057735
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/task_board.md:137:65 · **resolved** · fingerprint: 2e2ac820f2b2ecba84ec2b97
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **present-perfect** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:261 · **resolved** · fingerprint: dc863a59620ce525978fa30c
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:265 · **resolved** · fingerprint: 17a4d086602b381ce65c59f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:43:257 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:44:3 · **resolved** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:3 · **resolved** · fingerprint: 5234929a399cf01e0d7f595c
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:129 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:153 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:185 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:207 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:53:80 · **resolved** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:80:16 · **resolved** · fingerprint: 2b26cf53803b151c21212120
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:1 · **resolved** · fingerprint: b394b51b09ad308cc8feeae3
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:179 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:116:72 · **resolved** · fingerprint: f7c21f7d8940f28c70370284
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:117:114 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:120:175 · **resolved** · fingerprint: 44fcd3dad59ced40bc859413
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:121:203 · **resolved** · fingerprint: 45a08d05aee0fa7834e7cd1d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:151:44 · **resolved** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:153:3 · **resolved** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:159:127 · **resolved** · fingerprint: beb9ea53ee058f3d9e59ec0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:14 · **resolved** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:88 · **resolved** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:188:70 · **resolved** · fingerprint: 15acf5b3ddc984f62af012a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:189:56 · **resolved** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:191:51 · **resolved** · fingerprint: 51cadbdd6b8eb0498821f9bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:210:9 · **resolved** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:212:94 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:213:7 · **resolved** · fingerprint: 33b3ff5444bee044b23c7ce9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:214:33 · **resolved** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:3 · **resolved** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:69 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:94 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:133 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:169 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:207 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:222:186 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:97 · **resolved** · fingerprint: 03a989d439e11fa4326ad6bc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:134 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:228:125 · **resolved** · fingerprint: 36e134bec11bbd982d0e34fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:38 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:61 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:71 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:104 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:131 · **resolved** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### skills/decision-governance/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 2203
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **synonym-rotation** · skills/decision-governance/SKILL.md:95:35 · **new** · fingerprint: a894730c426b5a08cb0d4e4c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check


### skills/document-standards/references/document-type-catalog.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 4373
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1448
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 886
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/README.md:58:376 · **recurring** · fingerprint: 3659e4816d32f3f6e196b772
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
