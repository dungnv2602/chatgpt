# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** 20261128-230000-04
- **Source SHA:** e67c2dc5f23e52cabadab769c9ec5fdc5343ac18
- **Coordinator run:** 46164128871
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** 3e0efd87728646c0be2eb5854f95140151a3c44b
- **Completed at:** 2026-11-28T16:15:03Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46164128871

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
