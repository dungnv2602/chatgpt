# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#943](https://github.com/dungnv2602/chatgpt/actions/runs/45966409448)
- **Run ID / attempt:** 45966409448 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 2bfafa7b7fea00a93b3290eac643fdb27a414ada
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 95ad9b2a3b21604bcc3be56826dc2ac7a2503fe7
- **Linter source SHA:** 2bfafa7b7fea00a93b3290eac643fdb27a414ada
- **Generated (UTC):** 2026-11-27T08:33:13.414412+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 7 |
| Files that failed | 7 |
| Files with findings | 7 |
| Total findings | 55 |
| Hard findings | 26 |
| Advisory findings | 29 |
| New findings | 30 |
| Recurring findings | 25 |
| Resolved findings | 16 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/SKILL.md
- .agent/skills/document-standards/references/document-type-catalog.md
- .agent/skills/the-worker/references/conversation-mode.md
- workspace/task_board.md
- workspace/TASK_TEMPLATE.md
- workspace/README.md
- workspace/SUBTASK_TEMPLATE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/SKILL.md | FAIL | 20 | 11 | 0 | 930 | 2.2 | 1 |
| .agent/skills/document-standards/references/document-type-catalog.md | FAIL | 6 | 2 | 0 | 4603 | 0.1 | 1 |
| .agent/skills/the-worker/references/conversation-mode.md | FAIL | 6 | 2 | 0 | 335 | 1.8 | 1 |
| workspace/task_board.md | FAIL | 5 | 1 | 0 | 491 | 1.0 | 1 |
| workspace/TASK_TEMPLATE.md | FAIL | 10 | 5 | 0 | 588 | 1.7 | 1 |
| workspace/README.md | FAIL | 4 | 2 | 0 | 1222 | 0.3 | 1 |
| workspace/SUBTASK_TEMPLATE.md | FAIL | 4 | 3 | 0 | 526 | 0.8 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 26 |
| semicolon | 18 |
| synonym-rotation | 6 |
| present-perfect | 3 |
| long-sentence | 2 |

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
Ran 4 tests in 0.362s

OK
~~~

### Markdown anchor regression tests

- **Result:** Failed
- **Exit code:** 1

~~~~~~~~~~~~~~~~~~~~~~~text
..F.....
======================================================================
FAIL: test_incremental_scope_rejects_inactive_or_untracked_sources (__main__.MarkdownAnchorTests.test_incremental_scope_rejects_inactive_or_untracked_sources) (path='.archive/adr/old.md')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_check_markdown_anchors.py", line 80, in test_incremental_scope_rejects_inactive_or_untracked_sources
    with self.assertRaisesRegex(ValueError, "inactive or untracked"):
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 8 tests in 0.007s

FAILED (failures=1)
~~~~~~~~~~~~~~~~~~~~~~~

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
Scanned 7 changed Markdown sources (372 available as link targets) and 23 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:13:267 · **new** · fingerprint: 646b7bb10f9a4afa968e76a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · .agent/skills/the-worker/SKILL.md:34:286 · **new** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected
- **passive-voice** · .agent/skills/the-worker/SKILL.md:35:16 · **new** · fingerprint: 744124c649cfe9432abfa28d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are collected
- **long-sentence** · .agent/skills/the-worker/SKILL.md:36:67 · **new** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:38:116 · **new** · fingerprint: 15f03876d973741a8c5cb8e4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is completed
- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:29 · **new** · fingerprint: a5d55557cb1399d0acf7ac08
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:167 · **new** · fingerprint: 741749aa0db79422e1509169
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **passive-voice** · .agent/skills/the-worker/SKILL.md:56:300 · **new** · fingerprint: 39ce18413ef5d1941ef0df0a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is omitted
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:56:319 · **new** · fingerprint: 4a50516b3278c464640d6067
  - **Level:** advisory-free
  - **Message:** 'initiate' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** initiate
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:17 · **new** · fingerprint: 485cc95c832398176cc2730f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:294 · **new** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected
- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:131:297 · **new** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:143 · **new** · fingerprint: 42f86e8fba1534a97a0dd2a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:228 · **new** · fingerprint: de21f21791e1cf986fde4201
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:89 · **new** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:179 · **new** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **synonym-rotation** · .agent/skills/document-standards/references/document-type-catalog.md:213:206 · **new** · fingerprint: 4fc10f3be849a3fb43a60d2a
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:20:214 · **new** · fingerprint: 6ae9a6a4a2db5981a11a3382
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been collected
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:20:219 · **new** · fingerprint: bdeb60b7ecf5b8b23d08fe8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been collected
- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:26:339 · **new** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:26:365 · **new** · fingerprint: 20ab01d0763dc8b1779dc36e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:26:378 · **new** · fingerprint: bd4591524e78ee2f7fa8b868
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:30:156 · **new** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **semicolon** · workspace/task_board.md:9:184 · **new** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:9:211 · **new** · fingerprint: 2576c78693220ab79f5566ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · workspace/task_board.md:19:66 · **new** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed
- **passive-voice** · workspace/task_board.md:21:77 · **new** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **passive-voice** · workspace/task_board.md:62:97 · **new** · fingerprint: d8beb3526c98bbf7b37d724b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied
- **passive-voice** · workspace/TASK_TEMPLATE.md:20:60 · **new** · fingerprint: d6cb213a49d24318311d0da8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:19:60 · **new** · fingerprint: f1ec495bc7a973b2581b8695
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Recurring findings

