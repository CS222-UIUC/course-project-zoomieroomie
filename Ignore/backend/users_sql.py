
#####NOT NECESSARY######

"""Creating users SQLite database"""
import sqlite3

conn = sqlite3.connect("backend/users.sql")

conn.execute("""DROP TABLE users;""")
conn.execute(
    """
    CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);
    """
)

#test-----------------------------------
conn.execute(
    """INSERT INTO users (username, password) VALUES ('ayush', 'sharma');"""
)

# execute a query
cursor = conn.execute('SELECT * FROM users')

# fetch the results
results = cursor.fetchall()

# print the results
for row in results:
    print(row)