# Session 10 - Authentication, secrets, and rate limiting

## Question

How do we protect users, credentials, and paid AI endpoints?

## Example code

- configuration references
- `backend/app/core/jwt.py`
- `backend/app/core/oauth_verifier.py`
- `backend/app/core/authz.py`
- `backend/app/core/rate_limit.py`

## Lab

Write an authorization test matrix for normal users and admins. Verify issuer, audience, expiry, and signature. Define a Redis token-bucket key and TTL. Use placeholder values only.

## Azure/GitHub mapping

Store secrets in Azure Key Vault and access them through managed identity. Use Microsoft Entra ID where appropriate, API Management for gateway policies, GitHub secret scanning, and GitHub Actions secrets for CI.

## Interview answer

Short-lived access tokens limit exposure; refresh rotation and a denylist or token version provide revocation. Authorization must check the resource owner or role, not only token validity.
