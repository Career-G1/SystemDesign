"""Show how a lagging replica can violate read-after-write."""

primary: dict[str, str] = {}
replica: dict[str, str] = {}

primary["order-1"] = "paid"
print("write primary: order-1=paid")
print("immediate replica read:", replica.get("order-1", "<stale/missing>"))

replica.update(primary)
print("after replication:", replica["order-1"])
print("lesson: route read-after-write traffic to the primary or use a session token.")
