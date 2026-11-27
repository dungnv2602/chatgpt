# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#889](https://github.com/dungnv2602/chatgpt/actions/runs/45935299170)
- **Run ID / attempt:** 45935299170 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 1d675d93fd54b7215919ddbd5c3d7b9c1eb1aa30
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 5f8a6b94fefd63b0a4269178deb2fe04c7195514
- **Linter source SHA:** 1d675d93fd54b7215919ddbd5c3d7b9c1eb1aa30
- **Generated (UTC):** 2026-11-27T03:38:57.106854+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 3 |
| Files with findings | 3 |
| Total findings | 31 |
| Hard findings | 16 |
| Advisory findings | 15 |
| New findings | 29 |
| Recurring findings | 2 |
| Resolved findings | 81 |
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
- workspace/SUBTASK_TEMPLATE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/github-actions/SKILL.md | FAIL | 20 | 12 | 0 | 3266 | 0.6 | 1 |
| workspace/task_board.md | FAIL | 4 | 3 | 0 | 1492 | 0.3 | 1 |
| workspace/SUBTASK_TEMPLATE.md | FAIL | 7 | 1 | 0 | 381 | 1.8 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 15 |
| synonym-rotation | 7 |
| semicolon | 6 |
| long-sentence | 3 |

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
Ran 4 tests in 0.365s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

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
Scanned 3 changed Markdown sources (526 available as link targets) and 62 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/skills/github-actions/SKILL.md:21:206 · **new** · fingerprint: ce5c879312639d5e4a37c1f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · .agent/skills/github-actions/SKILL.md:23:59 · **new** · fingerprint: 5ef6ce13baf5600a1694be8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:34:56 · **new** · fingerprint: 00ff55742e1a76adf05e8f19
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:72:35 · **new** · fingerprint: cffdf948bb88f727bace9878
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:209 · **new** · fingerprint: de2e6ff859150e25d2ddbdf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:236 · **new** · fingerprint: 67be1862f0bcd76c81a66643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:284 · **new** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **long-sentence** · .agent/skills/github-actions/SKILL.md:80:1 · **new** · fingerprint: 4baec72a55fa29cd2e674673
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:84:240 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:85:106 · **new** · fingerprint: 585f1dd2fc6ade752cecb1db
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** corrected
- **long-sentence** · .agent/skills/github-actions/SKILL.md:86:63 · **new** · fingerprint: 069c795a0a52ebd5721e8aa1
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:86:305 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/github-actions/SKILL.md:87:204 · **new** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/github-actions/SKILL.md:87:283 · **new** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · .agent/skills/github-actions/SKILL.md:87:349 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:88:50 · **new** · fingerprint: ef1c126313fcc76c2583dac7
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **semicolon** · .agent/skills/github-actions/SKILL.md:88:353 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/github-actions/SKILL.md:90:105 · **new** · fingerprint: cd7ba366b1a6c942aa7fd8b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:90:130 · **new** · fingerprint: 82d53272cc36ef4ea58a00e3
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:162:42 · **new** · fingerprint: 7f75534bb1aa53c4310430aa
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'obtain' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **passive-voice** · workspace/task_board.md:5:233 · **new** · fingerprint: d6ac34f6216a8a5c7f5df9d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · workspace/task_board.md:5:311 · **new** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:47:32 · **new** · fingerprint: ce1654ab0d039468ca6174c7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:70:19 · **new** · fingerprint: cc5d31650b33c31ea7880172
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:70:60 · **new** · fingerprint: 77496caee1aa1b14090beb02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:70:96 · **new** · fingerprint: e89423f8de7a7a04a5c121a7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:80:41 · **new** · fingerprint: e0bf4bfde83ef287edeaa7a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Approved
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:80:95 · **new** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:88:142 · **new** · fingerprint: 3bf67591c2c0dcf331c90e43
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted

### Recurring findings

- **long-sentence** · workspace/task_board.md:76:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words
- **synonym-rotation** · workspace/task_board.md:100:63 · **recurring** · fingerprint: fe0043dd1c2c55650b8f76ae
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

