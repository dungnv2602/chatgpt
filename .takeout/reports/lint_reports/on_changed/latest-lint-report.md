# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#1003](https://github.com/dungnv2602/chatgpt/actions/runs/46003913637)
- **Run ID / attempt:** 46003913637 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / eb780b92aa048fdaf2c9bc6a1e1783c8bc2adceb
- **Source task:** 20261127-173000-11
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 8324ee76f6ba30cbe04ca8b82414b2d51e98cdd0
- **Linter source SHA:** eb780b92aa048fdaf2c9bc6a1e1783c8bc2adceb
- **Generated (UTC):** 2026-11-27T13:04:56.091255+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 1 |
| Files with findings | 2 |
| Total findings | 3 |
| Hard findings | 2 |
| Advisory findings | 1 |
| New findings | 1 |
| Recurring findings | 2 |
| Resolved findings | 2 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/agent-skill-authoring/SKILL.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/agent-skill-authoring/SKILL.md | PASS | 1 | 1 | 6 | 2256 | 0.0 | 0 |
| workspace/task_board.md | FAIL | 2 | 1 | 0 | 1604 | 0.1 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 2 |
| passive-voice | 1 |

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
Ran 6 tests in 0.477s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.007s

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
Scanned 2 changed Markdown sources (440 available as link targets) and 46 local Markdown links.
Found 37 unresolved local Markdown targets or anchors.
workspace/task_board.md: missing Markdown file: 12-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-skill-md.md
workspace/task_board.md: missing Markdown file: 13-ci-remediation-review-synonym-rotation-findings-in-agent-session-start-md.md
workspace/task_board.md: missing Markdown file: 14-ci-remediation-review-phrasal-verb-findings-in-agent-skills-asd-ste100-skill-md.md
workspace/task_board.md: missing Markdown file: 15-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-skill-m.md
workspace/task_board.md: missing Markdown file: 16-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-references.md
workspace/task_board.md: missing Markdown file: 17-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-skil.md
workspace/task_board.md: missing Markdown file: 18-ci-remediation-review-passive-voice-findings-in-agent-session-start-md.md
workspace/task_board.md: missing Markdown file: 19-ci-remediation-review-passive-voice-findings-in-agent-skills-asd-ste100-skill-m.md
workspace/task_board.md: missing Markdown file: 20-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md
workspace/task_board.md: missing Markdown file: 21-ci-remediation-review-semicolon-findings-in-workspace-readme-md.md
workspace/task_board.md: missing Markdown file: 22-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-refe.md
workspace/task_board.md: missing Markdown file: 23-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-skill-m.md
workspace/task_board.md: missing Markdown file: 24-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md
workspace/task_board.md: missing Markdown file: 26-ci-remediation-review-long-sentence-findings-in-agent-session-start-md.md
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

- **synonym-rotation** · .agent/skills/agent-skill-authoring/SKILL.md:223:46 · **new** · fingerprint: 78a70aacc34addace6e797ec
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

### Recurring findings

- **synonym-rotation** · workspace/task_board.md:81:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/task_board.md:81:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Resolved findings

- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:78:206 · **resolved** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:125:65 · **resolved** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/agent-skill-authoring/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 6
- **Words:** 2256
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/agent-skill-authoring/SKILL.md:223:46 · **new** · fingerprint: 78a70aacc34addace6e797ec
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1604
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:81:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **passive-voice** · workspace/task_board.md:81:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
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
