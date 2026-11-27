# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#1005](https://github.com/dungnv2602/chatgpt/actions/runs/46004636376)
- **Run ID / attempt:** 46004636376 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 86ef132fb4948487f7f8aefe324ca1b74e19db0f
- **Source task:** 20261127-173000-13
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** f62d4cc6692f764cad57f1a291066c8af0966ca0
- **Linter source SHA:** 86ef132fb4948487f7f8aefe324ca1b74e19db0f
- **Generated (UTC):** 2026-11-27T13:09:44.971886+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 9 |
| Hard findings | 3 |
| Advisory findings | 6 |
| New findings | 7 |
| Recurring findings | 2 |
| Resolved findings | 17 |
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
| .agent/SESSION_START.md | FAIL | 7 | 2 | 0 | 2934 | 0.2 | 1 |
| workspace/task_board.md | FAIL | 2 | 1 | 0 | 1536 | 0.1 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 5 |
| synonym-rotation | 2 |
| long-sentence | 1 |
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
Ran 6 tests in 0.498s

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
Scanned 2 changed Markdown sources (440 available as link targets) and 43 local Markdown links.
Found 35 unresolved local Markdown targets or anchors.
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

- **passive-voice** · .agent/SESSION_START.md:22:209 · **new** · fingerprint: 00654de2a95772d4a870e55f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being fetched
- **passive-voice** · .agent/SESSION_START.md:92:158 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:93:60 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **synonym-rotation** · .agent/SESSION_START.md:177:7 · **new** · fingerprint: 93101ce1787c7b9208b4031d
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** retrieved
- **passive-voice** · .agent/SESSION_START.md:237:164 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · .agent/SESSION_START.md:253:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · .agent/SESSION_START.md:278:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

### Recurring findings

- **synonym-rotation** · workspace/task_board.md:79:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/task_board.md:79:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Resolved findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:36:83 · **resolved** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:61:141 · **resolved** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/SKILL.md:67:10 · **resolved** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:85:91 · **resolved** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **long-sentence** · .agent/skills/the-worker/SKILL.md:112:3 · **resolved** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:116:70 · **resolved** · fingerprint: 030301d369a6833422178b29
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:116:330 · **resolved** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:124:139 · **resolved** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:124:169 · **resolved** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **long-sentence** · .agent/skills/the-worker/SKILL.md:125:182 · **resolved** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:125:201 · **resolved** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **passive-voice** · .agent/skills/the-worker/SKILL.md:155:129 · **resolved** · fingerprint: 50c502e6476c7d33f9c052f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is activated
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:171:286 · **resolved** · fingerprint: f071e35d93664b24286e6bb7
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:172:302 · **resolved** · fingerprint: 5d8336dc915865ae43f6b3a8
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **passive-voice** · .agent/skills/the-worker/SKILL.md:174:100 · **resolved** · fingerprint: e5c16c0bb6df9d137ce2bf13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are exhausted
- **long-sentence** · .agent/skills/the-worker/SKILL.md:174:142 · **resolved** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:174:228 · **resolved** · fingerprint: 961e310a4d56d86392dd989d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were examined

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 2934
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/SESSION_START.md:22:209 · **new** · fingerprint: 00654de2a95772d4a870e55f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being fetched

- **passive-voice** · .agent/SESSION_START.md:92:158 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/SESSION_START.md:93:60 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **synonym-rotation** · .agent/SESSION_START.md:177:7 · **new** · fingerprint: 93101ce1787c7b9208b4031d
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** retrieved

- **passive-voice** · .agent/SESSION_START.md:237:164 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **present-perfect** · .agent/SESSION_START.md:253:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed

- **long-sentence** · .agent/SESSION_START.md:278:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1536
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:79:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **passive-voice** · workspace/task_board.md:79:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
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
