"""Shared eligibility policy for persisted GitHub Actions error reports.

The reporter may retain an incomplete post-run error capture so its bounded retry
policy can finish collecting evidence. The Ledger requires the same report to be
complete before creating observations. Both consumers use this module's one
independent-error predicate.
"""

IGNORED_ACTION_CATEGORIES = frozenset({
    "cancelled", "skipped", "neutral", "queued", "in_progress",
    "unavailable", "unknown", "not_available",
})


def is_status_propagation_step(step_name):
    name = str(step_name or "").strip().casefold()
    return (
        ("preserve" in name and any(term in name for term in ("conclusion", "result", "status")))
        or ("propagat" in name and any(term in name for term in ("conclusion", "result", "status")))
        or name.startswith("set workflow result")
    )


def has_independent_diagnostic(issue):
    """Require a real diagnostic when the classifier supplies no job or step identity."""
    if issue.get("job_id") or issue.get("job_name") or issue.get("step_name"):
        return True
    message = " ".join(str(issue.get("message") or "").split()).strip().casefold()
    return message not in {
        "", "step conclusion: failure", "job conclusion: failure",
        "step conclusion: timed_out", "job conclusion: timed_out",
    }


def independent_actions_issues(report):
    """Return only independently actionable classified Actions issues."""
    classification = report.get("classification") or {}
    issues = classification.get("issues")
    if not isinstance(issues, list):
        return []
    result = []
    for issue in issues:
        if not isinstance(issue, dict):
            continue
        category = str(issue.get("category") or "unknown").strip().casefold()
        if category in IGNORED_ACTION_CATEGORIES:
            continue
        if is_status_propagation_step(issue.get("step_name")):
            continue
        if not has_independent_diagnostic(issue):
            continue
        result.append(issue)
    return result


def actions_report_is_eligible(report, require_complete=False):
    """Shared Actions error eligibility gate used by retention and Ledger ingestion."""
    capture = report.get("capture") or {}
    source = report.get("source_run") or {}
    if capture.get("stage") != "post_run" or source.get("status") != "completed":
        return False
    if require_complete and capture.get("completeness") != "Complete":
        return False
    return bool(independent_actions_issues(report))
