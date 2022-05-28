import sqlite3 as sql3

def run_query(query, parameters = ()):
    """
        Es para ejecutar una consulta para la base de datos
    """

    #Conectar a la base de datos
    with sql3.connect('./utils/database.db') as conn: 
        cursor = conn.cursor()
        #Ejecutar la consulta
        result = cursor.execute(query, parameters)
        #confirmar
        conn.commit()
        return result