import sqlite3

conn = sqlite3.connect("shipping.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM cargo_vc"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()