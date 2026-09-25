# Session 10 - Authentication, secrets, and rate limiting

## Question

How do we protect users, credentials, and paid APIs?

## Example code

- configuration references
- `backend/app/core/jwt.py`
- `backend/app/core/oauth_verifier.py`
- `backend/app/core/authz.py`
- `backend/app/core/rate_limit.py`

## Lab

Write an authorization test matrix for normal users and admins. Verify issuer, audience, expiry, and signature. Define a Redis token-bucket key and TTL. Use placeholder values only.

## AWS/Google Cloud/GitHub mapping

For interview discussion, compare a secret manager, workload identity, an identity provider, and gateway policies. AWS examples include Secrets Manager, IAM, and Cognito; Google Cloud examples include Secret Manager, IAM, and Identity Platform. GitHub examples include repository secrets and secret scanning.

## Interview answer

Short-lived access tokens limit exposure; refresh rotation and a denylist or token version provide revocation. Authorization must check the resource owner or role, not only token validity.
