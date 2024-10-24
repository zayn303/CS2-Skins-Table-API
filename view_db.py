import sqlite3

# Specify the path to your database file
db_path = "cs2_skins.db"

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# Fetch all table names in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:", tables)

cursor.execute("SELECT * FROM cs2_skins;")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
