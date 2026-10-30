"""Validate a signed placeholder token and apply a token bucket."""

import base64
import hashlib
import hmac
import time

secret = b"local-demo-only"
payload = b"user=alice;role=user"
signature = hmac.new(secret, payload, hashlib.sha256).digest()
token = base64.urlsafe_b64encode(payload + b"." + signature).decode()

decoded_payload, decoded_signature = base64.urlsafe_b64decode(token).rsplit(b".", 1)
valid = hmac.compare_digest(
    decoded_signature, hmac.new(secret, decoded_payload, hashlib.sha256).digest()
)
print("signature_valid:", valid)

tokens = 3.0
last = time.monotonic()
for request_number in range(5):
    now = time.monotonic()
    tokens = min(3.0, tokens + (now - last) * 1.0)
    last = now
    allowed = tokens >= 1
    if allowed:
        tokens -= 1
    print(f"request={request_number + 1} allowed={allowed} remaining={tokens:.2f}")
