# [Session 10] Authentication, credentials, and rate limiting

Explain OAuth/OIDC, JWT validation, refresh rotation, authorization, secret management, and token-bucket rate limiting using placeholders only.

## Evidence

- `notes/session-10/`
- `evidence/session-10/auth-matrix.md`

## Acceptance criteria

- [ ] I can explain issuer, audience, expiry, and signature validation.
- [ ] I distinguished authentication from authorization.
- [ ] I compared Cognito/Secrets Manager with Identity Platform/Secret Manager.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Explain OAuth 2.0, OIDC, access tokens, refresh tokens, scopes, and roles.
2. Define JWT validation for issuer, audience, expiry, not-before, signature, algorithm, and key rotation.
3. Separate authentication from authorization and test owner, member, admin, anonymous, and revoked cases.
4. Explain short-lived tokens, refresh rotation, token versioning, denylisting, logout, and compromise response.
5. Define secret storage, least privilege, workload identity, rotation, redaction, and secret scanning.
6. Design a token bucket with a key, capacity, refill rate, TTL, response headers, and proxy assumptions.
7. Compare Cognito/Secrets Manager with Identity Platform/Secret Manager.

## Ready-to-copy Issue details

- **Question:** How do we protect users, credentials, and paid APIs?
- **Evidence:** `notes/session-10/interview-notes.md` and `evidence/session-10/auth-matrix.md`.
- **Reviewer prompt:** Ask whether a valid token is enough to authorize access to another user's resource.
