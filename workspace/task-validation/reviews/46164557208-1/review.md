# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** 20261128-230000-04
- **Source SHA:** 6ed068ce19ddd29cccfc1294cfd2d07ce455ed84
- **Coordinator run:** 46164557208
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** 3e0efd87728646c0be2eb5854f95140151a3c44b
- **Completed at:** 2026-11-28T16:19:45Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46164557208

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
