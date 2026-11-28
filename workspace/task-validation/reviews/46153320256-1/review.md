# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** 20261128-230000-04
- **Source SHA:** a76c2523f240f2f29a89fb03e002748ef6b6941d
- **Coordinator run:** 46153320256
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** 5b0dcdc127e85ac3496e5444aaebe03658e1e435
- **Completed at:** 2026-11-28T14:10:52Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46153320256

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
