# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** 20261128-230000-04
- **Source SHA:** 8ff87de0cc14b6da10ade88c14135f459cc14485
- **Coordinator run:** 46154084889
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** a0a8173b716675638e18a30ff037f98dc52d60f6
- **Completed at:** 2026-11-28T14:19:43Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46154084889

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