- **semicolon** · .agent/skills/the-worker/SKILL.md:5:170 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:13:238 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:19:316 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:35:108 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:42:257 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:44:81 · **recurring** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:147 · **recurring** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **semicolon** · .agent/skills/the-worker/SKILL.md:62:232 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:62:275 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/TASK_TEMPLATE.md:24:152 · **recurring** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/TASK_TEMPLATE.md:24:182 · **recurring** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/TASK_TEMPLATE.md:28:42 · **recurring** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/TASK_TEMPLATE.md:30:136 · **recurring** · fingerprint: 3a0997aa00ae589847e48a35
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · workspace/TASK_TEMPLATE.md:58:32 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:84:20 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:85:23 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **semicolon** · workspace/TASK_TEMPLATE.md:101:110 · **recurring** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:101:247 · **recurring** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **semicolon** · workspace/README.md:36:183 · **recurring** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:36:210 · **recurring** · fingerprint: 7db95bfd4fd923e46bee569d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · workspace/README.md:36:484 · **recurring** · fingerprint: f5049c86552d80c254f92f30
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **synonym-rotation** · workspace/README.md:48:200 · **recurring** · fingerprint: d8d5bdd914126f90076410ea
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:28:42 · **recurring** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:84:152 · **recurring** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/SUBTASK_TEMPLATE.md:84:182 · **recurring** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Resolved findings

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:50:216 · **resolved** · fingerprint: 51ff27cef408cb594ac67b7c
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **long-sentence** · .agent/skills/the-worker/SKILL.md:52:6 · **resolved** · fingerprint: c09f1bc6b6ff605eea355d56
  - **Level:** advisory-free
  - **Message:** Sentence has 40 words (cap 25). Split it.
  - **Matched text:** 40 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:219 · **resolved** · fingerprint: 607a101b2ac06f3f48c4f94f
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** correct
- **long-sentence** · .agent/skills/the-worker/SKILL.md:55:51 · **resolved** · fingerprint: e50de15b76c7c77c6df3a052
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:55:435 · **resolved** · fingerprint: 33645e288105a4650deff87a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is declined
- **passive-voice** · .agent/skills/the-worker/SKILL.md:57:393 · **resolved** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:72 · **resolved** · fingerprint: cdb8abd8d99c0c48c49b64ed
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is drained
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:164 · **resolved** · fingerprint: 2be96c6aa40a9ac717577677
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was resolved
- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:464 · **resolved** · fingerprint: ed0aae51db7a829a76e63e74
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exhausted
- **passive-voice** · .agent/skills/the-worker/SKILL.md:127:40 · **resolved** · fingerprint: 58a47654e8fe2ff210753ac7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · .agent/skills/the-worker/SKILL.md:187:43 · **resolved** · fingerprint: cd17c3f4dff3482f2ea98682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been granted
- **passive-voice** · .agent/skills/the-worker/SKILL.md:225:91 · **resolved** · fingerprint: 448e62e062b885437ed3015e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **passive-voice** · .agent/skills/the-worker/SKILL.md:273:144 · **resolved** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:278:3 · **resolved** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:366:196 · **resolved** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:398:33 · **resolved** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 20
- **Hard findings:** 11
- **Baseline:** 0
- **Words:** 930
- **Findings per 100 words:** 2.2

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/SKILL.md:5:170 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:13:238 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:13:267 · **new** · fingerprint: 646b7bb10f9a4afa968e76a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **semicolon** · .agent/skills/the-worker/SKILL.md:19:316 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:34:286 · **new** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected

- **passive-voice** · .agent/skills/the-worker/SKILL.md:35:16 · **new** · fingerprint: 744124c649cfe9432abfa28d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are collected

- **semicolon** · .agent/skills/the-worker/SKILL.md:35:108 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/SKILL.md:36:67 · **new** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:38:116 · **new** · fingerprint: 15f03876d973741a8c5cb8e4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is completed

