# [Project] — Attempt [NN]: [Short scene title]

## Record

- **Template version:** 1.1
- **Attempt:** [Sequential number]
- **Session ID:** [Exact session ID]
- **Session brief:** [Exact relative path]
- **Date:** [YYYY-MM-DD]
- **Opening direction authority:** [Active session brief link]
- **Series ID / name / theme:** [Conditional: use verified details only when the active brief adopts a series. Otherwise write standalone/unassigned]
- **Membership role:** [Conditional: Series seed / Continuation / Subseries / Branch / Crossover / Provisional. Use Standalone when no series applies]
- **Scene:** [Conditional: approved named scene, or Not applicable for day drawing]
- **Operation:** [Fresh generation / Prompt-first reconstruction / Direct image edit]
- **Record status:** [Draft / Committed / Superseded]
- **Generation status:** [Not started / Generated / Refused / Failed / No output / Unconfirmed]
- **User decision:** [Not requested / Pending / Approved / Rejected / Superseded / Not recorded]
- **Prompt ID:** [Stable prompt ID or Not assigned]
- **Specific detail tested:** [One clear visual change or question]
- **Continuity anchors and permitted variation:** [Details from the active brief that must remain stable, plus permitted changes]
- **Baseline provenance:** [Conditional: exact successful prompt path and attempt, plus why it qualifies. Otherwise write None / first attempt]
- **Latest-attempt diagnostic reference:** [Conditional: exact later attempt inspected and its relevance. Otherwise write None]
- **Source image / reference:** [Conditional: exact asset path or supplied image ID and its role for a direct edit or adopted reference. Otherwise write None]

Use `Unknown` for missing evidence and `Not applicable` when a field does not apply. Do not leave required fields blank. For a new attempt, set Record status to `Committed` and Generation status to `Not started` before the generation call.

## Generation prompt — copyable

```text
[Paste the complete authored generation prompt here. Keep this block limited to visual instructions. Do not place provenance, attempt labels, file paths, prompt references, or workflow notes inside it.]
```

## Acceptance criteria — before generation/editing

Record three to five observable requirements from the active brief. Mark critical requirements and state the expected visible evidence.

| # | Observable requirement | Priority | Expected visible evidence |
|---|---|---|---|
| 1 | [Requirement] | [Critical / Standard] | [Visible evidence] |

## Prompt difference

- **Baseline:** [Exact successful prompt path and attempt, or None / first attempt]
- **Preserved:** [Details carried forward from the baseline and active brief]
- **Changed:** [Exact changes and the user instruction that authorizes each change]
- **Excluded:** [Details deliberately not carried forward and why]

## Generation and outputs

- **Authored prompt committed before generation:** [Yes / No]
- **Actual submitted payload:** [Exact text if exposed / Not exposed]
- **Generation result:** [Not started / Generated / Refused / Failed / No output / Unconfirmed]
- **Output count and order:** [Actual count and sequence, or Not started]

| Output ID | Native generation ID | Native image ID | Mapping evidence and status | Original / archive asset | SHA-256 |
|---|---|---|---|---|---|
| [Internal output ID] | [Native ID or Unavailable] | [Native ID or Unavailable] | [Evidence] — [Verified / Corroborated / Probable / Unmapped / Conflicting] | [Verified path or Unavailable] | [Hash or Unavailable] |

## Per-output assessment — after generation/editing

Assess every returned image separately. If no image was returned, write Not applicable. Do not treat one successful output as proof that all outputs succeeded.

| Output ID | Acceptance criterion | Result: Pass / Partial / Fail / Not assessable | Visible evidence |
|---|---|---|---|
| [Output ID] | [Criterion] | [Result] | [Brief observation] |

## Review

- **Prompt/result success:** [Yes / No / Unconfirmed — state why]
- **User-approved visual keeper:** [Yes / No / Pending / Not applicable]
- **Outcome:** [Successful match / Partial match / Generated but missed target / Fresh generation, not an edit / Rejected or failed]
- **User decision:** [Not requested / Pending / Approved / Rejected / Superseded / Not recorded]
- **Next action:** [One concise next step, or None]