### Resolved findings

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
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **resolved** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:103 · **resolved** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · .agent/skills/the-worker/SKILL.md:75:15 · **resolved** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
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
- **long-sentence** · .agent/skills/the-worker/SKILL.md:390:299 · **resolved** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:390:393 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
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
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:414:513 · **resolved** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
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
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:84:157 · **resolved** · fingerprint: 50194bcb1c09593a6b8df74f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:96:72 · **resolved** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:101:41 · **resolved** · fingerprint: 01c59b00a54bee35fe1936cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:129:88 · **resolved** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:78 · **resolved** · fingerprint: 13168d32e5aeb357a6f05047
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:108 · **resolved** · fingerprint: 2d62a35466a8134401aac697
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:61 · **resolved** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:272 · **resolved** · fingerprint: a49119a4bb942d7711bad4ec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:146:63 · **resolved** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:151:36 · **resolved** · fingerprint: 3ca196dd83b56964e6c9c511
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:153:106 · **resolved** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:162:180 · **resolved** · fingerprint: 8b93e6445dd13d5345069497
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:260 · **resolved** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:206:94 · **resolved** · fingerprint: b8c8647d519418bedc546521
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:233:126 · **resolved** · fingerprint: f70f53510f186a20aefa39a5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:233:130 · **resolved** · fingerprint: 9c5f95ce73981d93b428a229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:254:75 · **resolved** · fingerprint: d3280be9a8e338d6afc3f804
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:15:1 · **resolved** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:19:244 · **resolved** · fingerprint: b21e8e6015efba9bf5396408
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:31:92 · **resolved** · fingerprint: 0f6a0a839cf9723f76ad08cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:48:90 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:49:4 · **resolved** · fingerprint: 62caae9adf1fe0478e35b91e
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:52:140 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:54:119 · **resolved** · fingerprint: c6700813c1ef8a45b5212e0b
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:64:80 · **resolved** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:103:154 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:105:78 · **resolved** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:105:140 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:108:132 · **resolved** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:110:166 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:114:1 · **resolved** · fingerprint: cd108a111856938ac534f698
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:73 · **resolved** · fingerprint: 3ebed580ed89e11512cc3209
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:119 · **resolved** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:146 · **resolved** · fingerprint: b4a49fad74e43f16944593ba
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:182 · **resolved** · fingerprint: f3db8df3f6f0854270713679
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:289 · **resolved** · fingerprint: 75a6091a01c4060c972ae09a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:116:4 · **resolved** · fingerprint: 06781e91b8c02b9bfbcc5637
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:119:443 · **resolved** · fingerprint: b22fc281e33d4abf19ef71ef
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **present-perfect** · .agent/skills/ci-ledger/SKILL.md:119:500 · **resolved** · fingerprint: 3fef11eb6c41031d7263429e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has expired
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:119:662 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:123:96 · **resolved** · fingerprint: c1fc8e55e266407cd9fce7f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:123:107 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:129:20 · **resolved** · fingerprint: 4b1b6661164047c147b88a63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:139:61 · **resolved** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:148:95 · **resolved** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 20
- **Hard findings:** 12
- **Baseline:** 0
- **Words:** 3266
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/github-actions/SKILL.md:21:206 · **new** · fingerprint: ce5c879312639d5e4a37c1f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted

- **passive-voice** · .agent/skills/github-actions/SKILL.md:23:59 · **new** · fingerprint: 5ef6ce13baf5600a1694be8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:34:56 · **new** · fingerprint: 00ff55742e1a76adf05e8f19
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:72:35 · **new** · fingerprint: cffdf948bb88f727bace9878
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:209 · **new** · fingerprint: de2e6ff859150e25d2ddbdf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:236 · **new** · fingerprint: 67be1862f0bcd76c81a66643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:284 · **new** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **long-sentence** · .agent/skills/github-actions/SKILL.md:80:1 · **new** · fingerprint: 4baec72a55fa29cd2e674673
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **semicolon** · .agent/skills/github-actions/SKILL.md:84:240 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:85:106 · **new** · fingerprint: 585f1dd2fc6ade752cecb1db
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** corrected

- **long-sentence** · .agent/skills/github-actions/SKILL.md:86:63 · **new** · fingerprint: 069c795a0a52ebd5721e8aa1
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **semicolon** · .agent/skills/github-actions/SKILL.md:86:305 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/github-actions/SKILL.md:87:204 · **new** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · .agent/skills/github-actions/SKILL.md:87:283 · **new** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **semicolon** · .agent/skills/github-actions/SKILL.md:87:349 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:88:50 · **new** · fingerprint: ef1c126313fcc76c2583dac7
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **semicolon** · .agent/skills/github-actions/SKILL.md:88:353 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/github-actions/SKILL.md:90:105 · **new** · fingerprint: cd7ba366b1a6c942aa7fd8b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:90:130 · **new** · fingerprint: 82d53272cc36ef4ea58a00e3
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:162:42 · **new** · fingerprint: 7f75534bb1aa53c4310430aa
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'obtain' name the same action. Pick one and use it every time.
  - **Matched text:** fetch


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 1492
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:5:233 · **new** · fingerprint: d6ac34f6216a8a5c7f5df9d3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **semicolon** · workspace/task_board.md:5:311 · **new** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/task_board.md:76:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

- **synonym-rotation** · workspace/task_board.md:100:63 · **recurring** · fingerprint: fe0043dd1c2c55650b8f76ae
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate


### workspace/SUBTASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 381
- **Findings per 100 words:** 1.8

#### Complete diagnostics

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:47:32 · **new** · fingerprint: ce1654ab0d039468ca6174c7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:70:19 · **new** · fingerprint: cc5d31650b33c31ea7880172
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:70:60 · **new** · fingerprint: 77496caee1aa1b14090beb02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:70:96 · **new** · fingerprint: e89423f8de7a7a04a5c121a7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:80:41 · **new** · fingerprint: e0bf4bfde83ef287edeaa7a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Approved

- **semicolon** · workspace/SUBTASK_TEMPLATE.md:80:95 · **new** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:88:142 · **new** · fingerprint: 3bf67591c2c0dcf331c90e43
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
