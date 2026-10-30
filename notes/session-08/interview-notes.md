# Session 08 personal interview notes

## Topic

Message queues and asynchronous work.

## Concept in my own words

A queue separates request latency from work duration and provides buffering when producers are faster than consumers. It does not remove failure; it makes retries, duplicate delivery, visibility timeouts, dead letters, and job state explicit.

## Two-minute answer

For long-running work, the API validates the request, creates a durable run record, publishes a message, and returns `202 Accepted` with a job ID. A worker claims the message, updates the state, performs idempotent work, stores the terminal result, and acknowledges only after that result is durable. Because delivery is often at least once, the idempotency key and result record prevent duplicate side effects. I monitor queue depth, oldest message age, retry count, worker utilization, and dead-letter volume.

## State machine

`queued -> running -> succeeded`

`queued/running -> failed | cancelled`

## Follow-ups

- What if the worker completes before acknowledging?
- How does back pressure protect the database?
