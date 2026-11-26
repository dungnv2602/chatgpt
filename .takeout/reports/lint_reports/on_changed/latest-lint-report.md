# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#830](https://github.com/dungnv2602/chatgpt/actions/runs/45903483133)
- **Run ID / attempt:** 45903483133 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / e5138cc21dbadb28fb9c38bb0985436a763633aa
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 881a990d09a455534a392dfcaa5b2449baac3c22
- **Linter source SHA:** e5138cc21dbadb28fb9c38bb0985436a763633aa
- **Generated (UTC):** 2026-11-26T22:15:06.363498+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 9 |
| Hard findings | 5 |
| Advisory findings | 4 |
| New findings | 9 |
| Recurring findings | 0 |
| Resolved findings | 4 |
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
| .agent/skills/the-worker/SKILL.md | FAIL | 9 | 5 | 0 | 5927 | 0.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 4 |
| long-sentence | 2 |
| synonym-rotation | 2 |
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
Ran 4 tests in 0.336s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.005s

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
Scanned 1 changed Markdown sources (333 available as link targets) and 3 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:84 · **new** · fingerprint: e1589b5207c7991dd0eac000
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are identified
- **passive-voice** · .agent/skills/the-worker/SKILL.md:44:60 · **new** · fingerprint: 5524d0b44a548a67e3636a68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:45:28 · **new** · fingerprint: b1e35b2851bbde31553d9cfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are validated
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:45:32 · **new** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **semicolon** · .agent/skills/the-worker/SKILL.md:45:173 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:69:51 · **new** · fingerprint: 15a39e78d06fa29daf65aba3
  - **Level:** advisory-free
  - **Message:** 'start' and 'initiate' name the same action. Pick one and use it every time.
  - **Matched text:** start
- **passive-voice** · .agent/skills/the-worker/SKILL.md:280:144 · **new** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:282:124 · **new** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:285:3 · **new** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words

### Recurring findings

None.

### Resolved findings

- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:90:102 · **resolved** · fingerprint: e65e3922aa38293af2adc5e0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** Delete
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:92:104 · **resolved** · fingerprint: c71ff84334a10d7dd38255c9
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:158:108 · **resolved** · fingerprint: 3f34a81299a3d18ae26e4279
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **synonym-rotation** · workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md:159:149 · **resolved** · fingerprint: 563af8dd74cf1ba4bd074708
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 5927
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:84 · **new** · fingerprint: e1589b5207c7991dd0eac000
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are identified

- **passive-voice** · .agent/skills/the-worker/SKILL.md:44:60 · **new** · fingerprint: 5524d0b44a548a67e3636a68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:45:28 · **new** · fingerprint: b1e35b2851bbde31553d9cfc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are validated

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:45:32 · **new** · fingerprint: d04c76628166e8796dcfc446
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **semicolon** · .agent/skills/the-worker/SKILL.md:45:173 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:69:51 · **new** · fingerprint: 15a39e78d06fa29daf65aba3
  - **Level:** advisory-free
  - **Message:** 'start' and 'initiate' name the same action. Pick one and use it every time.
  - **Matched text:** start

- **passive-voice** · .agent/skills/the-worker/SKILL.md:280:144 · **new** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized

- **long-sentence** · .agent/skills/the-worker/SKILL.md:282:124 · **new** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **long-sentence** · .agent/skills/the-worker/SKILL.md:285:3 · **new** · fingerprint: bca5f43ed3545a47de04d134
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
