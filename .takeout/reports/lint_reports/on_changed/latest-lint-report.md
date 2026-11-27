# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#1016](https://github.com/dungnv2602/chatgpt/actions/runs/46008770801)
- **Run ID / attempt:** 46008770801 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / feb9767d6a61ce9d32cd53b251afaace810ca515
- **Source task:** 20261127-173000-26
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 80440b3c6a81e440826071a66dd9f9c3a3e38747
- **Linter source SHA:** feb9767d6a61ce9d32cd53b251afaace810ca515
- **Generated (UTC):** 2026-11-27T13:38:18.716138+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 5 |
| Hard findings | 2 |
| Advisory findings | 3 |
| New findings | 3 |
| Recurring findings | 2 |
| Resolved findings | 3 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/SESSION_START.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/SESSION_START.md | FAIL | 3 | 1 | 0 | 2945 | 0.1 | 1 |
| workspace/task_board.md | FAIL | 2 | 1 | 0 | 1128 | 0.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 2 |
| synonym-rotation | 2 |
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
......
----------------------------------------------------------------------
Ran 6 tests in 0.303s

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

- **Result:** Failed
- **Exit code:** 1

~~~text
Scanned 2 changed Markdown sources (439 available as link targets) and 31 local Markdown links.
Found 23 unresolved local Markdown targets or anchors.
workspace/task_board.md: missing Markdown file: 27-ci-remediation-review-passive-voice-findings-in-workspace-readme-md.md
workspace/task_board.md: missing Markdown file: 28-ci-remediation-review-marketing-adjective-findings-in-agent-skills-asd-ste100-s.md
workspace/task_board.md: missing Markdown file: 29-ci-remediation-review-nominalization-findings-in-agent-skills-asd-ste100-skill.md
workspace/task_board.md: missing Markdown file: 30-ci-remediation-review-present-perfect-findings-in-agent-skills-asd-ste100-skill.md
workspace/task_board.md: missing Markdown file: 31-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-references.md
workspace/task_board.md: missing Markdown file: 32-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-referen.md
workspace/task_board.md: missing Markdown file: 33-ci-remediation-review-present-perfect-findings-in-agent-session-start-md.md
workspace/task_board.md: missing Markdown file: 34-ci-remediation-review-synonym-rotation-findings-in-workspace-adr-0003-canonical.md
workspace/task_board.md: missing Markdown file: 35-ci-remediation-review-semicolon-findings-in-workspace-task-template-md.md
workspace/task_board.md: missing Markdown file: 36-ci-remediation-review-passive-voice-findings-in-workspace-subtask-template-md.md
workspace/task_board.md: missing Markdown file: 37-ci-remediation-review-semicolon-findings-in-workspace-adr-0004-task-folders-sub.md
workspace/task_board.md: missing Markdown file: 38-ci-remediation-review-passive-voice-findings-in-workspace-task-template-md.md
workspace/task_board.md: missing Markdown file: 39-ci-remediation-review-synonym-rotation-findings-in-workspace-adr-0004-task-fold.md
workspace/task_board.md: missing Markdown file: 40-ci-remediation-review-passive-voice-findings-in-workspace-adr-0004-task-folders.md
workspace/task_board.md: missing Markdown file: 41-ci-remediation-review-long-sentence-findings-in-workspace-adr-0004-task-folders.md
workspace/task_board.md: missing Markdown file: 42-ci-remediation-review-passive-voice-findings-in-workspace-adr-0001-establish-dr.md
workspace/task_board.md: missing Markdown file: 43-ci-remediation-review-semicolon-findings-in-workspace-subtask-template-md.md
workspace/task_board.md: missing Markdown file: 44-ci-remediation-review-semicolon-findings-in-workspace-adr-0001-establish-draft.md
workspace/task_board.md: missing Markdown file: 45-ci-remediation-review-semicolon-findings-in-workspace-adr-readme-md.md
workspace/task_board.md: missing Markdown file: 46-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md
workspace/task_board.md: missing Markdown file: 47-ci-remediation-review-passive-voice-findings-in-agent-skills-asd-ste100-referen.md
workspace/task_board.md: missing Markdown file: 48-ci-remediation-review-synonym-rotation-findings-in-agent-skills-agent-skill-aut.md
workspace/task_board.md: missing Markdown file: 49-ci-remediation-review-passive-voice-findings-in-workspace-task-board-md.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/SESSION_START.md:22:209 · **new** · fingerprint: 00654de2a95772d4a870e55f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being fetched
- **synonym-rotation** · .agent/SESSION_START.md:177:7 · **new** · fingerprint: 93101ce1787c7b9208b4031d
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** retrieved
- **present-perfect** · .agent/SESSION_START.md:253:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed

### Recurring findings

- **synonym-rotation** · workspace/task_board.md:67:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/task_board.md:67:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Resolved findings

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:43:131 · **resolved** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:44:275 · **resolved** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:131:297 · **resolved** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 2945
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · .agent/SESSION_START.md:22:209 · **new** · fingerprint: 00654de2a95772d4a870e55f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being fetched

- **synonym-rotation** · .agent/SESSION_START.md:177:7 · **new** · fingerprint: 93101ce1787c7b9208b4031d
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** retrieved

- **present-perfect** · .agent/SESSION_START.md:253:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1128
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:67:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **passive-voice** · workspace/task_board.md:67:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
