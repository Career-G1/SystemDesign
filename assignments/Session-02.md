# [Session 02] CAP and consistency

Explain CAP, consistency models, read-after-write, and the difference between strong and eventual consistency. Produce a store-by-store consistency table.

## Evidence

- `notes/session-02/`
- `evidence/session-02/consistency-table.md`

## Acceptance criteria

- [ ] I can explain CAP without relying on a triangle diagram.
- [ ] I chose consistency per data type and justified it.
- [ ] I compared Amazon RDS/ElastiCache with Cloud SQL/Memorystore.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Explain CAP using a network-partition scenario, not a permanent triangle choice.
2. Define strong consistency, eventual consistency, linearizability, read-after-write, and monotonic reads.
3. Create a table for ownership/payment data, profiles, cached search, rate-limit counters, and JWT revocation.
4. For each data type, record the stale-read consequence, consistency choice, and recovery behavior.
5. Write one read-after-write failure trace caused by replica lag.
6. Explain why consistency is chosen per access pattern and business invariant.
7. Compare Amazon RDS/ElastiCache with Cloud SQL/Memorystore.

## Ready-to-copy Issue details

- **Question:** How do you choose between strong and eventual consistency for different data in one system?
- **Evidence:** `notes/session-02/interview-notes.md` and `evidence/session-02/consistency-table.md`.
- **Reviewer prompt:** Ask which user-visible error is acceptable when a replica is stale.
