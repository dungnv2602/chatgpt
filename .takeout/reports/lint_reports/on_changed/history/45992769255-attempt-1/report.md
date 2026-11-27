# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#992](https://github.com/dungnv2602/chatgpt/actions/runs/45992769255)
- **Run ID / attempt:** 45992769255 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 80819ac6f8d3640671dd3b550ac2008cf3a0acc5
- **Source task:** 20261127-173000-02
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 22907d4bfb9905ee155d0d16164982c96d415762
- **Linter source SHA:** 80819ac6f8d3640671dd3b550ac2008cf3a0acc5
- **Generated (UTC):** 2026-11-27T11:44:16.989293+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 13 |
| Files that failed | 7 |
| Files with findings | 11 |
| Total findings | 98 |
| Hard findings | 51 |
| Advisory findings | 47 |
| New findings | 97 |
| Recurring findings | 1 |
| Resolved findings | 9 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/INITIALIZATION_POLICY.md
- .agent/skills/the-worker/references/decision-governance.md
- .agent/skills/README.md
- .agent/SESSION_START.md
- .agent/skills/the-worker/SKILL.md
- .agent/skills/the-worker/references/document-type-catalog.md
- .agent/skills/the-worker/references/github-actions.md
- .agent/skills/agent-skill-authoring/SKILL.md
- workspace/task_board.md
- workspace/draft/README.md
- .agent/skills/the-worker/references/ci-ledger.md
- workspace/README.md
- .agent/skills/asd-ste100/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/INITIALIZATION_POLICY.md | PASS | 1 | 1 | 4 | 2027 | 0.0 | 0 |
| .agent/skills/the-worker/references/decision-governance.md | FAIL | 9 | 5 | 0 | 2988 | 0.3 | 1 |
| .agent/skills/README.md | PASS | 0 | 0 | 0 | 457 | 0.0 | 0 |
| .agent/SESSION_START.md | FAIL | 7 | 3 | 0 | 2927 | 0.2 | 1 |
| .agent/skills/the-worker/SKILL.md | FAIL | 25 | 18 | 0 | 2540 | 1.0 | 1 |
| .agent/skills/the-worker/references/document-type-catalog.md | FAIL | 8 | 4 | 0 | 4578 | 0.2 | 1 |
| .agent/skills/the-worker/references/github-actions.md | FAIL | 2 | 2 | 0 | 1852 | 0.1 | 1 |
| .agent/skills/agent-skill-authoring/SKILL.md | PASS | 15 | 0 | 6 | 2260 | 0.7 | 0 |
| workspace/task_board.md | PASS | 1 | 0 | 0 | 318 | 0.3 | 0 |
| workspace/draft/README.md | PASS | 0 | 0 | 0 | 669 | 0.0 | 0 |
| .agent/skills/the-worker/references/ci-ledger.md | FAIL | 4 | 2 | 0 | 704 | 0.6 | 1 |
| workspace/README.md | FAIL | 6 | 4 | 0 | 502 | 1.2 | 1 |
| .agent/skills/asd-ste100/SKILL.md | PASS | 20 | 12 | 31 | 2609 | 0.8 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 39 |
| semicolon | 16 |
| synonym-rotation | 15 |
| long-sentence | 8 |
| present-perfect | 8 |
| marketing-adjective | 5 |
| phrasal-verb | 5 |
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
Ran 6 tests in 0.440s

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
Scanned 13 changed Markdown sources (390 available as link targets) and 42 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/INITIALIZATION_POLICY.md:70:1 · **new** · fingerprint: 4e20a50af596bd1c8120efea
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** Retrieve
- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:78:206 · **new** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/references/decision-governance.md:97:283 · **new** · fingerprint: f0924ddd2b0dc8bbc49b968e
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · .agent/skills/the-worker/references/decision-governance.md:101:38 · **new** · fingerprint: def411a40f6be2c48a4cd3be
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:103:34 · **new** · fingerprint: c7517e9068fe8c09010e809b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:109:47 · **new** · fingerprint: 3cfa441ce1b36c919b05cc87
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated
- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:109:57 · **new** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:109:102 · **new** · fingerprint: a5f01370d23783e6b0e83a7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied
- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:111:86 · **new** · fingerprint: 24b3d9a71feccea3fb1206db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed
- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:125:65 · **new** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
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
- **passive-voice** · .agent/skills/the-worker/SKILL.md:36:83 · **new** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **long-sentence** · .agent/skills/the-worker/SKILL.md:45:165 · **new** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:45:319 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/SKILL.md:45:468 · **new** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:45:750 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:61:141 · **new** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/SKILL.md:67:10 · **new** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed
- **semicolon** · .agent/skills/the-worker/SKILL.md:72:41 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:73:29 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:74:16 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:85:91 · **new** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
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
- **semicolon** · .agent/skills/the-worker/SKILL.md:141:257 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:155:129 · **new** · fingerprint: 50c502e6476c7d33f9c052f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is activated
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:171:286 · **new** · fingerprint: f071e35d93664b24286e6bb7
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:172:302 · **new** · fingerprint: 5d8336dc915865ae43f6b3a8
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **passive-voice** · .agent/skills/the-worker/SKILL.md:174:100 · **new** · fingerprint: e5c16c0bb6df9d137ce2bf13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are exhausted
- **long-sentence** · .agent/skills/the-worker/SKILL.md:174:142 · **new** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:174:228 · **new** · fingerprint: 961e310a4d56d86392dd989d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were examined
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:43:131 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:44:275 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:131:297 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:145:143 · **new** · fingerprint: 3c37bdb100e76e92190f285d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed
- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:145:228 · **new** · fingerprint: 635c1984012e0d9f0ec925af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:213:89 · **new** · fingerprint: 6b4e11cdd83b54cefd8c9eb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:213:179 · **new** · fingerprint: 6b4e11cdd83b54cefd8c9eb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **synonym-rotation** · .agent/skills/the-worker/references/document-type-catalog.md:213:206 · **new** · fingerprint: 462e0ea3915e8d7012fd216c
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **synonym-rotation** · .agent/skills/the-worker/references/github-actions.md:34:96 · **new** · fingerprint: 87c805f0894d01b1d24ca3b6
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **long-sentence** · .agent/skills/the-worker/references/github-actions.md:45:3 · **new** · fingerprint: 933a579fb10c54b6f0b0201a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:14:79 · **new** · fingerprint: 02b57d3b2df16eb3468595dc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:159:29 · **new** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:166:23 · **new** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:172:149 · **new** · fingerprint: ba8e0ed371140388669d2100
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:172:153 · **new** · fingerprint: 1b62b1b2e8581f74a08af948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:185:36 · **new** · fingerprint: 97f02ce3bcf5b6ef7653d521
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:223:38 · **new** · fingerprint: 6791e38cdf43e2f4c45df46b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:245:28 · **new** · fingerprint: eb4ac5866a5a9ae0a950a472
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:246:65 · **new** · fingerprint: 301135338f19f01e083e45ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:246:70 · **new** · fingerprint: e6c88a755850e4cbcab58fa8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:253:17 · **new** · fingerprint: bbeb4b1299f984862be3ce2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:255:37 · **new** · fingerprint: 6d4fd87d7c04e6106995412e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been made
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:255:41 · **new** · fingerprint: 5b69fb1b48037b85a2f02a19
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been made
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:257:32 · **new** · fingerprint: 19df0784fbab3f590bc978f2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:257:36 · **new** · fingerprint: 9124dbf071fc471856835398
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:35:132 · **new** · fingerprint: 20a3b946ee1ae4877e53e449
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:35:209 · **new** · fingerprint: a913a887a540db8f083a49d4
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes
- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:37:154 · **new** · fingerprint: b57ced8a931e2c7579ee7ae3
  - **Level:** advisory-free
  - **Message:** 'alter' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:48:137 · **new** · fingerprint: 02e6a360a86d394444d7be9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned
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
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:58:99 · **new** · fingerprint: 70281f9b33028652f7a1daae
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** Spin up
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
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:29 · **new** · fingerprint: d272642fbbf9daaca0e0f89b
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** spin up
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:38 · **new** · fingerprint: 0069ef4a67380240203a7d96
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** reach out
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:49 · **new** · fingerprint: a00e46d5c1d01ed73aeb5e48
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** dive into
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:60 · **new** · fingerprint: 186eeebc10bfa90b61b9f168
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** kick off
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:113:134 · **new** · fingerprint: 361fe239198e1c7837a878ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:146:58 · **new** · fingerprint: 9efba8ed23b805f9a79bdc62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized

