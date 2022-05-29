import tkinter as tkr

class SubmitButton(tkr.Button):
     #This class is for creating an object that serves as a component for the application.
    """
        It is a button to send the data.
    """
    def __init__(self, container, text, command, spancol, i):
        """
            Inicializa el objecto y lo ubica.
            
            self: It is to access any attribute or method of the class.
            container: Receives a widget object that is the container for everything.
            text: Receive a string indicating the function of the button.
            command: Receive a function that is executed when pressed.
            spancol: Receives an integer that determines how many columns the button can occupy.
            i: Receives an integer that is the row in which it is located in the grid.
        """
        #Overload the parent constructor.
        super().__init__(container, text = text, command = command)
        #Location in the grid.
        self.grid(row = i, columnspan = spancol, sticky = tkr.W + tkr.E)

