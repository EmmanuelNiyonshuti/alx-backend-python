import sqlite3

# Create a file-based SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create the `user_data` table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# Insert some test users
users = [
    ("Alice", 25),
    ("Bob", 42),
    ("Charlie", 38),
    ("Diana", 45),
    ("Eve", 29),
    ("John", 50)
]

cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
conn.commit()

print("Database created and users inserted.")
conn.close()
