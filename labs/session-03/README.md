# Session 03 lab

Draw the request path through a load balancer to two stateless replicas and list all process-local state that must move to Redis or a database.
## Practical exercise

Run the local load-balancer simulation and document what happens when one replica fails its health check.

```powershell
python labs/session-03/load_balancer_sim.py
```

Expected output: `evidence/session-03/request-flow.md`.
