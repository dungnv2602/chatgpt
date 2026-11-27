# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#888](https://github.com/dungnv2602/chatgpt/actions/runs/45935162405)
- **Run ID / attempt:** 45935162405 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 5f8a6b94fefd63b0a4269178deb2fe04c7195514
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 0814be54a9a2a4dc365794f03de98c1d71d66fba
- **Linter source SHA:** 5f8a6b94fefd63b0a4269178deb2fe04c7195514
- **Generated (UTC):** 2026-11-27T03:37:08.310834+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 4 |
| Files that failed | 3 |
| Files with findings | 4 |
| Total findings | 83 |
| Hard findings | 32 |
| Advisory findings | 51 |
| New findings | 49 |
| Recurring findings | 34 |
| Resolved findings | 90 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/SKILL.md
- .agent/skills/the-worker/references/conversation-mode.md
- workspace/task_board.md
- .agent/skills/ci-ledger/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/SKILL.md | FAIL | 36 | 15 | 0 | 6189 | 0.6 | 1 |
| .agent/skills/the-worker/references/conversation-mode.md | PASS | 17 | 0 | 0 | 3221 | 0.5 | 0 |
| workspace/task_board.md | FAIL | 2 | 2 | 0 | 1420 | 0.1 | 1 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 28 | 15 | 0 | 2257 | 1.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 46 |
| semicolon | 14 |
| long-sentence | 10 |
| synonym-rotation | 8 |
| present-perfect | 5 |

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
Ran 4 tests in 0.237s

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
Scanned 4 changed Markdown sources (519 available as link targets) and 71 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **long-sentence** · .agent/skills/the-worker/SKILL.md:39:1 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:346:29 · **new** · fingerprint: 14ea9a11815506c5f4355b7d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Approved
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
- **long-sentence** · workspace/task_board.md:70:1 · **new** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words
- **synonym-rotation** · workspace/task_board.md:94:63 · **new** · fingerprint: fe0043dd1c2c55650b8f76ae
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:15:1 · **new** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:19:244 · **new** · fingerprint: b21e8e6015efba9bf5396408
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:31:92 · **new** · fingerprint: 0f6a0a839cf9723f76ad08cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:48:90 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:49:4 · **new** · fingerprint: 62caae9adf1fe0478e35b91e
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:52:140 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:54:119 · **new** · fingerprint: c6700813c1ef8a45b5212e0b
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:64:80 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:103:154 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:105:78 · **new** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:105:140 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:108:132 · **new** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:110:166 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:114:1 · **new** · fingerprint: cd108a111856938ac534f698
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:73 · **new** · fingerprint: 3ebed580ed89e11512cc3209
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:119 · **new** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:146 · **new** · fingerprint: b4a49fad74e43f16944593ba
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:182 · **new** · fingerprint: f3db8df3f6f0854270713679
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:289 · **new** · fingerprint: 75a6091a01c4060c972ae09a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:116:4 · **new** · fingerprint: 06781e91b8c02b9bfbcc5637
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:119:443 · **new** · fingerprint: b22fc281e33d4abf19ef71ef
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **present-perfect** · .agent/skills/ci-ledger/SKILL.md:119:500 · **new** · fingerprint: 3fef11eb6c41031d7263429e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has expired
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:119:662 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:123:96 · **new** · fingerprint: c1fc8e55e266407cd9fce7f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:123:107 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:129:20 · **new** · fingerprint: 4b1b6661164047c147b88a63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:139:61 · **new** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:148:95 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

### Recurring findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:62 · **recurring** · fingerprint: 2a95aa3417dfc57540b6934b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:110 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:137 · **recurring** · fingerprint: b31436362c5e38fa10263166
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:189 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · .agent/skills/the-worker/SKILL.md:39:247 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:392 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **semicolon** · .agent/skills/the-worker/SKILL.md:46:133 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:50:16 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **recurring** · fingerprint: 952a5f851897b7d21a178421
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
- **semicolon** · .agent/skills/the-worker/SKILL.md:86:70 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:146:48 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:295:144 · **recurring** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:297:124 · **recurring** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:300:3 · **recurring** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:346:80 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:96 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:165 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:126 · **recurring** · fingerprint: 30a5f5010d39a09d4d44c82a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:215 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/the-worker/SKILL.md:388:395 · **recurring** · fingerprint: 0903f3b4306b2fc6c361a363
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **long-sentence** · .agent/skills/the-worker/SKILL.md:390:299 · **recurring** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:390:393 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/SKILL.md:412:1 · **recurring** · fingerprint: 12a0c65c6ffb1f23bd33659b
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:67 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:101 · **recurring** · fingerprint: b7a2bc4c1fde83c1a7f84a08
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:152 · **recurring** · fingerprint: f2c0edb97a4132169f97b4ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:184 · **recurring** · fingerprint: 1b18d543a8c344d3fcfffc26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reconciled
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:414:513 · **recurring** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:416:644 · **recurring** · fingerprint: 1ead56a935297678d525088d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **semicolon** · .agent/skills/the-worker/SKILL.md:422:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:437:200 · **recurring** · fingerprint: a67c2e85b92372da8a36a067
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is expected

