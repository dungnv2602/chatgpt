# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#715](https://github.com/dungnv2602/chatgpt/actions/runs/45744913427)
- **Run ID / attempt:** 45744913427 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 8bd3effd90a5cce8c3b1d4f802838bd844adef37
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** c91c7dedd734c09c21ab765c169aadc83dc408e9
- **Linter source SHA:** 8bd3effd90a5cce8c3b1d4f802838bd844adef37
- **Generated (UTC):** 2026-11-26T02:50:49.707859+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 5 |
| Files that failed | 5 |
| Files with findings | 0 |
| Total findings | 0 |
| Hard findings | 0 |
| Advisory findings | 0 |
| New findings | 0 |
| Recurring findings | 0 |
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

- .agent/skills/the-worker/references/image-provenance-and-webp.md
- .agent/skills/drawing/references/archive-and-delivery.md
- .agent/skills/document-standards/references/document-type-catalog.md
- .takeout/images/README-1.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/references/image-provenance-and-webp.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/drawing/references/archive-and-delivery.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .agent/skills/document-standards/references/document-type-catalog.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| .takeout/images/README-1.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |
| workspace/task_board.md | FAIL | 0 | 0 | 0 | 0 | 0 | 2 |

## 5. Findings by rule

Counts include hard and advisory findings.

No findings.

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
Ran 4 tests in 0.366s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

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

None.

### Resolved findings

None.

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/references/image-provenance-and-webp.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/drawing/references/archive-and-delivery.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .agent/skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### .takeout/images/README-1.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 2
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 0
- **Findings per 100 words:** 0

**Capture error:**

~~~text
python3: can't open file '/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/ste-lint.py': [Errno 2] No such file or directory
~~~

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
