# On Changed STE Lint Evidence Report

- **Result:** Passed
- **Schema version:** 1.1.0
- **Run:** [#673](https://github.com/dungnv2602/chatgpt/actions/runs/45455441513)
- **Run ID / attempt:** 45455441513 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 2d99f8228644c2c25c957f4dbd195325d620d6d2
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 1c63b0e97e4e94fd298d4f4e753f1c848877e479
- **Linter source SHA:** 2d99f8228644c2c25c957f4dbd195325d620d6d2
- **Generated (UTC):** 2026-11-24T18:05:38.328408+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 0 |
| Files with findings | 0 |
| Total findings | 0 |
| Hard findings | 0 |
| Advisory findings | 0 |
| New findings | 0 |
| Recurring findings | 0 |
| Resolved findings | 6 |
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
- workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/task_board.md | PASS | 0 | 0 | 0 | 1440 | 0.0 | 0 |
| workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md | PASS | 0 | 0 | 0 | 2803 | 0.0 | 0 |

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
Ran 4 tests in 0.272s

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

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:94:29 · **resolved** · fingerprint: 2b26cf53803b151c21212120
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:122:162 · **resolved** · fingerprint: 44fcd3dad59ced40bc859413
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:133:33 · **resolved** · fingerprint: 7614765438b1a170a448306a
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:153:44 · **resolved** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:161:127 · **resolved** · fingerprint: beb9ea53ee058f3d9e59ec0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:193:1 · **resolved** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1440
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 2803
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
