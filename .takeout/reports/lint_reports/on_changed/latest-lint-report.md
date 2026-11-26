# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#807](https://github.com/dungnv2602/chatgpt/actions/runs/45831761330)
- **Run ID / attempt:** 45831761330 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 1990c8ac733f7ae9a9947f97772822fb7e00edde
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 1833d0712252f101348eef49828f0ae6cf260e71
- **Linter source SHA:** 1990c8ac733f7ae9a9947f97772822fb7e00edde
- **Generated (UTC):** 2026-11-26T13:43:09.592586+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 10 |
| Hard findings | 7 |
| Advisory findings | 3 |
| New findings | 3 |
| Recurring findings | 7 |
| Resolved findings | 12 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/document-standards/references/document-type-catalog.md | FAIL | 7 | 4 | 0 | 4629 | 0.2 | 1 |
| workspace/task_board.md | FAIL | 3 | 3 | 0 | 291 | 1.0 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 3 |
| semicolon | 3 |
| synonym-rotation | 3 |
| long-sentence | 1 |

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
Ran 4 tests in 0.390s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.006s

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

- **synonym-rotation** · workspace/task_board.md:21:38 · **new** · fingerprint: f8874d55207a198913c99e59
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/task_board.md:23:24 · **new** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **synonym-rotation** · workspace/task_board.md:34:21 · **new** · fingerprint: 7cb82e69e7844d17f868b2a2
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Repair

### Recurring findings

- **long-sentence** · .agent/skills/document-standards/references/document-type-catalog.md:45:121 · **recurring** · fingerprint: 2dd7b3784611553473e6528c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:45:212 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:45:458 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:191 · **recurring** · fingerprint: 3ae524e22114a03c0ab4422a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:228 · **recurring** · fingerprint: 2115664c682d98befee7c6f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is tracked
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:126:145 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:143 · **recurring** · fingerprint: 3d0eb996eb2ac7266bac89b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are restored

### Resolved findings

- **semicolon** · workspace/adr/README.md:69:154 · **resolved** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/README.md:70:170 · **resolved** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/decision-governance/SKILL.md:84:206 · **resolved** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:103:283 · **resolved** · fingerprint: 7c881c753a4078cb6de1c860
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:107:38 · **resolved** · fingerprint: 7e15f02585cf13c74c4d9066
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:109:34 · **resolved** · fingerprint: ed925553639766f753b1e47c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:47 · **resolved** · fingerprint: c6fdcf445b99331b3955a823
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated
- **semicolon** · .agent/skills/decision-governance/SKILL.md:115:57 · **resolved** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:102 · **resolved** · fingerprint: c5cbda1d2fcdc95906e3b0f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:117:86 · **resolved** · fingerprint: 9248adb057e0be913c820595
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed
- **semicolon** · .agent/skills/decision-governance/SKILL.md:131:65 · **resolved** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:148:192 · **resolved** · fingerprint: e1fbc1afe62a844787cdbdb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 4629
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **long-sentence** · .agent/skills/document-standards/references/document-type-catalog.md:45:121 · **recurring** · fingerprint: 2dd7b3784611553473e6528c
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:45:212 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:45:458 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:191 · **recurring** · fingerprint: 3ae524e22114a03c0ab4422a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:56:228 · **recurring** · fingerprint: 2115664c682d98befee7c6f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is tracked

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:126:145 · **recurring** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:143 · **recurring** · fingerprint: 3d0eb996eb2ac7266bac89b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are restored


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 291
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:21:38 · **new** · fingerprint: f8874d55207a198913c99e59
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · workspace/task_board.md:23:24 · **new** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **synonym-rotation** · workspace/task_board.md:34:21 · **new** · fingerprint: 7cb82e69e7844d17f868b2a2
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Repair

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
