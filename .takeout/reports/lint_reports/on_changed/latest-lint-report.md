# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#874](https://github.com/dungnv2602/chatgpt/actions/runs/45921789448)
- **Run ID / attempt:** 45921789448 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / abb4fac02027981e265bc0a16859695a1108f655
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 2944f6bf4af7847944660a4f7a22ba54313a9ffc
- **Linter source SHA:** abb4fac02027981e265bc0a16859695a1108f655
- **Generated (UTC):** 2026-11-27T01:19:44.607923+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 4 |
| Files that failed | 3 |
| Files with findings | 4 |
| Total findings | 60 |
| Hard findings | 24 |
| Advisory findings | 36 |
| New findings | 29 |
| Recurring findings | 31 |
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

- .agent/skills/the-worker/SKILL.md
- workspace/task_board.md
- .agent/skills/ci-ledger/SKILL.md
- workspace/README.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/SKILL.md | FAIL | 31 | 11 | 0 | 6059 | 0.5 | 1 |
| workspace/task_board.md | FAIL | 1 | 1 | 0 | 470 | 0.2 | 1 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 21 | 12 | 0 | 2030 | 1.0 | 1 |
| workspace/README.md | PASS | 7 | 0 | 0 | 967 | 0.7 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 35 |
| semicolon | 11 |
| long-sentence | 7 |
| synonym-rotation | 6 |
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
Ran 4 tests in 0.344s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.040s

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
Scanned 4 changed Markdown sources (371 available as link targets) and 35 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **long-sentence** · workspace/task_board.md:22:1 · **new** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words
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
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:106:66 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:107:132 · **new** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:109:48 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:113:156 · **new** · fingerprint: 75a6091a01c4060c972ae09a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:115:4 · **new** · fingerprint: 06781e91b8c02b9bfbcc5637
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:118:165 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:120:27 · **new** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes
- **present-perfect** · .agent/skills/ci-ledger/SKILL.md:122:91 · **new** · fingerprint: e9e6a23d2f10dd7ba3a83f2d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has started
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:122:151 · **new** · fingerprint: c1fc8e55e266407cd9fce7f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:122:162 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:128:20 · **new** · fingerprint: 4b1b6661164047c147b88a63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:138:61 · **new** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:147:95 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/README.md:47:77 · **new** · fingerprint: 52ba35678185966f3e495ffc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/README.md:59:75 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · workspace/README.md:59:111 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/README.md:59:220 · **new** · fingerprint: bd41e95b24e62139f9055fb7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/README.md:59:480 · **new** · fingerprint: eb43c2017cbbb6f4ef69df3f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **passive-voice** · workspace/README.md:63:202 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · workspace/README.md:63:277 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

### Recurring findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **long-sentence** · .agent/skills/the-worker/SKILL.md:39:1 · **recurring** · fingerprint: 678ab67701d0d18a96087add
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:50 · **recurring** · fingerprint: 2a95aa3417dfc57540b6934b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:98 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:125 · **recurring** · fingerprint: b31436362c5e38fa10263166
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:177 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · .agent/skills/the-worker/SKILL.md:39:229 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:359 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
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
- **passive-voice** · .agent/skills/the-worker/SKILL.md:388:332 · **recurring** · fingerprint: 0903f3b4306b2fc6c361a363
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
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
- **semicolon** · .agent/skills/the-worker/SKILL.md:422:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:437:200 · **recurring** · fingerprint: a67c2e85b92372da8a36a067
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is expected

### Resolved findings

None.

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 31
- **Hard findings:** 11
- **Baseline:** 0
- **Words:** 6059
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed

- **long-sentence** · .agent/skills/the-worker/SKILL.md:39:1 · **recurring** · fingerprint: 678ab67701d0d18a96087add
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:50 · **recurring** · fingerprint: 2a95aa3417dfc57540b6934b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:98 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:125 · **recurring** · fingerprint: b31436362c5e38fa10263166
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:177 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **semicolon** · .agent/skills/the-worker/SKILL.md:39:229 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:359 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

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

- **passive-voice** · .agent/skills/the-worker/SKILL.md:388:332 · **recurring** · fingerprint: 0903f3b4306b2fc6c361a363
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

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

- **semicolon** · .agent/skills/the-worker/SKILL.md:422:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:437:200 · **recurring** · fingerprint: a67c2e85b92372da8a36a067
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is expected


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 470
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **long-sentence** · workspace/task_board.md:22:1 · **new** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 21
- **Hard findings:** 12
- **Baseline:** 0
- **Words:** 2030
- **Findings per 100 words:** 1.0

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

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:106:66 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:107:132 · **new** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:109:48 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:113:156 · **new** · fingerprint: 75a6091a01c4060c972ae09a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:115:4 · **new** · fingerprint: 06781e91b8c02b9bfbcc5637
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:118:165 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:120:27 · **new** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes

- **present-perfect** · .agent/skills/ci-ledger/SKILL.md:122:91 · **new** · fingerprint: e9e6a23d2f10dd7ba3a83f2d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has started

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:122:151 · **new** · fingerprint: c1fc8e55e266407cd9fce7f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:122:162 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:128:20 · **new** · fingerprint: 4b1b6661164047c147b88a63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:138:61 · **new** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:147:95 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required


### workspace/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 7
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 967
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · workspace/README.md:47:77 · **new** · fingerprint: 52ba35678185966f3e495ffc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/README.md:59:75 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · workspace/README.md:59:111 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/README.md:59:220 · **new** · fingerprint: bd41e95b24e62139f9055fb7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **passive-voice** · workspace/README.md:59:480 · **new** · fingerprint: eb43c2017cbbb6f4ef69df3f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

- **passive-voice** · workspace/README.md:63:202 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · workspace/README.md:63:277 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
