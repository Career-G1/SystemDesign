# Session 10 personal interview notes

## Topic

Authentication, credentials, and rate limiting.

## Concept in my own words

Authentication establishes who the caller is; authorization decides what that caller may do. A valid JWT is not proof that the caller owns every resource. Secrets need managed storage and rotation, while rate limits need a clearly defined identity key and a behavior for trusted proxies.

## Two-minute answer

I validate a token's signature, algorithm, issuer, audience, expiry, and key version before using its claims. Then I authorize the requested resource using ownership, role, or scope checks. I use short-lived access tokens and refresh rotation, with token versioning or a denylist when revocation is required. Secrets stay in a managed secret store or workload identity rather than source code. For paid APIs, I use a token bucket keyed by the right identity, return retry information, and monitor rejected requests and abuse patterns.

## Authorization matrix starter

| Caller | Own resource | Other user's resource | Admin action |
|---|---|---|---|
| Anonymous | deny | deny | deny |
| User | allow | deny | deny |
| Admin | allow | policy-dependent | allow |

## Follow-ups

- How do you handle signing-key rotation?
- What if a proxy lets callers spoof an IP-based limit key?
