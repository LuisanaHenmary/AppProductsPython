import tkinter as tkr

class Root(tkr.Tk):
    #Esta clase es para crear un objecto que sirve como componente para la aplicacion
    """
        Es la ventana principal.
    """
    def __init__(self):
        """
            Inicializa el objecto y lo ubica.

             self: Es para acceder a cualquier atributo o metodo de la clase.
        """
        super().__init__()
        super().title("Products Aplication") #Titulo para la aplicacion.
        self.resizable(False, False) #Para que no se ajuste el tamaño.