# On Changed STE Lint Evidence Report

- **Result:** Passed
- **Schema version:** 1.2.0
- **Run:** [#1019](https://github.com/dungnv2602/chatgpt/actions/runs/46015025342)
- **Run ID / attempt:** 46015025342 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 7744b9fccf0f5671054a0e9d4031c0bb3ff1ab29
- **Source task:** 20261127-173000-51
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 2248c282fc86076a5a48b4493862beadeb2025a8
- **Linter source SHA:** 7744b9fccf0f5671054a0e9d4031c0bb3ff1ab29
- **Generated (UTC):** 2026-11-27T14:20:54.816264+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 0 |
| Files with findings | 1 |
| Total findings | 3 |
| Hard findings | 0 |
| Advisory findings | 3 |
| New findings | 3 |
| Recurring findings | 0 |
| Resolved findings | 7 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/assets/actions-report-template.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/assets/actions-report-template.md | PASS | 3 | 0 | 0 | 156 | 1.9 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 3 |

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
......
----------------------------------------------------------------------
Ran 6 tests in 0.390s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.029s

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
Scanned 1 changed Markdown sources (444 available as link targets) and 0 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/skills/the-worker/assets/actions-report-template.md:15:175 · **new** · fingerprint: c4694e88f04cd654220cc23d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · .agent/skills/the-worker/assets/actions-report-template.md:15:263 · **new** · fingerprint: c4694e88f04cd654220cc23d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · .agent/skills/the-worker/assets/actions-report-template.md:15:393 · **new** · fingerprint: 4d345e231ac14cad2ca77be0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are excluded

### Recurring findings

None.

### Resolved findings

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:87:19 · **resolved** · fingerprint: 4900e43fc0a2db0bbbee87ae
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · .agent/skills/the-worker/SKILL.md:173:47 · **resolved** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:183:108 · **resolved** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **long-sentence** · .agent/skills/the-worker/references/github-actions.md:45:3 · **resolved** · fingerprint: 933a579fb10c54b6f0b0201a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **synonym-rotation** · workspace/task_board.md:73:24 · **resolved** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/task_board.md:73:113 · **resolved** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:64:235 · **resolved** · fingerprint: aa0de8573960d54a21c2d1d2
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/assets/actions-report-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 156
- **Findings per 100 words:** 1.9

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/assets/actions-report-template.md:15:175 · **new** · fingerprint: c4694e88f04cd654220cc23d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **passive-voice** · .agent/skills/the-worker/assets/actions-report-template.md:15:263 · **new** · fingerprint: c4694e88f04cd654220cc23d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **passive-voice** · .agent/skills/the-worker/assets/actions-report-template.md:15:393 · **new** · fingerprint: 4d345e231ac14cad2ca77be0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are excluded

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
