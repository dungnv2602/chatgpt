# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#960](https://github.com/dungnv2602/chatgpt/actions/runs/45974724264)
- **Run ID / attempt:** 45974724264 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / f75ec2958ef664727a643062ef601400c0bcd45e
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** a57c0a6c71f74a486bb7e287d1f55add9931b313
- **Linter source SHA:** f75ec2958ef664727a643062ef601400c0bcd45e
- **Generated (UTC):** 2026-11-27T09:36:47.784752+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 8 |
| Files that failed | 7 |
| Files with findings | 8 |
| Total findings | 56 |
| Hard findings | 30 |
| Advisory findings | 26 |
| New findings | 28 |
| Recurring findings | 28 |
| Resolved findings | 59 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1018-aws-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/github-actions/SKILL.md
- .agent/skills/the-worker/SKILL.md
- .agent/skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md
- .agent/skills/ci-ledger/SKILL.md
- workspace/TASK_TEMPLATE.md
- workspace/README.md
- workspace/SUBTASK_TEMPLATE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/github-actions/SKILL.md | FAIL | 9 | 7 | 0 | 3083 | 0.3 | 1 |
| .agent/skills/the-worker/SKILL.md | FAIL | 14 | 8 | 0 | 1011 | 1.4 | 1 |
| .agent/skills/document-standards/references/document-type-catalog.md | FAIL | 8 | 4 | 0 | 4578 | 0.2 | 1 |
| workspace/task_board.md | FAIL | 9 | 2 | 0 | 327 | 2.8 | 1 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 6 | 4 | 0 | 707 | 0.8 | 1 |
| workspace/TASK_TEMPLATE.md | FAIL | 3 | 1 | 0 | 378 | 0.8 | 1 |
| workspace/README.md | FAIL | 6 | 4 | 0 | 493 | 1.2 | 1 |
| workspace/SUBTASK_TEMPLATE.md | PASS | 1 | 0 | 0 | 332 | 0.3 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 25 |
| semicolon | 21 |
| synonym-rotation | 5 |
| long-sentence | 4 |
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
Ran 4 tests in 0.235s

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
Scanned 8 changed Markdown sources (348 available as link targets) and 12 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:13:124 · **new** · fingerprint: 30a5f5010d39a09d4d44c82a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · .agent/skills/the-worker/SKILL.md:19:60 · **new** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:40:141 · **new** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/SKILL.md:46:10 · **new** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:64:91 · **new** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · .agent/skills/the-worker/SKILL.md:68:53 · **new** · fingerprint: b336f74954a3548f82ab7c54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were executed
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:78:76 · **new** · fingerprint: 8ed72353c79e8cb075e2d945
  - **Level:** advisory-free
  - **Message:** 'start' and 'begin' name the same action. Pick one and use it every time.
  - **Matched text:** starting
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:43:131 · **new** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:44:275 · **new** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:131:297 · **new** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:143 · **new** · fingerprint: 42f86e8fba1534a97a0dd2a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:228 · **new** · fingerprint: de21f21791e1cf986fde4201
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:89 · **new** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:179 · **new** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **synonym-rotation** · .agent/skills/document-standards/references/document-type-catalog.md:213:206 · **new** · fingerprint: 4fc10f3be849a3fb43a60d2a
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:41:209 · **new** · fingerprint: c9e22528ce04a72820e83cd1
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:66:72 · **new** · fingerprint: 1f954c173b07804351eff72a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:66:75 · **new** · fingerprint: 7966f136f54c681540016f83
  - **Level:** advisory-free
  - **Message:** 'delete' and 'erase' name the same action. Pick one and use it every time.
  - **Matched text:** deleted
- **passive-voice** · workspace/TASK_TEMPLATE.md:23:182 · **new** · fingerprint: 174cb92f03c94b341eec0955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **semicolon** · workspace/TASK_TEMPLATE.md:76:135 · **new** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:76:153 · **new** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **semicolon** · workspace/README.md:13:41 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:22:210 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · workspace/README.md:23:104 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/README.md:32:224 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:42:209 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · workspace/README.md:42:220 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:63:88 · **new** · fingerprint: 7d67f86bef206623d83369e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

### Recurring findings

