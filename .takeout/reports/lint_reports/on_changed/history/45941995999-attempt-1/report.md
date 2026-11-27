# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#899](https://github.com/dungnv2602/chatgpt/actions/runs/45941995999)
- **Run ID / attempt:** 45941995999 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / ff7104f21cc2d82809004813cbb89c18615faf31
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 3b57ddb169167d8b3a450033c4a743a45e8c8fe8
- **Linter source SHA:** ff7104f21cc2d82809004813cbb89c18615faf31
- **Generated (UTC):** 2026-11-27T04:48:15.899632+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 1 |
| Files with findings | 2 |
| Total findings | 5 |
| Hard findings | 3 |
| Advisory findings | 2 |
| New findings | 1 |
| Recurring findings | 4 |
| Resolved findings | 1 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/references/conversation-mode.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/references/conversation-mode.md | PASS | 1 | 0 | 0 | 3215 | 0.0 | 0 |
| workspace/task_board.md | FAIL | 4 | 3 | 0 | 1387 | 0.3 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 2 |
| synonym-rotation | 2 |
| long-sentence | 1 |

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
Ran 4 tests in 0.345s

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
Scanned 2 changed Markdown sources (552 available as link targets) and 68 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:263 · **new** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

### Recurring findings

- **passive-voice** · workspace/task_board.md:5:336 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · workspace/task_board.md:41:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words
- **synonym-rotation** · workspace/task_board.md:67:41 · **recurring** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/task_board.md:99:88 · **recurring** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate

### Resolved findings

- **semicolon** · workspace/adr/README.md:72:170 · **resolved** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/references/conversation-mode.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 3215
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:263 · **new** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 1387
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:5:336 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **long-sentence** · workspace/task_board.md:41:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

- **synonym-rotation** · workspace/task_board.md:67:41 · **recurring** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · workspace/task_board.md:99:88 · **recurring** · fingerprint: e62ca06f23c949cf9f748c10
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
