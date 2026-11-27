# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#896](https://github.com/dungnv2602/chatgpt/actions/runs/45939776913)
- **Run ID / attempt:** 45939776913 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 0d4560f59f779819c5fb82cc53507a12526f4117
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 3ff28bcb5d9ff1bccffe69c4b79affa4082f3795
- **Linter source SHA:** 0d4560f59f779819c5fb82cc53507a12526f4117
- **Generated (UTC):** 2026-11-27T04:25:15.161461+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 7 |
| Hard findings | 6 |
| Advisory findings | 1 |
| New findings | 3 |
| Recurring findings | 4 |
| Resolved findings | 4 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/task_board.md
- .agent/skills/ci-ledger/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/task_board.md | FAIL | 4 | 3 | 0 | 1348 | 0.3 | 1 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 3 | 3 | 0 | 2264 | 0.1 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 5 |
| long-sentence | 1 |
| passive-voice | 1 |

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
Ran 4 tests in 0.362s

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
Scanned 2 changed Markdown sources (548 available as link targets) and 65 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **new** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:27 · **new** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **new** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

### Recurring findings

- **passive-voice** · workspace/task_board.md:5:336 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · workspace/task_board.md:34:41 · **recurring** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **long-sentence** · workspace/task_board.md:66:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words
- **synonym-rotation** · workspace/task_board.md:98:88 · **recurring** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate

### Resolved findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:295:144 · **resolved** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:196 · **resolved** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:414:513 · **resolved** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:416:708 · **resolved** · fingerprint: 9cca8e1414feae74d470296b
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 1348
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:5:336 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · workspace/task_board.md:34:41 · **recurring** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **long-sentence** · workspace/task_board.md:66:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

- **synonym-rotation** · workspace/task_board.md:98:88 · **recurring** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 2264
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **new** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:27 · **new** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes

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
