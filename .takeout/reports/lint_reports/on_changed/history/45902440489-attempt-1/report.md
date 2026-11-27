# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#823](https://github.com/dungnv2602/chatgpt/actions/runs/45902440489)
- **Run ID / attempt:** 45902440489 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 18544ec38967abe06c7276816ef67d04e75add09
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** c22f51846d9bf5dca2dc22ce8cb36934bf56bdc9
- **Linter source SHA:** 18544ec38967abe06c7276816ef67d04e75add09
- **Generated (UTC):** 2026-11-26T22:05:40.937907+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 2 |
| Hard findings | 1 |
| Advisory findings | 1 |
| New findings | 2 |
| Recurring findings | 0 |
| Resolved findings | 22 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/SKILL.md | FAIL | 2 | 1 | 0 | 5619 | 0.0 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| long-sentence | 1 |
| passive-voice | 1 |

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
Ran 4 tests in 0.215s

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
Scanned 1 changed Markdown sources (330 available as link targets) and 3 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:270:144 · **new** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:273:3 · **new** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words

### Recurring findings

None.

### Resolved findings

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:66:50 · **resolved** · fingerprint: 3f34a81299a3d18ae26e4279
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:74:38 · **resolved** · fingerprint: 0642057a58aa1965274b9762
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:102 · **resolved** · fingerprint: c71ff84334a10d7dd38255c9
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:106:202 · **resolved** · fingerprint: 0ee5ca333d00a4f63756c25b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is generated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:107:185 · **resolved** · fingerprint: 96c00d0b1528652722c7e2e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was measured
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:119:123 · **resolved** · fingerprint: 3a2d463bad961d4a2f26d082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was evaluated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:103 · **resolved** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:129:191 · **resolved** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:46 · **resolved** · fingerprint: 421ce0d953be11182d9e810a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stored
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:131:115 · **resolved** · fingerprint: 6937ea80a6afca82e7f414d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is rendered
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:133:54 · **resolved** · fingerprint: 2e0dfecf96eeb4735f44ac24
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:149:70 · **resolved** · fingerprint: 6a75e8e708a43c0d36cdde23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:154:260 · **resolved** · fingerprint: d2ff8094ef84d15b57e688d1
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:157:125 · **resolved** · fingerprint: 87a065e710f1792ecf1034fc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is migrated
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:159:295 · **resolved** · fingerprint: 6f3d1a1473ce547dba606827
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was used
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:178:70 · **resolved** · fingerprint: 494f747b32f0b27099114e91
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are filtered
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:193:259 · **resolved** · fingerprint: f331458e480ad4445c592130
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:204:15 · **resolved** · fingerprint: a5b303c3291ad245c6135b6c
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** deletes
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:214:263 · **resolved** · fingerprint: ca82b6e19a6f4ef4347ae654
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:216:260 · **resolved** · fingerprint: 6d4df52d9a6f40d7fd4657d2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **semicolon** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:233:49 · **resolved** · fingerprint: 0d416a176834b9a3c1481769
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/task_board.md:21:1 · **resolved** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 5619
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:270:144 · **new** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized

- **long-sentence** · .agent/skills/the-worker/SKILL.md:273:3 · **new** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
