from itertools import tee
import tkinter as tkr

class Field:
    #Esta clase es para crear un objecto que sirve como componente para la aplicacion
    """
        Es un campo de texto con su propia etiqueta
        __value: Es el valor del campo de texto.
    """
    __value = 0

    def __init__(self, containe, name, i, j, focus=False):
        """
            Inicializa el objecto y lo ubica
        """

        #La etiqueta
        tkr.Label(containe, text = name).grid(row = i, column = j)
        #El campo de texto
        self.__value = tkr.Entry(containe)
        if(focus):
            self.__value.focus()
        #ubicacion en la grilla
        self.__value.grid(row = i, column = j + 1)
        

    def get_value(self):
        """
            Devuelve el valor que se ingreso en el
            campo de texto
        """
        return self.__value.get()

    def get_length(self):
        """
            Devuelve la longitud fel valor que se 
            ingreso en el campo de texto
        """
        return len(self.__value.get())

    def reboot(self):
        """
            Reinicia el campo de texto a una cadena vacia
        """
        self.__value.delete(0,tkr.END)

class FieldEdit:
    #Esta clase es para crear un objecto que sirve como componente para la aplicacion
    """
        Es un campo que muestra el viejo valor de un producto
        y tiene un campo de texto para ingresar un nuevo valor
        __new_value: Representa el nuevo valor que se ingresa.
    """

    def __init__(self, containe, name, old_value, i, j):
        """
            Inicializa el objecto y lo ubica
        """
        #La etiqueta
        tkr.Label(containe, text = name).grid(row = i, column = j)

        #Un indicador de viejo valor
        tkr.Entry(
            containe,
            text = f"Old {name}",
            textvariable = tkr.StringVar(containe, value = old_value),
            state = 'readonly' 
        ).grid(row = i, column = j + 1)

        #Campo de texto para ingresar el nuevo valor
        self.__new_value = Field(containe = containe, name = f"New {name}", i = i + 1, j = j)

    def get_value(self):
        """
            Devuelve el valor que se ingreso en el
            campo de texto
        """
        return self.__new_value.get_value()

    def get_length(self):
        """
            Devuelve la longitud fel valor que se 
            ingreso en el campo de texto
        """
        return self.__new_value.get_length()