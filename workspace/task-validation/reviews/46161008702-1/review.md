# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** 20261127-173000-76
- **Source SHA:** 9c003854754dcebf370cafc236f978bfc7265ee6
- **Coordinator run:** 46161008702
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** e61129bf855ae3eacd59dc77b53e835ca45bf86f
- **Completed at:** 2026-11-28T15:39:26Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46161008702

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
