import sqlite3
import os

db_path = 'backend/db.sqlite3'

# Check if the file exists
if not os.path.exists(db_path):
    print(f"❌ Database file not found at: {db_path}")
    exit()

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Loop through each table and print its contents
for table in tables:
    table_name = table[0]
    print(f"\n📌 Table: {table_name}")
    
    try:
        # Print columns
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = [col[1] for col in cursor.fetchall()]
        print("Columns:", columns)

        # Print data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error reading table {table_name}: {e}")

# Close the connection
conn.close()


