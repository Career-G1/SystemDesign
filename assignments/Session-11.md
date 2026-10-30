# [Session 11] Capstone mock interview

Design a familiar product aloud using use cases, assumptions, high-level components, data flow, bottlenecks, scaling, reliability, security, observability, and cost.

## Evidence

- `notes/session-11/`
- `evidence/session-11/capstone.md`

## Acceptance criteria

- [ ] I completed a timed 30-minute design.
- [ ] I stated assumptions and capacity estimates.
- [ ] I identified the first three bottlenecks and measurements.
- [ ] I compared AWS and Google Cloud choices.

## Detailed assignment

1. Spend the first five minutes clarifying functional and non-functional requirements.
2. State users, traffic, read/write ratio, payload size, retention, availability, latency, and growth assumptions.
3. Estimate peak requests per second, storage, bandwidth, and a rough cost driver.
4. Draw the client, web tier, load balancer, cache, database, queue, workers, auth, and observability.
5. Walk one read path, one write path, and one failure path.
6. Explain consistency, idempotency, retries, back pressure, and data ownership.
7. Identify the first three bottlenecks, measurements, and next scaling steps.
8. Compare one AWS and one Google Cloud deployment without treating provider names as the design.
9. End with risks, open questions, and a concise two-minute summary.

## Ready-to-copy Issue details

- **Question:** Design a familiar product for the stated scale and explain how it remains reliable as usage grows.
- **Evidence:** `notes/session-11/interview-notes.md` and `evidence/session-11/capstone.md`.
- **Reviewer prompt:** Ask which assumption, if changed by 10x, would force a different architecture.
