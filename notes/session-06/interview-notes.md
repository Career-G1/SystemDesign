# Session 06 personal interview notes

## Topic

Replication and sharding.

## Concept in my own words

Replication creates additional copies for read capacity or availability, but asynchronous copies can lag. Sharding partitions ownership of data so one database is not the limit, but it introduces routing, rebalancing, cross-shard queries, and hot-partition risks.

## Two-minute answer

I first ask whether read replicas solve the actual bottleneck. If writes, storage, or a single hot tenant are the problem, replicas alone are insufficient. I choose a shard key from the dominant access patterns, cardinality, growth, and the need to keep related records together. I document how reads route after a write, how lag is handled, and how a tenant can be moved without a downtime migration. I would delay sharding until measurements show the simpler design is no longer adequate.

## Follow-ups

- What happens when one tenant is much larger?
- How do you reshard without changing every client?
