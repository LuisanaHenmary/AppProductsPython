from tkinter import ttk
import tkinter as tkr
import sys
sys.path.insert(1,"..")
from utils.database import run_query


class Tree(ttk.Treeview):
    #Esta clase es para crear un objecto que sirve como componente para la aplicacion
    """
        Es una tablero donde muestra los registros actuales de la tabla product.
    """

    def __init__(self, field_name, i, j):
        """
            Inicializa el objecto y lo ubica.

            self: Es para acceder a cualquier atributo o metodo de la clase.
            field_name: Lista con los nombres de los campos.
            i: Fila en que se ubica en la grilla
            j: Columna en que se ubica en la grilla
        """

        #Determina el alto y el numero de columnas
        super().__init__(height=10,columns=2)

        #Ubicacion en la grilla
        self.grid(row = i, column = j, columnspan = 2)

        #Se imprime los cabezales
        for index, field in enumerate(field_name):
            self.heading(f"#{index}", text = field, anchor = tkr.CENTER)

    def get_products(self):
        """
            Actualiza el tableto deacuerdo a los registros actuales de
            la tabla product en la base de datos
        """

        #Obtiene los antiguos registros
        records = self.get_children() 

        #Los elimina
        for element in records:
            self.delete(element)

        #Ejecuta la consulta
        query = "SELECT * FROM product ORDER BY name DESC"
        db_rows = run_query(query = query)

        #Inserta los actuales registros en el tablero
        for row in db_rows:
            self.insert('', 0, text = row[1], values = row[2])