### Resolved findings

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:125 · **resolved** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:205 · **resolved** · fingerprint: 71fd369fd4ce87f3145d3f61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are contained
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:37:57 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:42:32 · **resolved** · fingerprint: 0b78e160768da5f8fc81245e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are surfaced
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:46:184 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:50:263 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:72:40 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:72:92 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:74:105 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:76:181 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:80:163 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:83:120 · **resolved** · fingerprint: f344f235da524619c5f3958e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are represented
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:84:107 · **resolved** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:84:247 · **resolved** · fingerprint: 9997ef7899ffcdb243897741
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reviewed
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:86:3 · **resolved** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:177 · **resolved** · fingerprint: b29e4df2ee98e11a4663446d
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:364 · **resolved** · fingerprint: 9943dcb3a220dcbe0a08ff17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:533 · **resolved** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:93:131 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:95:345 · **resolved** · fingerprint: 6ecaad7e08b08c8dc23c4ac5
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** deletes
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:96:213 · **resolved** · fingerprint: d88c984bfabc22fedfc1df95
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:97:86 · **resolved** · fingerprint: 6a157062d0e778513b660642
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has validated
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:111:162 · **resolved** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:115:3 · **resolved** · fingerprint: 95b3ae27d255dd6d3908c02c
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:115:67 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:115:115 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:116:3 · **resolved** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:118:95 · **resolved** · fingerprint: e9a8ebb703f48aa4c6b3f8f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:119:24 · **resolved** · fingerprint: 87531091dab5fb40e4c2d4ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were run
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:119:83 · **resolved** · fingerprint: dfff58b82bd3b79192dfa4bf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was replayed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:119:118 · **resolved** · fingerprint: e9a8ebb703f48aa4c6b3f8f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:125:143 · **resolved** · fingerprint: 298a9b83f5adba5f46527b78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:126:57 · **resolved** · fingerprint: 0ed0ae36b993057bc70765a0
  - **Level:** advisory-free
  - **Message:** 'verify' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:127:21 · **resolved** · fingerprint: f85e8d2b3bb15312e48006c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is confused
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:128:107 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:128:181 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:130:22 · **resolved** · fingerprint: 3c01363d8fccb6632309a933
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:41 · **resolved** · fingerprint: 0a8fdd51c323d7e6c5184e93
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:133:109 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:134:224 · **resolved** · fingerprint: de92bd816462c66ade721476
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:145:206 · **resolved** · fingerprint: 579e397c39954135265f1d98
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:146:81 · **resolved** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:154:95 · **resolved** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:4 · **resolved** · fingerprint: 911fad1e156f4210f836f36c
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:69 · **resolved** · fingerprint: 14114c25a67a248bad384f1b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:214 · **resolved** · fingerprint: 9943dcb3a220dcbe0a08ff17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:158:54 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:158:178 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:174:3 · **resolved** · fingerprint: 95b3ae27d255dd6d3908c02c
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:175:95 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:175:109 · **resolved** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:177:75 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:180:85 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:100 · **resolved** · fingerprint: e9365b9cbb59d135219ec64e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:201:81 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:206:85 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:3 · **resolved** · fingerprint: 8529e180856bf3676ae3fab0
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:43 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:71 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:89 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:148 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:232 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:269 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:292 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:328 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:346 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:3 · **resolved** · fingerprint: 13f3933d006440387035088b
  - **Level:** advisory-free
  - **Message:** Sentence has 47 words (cap 25). Split it.
  - **Matched text:** 47 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:63 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:199 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:279 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:353 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:385 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:215:3 · **resolved** · fingerprint: 3d2b37a88e8f61e65de9b8fa
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:215:125 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:215:158 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:219:98 · **resolved** · fingerprint: 1667b4bb6e8771c9446dd6e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:219:135 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:220:133 · **resolved** · fingerprint: 94d4b6dd593fe428491082fb
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repairs
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:221:71 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:221:140 · **resolved** · fingerprint: dbe769c0dba8d9167f6f8147
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** altering
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:240:312 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:245:164 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/SKILL.md:39:1 · **resolved** · fingerprint: 678ab67701d0d18a96087add
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · workspace/README.md:47:77 · **resolved** · fingerprint: 52ba35678185966f3e495ffc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/README.md:59:75 · **resolved** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · workspace/README.md:59:111 · **resolved** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/README.md:59:220 · **resolved** · fingerprint: bd41e95b24e62139f9055fb7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/README.md:59:480 · **resolved** · fingerprint: eb43c2017cbbb6f4ef69df3f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **passive-voice** · workspace/README.md:63:202 · **resolved** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · workspace/README.md:63:277 · **resolved** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 36
- **Hard findings:** 15
- **Baseline:** 0
- **Words:** 6189
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed

