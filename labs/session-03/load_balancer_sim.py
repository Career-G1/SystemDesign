"""Route requests across healthy replicas and remove an unhealthy one."""

from itertools import cycle


replicas = {"api-1": True, "api-2": True}
requests = cycle(["api-1", "api-2"])

for index in range(6):
    if index == 3:
        replicas["api-2"] = False
        print("health check: api-2 unhealthy")
    while True:
        candidate = next(requests)
        if replicas[candidate]:
            print(f"request-{index + 1} -> {candidate}")
            break
