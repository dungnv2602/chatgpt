# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#852](https://github.com/dungnv2602/chatgpt/actions/runs/45906789462)
- **Run ID / attempt:** 45906789462 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / b85adbc5028420661a3c7c69c477d64c4098d29d
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 9aea6172959fa0ac677a685790d559379aefd20f
- **Linter source SHA:** b85adbc5028420661a3c7c69c477d64c4098d29d
- **Generated (UTC):** 2026-11-26T22:48:09.970293+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 5 |
| Files that failed | 4 |
| Files with findings | 5 |
| Total findings | 46 |
| Hard findings | 14 |
| Advisory findings | 32 |
| New findings | 37 |
| Recurring findings | 9 |
| Resolved findings | 26 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/INITIALIZATION_POLICY.md
- .agent/SESSION_START.md
- .agent/skills/the-worker/SKILL.md
- .agent/skills/the-worker/references/conversation-mode.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/INITIALIZATION_POLICY.md | PASS | 7 | 3 | 4 | 1948 | 0.4 | 0 |
| .agent/SESSION_START.md | FAIL | 10 | 4 | 0 | 3002 | 0.3 | 1 |
| .agent/skills/the-worker/SKILL.md | FAIL | 9 | 4 | 0 | 5874 | 0.2 | 1 |
| .agent/skills/the-worker/references/conversation-mode.md | FAIL | 19 | 2 | 0 | 3218 | 0.6 | 1 |
| workspace/task_board.md | FAIL | 1 | 1 | 0 | 495 | 0.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 25 |
| long-sentence | 8 |
| present-perfect | 7 |
| synonym-rotation | 5 |
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
Ran 4 tests in 0.347s

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
Scanned 5 changed Markdown sources (341 available as link targets) and 27 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **present-perfect** · .agent/INITIALIZATION_POLICY.md:40:53 · **new** · fingerprint: a68d4b2091de8244b08b0984
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:40:57 · **new** · fingerprint: cc8f76f7786acf5d8492b443
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **long-sentence** · .agent/INITIALIZATION_POLICY.md:157:3 · **new** · fingerprint: 18db183bae30a8739132c97b
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:166:154 · **new** · fingerprint: 0bd04eaf142f6db0f46ab9bd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:201:94 · **new** · fingerprint: 0d79d452758ac898f00007d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is handled
- **long-sentence** · .agent/INITIALIZATION_POLICY.md:202:3 · **new** · fingerprint: 33a3f9c5452d51f7c5c89fda
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **synonym-rotation** · .agent/INITIALIZATION_POLICY.md:202:215 · **new** · fingerprint: 88ebd6db25291d630f2b140f
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **synonym-rotation** · .agent/SESSION_START.md:29:137 · **new** · fingerprint: 77f3c453c24559d624144da4
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **present-perfect** · .agent/SESSION_START.md:41:114 · **new** · fingerprint: 7e401b80fb2469d88b8b16c6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved
- **passive-voice** · .agent/SESSION_START.md:41:119 · **new** · fingerprint: 65e01e8ee980bec2c691cd07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **synonym-rotation** · .agent/SESSION_START.md:53:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/SESSION_START.md:93:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:94:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · .agent/SESSION_START.md:238:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · .agent/SESSION_START.md:254:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · .agent/SESSION_START.md:279:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · .agent/SESSION_START.md:293:146 · **new** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **new** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:68:60 · **new** · fingerprint: d6fb83cbafb61644c729d606
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:68:162 · **new** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:84:157 · **new** · fingerprint: 50194bcb1c09593a6b8df74f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:96:72 · **new** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:101:41 · **new** · fingerprint: 01c59b00a54bee35fe1936cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:129:88 · **new** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:78 · **new** · fingerprint: 13168d32e5aeb357a6f05047
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:108 · **new** · fingerprint: 2d62a35466a8134401aac697
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:61 · **new** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:272 · **new** · fingerprint: a49119a4bb942d7711bad4ec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:146:63 · **new** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:151:36 · **new** · fingerprint: 3ca196dd83b56964e6c9c511
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:153:106 · **new** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:162:180 · **new** · fingerprint: 8b93e6445dd13d5345069497
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:260 · **new** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:206:94 · **new** · fingerprint: b8c8647d519418bedc546521
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:233:126 · **new** · fingerprint: f70f53510f186a20aefa39a5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:233:130 · **new** · fingerprint: 9c5f95ce73981d93b428a229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:254:75 · **new** · fingerprint: d3280be9a8e338d6afc3f804
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed

