import sqlite3

# Connect to the database file (it will be created if it doesn't exist)
connection = sqlite3.connect('database.db')

# Open the schema file and execute the SQL commands
with open('schema.sql', encoding='utf-8') as f:
    connection.executescript(f.read())

# Close the connection
connection.close()
print("Database initialized successfully.")
