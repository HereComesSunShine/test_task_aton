import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Fetch some records from the users table
c.execute("SELECT * FROM users LIMIT 5")
users = c.fetchall()
print("Users:")
for user in users:
    print(user)
    # Fetch clients associated with the current user
    c.execute("SELECT * FROM clients WHERE Manager = ?", (user[1],))
    clients = c.fetchall()
    print("Clients for", user[1])
    for client in clients:
        print(client)

# Close the connection
conn.close()
