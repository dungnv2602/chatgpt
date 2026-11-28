# Subtasks — ADR 8 implementation

Parent: [20261128-230000](../task.md)

| ID | Subtask | Status | Required | Dependencies |
|---|---|---|---|---|
| 20261128-230000-01 | Coordinator, protected policy, contracts, and reusable workflow entry points | Done | Yes | None |
| 20261128-230000-02 | Generic verifier, exact-SHA aggregate, and coverage-preserving workflow migration | Done | Yes | 20261128-230000-01 |
| 20261128-230000-03 | Secure publisher, idempotency, recovery, checkpoint, and recursion prevention | Done | Yes | 20261128-230000-01 |
| 20261128-230000-04 | Worker queue, review/remediation lifecycle, attribution, grouping, and report migration | Blocked | Yes | 20261128-230000-02; 20261128-230000-03 |
| 20261128-230000-05 | Operational Confirmation, scenario demonstrations, coverage reconciliation, and gated retirement | Ready | Yes | 20261128-230000-02; 20261128-230000-03; 20261128-230000-04 |
