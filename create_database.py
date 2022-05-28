import sqlite3

"""
    Este archivo crea una base de datos y una
    tabla llamada product, con sus campos. solo
    es necesario ejecutarlo una vez.
"""

#Si en utils no existe la base de datos la crea
#Pero si existe hace la conexion.
conexion = sqlite3.connect("./utils/database.db") 

cursor = conexion.cursor()

#Trata de crear la tabla, solo falla si la tabla
#existe.
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
    


conexion.close()