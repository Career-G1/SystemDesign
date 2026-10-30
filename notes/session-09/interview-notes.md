# Session 09 personal interview notes

## Topic

REST and idempotency.

## Concept in my own words

A good API makes resources, state transitions, errors, pagination, and retry behavior predictable. HTTP method semantics help, but operations such as payment or job creation often need an application-level idempotency key.

## Two-minute answer

I start with resource nouns, clear status codes, and a consistent error shape. For a non-idempotent operation, the client sends an idempotency key scoped to the authenticated actor and operation. The server stores the request hash and final response for a retention window; a repeated identical request returns the same response, while a conflicting payload returns a conflict error. I also choose cursor pagination for changing large datasets, define timeout and retry behavior, and preserve backward compatibility through versioning or additive changes.

## Error shape

`code`, `message`, `request_id`, and optional field-level details.

## Follow-ups

- What happens when the same key is reused with a different payload?
- Why can offset pagination duplicate or skip rows?
