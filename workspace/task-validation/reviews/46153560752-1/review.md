# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** 20261128-230000-04
- **Source SHA:** 146edc382863fbc247d0a3e8f0723718a0d4c82a
- **Coordinator run:** 46153560752
- **Attempt:** 1
- **Check-set identity:** Unavailable
- **Policy revision:** 46cdbe5b85a9d0731b0a4810644aad3177a94ebc
- **Completed at:** 2026-11-28T14:13:36Z
- **Outcome:** capture_failure
- **Actions:** https://github.com/dungnv2602/chatgpt/actions/runs/46153560752

## Worker handling

Read the task-validation status index first. Compare the attempt's exact source SHA with the task's Validation Lifecycle block and current source commit. Do not let a stale result change current task state. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks when hosted inspection is authorized. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result. Cancelled and superseded attempts do not change task lifecycle.
