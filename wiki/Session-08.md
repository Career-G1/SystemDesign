# Session 08 - Message queues and async work

## Question

How should a long-running task avoid occupying an HTTP worker?

## Example code

- `backend/app/api/endpoints/agents.py`
- `backend/app/agents/graph.py`
- `backend/app/models/ai.py`

## Lab

Define a producer/consumer contract. `POST /agents/run` returns `202 Accepted` and a `run_id`; `GET /agents/runs/{run_id}` returns queued, running, succeeded, failed, or cancelled. Add an idempotency key and a duplicate-delivery test.

## AWS/Google Cloud/GitHub mapping

Amazon SQS/SNS or Google Pub/Sub provides durable delivery, retries, dead-lettering, and competing consumers. ECS, Cloud Run Jobs, or GKE can process the task. GitHub Issues track the API contract and pull request.

## Interview answer

Use a bounded queue and return a job ID immediately. Make the consumer idempotent by storing the idempotency key and terminal result before acknowledging the message.
