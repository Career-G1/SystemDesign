# Session 10 lab

Create tests using fake tokens and placeholder secrets. Cover invalid signature, wrong issuer, wrong audience, expired token, missing role, object ownership, and rate-limit exhaustion.

Expected output: `evidence/session-10/auth-matrix.md`.
## Practical exercise

Run the local signed-token and token-bucket example. The secret is intentionally a demo placeholder and must not be reused.

```powershell
python labs/session-10/auth_rate_limit.py
```

Expected output: `evidence/session-10/auth-matrix.md`.
