import tkinter as tkr

class Field:
    #This class is for creating an object that serves as a component for the application.
    """
        It is a text field, with its own label, used to enter a value.

        __value: It is the value of the text field.
    """
    __value = 0

    def __init__(self, container, name, i, j, focus=False):
        """
            Initializes the object and places it in the grid.

            self: It is to access any attribute or method of the class.
            container: Receives a widget object that is the container for everything.
            name: Receives a string that is the name of the field.
            i: Receives an integer that is the row in which it is located in the grid.
            j: Receives an integer that is the column in which it is located in the grid.
            focus: Receives a boolean that determines whether to start with focus.
        """

        #The label.
        tkr.Label(container, text = name).grid(row = i, column = j)
        #The text field.
        self.__value = tkr.Entry(container)
        if(focus):
            self.__value.focus()
        #Location in the grid.
        self.__value.grid(row = i, column = j + 1)
        

    def get_value(self):
        """
            Returns the value that was entered in the
            text field.

            self: It is to access any attribute or method of the class.
        """
        return self.__value.get()

    def reboot(self):
        """
            Resets the text field to an empty string.

            self: It is to access any attribute or method of the class.
        """
        self.__value.delete(0,tkr.END)


class FieldEdit:
    #This class is for creating an object that serves as a component for the application.
    """
        It is a field that shows the old value of a product
        and has a text field to enter a new value.

        __new_value: It is the new value that is entered.
    """

    def __init__(self, container, name, old_value, i, j):
        """
            Initializes the object and places it in the grid.

            self: It is to access any attribute or method of the class.
            container: Receives a widget object that is the container for everything.
            name: Receives a string that is the name of the field.
            old_value: Receive a string that is the old value.
            i: Receives an integer that is the row in which it is located in the grid.
            j: Receives an integer that is the column in which it is located in the grid.
        """
        #The label.
        tkr.Label(container, text = name).grid(row = i, column = j)

        #An old value indicator that is not altered.
        tkr.Entry(
            container,
            text = f"Old {name}",
            textvariable = tkr.StringVar(container, value = old_value),
            state = 'readonly' 
        ).grid(row = i, column = j + 1)

        # Text field to enter the new value.
        self.__new_value = Field(container = container, name = f"New {name}", i = i + 1, j = j)

    def get_value(self):
        """
            Returns the new value that was entered in the
            text field.

            self: It is to access any attribute or method of the class.
        """
        return self.__new_value.get_value()