# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#972](https://github.com/dungnv2602/chatgpt/actions/runs/45980978400)
- **Run ID / attempt:** 45980978400 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / b2386ff65ca10c16560301210ab5853c989401df
- **Source task:** 20261126-142500-22
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** a41f781b95481f42bed9fd2c151241d7be40a372
- **Linter source SHA:** b2386ff65ca10c16560301210ab5853c989401df
- **Generated (UTC):** 2026-11-27T10:19:49.199080+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 5 |
| Files that failed | 3 |
| Files with findings | 3 |
| Total findings | 40 |
| Hard findings | 28 |
| Advisory findings | 12 |
| New findings | 29 |
| Recurring findings | 11 |
| Resolved findings | 9 |
| Failed workflow checks | 2 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/README.md
- .agent/SESSION_START.md
- .agent/skills/the-worker/SKILL.md
- workspace/task_board.md
- .agent/skills/document-standards/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/README.md | PASS | 0 | 0 | 0 | 439 | 0.0 | 0 |
| .agent/SESSION_START.md | FAIL | 7 | 3 | 0 | 2931 | 0.2 | 1 |
| .agent/skills/the-worker/SKILL.md | FAIL | 22 | 17 | 0 | 1504 | 1.5 | 1 |
| workspace/task_board.md | FAIL | 11 | 8 | 0 | 533 | 2.1 | 1 |
| .agent/skills/document-standards/SKILL.md | PASS | 0 | 0 | 0 | 60 | 0.0 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| semicolon | 18 |
| passive-voice | 11 |
| synonym-rotation | 7 |
| long-sentence | 3 |
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
AssertionError: 'Source task: Unassigned' not found in '# On Repo STE Lint Evidence Report\n\n- **Result:** Passed\n- **Schema version:** 1.2.0\n- **Run:** [#902](https://example.invalid/run/902)\n- **Run ID / attempt:** 902 / 1\n- **Workflow:** Test lint report\n- **Branch / commit:** gpt / abc123\n- **Source task:** Unassigned\n- **Event:** schedule\n- **Execution mode:** repository-wide\n- **Baseline SHA:** Not applicable\n- **Linter source SHA:** Unknown\n- **Generated (UTC):** 2026-11-27T10:19:42.765520+00:00\n\n## 1. Executive summary\n\n| Measure | Result |\n|---|---:|\n| Files evaluated | 1 |\n| Files that failed | 0 |\n| Files with findings | 0 |\n| Total findings | 0 |\n| Hard findings | 0 |\n| Advisory findings | 0 |\n| New findings | 0 |\n| Recurring findings | 0 |\n| Resolved findings | 0 |\n| Failed workflow checks | 0 |\n\n## 2. Execution environment\n\n- Runner OS: Linux\n- Python: 3.15.2\n- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43\n- The JSON report records the full runtime version and every original per-file linter response.\n- The report records the commit that supplied the linter and generator code.\n\n## 3. Exact evaluation coverage\n\nThis list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.\n\n- docs/a.md\n\n## 4. Per-file result matrix\n\nThe table includes every evaluated file, including files with zero findings and files with execution errors.\n\n| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| docs/a.md | PASS | 0 | 0 | 0 | 0 | 0 | 0 |\n\n## 5. Findings by rule\n\nCounts include hard and advisory findings.\n\nNo findings.\n\n## 6. Workflow and validation checks\n\nEach check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.\n\nNo separate workflow checks were recorded.\n\n## 7. Baseline comparison\n\nFingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.\n\n### New findings\n\nNone.\n\n### Recurring findings\n\nNone.\n\n### Resolved findings\n\nNone.\n\n## 8. Complete per-file diagnostics\n\nThis section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.\n\n### docs/a.md\n\n- **Result:** PASS\n- **Exit code:** 0\n- **Findings:** 0\n- **Hard findings:** 0\n- **Baseline:** 0\n- **Words:** 0\n- **Findings per 100 words:** 0\n\nNo STE findings were recorded for this file.\n\n## 9. Structured evidence and integrity\n\n- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.\n- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.\n- **index.json:** Run locator and summary metadata, ordered newest first.\n- **history:** Immutable report files for each run ID and attempt.\n- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.\n\nA successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.\n'

