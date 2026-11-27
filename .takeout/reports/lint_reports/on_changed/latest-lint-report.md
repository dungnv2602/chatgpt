# On Changed STE Lint Evidence Report

- **Result:** Passed
- **Schema version:** 1.2.0
- **Run:** [#994](https://github.com/dungnv2602/chatgpt/actions/runs/45994577533)
- **Run ID / attempt:** 45994577533 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / b7de07d9138d3095e8b590f19a1a22da24595361
- **Source task:** 20261127-173000-05
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 8a00ccfe91f0acfea20bb03a0a01d7203ac3836a
- **Linter source SHA:** b7de07d9138d3095e8b590f19a1a22da24595361
- **Generated (UTC):** 2026-11-27T11:57:21.713601+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 0 |
| Files with findings | 3 |
| Total findings | 10 |
| Hard findings | 1 |
| Advisory findings | 9 |
| New findings | 10 |
| Recurring findings | 0 |
| Resolved findings | 4 |
| Failed workflow checks | 0 |

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
- .agent/skills/asd-ste100/references/repository-writing-policy.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/agent-skill-authoring/SKILL.md | PASS | 8 | 1 | 6 | 2257 | 0.4 | 0 |
| workspace/task_board.md | PASS | 1 | 0 | 0 | 1019 | 0.1 | 0 |
| .agent/skills/asd-ste100/references/repository-writing-policy.md | PASS | 1 | 0 | 0 | 571 | 0.2 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 9 |
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
Ran 6 tests in 0.454s

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
Scanned 3 changed Markdown sources (434 available as link targets) and 50 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:14:79 · **new** · fingerprint: 02b57d3b2df16eb3468595dc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:159:29 · **new** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:166:23 · **new** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:185:36 · **new** · fingerprint: 97f02ce3bcf5b6ef7653d521
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:223:38 · **new** · fingerprint: 6791e38cdf43e2f4c45df46b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:245:28 · **new** · fingerprint: eb4ac5866a5a9ae0a950a472
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:253:17 · **new** · fingerprint: bbeb4b1299f984862be3ce2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected
- **synonym-rotation** · .agent/skills/agent-skill-authoring/SKILL.md:257:21 · **new** · fingerprint: 78a70aacc34addace6e797ec
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · workspace/task_board.md:83:113 · **new** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **passive-voice** · .agent/skills/asd-ste100/references/repository-writing-policy.md:18:36 · **new** · fingerprint: fa71e22a78d6e4ce44e3a977
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

### Recurring findings

None.

### Resolved findings

- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:35:132 · **resolved** · fingerprint: 20a3b946ee1ae4877e53e449
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:35:209 · **resolved** · fingerprint: a913a887a540db8f083a49d4
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes
- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:37:154 · **resolved** · fingerprint: b57ced8a931e2c7579ee7ae3
  - **Level:** advisory-free
  - **Message:** 'alter' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:48:137 · **resolved** · fingerprint: 02e6a360a86d394444d7be9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/agent-skill-authoring/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 8
- **Hard findings:** 1
- **Baseline:** 6
- **Words:** 2257
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:14:79 · **new** · fingerprint: 02b57d3b2df16eb3468595dc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:159:29 · **new** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:166:23 · **new** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:185:36 · **new** · fingerprint: 97f02ce3bcf5b6ef7653d521
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:223:38 · **new** · fingerprint: 6791e38cdf43e2f4c45df46b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:245:28 · **new** · fingerprint: eb4ac5866a5a9ae0a950a472
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:253:17 · **new** · fingerprint: bbeb4b1299f984862be3ce2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected

- **synonym-rotation** · .agent/skills/agent-skill-authoring/SKILL.md:257:21 · **new** · fingerprint: 78a70aacc34addace6e797ec
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1019
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:83:113 · **new** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred


### .agent/skills/asd-ste100/references/repository-writing-policy.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 571
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/asd-ste100/references/repository-writing-policy.md:18:36 · **new** · fingerprint: fa71e22a78d6e4ce44e3a977
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
