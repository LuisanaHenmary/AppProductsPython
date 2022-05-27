import tkinter as tkr

class Message(tkr.Label):
    #Esta clase es para crear un objecto que sirve como componente para la aplicacion
    """
        Es para mostrar un mensaje si se hizo
        una accion
    """
    def __init__(self):
        """
            Inicializa el objecto y lo ubica
        """
        super().__init__(text = "", fg = "red")
        #Ubicacion en la grilla
        self.grid(row = 3, column = 0, columnspan = 2, sticky = tkr.W + tkr.E)