### Recurring findings

- **passive-voice** · workspace/task_board.md:42:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred

### Resolved findings

- **synonym-rotation** · workspace/task_board.md:44:24 · **resolved** · fingerprint: f3da998ac0ab93f31587c635
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:34:64 · **resolved** · fingerprint: fbe6150d9b5e8dab3b1e43a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:47:41 · **resolved** · fingerprint: 8d3ad3a1e3838d879ee9b85a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:111:44 · **resolved** · fingerprint: e871aaaf906a610ac0db5605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are implemented
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:150:86 · **resolved** · fingerprint: e56053c3ddae76d3a0704b63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was retired
- **semicolon** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:152:54 · **resolved** · fingerprint: 9a23cba48e9d5ffca1df4cc7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:160:67 · **resolved** · fingerprint: 2eafa78f211213b12b14d4d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **semicolon** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:163:53 · **resolved** · fingerprint: 9a23cba48e9d5ffca1df4cc7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:163:93 · **resolved** · fingerprint: cb29534f35d8d330ae1e06be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/INITIALIZATION_POLICY.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 4
- **Words:** 2027
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **synonym-rotation** · .agent/INITIALIZATION_POLICY.md:70:1 · **new** · fingerprint: 4e20a50af596bd1c8120efea
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** Retrieve


