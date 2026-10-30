"""Simulate at-least-once delivery with idempotent consumer behavior."""

queue = [{"id": "m1", "job": "run-agent", "attempts": 0}]
completed: set[str] = set()

while queue:
    message = queue.pop(0)
    message["attempts"] += 1
    print(f"consume {message['id']} attempt={message['attempts']}")
    if message["id"] in completed:
        print("duplicate ignored")
        continue
    completed.add(message["id"])
    print("terminal result stored before acknowledgement")
    queue.append(message)
