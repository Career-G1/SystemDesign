"""Compare an N+1 query pattern with a single joined query using SQLite."""

import sqlite3

db = sqlite3.connect(":memory:")
db.executescript(
    "create table users(id integer primary key, name text);"
    "create table orders(id integer primary key, user_id integer, total integer);"
    "insert into users values (1, 'A'), (2, 'B'), (3, 'C');"
    "insert into orders values (1, 1, 10), (2, 2, 20), (3, 3, 30);"
)

n_plus_one = 1
users = db.execute("select id, name from users").fetchall()
for user_id, _ in users:
    db.execute("select total from orders where user_id = ?", (user_id,)).fetchall()
    n_plus_one += 1

joined = db.execute(
    "select users.name, orders.total from users "
    "join orders on orders.user_id = users.id"
).fetchall()
print(f"n_plus_one_queries={n_plus_one} joined_queries=1 joined_rows={len(joined)}")
