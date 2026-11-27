# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#953](https://github.com/dungnv2602/chatgpt/actions/runs/45970411285)
- **Run ID / attempt:** 45970411285 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / a57c0a6c71f74a486bb7e287d1f55add9931b313
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** bd89ad40440ee10c83b2e6a08770f082dc184fb3
- **Linter source SHA:** a57c0a6c71f74a486bb7e287d1f55add9931b313
- **Generated (UTC):** 2026-11-27T09:05:21.844369+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 6 |
| Files that failed | 6 |
| Files with findings | 6 |
| Total findings | 94 |
| Hard findings | 53 |
| Advisory findings | 41 |
| New findings | 50 |
| Recurring findings | 44 |
| Resolved findings | 2 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md
- workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md
- .agent/skills/github-actions/SKILL.md
- .agent/skills/the-worker/SKILL.md
- workspace/task_board.md
- .agent/skills/ci-ledger/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | FAIL | 37 | 17 | 0 | 3631 | 1.0 | 1 |
| workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | FAIL | 2 | 2 | 0 | 3478 | 0.1 | 1 |
| .agent/skills/github-actions/SKILL.md | FAIL | 8 | 6 | 0 | 3017 | 0.3 | 1 |
| .agent/skills/the-worker/SKILL.md | FAIL | 25 | 15 | 0 | 970 | 2.6 | 1 |
| workspace/task_board.md | FAIL | 9 | 2 | 0 | 324 | 2.8 | 1 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 13 | 11 | 0 | 2152 | 0.6 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 38 |
| semicolon | 24 |
| long-sentence | 15 |
| synonym-rotation | 14 |
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
Ran 4 tests in 0.227s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

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
Scanned 6 changed Markdown sources (352 available as link targets) and 1 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:201 · **new** · fingerprint: 6ecaad7e08b08c8dc23c4ac5
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** deletes
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:386 · **new** · fingerprint: 0ce56fdfcbc85adb0c649e73
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are inspected
- **semicolon** · .agent/skills/github-actions/SKILL.md:40:336 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/github-actions/SKILL.md:51:140 · **new** · fingerprint: 26126e68e07c3d0e59c329ee
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/github-actions/SKILL.md:51:323 · **new** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · .agent/skills/github-actions/SKILL.md:53:4 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/github-actions/SKILL.md:59:1 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:67:351 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/github-actions/SKILL.md:67:430 · **new** · fingerprint: 75d03b744986296661ae3292
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **long-sentence** · .agent/skills/github-actions/SKILL.md:75:3 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:5:170 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:7:296 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:13:238 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:13:267 · **new** · fingerprint: 646b7bb10f9a4afa968e76a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **semicolon** · .agent/skills/the-worker/SKILL.md:19:316 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:34:286 · **new** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected
- **passive-voice** · .agent/skills/the-worker/SKILL.md:35:16 · **new** · fingerprint: 744124c649cfe9432abfa28d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are collected
- **semicolon** · .agent/skills/the-worker/SKILL.md:35:108 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/SKILL.md:36:67 · **new** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:37:111 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:136 · **new** · fingerprint: fbbd420487349088b9286d6b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are handled
- **passive-voice** · .agent/skills/the-worker/SKILL.md:38:116 · **new** · fingerprint: 15f03876d973741a8c5cb8e4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is completed
- **semicolon** · .agent/skills/the-worker/SKILL.md:42:257 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:44:81 · **new** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:147 · **new** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **semicolon** · .agent/skills/the-worker/SKILL.md:52:322 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:331 · **new** · fingerprint: 1b0e16e405ca623501c8a765
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:29 · **new** · fingerprint: a5d55557cb1399d0acf7ac08
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:167 · **new** · fingerprint: 741749aa0db79422e1509169
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **passive-voice** · .agent/skills/the-worker/SKILL.md:56:300 · **new** · fingerprint: 39ce18413ef5d1941ef0df0a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is omitted
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:56:319 · **new** · fingerprint: 4a50516b3278c464640d6067
  - **Level:** advisory-free
  - **Message:** 'initiate' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** initiate
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:17 · **new** · fingerprint: 485cc95c832398176cc2730f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:294 · **new** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected
- **semicolon** · .agent/skills/the-worker/SKILL.md:62:232 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:62:275 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · workspace/task_board.md:31:27 · **new** · fingerprint: 9612c1c87b475ef28776a775
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been remediated
- **passive-voice** · workspace/task_board.md:31:32 · **new** · fingerprint: ad9a72b9a291435f0a3c005b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been remediated
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:38:155 · **new** · fingerprint: a4e5c923c31ec30191d6b854
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is suppressed
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:44:118 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **new** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:105:103 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:110:143 · **new** · fingerprint: 0e62ca8d71819e8e8727168f
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:110:198 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:110:582 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:114:28 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:117:261 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:117:286 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:24 · **new** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:139:61 · **new** · fingerprint: 6f358d459967131650a4170d
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **new** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

