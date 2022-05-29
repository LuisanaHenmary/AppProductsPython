import tkinter as tkr

class Panel:
    #This class is for creating an object that serves as a component for the application.
    """
        Shows the buttons to delete and edit.
    """
    
    def __init__(self, delete_command, edit_command):
        """
            Initializes the object and places it in the grid.

             self: It is to access any attribute or method of the class.
             delete_command: Receive a function that is executed when pressing the delete button.
             edit_command: Receive a function that is executed when pressing the edit button.
        """

       #Delete button.
        tkr.Button(
            text = "DELETE",
            command = delete_command
        ).grid(
            row = 5,
            column = 0,
            sticky = tkr.W + tkr.E
        )

        #Edit button.
        tkr.Button(
            text = "EDIT",
            command = edit_command
        ).grid(
            row = 5,
            column = 1,
            sticky = tkr.W + tkr.E
        )