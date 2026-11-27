# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#965](https://github.com/dungnv2602/chatgpt/actions/runs/45977120769)
- **Run ID / attempt:** 45977120769 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 27824c83285f49522e578fa9ce4ea87403e931df
- **Source task:** 20261126-142500-02
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** f75ec2958ef664727a643062ef601400c0bcd45e
- **Linter source SHA:** 27824c83285f49522e578fa9ce4ea87403e931df
- **Generated (UTC):** 2026-11-27T09:53:14.245213+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 6 |
| Files that failed | 5 |
| Files with findings | 5 |
| Total findings | 38 |
| Hard findings | 20 |
| Advisory findings | 18 |
| New findings | 10 |
| Recurring findings | 28 |
| Resolved findings | 24 |
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
- .agent/skills/the-worker/SKILL.md
- .agent/skills/the-worker/references/conversation-mode.md
- workspace/task_board.md
- .agent/skills/ci-ledger/SKILL.md
- .agent/skills/asd-ste100/assets/lint-report-template.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/github-actions/SKILL.md | FAIL | 3 | 3 | 0 | 1864 | 0.2 | 1 |
| .agent/skills/the-worker/SKILL.md | FAIL | 13 | 8 | 0 | 1042 | 1.2 | 1 |
| .agent/skills/the-worker/references/conversation-mode.md | FAIL | 7 | 3 | 0 | 355 | 2.0 | 1 |
| workspace/task_board.md | FAIL | 8 | 2 | 0 | 321 | 2.5 | 1 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 7 | 4 | 0 | 724 | 1.0 | 1 |
| .agent/skills/asd-ste100/assets/lint-report-template.md | PASS | 0 | 0 | 0 | 389 | 0.0 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 16 |
| semicolon | 13 |
| synonym-rotation | 4 |
| long-sentence | 3 |
| present-perfect | 2 |

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
Ran 4 tests in 0.390s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.007s

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
Scanned 6 changed Markdown sources (351 available as link targets) and 1 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:40:96 · **new** · fingerprint: 00ff55742e1a76adf05e8f19
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **long-sentence** · .agent/skills/the-worker/SKILL.md:19:3 · **new** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:14:106 · **new** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:20:214 · **new** · fingerprint: 6ae9a6a4a2db5981a11a3382
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been collected
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:20:219 · **new** · fingerprint: bdeb60b7ecf5b8b23d08fe8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been collected
- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:26:339 · **new** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:26:365 · **new** · fingerprint: 20ab01d0763dc8b1779dc36e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:26:378 · **new** · fingerprint: bd4591524e78ee2f7fa8b868
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:30:156 · **new** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:54:146 · **new** · fingerprint: 59cc95b17372dc812b5f9dbd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned

### Recurring findings

- **semicolon** · .agent/skills/github-actions/SKILL.md:17:66 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/github-actions/SKILL.md:51:3 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:20:83 · **recurring** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:41:141 · **recurring** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/SKILL.md:47:10 · **recurring** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed
- **semicolon** · .agent/skills/the-worker/SKILL.md:49:169 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:52:41 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:53:29 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:54:16 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:91 · **recurring** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **semicolon** · .agent/skills/the-worker/SKILL.md:65:146 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:67:77 · **recurring** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · .agent/skills/the-worker/SKILL.md:69:53 · **recurring** · fingerprint: b336f74954a3548f82ab7c54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were executed
- **semicolon** · .agent/skills/the-worker/SKILL.md:69:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
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
- **passive-voice** · workspace/task_board.md:19:66 · **recurring** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed
- **passive-voice** · workspace/task_board.md:21:31 · **recurring** · fingerprint: bd8b55f1d04f97c603ef1aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconciled
- **semicolon** · workspace/task_board.md:21:204 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:21:224 · **recurring** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued
- **present-perfect** · workspace/task_board.md:31:27 · **recurring** · fingerprint: 9612c1c87b475ef28776a775
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been remediated
- **passive-voice** · workspace/task_board.md:31:32 · **recurring** · fingerprint: ad9a72b9a291435f0a3c005b
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
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:41:209 · **recurring** · fingerprint: c9e22528ce04a72820e83cd1
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:51:58 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:66:72 · **recurring** · fingerprint: 1f954c173b07804351eff72a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:66:75 · **recurring** · fingerprint: 7966f136f54c681540016f83
  - **Level:** advisory-free
  - **Message:** 'delete' and 'erase' name the same action. Pick one and use it every time.
  - **Matched text:** deleted

### Resolved findings