### .agent/skills/the-worker/references/decision-governance.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 2988
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:78:206 · **new** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/references/decision-governance.md:97:283 · **new** · fingerprint: f0924ddd2b0dc8bbc49b968e
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · .agent/skills/the-worker/references/decision-governance.md:101:38 · **new** · fingerprint: def411a40f6be2c48a4cd3be
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:103:34 · **new** · fingerprint: c7517e9068fe8c09010e809b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included

- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:109:47 · **new** · fingerprint: 3cfa441ce1b36c919b05cc87
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated

- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:109:57 · **new** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:109:102 · **new** · fingerprint: a5f01370d23783e6b0e83a7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied

- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:111:86 · **new** · fingerprint: 24b3d9a71feccea3fb1206db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed

- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:125:65 · **new** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 457
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 7
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 2927
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
- **Findings:** 25
- **Hard findings:** 18
- **Baseline:** 0
- **Words:** 2540
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:36:83 · **new** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **long-sentence** · .agent/skills/the-worker/SKILL.md:45:165 · **new** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · .agent/skills/the-worker/SKILL.md:45:319 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/SKILL.md:45:468 · **new** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **semicolon** · .agent/skills/the-worker/SKILL.md:45:750 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:61:141 · **new** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · .agent/skills/the-worker/SKILL.md:67:10 · **new** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed

- **semicolon** · .agent/skills/the-worker/SKILL.md:72:41 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:73:29 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:74:16 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:85:91 · **new** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

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

- **semicolon** · .agent/skills/the-worker/SKILL.md:141:257 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:155:129 · **new** · fingerprint: 50c502e6476c7d33f9c052f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is activated

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:171:286 · **new** · fingerprint: f071e35d93664b24286e6bb7
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:172:302 · **new** · fingerprint: 5d8336dc915865ae43f6b3a8
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch

