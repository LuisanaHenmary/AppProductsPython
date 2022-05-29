import sqlite3 as sql3

"""They are functions that are used in different modules."""

def run_query(query, parameters = ()):
    """
        It is to execute a query against the database.
        
        query: Receives a string that is the query.
        parameters: Receive a tuple with the parameters for the query.
    """

    #Connect to the database
    with sql3.connect('./utils/database.db') as Connection: 
        cursor = Connection.cursor()
        #Run the query
        result = cursor.execute(query, parameters)
        #confirm the query, to make it permanent
        Connection.commit()
        return result

def validation(field1, field2):
    """
         Validates if one or both fields are empty.

        field1: Receives the value of the first field.
        field2: Receives the value of the second field.
    """
        
    return len(field1) > 0 and len(field2) > 0