### Recurring findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:50:16 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:103 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · .agent/skills/the-worker/SKILL.md:75:15 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:294:144 · **recurring** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:296:124 · **recurring** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:299:3 · **recurring** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:382:361 · **recurring** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **long-sentence** · workspace/task_board.md:22:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
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
- **present-perfect** · .agent/skills/github-actions/SKILL.md:33:40 · **resolved** · fingerprint: e8019ef8bf6c31ab6be19a58
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:69:35 · **resolved** · fingerprint: cffdf948bb88f727bace9878
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **long-sentence** · .agent/skills/github-actions/SKILL.md:77:1 · **resolved** · fingerprint: 4baec72a55fa29cd2e674673
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:81:240 · **resolved** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:82:106 · **resolved** · fingerprint: 585f1dd2fc6ade752cecb1db
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** corrected
- **long-sentence** · .agent/skills/github-actions/SKILL.md:83:63 · **resolved** · fingerprint: 069c795a0a52ebd5721e8aa1
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:83:305 · **resolved** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:84:6 · **resolved** · fingerprint: da3efccaf70f209c43bc39f7
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:85:50 · **resolved** · fingerprint: ef1c126313fcc76c2583dac7
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **passive-voice** · .agent/skills/github-actions/SKILL.md:87:105 · **resolved** · fingerprint: cd7ba366b1a6c942aa7fd8b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:87:130 · **resolved** · fingerprint: 82d53272cc36ef4ea58a00e3
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:159:42 · **resolved** · fingerprint: 7f75534bb1aa53c4310430aa
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'obtain' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:15:1 · **resolved** · fingerprint: e25170de63660ceb2bb6b239
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:31:92 · **resolved** · fingerprint: 0f6a0a839cf9723f76ad08cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:50:119 · **resolved** · fingerprint: c6700813c1ef8a45b5212e0b
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:60:57 · **resolved** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:100:110 · **resolved** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:115:4 · **resolved** · fingerprint: 120777a1feeba73d7b56cd81
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:115:134 · **resolved** · fingerprint: a9bf21d3ce104680e2d861b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:118:36 · **resolved** · fingerprint: 1129812f092e8f4918e212e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Proposed
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:126:20 · **resolved** · fingerprint: 4b1b6661164047c147b88a63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:136:61 · **resolved** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:145:95 · **resolved** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:147:36 · **resolved** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/INITIALIZATION_POLICY.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 7
- **Hard findings:** 3
- **Baseline:** 4
- **Words:** 1948
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **present-perfect** · .agent/INITIALIZATION_POLICY.md:40:53 · **new** · fingerprint: a68d4b2091de8244b08b0984
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved

- **passive-voice** · .agent/INITIALIZATION_POLICY.md:40:57 · **new** · fingerprint: cc8f76f7786acf5d8492b443
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved

- **long-sentence** · .agent/INITIALIZATION_POLICY.md:157:3 · **new** · fingerprint: 18db183bae30a8739132c97b
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · .agent/INITIALIZATION_POLICY.md:166:154 · **new** · fingerprint: 0bd04eaf142f6db0f46ab9bd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored

- **passive-voice** · .agent/INITIALIZATION_POLICY.md:201:94 · **new** · fingerprint: 0d79d452758ac898f00007d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is handled

- **long-sentence** · .agent/INITIALIZATION_POLICY.md:202:3 · **new** · fingerprint: 33a3f9c5452d51f7c5c89fda
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **synonym-rotation** · .agent/INITIALIZATION_POLICY.md:202:215 · **new** · fingerprint: 88ebd6db25291d630f2b140f
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirms


### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 10
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 3002
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **synonym-rotation** · .agent/SESSION_START.md:29:137 · **new** · fingerprint: 77f3c453c24559d624144da4
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirm

- **present-perfect** · .agent/SESSION_START.md:41:114 · **new** · fingerprint: 7e401b80fb2469d88b8b16c6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved

- **passive-voice** · .agent/SESSION_START.md:41:119 · **new** · fingerprint: 65e01e8ee980bec2c691cd07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved

- **synonym-rotation** · .agent/SESSION_START.md:53:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · .agent/SESSION_START.md:93:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/SESSION_START.md:94:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **passive-voice** · .agent/SESSION_START.md:238:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **present-perfect** · .agent/SESSION_START.md:254:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed

- **long-sentence** · .agent/SESSION_START.md:279:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · .agent/SESSION_START.md:293:146 · **new** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 5874
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:50:16 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **new** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm

- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:103 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **passive-voice** · .agent/skills/the-worker/SKILL.md:75:15 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:294:144 · **recurring** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized

- **long-sentence** · .agent/skills/the-worker/SKILL.md:296:124 · **recurring** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **long-sentence** · .agent/skills/the-worker/SKILL.md:299:3 · **recurring** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words

- **long-sentence** · .agent/skills/the-worker/SKILL.md:382:361 · **recurring** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words


### .agent/skills/the-worker/references/conversation-mode.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 19
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 3218
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:68:60 · **new** · fingerprint: d6fb83cbafb61644c729d606
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:68:162 · **new** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:84:157 · **new** · fingerprint: 50194bcb1c09593a6b8df74f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:96:72 · **new** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:101:41 · **new** · fingerprint: 01c59b00a54bee35fe1936cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:129:88 · **new** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:78 · **new** · fingerprint: 13168d32e5aeb357a6f05047
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:108 · **new** · fingerprint: 2d62a35466a8134401aac697
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:61 · **new** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:272 · **new** · fingerprint: a49119a4bb942d7711bad4ec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:146:63 · **new** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:151:36 · **new** · fingerprint: 3ca196dd83b56964e6c9c511
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:153:106 · **new** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:162:180 · **new** · fingerprint: 8b93e6445dd13d5345069497
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:260 · **new** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:206:94 · **new** · fingerprint: b8c8647d519418bedc546521
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:233:126 · **new** · fingerprint: f70f53510f186a20aefa39a5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:233:130 · **new** · fingerprint: 9c5f95ce73981d93b428a229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:254:75 · **new** · fingerprint: d3280be9a8e338d6afc3f804
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 495
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **long-sentence** · workspace/task_board.md:22:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
