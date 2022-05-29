import tkinter as tkr

class Message(tkr.Label):
    #This class is for creating an object that serves as a component for the application.
    """
        It is to show a message if it was done or not
        an action.
    """
    def __init__(self):
        """
            Initializes the object and places it in the grid.

             self: It is to access any attribute or method of the class.
        """
        #Overload the parent constructor.
        super().__init__(text = "", fg = "red")
        #Location on the grid.
        self.grid(row = 3, column = 0, columnspan = 2, sticky = tkr.W + tkr.E)