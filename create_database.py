import sqlite3

"""
    This file creates a database and a
    table called product, with its fields. only
    you need to run it once.
"""

#If the database is not created, but if it exists, it makes the connection.
Connection = sqlite3.connect("./utils/database.db") 

cursor = Connection.cursor()

#Try to create the table, only fails if the table already exists.
try:
    cursor.execute("""
        CREATE TABLE product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            price FLOAT NOT NULL
        )
    """)

except Exception as e:
    print(f"{type(e).__name__}: {e}")
    

#close the connection.
Connection.close()