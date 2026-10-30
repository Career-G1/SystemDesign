# [Session 03] Load balancing and horizontal scaling

Explain L4/L7 load balancing, health checks, stateless services, and why sticky sessions are usually a workaround. Draw a request-flow diagram for two replicas.

## Evidence

- `notes/session-03/`
- `evidence/session-03/request-flow.md`

## Acceptance criteria

- [ ] I can explain how unhealthy instances are removed.
- [ ] I identified process-local state that breaks with two replicas.
- [ ] I compared ECS/EKS with Cloud Run/GKE.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Explain L4 versus L7 load balancing, TLS termination, routing, retries, and connection draining.
2. Draw a request flow with a client, load balancer, two replicas, a shared database, and a shared cache.
3. List process-local state that breaks when traffic moves between replicas.
4. Define startup, liveness, readiness, and dependency health checks.
5. Explain why sticky sessions can hide a state-management problem.
6. Describe graceful shutdown, autoscaling signals, and retry storms.
7. Compare ECS/EKS with Cloud Run/GKE.

## Ready-to-copy Issue details

- **Question:** What must change when a service moves from one instance to two or more instances?
- **Evidence:** `notes/session-03/interview-notes.md` and `evidence/session-03/request-flow.md`.
- **Reviewer prompt:** Ask what happens to in-memory sessions, rate limits, uploads, and caches.
