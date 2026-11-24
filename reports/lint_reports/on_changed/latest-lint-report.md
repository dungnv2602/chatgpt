# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#664](https://github.com/dungnv2602/chatgpt/actions/runs/45440436265)
- **Run ID / attempt:** 45440436265 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 80e67808c0b97fbd4f1e69896c806b2145316d7c
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** de6f18a6cb4d91784b71fce334de73505c7328fe
- **Linter source SHA:** 80e67808c0b97fbd4f1e69896c806b2145316d7c
- **Generated (UTC):** 2026-11-24T16:44:29.611964+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 9 |
| Files that failed | 5 |
| Files with findings | 5 |
| Total findings | 50 |
| Hard findings | 36 |
| Advisory findings | 14 |
| New findings | 4 |
| Recurring findings | 46 |
| Resolved findings | 67 |
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
- workspace/ADR_TEMPLATE.md
- skills/decision-governance/SKILL.md
- skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md
- workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md
- workspace/draft/README.md
- workspace/README.md
- workspace/DRAFT_TEMPLATE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/README.md | PASS | 0 | 0 | 0 | 515 | 0.0 | 0 |
| workspace/ADR_TEMPLATE.md | PASS | 0 | 0 | 0 | 349 | 0.0 | 0 |
| skills/decision-governance/SKILL.md | FAIL | 2 | 2 | 0 | 2202 | 0.1 | 1 |
| skills/document-standards/references/document-type-catalog.md | FAIL | 2 | 2 | 0 | 4373 | 0.0 | 1 |
| workspace/task_board.md | FAIL | 1 | 1 | 0 | 1435 | 0.1 | 1 |
| workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md | FAIL | 44 | 30 | 0 | 2622 | 1.7 | 1 |
| workspace/draft/README.md | PASS | 0 | 0 | 0 | 409 | 0.0 | 0 |
| workspace/README.md | FAIL | 1 | 1 | 0 | 886 | 0.1 | 1 |
| workspace/DRAFT_TEMPLATE.md | PASS | 0 | 0 | 0 | 428 | 0.0 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| semicolon | 20 |
| passive-voice | 13 |
| synonym-rotation | 11 |
| long-sentence | 5 |
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
Ran 4 tests in 0.343s

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

- **synonym-rotation** · skills/decision-governance/SKILL.md:142:28 · **new** · fingerprint: 4b2ab07116317a3363e3cd06
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:45:159 · **new** · fingerprint: ee3dcb468a833bb24e5822bc
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:46:331 · **new** · fingerprint: 7de3890b6aa2dea92c057735
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/task_board.md:137:65 · **new** · fingerprint: 2e2ac820f2b2ecba84ec2b97
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

### Recurring findings

- **synonym-rotation** · skills/decision-governance/SKILL.md:63:90 · **recurring** · fingerprint: 2624698c9e0a949a01e1c0be
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **present-perfect** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:261 · **recurring** · fingerprint: dc863a59620ce525978fa30c
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:265 · **recurring** · fingerprint: 17a4d086602b381ce65c59f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:43:257 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:44:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:3 · **recurring** · fingerprint: 5234929a399cf01e0d7f595c
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:129 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:153 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:185 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:207 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:53:80 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:80:16 · **recurring** · fingerprint: 2b26cf53803b151c21212120
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:1 · **recurring** · fingerprint: b394b51b09ad308cc8feeae3
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:179 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:116:72 · **recurring** · fingerprint: f7c21f7d8940f28c70370284
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:117:114 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:120:175 · **recurring** · fingerprint: 44fcd3dad59ced40bc859413
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:121:203 · **recurring** · fingerprint: 45a08d05aee0fa7834e7cd1d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:151:44 · **recurring** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:153:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:159:127 · **recurring** · fingerprint: beb9ea53ee058f3d9e59ec0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:14 · **recurring** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:88 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:188:70 · **recurring** · fingerprint: 15acf5b3ddc984f62af012a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:189:56 · **recurring** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:191:51 · **recurring** · fingerprint: 51cadbdd6b8eb0498821f9bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:210:9 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:212:94 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:213:7 · **recurring** · fingerprint: 33b3ff5444bee044b23c7ce9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:214:33 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:69 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:94 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:133 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:169 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:207 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:222:186 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:97 · **recurring** · fingerprint: 03a989d439e11fa4326ad6bc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:134 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:228:125 · **recurring** · fingerprint: 36e134bec11bbd982d0e34fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:38 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:61 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:71 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:104 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:131 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/README.md:58:376 · **recurring** · fingerprint: 3659e4816d32f3f6e196b772
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

