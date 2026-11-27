# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#1044](https://github.com/dungnv2602/chatgpt/actions/runs/46020530596)
- **Run ID / attempt:** 46020530596 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 14d4c19a70bf36217313b3a7dc1a84401d0f9113
- **Source task:** Unassigned
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 9c2adb27eff65c81b7bb768cf9f6dab9196db481
- **Linter source SHA:** 14d4c19a70bf36217313b3a7dc1a84401d0f9113
- **Generated (UTC):** 2026-11-27T15:12:56.990047+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 12 |
| Files that failed | 8 |
| Files with findings | 11 |
| Total findings | 41 |
| Hard findings | 22 |
| Advisory findings | 19 |
| New findings | 34 |
| Recurring findings | 7 |
| Resolved findings | 2 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/assets/README.md
- .agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md
- .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md
- .agent/skills/the-worker/assets/ADR_TEMPLATE.md
- .agent/skills/the-worker/SKILL.md
- .agent/skills/the-worker/references/document-type-catalog.md
- .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md
- .agent/skills/the-worker/assets/TASK_TEMPLATE.md
- .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md
- workspace/task_board.md
- workspace/README.md
- .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/assets/README.md | FAIL | 1 | 1 | 0 | 90 | 1.1 | 1 |
| .agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md | PASS | 1 | 0 | 0 | 384 | 0.3 | 0 |
| .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md | FAIL | 5 | 3 | 0 | 330 | 1.5 | 1 |
| .agent/skills/the-worker/assets/ADR_TEMPLATE.md | PASS | 0 | 0 | 0 | 349 | 0.0 | 0 |
| .agent/skills/the-worker/SKILL.md | FAIL | 4 | 4 | 0 | 2677 | 0.1 | 1 |
| .agent/skills/the-worker/references/document-type-catalog.md | FAIL | 3 | 3 | 0 | 4584 | 0.1 | 1 |
| .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md | FAIL | 6 | 4 | 0 | 433 | 1.4 | 1 |
| .agent/skills/the-worker/assets/TASK_TEMPLATE.md | FAIL | 4 | 2 | 0 | 461 | 0.9 | 1 |
| .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md | PASS | 2 | 0 | 0 | 175 | 1.1 | 0 |
| workspace/task_board.md | FAIL | 4 | 1 | 0 | 1166 | 0.3 | 1 |
| workspace/README.md | PASS | 2 | 0 | 0 | 521 | 0.4 | 0 |
| .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md | FAIL | 9 | 4 | 0 | 1242 | 0.7 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 19 |
| semicolon | 14 |
| long-sentence | 4 |
| synonym-rotation | 4 |

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
Ran 6 tests in 0.394s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.025s

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
Scanned 12 changed Markdown sources (447 available as link targets) and 62 local Markdown links.
Found 24 unresolved local Markdown targets or anchors.
.agent/skills/the-worker/assets/TASK_TEMPLATE.md: missing Markdown file: subtasks/README.md
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

- **semicolon** · .agent/skills/the-worker/assets/README.md:19:120 · **new** · fingerprint: 19955fcc943cf8eeee92b44a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md:53:50 · **new** · fingerprint: 9a3dfb833eec48c088dd3ac5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:11:87 · **new** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:27 · **new** · fingerprint: 6c97e45994588b7aa8554e68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is occupied
- **passive-voice** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:52 · **new** · fingerprint: 8cf80886a3416c97628e4968
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:63 · **new** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:51:159 · **new** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:141:71 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:43:153 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:44:297 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:131:297 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:92 · **new** · fingerprint: 5bfccaea8cce744d68ac5ecf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **long-sentence** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:107 · **new** · fingerprint: 649db466b9f274a2a7a09e91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:177 · **new** · fingerprint: e991d925d19d54686d821bd0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:245 · **new** · fingerprint: e991d925d19d54686d821bd0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:58:5 · **new** · fingerprint: 1b2e52219335b463f7d98b72
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Checks
- **passive-voice** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:67:104 · **new** · fingerprint: 17f20f329349a83ed7e99014
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:25:182 · **new** · fingerprint: e018527647fd5d9cda70e20b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **semicolon** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:25:259 · **new** · fingerprint: d41c279493ed98cb17be6862
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:78:135 · **new** · fingerprint: d41c279493ed98cb17be6862
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:78:153 · **new** · fingerprint: 0aa322b1177153d8a1782ce5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **passive-voice** · .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md:11:135 · **new** · fingerprint: fe46427e0d26f8d6d2c1beac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md:19:77 · **new** · fingerprint: 7a6a1d5106ec02299859cbeb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · workspace/README.md:27:210 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/README.md:47:209 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:25:119 · **new** · fingerprint: e39ef11f5de0397fccbd4300
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:51:26 · **new** · fingerprint: bf3935a0a8bd3a21bede2664
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were identified
- **semicolon** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:53:58 · **new** · fingerprint: 35b120d44eaf302e06cc3ea3
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:63:103 · **new** · fingerprint: 35b120d44eaf302e06cc3ea3
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:78:47 · **new** · fingerprint: 34506057e79270f827c32ab2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:91:47 · **new** · fingerprint: 34506057e79270f827c32ab2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **long-sentence** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:111:75 · **new** · fingerprint: fa568bf51d5baecd16642740
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:124:55 · **new** · fingerprint: 60478eb314584bde9e22cd50
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **synonym-rotation** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:166:28 · **new** · fingerprint: 748a26ac5faada2929a3a339
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

