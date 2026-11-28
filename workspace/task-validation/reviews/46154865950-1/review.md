# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** Unattributed
- **Source SHA:** 78d93516a037a0afaa802a7de994d04f220fe010
- **Coordinator run:** 46154865950
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** e61129bf855ae3eacd59dc77b53e835ca45bf86f
- **Completed at:** 2026-11-28T14:28:54Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46154865950

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
