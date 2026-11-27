# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#1045](https://github.com/dungnv2602/chatgpt/actions/runs/46023746732)
- **Run ID / attempt:** 46023746732 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 82c2e57bd88ead22220b21f7362139507796fc0a
- **Source task:** 20261127-173000-53
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 14d4c19a70bf36217313b3a7dc1a84401d0f9113
- **Linter source SHA:** 82c2e57bd88ead22220b21f7362139507796fc0a
- **Generated (UTC):** 2026-11-27T15:19:31.629341+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 5 |
| Files that failed | 4 |
| Files with findings | 5 |
| Total findings | 32 |
| Hard findings | 13 |
| Advisory findings | 19 |
| New findings | 26 |
| Recurring findings | 6 |
| Resolved findings | 35 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/references/image-provenance-and-webp.md
- .agent/skills/drawing/references/archive-and-delivery.md
- .agent/skills/the-worker/references/document-type-catalog.md
- workspace/task_board.md
- .takeout/images/README.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/references/image-provenance-and-webp.md | FAIL | 15 | 7 | 0 | 1248 | 1.2 | 1 |
| .agent/skills/drawing/references/archive-and-delivery.md | PASS | 3 | 1 | 7 | 458 | 0.7 | 0 |
| .agent/skills/the-worker/references/document-type-catalog.md | FAIL | 3 | 3 | 0 | 4577 | 0.1 | 1 |
| workspace/task_board.md | FAIL | 3 | 1 | 0 | 1168 | 0.3 | 1 |
| .takeout/images/README.md | FAIL | 8 | 1 | 0 | 2283 | 0.4 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 17 |
| semicolon | 8 |
| synonym-rotation | 5 |
| present-perfect | 2 |

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
Ran 6 tests in 0.461s

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

- **Result:** Failed
- **Exit code:** 1

~~~text
Scanned 5 changed Markdown sources (448 available as link targets) and 40 local Markdown links.
Found 23 unresolved local Markdown targets or anchors.
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

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:15:100 · **new** · fingerprint: 42ccfb93a745583fff3188b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:293 · **new** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:467 · **new** · fingerprint: caa7a81dbcbd2ca9a41f3f6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied
- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:592 · **new** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:29:579 · **new** · fingerprint: 327d345785066c739b823948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted
- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:29:621 · **new** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:40:4 · **new** · fingerprint: 691140761bb44de115fa7cff
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:43:106 · **new** · fingerprint: 6d33e304d616c2a0e3cf5f55
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated
- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:43:357 · **new** · fingerprint: 5e4c8482fd167c730eb47fe1
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:45:50 · **new** · fingerprint: cd327a2cb9681d781a088b3a
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:47:139 · **new** · fingerprint: 42ccfb93a745583fff3188b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:57:366 · **new** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:65 · **new** · fingerprint: eda9543144c60d68e835bcc2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **present-perfect** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:138 · **new** · fingerprint: 3e65c7310bbf6667184ee5cf
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been read
- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:143 · **new** · fingerprint: 0b7ac6199463b1f46f7ddf4f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **present-perfect** · .agent/skills/drawing/references/archive-and-delivery.md:11:167 · **new** · fingerprint: c5d02a5017b863230f3b252a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been verified
- **passive-voice** · .agent/skills/drawing/references/archive-and-delivery.md:11:172 · **new** · fingerprint: 6c7d74fe7edec2361ca15c24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **synonym-rotation** · .agent/skills/drawing/references/archive-and-delivery.md:45:13 · **new** · fingerprint: 8d54e05e87ff737f0d036438
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .takeout/images/README.md:17:543 · **new** · fingerprint: a46dcd004377371af1ad777b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted
- **passive-voice** · .takeout/images/README.md:61:255 · **new** · fingerprint: 4e96ea8fc825b297d7a1488f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged
- **passive-voice** · .takeout/images/README.md:65:214 · **new** · fingerprint: 800ff66f8c348885b5ff1143
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated
- **passive-voice** · .takeout/images/README.md:131:188 · **new** · fingerprint: 62a96cb11641d0e6d12549a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied
- **passive-voice** · .takeout/images/README.md:132:44 · **new** · fingerprint: d7861d12f8a807a189c2e6c2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · .takeout/images/README.md:179:203 · **new** · fingerprint: 02f6557a4c3a46774d4b12d6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **semicolon** · .takeout/images/README.md:220:266 · **new** · fingerprint: 4f3c09afea0131b6ca36b0d2
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .takeout/images/README.md:243:40 · **new** · fingerprint: eca026296a1fb006e7c0dd1c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved

### Recurring findings

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:43:153 · **recurring** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:44:297 · **recurring** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:130:297 · **recurring** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
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

