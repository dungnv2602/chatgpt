# {title}

## Run identity

{identity}

## Executive summary

{summary}

## Failure classification

{classification}

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests may bypass retry timing for one exact completed run, but they cannot override the error-only retention rule. Successful and cancellation-only runs are never retained.

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