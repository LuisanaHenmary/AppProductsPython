import sqlite3 as sql3

def run_query(query, parameters = ()):
    """
        Es para ejecutar una consulta para la base de datos.
        
        query: Una cadena que es la consulta para la base de datos.
        parameters: Una tupla con los parametros para la consulta.
    """

    #Conectar a la base de datos
    with sql3.connect('./utils/database.db') as conn: 
        cursor = conn.cursor()
        #Ejecutar la consulta
        result = cursor.execute(query, parameters)
        #confirmar
        conn.commit()
        return result