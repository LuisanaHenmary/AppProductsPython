import tkinter as tkr
from components.root import Root
from utils.database import run_query
from components.field import Field
from components.tree import Tree
from components.edit_window import EditWindow
from components.panel import Panel
from components.message import Message
from components.submit_button import SubmitButton

class App(tkr.LabelFrame):

    """
        Es la aplicacion ya armada.

        __name: Es el campo para guardar el nombre del producto.
        __price: Es el campo para guardar el precio del producto.
        __message: Es para ir actualizando el componente mensaje.
        __tree: Es el tablero con los registros.
    """

    def __init__(self, container):
        super().__init__(container, text = "Add a new product")
        super().grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = 5)

        #Campo para el nombre del producto
        self.__name = Field(self,"Name",1,0,True)

        #Campo para el nombre del producto
        self.__price = Field(self,"Price",2,0)

        #Mensaje de aviso
        self.__message = Message()
        
        #Boton para guardar regitros
        SubmitButton(container = self, text = "Save Product", i = 3, spancol = 2, command = self.add_product)
        
        #Tablero con los registros
        self.__tree = Tree(field_name=["Name","Price"], i = 4, j = 0)

        #Boton de borrar y editar
        Panel(delete_command = self.delete_product, edit_command = self.edit_product)

        #Da el tablero de registros actualizado
        self.__tree.get_products()

    def validation(self):

        """
            Valida si ambos campos estan vacios o no.

            self: Es para acceder a cualquier atributo o metodo de la clase.
        """

        return self.__name.get_length() > 0 and self.__price.get_length() > 0 

    def add_product(self):
        """
            Es lo que se ejecuta al presionar el boton de guarsar, hace la consulta
            para agregar un nuevo registro en el tablero.

            self: Es para acceder a cualquier atributo o metodo de la clase.
        """

        #Primero verifica si los campos estan llenos
        if self.validation():
            #Se hace la consulta
            query = "INSERT INTO product VALUES(null,?,?)"
            run_query(query = query, parameters = (self.__name.get_value(), self.__price.get_value()))
            #Se da el mensaje que la consulta fue exitosa
            self.__message['text'] = f"Product {self.__name.get_value()} added successfully"
            #Se reinicia los campos, para que vuelvan ser vacios
            self.__name.reboot()
            self.__price.reboot()
        else:
            #Se da el mensaje que se requiere ambos campos
            self.__message['text'] = f"Name and Price are requerid"
        
        #Da el tablero de registros actualizado
        self.__tree.get_products()


    def delete_product(self):
        """
            Es lo que se ejecuta al presionar el boton de borrar, hace la consulta
            para borrar un registro seleccionado en el tablero.

            self: Es para acceder a cualquier atributo o metodo de la clase.
        """

        self.__message['text'] = ""

        try:
            #Verifica si hay un record seleccionado
            self.__tree.item(self.__tree.selection())['text'][0]
        except IndexError as e:
            #Se da el mensaje que se requiere seleccionar un record
            self.__message['text'] = "Please Select a Record"
            return
        
        self.__message['text'] = ""
        #Obtiene el nombre del producto, por el record seleccionado
        name_product = self.__tree.item(self.__tree.selection())['text']
        #Se hace la consulta
        query = "DELETE FROM product WHERE name= ?"
        run_query(query = query, parameters=(name_product,))
        #Se da el mensaje que la consulta fue exitosa
        self.__message['text'] = f"Record {name_product} deleted successfully"
        #Da el tablero de registros actualizado
        self.__tree.get_products()
        
    def edit_record(self, update_parameters=()):
        """
            Hace la consulta para actulizar un registro seleccionado
            en el tablero.

            self: Es para acceder a cualquier atributo o metodo de la clase.
            update_parameters: Es una tupla con los parametros para actualizar
            (nombre_nuevo, precio_nuevo, nombre_viejo, precio_viejo).
        """

        #Se hace la consulta
        query = "UPDATE product set name = ?, price = ? WHERE name = ? AND price = ?"
        run_query(query = query, parameters = update_parameters)
        #Se da el mensaje que la consulta fue exitosa
        self.__message['text'] = "Update successfully"
        #Da el tablero de registros actualizado
        self.__tree.get_products()

    def edit_product(self):
        """
             Es lo que se ejecuta al presionar el boton de editar.

            self: Es para acceder a cualquier atributo o metodo de la clase.
        """
        self.__message['text'] = ""

        try:
            #Verifica si hay un record seleccionado
            self.__tree.item(self.__tree.selection())['text'][0]
        except IndexError as e:
            #Se da el mensaje que se requiere seleccionar un record
            self.__message['text'] = "Please Select a Record"
            return
        self.__message['text'] = ""
        
        #Obtiene el nombre del producto, por el record seleccionado
        name_product = self.__tree.item(self.__tree.selection())['text']
        #Obtiene el nombre del precio, por el record seleccionado
        price_product = self.__tree.item(self.__tree.selection())['values'][0]
        #Se abre la ventana emergente, para ingresar los nuevos valores
        EditWindow(name_product, price_product, edit_command = self.edit_record)
        
    
#Aqui se ejecuta la app
if __name__ == "__main__":
    window = Root()
    app = App(window)
    window.mainloop()