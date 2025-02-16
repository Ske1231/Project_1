import sqlite3

db_path = r"C:\data\ticket-sales.db"
output_file = r"C:\data\ticket-sales-report.txt"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = "SELECT SUM(units * price) FROM tickets WHERE type='Gold';"
cursor.execute(query)
result = cursor.fetchone()[0]

with open(output_file, "w") as f:
    f.write(str(result))

print(f"✅ Report saved: {output_file}")
conn.close()