- **long-sentence** · .agent/skills/github-actions/SKILL.md:54:140 · **resolved** · fingerprint: 26126e68e07c3d0e59c329ee
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/github-actions/SKILL.md:54:323 · **resolved** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/github-actions/SKILL.md:70:430 · **resolved** · fingerprint: 75d03b744986296661ae3292
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/SKILL.md:13:124 · **resolved** · fingerprint: 30a5f5010d39a09d4d44c82a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:78:76 · **resolved** · fingerprint: 8ed72353c79e8cb075e2d945
  - **Level:** advisory-free
  - **Message:** 'start' and 'begin' name the same action. Pick one and use it every time.
  - **Matched text:** starting
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:43:131 · **resolved** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:44:275 · **resolved** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:131:297 · **resolved** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:143 · **resolved** · fingerprint: 42f86e8fba1534a97a0dd2a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:228 · **resolved** · fingerprint: de21f21791e1cf986fde4201
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:89 · **resolved** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:179 · **resolved** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **synonym-rotation** · .agent/skills/document-standards/references/document-type-catalog.md:213:206 · **resolved** · fingerprint: 4fc10f3be849a3fb43a60d2a
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · workspace/task_board.md:23:151 · **resolved** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **passive-voice** · workspace/TASK_TEMPLATE.md:23:182 · **resolved** · fingerprint: 174cb92f03c94b341eec0955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **semicolon** · workspace/TASK_TEMPLATE.md:76:135 · **resolved** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:76:153 · **resolved** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **semicolon** · workspace/README.md:13:41 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:22:210 · **resolved** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · workspace/README.md:23:104 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/README.md:32:224 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:42:209 · **resolved** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · workspace/README.md:42:220 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:63:88 · **resolved** · fingerprint: 7d67f86bef206623d83369e2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 1864
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **semicolon** · .agent/skills/github-actions/SKILL.md:17:66 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:40:96 · **new** · fingerprint: 00ff55742e1a76adf05e8f19
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **long-sentence** · .agent/skills/github-actions/SKILL.md:51:3 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 13
- **Hard findings:** 8
- **Baseline:** 0
- **Words:** 1042
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **long-sentence** · .agent/skills/the-worker/SKILL.md:19:3 · **new** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:20:83 · **recurring** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:41:141 · **recurring** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · .agent/skills/the-worker/SKILL.md:47:10 · **recurring** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed

- **semicolon** · .agent/skills/the-worker/SKILL.md:49:169 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:52:41 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:53:29 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:54:16 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:91 · **recurring** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **semicolon** · .agent/skills/the-worker/SKILL.md:65:146 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:67:77 · **recurring** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **passive-voice** · .agent/skills/the-worker/SKILL.md:69:53 · **recurring** · fingerprint: b336f74954a3548f82ab7c54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were executed

- **semicolon** · .agent/skills/the-worker/SKILL.md:69:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/the-worker/references/conversation-mode.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 355
- **Findings per 100 words:** 2.0

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:14:106 · **new** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:20:214 · **new** · fingerprint: 6ae9a6a4a2db5981a11a3382
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been collected

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:20:219 · **new** · fingerprint: bdeb60b7ecf5b8b23d08fe8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been collected

- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:26:339 · **new** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:26:365 · **new** · fingerprint: 20ab01d0763dc8b1779dc36e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:26:378 · **new** · fingerprint: bd4591524e78ee2f7fa8b868
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:30:156 · **new** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 321
- **Findings per 100 words:** 2.5

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

- **semicolon** · workspace/task_board.md:21:204 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:21:224 · **recurring** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued

- **present-perfect** · workspace/task_board.md:31:27 · **recurring** · fingerprint: 9612c1c87b475ef28776a775
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been remediated

- **passive-voice** · workspace/task_board.md:31:32 · **recurring** · fingerprint: ad9a72b9a291435f0a3c005b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been remediated


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 724
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:32:56 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:41:132 · **recurring** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:41:209 · **recurring** · fingerprint: c9e22528ce04a72820e83cd1
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:51:58 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:54:146 · **new** · fingerprint: 59cc95b17372dc812b5f9dbd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:66:72 · **recurring** · fingerprint: 1f954c173b07804351eff72a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:66:75 · **recurring** · fingerprint: 7966f136f54c681540016f83
  - **Level:** advisory-free
  - **Message:** 'delete' and 'erase' name the same action. Pick one and use it every time.
  - **Matched text:** deleted


### .agent/skills/asd-ste100/assets/lint-report-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 389
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