- **semicolon** · .agent/skills/the-worker/assets/README.md:19:120 · **resolved** · fingerprint: 19955fcc943cf8eeee92b44a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/ANALYSIS_TEMPLATE.md:53:50 · **resolved** · fingerprint: 9a3dfb833eec48c088dd3ac5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:11:87 · **resolved** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:27 · **resolved** · fingerprint: 6c97e45994588b7aa8554e68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is occupied
- **passive-voice** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:52 · **resolved** · fingerprint: 8cf80886a3416c97628e4968
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:25:63 · **resolved** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md:51:159 · **resolved** · fingerprint: ac4ecbcdd3920329dda05e7a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:87:19 · **resolved** · fingerprint: 4900e43fc0a2db0bbbee87ae
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **semicolon** · .agent/skills/the-worker/SKILL.md:141:71 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/SKILL.md:173:47 · **resolved** · fingerprint: 009f1803dee803be87a4fa14
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:183:108 · **resolved** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:92 · **resolved** · fingerprint: 5bfccaea8cce744d68ac5ecf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **long-sentence** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:107 · **resolved** · fingerprint: 649db466b9f274a2a7a09e91
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:177 · **resolved** · fingerprint: e991d925d19d54686d821bd0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:28:245 · **resolved** · fingerprint: e991d925d19d54686d821bd0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:58:5 · **resolved** · fingerprint: 1b2e52219335b463f7d98b72
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Checks
- **passive-voice** · .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md:67:104 · **resolved** · fingerprint: 17f20f329349a83ed7e99014
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:25:182 · **resolved** · fingerprint: e018527647fd5d9cda70e20b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **semicolon** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:25:259 · **resolved** · fingerprint: d41c279493ed98cb17be6862
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:78:135 · **resolved** · fingerprint: d41c279493ed98cb17be6862
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/TASK_TEMPLATE.md:78:153 · **resolved** · fingerprint: 0aa322b1177153d8a1782ce5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **passive-voice** · .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md:11:135 · **resolved** · fingerprint: fe46427e0d26f8d6d2c1beac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md:19:77 · **resolved** · fingerprint: 7a6a1d5106ec02299859cbeb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · workspace/task_board.md:17:137 · **resolved** · fingerprint: 92838e68c54a583cee272835
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is closed
- **passive-voice** · workspace/README.md:27:210 · **resolved** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/README.md:47:209 · **resolved** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:25:119 · **resolved** · fingerprint: e39ef11f5de0397fccbd4300
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:51:26 · **resolved** · fingerprint: bf3935a0a8bd3a21bede2664
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were identified
- **semicolon** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:53:58 · **resolved** · fingerprint: 35b120d44eaf302e06cc3ea3
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:63:103 · **resolved** · fingerprint: 35b120d44eaf302e06cc3ea3
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:78:47 · **resolved** · fingerprint: 34506057e79270f827c32ab2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:91:47 · **resolved** · fingerprint: 34506057e79270f827c32ab2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **long-sentence** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:111:75 · **resolved** · fingerprint: fa568bf51d5baecd16642740
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:124:55 · **resolved** · fingerprint: 60478eb314584bde9e22cd50
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **synonym-rotation** · .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md:166:28 · **resolved** · fingerprint: 748a26ac5faada2929a3a339
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/references/image-provenance-and-webp.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 15
- **Hard findings:** 7
- **Baseline:** 0
- **Words:** 1248
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:15:100 · **new** · fingerprint: 42ccfb93a745583fff3188b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:293 · **new** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:467 · **new** · fingerprint: caa7a81dbcbd2ca9a41f3f6a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied

- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:27:592 · **new** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:29:579 · **new** · fingerprint: 327d345785066c739b823948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted

- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:29:621 · **new** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:40:4 · **new** · fingerprint: 691140761bb44de115fa7cff
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:43:106 · **new** · fingerprint: 6d33e304d616c2a0e3cf5f55
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated

- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:43:357 · **new** · fingerprint: 5e4c8482fd167c730eb47fe1
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms

- **synonym-rotation** · .agent/skills/the-worker/references/image-provenance-and-webp.md:45:50 · **new** · fingerprint: cd327a2cb9681d781a088b3a
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validates

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:47:139 · **new** · fingerprint: 42ccfb93a745583fff3188b6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **semicolon** · .agent/skills/the-worker/references/image-provenance-and-webp.md:57:366 · **new** · fingerprint: 87aa85f564e164014b1efb51
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:65 · **new** · fingerprint: eda9543144c60d68e835bcc2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed

- **present-perfect** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:138 · **new** · fingerprint: 3e65c7310bbf6667184ee5cf
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been read

- **passive-voice** · .agent/skills/the-worker/references/image-provenance-and-webp.md:61:143 · **new** · fingerprint: 0b7ac6199463b1f46f7ddf4f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read


### .agent/skills/drawing/references/archive-and-delivery.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 7
- **Words:** 458
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **present-perfect** · .agent/skills/drawing/references/archive-and-delivery.md:11:167 · **new** · fingerprint: c5d02a5017b863230f3b252a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been verified

- **passive-voice** · .agent/skills/drawing/references/archive-and-delivery.md:11:172 · **new** · fingerprint: 6c7d74fe7edec2361ca15c24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **synonym-rotation** · .agent/skills/drawing/references/archive-and-delivery.md:45:13 · **new** · fingerprint: 8d54e05e87ff737f0d036438
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify


### .agent/skills/the-worker/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 4577
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:43:153 · **recurring** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:44:297 · **recurring** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:130:297 · **recurring** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1168
- **Findings per 100 words:** 0.3

#### Complete diagnostics

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


### .takeout/images/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 2283
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **passive-voice** · .takeout/images/README.md:17:543 · **new** · fingerprint: a46dcd004377371af1ad777b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted

- **passive-voice** · .takeout/images/README.md:61:255 · **new** · fingerprint: 4e96ea8fc825b297d7a1488f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged

- **passive-voice** · .takeout/images/README.md:65:214 · **new** · fingerprint: 800ff66f8c348885b5ff1143
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is relocated

- **passive-voice** · .takeout/images/README.md:131:188 · **new** · fingerprint: 62a96cb11641d0e6d12549a8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supplied

- **passive-voice** · .takeout/images/README.md:132:44 · **new** · fingerprint: d7861d12f8a807a189c2e6c2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **passive-voice** · .takeout/images/README.md:179:203 · **new** · fingerprint: 02f6557a4c3a46774d4b12d6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

- **semicolon** · .takeout/images/README.md:220:266 · **new** · fingerprint: 4f3c09afea0131b6ca36b0d2
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .takeout/images/README.md:243:40 · **new** · fingerprint: eca026296a1fb006e7c0dd1c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