- **semicolon** · .agent/skills/the-worker/SKILL.md:42:257 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:44:81 · **recurring** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:52:147 · **recurring** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:29 · **new** · fingerprint: a5d55557cb1399d0acf7ac08
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received

- **present-perfect** · .agent/skills/the-worker/SKILL.md:56:167 · **new** · fingerprint: 741749aa0db79422e1509169
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **passive-voice** · .agent/skills/the-worker/SKILL.md:56:300 · **new** · fingerprint: 39ce18413ef5d1941ef0df0a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is omitted

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:56:319 · **new** · fingerprint: 4a50516b3278c464640d6067
  - **Level:** advisory-free
  - **Message:** 'initiate' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** initiate

- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:17 · **new** · fingerprint: 485cc95c832398176cc2730f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/skills/the-worker/SKILL.md:58:294 · **new** · fingerprint: 191f16d660022070d80486cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is collected

- **semicolon** · .agent/skills/the-worker/SKILL.md:62:232 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:62:275 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 4603
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **semicolon** · .agent/skills/document-standards/references/document-type-catalog.md:131:297 · **new** · fingerprint: e2e4500a529bb5cf3751722a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:143 · **new** · fingerprint: 42f86e8fba1534a97a0dd2a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:228 · **new** · fingerprint: de21f21791e1cf986fde4201
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:89 · **new** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:179 · **new** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted

- **synonym-rotation** · .agent/skills/document-standards/references/document-type-catalog.md:213:206 · **new** · fingerprint: 4fc10f3be849a3fb43a60d2a
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks


### .agent/skills/the-worker/references/conversation-mode.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 335
- **Findings per 100 words:** 1.8

#### Complete diagnostics

- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:20:214 · **new** · fingerprint: 6ae9a6a4a2db5981a11a3382
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been collected

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:20:219 · **new** · fingerprint: bdeb60b7ecf5b8b23d08fe8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been collected

- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:26:339 · **new** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:26:365 · **new** · fingerprint: 20ab01d0763dc8b1779dc36e
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:26:378 · **new** · fingerprint: bd4591524e78ee2f7fa8b868
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:30:156 · **new** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 5
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 491
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **semicolon** · workspace/task_board.md:9:184 · **new** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/task_board.md:9:211 · **new** · fingerprint: 2576c78693220ab79f5566ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **passive-voice** · workspace/task_board.md:19:66 · **new** · fingerprint: 41baa6b366e177c2499f5233
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are listed

- **passive-voice** · workspace/task_board.md:21:77 · **new** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

- **passive-voice** · workspace/task_board.md:62:97 · **new** · fingerprint: d8beb3526c98bbf7b37d724b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is satisfied


### workspace/TASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 10
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 588
- **Findings per 100 words:** 1.7

#### Complete diagnostics

- **passive-voice** · workspace/TASK_TEMPLATE.md:20:60 · **new** · fingerprint: d6cb213a49d24318311d0da8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

- **semicolon** · workspace/TASK_TEMPLATE.md:24:152 · **recurring** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/TASK_TEMPLATE.md:24:182 · **recurring** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/TASK_TEMPLATE.md:28:42 · **recurring** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/TASK_TEMPLATE.md:30:136 · **recurring** · fingerprint: 3a0997aa00ae589847e48a35
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **passive-voice** · workspace/TASK_TEMPLATE.md:58:32 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **passive-voice** · workspace/TASK_TEMPLATE.md:84:20 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **passive-voice** · workspace/TASK_TEMPLATE.md:85:23 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **semicolon** · workspace/TASK_TEMPLATE.md:101:110 · **recurring** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/TASK_TEMPLATE.md:101:247 · **recurring** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1222
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · workspace/README.md:36:183 · **recurring** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/README.md:36:210 · **recurring** · fingerprint: 7db95bfd4fd923e46bee569d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **passive-voice** · workspace/README.md:36:484 · **recurring** · fingerprint: f5049c86552d80c254f92f30
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **synonym-rotation** · workspace/README.md:48:200 · **recurring** · fingerprint: d8d5bdd914126f90076410ea
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove


### workspace/SUBTASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 526
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · workspace/SUBTASK_TEMPLATE.md:19:60 · **new** · fingerprint: f1ec495bc7a973b2581b8695
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

- **semicolon** · workspace/SUBTASK_TEMPLATE.md:28:42 · **recurring** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/SUBTASK_TEMPLATE.md:84:152 · **recurring** · fingerprint: ae777a92ddc5d2c5149411bc
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/SUBTASK_TEMPLATE.md:84:182 · **recurring** · fingerprint: ae777a92ddc5d2c5149411bc
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
