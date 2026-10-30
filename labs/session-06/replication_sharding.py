"""Demonstrate replica lag and deterministic tenant routing."""

tenants = {"acme": "shard-a", "globex": "shard-b"}
primary = {"acme": ["event-1"], "globex": []}
replica = {"acme": [], "globex": []}

primary["acme"].append("event-2")
print("primary:", primary["acme"])
print("replica before catch-up:", replica["acme"])
replica["acme"] = list(primary["acme"])
print("replica after catch-up:", replica["acme"])
print("tenant routing:", tenants)
