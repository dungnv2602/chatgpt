# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#979](https://github.com/dungnv2602/chatgpt/actions/runs/45984083069)
- **Run ID / attempt:** 45984083069 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 32c44fd8c2ed0b7f2b8a7540ae1bafd63842fb0a
- **Source task:** 20261126-142500-13
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 871743475e325dce4098df5256df8d91f99dfb66
- **Linter source SHA:** 32c44fd8c2ed0b7f2b8a7540ae1bafd63842fb0a
- **Generated (UTC):** 2026-11-27T10:42:08.140986+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 5 |
| Files that failed | 4 |
| Files with findings | 5 |
| Total findings | 23 |
| Hard findings | 16 |
| Advisory findings | 7 |
| New findings | 21 |
| Recurring findings | 2 |
| Resolved findings | 21 |
| Failed workflow checks | 2 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/github-actions/SKILL.md
- .agent/skills/the-worker/SKILL.md
- .agent/skills/the-worker/references/conversation-mode.md
- workspace/task_board.md
- .agent/skills/ci-ledger/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/github-actions/SKILL.md | FAIL | 2 | 2 | 0 | 1862 | 0.1 | 1 |
| .agent/skills/the-worker/SKILL.md | FAIL | 14 | 10 | 0 | 1771 | 0.8 | 1 |
| .agent/skills/the-worker/references/conversation-mode.md | PASS | 1 | 0 | 0 | 328 | 0.3 | 0 |
| workspace/task_board.md | FAIL | 2 | 2 | 0 | 546 | 0.4 | 1 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 4 | 2 | 0 | 707 | 0.6 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 9 |
| passive-voice | 7 |
| long-sentence | 4 |
| semicolon | 3 |

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
AssertionError: 'Source task: Unassigned' not found in '# On Repo STE Lint Evidence Report\n\n- **Result:** Passed\n- **Schema version:** 1.2.0\n- **Run:** [#902](https://example.invalid/run/902)\n- **Run ID / attempt:** 902 / 1\n- **Workflow:** Test lint report\n- **Branch / commit:** gpt / abc123\n- **Source task:** Unassigned\n- **Event:** schedule\n- **Execution mode:** repository-wide\n- **Baseline SHA:** Not applicable\n- **Linter source SHA:** Unknown\n- **Generated (UTC):** 2026-11-27T10:42:01.577961+00:00\n\n## 1. Executive summary\n\n| Measure | Result |\n|---|---:|\n| Files evaluated | 1 |\n| Files that failed | 0 |\n| Files with findings | 0 |\n| Total findings | 0 |\n| Hard findings | 0 |\n| Advisory findings | 0 |\n| New findings | 0 |\n| Recurring findings | 0 |\n| Resolved findings | 0 |\n| Failed workflow checks | 0 |\n\n## 2. Execution environment\n\n- Runner OS: Linux\n- Python: 3.15.2\n- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43\n- The JSON report records the full runtime version and every original per-file linter response.\n- The report records the commit that supplied the linter and generator code.\n\n## 3. Exact evaluation coverage\n\nThis list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.\n\n- docs/a.md\n\n## 4. Per-file result matrix\n\nThe table includes every evaluated file, including files with zero findings and files with execution errors.\n\n| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| docs/a.md | PASS | 0 | 0 | 0 | 0 | 0 | 0 |\n\n## 5. Findings by rule\n\nCounts include hard and advisory findings.\n\nNo findings.\n\n## 6. Workflow and validation checks\n\nEach check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.\n\nNo separate workflow checks were recorded.\n\n## 7. Baseline comparison\n\nFingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.\n\n### New findings\n\nNone.\n\n### Recurring findings\n\nNone.\n\n### Resolved findings\n\nNone.\n\n## 8. Complete per-file diagnostics\n\nThis section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.\n\n### docs/a.md\n\n- **Result:** PASS\n- **Exit code:** 0\n- **Findings:** 0\n- **Hard findings:** 0\n- **Baseline:** 0\n- **Words:** 0\n- **Findings per 100 words:** 0\n\nNo STE findings were recorded for this file.\n\n## 9. Structured evidence and integrity\n\n- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.\n- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.\n- **index.json:** Run locator and summary metadata, ordered newest first.\n- **history:** Immutable report files for each run ID and attempt.\n- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.\n\nA successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.\n'

