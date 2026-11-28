# Task Validation Review

- **Status:** Pending
- **Source Task-ID:** {{source_task_id}}
- **Source SHA:** {{source_sha}}
- **Coordinator run:** {{coordinator_run_id}}
- **Attempt:** {{attempt}}
- **Check-set identity:** {{check_set_id}}
- **Policy revision:** {{policy_revision}}
- **Completed at:** {{completed_at}}
- **Outcome:** {{outcome}}
- **Actions:** {{actions_url}}

## Worker handling

Read the task-validation status index first. Do not inspect logs for successful, cancelled, or superseded attempts. For recorded actionable failures, inspect only the relevant failed checks. Group related failures by root cause. Create one remediation child per distinct actionable root cause under the correctly attributed parent. Do not rerun checks or override the aggregate result.