- **passive-voice** · .agent/skills/the-worker/SKILL.md:174:100 · **new** · fingerprint: e5c16c0bb6df9d137ce2bf13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are exhausted

- **long-sentence** · .agent/skills/the-worker/SKILL.md:174:142 · **new** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:174:228 · **new** · fingerprint: 961e310a4d56d86392dd989d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were examined


### .agent/skills/the-worker/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 4578
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:43:131 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:44:275 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:131:297 · **new** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:145:143 · **new** · fingerprint: 3c37bdb100e76e92190f285d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed

- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:145:228 · **new** · fingerprint: 635c1984012e0d9f0ec925af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted

- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:213:89 · **new** · fingerprint: 6b4e11cdd83b54cefd8c9eb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted

- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:213:179 · **new** · fingerprint: 6b4e11cdd83b54cefd8c9eb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted

- **synonym-rotation** · .agent/skills/the-worker/references/document-type-catalog.md:213:206 · **new** · fingerprint: 462e0ea3915e8d7012fd216c
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks


### .agent/skills/the-worker/references/github-actions.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1852
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/the-worker/references/github-actions.md:34:96 · **new** · fingerprint: 87c805f0894d01b1d24ca3b6
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **long-sentence** · .agent/skills/the-worker/references/github-actions.md:45:3 · **new** · fingerprint: 933a579fb10c54b6f0b0201a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words


### .agent/skills/agent-skill-authoring/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 15
- **Hard findings:** 0
- **Baseline:** 6
- **Words:** 2260
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:14:79 · **new** · fingerprint: 02b57d3b2df16eb3468595dc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:159:29 · **new** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:166:23 · **new** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:172:149 · **new** · fingerprint: ba8e0ed371140388669d2100
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been loaded

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:172:153 · **new** · fingerprint: 1b62b1b2e8581f74a08af948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:185:36 · **new** · fingerprint: 97f02ce3bcf5b6ef7653d521
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:223:38 · **new** · fingerprint: 6791e38cdf43e2f4c45df46b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:245:28 · **new** · fingerprint: eb4ac5866a5a9ae0a950a472
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused

- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:246:65 · **new** · fingerprint: 301135338f19f01e083e45ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:246:70 · **new** · fingerprint: e6c88a755850e4cbcab58fa8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:253:17 · **new** · fingerprint: bbeb4b1299f984862be3ce2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected

- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:255:37 · **new** · fingerprint: 6d4fd87d7c04e6106995412e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been made

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:255:41 · **new** · fingerprint: 5b69fb1b48037b85a2f02a19
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been made

- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:257:32 · **new** · fingerprint: 19df0784fbab3f590bc978f2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read

- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:257:36 · **new** · fingerprint: 9124dbf071fc471856835398
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 318
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:42:113 · **recurring** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred


### workspace/draft/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 669
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### .agent/skills/the-worker/references/ci-ledger.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 704
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:35:132 · **new** · fingerprint: 20a3b946ee1ae4877e53e449
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:35:209 · **new** · fingerprint: a913a887a540db8f083a49d4
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes

- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:37:154 · **new** · fingerprint: b57ced8a931e2c7579ee7ae3
  - **Level:** advisory-free
  - **Message:** 'alter' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** alter

- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:48:137 · **new** · fingerprint: 02e6a360a86d394444d7be9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 502
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


### .agent/skills/asd-ste100/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 20
- **Hard findings:** 12
- **Baseline:** 31
- **Words:** 2609
- **Findings per 100 words:** 0.8

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

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:58:99 · **new** · fingerprint: 70281f9b33028652f7a1daae
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** Spin up

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

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:29 · **new** · fingerprint: d272642fbbf9daaca0e0f89b
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** spin up

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:38 · **new** · fingerprint: 0069ef4a67380240203a7d96
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** reach out

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:49 · **new** · fingerprint: a00e46d5c1d01ed73aeb5e48
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** dive into

- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:60 · **new** · fingerprint: 186eeebc10bfa90b61b9f168
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** kick off

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
