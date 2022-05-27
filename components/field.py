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

