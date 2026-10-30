# [Session 09] REST and idempotency

Audit resource naming, HTTP verbs, pagination, versioning, error shape, and retry behavior. Define an idempotency key for a non-idempotent operation.

## Evidence

- `notes/session-09/`
- `evidence/session-09/api-contract.md`

## Acceptance criteria

- [ ] I can explain which verbs are idempotent and why.
- [ ] I defined one consistent error response.
- [ ] I compared API Gateway with Apigee.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Define resources and relationships before choosing endpoint paths.
2. Explain safe and idempotent methods and identify operations needing application-level idempotency.
3. Design an idempotency-key contract: scope, request hash, stored response, retention, conflicts, and replay.
4. Choose cursor or offset pagination and explain ordering, duplicates, and deletion behavior.
5. Define an error shape with a machine-readable code, message, request ID, and validation details.
6. Describe timeouts, retries, backoff, rate limits, versioning, and backward compatibility.
7. Compare API Gateway with Apigee.

## Ready-to-copy Issue details

- **Question:** How do you make a public API safe and predictable when clients retry requests?
- **Evidence:** `notes/session-09/interview-notes.md` and `evidence/session-09/api-contract.md`.
- **Reviewer prompt:** Retry the same non-idempotent request and ask whether the result is duplicated.
