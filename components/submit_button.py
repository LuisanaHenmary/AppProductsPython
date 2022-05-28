import tkinter as tkr

class SubmitButton(tkr.Button):
     #Esta clase es para crear un objecto que sirve como componente para la aplicacion
    """
        Es un boton para enviar los datos.
    """
    def __init__(self, container, text, command, spancol, i):
        """
            Inicializa el objecto y lo ubica.
            
            self: Es para acceder a cualquier atributo o metodo de la clase.
            container: Contenedor del campo.
            text: Texto del boton.
            command: Funcion que se ejecuta al presinarlo.
            spancol: Es para determinar cuantas columnas puede ocupar.
            i: Fila en que se en la grilla.
        """
        super().__init__(container, text = text, command = command)
        #Ubicacion en la grilla
        self.grid(row = i, columnspan = spancol, sticky = tkr.W + tkr.E)

