# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#982](https://github.com/dungnv2602/chatgpt/actions/runs/45985475477)
- **Run ID / attempt:** 45985475477 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 4435c51224e8cb471f990275bd35ae7b32a5193e
- **Source task:** 20261127-173100-01
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 6292ba81a7e0757b61fbe44ccf05761bf553ac1d
- **Linter source SHA:** 4435c51224e8cb471f990275bd35ae7b32a5193e
- **Generated (UTC):** 2026-11-27T10:51:53.684320+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 3 |
| Files with findings | 3 |
| Total findings | 18 |
| Hard findings | 8 |
| Advisory findings | 10 |
| New findings | 16 |
| Recurring findings | 2 |
| Resolved findings | 19 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/TASK_BOARD_TEMPLATE.md
- workspace/task_board.md
- workspace/README.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/TASK_BOARD_TEMPLATE.md | FAIL | 5 | 3 | 0 | 330 | 1.5 | 1 |
| workspace/task_board.md | FAIL | 7 | 1 | 0 | 384 | 1.8 | 1 |
| workspace/README.md | FAIL | 6 | 4 | 0 | 500 | 1.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 10 |
| semicolon | 7 |
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

- **Result:** Failed
- **Exit code:** 1

~~~~~~~~~~~~~~text
....FF
======================================================================
FAIL: test_scheduled_report_does_not_claim_a_task (__main__.ReportGeneratorTests.test_scheduled_report_does_not_claim_a_task)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_generate_lint_report.py", line 193, in test_scheduled_report_does_not_claim_a_task
    self.assertIn("Source task: Unassigned", markdown)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'Source task: Unassigned' not found in '# On Repo STE Lint Evidence Report\n\n- **Result:** Passed\n- **Schema version:** 1.2.0\n- **Run:** [#902](https://example.invalid/run/902)\n- **Run ID / attempt:** 902 / 1\n- **Workflow:** Test lint report\n- **Branch / commit:** gpt / abc123\n- **Source task:** Unassigned\n- **Event:** schedule\n- **Execution mode:** repository-wide\n- **Baseline SHA:** Not applicable\n- **Linter source SHA:** Unknown\n- **Generated (UTC):** 2026-11-27T10:51:50.154128+00:00\n\n## 1. Executive summary\n\n| Measure | Result |\n|---|---:|\n| Files evaluated | 1 |\n| Files that failed | 0 |\n| Files with findings | 0 |\n| Total findings | 0 |\n| Hard findings | 0 |\n| Advisory findings | 0 |\n| New findings | 0 |\n| Recurring findings | 0 |\n| Resolved findings | 0 |\n| Failed workflow checks | 0 |\n\n## 2. Execution environment\n\n- Runner OS: Linux\n- Python: 3.15.2\n- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43\n- The JSON report records the full runtime version and every original per-file linter response.\n- The report records the commit that supplied the linter and generator code.\n\n## 3. Exact evaluation coverage\n\nThis list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.\n\n- docs/a.md\n\n## 4. Per-file result matrix\n\nThe table includes every evaluated file, including files with zero findings and files with execution errors.\n\n| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| docs/a.md | PASS | 0 | 0 | 0 | 0 | 0 | 0 |\n\n## 5. Findings by rule\n\nCounts include hard and advisory findings.\n\nNo findings.\n\n## 6. Workflow and validation checks\n\nEach check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.\n\nNo separate workflow checks were recorded.\n\n## 7. Baseline comparison\n\nFingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.\n\n### New findings\n\nNone.\n\n### Recurring findings\n\nNone.\n\n### Resolved findings\n\nNone.\n\n## 8. Complete per-file diagnostics\n\nThis section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.\n\n### docs/a.md\n\n- **Result:** PASS\n- **Exit code:** 0\n- **Findings:** 0\n- **Hard findings:** 0\n- **Baseline:** 0\n- **Words:** 0\n- **Findings per 100 words:** 0\n\nNo STE findings were recorded for this file.\n\n## 9. Structured evidence and integrity\n\n- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.\n- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.\n- **index.json:** Run locator and summary metadata, ordered newest first.\n- **history:** Immutable report files for each run ID and attempt.\n- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.\n\nA successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.\n'

