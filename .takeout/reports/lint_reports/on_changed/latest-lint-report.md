# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#814](https://github.com/dungnv2602/chatgpt/actions/runs/45843115356)
- **Run ID / attempt:** 45843115356 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 10d05fb67773a7c244bf8c175fe4cf0a6b000f40
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** c3ef2c4dc0635033c5cebaef0b7624af3b2fccb6
- **Linter source SHA:** 10d05fb67773a7c244bf8c175fe4cf0a6b000f40
- **Generated (UTC):** 2026-11-26T14:51:58.858989+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 1 |
| Hard findings | 1 |
| Advisory findings | 0 |
| New findings | 1 |
| Recurring findings | 0 |
| Resolved findings | 2 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1018-aws-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/task_board.md
- workspace/draft/README.md
- workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/task_board.md | PASS | 0 | 0 | 0 | 427 | 0.0 | 0 |
| workspace/draft/README.md | PASS | 0 | 0 | 0 | 663 | 0.0 | 0 |
| workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md | FAIL | 1 | 1 | 0 | 9015 | 0.0 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 1 |

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
Ran 4 tests in 0.228s

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
Scanned 3 changed Markdown sources (327 available as link targets) and 22 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:241:148 · **new** · fingerprint: 1ba75e66fd8777920c74a662
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validates

### Recurring findings

None.

### Resolved findings

- **synonym-rotation** · workspace/task_board.md:30:61 · **resolved** · fingerprint: fe0043dd1c2c55650b8f76ae
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:216:73 · **resolved** · fingerprint: 5c822b17641bfca685187467
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validate

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 427
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/draft/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 663
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 9015
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:241:148 · **new** · fingerprint: 1ba75e66fd8777920c74a662
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validates

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
