# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.2.0
- **Run:** [#993](https://github.com/dungnv2602/chatgpt/actions/runs/45992981903)
- **Run ID / attempt:** 45992981903 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 8a00ccfe91f0acfea20bb03a0a01d7203ac3836a
- **Source task:** 20261127-173000-02
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 80819ac6f8d3640671dd3b550ac2008cf3a0acc5
- **Linter source SHA:** 8a00ccfe91f0acfea20bb03a0a01d7203ac3836a
- **Generated (UTC):** 2026-11-27T11:46:56.381356+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 4 |
| Hard findings | 2 |
| Advisory findings | 2 |
| New findings | 0 |
| Recurring findings | 4 |
| Resolved findings | 94 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/references/ci-ledger.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/references/ci-ledger.md | FAIL | 4 | 2 | 0 | 704 | 0.6 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 2 |
| synonym-rotation | 2 |

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
Ran 6 tests in 0.399s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
........
----------------------------------------------------------------------
Ran 8 tests in 0.007s

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
Scanned 1 changed Markdown sources (421 available as link targets) and 0 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:35:132 · **recurring** · fingerprint: 20a3b946ee1ae4877e53e449
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:35:209 · **recurring** · fingerprint: a913a887a540db8f083a49d4
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes
- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:37:154 · **recurring** · fingerprint: b57ced8a931e2c7579ee7ae3
  - **Level:** advisory-free
  - **Message:** 'alter' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:48:137 · **recurring** · fingerprint: 02e6a360a86d394444d7be9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unassigned

### Resolved findings

- **synonym-rotation** · .agent/INITIALIZATION_POLICY.md:70:1 · **resolved** · fingerprint: 4e20a50af596bd1c8120efea
  - **Level:** advisory-free
  - **Message:** 'retrieve' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** Retrieve
- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:78:206 · **resolved** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/references/decision-governance.md:97:283 · **resolved** · fingerprint: f0924ddd2b0dc8bbc49b968e
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · .agent/skills/the-worker/references/decision-governance.md:101:38 · **resolved** · fingerprint: def411a40f6be2c48a4cd3be
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:103:34 · **resolved** · fingerprint: c7517e9068fe8c09010e809b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:109:47 · **resolved** · fingerprint: 3cfa441ce1b36c919b05cc87
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated
- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:109:57 · **resolved** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:109:102 · **resolved** · fingerprint: a5f01370d23783e6b0e83a7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied
- **passive-voice** · .agent/skills/the-worker/references/decision-governance.md:111:86 · **resolved** · fingerprint: 24b3d9a71feccea3fb1206db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed
- **semicolon** · .agent/skills/the-worker/references/decision-governance.md:125:65 · **resolved** · fingerprint: b705ef6f747ccfaf4dd42d95
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/SESSION_START.md:41:99 · **resolved** · fingerprint: b364e80e8c98116d3ebcfb38
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **synonym-rotation** · .agent/SESSION_START.md:52:31 · **resolved** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/SESSION_START.md:92:161 · **resolved** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:93:63 · **resolved** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · .agent/SESSION_START.md:237:167 · **resolved** · fingerprint: 6df4df8dd70ff7a6b7fcd357
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
- **passive-voice** · .agent/skills/the-worker/SKILL.md:36:83 · **resolved** · fingerprint: 7b14acb1f2bd5527bba85225
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **long-sentence** · .agent/skills/the-worker/SKILL.md:45:165 · **resolved** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:45:319 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/SKILL.md:45:468 · **resolved** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **semicolon** · .agent/skills/the-worker/SKILL.md:45:750 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:61:141 · **resolved** · fingerprint: 41c8fb47b6b000b0b2e47dfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · .agent/skills/the-worker/SKILL.md:67:10 · **resolved** · fingerprint: 0ccd1f7c4af982aef5659c2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Proposed
- **semicolon** · .agent/skills/the-worker/SKILL.md:72:41 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:73:29 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:74:16 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:85:91 · **resolved** · fingerprint: 0aaa53d17394c2697ff91643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **long-sentence** · .agent/skills/the-worker/SKILL.md:112:3 · **resolved** · fingerprint: 29bf7cd1e44f6d01fc347374
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:116:70 · **resolved** · fingerprint: 030301d369a6833422178b29
  - **Level:** advisory-free
  - **Message:** Sentence has 42 words (cap 25). Split it.
  - **Matched text:** 42 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:116:330 · **resolved** · fingerprint: e749a89a221be9cabe94904f
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:124:139 · **resolved** · fingerprint: 90e6b7d1bbc5bc36ea42d40b
  - **Level:** advisory-free
  - **Message:** 'modify' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** modifying
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:124:169 · **resolved** · fingerprint: 9a91179e5c545e21411d154c
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begin
- **long-sentence** · .agent/skills/the-worker/SKILL.md:125:182 · **resolved** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:125:201 · **resolved** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **semicolon** · .agent/skills/the-worker/SKILL.md:141:257 · **resolved** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:155:129 · **resolved** · fingerprint: 50c502e6476c7d33f9c052f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is activated
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:171:286 · **resolved** · fingerprint: f071e35d93664b24286e6bb7
  - **Level:** advisory-free
  - **Message:** 'repair' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:172:302 · **resolved** · fingerprint: 5d8336dc915865ae43f6b3a8
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **passive-voice** · .agent/skills/the-worker/SKILL.md:174:100 · **resolved** · fingerprint: e5c16c0bb6df9d137ce2bf13
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are exhausted
- **long-sentence** · .agent/skills/the-worker/SKILL.md:174:142 · **resolved** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:174:228 · **resolved** · fingerprint: 961e310a4d56d86392dd989d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were examined
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:43:131 · **resolved** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:44:275 · **resolved** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/references/document-type-catalog.md:131:297 · **resolved** · fingerprint: e7ff64fedb3eddf5ee3c1564
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:145:143 · **resolved** · fingerprint: 3c37bdb100e76e92190f285d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed
- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:145:228 · **resolved** · fingerprint: 635c1984012e0d9f0ec925af
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:213:89 · **resolved** · fingerprint: 6b4e11cdd83b54cefd8c9eb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · .agent/skills/the-worker/references/document-type-catalog.md:213:179 · **resolved** · fingerprint: 6b4e11cdd83b54cefd8c9eb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **synonym-rotation** · .agent/skills/the-worker/references/document-type-catalog.md:213:206 · **resolved** · fingerprint: 462e0ea3915e8d7012fd216c
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **synonym-rotation** · .agent/skills/the-worker/references/github-actions.md:34:96 · **resolved** · fingerprint: 87c805f0894d01b1d24ca3b6
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **long-sentence** · .agent/skills/the-worker/references/github-actions.md:45:3 · **resolved** · fingerprint: 933a579fb10c54b6f0b0201a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:14:79 · **resolved** · fingerprint: 02b57d3b2df16eb3468595dc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:159:29 · **resolved** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:166:23 · **resolved** · fingerprint: f2222fc7270c8971f6aea92a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:172:149 · **resolved** · fingerprint: ba8e0ed371140388669d2100
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:172:153 · **resolved** · fingerprint: 1b62b1b2e8581f74a08af948
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:185:36 · **resolved** · fingerprint: 97f02ce3bcf5b6ef7653d521
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:223:38 · **resolved** · fingerprint: 6791e38cdf43e2f4c45df46b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:245:28 · **resolved** · fingerprint: eb4ac5866a5a9ae0a950a472
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:246:65 · **resolved** · fingerprint: 301135338f19f01e083e45ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:246:70 · **resolved** · fingerprint: e6c88a755850e4cbcab58fa8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:253:17 · **resolved** · fingerprint: bbeb4b1299f984862be3ce2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:255:37 · **resolved** · fingerprint: 6d4fd87d7c04e6106995412e
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been made
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:255:41 · **resolved** · fingerprint: 5b69fb1b48037b85a2f02a19
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been made
- **present-perfect** · .agent/skills/agent-skill-authoring/SKILL.md:257:32 · **resolved** · fingerprint: 19df0784fbab3f590bc978f2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · .agent/skills/agent-skill-authoring/SKILL.md:257:36 · **resolved** · fingerprint: 9124dbf071fc471856835398
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · workspace/task_board.md:42:113 · **resolved** · fingerprint: 9db0ccdc5f344a34e6b09777
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deferred
- **semicolon** · workspace/README.md:14:41 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:23:210 · **resolved** · fingerprint: 66ac36e2cdb3db3683c0c8f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · workspace/README.md:24:104 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/README.md:33:224 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/README.md:43:209 · **resolved** · fingerprint: bdeb2ff1622490b994e19f76
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **semicolon** · workspace/README.md:43:220 · **resolved** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:21:69 · **resolved** · fingerprint: 170e10c67c5ddb4ac54ea4b2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was violated
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:49:227 · **resolved** · fingerprint: cb0ac7a2c5dda8b0dbd1051d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are defined
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:57:60 · **resolved** · fingerprint: 8a011f6518e4f647accaa107
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:58:99 · **resolved** · fingerprint: 70281f9b33028652f7a1daae
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** Spin up
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:73:118 · **resolved** · fingerprint: 28ef39a3cb8b2ca848f4ec97
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **nominalization** · .agent/skills/asd-ste100/SKILL.md:74:53 · **resolved** · fingerprint: 7e86fc5d602e4865ed4a0ff6
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:79:203 · **resolved** · fingerprint: 7a15da17f8212acf9cbcd80a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:81:140 · **resolved** · fingerprint: 320768d857c6a3e84654f3f5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed
- **nominalization** · .agent/skills/asd-ste100/SKILL.md:89:56 · **resolved** · fingerprint: fa833ca0d8a25be575faf6e0
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:79 · **resolved** · fingerprint: 12a9fb2640f958cc7e75f621
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:89 · **resolved** · fingerprint: c50be8a609eda6ecc738029b
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:107 · **resolved** · fingerprint: d7e2c69987f9328ac247ac53
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:121 · **resolved** · fingerprint: 0d5ed7f9257c40733f5c321d
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless
- **marketing-adjective** · .agent/skills/asd-ste100/SKILL.md:90:133 · **resolved** · fingerprint: 2673e9a5ae5dd03778f880c9
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:29 · **resolved** · fingerprint: d272642fbbf9daaca0e0f89b
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** spin up
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:38 · **resolved** · fingerprint: 0069ef4a67380240203a7d96
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** reach out
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:49 · **resolved** · fingerprint: a00e46d5c1d01ed73aeb5e48
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** dive into
- **phrasal-verb** · .agent/skills/asd-ste100/SKILL.md:92:60 · **resolved** · fingerprint: 186eeebc10bfa90b61b9f168
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** kick off
- **present-perfect** · .agent/skills/asd-ste100/SKILL.md:113:134 · **resolved** · fingerprint: 361fe239198e1c7837a878ba
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **passive-voice** · .agent/skills/asd-ste100/SKILL.md:146:58 · **resolved** · fingerprint: 9efba8ed23b805f9a79bdc62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/references/ci-ledger.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 704
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:35:132 · **recurring** · fingerprint: 20a3b946ee1ae4877e53e449
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:35:209 · **recurring** · fingerprint: a913a887a540db8f083a49d4
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changes

- **synonym-rotation** · .agent/skills/the-worker/references/ci-ledger.md:37:154 · **recurring** · fingerprint: b57ced8a931e2c7579ee7ae3
  - **Level:** advisory-free
  - **Message:** 'alter' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** alter

- **passive-voice** · .agent/skills/the-worker/references/ci-ledger.md:48:137 · **recurring** · fingerprint: 02e6a360a86d394444d7be9c
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
