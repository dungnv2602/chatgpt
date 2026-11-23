# Central CI issue ledger

The ledger tracks distinct lint and GitHub Actions issues across report runs. It stores normalized issue records and links to immutable source reports.

## Finding identity

- Lint findings use the report's stable \`fingerprint\`. The same fingerprint in both lint scopes maps to one finding.
- GitHub Actions findings use workflow ID and path, job name, step name, category, and normalized diagnostic text.
- The generator normalizes commit hashes, run IDs, timestamps, and whitespace in diagnostic signatures.
- A workflow conclusion alone does not create a finding. The report must contain a specific classified issue.
- Only complete post-run Actions reports contribute findings. Pre-finalizer reports do not create issues.
- Cancelled, skipped, neutral, queued, in-progress, and unavailable states do not create findings by themselves.

Each evidence entry records its immutable report path, run URL, observation time, and run identity. The occurrence count measures unique source run attempts. A lint finding in both scopes counts once for the same run.

## Ingestion and publication

The generator reads report paths from the lint and Actions indexes. It does not scan report history directories.

The existing capture action ingests published lint reports. The diagnostics sweep ingests complete post-run Actions reports. Both use the shared non-cancelling \`gh-ac-report-writer\` concurrency group. This group serializes ledger writers.

The generator writes the ledger with an atomic file replacement. It does not modify source reports.

GitHub Actions runs the generator and its regression tests on hosted runners. Do not run repository scripts locally.

The ledger uses schema version \`1.1.0\`. The generator migrates version \`1.0.0\` and preserves existing findings. The initial bootstrap marks all indexed reports as processed. It does not import historical findings.

The publisher runs this command:

\`\`\`bash
python3 reports/triage/scripts/ledger.py --mode ingest
\`\`\`

## Triage lifecycle

New findings start with status \`open\`. The allowed statuses are:

\`open\`, \`investigating\`, \`planned\`, \`fixing\`, \`verifying\`, \`resolved\`, \`accepted\`, \`false_positive\`, and \`duplicate\`.

Humans control status, owner, severity, accepted risk, duplicate links, and resolution notes. Ingestion does not overwrite these fields.

### Default severity

- Lint \`advisory-free\` and \`hard\` findings start at \`medium\`.
- Lint \`advisory\` findings start at \`low\`.
- Unknown lint levels start at \`informational\`.
- Blocking Actions issues with high confidence start at \`high\`.
- Medium-confidence Actions issues start at \`medium\`.
- Low-confidence Actions issues start at \`low\`.
- High-confidence non-blocking Actions issues start at \`medium\`.

Humans can change severity when evidence supports an override.

### Accepted risk and duplicates

An \`accepted\` finding requires an \`accepted_risk\` object. Record its rationale, approver, and UTC acceptance time.

A \`duplicate\` finding requires \`duplicate_of\` with the ID of another ledger finding. Do not create duplicate links to the same finding.

### Resolution and recurrence

A \`resolved\` finding requires a fix commit and successful validation evidence. Record the validation run URL and UTC validation time. Add a UTC resolution time and an optional note.

When a new run observes a resolved finding, the generator reopens it. The generator moves the previous resolution into \`resolution_history\`. A second scope from the same run does not count as recurrence.

## Historical backfill

Do not clear \`ingestion_state.processed_reports\` to force a backfill. Do not import every historical run as a separate issue.

Historical backfill requires a separate approved task. Review identity rules first. Then deduplicate observations and preserve every immutable evidence reference.

## Operator procedure

1. Review the evidence paths and run URLs before changing a finding.
2. Assign an owner and set severity based on impact and confidence.
3. Use \`investigating\`, \`planned\`, \`fixing\`, and \`verifying\` to record work.
4. Add an \`accepted_risk\` object before setting status to \`accepted\`.
5. Add a valid \`duplicate_of\` ID before setting status to \`duplicate\`.
6. Record the fix commit and successful relevant validation before setting status to \`resolved\`.
7. Preserve resolution notes and prior validation evidence in \`resolution_history\` after recurrence.

The schema at \`ledger-schema.json\` defines the record fields. The regression tests at \`scripts/test_ledger.py\` cover identity, deduplication, lifecycle, malformed input, and atomic publication.
