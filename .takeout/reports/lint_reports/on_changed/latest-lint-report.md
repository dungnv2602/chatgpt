# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#967](https://github.com/dungnv2602/chatgpt/actions/runs/45979960470)
- **Run ID / attempt:** 45979960470 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / a41f781b95481f42bed9fd2c151241d7be40a372
- **Source task:** Unassigned
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 27824c83285f49522e578fa9ce4ea87403e931df
- **Linter source SHA:** a41f781b95481f42bed9fd2c151241d7be40a372
- **Generated (UTC):** 2026-11-27T10:12:36.665960+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 3 |
| Files with findings | 3 |
| Total findings | 19 |
| Hard findings | 12 |
| Advisory findings | 7 |
| New findings | 12 |
| Recurring findings | 7 |
| Resolved findings | 35 |
| Failed workflow checks | 2 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/task_board.md
- workspace/TASK_TEMPLATE.md
- workspace/SUBTASK_TEMPLATE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/task_board.md | FAIL | 10 | 7 | 0 | 503 | 2.0 | 1 |
| workspace/TASK_TEMPLATE.md | FAIL | 4 | 2 | 0 | 409 | 1.0 | 1 |
| workspace/SUBTASK_TEMPLATE.md | FAIL | 5 | 3 | 0 | 384 | 1.3 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| semicolon | 10 |
| passive-voice | 7 |
| long-sentence | 1 |
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
AssertionError: 'Source task: Unassigned' not found in '# On Repo STE Lint Evidence Report\n\n- **Result:** Passed\n- **Schema version:** 1.2.0\n- **Run:** [#902](https://example.invalid/run/902)\n- **Run ID / attempt:** 902 / 1\n- **Workflow:** Test lint report\n- **Branch / commit:** gpt / abc123\n- **Source task:** Unassigned\n- **Event:** schedule\n- **Execution mode:** repository-wide\n- **Baseline SHA:** Not applicable\n- **Linter source SHA:** Unknown\n- **Generated (UTC):** 2026-11-27T10:12:32.491765+00:00\n\n## 1. Executive summary\n\n| Measure | Result |\n|---|---:|\n| Files evaluated | 1 |\n| Files that failed | 0 |\n| Files with findings | 0 |\n| Total findings | 0 |\n| Hard findings | 0 |\n| Advisory findings | 0 |\n| New findings | 0 |\n| Recurring findings | 0 |\n| Resolved findings | 0 |\n| Failed workflow checks | 0 |\n\n## 2. Execution environment\n\n- Runner OS: Linux\n- Python: 3.15.2\n- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43\n- The JSON report records the full runtime version and every original per-file linter response.\n- The report records the commit that supplied the linter and generator code.\n\n## 3. Exact evaluation coverage\n\nThis list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.\n\n- docs/a.md\n\n## 4. Per-file result matrix\n\nThe table includes every evaluated file, including files with zero findings and files with execution errors.\n\n| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| docs/a.md | PASS | 0 | 0 | 0 | 0 | 0 | 0 |\n\n## 5. Findings by rule\n\nCounts include hard and advisory findings.\n\nNo findings.\n\n## 6. Workflow and validation checks\n\nEach check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.\n\nNo separate workflow checks were recorded.\n\n## 7. Baseline comparison\n\nFingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.\n\n### New findings\n\nNone.\n\n### Recurring findings\n\nNone.\n\n### Resolved findings\n\nNone.\n\n## 8. Complete per-file diagnostics\n\nThis section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.\n\n### docs/a.md\n\n- **Result:** PASS\n- **Exit code:** 0\n- **Findings:** 0\n- **Hard findings:** 0\n- **Baseline:** 0\n- **Words:** 0\n- **Findings per 100 words:** 0\n\nNo STE findings were recorded for this file.\n\n## 9. Structured evidence and integrity\n\n- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.\n- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.\n- **index.json:** Run locator and summary metadata, ordered newest first.\n- **history:** Immutable report files for each run ID and attempt.\n- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.\n\nA successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.\n'

