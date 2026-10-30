# [Session 04] Caching

Explain cache-aside, write-through, TTL, invalidation, and thundering herd prevention. Design one cache key and test its hit/miss behavior.

## Evidence

- `notes/session-04/`
- `evidence/session-04/cache-decision.md`

## Acceptance criteria

- [ ] I selected a caching strategy and justified it.
- [ ] I documented key format, TTL, invalidation, and stampede protection.
- [ ] I compared ElastiCache and Memorystore.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Compare cache-aside, read-through, write-through, write-behind, and refresh-ahead.
2. Design a key containing a namespace, tenant or owner boundary, resource ID, and version.
3. Choose a TTL and explain the stale-data consequence.
4. Define invalidation for create, update, delete, and permission changes.
5. Explain misses, negative caching, eviction, hot keys, serialization cost, and thundering herd.
6. Choose one mitigation: request coalescing, jittered TTLs, locking, or refresh-ahead.
7. Describe cache failure behavior and compare ElastiCache with Memorystore.

## Ready-to-copy Issue details

- **Question:** When should you add a cache, and how do you keep it from becoming a correctness problem?
- **Evidence:** `notes/session-04/interview-notes.md` and `evidence/session-04/cache-decision.md`.
- **Reviewer prompt:** Ask what happens when the cache is unavailable or contains stale permissions.
