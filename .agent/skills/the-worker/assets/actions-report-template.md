# {title}

## Run identity

{identity}

## Executive summary

{summary}

## Failure classification

{classification}

The report records an actionable workflow failure or operational exception. By default, the capture process excludes ordinary successful runs and runs that only involve cancellation. The capture process retains a successful run when a step failed but the workflow continued. The capture process retains a cancelled run only when it contains an independent actionable failure. The capture process excludes known downstream status-propagation steps after cancellation. Explicit run-backfill requests may bypass retry timing for one exact completed run, but they cannot override the error-only retention rule. The capture process never retains successful runs or runs that only involve cancellation.

## Jobs and steps

{jobs}

## Actionable step outcomes

{issues}

## Check annotations

{annotations}

## Artifacts

{artifacts}

## Captured job logs

{logs}

## Evidence coverage

{coverage}

## Related lint evidence

{lint_reference}

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.