- **semicolon** · .agent/skills/github-actions/SKILL.md:28:364 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/github-actions/SKILL.md:43:336 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/github-actions/SKILL.md:54:140 · **recurring** · fingerprint: 26126e68e07c3d0e59c329ee
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/github-actions/SKILL.md:54:323 · **recurring** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · .agent/skills/github-actions/SKILL.md:56:4 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/github-actions/SKILL.md:62:1 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:70:351 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/github-actions/SKILL.md:70:430 · **recurring** · fingerprint: 75d03b744986296661ae3292
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **long-sentence** · .agent/skills/github-actions/SKILL.md:78:3 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:48:169 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:51:41 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:52:29 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:53:16 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:64:146 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:66:77 · **recurring** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **semicolon** · .agent/skills/the-worker/SKILL.md:68:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:9:184 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:9:211 · **recurring** · fingerprint: 2576c78693220ab79f5566ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · workspace/task_board.md:21:66 · **recurring** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed
- **passive-voice** · workspace/task_board.md:23:31 · **recurring** · fingerprint: bd8b55f1d04f97c603ef1aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconciled
- **passive-voice** · workspace/task_board.md:23:151 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **semicolon** · workspace/task_board.md:23:211 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:23:231 · **recurring** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued
- **present-perfect** · workspace/task_board.md:33:27 · **recurring** · fingerprint: 9612c1c87b475ef28776a775
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been remediated
- **passive-voice** · workspace/task_board.md:33:32 · **recurring** · fingerprint: ad9a72b9a291435f0a3c005b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been remediated
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:32:56 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:41:132 · **recurring** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:51:58 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Resolved findings

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:125 · **resolved** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:205 · **resolved** · fingerprint: 71fd369fd4ce87f3145d3f61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are contained
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:42:32 · **resolved** · fingerprint: 0b78e160768da5f8fc81245e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are surfaced
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
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:94:221 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:96:302 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:97:90 · **resolved** · fingerprint: ae3383c2340edc8feecfe4eb
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirmd
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:111:162 · **resolved** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:116:3 · **resolved** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:125:143 · **resolved** · fingerprint: 298a9b83f5adba5f46527b78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:127:21 · **resolved** · fingerprint: f85e8d2b3bb15312e48006c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is confused
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:130:22 · **resolved** · fingerprint: 3c01363d8fccb6632309a933
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:41 · **resolved** · fingerprint: 0a8fdd51c323d7e6c5184e93
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:78 · **resolved** · fingerprint: f3f1d34b2d9fc9aa8def0bd1
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate
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
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:158:198 · **resolved** · fingerprint: 8b94e2d2ab83e942a9c53498
  - **Level:** advisory-free
  - **Message:** 'erase' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** erase
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:165:76 · **resolved** · fingerprint: 3f4020ebc1df4b02b6bc194e
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:174:3 · **resolved** · fingerprint: 95b3ae27d255dd6d3908c02c
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:175:109 · **resolved** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:184:44 · **resolved** · fingerprint: f0bb2234abbfaadfb9b32f17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:184:113 · **resolved** · fingerprint: e034604c115f5b656a6c5ab9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:201 · **resolved** · fingerprint: 6ecaad7e08b08c8dc23c4ac5
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** deletes
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:366 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:386 · **resolved** · fingerprint: 0ce56fdfcbc85adb0c649e73
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are inspected
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:214:190 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:219:98 · **resolved** · fingerprint: 4173039ab32cefe8e6332828
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:220:3 · **resolved** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:97:260 · **resolved** · fingerprint: e65e3922aa38293af2adc5e0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** Delete
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:99:87 · **resolved** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · .agent/skills/the-worker/SKILL.md:13:267 · **resolved** · fingerprint: 646b7bb10f9a4afa968e76a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · .agent/skills/the-worker/SKILL.md:34:286 · **resolved** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected
- **passive-voice** · .agent/skills/the-worker/SKILL.md:35:16 · **resolved** · fingerprint: 744124c649cfe9432abfa28d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are collected
- **long-sentence** · .agent/skills/the-worker/SKILL.md:36:67 · **resolved** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:136 · **resolved** · fingerprint: fbbd420487349088b9286d6b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are handled
- **passive-voice** · .agent/skills/the-worker/SKILL.md:38:116 · **resolved** · fingerprint: 15f03876d973741a8c5cb8e4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is completed
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:147 · **resolved** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:331 · **resolved** · fingerprint: 1b0e16e405ca623501c8a765
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:29 · **resolved** · fingerprint: a5d55557cb1399d0acf7ac08
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:167 · **resolved** · fingerprint: 741749aa0db79422e1509169
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **passive-voice** · .agent/skills/the-worker/SKILL.md:56:300 · **resolved** · fingerprint: 39ce18413ef5d1941ef0df0a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is omitted
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:56:319 · **resolved** · fingerprint: 4a50516b3278c464640d6067
  - **Level:** advisory-free
  - **Message:** 'initiate' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** initiate
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:17 · **resolved** · fingerprint: 485cc95c832398176cc2730f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:294 · **resolved** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:38:155 · **resolved** · fingerprint: a4e5c923c31ec30191d6b854
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is suppressed
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **resolved** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:110:143 · **resolved** · fingerprint: 0e62ca8d71819e8e8727168f
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:24 · **resolved** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:139:61 · **resolved** · fingerprint: 6f358d459967131650a4170d
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **resolved** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 7
- **Baseline:** 0
- **Words:** 3083
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · .agent/skills/github-actions/SKILL.md:28:364 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/github-actions/SKILL.md:43:336 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/github-actions/SKILL.md:54:140 · **recurring** · fingerprint: 26126e68e07c3d0e59c329ee
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/github-actions/SKILL.md:54:323 · **recurring** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **long-sentence** · .agent/skills/github-actions/SKILL.md:56:4 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · .agent/skills/github-actions/SKILL.md:62:1 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/github-actions/SKILL.md:70:351 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/github-actions/SKILL.md:70:430 · **recurring** · fingerprint: 75d03b744986296661ae3292
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **long-sentence** · .agent/skills/github-actions/SKILL.md:78:3 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 14
- **Hard findings:** 8
- **Baseline:** 0
- **Words:** 1011
- **Findings per 100 words:** 1.4

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:13:124 · **new** · fingerprint: 30a5f5010d39a09d4d44c82a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **passive-voice** · .agent/skills/the-worker/SKILL.md:19:60 · **new** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:40:141 · **new** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · .agent/skills/the-worker/SKILL.md:46:10 · **new** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed

- **semicolon** · .agent/skills/the-worker/SKILL.md:48:169 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:51:41 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:52:29 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:53:16 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:64:91 · **new** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **semicolon** · .agent/skills/the-worker/SKILL.md:64:146 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:66:77 · **recurring** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **passive-voice** · .agent/skills/the-worker/SKILL.md:68:53 · **new** · fingerprint: b336f74954a3548f82ab7c54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were executed

- **semicolon** · .agent/skills/the-worker/SKILL.md:68:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:78:76 · **new** · fingerprint: 8ed72353c79e8cb075e2d945
  - **Level:** advisory-free
  - **Message:** 'start' and 'begin' name the same action. Pick one and use it every time.
  - **Matched text:** starting


### .agent/skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 4578
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:43:131 · **new** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:44:275 · **new** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:131:297 · **new** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:143 · **new** · fingerprint: 42f86e8fba1534a97a0dd2a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:228 · **new** · fingerprint: de21f21791e1cf986fde4201
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:89 · **new** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:179 · **new** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted

- **synonym-rotation** · .agent/skills/document-standards/references/document-type-catalog.md:213:206 · **new** · fingerprint: 4fc10f3be849a3fb43a60d2a
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 327
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

- **passive-voice** · workspace/task_board.md:21:66 · **recurring** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed

- **passive-voice** · workspace/task_board.md:23:31 · **recurring** · fingerprint: bd8b55f1d04f97c603ef1aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconciled

- **passive-voice** · workspace/task_board.md:23:151 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

- **semicolon** · workspace/task_board.md:23:211 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:23:231 · **recurring** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued

- **present-perfect** · workspace/task_board.md:33:27 · **recurring** · fingerprint: 9612c1c87b475ef28776a775
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been remediated

- **passive-voice** · workspace/task_board.md:33:32 · **recurring** · fingerprint: ad9a72b9a291435f0a3c005b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been remediated


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 707
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:32:56 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:41:132 · **recurring** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:41:209 · **new** · fingerprint: c9e22528ce04a72820e83cd1
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:51:58 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:66:72 · **new** · fingerprint: 1f954c173b07804351eff72a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:66:75 · **new** · fingerprint: 7966f136f54c681540016f83
  - **Level:** advisory-free
  - **Message:** 'delete' and 'erase' name the same action. Pick one and use it every time.
  - **Matched text:** deleted


### workspace/TASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 378
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · workspace/TASK_TEMPLATE.md:23:182 · **new** · fingerprint: 174cb92f03c94b341eec0955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **semicolon** · workspace/TASK_TEMPLATE.md:76:135 · **new** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/TASK_TEMPLATE.md:76:153 · **new** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 493
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **semicolon** · workspace/README.md:13:41 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/README.md:22:210 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **semicolon** · workspace/README.md:23:104 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/README.md:32:224 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/README.md:42:209 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **semicolon** · workspace/README.md:42:220 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/SUBTASK_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 332
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:63:88 · **new** · fingerprint: 7d67f86bef206623d83369e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
