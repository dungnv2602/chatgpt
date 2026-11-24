# Drawing Pattern Entry Templates

**Template version:** 1.1

Use this note when adding or revising entries in the global drawing pattern indexes:

- `successful-patterns.md` — reusable techniques supported by observed results.
- `failure-patterns.md` — recurring failures, investigated causes, and tested countermeasures.

These are copy-ready templates, not pattern records. Do not place illustrative or unverified examples in the global indexes.

## Shared conventions

- Assign each approved entry a permanent, unique ID.
- Do not assign a new ID or change an index until the user approves the exact proposal.
- Record the date and scope of the user's approval in each new or revised entry.
- For an existing entry, preserve its ID and update only the fields the user approved.
- Use `S-001`, `S-002`, and similar IDs for successful patterns.
- Use `F-001`, `F-002`, and similar IDs for failure patterns.
- Do not reuse an ID, even if an entry is retired.
- Link evidence to the relevant daily attempt record. Include a direct image link only when the image's provenance and path are verified.
- Describe observed results separately from interpretations or hypotheses.
- Keep entries generalizable. Individual attempt details belong in the daily archive.
- Use one confidence field with one of these values:
  - **Provisional** — one meaningful observation. Further testing is needed.
  - **Supported** — repeated evidence in comparable situations.
  - **Validated** — repeated evidence across sufficiently distinct attempts or sessions.
  - **Retired** — disproven, superseded, or no longer reliable.
- Confidence applies to the documented pattern, not automatically to every explanation or remedy mentioned inside it.
- The active drawing brief and its explicit constraints always take precedence over index guidance.

---

## Successful pattern template

Copy this block into `successful-patterns.md` and replace every bracketed instruction.

```markdown
## S-XXX — [Concise pattern title]

- Confidence: Provisional
- Last reviewed: YYYY-MM-DD
- Last user approval: YYYY-MM-DD
- Approved change: New entry / Evidence update / Confidence update / Scope update / Limitation update / Retirement
- Scope: [Scenes, subjects, prompt types, or conditions where this applies]

### Principle
[State the reusable technique as a concise rule.]

### Problem addressed
[Describe the recurring difficulty or requirement this technique helps with.]

### Implementation
[Explain how to apply the technique. Be specific enough to reuse.]

### Evidence
- [YYYY-MM-DD / attempt reference] — [Observed result and which requirement it satisfied]
- [YYYY-MM-DD / attempt reference] — [Additional result, if available]

### Limitations
[Describe known exceptions, trade-offs, or conditions where the technique may not work.]
```

### Entry standard

Add a successful pattern only when the evidence shows that the technique contributed to a meaningful improvement or reliably protected an important requirement. Do not infer effectiveness from prompt wording alone. The user must approve the exact entry before you write it.

---

## Failure pattern template

Copy this block into `failure-patterns.md` and replace every bracketed instruction.

```markdown
## F-XXX — [Concise failure title]

- Confidence: Provisional
- Last reviewed: YYYY-MM-DD
- Last user approval: YYYY-MM-DD
- Approved change: New entry / Evidence update / Confidence update / Scope update / Limitation update / Retirement
- Scope: [Scenes, subjects, prompt types, or conditions where this occurs]

### Observed failure
[Describe what visibly or operationally went wrong. Keep this factual.]

### Impact
[Identify the affected requirement, attribute, or workflow step.]

### Suspected cause
[State the current explanation, if any. Label it as a hypothesis unless it has been isolated and demonstrated.]

### Countermeasures tested

| Countermeasure | Evidence | Result |
|---|---|---|
| [Specific change tested] | [Attempt reference] | [Observed outcome: effective, ineffective, mixed, or inconclusive] |

### Effective prevention rule
[Add only when a countermeasure has evidence of effectiveness. Otherwise write: Not established.]

### Limitations
[Record exceptions, side effects, unresolved questions, or conditions that still trigger the failure.]
```

### Entry standard

Record a failure pattern when a failure is recurring or when a single incident reveals a sufficiently important, reusable risk. A suspected cause must not be presented as fact. A countermeasure is not an effective remedy until an actual attempt has tested it. The user must approve the exact entry or revision before you write it.

---

## Review checklist

Before committing a new or revised entry, validate:

- [ ] The user approved the exact entry or revision before the index update.
- [ ] The approval date and approved change scope are recorded.
- [ ] A new ID was assigned only after approval.
- [ ] The ID is unique and follows the correct prefix.
- [ ] The title describes one recognizable pattern.
- [ ] The scope is explicit.
- [ ] Observations are separated from hypotheses.
- [ ] Evidence links resolve to real daily records.
- [ ] Results are described accurately, including mixed or inconclusive outcomes.
- [ ] Confidence matches the strength and breadth of evidence.
- [ ] Limitations are recorded where known.
- [ ] The entry captures a reusable lesson rather than duplicating an attempt log.
- [ ] No guidance contradicts the authority of the active drawing brief.
