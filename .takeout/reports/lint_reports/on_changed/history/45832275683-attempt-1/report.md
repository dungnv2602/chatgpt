# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#808](https://github.com/dungnv2602/chatgpt/actions/runs/45832275683)
- **Run ID / attempt:** 45832275683 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / b41d486cfa8b094be9d810707262878485e219bc
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 1990c8ac733f7ae9a9947f97772822fb7e00edde
- **Linter source SHA:** b41d486cfa8b094be9d810707262878485e219bc
- **Generated (UTC):** 2026-11-26T13:46:24.179536+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 4 |
| Hard findings | 4 |
| Advisory findings | 0 |
| New findings | 0 |
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

- .agent/skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/document-standards/references/document-type-catalog.md | FAIL | 1 | 1 | 0 | 4625 | 0.0 | 1 |
| workspace/task_board.md | FAIL | 3 | 3 | 0 | 291 | 1.0 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 3 |
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
Ran 4 tests in 0.343s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.005s

OK
~~~

### STE linter self-test

- **Result:** Passed
- **Exit code:** 0

~~~text
selftest OK
~~~

### Markdown links and heading anchors

- **Result:** Skipped
- **Exit code:** Unknown

~~~text
Not required for this incremental run.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:126:145 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/task_board.md:21:38 · **recurring** · fingerprint: f8874d55207a198913c99e59
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/task_board.md:23:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **synonym-rotation** · workspace/task_board.md:34:21 · **recurring** · fingerprint: 7cb82e69e7844d17f868b2a2
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Repair

### Resolved findings

- **long-sentence** · .agent/skills/document-standards/references/document-type-catalog.md:45:121 · **resolved** · fingerprint: 2dd7b3784611553473e6528c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:191 · **resolved** · fingerprint: 3ae524e22114a03c0ab4422a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:228 · **resolved** · fingerprint: 2115664c682d98befee7c6f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is tracked
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:143 · **resolved** · fingerprint: 3d0eb996eb2ac7266bac89b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are restored

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 4625
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:126:145 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 291
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:21:38 · **recurring** · fingerprint: f8874d55207a198913c99e59
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · workspace/task_board.md:23:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **synonym-rotation** · workspace/task_board.md:34:21 · **recurring** · fingerprint: 7cb82e69e7844d17f868b2a2
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Repair

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
