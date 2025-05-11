import sqlite3

DB_NAME = "mediadatabase.db"
COLUMN_NAME = "thumb_id"

# Connect to the database
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Check if 'thumb_id' column already exists
cursor.execute("PRAGMA table_info(media)")
columns = {col[1] for col in cursor.fetchall()}  # Use a set for faster lookup

if COLUMN_NAME not in columns:
    cursor.execute(f"ALTER TABLE media ADD COLUMN {COLUMN_NAME} TEXT")
    conn.commit()
    print(f"✅ Successfully added '{COLUMN_NAME}' column!")
else:
    print(f"⚠️ Column '{COLUMN_NAME}' already exists.")

# Display the updated table schema
cursor.execute("PRAGMA table_info(media)")
print("📌 Current Table Schema:")
for col in cursor.fetchall():
    print(col)

# Close the connection
conn.close()