### Recurring findings

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:125 · **recurring** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:205 · **recurring** · fingerprint: 71fd369fd4ce87f3145d3f61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are contained
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:42:32 · **recurring** · fingerprint: 0b78e160768da5f8fc81245e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are surfaced
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:84:107 · **recurring** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:84:247 · **recurring** · fingerprint: 9997ef7899ffcdb243897741
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reviewed
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:86:3 · **recurring** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:177 · **recurring** · fingerprint: b29e4df2ee98e11a4663446d
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:364 · **recurring** · fingerprint: 9943dcb3a220dcbe0a08ff17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:533 · **recurring** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:94:221 · **recurring** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:96:302 · **recurring** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:97:90 · **recurring** · fingerprint: ae3383c2340edc8feecfe4eb
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirmd
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:111:162 · **recurring** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:116:3 · **recurring** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:125:143 · **recurring** · fingerprint: 298a9b83f5adba5f46527b78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:127:21 · **recurring** · fingerprint: f85e8d2b3bb15312e48006c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is confused
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:130:22 · **recurring** · fingerprint: 3c01363d8fccb6632309a933
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:41 · **recurring** · fingerprint: 0a8fdd51c323d7e6c5184e93
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:78 · **recurring** · fingerprint: f3f1d34b2d9fc9aa8def0bd1
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:145:206 · **recurring** · fingerprint: 579e397c39954135265f1d98
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:146:81 · **recurring** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:154:95 · **recurring** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:4 · **recurring** · fingerprint: 911fad1e156f4210f836f36c
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:69 · **recurring** · fingerprint: 14114c25a67a248bad384f1b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:214 · **recurring** · fingerprint: 9943dcb3a220dcbe0a08ff17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:158:198 · **recurring** · fingerprint: 8b94e2d2ab83e942a9c53498
  - **Level:** advisory-free
  - **Message:** 'erase' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** erase
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:165:76 · **recurring** · fingerprint: 3f4020ebc1df4b02b6bc194e
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:174:3 · **recurring** · fingerprint: 95b3ae27d255dd6d3908c02c
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:175:109 · **recurring** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:184:44 · **recurring** · fingerprint: f0bb2234abbfaadfb9b32f17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:184:113 · **recurring** · fingerprint: e034604c115f5b656a6c5ab9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:366 · **recurring** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:214:190 · **recurring** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:219:98 · **recurring** · fingerprint: 4173039ab32cefe8e6332828
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:220:3 · **recurring** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:97:260 · **recurring** · fingerprint: e65e3922aa38293af2adc5e0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** Delete
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:99:87 · **recurring** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **semicolon** · workspace/task_board.md:9:184 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:9:211 · **recurring** · fingerprint: 2576c78693220ab79f5566ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · workspace/task_board.md:19:66 · **recurring** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed
- **passive-voice** · workspace/task_board.md:21:31 · **recurring** · fingerprint: bd8b55f1d04f97c603ef1aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconciled
- **passive-voice** · workspace/task_board.md:21:151 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **semicolon** · workspace/task_board.md:21:211 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:21:231 · **recurring** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued

### Resolved findings

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:100 · **resolved** · fingerprint: e9365b9cbb59d135219ec64e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed
- **passive-voice** · workspace/task_board.md:56:97 · **resolved** · fingerprint: d8beb3526c98bbf7b37d724b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 37
- **Hard findings:** 17
- **Baseline:** 0
- **Words:** 3631
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:125 · **recurring** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:205 · **recurring** · fingerprint: 71fd369fd4ce87f3145d3f61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are contained

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:42:32 · **recurring** · fingerprint: 0b78e160768da5f8fc81245e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are surfaced

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:84:107 · **recurring** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:84:247 · **recurring** · fingerprint: 9997ef7899ffcdb243897741
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reviewed

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:86:3 · **recurring** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:177 · **recurring** · fingerprint: b29e4df2ee98e11a4663446d
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:364 · **recurring** · fingerprint: 9943dcb3a220dcbe0a08ff17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:533 · **recurring** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:94:221 · **recurring** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:96:302 · **recurring** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:97:90 · **recurring** · fingerprint: ae3383c2340edc8feecfe4eb
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirmd

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:111:162 · **recurring** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:116:3 · **recurring** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:125:143 · **recurring** · fingerprint: 298a9b83f5adba5f46527b78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:127:21 · **recurring** · fingerprint: f85e8d2b3bb15312e48006c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is confused

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:130:22 · **recurring** · fingerprint: 3c01363d8fccb6632309a933
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:41 · **recurring** · fingerprint: 0a8fdd51c323d7e6c5184e93
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:78 · **recurring** · fingerprint: f3f1d34b2d9fc9aa8def0bd1
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:145:206 · **recurring** · fingerprint: 579e397c39954135265f1d98
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:146:81 · **recurring** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:154:95 · **recurring** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:4 · **recurring** · fingerprint: 911fad1e156f4210f836f36c
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:69 · **recurring** · fingerprint: 14114c25a67a248bad384f1b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:214 · **recurring** · fingerprint: 9943dcb3a220dcbe0a08ff17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:158:198 · **recurring** · fingerprint: 8b94e2d2ab83e942a9c53498
  - **Level:** advisory-free
  - **Message:** 'erase' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** erase

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:165:76 · **recurring** · fingerprint: 3f4020ebc1df4b02b6bc194e
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:174:3 · **recurring** · fingerprint: 95b3ae27d255dd6d3908c02c
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:175:109 · **recurring** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:184:44 · **recurring** · fingerprint: f0bb2234abbfaadfb9b32f17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:184:113 · **recurring** · fingerprint: e034604c115f5b656a6c5ab9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:201 · **new** · fingerprint: 6ecaad7e08b08c8dc23c4ac5
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** deletes

- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:366 · **recurring** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:386 · **new** · fingerprint: 0ce56fdfcbc85adb0c649e73
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are inspected

- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:214:190 · **recurring** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:219:98 · **recurring** · fingerprint: 4173039ab32cefe8e6332828
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:220:3 · **recurring** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words


### workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 3478
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:97:260 · **recurring** · fingerprint: e65e3922aa38293af2adc5e0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** Delete

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:99:87 · **recurring** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks


### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 6
- **Baseline:** 0
- **Words:** 3017
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · .agent/skills/github-actions/SKILL.md:40:336 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/github-actions/SKILL.md:51:140 · **new** · fingerprint: 26126e68e07c3d0e59c329ee
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/github-actions/SKILL.md:51:323 · **new** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **long-sentence** · .agent/skills/github-actions/SKILL.md:53:4 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · .agent/skills/github-actions/SKILL.md:59:1 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/github-actions/SKILL.md:67:351 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/github-actions/SKILL.md:67:430 · **new** · fingerprint: 75d03b744986296661ae3292
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **long-sentence** · .agent/skills/github-actions/SKILL.md:75:3 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 25
- **Hard findings:** 15
- **Baseline:** 0
- **Words:** 970
- **Findings per 100 words:** 2.6

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/SKILL.md:5:170 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:7:296 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:13:238 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:13:267 · **new** · fingerprint: 646b7bb10f9a4afa968e76a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **semicolon** · .agent/skills/the-worker/SKILL.md:19:316 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:34:286 · **new** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected

- **passive-voice** · .agent/skills/the-worker/SKILL.md:35:16 · **new** · fingerprint: 744124c649cfe9432abfa28d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are collected

- **semicolon** · .agent/skills/the-worker/SKILL.md:35:108 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/SKILL.md:36:67 · **new** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · .agent/skills/the-worker/SKILL.md:37:111 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:136 · **new** · fingerprint: fbbd420487349088b9286d6b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are handled

- **passive-voice** · .agent/skills/the-worker/SKILL.md:38:116 · **new** · fingerprint: 15f03876d973741a8c5cb8e4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is completed

- **semicolon** · .agent/skills/the-worker/SKILL.md:42:257 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:44:81 · **new** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:147 · **new** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **semicolon** · .agent/skills/the-worker/SKILL.md:52:322 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:331 · **new** · fingerprint: 1b0e16e405ca623501c8a765
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix

- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:29 · **new** · fingerprint: a5d55557cb1399d0acf7ac08
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received

- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:167 · **new** · fingerprint: 741749aa0db79422e1509169
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **passive-voice** · .agent/skills/the-worker/SKILL.md:56:300 · **new** · fingerprint: 39ce18413ef5d1941ef0df0a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is omitted

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:56:319 · **new** · fingerprint: 4a50516b3278c464640d6067
  - **Level:** advisory-free
  - **Message:** 'initiate' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** initiate

- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:17 · **new** · fingerprint: 485cc95c832398176cc2730f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:294 · **new** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected

- **semicolon** · .agent/skills/the-worker/SKILL.md:62:232 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:62:275 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 324
- **Findings per 100 words:** 2.8

#### Complete diagnostics

- **semicolon** · workspace/task_board.md:9:184 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:9:211 · **recurring** · fingerprint: 2576c78693220ab79f5566ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **passive-voice** · workspace/task_board.md:19:66 · **recurring** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed

- **passive-voice** · workspace/task_board.md:21:31 · **recurring** · fingerprint: bd8b55f1d04f97c603ef1aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconciled

- **passive-voice** · workspace/task_board.md:21:151 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

- **semicolon** · workspace/task_board.md:21:211 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:21:231 · **recurring** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued

- **present-perfect** · workspace/task_board.md:31:27 · **new** · fingerprint: 9612c1c87b475ef28776a775
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been remediated

- **passive-voice** · workspace/task_board.md:31:32 · **new** · fingerprint: ad9a72b9a291435f0a3c005b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been remediated


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 13
- **Hard findings:** 11
- **Baseline:** 0
- **Words:** 2152
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:38:155 · **new** · fingerprint: a4e5c923c31ec30191d6b854
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is suppressed

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:44:118 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **new** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:105:103 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:110:143 · **new** · fingerprint: 0e62ca8d71819e8e8727168f
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:110:198 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:110:582 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:114:28 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:117:261 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:117:286 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:24 · **new** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:139:61 · **new** · fingerprint: 6f358d459967131650a4170d
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **new** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
