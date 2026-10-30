# Session 04 personal interview notes

## Topic

Caching.

## Concept in my own words

A cache is a performance optimization, not the source of truth unless the product explicitly makes it one. Cache-aside is a useful default: read from cache, load on a miss, then populate it. The design must state key scope, TTL, invalidation, eviction, and behavior when the cache fails.

## Two-minute answer

I add a cache when repeated reads or expensive computation create measurable latency or source load. I choose a stable key with tenant and authorization boundaries, a TTL based on acceptable staleness, and explicit invalidation for important writes. I protect hot keys and cache misses with jitter, request coalescing, or refresh-ahead. If the cache is unavailable, the source of truth remains authoritative and the system degrades with a bounded timeout rather than treating a cache hit as guaranteed.

## Key decision

`resource:v1:{tenant_id}:{resource_id}` with a short TTL; invalidate on update or permission change. Add jitter to avoid synchronized expiry.

## Follow-ups

- What happens if a permission cache is stale?
- How do you prevent a thundering herd after expiry?
