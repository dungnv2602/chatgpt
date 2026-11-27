# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#1006](https://github.com/dungnv2602/chatgpt/actions/runs/46005287766)
- **Run ID / attempt:** 46005287766 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 958b18f9878db02cc9cbf3e788b27d54dbbb4a87
- **Source task:** 20261127-173000-15
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 86ef132fb4948487f7f8aefe324ca1b74e19db0f
- **Linter source SHA:** 958b18f9878db02cc9cbf3e788b27d54dbbb4a87
- **Generated (UTC):** 2026-11-27T13:14:13.896038+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 2 |
| Files with findings | 3 |
| Total findings | 27 |
| Hard findings | 18 |
| Advisory findings | 9 |
| New findings | 25 |
| Recurring findings | 2 |
| Resolved findings | 7 |
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
- workspace/task_board.md
- .agent/skills/asd-ste100/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/SKILL.md | FAIL | 10 | 10 | 0 | 2543 | 0.4 | 1 |
| workspace/task_board.md | FAIL | 2 | 1 | 0 | 1468 | 0.1 | 1 |
| .agent/skills/asd-ste100/SKILL.md | PASS | 15 | 7 | 31 | 2616 | 0.6 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 7 |
| passive-voice | 6 |
| marketing-adjective | 5 |
| long-sentence | 4 |
| present-perfect | 3 |
| nominalization | 2 |

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
Ran 6 tests in 0.443s

OK
~~~

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
Scanned 3 changed Markdown sources (440 available as link targets) and 40 local Markdown links.
Found 33 unresolved local Markdown targets or anchors.
workspace/task_board.md: missing Markdown file: 16-ci-remediation-review-semicolon-findings-in-agent-skills-the-worker-references.md
workspace/task_board.md: missing Markdown file: 17-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-skil.md
workspace/task_board.md: missing Markdown file: 18-ci-remediation-review-passive-voice-findings-in-agent-session-start-md.md
workspace/task_board.md: missing Markdown file: 19-ci-remediation-review-passive-voice-findings-in-agent-skills-asd-ste100-skill-m.md
workspace/task_board.md: missing Markdown file: 20-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md
workspace/task_board.md: missing Markdown file: 21-ci-remediation-review-semicolon-findings-in-workspace-readme-md.md
workspace/task_board.md: missing Markdown file: 22-ci-remediation-review-synonym-rotation-findings-in-agent-skills-the-worker-refe.md
workspace/task_board.md: missing Markdown file: 23-ci-remediation-review-long-sentence-findings-in-agent-skills-the-worker-skill-m.md
workspace/task_board.md: missing Markdown file: 24-ci-remediation-review-passive-voice-findings-in-agent-skills-the-worker-referen.md
workspace/task_board.md: missing Markdown file: 26-ci-remediation-review-long-sentence-findings-in-agent-session-start-md.md
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

- **long-sentence** · .agent/skills/the-worker/SKILL.md:112:3 · **new** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:116:70 · **new** · fingerprint: 030301d369a6833422178b29
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:116:330 · **new** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:124:139 · **new** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:124:169 · **new** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **long-sentence** · .agent/skills/the-worker/SKILL.md:125:182 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:125:201 · **new** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:171:286 · **new** · fingerprint: f071e35d93664b24286e6bb7
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:172:302 · **new** · fingerprint: 5d8336dc915865ae43f6b3a8
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **long-sentence** · .agent/skills/the-worker/SKILL.md:174:140 · **new** · fingerprint: f32bb2e57cc49f8136c280d8
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:21:69 · **new** · fingerprint: 170e10c67c5ddb4ac54ea4b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was violated
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:49:227 · **new** · fingerprint: cb0ac7a2c5dda8b0dbd1051d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are defined
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:57:60 · **new** · fingerprint: 8a011f6518e4f647accaa107
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:73:118 · **new** · fingerprint: 28ef39a3cb8b2ca848f4ec97
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **nominalization** · .agent/skills/asd-ste100/SKILL.md:74:53 · **new** · fingerprint: 7e86fc5d602e4865ed4a0ff6
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:79:203 · **new** · fingerprint: 7a15da17f8212acf9cbcd80a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:81:140 · **new** · fingerprint: 320768d857c6a3e84654f3f5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed
- **nominalization** · .agent/skills/asd-ste100/SKILL.md:89:56 · **new** · fingerprint: fa833ca0d8a25be575faf6e0
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:79 · **new** · fingerprint: 12a9fb2640f958cc7e75f621
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:89 · **new** · fingerprint: c50be8a609eda6ecc738029b
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:107 · **new** · fingerprint: d7e2c69987f9328ac247ac53
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:121 · **new** · fingerprint: 0d5ed7f9257c40733f5c321d
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:133 · **new** · fingerprint: 2673e9a5ae5dd03778f880c9
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:113:134 · **new** · fingerprint: 361fe239198e1c7837a878ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:146:58 · **new** · fingerprint: 9efba8ed23b805f9a79bdc62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized

