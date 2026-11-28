# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** Unattributed
- **Source SHA:** 29eab76efebf2f4ee84d7bec2fbce123e53adcbc
- **Coordinator run:** 46162583540
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** efa56c7e8e493908819ffc18bde0eb6ade3e8a0e
- **Completed at:** 2026-11-28T15:57:43Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46162583540

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
