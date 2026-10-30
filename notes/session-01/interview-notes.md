# Session 01 personal interview notes

## Topic

Performance versus scalability.

## Concept in my own words

Performance asks how quickly one request completes. Scalability asks how capacity changes when traffic, data, or concurrency grows. A system can have good average latency at low load and still fail at the tail when workers, connections, CPU, or a dependency saturate.

## Assumptions to fill in

- Peak requests per second:
- Concurrent requests:
- p95 latency target:
- Main dependency:

## Trade-offs

| Choice | Benefit | Cost or risk |
|---|---|---|
| Vertical scaling | Simple operationally | Has a hardware ceiling |
| Horizontal scaling | Adds capacity incrementally | Requires statelessness and coordination |
| Cache or batch | Reduces repeated work | Can create stale data or bursts |

## Two-minute answer

I separate single-request performance from system scalability. I would measure p50, p95, p99, throughput, error rate, saturation, and dependency timing under both sequential and concurrent load. If the tail grows as concurrency rises, I would identify the first saturated resource, such as CPU, database connections, or an external API, before changing the architecture. I would then choose the smallest fix, such as query optimization, caching, more workers, or asynchronous work, and verify it with the same workload.

## Follow-ups

- Why is p95 more useful than average for user experience?
- What would change at 10x traffic?
- Which measurement proves the database is the bottleneck?