### Recurring findings

- **synonym-rotation** · workspace/task_board.md:77:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/task_board.md:77:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Resolved findings

- **passive-voice** · .agent/SESSION_START.md:22:209 · **resolved** · fingerprint: 00654de2a95772d4a870e55f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being fetched
- **passive-voice** · .agent/SESSION_START.md:92:158 · **resolved** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:93:60 · **resolved** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **synonym-rotation** · .agent/SESSION_START.md:177:7 · **resolved** · fingerprint: 93101ce1787c7b9208b4031d
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** retrieved
- **passive-voice** · .agent/SESSION_START.md:237:164 · **resolved** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · .agent/SESSION_START.md:253:154 · **resolved** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · .agent/SESSION_START.md:278:1 · **resolved** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 10
- **Hard findings:** 10
- **Baseline:** 0
- **Words:** 2543
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **long-sentence** · .agent/skills/the-worker/SKILL.md:112:3 · **new** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · .agent/skills/the-worker/SKILL.md:116:70 · **new** · fingerprint: 030301d369a6833422178b29
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:116:330 · **new** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:124:139 · **new** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:124:169 · **new** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin

- **long-sentence** · .agent/skills/the-worker/SKILL.md:125:182 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:125:201 · **new** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:171:286 · **new** · fingerprint: f071e35d93664b24286e6bb7
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:172:302 · **new** · fingerprint: 5d8336dc915865ae43f6b3a8
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch

- **long-sentence** · .agent/skills/the-worker/SKILL.md:174:140 · **new** · fingerprint: f32bb2e57cc49f8136c280d8
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 1468
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · workspace/task_board.md:77:24 · **recurring** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **passive-voice** · workspace/task_board.md:77:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred


### .agent/skills/asd-ste100/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 15
- **Hard findings:** 7
- **Baseline:** 31
- **Words:** 2616
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:21:69 · **new** · fingerprint: 170e10c67c5ddb4ac54ea4b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was violated

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:49:227 · **new** · fingerprint: cb0ac7a2c5dda8b0dbd1051d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are defined

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:57:60 · **new** · fingerprint: 8a011f6518e4f647accaa107
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:73:118 · **new** · fingerprint: 28ef39a3cb8b2ca848f4ec97
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved

- **nominalization** · .agent/skills/asd-ste100/SKILL.md:74:53 · **new** · fingerprint: 7e86fc5d602e4865ed4a0ff6
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis

- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:79:203 · **new** · fingerprint: 7a15da17f8212acf9cbcd80a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received

- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:81:140 · **new** · fingerprint: 320768d857c6a3e84654f3f5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed

- **nominalization** · .agent/skills/asd-ste100/SKILL.md:89:56 · **new** · fingerprint: fa833ca0d8a25be575faf6e0
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:79 · **new** · fingerprint: 12a9fb2640f958cc7e75f621
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:89 · **new** · fingerprint: c50be8a609eda6ecc738029b
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:107 · **new** · fingerprint: d7e2c69987f9328ac247ac53
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:121 · **new** · fingerprint: 0d5ed7f9257c40733f5c321d
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless

- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:133 · **new** · fingerprint: 2673e9a5ae5dd03778f880c9
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast

- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:113:134 · **new** · fingerprint: 361fe239198e1c7837a878ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped

- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:146:58 · **new** · fingerprint: 9efba8ed23b805f9a79bdc62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
