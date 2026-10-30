# Session 11 personal interview notes

## Topic

Capstone mock interview.

## Interview structure

1. Clarify use cases and non-goals.
2. State scale, latency, availability, retention, and growth assumptions.
3. Estimate peak traffic, storage, and bandwidth.
4. Draw the simple high-level architecture.
5. Walk a read path, write path, and failure path.
6. Explain data model, consistency, idempotency, and asynchronous work.
7. Identify the first three bottlenecks and measurements.
8. Discuss security, observability, cost, and future evolution.

## Two-minute answer template

I would start by confirming the core use cases and the scale assumptions rather than choosing services immediately. The initial design would use a stateless web tier behind a load balancer, a relational source of truth, a cache for measured hot reads, and a queue for work that exceeds the request budget. I would make writes idempotent, define failure and retry behavior, and monitor latency tails, errors, queue age, database saturation, and cost. The next scaling step would be driven by the first measured bottleneck, not by adding components preemptively.

## Self-review

- What assumption was weakest?
- Which component fails first at 10x?
- Which requirement did I not clarify?
- Did I explain why each component exists?
- Did I finish with trade-offs instead of a service list?
