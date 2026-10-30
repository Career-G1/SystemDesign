# Session 03 personal interview notes

## Topic

Load balancing and horizontal scaling.

## Concept in my own words

Horizontal scaling adds instances and requires requests to succeed regardless of which instance receives them. A load balancer routes traffic and removes instances that fail the right health checks. Shared state belongs in a durable or shared service rather than process memory.

## Two-minute answer

With two replicas, I remove process-local assumptions. Sessions, rate limits, locks, uploads, and caches either move to shared infrastructure or become stateless. The load balancer needs startup, readiness, and liveness behavior so it does not send traffic to an instance that is alive but unable to serve. I also need graceful shutdown, connection draining, autoscaling signals, and protection from retry storms. Sticky sessions can help temporarily, but they reduce flexibility and hide the underlying state problem.

## Diagram checklist

- Client and TLS boundary
- L4 or L7 load balancer
- Two replicas
- Shared database and cache
- Health-check paths
- Failure and drain path

## Follow-ups

- What does readiness check that liveness should not?
- Where does a session live after a replica is terminated?
