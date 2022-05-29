import tkinter as tkr

class Root(tkr.Tk):
    #This class is for creating an object that serves as a component for the application.
    """
        It is the main window.
    """
    def __init__(self):
        """
            Initialize the object.

             self: It is to access any attribute or method of the class.
        """
        #Overload the parent constructor.
        super().__init__()
        #Title for the application.
        super().title("Products Aplication")
        #So that the size is not adjusted.
        self.resizable(False, False) 