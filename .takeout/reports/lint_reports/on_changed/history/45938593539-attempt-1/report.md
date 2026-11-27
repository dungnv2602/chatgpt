# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#892](https://github.com/dungnv2602/chatgpt/actions/runs/45938593539)
- **Run ID / attempt:** 45938593539 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 010b310bda2d138130bf8287b3d9d42b5e6437bc
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 6cfbea7e8c0e092a5ab47cd498ec748cb3b54ef1
- **Linter source SHA:** 010b310bda2d138130bf8287b3d9d42b5e6437bc
- **Generated (UTC):** 2026-11-27T04:13:14.316119+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 10 |
| Hard findings | 6 |
| Advisory findings | 4 |
| New findings | 5 |
| Recurring findings | 5 |
| Resolved findings | 53 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/github-actions/SKILL.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/github-actions/SKILL.md | FAIL | 6 | 3 | 0 | 3318 | 0.2 | 1 |
| workspace/task_board.md | FAIL | 4 | 3 | 0 | 1341 | 0.3 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 4 |
| synonym-rotation | 3 |
| long-sentence | 2 |
| semicolon | 1 |

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
Ran 4 tests in 0.335s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.006s

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
Scanned 2 changed Markdown sources (545 available as link targets) and 65 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:36:65 · **new** · fingerprint: 3729cd2e886059e21da61ef7
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **long-sentence** · .agent/skills/github-actions/SKILL.md:80:1 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/task_board.md:5:336 · **new** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · workspace/task_board.md:41:41 · **new** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/task_board.md:98:88 · **new** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate

### Recurring findings

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:209 · **recurring** · fingerprint: de2e6ff859150e25d2ddbdf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:236 · **recurring** · fingerprint: 67be1862f0bcd76c81a66643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:284 · **recurring** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · .agent/skills/github-actions/SKILL.md:88:351 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/task_board.md:73:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

### Resolved findings

- **passive-voice** · .agent/skills/github-actions/SKILL.md:21:206 · **resolved** · fingerprint: ce5c879312639d5e4a37c1f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · .agent/skills/github-actions/SKILL.md:23:59 · **resolved** · fingerprint: 5ef6ce13baf5600a1694be8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:34:56 · **resolved** · fingerprint: 00ff55742e1a76adf05e8f19
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:72:35 · **resolved** · fingerprint: cffdf948bb88f727bace9878
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **long-sentence** · .agent/skills/github-actions/SKILL.md:80:1 · **resolved** · fingerprint: 4baec72a55fa29cd2e674673
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:85:106 · **resolved** · fingerprint: 585f1dd2fc6ade752cecb1db
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** corrected
- **long-sentence** · .agent/skills/github-actions/SKILL.md:86:63 · **resolved** · fingerprint: 069c795a0a52ebd5721e8aa1
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · .agent/skills/github-actions/SKILL.md:87:204 · **resolved** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:88:50 · **resolved** · fingerprint: ef1c126313fcc76c2583dac7
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **long-sentence** · .agent/skills/github-actions/SKILL.md:90:1 · **resolved** · fingerprint: 638245882c673be553a56771
  - **Level:** advisory-free
  - **Message:** Sentence has 37 words (cap 25). Split it.
  - **Matched text:** 37 words
- **passive-voice** · .agent/skills/github-actions/SKILL.md:90:103 · **resolved** · fingerprint: cd7ba366b1a6c942aa7fd8b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:162:42 · **resolved** · fingerprint: 7f75534bb1aa53c4310430aa
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'obtain' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **resolved** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **long-sentence** · .agent/skills/the-worker/SKILL.md:39:1 · **resolved** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:62 · **resolved** · fingerprint: 2a95aa3417dfc57540b6934b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:110 · **resolved** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:137 · **resolved** · fingerprint: b31436362c5e38fa10263166
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:189 · **resolved** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · .agent/skills/the-worker/SKILL.md:39:247 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:392 · **resolved** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **semicolon** · .agent/skills/the-worker/SKILL.md:46:133 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:50:16 · **resolved** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **long-sentence** · .agent/skills/the-worker/SKILL.md:51:4 · **resolved** · fingerprint: e50de15b76c7c77c6df3a052
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:51:48 · **resolved** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **long-sentence** · .agent/skills/the-worker/SKILL.md:52:4 · **resolved** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:52:45 · **resolved** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · .agent/skills/the-worker/SKILL.md:52:368 · **resolved** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:52:493 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **resolved** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:103 · **resolved** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **semicolon** · .agent/skills/the-worker/SKILL.md:86:70 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:146:48 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:295:144 · **resolved** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:297:124 · **resolved** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:300:3 · **resolved** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:346:29 · **resolved** · fingerprint: 14ea9a11815506c5f4355b7d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Approved
- **semicolon** · .agent/skills/the-worker/SKILL.md:346:80 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:96 · **resolved** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:165 · **resolved** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:126 · **resolved** · fingerprint: 30a5f5010d39a09d4d44c82a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:215 · **resolved** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/the-worker/SKILL.md:388:395 · **resolved** · fingerprint: 0903f3b4306b2fc6c361a363
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **long-sentence** · .agent/skills/the-worker/SKILL.md:412:1 · **resolved** · fingerprint: 12a0c65c6ffb1f23bd33659b
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:67 · **resolved** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:101 · **resolved** · fingerprint: b7a2bc4c1fde83c1a7f84a08
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:152 · **resolved** · fingerprint: f2c0edb97a4132169f97b4ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:184 · **resolved** · fingerprint: 1b18d543a8c344d3fcfffc26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reconciled
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:416:644 · **resolved** · fingerprint: 1ead56a935297678d525088d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **semicolon** · .agent/skills/the-worker/SKILL.md:422:175 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:437:200 · **resolved** · fingerprint: a67c2e85b92372da8a36a067
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is expected
- **passive-voice** · workspace/task_board.md:5:233 · **resolved** · fingerprint: d6ac34f6216a8a5c7f5df9d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · workspace/task_board.md:5:311 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/task_board.md:104:63 · **resolved** · fingerprint: fe0043dd1c2c55650b8f76ae
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 3318
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:36:65 · **new** · fingerprint: 3729cd2e886059e21da61ef7
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:209 · **recurring** · fingerprint: de2e6ff859150e25d2ddbdf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:236 · **recurring** · fingerprint: 67be1862f0bcd76c81a66643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:284 · **recurring** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **long-sentence** · .agent/skills/github-actions/SKILL.md:80:1 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/github-actions/SKILL.md:88:351 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 1341
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:5:336 · **new** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · workspace/task_board.md:41:41 · **new** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **long-sentence** · workspace/task_board.md:73:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

- **synonym-rotation** · workspace/task_board.md:98:88 · **new** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
