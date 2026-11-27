# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#912](https://github.com/dungnv2602/chatgpt/actions/runs/45949249000)
- **Run ID / attempt:** 45949249000 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / fe3a0a1d9f506caad8fd8505171b31ec72e419d2
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 8ec1f0b81680f22f53a4180b9cb839b70fca163e
- **Linter source SHA:** fe3a0a1d9f506caad8fd8505171b31ec72e419d2
- **Generated (UTC):** 2026-11-27T06:03:19.927193+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 4 |
| Files that failed | 3 |
| Files with findings | 3 |
| Total findings | 9 |
| Hard findings | 6 |
| Advisory findings | 3 |
| New findings | 6 |
| Recurring findings | 3 |
| Resolved findings | 18 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md
- workspace/task_board.md
- workspace/draft/README.md
- workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md | FAIL | 3 | 2 | 0 | 1957 | 0.2 | 1 |
| workspace/task_board.md | FAIL | 3 | 2 | 0 | 1415 | 0.2 | 1 |
| workspace/draft/README.md | PASS | 0 | 0 | 0 | 728 | 0.0 | 0 |
| workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md | FAIL | 3 | 2 | 0 | 2081 | 0.1 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 6 |
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
....
----------------------------------------------------------------------
Ran 4 tests in 0.274s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.005s

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
Scanned 4 changed Markdown sources (557 available as link targets) and 91 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:90:59 · **new** · fingerprint: 3a5b8412eaf100e118f17c8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:158:19 · **new** · fingerprint: 88c525f2c2d9aadc1e2f7faf
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **synonym-rotation** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:171:143 · **new** · fingerprint: 13f39a799a7213976339c951
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix
- **passive-voice** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:99:59 · **new** · fingerprint: c39323ab6689958912bbc8ba
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:168:19 · **new** · fingerprint: 26a6732babf8a18c8f5ce179
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **synonym-rotation** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:182:143 · **new** · fingerprint: 2a02d81fb2a9bfbd6ffc2294
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix

### Recurring findings

- **passive-voice** · workspace/task_board.md:5:556 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · workspace/task_board.md:73:41 · **recurring** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/task_board.md:105:88 · **recurring** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate

### Resolved findings

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
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **resolved** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:27 · **resolved** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **resolved** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · workspace/TASK_TEMPLATE.md:25:159 · **resolved** · fingerprint: 5275280719ed16d2a5b7ad67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is written
- **passive-voice** · workspace/TASK_TEMPLATE.md:53:32 · **resolved** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:79:20 · **resolved** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:80:23 · **resolved** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **semicolon** · workspace/TASK_TEMPLATE.md:96:110 · **resolved** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:96:247 · **resolved** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1957
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:90:59 · **new** · fingerprint: 3a5b8412eaf100e118f17c8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:158:19 · **new** · fingerprint: 88c525f2c2d9aadc1e2f7faf
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter

- **synonym-rotation** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:171:143 · **new** · fingerprint: 13f39a799a7213976339c951
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1415
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:5:556 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · workspace/task_board.md:73:41 · **recurring** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · workspace/task_board.md:105:88 · **recurring** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate


### workspace/draft/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 728
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 2081
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:99:59 · **new** · fingerprint: c39323ab6689958912bbc8ba
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:168:19 · **new** · fingerprint: 26a6732babf8a18c8f5ce179
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter

- **synonym-rotation** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:182:143 · **new** · fingerprint: 2a02d81fb2a9bfbd6ffc2294
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
