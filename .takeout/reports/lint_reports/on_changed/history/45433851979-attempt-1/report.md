# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#652](https://github.com/dungnv2602/chatgpt/actions/runs/45433851979)
- **Run ID / attempt:** 45433851979 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / cf293d2d7bc3396eefb91360f0b36561d777ceb4
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** f3ffc8590cd01ca6eaf26ff25f7f08d32f2b4c76
- **Linter source SHA:** cf293d2d7bc3396eefb91360f0b36561d777ceb4
- **Generated (UTC):** 2026-11-24T16:13:13.144253+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 5 |
| Files that failed | 4 |
| Files with findings | 5 |
| Total findings | 78 |
| Hard findings | 40 |
| Advisory findings | 38 |
| New findings | 73 |
| Recurring findings | 5 |
| Resolved findings | 36 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/README.md
- workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md
- workspace/task_board.md
- workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md
- workspace/draft/README.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/README.md | FAIL | 4 | 2 | 0 | 411 | 1.0 | 1 |
| workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md | FAIL | 19 | 7 | 0 | 3360 | 0.6 | 1 |
| workspace/task_board.md | PASS | 4 | 0 | 0 | 1303 | 0.3 | 0 |
| workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md | FAIL | 48 | 30 | 0 | 2567 | 1.9 | 1 |
| workspace/draft/README.md | FAIL | 3 | 1 | 0 | 340 | 0.9 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 34 |
| semicolon | 23 |
| synonym-rotation | 11 |
| long-sentence | 6 |
| present-perfect | 4 |

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
Ran 4 tests in 0.355s

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
- **semicolon** · workspace/adr/README.md:60:135 · **new** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/README.md:61:203 · **new** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/README.md:61:240 · **new** · fingerprint: 1e1a8d236c2a85c807def489
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:42:64 · **new** · fingerprint: 04ec4f5fbb130c1324f44f00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:83:41 · **new** · fingerprint: 5d7ba294a41810bbc4f7a8fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made
- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:179:31 · **new** · fingerprint: 015ecb389e532dd8875c1837
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has presented
- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:180:34 · **new** · fingerprint: 0f4521e8c2b440c5ef392f4b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has requested
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:182:23 · **new** · fingerprint: 852ed94029abbea4e6fab0f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:203:14 · **new** · fingerprint: 8d81ddd804dfe2c99c883b3e
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:219:237 · **new** · fingerprint: 4c95c42ba0a8e33df95da64d
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:271:158 · **new** · fingerprint: a317f5b19e2ab5d770d78d2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grandfathered
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:277:55 · **new** · fingerprint: 54ced16a4522c38f24c053a6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was implemented
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:279:21 · **new** · fingerprint: 469e1521575230ced366ea79
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:281:38 · **new** · fingerprint: 21fa99cd9adb2127f01fc204
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:283:132 · **new** · fingerprint: 101211397f76806715447ab0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:287:85 · **new** · fingerprint: befabfa16e1d11b4cc317bc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:297:42 · **new** · fingerprint: 063bc6652b2f8cba7e22ed0d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:305:59 · **new** · fingerprint: 8ab2123627f631a8c49701db
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fixed
- **long-sentence** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:335:3 · **new** · fingerprint: 8bf6c58f1f0bd3c79519cfd1
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:357:45 · **new** · fingerprint: 7a97a9361b4bcc774d6f0ab9
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:374:95 · **new** · fingerprint: e1b81119b147b4cb2485bf75
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:404:17 · **new** · fingerprint: 396aabeca89bdc013b3dc544
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
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
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:239:39 · **new** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:241:18 · **new** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:242:26 · **new** · fingerprint: d76d92c78578fde984466a23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:248:84 · **new** · fingerprint: 732e2543da3ef19c1be7937b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read
- **present-perfect** · workspace/draft/README.md:19:179 · **new** · fingerprint: 3832db9cae5a8a4e53c68141
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been corrected
- **passive-voice** · workspace/draft/README.md:19:183 · **new** · fingerprint: a490f7b04ccd2a7c6fb6e16d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been corrected

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
- **passive-voice** · workspace/task_board.md:11:31 · **recurring** · fingerprint: ed2247bc287f94142d470682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected
- **semicolon** · workspace/draft/README.md:19:152 · **recurring** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Resolved findings

- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:23:255 · **resolved** · fingerprint: b2db79571b0fd793f16cfc6e
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:23:261 · **resolved** · fingerprint: f33785399ee477f140c53be5
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:27:74 · **resolved** · fingerprint: 682e7a3c6258df9314cac8ab
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:38:154 · **resolved** · fingerprint: 417028a1c6ce0cd86f44b467
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has clarified
- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:40:229 · **resolved** · fingerprint: 8a7eac590ca1275b3cbb1898
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:42:64 · **resolved** · fingerprint: e393f743a72abc7c888f6cec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:55:41 · **resolved** · fingerprint: c447d529f7b20b4590b587f7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:86:39 · **resolved** · fingerprint: 0b579768d40496de9c52eb18
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:90:52 · **resolved** · fingerprint: c447d529f7b20b4590b587f7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **synonym-rotation** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:99:16 · **resolved** · fingerprint: dd3e21d877e9a2d231775f40
  - **Level:** advisory-free
  - **Message:** 'verify' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **present-perfect** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:138:90 · **resolved** · fingerprint: 74b25e7a1f97c63191134119
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has passed
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:151:27 · **resolved** · fingerprint: b9a84ebe6dcce03f0dc6bba8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were considered
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:168:50 · **resolved** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:170:3 · **resolved** · fingerprint: 88383bbb9edb4a64f57b4f5d
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:176:127 · **resolved** · fingerprint: 60f3249b1cd98b7bfc324e27
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:179:14 · **resolved** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:179:85 · **resolved** · fingerprint: e3f45e1c3ad0739bdf1dd4df
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:197:19 · **resolved** · fingerprint: 905526addeefb056e33bf047
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:205:21 · **resolved** · fingerprint: e393f743a72abc7c888f6cec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:206:58 · **resolved** · fingerprint: dbf3d2cb4647779b785af24a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:208:51 · **resolved** · fingerprint: 9ddf121d6af934b7f894ee93
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:217:77 · **resolved** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:217:122 · **resolved** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:220:83 · **resolved** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:222:91 · **resolved** · fingerprint: 5adb2f8b4d0fd44cce39c150
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retired
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:223:80 · **resolved** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:234:102 · **resolved** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:237:63 · **resolved** · fingerprint: 4d6943b3cf48f72f6c117611
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is scheduled
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:243:24 · **resolved** · fingerprint: d7ce4a873457263c7e94b520
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:262:9 · **resolved** · fingerprint: 98c2fc965a4ebb8e335136f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:264:97 · **resolved** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:265:13 · **resolved** · fingerprint: ce34144ae929301d185371c6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:266:33 · **resolved** · fingerprint: 98c2fc965a4ebb8e335136f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **long-sentence** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:287:4 · **resolved** · fingerprint: 12e588d9bbad646077be3159
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **passive-voice** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:301:285 · **resolved** · fingerprint: 3d55bac6a43511c9d51dfea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was prepared
- **semicolon** · workspace/draft/DRAFT-0003-retire-source-drafts-after-verified-adr-promotion.md:302:159 · **resolved** · fingerprint: 04c9ac442f56ef3b58400722
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 411
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **passive-voice** · workspace/adr/README.md:54:38 · **new** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **semicolon** · workspace/adr/README.md:60:135 · **new** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/README.md:61:203 · **new** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/README.md:61:240 · **new** · fingerprint: 1e1a8d236c2a85c807def489
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded


### workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 19
- **Hard findings:** 7
- **Baseline:** 0
- **Words:** 3360
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:42:64 · **new** · fingerprint: 04ec4f5fbb130c1324f44f00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:83:41 · **new** · fingerprint: 5d7ba294a41810bbc4f7a8fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made

- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:179:31 · **new** · fingerprint: 015ecb389e532dd8875c1837
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has presented

- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:180:34 · **new** · fingerprint: 0f4521e8c2b440c5ef392f4b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has requested

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:182:23 · **new** · fingerprint: 852ed94029abbea4e6fab0f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:203:14 · **new** · fingerprint: 8d81ddd804dfe2c99c883b3e
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:219:237 · **new** · fingerprint: 4c95c42ba0a8e33df95da64d
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:271:158 · **new** · fingerprint: a317f5b19e2ab5d770d78d2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grandfathered

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:277:55 · **new** · fingerprint: 54ced16a4522c38f24c053a6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was implemented

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:279:21 · **new** · fingerprint: 469e1521575230ced366ea79
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:281:38 · **new** · fingerprint: 21fa99cd9adb2127f01fc204
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:283:132 · **new** · fingerprint: 101211397f76806715447ab0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:287:85 · **new** · fingerprint: befabfa16e1d11b4cc317bc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:297:42 · **new** · fingerprint: 063bc6652b2f8cba7e22ed0d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:305:59 · **new** · fingerprint: 8ab2123627f631a8c49701db
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fixed

- **long-sentence** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:335:3 · **new** · fingerprint: 8bf6c58f1f0bd3c79519cfd1
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:357:45 · **new** · fingerprint: 7a97a9361b4bcc774d6f0ab9
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:374:95 · **new** · fingerprint: e1b81119b147b4cb2485bf75
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:404:17 · **new** · fingerprint: 396aabeca89bdc013b3dc544
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 4
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1303
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

- **passive-voice** · workspace/task_board.md:11:31 · **recurring** · fingerprint: ed2247bc287f94142d470682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected


### workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 48
- **Hard findings:** 30
- **Baseline:** 0
- **Words:** 2567
- **Findings per 100 words:** 1.9

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

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:239:39 · **new** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:241:18 · **new** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:242:26 · **new** · fingerprint: d76d92c78578fde984466a23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:248:84 · **new** · fingerprint: 732e2543da3ef19c1be7937b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read


### workspace/draft/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 340
- **Findings per 100 words:** 0.9

#### Complete diagnostics

- **semicolon** · workspace/draft/README.md:19:152 · **recurring** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · workspace/draft/README.md:19:179 · **new** · fingerprint: 3832db9cae5a8a4e53c68141
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been corrected

- **passive-voice** · workspace/draft/README.md:19:183 · **new** · fingerprint: a490f7b04ccd2a7c6fb6e16d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been corrected

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
