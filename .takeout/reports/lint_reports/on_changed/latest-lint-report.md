# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#822](https://github.com/dungnv2602/chatgpt/actions/runs/45901977965)
- **Run ID / attempt:** 45901977965 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / c22f51846d9bf5dca2dc22ce8cb36934bf56bdc9
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** b68ab7a239b5dc17e67b9c005b4541dc998caf2b
- **Linter source SHA:** c22f51846d9bf5dca2dc22ce8cb36934bf56bdc9
- **Generated (UTC):** 2026-11-26T22:01:28.129182+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 22 |
| Hard findings | 7 |
| Advisory findings | 15 |
| New findings | 5 |
| Recurring findings | 17 |
| Resolved findings | 10 |
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
| workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md | FAIL | 21 | 6 | 0 | 3456 | 0.6 | 1 |
| workspace/task_board.md | FAIL | 1 | 1 | 0 | 439 | 0.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 15 |
| synonym-rotation | 5 |
| long-sentence | 1 |
| semicolon | 1 |

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
Ran 4 tests in 0.358s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.007s

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
Scanned 2 changed Markdown sources (329 available as link targets) and 16 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:66:50 · **new** · fingerprint: 3f34a81299a3d18ae26e4279
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:102 · **new** · fingerprint: c71ff84334a10d7dd38255c9
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:260 · **new** · fingerprint: d2ff8094ef84d15b57e688d1
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:204:15 · **new** · fingerprint: a5b303c3291ad245c6135b6c
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** deletes
- **long-sentence** · workspace/task_board.md:21:1 · **new** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

### Recurring findings

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:74:38 · **recurring** · fingerprint: 0642057a58aa1965274b9762
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:106:202 · **recurring** · fingerprint: 0ee5ca333d00a4f63756c25b
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
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:149:70 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:157:125 · **recurring** · fingerprint: 87a065e710f1792ecf1034fc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is migrated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:159:295 · **recurring** · fingerprint: 6f3d1a1473ce547dba606827
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was used
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:178:70 · **recurring** · fingerprint: 494f747b32f0b27099114e91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are filtered
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:193:259 · **recurring** · fingerprint: f331458e480ad4445c592130
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:263 · **recurring** · fingerprint: ca82b6e19a6f4ef4347ae654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:216:260 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:233:49 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Resolved findings

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:66:61 · **resolved** · fingerprint: 3d753fd2c4828ff430fdb6c2
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:100:85 · **resolved** · fingerprint: 869c8495109dea6f34af871c
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:105:254 · **resolved** · fingerprint: c165f6e8824400b2723a92ab
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is controlled
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:143:183 · **resolved** · fingerprint: f8411801c3d8953cd8c2acbe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is identified
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:150:203 · **resolved** · fingerprint: a0bfc1f95f604fc3f864783e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is performed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:149 · **resolved** · fingerprint: 0da19e7aab04deb7911a62a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are unchanged
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:213 · **resolved** · fingerprint: fa6c012aa723a1be302eb24c
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:347 · **resolved** · fingerprint: 4d9fcdb8f2b29ee7904ba6a4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were copied
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:158:130 · **resolved** · fingerprint: 051c97c1441fc96df828d5f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:222:62 · **resolved** · fingerprint: 6b4576cd5b0f0b9ac4699130
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was deleted

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 21
- **Hard findings:** 6
- **Baseline:** 0
- **Words:** 3456
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:66:50 · **new** · fingerprint: 3f34a81299a3d18ae26e4279
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:74:38 · **recurring** · fingerprint: 0642057a58aa1965274b9762
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:102 · **new** · fingerprint: c71ff84334a10d7dd38255c9
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:106:202 · **recurring** · fingerprint: 0ee5ca333d00a4f63756c25b
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

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:149:70 · **recurring** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:260 · **new** · fingerprint: d2ff8094ef84d15b57e688d1
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:157:125 · **recurring** · fingerprint: 87a065e710f1792ecf1034fc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is migrated

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:159:295 · **recurring** · fingerprint: 6f3d1a1473ce547dba606827
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was used

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:178:70 · **recurring** · fingerprint: 494f747b32f0b27099114e91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are filtered

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:193:259 · **recurring** · fingerprint: f331458e480ad4445c592130
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:204:15 · **new** · fingerprint: a5b303c3291ad245c6135b6c
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** deletes

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:263 · **recurring** · fingerprint: ca82b6e19a6f4ef4347ae654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected

- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:216:260 · **recurring** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested

- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:233:49 · **recurring** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 439
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **long-sentence** · workspace/task_board.md:21:1 · **new** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
