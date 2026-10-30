"""Use access patterns to make a small data-store decision."""

patterns = {
    "ownership_transaction": "relational",
    "hot_profile_lookup": "key-value/cache",
    "flexible_activity_document": "document",
}
for access_pattern, store in patterns.items():
    print(f"{access_pattern:28} -> {store}")
print("rule: choose from access patterns, consistency, relationships, and operations.")
