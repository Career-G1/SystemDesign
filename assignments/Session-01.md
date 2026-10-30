# [Session 01] Performance vs scalability

## Assignment

Explain performance versus scalability, define latency and throughput, and practice using p50, p95, and p99. Complete the local timing lab and write a two-minute interview answer.

## Read

- `wiki/Session-01.md`
- `labs/session-01/README.md`

## Evidence

- `notes/session-01/`
- `evidence/session-01/baseline.md`

## Acceptance criteria

- [ ] I can distinguish a slow request from a system that fails under concurrency.
- [ ] I recorded p50, p95, p99, throughput, and errors.
- [ ] I compared CloudWatch and Google Cloud Monitoring.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Define latency, throughput, concurrency, saturation, availability, p50, p95, and p99 in your own words.
2. State a small workload assumption: requests per second, payload size, concurrency, and an acceptable p95 target.
3. Run the lab sequentially and concurrently against the local stub.
4. Record request count, successes, failures, p50, p95, p99, elapsed time, and throughput.
5. Identify the first bottleneck and name the next measurement that would confirm it.
6. Compare vertical scaling, horizontal scaling, batching, caching, and asynchronous work.
7. Explain why average latency alone can hide a bad tail.

## Ready-to-copy Issue details

- **Question:** How do we distinguish a slow individual request from a system that cannot handle more concurrent users?
- **Evidence:** `notes/session-01/interview-notes.md` and `evidence/session-01/baseline.md`.
- **Reviewer prompt:** Ask whether the answer separates single-request latency from capacity under concurrency.