======================================================================
FAIL: test_source_task_id_is_recorded_for_push_commit (__main__.ReportGeneratorTests.test_source_task_id_is_recorded_for_push_commit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_generate_lint_report.py", line 180, in test_source_task_id_is_recorded_for_push_commit
    self.assertIn("Source task: 20261127-090000", markdown)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'Source task: 20261127-090000' not found in '# On Repo STE Lint Evidence Report\n\n- **Result:** Passed\n- **Schema version:** 1.2.0\n- **Run:** [#901](https://example.invalid/run/901)\n- **Run ID / attempt:** 901 / 1\n- **Workflow:** Test lint report\n- **Branch / commit:** gpt / abc123\n- **Source task:** 20261127-090000\n- **Event:** push\n- **Execution mode:** repository-wide\n- **Baseline SHA:** Not applicable\n- **Linter source SHA:** Unknown\n- **Generated (UTC):** 2026-11-27T10:12:32.529783+00:00\n\n## 1. Executive summary\n\n| Measure | Result |\n|---|---:|\n| Files evaluated | 1 |\n| Files that failed | 0 |\n| Files with findings | 0 |\n| Total findings | 0 |\n| Hard findings | 0 |\n| Advisory findings | 0 |\n| New findings | 0 |\n| Recurring findings | 0 |\n| Resolved findings | 0 |\n| Failed workflow checks | 0 |\n\n## 2. Execution environment\n\n- Runner OS: Linux\n- Python: 3.15.2\n- Platform: Linux-7.0.0-1016-aws-x86_64-with-glibc2.43\n- The JSON report records the full runtime version and every original per-file linter response.\n- The report records the commit that supplied the linter and generator code.\n\n## 3. Exact evaluation coverage\n\nThis list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.\n\n- docs/a.md\n\n## 4. Per-file result matrix\n\nThe table includes every evaluated file, including files with zero findings and files with execution errors.\n\n| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| docs/a.md | PASS | 0 | 0 | 0 | 0 | 0 | 0 |\n\n## 5. Findings by rule\n\nCounts include hard and advisory findings.\n\nNo findings.\n\n## 6. Workflow and validation checks\n\nEach check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.\n\nNo separate workflow checks were recorded.\n\n## 7. Baseline comparison\n\nFingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.\n\n### New findings\n\nNone.\n\n### Recurring findings\n\nNone.\n\n### Resolved findings\n\nNone.\n\n## 8. Complete per-file diagnostics\n\nThis section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.\n\n### docs/a.md\n\n- **Result:** PASS\n- **Exit code:** 0\n- **Findings:** 0\n- **Hard findings:** 0\n- **Baseline:** 0\n- **Words:** 0\n- **Findings per 100 words:** 0\n\nNo STE findings were recorded for this file.\n\n## 9. Structured evidence and integrity\n\n- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.\n- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.\n- **index.json:** Run locator and summary metadata, ordered newest first.\n- **history:** Immutable report files for each run ID and attempt.\n- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.\n\nA successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.\n'

----------------------------------------------------------------------
Ran 6 tests in 0.304s

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

- **Result:** Failed
- **Exit code:** 1

~~~text
Scanned 3 changed Markdown sources (370 available as link targets) and 21 local Markdown links.
Found 1 unresolved local Markdown targets or anchors.
workspace/task_board.md: missing Markdown file: tasks/20261126-142500/subtasks/20-ci-remediation-review-passive-voice-findings-in-workspace-task-board-md.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · workspace/task_board.md:7:13 · **new** · fingerprint: ec19da848a6fcda5c3642ea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is checked
- **passive-voice** · workspace/task_board.md:7:133 · **new** · fingerprint: 4e5e525ca51a4e0ca4df72f4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ranked
- **synonym-rotation** · workspace/task_board.md:53:24 · **new** · fingerprint: 61290a3569b589a88314b958
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** Fix
- **passive-voice** · workspace/TASK_TEMPLATE.md:23:182 · **new** · fingerprint: 174cb92f03c94b341eec0955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **semicolon** · workspace/TASK_TEMPLATE.md:23:259 · **new** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/TASK_TEMPLATE.md:76:135 · **new** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:76:153 · **new** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:26:92 · **new** · fingerprint: 77496caee1aa1b14090beb02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **long-sentence** · workspace/SUBTASK_TEMPLATE.md:26:107 · **new** · fingerprint: 75ec0bdcda44d39480fbac03
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:26:177 · **new** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:26:245 · **new** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:65:104 · **new** · fingerprint: ab76e7bf8f0141a1ea1aec79
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

### Recurring findings

- **semicolon** · workspace/task_board.md:5:113 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:7:316 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:9:170 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:11:113 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:11:136 · **recurring** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed
- **semicolon** · workspace/task_board.md:21:63 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:53:176 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Resolved findings

- **semicolon** · .agent/skills/github-actions/SKILL.md:17:66 · **resolved** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:40:96 · **resolved** · fingerprint: 00ff55742e1a76adf05e8f19
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **long-sentence** · .agent/skills/github-actions/SKILL.md:51:3 · **resolved** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:19:3 · **resolved** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
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
- **semicolon** · .agent/skills/the-worker/SKILL.md:49:169 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
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
- **semicolon** · .agent/skills/the-worker/SKILL.md:65:146 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:67:77 · **resolved** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · .agent/skills/the-worker/SKILL.md:69:53 · **resolved** · fingerprint: b336f74954a3548f82ab7c54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were executed
- **semicolon** · .agent/skills/the-worker/SKILL.md:69:175 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:14:106 · **resolved** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:20:214 · **resolved** · fingerprint: 6ae9a6a4a2db5981a11a3382
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been collected
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:20:219 · **resolved** · fingerprint: bdeb60b7ecf5b8b23d08fe8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been collected
- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:26:339 · **resolved** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:26:365 · **resolved** · fingerprint: 20ab01d0763dc8b1779dc36e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:26:378 · **resolved** · fingerprint: bd4591524e78ee2f7fa8b868
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:30:156 · **resolved** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · workspace/task_board.md:9:211 · **resolved** · fingerprint: 2576c78693220ab79f5566ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · workspace/task_board.md:21:31 · **resolved** · fingerprint: bd8b55f1d04f97c603ef1aff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconciled
- **passive-voice** · workspace/task_board.md:21:224 · **resolved** · fingerprint: 4119e24c85ce36f95f82426b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is queued
- **present-perfect** · workspace/task_board.md:31:27 · **resolved** · fingerprint: 9612c1c87b475ef28776a775
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been remediated
- **passive-voice** · workspace/task_board.md:31:32 · **resolved** · fingerprint: ad9a72b9a291435f0a3c005b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been remediated
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:32:56 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:41:132 · **resolved** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:41:209 · **resolved** · fingerprint: c9e22528ce04a72820e83cd1
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:51:58 · **resolved** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:54:146 · **resolved** · fingerprint: 59cc95b17372dc812b5f9dbd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:66:72 · **resolved** · fingerprint: 1f954c173b07804351eff72a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:66:75 · **resolved** · fingerprint: 7966f136f54c681540016f83
  - **Level:** advisory-free
  - **Message:** 'delete' and 'erase' name the same action. Pick one and use it every time.
  - **Matched text:** deleted

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 10
- **Hard findings:** 7
- **Baseline:** 0
- **Words:** 503
- **Findings per 100 words:** 2.0

#### Complete diagnostics

- **semicolon** · workspace/task_board.md:5:113 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:7:13 · **new** · fingerprint: ec19da848a6fcda5c3642ea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is checked

- **passive-voice** · workspace/task_board.md:7:133 · **new** · fingerprint: 4e5e525ca51a4e0ca4df72f4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ranked

- **semicolon** · workspace/task_board.md:7:316 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/task_board.md:9:170 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/task_board.md:11:113 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:11:136 · **recurring** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed

- **semicolon** · workspace/task_board.md:21:63 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/task_board.md:53:24 · **new** · fingerprint: 61290a3569b589a88314b958
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** Fix

- **semicolon** · workspace/task_board.md:53:176 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/TASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 409
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **passive-voice** · workspace/TASK_TEMPLATE.md:23:182 · **new** · fingerprint: 174cb92f03c94b341eec0955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **semicolon** · workspace/TASK_TEMPLATE.md:23:259 · **new** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/TASK_TEMPLATE.md:76:135 · **new** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/TASK_TEMPLATE.md:76:153 · **new** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted


### workspace/SUBTASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 5
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 384
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:26:92 · **new** · fingerprint: 77496caee1aa1b14090beb02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **long-sentence** · workspace/SUBTASK_TEMPLATE.md:26:107 · **new** · fingerprint: 75ec0bdcda44d39480fbac03
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/SUBTASK_TEMPLATE.md:26:177 · **new** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/SUBTASK_TEMPLATE.md:26:245 · **new** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:65:104 · **new** · fingerprint: ab76e7bf8f0141a1ea1aec79
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
