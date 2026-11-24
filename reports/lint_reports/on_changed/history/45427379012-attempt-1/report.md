# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#641](https://github.com/dungnv2602/chatgpt/actions/runs/45427379012)
- **Run ID / attempt:** 45427379012 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / f3d11e25cdcc4335102725e51a5e4a20d1921753
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** e1c3f1804604e0b66d31437ded12e5711f199f96
- **Linter source SHA:** f3d11e25cdcc4335102725e51a5e4a20d1921753
- **Generated (UTC):** 2026-11-24T15:37:57.931607+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 5 |
| Hard findings | 5 |
| Advisory findings | 0 |
| New findings | 5 |
| Recurring findings | 0 |
| Resolved findings | 5 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md | FAIL | 5 | 5 | 0 | 5446 | 0.1 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| long-sentence | 2 |
| synonym-rotation | 2 |
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
Ran 4 tests in 0.287s

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

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:353:4 · **new** · fingerprint: b12cf7b98114051a3ef4ed4e
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:550:52 · **new** · fingerprint: 331ead622bd8b63c3dc8ec78
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:553:4 · **new** · fingerprint: 26959e3895827a98ea573e44
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:587:20 · **new** · fingerprint: 33dd6d895441c53e43bd10a2
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:602:90 · **new** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Recurring findings

None.

### Resolved findings

- **passive-voice** · workspace/adr/README.md:54:38 · **resolved** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/task_board.md:7:110 · **resolved** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/task_board.md:7:137 · **resolved** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · workspace/task_board.md:7:162 · **resolved** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/task_board.md:11:31 · **resolved** · fingerprint: ed2247bc287f94142d470682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 5
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 5446
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:353:4 · **new** · fingerprint: b12cf7b98114051a3ef4ed4e
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **synonym-rotation** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:550:52 · **new** · fingerprint: 331ead622bd8b63c3dc8ec78
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:553:4 · **new** · fingerprint: 26959e3895827a98ea573e44
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **long-sentence** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:587:20 · **new** · fingerprint: 33dd6d895441c53e43bd10a2
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words

- **semicolon** · workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md:602:90 · **new** · fingerprint: 0733dc3a8c16671792bda850
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
