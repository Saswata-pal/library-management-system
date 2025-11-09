import sqlite3

# Connect to the database
conn = sqlite3.connect('storebook.db')
cursor = conn.cursor()

# Execute the PRAGMA command
cursor.execute("PRAGMA table_info(stbook)")

# Fetch and print the results
table_info = cursor.fetchall()
for column in table_info:
    print(column)

# Close the connection
conn.close()
