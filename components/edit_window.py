import tkinter as tkr
import sys
sys.path.insert(1,"..")
from components.field import FieldEdit
from components.submit_button import SubmitButton

class EditWindow(tkr.Toplevel):
    #Esta clase es para crear un objecto que sirve como componente para la aplicacion
    """
        Es la ventana emergente que se usa para editar los registros.

        __old_name: Es para almacenar el viejo nombre del producto.
        __old_price: Es para almacenar el viejo precio del producto.
        __new_name: Es para almacenar el nuevo nombre del producto.
        __new_price: Es para almacenar el nuevo precio del producto.
        __message: Es un componente que advierte que se requiere ambos campos.
    """

    def __init__(self, old_name, old_price, edit_command):
        """
            Inicializa el objecto y lo ubica en la grilla.

            self: Es para acceder a cualquier atributo o metodo de la clase.
            old_name: Recive el viejo nombre del producto.
            old_price: Recive el viejo precio del producto.
            edit_command: Recive una funcion que sirve para la edicion de producto
        """

        super().__init__()
        self.title("Edit Product")
        self.__old_name = old_name
        self.__old_price = old_price

        self.__new_name = FieldEdit(
            self,
            name = "name",
            old_value = old_name,
            i = 0,
            j = 1
        )

        self.__new_price = FieldEdit(
            self,
            name = "price",
            old_value = old_price,
            i = 2,
            j = 1
        )

        #Evita que se cambie el tamaño de la ventana
        self.resizable(False, False)

        self.__message = tkr.Label(self ,text = "", fg = "red")

        #Ubicacion de la advertencia
        self.__message.grid(
            row = 4,
            columnspan = 2,
            sticky = tkr.W + tkr.E
        )

        #Boton de envio
        SubmitButton(
            container = self,
            text = "Save Product",
            i = 5,
            spancol = 3,
            command = lambda: self.edit_record(update_function = edit_command)
        )

    def validation(self):
        """
            Valida si ambos campos estan vacios o no.

            self: Es para acceder a cualquier atributo o metodo de la clase.
        """

        if(self.__new_name.get_length() > 0 and self.__new_price.get_length() > 0):
            return True
        return False
        
    def edit_record(self, update_function):
        """
            Ejecuta una funcion que actualiza un registro donde el viejo nombre
            y el viejo precio sean iguales a uno de los registros de la tabla

            self: Es para acceder a cualquier atributo o metodo de la clase.
            update_function: Es una funcion que se usa para la actualizacion.
        """

        #Primero verifica si los campos estan llenos
        if self.validation():
            #Ejecuta la funcion
            update_function((
                self.__new_name.get_value(),
                self.__new_price.get_value(),
                self.__old_name,
                self.__old_price
            ))
            #Se cierra la ventana
            self.destroy()
        else:
            #Avisa si un (o ambos) campo(s) esta(n) vacio(s)
            self.__message['text'] = f"Name and Price are requerid"

    



