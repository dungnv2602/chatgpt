# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** Unattributed
- **Source SHA:** 527d4fa75bad6d34f3f88b7f97b917a6ed2155d1
- **Coordinator run:** 46161720712
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** e61129bf855ae3eacd59dc77b53e835ca45bf86f
- **Completed at:** 2026-11-28T15:47:34Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46161720712

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