======================================================================
FAIL: test_source_task_id_is_recorded_for_push_commit (__main__.ReportGeneratorTests.test_source_task_id_is_recorded_for_push_commit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_generate_lint_report.py", line 180, in test_source_task_id_is_recorded_for_push_commit
    self.assertIn("Source task: 20261127-090000", markdown)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'Source task: 20261127-090000' not found in '# On Repo STE Lint Evidence Report\n\n- **Result:** Passed\n- **Schema version:** 1.2.0\n- **Run:** [#901](https://example.invalid/run/901)\n- **Run ID / attempt:** 901 / 1\n- **Workflow:** Test lint report\n- **Branch / commit:** gpt / abc123\n- **Source task:** 20261127-090000\n- **Event:** push\n- **Execution mode:** repository-wide\n- **Baseline SHA:** Not applicable\n- **Linter source SHA:** Unknown\n- **Generated (UTC):** 2026-11-27T10:42:01.635699+00:00\n\n## 1. Executive summary\n\n| Measure | Result |\n|---|---:|\n| Files evaluated | 1 |\n| Files that failed | 0 |\n| Files with findings | 0 |\n| Total findings | 0 |\n| Hard findings | 0 |\n| Advisory findings | 0 |\n| New findings | 0 |\n| Recurring findings | 0 |\n| Resolved findings | 0 |\n| Failed workflow checks | 0 |\n\n## 2. Execution environment\n\n- Runner OS: Linux\n- Python: 3.15.2\n- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43\n- The JSON report records the full runtime version and every original per-file linter response.\n- The report records the commit that supplied the linter and generator code.\n\n## 3. Exact evaluation coverage\n\nThis list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.\n\n- docs/a.md\n\n## 4. Per-file result matrix\n\nThe table includes every evaluated file, including files with zero findings and files with execution errors.\n\n| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| docs/a.md | PASS | 0 | 0 | 0 | 0 | 0 | 0 |\n\n## 5. Findings by rule\n\nCounts include hard and advisory findings.\n\nNo findings.\n\n## 6. Workflow and validation checks\n\nEach check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.\n\nNo separate workflow checks were recorded.\n\n## 7. Baseline comparison\n\nFingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.\n\n### New findings\n\nNone.\n\n### Recurring findings\n\nNone.\n\n### Resolved findings\n\nNone.\n\n## 8. Complete per-file diagnostics\n\nThis section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.\n\n### docs/a.md\n\n- **Result:** PASS\n- **Exit code:** 0\n- **Findings:** 0\n- **Hard findings:** 0\n- **Baseline:** 0\n- **Words:** 0\n- **Findings per 100 words:** 0\n\nNo STE findings were recorded for this file.\n\n## 9. Structured evidence and integrity\n\n- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.\n- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.\n- **index.json:** Run locator and summary metadata, ordered newest first.\n- **history:** Immutable report files for each run ID and attempt.\n- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.\n\nA successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.\n'

----------------------------------------------------------------------
Ran 6 tests in 0.472s

FAILED (failures=2)
~~~~~~~~~~~~~~

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
Scanned 5 changed Markdown sources (385 available as link targets) and 23 local Markdown links.
Found 1 unresolved local Markdown targets or anchors.
workspace/task_board.md: missing Markdown file: tasks/20261126-142500/subtasks/20-ci-remediation-review-passive-voice-findings-in-workspace-task-board-md.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:40:96 · **new** · fingerprint: 00ff55742e1a76adf05e8f19
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **long-sentence** · .agent/skills/github-actions/SKILL.md:51:3 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:20:83 · **new** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:41:141 · **new** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/SKILL.md:47:10 · **new** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed
- **semicolon** · .agent/skills/the-worker/SKILL.md:52:41 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:53:29 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:54:16 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:91 · **new** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **long-sentence** · .agent/skills/the-worker/SKILL.md:92:3 · **new** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:96:70 · **new** · fingerprint: 030301d369a6833422178b29
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:96:330 · **new** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:104:139 · **new** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:104:169 · **new** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **long-sentence** · .agent/skills/the-worker/SKILL.md:105:182 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:105:201 · **new** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:30:156 · **new** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:41:132 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:41:209 · **new** · fingerprint: c9e22528ce04a72820e83cd1
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:43:154 · **new** · fingerprint: 1e48cae958865ea2aad69434
  - **Level:** advisory-free
  - **Message:** 'alter' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:54:137 · **new** · fingerprint: 59cc95b17372dc812b5f9dbd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned

### Recurring findings

- **synonym-rotation** · workspace/task_board.md:53:24 · **recurring** · fingerprint: 61290a3569b589a88314b958
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** Fix
- **synonym-rotation** · workspace/task_board.md:63:24 · **recurring** · fingerprint: 97c434f4a38d6986b5f287d8
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

### Resolved findings

- **semicolon** · workspace/task_board.md:5:113 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:7:13 · **resolved** · fingerprint: ec19da848a6fcda5c3642ea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is checked
- **passive-voice** · workspace/task_board.md:7:133 · **resolved** · fingerprint: 4e5e525ca51a4e0ca4df72f4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ranked
- **semicolon** · workspace/task_board.md:7:316 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:9:170 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:11:113 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:11:136 · **resolved** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed
- **semicolon** · workspace/task_board.md:21:63 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:53:176 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:63:122 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:64:136 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:25:182 · **resolved** · fingerprint: 174cb92f03c94b341eec0955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **semicolon** · workspace/TASK_TEMPLATE.md:25:259 · **resolved** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/TASK_TEMPLATE.md:78:135 · **resolved** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:78:153 · **resolved** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:28:92 · **resolved** · fingerprint: 77496caee1aa1b14090beb02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **long-sentence** · workspace/SUBTASK_TEMPLATE.md:28:107 · **resolved** · fingerprint: 75ec0bdcda44d39480fbac03
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:28:177 · **resolved** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:28:245 · **resolved** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/SUBTASK_TEMPLATE.md:58:5 · **resolved** · fingerprint: 0a2a773c8ed0a57b54ddb04b
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Checks
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:67:104 · **resolved** · fingerprint: ab76e7bf8f0141a1ea1aec79
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1862
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:40:96 · **new** · fingerprint: 00ff55742e1a76adf05e8f19
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **long-sentence** · .agent/skills/github-actions/SKILL.md:51:3 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 14
- **Hard findings:** 10
- **Baseline:** 0
- **Words:** 1771
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:20:83 · **new** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:41:141 · **new** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · .agent/skills/the-worker/SKILL.md:47:10 · **new** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed

- **semicolon** · .agent/skills/the-worker/SKILL.md:52:41 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:53:29 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:54:16 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:91 · **new** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **long-sentence** · .agent/skills/the-worker/SKILL.md:92:3 · **new** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · .agent/skills/the-worker/SKILL.md:96:70 · **new** · fingerprint: 030301d369a6833422178b29
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:96:330 · **new** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:104:139 · **new** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:104:169 · **new** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin

- **long-sentence** · .agent/skills/the-worker/SKILL.md:105:182 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:105:201 · **new** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated


### .agent/skills/the-worker/references/conversation-mode.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 328
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:30:156 · **new** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 546
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:53:24 · **recurring** · fingerprint: 61290a3569b589a88314b958
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** Fix

- **synonym-rotation** · workspace/task_board.md:63:24 · **recurring** · fingerprint: 97c434f4a38d6986b5f287d8
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** Correct


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 707
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:41:132 · **new** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:41:209 · **new** · fingerprint: c9e22528ce04a72820e83cd1
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:43:154 · **new** · fingerprint: 1e48cae958865ea2aad69434
  - **Level:** advisory-free
  - **Message:** 'alter' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** alter

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:54:137 · **new** · fingerprint: 59cc95b17372dc812b5f9dbd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