- **long-sentence** · .agent/skills/the-worker/SKILL.md:39:1 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:62 · **recurring** · fingerprint: 2a95aa3417dfc57540b6934b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:110 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:137 · **recurring** · fingerprint: b31436362c5e38fa10263166
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:189 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **semicolon** · .agent/skills/the-worker/SKILL.md:39:247 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:392 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **semicolon** · .agent/skills/the-worker/SKILL.md:46:133 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:50:16 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **recurring** · fingerprint: 952a5f851897b7d21a178421
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

- **semicolon** · .agent/skills/the-worker/SKILL.md:86:70 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:146:48 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:295:144 · **recurring** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized

- **long-sentence** · .agent/skills/the-worker/SKILL.md:297:124 · **recurring** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **long-sentence** · .agent/skills/the-worker/SKILL.md:300:3 · **recurring** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:346:29 · **new** · fingerprint: 14ea9a11815506c5f4355b7d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Approved

- **semicolon** · .agent/skills/the-worker/SKILL.md:346:80 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:96 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:165 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:126 · **recurring** · fingerprint: 30a5f5010d39a09d4d44c82a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:215 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · .agent/skills/the-worker/SKILL.md:388:395 · **recurring** · fingerprint: 0903f3b4306b2fc6c361a363
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

- **long-sentence** · .agent/skills/the-worker/SKILL.md:390:299 · **recurring** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/the-worker/SKILL.md:390:393 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/SKILL.md:412:1 · **recurring** · fingerprint: 12a0c65c6ffb1f23bd33659b
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:67 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:101 · **recurring** · fingerprint: b7a2bc4c1fde83c1a7f84a08
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:152 · **recurring** · fingerprint: f2c0edb97a4132169f97b4ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:184 · **recurring** · fingerprint: 1b18d543a8c344d3fcfffc26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reconciled

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:414:513 · **recurring** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:416:644 · **recurring** · fingerprint: 1ead56a935297678d525088d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **semicolon** · .agent/skills/the-worker/SKILL.md:422:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:437:200 · **recurring** · fingerprint: a67c2e85b92372da8a36a067
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is expected


### .agent/skills/the-worker/references/conversation-mode.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 17
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 3221
- **Findings per 100 words:** 0.5

#### Complete diagnostics

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
- **Findings:** 2
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1420
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **long-sentence** · workspace/task_board.md:70:1 · **new** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

- **synonym-rotation** · workspace/task_board.md:94:63 · **new** · fingerprint: fe0043dd1c2c55650b8f76ae
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 28
- **Hard findings:** 15
- **Baseline:** 0
- **Words:** 2257
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:15:1 · **new** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:19:244 · **new** · fingerprint: b21e8e6015efba9bf5396408
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:31:92 · **new** · fingerprint: 0f6a0a839cf9723f76ad08cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:48:90 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:49:4 · **new** · fingerprint: 62caae9adf1fe0478e35b91e
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:52:140 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:54:119 · **new** · fingerprint: c6700813c1ef8a45b5212e0b
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:64:80 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:103:154 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:105:78 · **new** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:105:140 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:108:132 · **new** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:110:166 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:114:1 · **new** · fingerprint: cd108a111856938ac534f698
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:73 · **new** · fingerprint: 3ebed580ed89e11512cc3209
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:119 · **new** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:146 · **new** · fingerprint: b4a49fad74e43f16944593ba
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:182 · **new** · fingerprint: f3db8df3f6f0854270713679
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:114:289 · **new** · fingerprint: 75a6091a01c4060c972ae09a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:116:4 · **new** · fingerprint: 06781e91b8c02b9bfbcc5637
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:119:443 · **new** · fingerprint: b22fc281e33d4abf19ef71ef
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **present-perfect** · .agent/skills/ci-ledger/SKILL.md:119:500 · **new** · fingerprint: 3fef11eb6c41031d7263429e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has expired

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:119:662 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:123:96 · **new** · fingerprint: c1fc8e55e266407cd9fce7f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:123:107 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:129:20 · **new** · fingerprint: 4b1b6661164047c147b88a63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:139:61 · **new** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:148:95 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