### Recurring findings

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:87:19 · **recurring** · fingerprint: 4900e43fc0a2db0bbbee87ae
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · .agent/skills/the-worker/SKILL.md:173:47 · **recurring** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:183:108 · **recurring** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · workspace/task_board.md:17:137 · **recurring** · fingerprint: 92838e68c54a583cee272835
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is closed
- **passive-voice** · workspace/task_board.md:26:9 · **recurring** · fingerprint: ed2247bc287f94142d470682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected
- **synonym-rotation** · workspace/task_board.md:73:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/task_board.md:73:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Resolved findings

- **long-sentence** · .agent/skills/the-worker/references/github-actions.md:45:3 · **resolved** · fingerprint: 933a579fb10c54b6f0b0201a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/the-worker/references/github-actions.md:199:103 · **resolved** · fingerprint: 2ae048d7121a7648e37f1f35
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are maintained

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/assets/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 90
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/assets/README.md:19:120 · **new** · fingerprint: 19955fcc943cf8eeee92b44a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 384
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md:53:50 · **new** · fingerprint: 9a3dfb833eec48c088dd3ac5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified


### .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 5
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 330
- **Findings per 100 words:** 1.5

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:11:87 · **new** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:27 · **new** · fingerprint: 6c97e45994588b7aa8554e68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is occupied

- **passive-voice** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:52 · **new** · fingerprint: 8cf80886a3416c97628e4968
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:63 · **new** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:51:159 · **new** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/the-worker/assets/ADR_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 349
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 2677
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:87:19 · **recurring** · fingerprint: 4900e43fc0a2db0bbbee87ae
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **semicolon** · .agent/skills/the-worker/SKILL.md:141:71 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/SKILL.md:173:47 · **recurring** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **long-sentence** · .agent/skills/the-worker/SKILL.md:183:108 · **recurring** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words


### .agent/skills/the-worker/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 4584
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:43:153 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:44:297 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:131:297 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 433
- **Findings per 100 words:** 1.4

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:92 · **new** · fingerprint: 5bfccaea8cce744d68ac5ecf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **long-sentence** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:107 · **new** · fingerprint: 649db466b9f274a2a7a09e91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:177 · **new** · fingerprint: e991d925d19d54686d821bd0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:245 · **new** · fingerprint: e991d925d19d54686d821bd0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:58:5 · **new** · fingerprint: 1b2e52219335b463f7d98b72
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Checks

- **passive-voice** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:67:104 · **new** · fingerprint: 17f20f329349a83ed7e99014
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read


### .agent/skills/the-worker/assets/TASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 461
- **Findings per 100 words:** 0.9

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:25:182 · **new** · fingerprint: e018527647fd5d9cda70e20b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **semicolon** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:25:259 · **new** · fingerprint: d41c279493ed98cb17be6862
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:78:135 · **new** · fingerprint: d41c279493ed98cb17be6862
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:78:153 · **new** · fingerprint: 0aa322b1177153d8a1782ce5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted


### .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 175
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md:11:135 · **new** · fingerprint: fe46427e0d26f8d6d2c1beac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **passive-voice** · .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md:19:77 · **new** · fingerprint: 7a6a1d5106ec02299859cbeb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1166
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:17:137 · **recurring** · fingerprint: 92838e68c54a583cee272835
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is closed

- **passive-voice** · workspace/task_board.md:26:9 · **recurring** · fingerprint: ed2247bc287f94142d470682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected

- **synonym-rotation** · workspace/task_board.md:73:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **passive-voice** · workspace/task_board.md:73:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred


### workspace/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 521
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **passive-voice** · workspace/README.md:27:210 · **new** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/README.md:47:209 · **new** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified


### .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 1242
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:25:119 · **new** · fingerprint: e39ef11f5de0397fccbd4300
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:51:26 · **new** · fingerprint: bf3935a0a8bd3a21bede2664
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were identified

- **semicolon** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:53:58 · **new** · fingerprint: 35b120d44eaf302e06cc3ea3
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:63:103 · **new** · fingerprint: 35b120d44eaf302e06cc3ea3
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:78:47 · **new** · fingerprint: 34506057e79270f827c32ab2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:91:47 · **new** · fingerprint: 34506057e79270f827c32ab2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **long-sentence** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:111:75 · **new** · fingerprint: fa568bf51d5baecd16642740
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:124:55 · **new** · fingerprint: 60478eb314584bde9e22cd50
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified

- **synonym-rotation** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:166:28 · **new** · fingerprint: 748a26ac5faada2929a3a339
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
