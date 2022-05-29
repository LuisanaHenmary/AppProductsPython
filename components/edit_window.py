import tkinter as tkr
import sys
sys.path.insert(1,"..")
from components.field import FieldEdit
from components.submit_button import SubmitButton
from utils.funtions import validation

class EditWindow(tkr.Toplevel):
    #This class is for creating an object that serves as a component for the application.
    """
        It is a popup window used to edit the records.

        __id: It is to store the ID of the record.
        __old_name: It is to store the old name of the product.
        __old_price: It is to store the old price of the product.
        __new_name: It is to store the new name of the product.
        __new_price: It is to store the new price of the product.
        __message: It is a component that warns that both fields are required.
    """

    def __init__(self, id, old_name, old_price, edit_command):
        """
            Initializes the object and places it in the grid.

            self: It is to access any attribute or method of the class.
            id: Receive an integer that is the ID of the record.
            old_name: Receive the old name of the product.
            old_price: Receive the old price of the product.
            edit_command: Receive a function that is used for product edition.
        """

        #Overload the parent constructor.
        super().__init__()
        #Window title.
        self.title("Edit Product")
        #Record ID.
        self.__id = id
        #Old name.
        self.__old_name = old_name
        #Old price.
        self.__old_price = old_price

        #New name.
        self.__new_name = FieldEdit(
            self,
            name = "name",
            old_value = old_name,
            i = 0,
            j = 1
        )

        #New price.
        self.__new_price = FieldEdit(
            self,
            name = "price",
            old_value = old_price,
            i = 2,
            j = 1
        )

        #Prevent the window from being resized.
        self.resizable(False, False)

        self.__message = tkr.Label(self ,text = "", fg = "red")

        #Location of the warning.
        self.__message.grid(
            row = 4,
            columnspan = 2,
            sticky = tkr.W + tkr.E
        )

        #Submit button.
        SubmitButton(
            container = self,
            text = "Save Product",
            i = 5,
            spancol = 3,
            command = lambda: self.edit_record(update_function = edit_command)
        )       
        
    def edit_record(self, update_function):
        """
            Execute a function that updates a record where ID is equal to ID
            of one of the records of the product table.

            self: It is to access any attribute or method of the class.
            update_function: Receive a function that is used to update the records.
        """

        #First check if the fields are filled.
        if validation(self.__new_name.get_value(), self.__new_price.get_value()):
            #Run the function.
            update_function((
                self.__new_name.get_value(),
                self.__new_price.get_value(),
                self.__id
            ))
            #Close the mini-window.
            self.destroy()
        else:
            #Warn if one or both fields are empty.
            self.__message['text'] = f"Name and Price are requerid"

    



