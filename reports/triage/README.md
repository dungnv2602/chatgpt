# Report triage ledger

Deduplicate repeated observations into one issue. Use the stable lint `fingerprint` for lint findings; use normalized workflow/job/step/category identity for Actions findings. Keep source reports immutable and attach their paths and run URLs as evidence.

Statuses: `open`, `investigating`, `planned`, `fixing`, `verifying`, `resolved`, `accepted`, `false_positive`, `duplicate`. Mark resolved only after recording the fix commit and successful relevant validation. Recurrence reopens the same finding. Cancelled, skipped, neutral, queued, and in-progress runs are not defects by themselves.

`ledger.json` is the machine-readable source of truth. Do not bulk-import each historical run as a separate finding; deduplicate first. Existing history is not yet fully triaged.
