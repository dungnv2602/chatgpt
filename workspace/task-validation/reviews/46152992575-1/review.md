# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** 20261128-230000-04
- **Source SHA:** 74f41a589d607125728be54bd635a4b7ca73d73d
- **Coordinator run:** 46152992575
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** 5b0dcdc127e85ac3496e5444aaebe03658e1e435
- **Completed at:** 2026-11-28T14:07:03Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46152992575

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
