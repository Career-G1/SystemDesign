"""Demonstrate an idempotency key returning one stored result."""

results: dict[str, dict[str, object]] = {}


def create_payment(key: str, amount: int) -> dict[str, object]:
    if key in results:
        return results[key]
    result = {"status": 201, "payment_id": "pay-1", "amount": amount}
    results[key] = result
    return result


print(create_payment("request-123", 500))
print(create_payment("request-123", 500))
print("same result:", create_payment("request-123", 500) == create_payment("request-123", 500))
