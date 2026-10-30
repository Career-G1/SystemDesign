# [Session 06] Replication and sharding

Choose a tenant or shard key and explain read replicas, replication lag, federation, hot spots, and resharding risk.

## Evidence

- `notes/session-06/`
- `evidence/session-06/shard-decision.md`

## Acceptance criteria

- [ ] I defended a shard key using access patterns.
- [ ] I explained what happens when one tenant is much larger.
- [ ] I compared RDS replicas, Cloud SQL replicas, DynamoDB, and Spanner.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Compare primary/replica, synchronous/asynchronous, and multi-primary replication.
2. Describe replication lag and a read-after-write experience that exposes it.
3. Choose a shard key using cardinality, query locality, growth, tenant isolation, and rebalancing effort.
4. Explain hot tenants, hot partitions, cross-shard queries, fan-out reads, and cross-shard transactions.
5. Compare range, hash, directory-based, and tenant-based partitioning.
6. Define a migration or resharding approach that avoids a risky big-bang move.
7. Compare RDS replicas, Cloud SQL replicas, DynamoDB partition keys, and Spanner.

## Ready-to-copy Issue details

- **Question:** When do read replicas stop being enough, and how would you choose a shard key?
- **Evidence:** `notes/session-06/interview-notes.md` and `evidence/session-06/shard-decision.md`.
- **Reviewer prompt:** Ask what happens when one tenant is much larger than all others.
