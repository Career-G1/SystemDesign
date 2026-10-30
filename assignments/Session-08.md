# [Session 08] Message queues and async work

Design a producer, queue, and consumer for a long-running task. Define a 202 API, job states, retries, idempotency, back pressure, and a dead-letter path.

## Evidence

- `notes/session-08/`
- `evidence/session-08/queue-contract.md`

## Acceptance criteria

- [ ] I can explain why the request should return a job ID.
- [ ] I handled duplicate delivery and consumer failure.
- [ ] I compared SQS/SNS with Pub/Sub.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Define `POST /agents/run` returning `202 Accepted` and a `run_id`.
2. Define `GET /agents/runs/{run_id}` with queued, running, succeeded, failed, and cancelled states.
3. Specify the producer payload, message ID, visibility timeout or lease, retry policy, and dead-letter path.
4. Add an idempotency key and explain how duplicate delivery returns the same terminal result.
5. Explain at-least-once delivery, ordering limits, poison messages, back pressure, and worker concurrency.
6. Define cancellation, timeout, progress, and partial-failure behavior.
7. Compare SQS/SNS with Pub/Sub.

## Ready-to-copy Issue details

- **Question:** How should a long-running task avoid occupying an HTTP worker?
- **Evidence:** `notes/session-08/interview-notes.md` and `evidence/session-08/queue-contract.md`.
- **Reviewer prompt:** Ask what happens if the worker completes but crashes before acknowledging.
