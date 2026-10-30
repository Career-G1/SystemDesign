# Session 02 personal interview notes

## Topic

CAP and consistency.

## Concept in my own words

CAP describes behavior during a network partition: a distributed system cannot guarantee both perfect consistency and availability for every operation. The choice should be made per business invariant. Ownership, payments, and authorization usually need stronger guarantees, while cached search or analytics may tolerate stale results.

## Two-minute answer

I first identify the invariant and the consequence of a stale read. During a partition, a system may reject writes or serve potentially stale data; that is the consistency-versus-availability decision. I would keep the source of truth strongly protected for ownership or financial state, while allowing eventual consistency for caches, feeds, or analytics. I would also document read-after-write behavior, replica lag, retries, and how the user sees an unavailable or stale result.

## Decision table starter

| Data | Consistency | Stale-read consequence | Measurement |
|---|---|---|---|
| Ownership/payment | Strong | Incorrect access or charge | conflict/error rate |
| Cached search | Eventual | Older result | age of cached value |
| Rate limit | Bounded/eventual | Short overage | rejected requests |

## Follow-ups

- What does CAP mean only when a partition occurs?
- How do you provide read-after-write with replicas?
