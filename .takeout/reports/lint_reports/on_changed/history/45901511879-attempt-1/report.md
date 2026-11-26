# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#821](https://github.com/dungnv2602/chatgpt/actions/runs/45901511879)
- **Run ID / attempt:** 45901511879 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / b68ab7a239b5dc17e67b9c005b4541dc998caf2b
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 2a18f0c9576131ffaa126d405433cf6dc31b1ded
- **Linter source SHA:** b68ab7a239b5dc17e67b9c005b4541dc998caf2b
- **Generated (UTC):** 2026-11-26T21:57:16.383099+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 45 |
| Hard findings | 21 |
| Advisory findings | 24 |
| New findings | 0 |
| Recurring findings | 45 |
| Resolved findings | 1 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md
- workspace/task_board.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | FAIL | 45 | 21 | 0 | 3478 | 1.3 | 1 |
| workspace/task_board.md | PASS | 0 | 0 | 0 | 378 | 0.0 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 24 |
| semicolon | 17 |
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
....
----------------------------------------------------------------------
Ran 4 tests in 0.217s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.006s

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
Scanned 2 changed Markdown sources (328 available as link targets) and 16 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:66:61 · **recurring** · fingerprint: 3d753fd2c4828ff430fdb6c2
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:74:38 · **recurring** · fingerprint: 0642057a58aa1965274b9762
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:104 · **recurring** · fingerprint: f331458e480ad4445c592130
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:100:85 · **recurring** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:67 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:157 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:254 · **recurring** · fingerprint: c165f6e8824400b2723a92ab
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is controlled
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:106:205 · **recurring** · fingerprint: 0ee5ca333d00a4f63756c25b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is generated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:107:185 · **recurring** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:119:123 · **recurring** · fingerprint: 3a2d463bad961d4a2f26d082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was evaluated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:103 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:191 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:46 · **recurring** · fingerprint: 421ce0d953be11182d9e810a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stored
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:115 · **recurring** · fingerprint: 6937ea80a6afca82e7f414d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:133:54 · **recurring** · fingerprint: 2e0dfecf96eeb4735f44ac24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:143:183 · **recurring** · fingerprint: f8411801c3d8953cd8c2acbe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is identified
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:149:70 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:150:203 · **recurring** · fingerprint: a0bfc1f95f604fc3f864783e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is performed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:149 · **recurring** · fingerprint: 0da19e7aab04deb7911a62a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are unchanged
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:213 · **recurring** · fingerprint: fa6c012aa723a1be302eb24c
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:347 · **recurring** · fingerprint: 4d9fcdb8f2b29ee7904ba6a4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were copied
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:157:125 · **recurring** · fingerprint: 87a065e710f1792ecf1034fc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is migrated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:158:130 · **recurring** · fingerprint: 051c97c1441fc96df828d5f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:159:295 · **recurring** · fingerprint: 6f3d1a1473ce547dba606827
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was used
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:178:70 · **recurring** · fingerprint: 494f747b32f0b27099114e91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are filtered
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:192:43 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:200:137 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:263 · **recurring** · fingerprint: ca82b6e19a6f4ef4347ae654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:293 · **recurring** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:216:263 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:139 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:162 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:188 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:219 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:222:62 · **recurring** · fingerprint: 6b4576cd5b0f0b9ac4699130
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was deleted
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:89 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:134 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:186 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:246 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:290 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:335 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:77 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:119 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:177 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:233:49 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Resolved findings

- **long-sentence** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:190:3 · **resolved** · fingerprint: 0dc1b5fa54679407d060b44e
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 45
- **Hard findings:** 21
- **Baseline:** 0
- **Words:** 3478
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:66:61 · **recurring** · fingerprint: 3d753fd2c4828ff430fdb6c2
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:74:38 · **recurring** · fingerprint: 0642057a58aa1965274b9762
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:104 · **recurring** · fingerprint: f331458e480ad4445c592130
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:100:85 · **recurring** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:67 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:157 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:254 · **recurring** · fingerprint: c165f6e8824400b2723a92ab
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is controlled

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:106:205 · **recurring** · fingerprint: 0ee5ca333d00a4f63756c25b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is generated

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:107:185 · **recurring** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:119:123 · **recurring** · fingerprint: 3a2d463bad961d4a2f26d082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was evaluated

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:103 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:191 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:46 · **recurring** · fingerprint: 421ce0d953be11182d9e810a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stored

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:115 · **recurring** · fingerprint: 6937ea80a6afca82e7f414d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:133:54 · **recurring** · fingerprint: 2e0dfecf96eeb4735f44ac24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:143:183 · **recurring** · fingerprint: f8411801c3d8953cd8c2acbe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is identified

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:149:70 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:150:203 · **recurring** · fingerprint: a0bfc1f95f604fc3f864783e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is performed

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:149 · **recurring** · fingerprint: 0da19e7aab04deb7911a62a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are unchanged

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:213 · **recurring** · fingerprint: fa6c012aa723a1be302eb24c
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validates

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:347 · **recurring** · fingerprint: 4d9fcdb8f2b29ee7904ba6a4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were copied

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:157:125 · **recurring** · fingerprint: 87a065e710f1792ecf1034fc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is migrated

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:158:130 · **recurring** · fingerprint: 051c97c1441fc96df828d5f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:159:295 · **recurring** · fingerprint: 6f3d1a1473ce547dba606827
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was used

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:178:70 · **recurring** · fingerprint: 494f747b32f0b27099114e91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are filtered

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:192:43 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:200:137 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:263 · **recurring** · fingerprint: ca82b6e19a6f4ef4347ae654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:293 · **recurring** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:216:263 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:139 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:162 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:188 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:218:219 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:222:62 · **recurring** · fingerprint: 6b4576cd5b0f0b9ac4699130
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was deleted

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:89 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:134 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:186 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:246 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:290 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:225:335 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:77 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:119 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:226:177 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:233:49 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 378
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
