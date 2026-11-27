# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#900](https://github.com/dungnv2602/chatgpt/actions/runs/45942426065)
- **Run ID / attempt:** 45942426065 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / eef01bf946dff4bcbfc285e2f07607271a896074
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** ff7104f21cc2d82809004813cbb89c18615faf31
- **Linter source SHA:** eef01bf946dff4bcbfc285e2f07607271a896074
- **Generated (UTC):** 2026-11-27T04:52:44.753345+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 2 |
| Files with findings | 3 |
| Total findings | 13 |
| Hard findings | 8 |
| Advisory findings | 5 |
| New findings | 9 |
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

- .agent/INITIALIZATION_POLICY.md
- .agent/SESSION_START.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/INITIALIZATION_POLICY.md | PASS | 1 | 1 | 4 | 1965 | 0.1 | 0 |
| .agent/SESSION_START.md | FAIL | 8 | 4 | 0 | 3002 | 0.3 | 1 |
| workspace/task_board.md | FAIL | 4 | 3 | 0 | 1391 | 0.3 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 6 |
| passive-voice | 4 |
| long-sentence | 2 |
| present-perfect | 1 |

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
Ran 4 tests in 0.351s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.006s

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
Scanned 3 changed Markdown sources (553 available as link targets) and 67 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/INITIALIZATION_POLICY.md:64:1 · **new** · fingerprint: 4e20a50af596bd1c8120efea
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** Retrieve
- **synonym-rotation** · .agent/SESSION_START.md:41:99 · **new** · fingerprint: b364e80e8c98116d3ebcfb38
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **synonym-rotation** · .agent/SESSION_START.md:53:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/SESSION_START.md:93:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:94:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · .agent/SESSION_START.md:238:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · .agent/SESSION_START.md:254:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · .agent/SESSION_START.md:279:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · .agent/SESSION_START.md:293:146 · **new** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates

### Recurring findings

- **passive-voice** · workspace/task_board.md:5:336 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · workspace/task_board.md:37:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
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

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:263 · **resolved** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/INITIALIZATION_POLICY.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 4
- **Words:** 1965
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · .agent/INITIALIZATION_POLICY.md:64:1 · **new** · fingerprint: 4e20a50af596bd1c8120efea
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** Retrieve


### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 3002
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **synonym-rotation** · .agent/SESSION_START.md:41:99 · **new** · fingerprint: b364e80e8c98116d3ebcfb38
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch

- **synonym-rotation** · .agent/SESSION_START.md:53:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · .agent/SESSION_START.md:93:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/SESSION_START.md:94:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **passive-voice** · .agent/SESSION_START.md:238:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **present-perfect** · .agent/SESSION_START.md:254:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed

- **long-sentence** · .agent/SESSION_START.md:279:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · .agent/SESSION_START.md:293:146 · **new** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 1391
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:5:336 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **long-sentence** · workspace/task_board.md:37:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
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
