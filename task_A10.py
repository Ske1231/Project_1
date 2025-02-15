import sqlite3

# Connect to the SQLite database
db_path = "C:/data/ticket-sales.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query to calculate total sales for "Gold" tickets
cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type='Gold'")
total_sales = cursor.fetchone()[0]  # Fetch the result

# Save result to file
output_path = "C:/data/ticket-sales-gold.txt"
with open(output_path, "w", encoding="utf-8") as file:
    file.write(str(total_sales))

# Print result
print(f"✅ Total sales for Gold tickets: {total_sales}")

# Close the database connection
conn.close()
