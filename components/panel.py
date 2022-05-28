import tkinter as tkr

class Panel:
    #Esta clase es para crear un objecto que sirve como componente para la aplicacion
    """
        Muestra los botones para borrar y editar.
    """
    
    def __init__(self, delete_command, edit_command):
        """
            Inicializa el objecto y lo ubica en la grilla.

             self: Es para acceder a cualquier atributo o metodo de la clase.
             delete_command: Una funcion que sirve para el boton de borrado.
             edit_command: Una funcion que sirve para el boton de editar.
        """

        #Boton de borrar
        tkr.Button(
            text = "DELETE",
            command = delete_command
        ).grid(
            row = 5,
            column = 0,
            sticky = tkr.W + tkr.E
        )

        #Boton de editar
        tkr.Button(
            text = "EDIT",
            command = edit_command
        ).grid(
            row = 5,
            column = 1,
            sticky = tkr.W + tkr.E
        )