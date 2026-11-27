# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#947](https://github.com/dungnv2602/chatgpt/actions/runs/45968726096)
- **Run ID / attempt:** 45968726096 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / bd89ad40440ee10c83b2e6a08770f082dc184fb3
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 7fd5385e0be58b1b86f105e1c9dd8f214021d677
- **Linter source SHA:** bd89ad40440ee10c83b2e6a08770f082dc184fb3
- **Generated (UTC):** 2026-11-27T08:51:19.367024+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 3 |
| Files with findings | 3 |
| Total findings | 44 |
| Hard findings | 18 |
| Advisory findings | 26 |
| New findings | 14 |
| Recurring findings | 30 |
| Resolved findings | 9 |
| Failed workflow checks | 2 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md
- workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md | FAIL | 34 | 14 | 0 | 3593 | 0.9 | 1 |
| workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | FAIL | 2 | 2 | 0 | 3475 | 0.1 | 1 |
| workspace/task_board.md | FAIL | 8 | 2 | 0 | 465 | 1.7 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 26 |
| long-sentence | 8 |
| synonym-rotation | 6 |
| semicolon | 4 |

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
Ran 4 tests in 0.310s

OK
~~~

### Markdown anchor regression tests

- **Result:** Failed
- **Exit code:** 1

~~~~~~~~~~~~~~~~~~~~~~~text
..F.....
======================================================================
FAIL: test_incremental_scope_rejects_inactive_or_untracked_sources (__main__.MarkdownAnchorTests.test_incremental_scope_rejects_inactive_or_untracked_sources) (path='.archive/adr/old.md')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_check_markdown_anchors.py", line 80, in test_incremental_scope_rejects_inactive_or_untracked_sources
    with self.assertRaisesRegex(ValueError, "inactive or untracked"):
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 8 tests in 0.006s

FAILED (failures=1)
~~~~~~~~~~~~~~~~~~~~~~~

### STE linter self-test

- **Result:** Passed
- **Exit code:** 0

~~~text
selftest OK
~~~

### Markdown links and heading anchors

- **Result:** Failed
- **Exit code:** 1

~~~text
Scanned 3 changed Markdown sources (372 available as link targets) and 11 local Markdown links.
Found 1 unresolved local Markdown targets or anchors.
workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md: missing Markdown file: ./tasks/20261126-090154-review-validation-or-test-failures-in-confirm-document-standard.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:94:221 · **new** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:97:90 · **new** · fingerprint: ae3383c2340edc8feecfe4eb
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirmd
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:78 · **new** · fingerprint: f3f1d34b2d9fc9aa8def0bd1
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:165:76 · **new** · fingerprint: 3f4020ebc1df4b02b6bc194e
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:214:190 · **new** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:100:87 · **new** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **semicolon** · workspace/task_board.md:9:184 · **new** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:9:211 · **new** · fingerprint: 2576c78693220ab79f5566ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · workspace/task_board.md:19:66 · **new** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed
- **passive-voice** · workspace/task_board.md:21:31 · **new** · fingerprint: bd8b55f1d04f97c603ef1aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconciled
- **passive-voice** · workspace/task_board.md:21:151 · **new** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **semicolon** · workspace/task_board.md:21:228 · **new** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:21:248 · **new** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued
- **passive-voice** · workspace/task_board.md:56:97 · **new** · fingerprint: d8beb3526c98bbf7b37d724b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied

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
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:111:162 · **recurring** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
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
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:100 · **recurring** · fingerprint: e9365b9cbb59d135219ec64e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:219:98 · **recurring** · fingerprint: 4173039ab32cefe8e6332828
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:220:3 · **recurring** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:98:260 · **recurring** · fingerprint: e65e3922aa38293af2adc5e0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** Delete

### Resolved findings

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:83:120 · **resolved** · fingerprint: f344f235da524619c5f3958e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are represented
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:96:215 · **resolved** · fingerprint: d88c984bfabc22fedfc1df95
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
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
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:62 · **resolved** · fingerprint: ef0a8b26b3bc52102db6f7e1
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:165:76 · **resolved** · fingerprint: 3c057ccfc90ea7e884e85446
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:104 · **resolved** · fingerprint: c71ff84334a10d7dd38255c9
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 34
- **Hard findings:** 14
- **Baseline:** 0
- **Words:** 3593
- **Findings per 100 words:** 0.9

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

- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:94:221 · **new** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:97:90 · **new** · fingerprint: ae3383c2340edc8feecfe4eb
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirmd

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:111:162 · **recurring** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

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

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:78 · **new** · fingerprint: f3f1d34b2d9fc9aa8def0bd1
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

- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:165:76 · **new** · fingerprint: 3f4020ebc1df4b02b6bc194e
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

- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:100 · **recurring** · fingerprint: e9365b9cbb59d135219ec64e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed

- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:214:190 · **new** · fingerprint: 235b8a3528fa8a066c7b86a4
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
- **Words:** 3475
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:98:260 · **recurring** · fingerprint: e65e3922aa38293af2adc5e0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** Delete

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:100:87 · **new** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 465
- **Findings per 100 words:** 1.7

#### Complete diagnostics

- **semicolon** · workspace/task_board.md:9:184 · **new** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:9:211 · **new** · fingerprint: 2576c78693220ab79f5566ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **passive-voice** · workspace/task_board.md:19:66 · **new** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed

- **passive-voice** · workspace/task_board.md:21:31 · **new** · fingerprint: bd8b55f1d04f97c603ef1aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconciled

- **passive-voice** · workspace/task_board.md:21:151 · **new** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

- **semicolon** · workspace/task_board.md:21:228 · **new** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:21:248 · **new** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued

- **passive-voice** · workspace/task_board.md:56:97 · **new** · fingerprint: d8beb3526c98bbf7b37d724b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