======================================================================
FAIL: test_source_task_id_is_recorded_for_push_commit (__main__.ReportGeneratorTests.test_source_task_id_is_recorded_for_push_commit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_generate_lint_report.py", line 180, in test_source_task_id_is_recorded_for_push_commit
    self.assertIn("Source task: 20261127-090000", markdown)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'Source task: 20261127-090000' not found in '# On Repo STE Lint Evidence Report\n\n- **Result:** Passed\n- **Schema version:** 1.2.0\n- **Run:** [#901](https://example.invalid/run/901)\n- **Run ID / attempt:** 901 / 1\n- **Workflow:** Test lint report\n- **Branch / commit:** gpt / abc123\n- **Source task:** 20261127-090000\n- **Event:** push\n- **Execution mode:** repository-wide\n- **Baseline SHA:** Not applicable\n- **Linter source SHA:** Unknown\n- **Generated (UTC):** 2026-11-27T10:19:42.824856+00:00\n\n## 1. Executive summary\n\n| Measure | Result |\n|---|---:|\n| Files evaluated | 1 |\n| Files that failed | 0 |\n| Files with findings | 0 |\n| Total findings | 0 |\n| Hard findings | 0 |\n| Advisory findings | 0 |\n| New findings | 0 |\n| Recurring findings | 0 |\n| Resolved findings | 0 |\n| Failed workflow checks | 0 |\n\n## 2. Execution environment\n\n- Runner OS: Linux\n- Python: 3.15.2\n- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43\n- The JSON report records the full runtime version and every original per-file linter response.\n- The report records the commit that supplied the linter and generator code.\n\n## 3. Exact evaluation coverage\n\nThis list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.\n\n- docs/a.md\n\n## 4. Per-file result matrix\n\nThe table includes every evaluated file, including files with zero findings and files with execution errors.\n\n| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| docs/a.md | PASS | 0 | 0 | 0 | 0 | 0 | 0 |\n\n## 5. Findings by rule\n\nCounts include hard and advisory findings.\n\nNo findings.\n\n## 6. Workflow and validation checks\n\nEach check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.\n\nNo separate workflow checks were recorded.\n\n## 7. Baseline comparison\n\nFingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.\n\n### New findings\n\nNone.\n\n### Recurring findings\n\nNone.\n\n### Resolved findings\n\nNone.\n\n## 8. Complete per-file diagnostics\n\nThis section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.\n\n### docs/a.md\n\n- **Result:** PASS\n- **Exit code:** 0\n- **Findings:** 0\n- **Hard findings:** 0\n- **Baseline:** 0\n- **Words:** 0\n- **Findings per 100 words:** 0\n\nNo STE findings were recorded for this file.\n\n## 9. Structured evidence and integrity\n\n- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.\n- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.\n- **index.json:** Run locator and summary metadata, ordered newest first.\n- **history:** Immutable report files for each run ID and attempt.\n- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.\n\nA successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.\n'

----------------------------------------------------------------------
Ran 6 tests in 0.463s

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
Scanned 5 changed Markdown sources (371 available as link targets) and 37 local Markdown links.
Found 1 unresolved local Markdown targets or anchors.
workspace/task_board.md: missing Markdown file: tasks/20261126-142500/subtasks/20-ci-remediation-review-passive-voice-findings-in-workspace-task-board-md.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/SESSION_START.md:41:99 · **new** · fingerprint: b364e80e8c98116d3ebcfb38
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **synonym-rotation** · .agent/SESSION_START.md:52:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/SESSION_START.md:92:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:93:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · .agent/SESSION_START.md:237:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
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
- **long-sentence** · .agent/skills/the-worker/SKILL.md:19:3 · **new** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
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
- **semicolon** · .agent/skills/the-worker/SKILL.md:49:169 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
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
- **semicolon** · .agent/skills/the-worker/SKILL.md:65:146 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:67:77 · **new** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · .agent/skills/the-worker/SKILL.md:69:53 · **new** · fingerprint: b336f74954a3548f82ab7c54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were executed
- **semicolon** · .agent/skills/the-worker/SKILL.md:69:175 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:90:139 · **new** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:90:169 · **new** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **long-sentence** · .agent/skills/the-worker/SKILL.md:91:182 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:91:201 · **new** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **semicolon** · .agent/skills/the-worker/SKILL.md:91:409 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:93:217 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:105:307 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:107:103 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:107:295 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Recurring findings

- **semicolon** · workspace/task_board.md:5:113 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:7:13 · **recurring** · fingerprint: ec19da848a6fcda5c3642ea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is checked
- **passive-voice** · workspace/task_board.md:7:133 · **recurring** · fingerprint: 4e5e525ca51a4e0ca4df72f4
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
- **synonym-rotation** · workspace/task_board.md:53:24 · **recurring** · fingerprint: 61290a3569b589a88314b958
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** Fix
- **semicolon** · workspace/task_board.md:53:176 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/task_board.md:63:132 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Resolved findings

- **passive-voice** · workspace/TASK_TEMPLATE.md:23:182 · **resolved** · fingerprint: 174cb92f03c94b341eec0955
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **semicolon** · workspace/TASK_TEMPLATE.md:23:259 · **resolved** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/TASK_TEMPLATE.md:76:135 · **resolved** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:76:153 · **resolved** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:26:92 · **resolved** · fingerprint: 77496caee1aa1b14090beb02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **long-sentence** · workspace/SUBTASK_TEMPLATE.md:26:107 · **resolved** · fingerprint: 75ec0bdcda44d39480fbac03
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:26:177 · **resolved** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:26:245 · **resolved** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:65:104 · **resolved** · fingerprint: ab76e7bf8f0141a1ea1aec79
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 439
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 2931
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **synonym-rotation** · .agent/SESSION_START.md:41:99 · **new** · fingerprint: b364e80e8c98116d3ebcfb38
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch

- **synonym-rotation** · .agent/SESSION_START.md:52:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · .agent/SESSION_START.md:92:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/SESSION_START.md:93:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **passive-voice** · .agent/SESSION_START.md:237:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
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


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 22
- **Hard findings:** 17
- **Baseline:** 0
- **Words:** 1504
- **Findings per 100 words:** 1.5

#### Complete diagnostics

- **long-sentence** · .agent/skills/the-worker/SKILL.md:19:3 · **new** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

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

- **semicolon** · .agent/skills/the-worker/SKILL.md:49:169 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

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

- **semicolon** · .agent/skills/the-worker/SKILL.md:65:146 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:67:77 · **new** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **passive-voice** · .agent/skills/the-worker/SKILL.md:69:53 · **new** · fingerprint: b336f74954a3548f82ab7c54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were executed

- **semicolon** · .agent/skills/the-worker/SKILL.md:69:175 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:90:139 · **new** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:90:169 · **new** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin

- **long-sentence** · .agent/skills/the-worker/SKILL.md:91:182 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:91:201 · **new** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **semicolon** · .agent/skills/the-worker/SKILL.md:91:409 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:93:217 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:105:307 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:107:103 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:107:295 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 11
- **Hard findings:** 8
- **Baseline:** 0
- **Words:** 533
- **Findings per 100 words:** 2.1

#### Complete diagnostics

- **semicolon** · workspace/task_board.md:5:113 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:7:13 · **recurring** · fingerprint: ec19da848a6fcda5c3642ea6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is checked

- **passive-voice** · workspace/task_board.md:7:133 · **recurring** · fingerprint: 4e5e525ca51a4e0ca4df72f4
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

- **synonym-rotation** · workspace/task_board.md:53:24 · **recurring** · fingerprint: 61290a3569b589a88314b958
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** Fix

- **semicolon** · workspace/task_board.md:53:176 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/task_board.md:63:132 · **recurring** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/document-standards/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 60
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
