# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#670](https://github.com/dungnv2602/chatgpt/actions/runs/45447915270)
- **Run ID / attempt:** 45447915270 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / f150a5b5bc7f5eeaee922e85106564e78e10ffe3
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 4b8af56f38824e6b712447a54255d087ae37811e
- **Linter source SHA:** f150a5b5bc7f5eeaee922e85106564e78e10ffe3
- **Generated (UTC):** 2026-11-24T17:23:31.876476+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 45 |
| Hard findings | 31 |
| Advisory findings | 14 |
| New findings | 45 |
| Recurring findings | 0 |
| Resolved findings | 0 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md | FAIL | 45 | 31 | 0 | 2691 | 1.7 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| semicolon | 21 |
| passive-voice | 13 |
| long-sentence | 5 |
| synonym-rotation | 5 |
| present-perfect | 1 |

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
Ran 4 tests in 0.297s

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

- **present-perfect** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:261 · **new** · fingerprint: dc863a59620ce525978fa30c
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:265 · **new** · fingerprint: 17a4d086602b381ce65c59f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:43:257 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:44:3 · **new** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:3 · **new** · fingerprint: 5234929a399cf01e0d7f595c
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:129 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:153 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:185 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:207 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:53:80 · **new** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:80:16 · **new** · fingerprint: 2b26cf53803b151c21212120
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:1 · **new** · fingerprint: b394b51b09ad308cc8feeae3
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:179 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:116:72 · **new** · fingerprint: f7c21f7d8940f28c70370284
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:117:114 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:120:175 · **new** · fingerprint: 44fcd3dad59ced40bc859413
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:121:203 · **new** · fingerprint: 45a08d05aee0fa7834e7cd1d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:151:44 · **new** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:153:3 · **new** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:159:127 · **new** · fingerprint: beb9ea53ee058f3d9e59ec0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:14 · **new** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:88 · **new** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:188:70 · **new** · fingerprint: 15acf5b3ddc984f62af012a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:189:56 · **new** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:191:51 · **new** · fingerprint: 51cadbdd6b8eb0498821f9bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:210:9 · **new** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:212:94 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:213:7 · **new** · fingerprint: 33b3ff5444bee044b23c7ce9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:214:33 · **new** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:3 · **new** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:69 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:94 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:133 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:169 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:207 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:222:186 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:97 · **new** · fingerprint: 03a989d439e11fa4326ad6bc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:134 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:228:125 · **new** · fingerprint: 36e134bec11bbd982d0e34fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:38 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:61 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:71 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:104 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:131 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:251:377 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Recurring findings

None.

### Resolved findings

None.

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 45
- **Hard findings:** 31
- **Baseline:** 0
- **Words:** 2691
- **Findings per 100 words:** 1.7

#### Complete diagnostics

- **present-perfect** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:261 · **new** · fingerprint: dc863a59620ce525978fa30c
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:265 · **new** · fingerprint: 17a4d086602b381ce65c59f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:43:257 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:44:3 · **new** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:3 · **new** · fingerprint: 5234929a399cf01e0d7f595c
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:129 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:153 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:185 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:207 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:53:80 · **new** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:80:16 · **new** · fingerprint: 2b26cf53803b151c21212120
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:1 · **new** · fingerprint: b394b51b09ad308cc8feeae3
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:179 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:116:72 · **new** · fingerprint: f7c21f7d8940f28c70370284
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:117:114 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:120:175 · **new** · fingerprint: 44fcd3dad59ced40bc859413
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:121:203 · **new** · fingerprint: 45a08d05aee0fa7834e7cd1d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:151:44 · **new** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:153:3 · **new** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:159:127 · **new** · fingerprint: beb9ea53ee058f3d9e59ec0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:14 · **new** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:88 · **new** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:188:70 · **new** · fingerprint: 15acf5b3ddc984f62af012a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:189:56 · **new** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:191:51 · **new** · fingerprint: 51cadbdd6b8eb0498821f9bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:210:9 · **new** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:212:94 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:213:7 · **new** · fingerprint: 33b3ff5444bee044b23c7ce9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:214:33 · **new** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:3 · **new** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:69 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:94 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:133 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:169 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:207 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:222:186 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:97 · **new** · fingerprint: 03a989d439e11fa4326ad6bc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:134 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:228:125 · **new** · fingerprint: 36e134bec11bbd982d0e34fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:38 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:61 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:71 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:104 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:131 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:251:377 · **new** · fingerprint: 6b1a09dc16c81cc09cefa126
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
