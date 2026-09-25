# Session 01 - Performance vs scalability

## Question

How do we distinguish a slow individual request from a system that cannot handle more concurrent users?

## Example code

- `backend/app/api/endpoints/agents.py`
- `backend/app/agents/graph.py`

## Lab

Create a small local timing harness under `labs/session-01/` that records request count, concurrency, p50, p95, p99, and throughput. Use a local stub rather than a real service.

## Azure/GitHub mapping

Use Application Insights and Azure Monitor for request duration, dependency calls, failures, and percentile-based dashboards. Use GitHub Actions to run a repeatable local benchmark.

## Interview answer

Start by separating single-request latency from throughput under concurrency. Measure p95/p99 and dependency timing before changing architecture.