======================================================================
FAIL: test_source_task_id_is_recorded_for_push_commit (__main__.ReportGeneratorTests.test_source_task_id_is_recorded_for_push_commit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_generate_lint_report.py", line 180, in test_source_task_id_is_recorded_for_push_commit
    self.assertIn("Source task: 20261127-090000", markdown)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'Source task: 20261127-090000' not found in '# On Repo STE Lint Evidence Report\n\n- **Result:** Passed\n- **Schema version:** 1.2.0\n- **Run:** [#901](https://example.invalid/run/901)\n- **Run ID / attempt:** 901 / 1\n- **Workflow:** Test lint report\n- **Branch / commit:** gpt / abc123\n- **Source task:** 20261127-090000\n- **Event:** push\n- **Execution mode:** repository-wide\n- **Baseline SHA:** Not applicable\n- **Linter source SHA:** Unknown\n- **Generated (UTC):** 2026-11-27T10:51:50.194574+00:00\n\n## 1. Executive summary\n\n| Measure | Result |\n|---|---:|\n| Files evaluated | 1 |\n| Files that failed | 0 |\n| Files with findings | 0 |\n| Total findings | 0 |\n| Hard findings | 0 |\n| Advisory findings | 0 |\n| New findings | 0 |\n| Recurring findings | 0 |\n| Resolved findings | 0 |\n| Failed workflow checks | 0 |\n\n## 2. Execution environment\n\n- Runner OS: Linux\n- Python: 3.15.2\n- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43\n- The JSON report records the full runtime version and every original per-file linter response.\n- The report records the commit that supplied the linter and generator code.\n\n## 3. Exact evaluation coverage\n\nThis list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.\n\n- docs/a.md\n\n## 4. Per-file result matrix\n\nThe table includes every evaluated file, including files with zero findings and files with execution errors.\n\n| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| docs/a.md | PASS | 0 | 0 | 0 | 0 | 0 | 0 |\n\n## 5. Findings by rule\n\nCounts include hard and advisory findings.\n\nNo findings.\n\n## 6. Workflow and validation checks\n\nEach check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.\n\nNo separate workflow checks were recorded.\n\n## 7. Baseline comparison\n\nFingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.\n\n### New findings\n\nNone.\n\n### Recurring findings\n\nNone.\n\n### Resolved findings\n\nNone.\n\n## 8. Complete per-file diagnostics\n\nThis section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.\n\n### docs/a.md\n\n- **Result:** PASS\n- **Exit code:** 0\n- **Findings:** 0\n- **Hard findings:** 0\n- **Baseline:** 0\n- **Words:** 0\n- **Findings per 100 words:** 0\n\nNo STE findings were recorded for this file.\n\n## 9. Structured evidence and integrity\n\n- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.\n- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.\n- **index.json:** Run locator and summary metadata, ordered newest first.\n- **history:** Immutable report files for each run ID and attempt.\n- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.\n\nA successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.\n'

----------------------------------------------------------------------
Ran 6 tests in 0.328s

FAILED (failures=2)
~~~~~~~~~~~~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

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
Scanned 3 changed Markdown sources (389 available as link targets) and 18 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **semicolon** · workspace/TASK_BOARD_TEMPLATE.md:11:87 · **new** · fingerprint: 736a387285f333116605ea7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_BOARD_TEMPLATE.md:25:27 · **new** · fingerprint: 0a59d1cc2fd02789df09d955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is occupied
- **passive-voice** · workspace/TASK_BOARD_TEMPLATE.md:25:52 · **new** · fingerprint: 19dabf656ecfd6a9fbda6859
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **semicolon** · workspace/TASK_BOARD_TEMPLATE.md:25:63 · **new** · fingerprint: 736a387285f333116605ea7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/TASK_BOARD_TEMPLATE.md:51:159 · **new** · fingerprint: 736a387285f333116605ea7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:17:31 · **new** · fingerprint: 164db7fee07f2dc419fbc88a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · workspace/task_board.md:33:138 · **new** · fingerprint: b1a46d8a22d1e761ec9da309
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read
- **passive-voice** · workspace/task_board.md:33:227 · **new** · fingerprint: 5394c1cd56ff6a013f7fbb3d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **passive-voice** · workspace/task_board.md:34:132 · **new** · fingerprint: b1a46d8a22d1e761ec9da309
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read
- **passive-voice** · workspace/task_board.md:34:243 · **new** · fingerprint: 5394c1cd56ff6a013f7fbb3d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **semicolon** · workspace/README.md:14:41 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:23:210 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · workspace/README.md:24:104 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/README.md:33:224 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:43:209 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · workspace/README.md:43:220 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Recurring findings

- **synonym-rotation** · workspace/task_board.md:44:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/task_board.md:44:147 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Resolved findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:20:83 · **resolved** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:41:141 · **resolved** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/SKILL.md:47:10 · **resolved** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed
- **semicolon** · .agent/skills/the-worker/SKILL.md:52:41 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:53:29 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:54:16 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:91 · **resolved** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **long-sentence** · .agent/skills/the-worker/SKILL.md:92:3 · **resolved** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:96:70 · **resolved** · fingerprint: 030301d369a6833422178b29
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:96:330 · **resolved** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:104:139 · **resolved** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:104:169 · **resolved** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **long-sentence** · .agent/skills/the-worker/SKILL.md:105:182 · **resolved** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:105:201 · **resolved** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:129:286 · **resolved** · fingerprint: f071e35d93664b24286e6bb7
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:130:302 · **resolved** · fingerprint: 5d8336dc915865ae43f6b3a8
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **passive-voice** · .agent/skills/the-worker/SKILL.md:132:100 · **resolved** · fingerprint: e5c16c0bb6df9d137ce2bf13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are exhausted
- **long-sentence** · .agent/skills/the-worker/SKILL.md:132:142 · **resolved** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:132:228 · **resolved** · fingerprint: 961e310a4d56d86392dd989d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were examined

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/TASK_BOARD_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 5
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 330
- **Findings per 100 words:** 1.5

#### Complete diagnostics

- **semicolon** · workspace/TASK_BOARD_TEMPLATE.md:11:87 · **new** · fingerprint: 736a387285f333116605ea7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/TASK_BOARD_TEMPLATE.md:25:27 · **new** · fingerprint: 0a59d1cc2fd02789df09d955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is occupied

- **passive-voice** · workspace/TASK_BOARD_TEMPLATE.md:25:52 · **new** · fingerprint: 19dabf656ecfd6a9fbda6859
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

- **semicolon** · workspace/TASK_BOARD_TEMPLATE.md:25:63 · **new** · fingerprint: 736a387285f333116605ea7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/TASK_BOARD_TEMPLATE.md:51:159 · **new** · fingerprint: 736a387285f333116605ea7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 384
- **Findings per 100 words:** 1.8

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:17:31 · **new** · fingerprint: 164db7fee07f2dc419fbc88a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · workspace/task_board.md:33:138 · **new** · fingerprint: b1a46d8a22d1e761ec9da309
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read

- **passive-voice** · workspace/task_board.md:33:227 · **new** · fingerprint: 5394c1cd56ff6a013f7fbb3d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded

- **passive-voice** · workspace/task_board.md:34:132 · **new** · fingerprint: b1a46d8a22d1e761ec9da309
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read

- **passive-voice** · workspace/task_board.md:34:243 · **new** · fingerprint: 5394c1cd56ff6a013f7fbb3d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded

- **synonym-rotation** · workspace/task_board.md:44:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **passive-voice** · workspace/task_board.md:44:147 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 500
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **semicolon** · workspace/README.md:14:41 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/README.md:23:210 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **semicolon** · workspace/README.md:24:104 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/README.md:33:224 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/README.md:43:209 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **semicolon** · workspace/README.md:43:220 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