### Resolved findings

- **passive-voice** · workspace/adr/README.md:59:38 · **resolved** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **semicolon** · workspace/adr/README.md:65:135 · **resolved** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/README.md:66:203 · **resolved** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/README.md:66:240 · **resolved** · fingerprint: 1e1a8d236c2a85c807def489
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **passive-voice** · workspace/ADR_TEMPLATE.md:29:67 · **resolved** · fingerprint: 245ae5ff11bd1a7e1426ac61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/ADR_TEMPLATE.md:53:57 · **resolved** · fingerprint: 7161ac8330313d0a21373d48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **passive-voice** · skills/decision-governance/SKILL.md:29:58 · **resolved** · fingerprint: 62ba07312f0098deae0d2084
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · skills/decision-governance/SKILL.md:29:82 · **resolved** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **synonym-rotation** · skills/decision-governance/SKILL.md:97:79 · **resolved** · fingerprint: fe036b1c2041ea8ab5e5609d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · skills/decision-governance/SKILL.md:99:39 · **resolved** · fingerprint: 22de3080c9e96c2f5e360d7c
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · skills/decision-governance/SKILL.md:100:5 · **resolved** · fingerprint: 9d17b4b98b345cc668999283
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · skills/decision-governance/SKILL.md:127:44 · **resolved** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **synonym-rotation** · skills/decision-governance/SKILL.md:137:75 · **resolved** · fingerprint: 4e69277105db71c84c9a2d9e
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · skills/decision-governance/SKILL.md:139:23 · **resolved** · fingerprint: 712aaab97b2af72d676d1263
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/decision-governance/SKILL.md:156:56 · **resolved** · fingerprint: 60f7b0b5e3f1e7faa3f326cc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · skills/decision-governance/SKILL.md:156:115 · **resolved** · fingerprint: 50567c7971d82a5d8b54420a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are resolved
- **passive-voice** · skills/decision-governance/SKILL.md:158:97 · **resolved** · fingerprint: 7b5a481ca6d089fd1b1dedf0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified
- **passive-voice** · skills/decision-governance/SKILL.md:170:19 · **resolved** · fingerprint: 2d396573c9ffec67f6ef5943
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · skills/decision-governance/SKILL.md:201:89 · **resolved** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · skills/decision-governance/SKILL.md:208:50 · **resolved** · fingerprint: e1b2426fdfb12ab8d8076ca7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **passive-voice** · skills/decision-governance/SKILL.md:237:72 · **resolved** · fingerprint: 3b0fa6154ecfe49591695005
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked
- **present-perfect** · skills/decision-governance/SKILL.md:247:22 · **resolved** · fingerprint: 7481ea9586cd9998cf136bf1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · skills/decision-governance/SKILL.md:247:26 · **resolved** · fingerprint: 50eae35fe6ca9a2e19bff9a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · skills/decision-governance/SKILL.md:248:38 · **resolved** · fingerprint: 58b03457b929a04127a23698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:3:1 · **resolved** · fingerprint: 33b66dbc6dc280ae7c9be6c8
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:28:139 · **resolved** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:33:453 · **resolved** · fingerprint: bcb83f45ddf38808e5512023
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:37:304 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:39:264 · **resolved** · fingerprint: bd13d200f2cd36d327625082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:45:198 · **resolved** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:48:276 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:49:207 · **resolved** · fingerprint: a41ef6bbf64045f943d2af47
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:51:139 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:53:358 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:55:336 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:63:560 · **resolved** · fingerprint: 199f2603ee3fb1c3abd18ce6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are skipped
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:98:268 · **resolved** · fingerprint: 028b84870f82ee2f98dcbf3b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has run
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:100:169 · **resolved** · fingerprint: bb8de6bc648079b20917fbff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are catalogued
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:111:263 · **resolved** · fingerprint: 305641bf283ed85e29efe674
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is published
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:123:251 · **resolved** · fingerprint: 195a2fd68103c17c8542eb26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:158:39 · **resolved** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:163:448 · **resolved** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:163:452 · **resolved** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:136 · **resolved** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:166:131 · **resolved** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:166:206 · **resolved** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:167:199 · **resolved** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:169:262 · **resolved** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:179:230 · **resolved** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:187:129 · **resolved** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:199:138 · **resolved** · fingerprint: d8738c991b456b6b6a7cdd80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconstructed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:202:203 · **resolved** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:211:57 · **resolved** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:215:189 · **resolved** · fingerprint: 7e6ec02ac376dc4e638ffc6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was warranted
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:223:32 · **resolved** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **passive-voice** · workspace/task_board.md:7:110 · **resolved** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/task_board.md:7:137 · **resolved** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · workspace/task_board.md:7:162 · **resolved** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:242:26 · **resolved** · fingerprint: d76d92c78578fde984466a23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:248:84 · **resolved** · fingerprint: 732e2543da3ef19c1be7937b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:249:123 · **resolved** · fingerprint: 55c2f7882df07adcfce356d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is linked
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:250:118 · **resolved** · fingerprint: cb69fc175cc5d06b9d0e4942
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was removed
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:250:238 · **resolved** · fingerprint: 1f05f232e3f4079a09edc109
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was deleted
- **synonym-rotation** · workspace/draft/README.md:25:5 · **resolved** · fingerprint: 644228716a76a4c04d4becf4
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **passive-voice** · workspace/README.md:58:108 · **resolved** · fingerprint: 4a500644b11ea45e7a256ac0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/README.md:62:305 · **resolved** · fingerprint: 44bac24ecf823fa7716cc698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/DRAFT_TEMPLATE.md:46:106 · **resolved** · fingerprint: 19ad35858d820c065c7de6e1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has mixed

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 515
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/ADR_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 349
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/decision-governance/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 2202
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · skills/decision-governance/SKILL.md:63:90 · **recurring** · fingerprint: 2624698c9e0a949a01e1c0be
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **synonym-rotation** · skills/decision-governance/SKILL.md:142:28 · **new** · fingerprint: 4b2ab07116317a3363e3cd06
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove


### skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 4373
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:45:159 · **new** · fingerprint: ee3dcb468a833bb24e5822bc
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** confirms

- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:46:331 · **new** · fingerprint: 7de3890b6aa2dea92c057735
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1435
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:137:65 · **new** · fingerprint: 2e2ac820f2b2ecba84ec2b97
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove


### workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 44
- **Hard findings:** 30
- **Baseline:** 0
- **Words:** 2622
- **Findings per 100 words:** 1.7

#### Complete diagnostics

- **present-perfect** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:261 · **recurring** · fingerprint: dc863a59620ce525978fa30c
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:265 · **recurring** · fingerprint: 17a4d086602b381ce65c59f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:43:257 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:44:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:3 · **recurring** · fingerprint: 5234929a399cf01e0d7f595c
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:129 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:153 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:185 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:207 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:53:80 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:80:16 · **recurring** · fingerprint: 2b26cf53803b151c21212120
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:1 · **recurring** · fingerprint: b394b51b09ad308cc8feeae3
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:179 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:116:72 · **recurring** · fingerprint: f7c21f7d8940f28c70370284
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:117:114 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:120:175 · **recurring** · fingerprint: 44fcd3dad59ced40bc859413
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:121:203 · **recurring** · fingerprint: 45a08d05aee0fa7834e7cd1d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:151:44 · **recurring** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:153:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:159:127 · **recurring** · fingerprint: beb9ea53ee058f3d9e59ec0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:14 · **recurring** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:88 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:188:70 · **recurring** · fingerprint: 15acf5b3ddc984f62af012a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:189:56 · **recurring** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:191:51 · **recurring** · fingerprint: 51cadbdd6b8eb0498821f9bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:210:9 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:212:94 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:213:7 · **recurring** · fingerprint: 33b3ff5444bee044b23c7ce9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:214:33 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:69 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:94 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:133 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:169 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:207 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:222:186 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:97 · **recurring** · fingerprint: 03a989d439e11fa4326ad6bc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:134 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:228:125 · **recurring** · fingerprint: 36e134bec11bbd982d0e34fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:38 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:61 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:71 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:104 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:131 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/draft/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 409
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


### workspace/DRAFT_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 428
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
