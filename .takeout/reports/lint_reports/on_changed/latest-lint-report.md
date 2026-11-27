# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#1012](https://github.com/dungnv2602/chatgpt/actions/runs/46007505787)
- **Run ID / attempt:** 46007505787 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 50b029374102b3a593c5e63dd38f54586158ac8e
- **Source task:** 20261127-173000-21
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** d2e5abb40b6df969d74a748df90a135c47b34f59
- **Linter source SHA:** 50b029374102b3a593c5e63dd38f54586158ac8e
- **Generated (UTC):** 2026-11-27T13:29:51.391862+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 1 |
| Files with findings | 2 |
| Total findings | 4 |
| Hard findings | 1 |
| Advisory findings | 3 |
| New findings | 2 |
| Recurring findings | 2 |
| Resolved findings | 12 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/task_board.md
- workspace/README.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/task_board.md | FAIL | 2 | 1 | 0 | 1264 | 0.2 | 1 |
| workspace/README.md | PASS | 2 | 0 | 0 | 510 | 0.4 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 3 |
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
......
----------------------------------------------------------------------
Ran 6 tests in 0.462s

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
Scanned 2 changed Markdown sources (439 available as link targets) and 49 local Markdown links.
Found 27 unresolved local Markdown targets or anchors.
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

- **passive-voice** · workspace/README.md:24:210 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/README.md:44:209 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

### Recurring findings

- **synonym-rotation** · workspace/task_board.md:71:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/task_board.md:71:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Resolved findings

- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:64:235 · **resolved** · fingerprint: aa0de8573960d54a21c2d1d2
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed
- **synonym-rotation** · .agent/skills/asd-ste100/SKILL.md:73:128 · **resolved** · fingerprint: 80139a54a075b106eac7c23c
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **nominalization** · .agent/skills/asd-ste100/SKILL.md:74:53 · **resolved** · fingerprint: 7e86fc5d602e4865ed4a0ff6
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:79:203 · **resolved** · fingerprint: 7a15da17f8212acf9cbcd80a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:81:140 · **resolved** · fingerprint: 320768d857c6a3e84654f3f5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed
- **nominalization** · .agent/skills/asd-ste100/SKILL.md:89:56 · **resolved** · fingerprint: fa833ca0d8a25be575faf6e0
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:79 · **resolved** · fingerprint: 12a9fb2640f958cc7e75f621
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:89 · **resolved** · fingerprint: c50be8a609eda6ecc738029b
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:107 · **resolved** · fingerprint: d7e2c69987f9328ac247ac53
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:121 · **resolved** · fingerprint: 0d5ed7f9257c40733f5c321d
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:133 · **resolved** · fingerprint: 2673e9a5ae5dd03778f880c9
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:113:134 · **resolved** · fingerprint: 361fe239198e1c7837a878ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1264
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:71:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **passive-voice** · workspace/task_board.md:71:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred


### workspace/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 510
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **passive-voice** · workspace/README.md:24:210 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/README.md:44:209 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
