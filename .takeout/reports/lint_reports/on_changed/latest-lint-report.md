# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#829](https://github.com/dungnv2602/chatgpt/actions/runs/45903174690)
- **Run ID / attempt:** 45903174690 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 881a990d09a455534a392dfcaa5b2449baac3c22
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** d61d47cbcab8d691a076cb7302fa7f3c50804d2f
- **Linter source SHA:** 881a990d09a455534a392dfcaa5b2449baac3c22
- **Generated (UTC):** 2026-11-26T22:12:23.752669+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 4 |
| Hard findings | 4 |
| Advisory findings | 0 |
| New findings | 2 |
| Recurring findings | 2 |
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

- workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | FAIL | 4 | 4 | 0 | 3456 | 0.1 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 4 |

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
Ran 4 tests in 0.400s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.004s

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
Scanned 1 changed Markdown sources (332 available as link targets) and 1 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:90:102 · **new** · fingerprint: e65e3922aa38293af2adc5e0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** Delete
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:104 · **new** · fingerprint: c71ff84334a10d7dd38255c9
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

### Recurring findings

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:158:108 · **recurring** · fingerprint: 3f34a81299a3d18ae26e4279
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:159:149 · **recurring** · fingerprint: 563af8dd74cf1ba4bd074708
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

### Resolved findings

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:100:85 · **resolved** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:193:259 · **resolved** · fingerprint: f331458e480ad4445c592130
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .agent/skills/the-worker/SKILL.md:270:144 · **resolved** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:272:124 · **resolved** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:275:3 · **resolved** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words
- **long-sentence** · workspace/task_board.md:21:1 · **resolved** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 3456
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:90:102 · **new** · fingerprint: e65e3922aa38293af2adc5e0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** Delete

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:104 · **new** · fingerprint: c71ff84334a10d7dd38255c9
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:158:108 · **recurring** · fingerprint: 3f34a81299a3d18ae26e4279
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:159:149 · **recurring** · fingerprint: 563af8dd74cf1ba4bd074708
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
