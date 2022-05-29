import tkinter as tkr
from components.root import Root
from utils.funtions import run_query, validation
from components.field import Field
from components.tree import Tree
from components.edit_window import EditWindow
from components.panel import Panel
from components.message import Message
from components.submit_button import SubmitButton

class App(tkr.LabelFrame):

    """
        It is the application already built.

        __name: It is the field to store the name of the product.
        __price: It is the field to store the price of the product.
        __message: It is to update the message.
        __tree: It is the board with the records.
    """

    def __init__(self, container):


        """
            Initialize the application.

            self: It is to access any attribute or method of the class.
            container: container: receives a widget object that is the
            container of everything, which will be the Root component.
        """

        #Overload the parent constructor.
        super().__init__(container, text = "Add a new product")

        #Location in the container
        super().grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = 5)

        #Field for the product name.
        self.__name = Field(self,"Name",1,0,True)

        #Field for product price.
        self.__price = Field(self,"Price",2,0)

        #Warning message.
        self.__message = Message()
        
        #Button to save the records.
        SubmitButton(
            container = self,
            text = "Save Product",
            i = 3, spancol = 2,
            command = self.add_product
        )
        
        #Board with the records.
        self.__tree = Tree( i = 4, j = 0)

        #Button to delete and edit.
        Panel(
            delete_command = self.delete_product,
            edit_command = self.edit_product
        )

        #The board with the updated records.
        self.__tree.get_products()

    def add_product(self):
        """
            It is the function that is executed when pressing the save button, it makes the query
            to add a new record to the dashboard.

            self: It is to access any attribute or method of the class.
        """

        #First check if the fields are filled.
        if validation(self.__name.get_value(), self.__price.get_value()):
            #Run the query.
            query = "INSERT INTO product VALUES(null,?,?)"
            run_query(
                query = query,
                parameters = (self.__name.get_value(), self.__price.get_value())
            )
           #The message that the query was successful is given.
            self.__message['text'] = f"Product {self.__name.get_value()} added successfully"
           #The fields are reset, so that they are empty again.
            self.__name.reboot()
            self.__price.reboot()
        else:
            #The message is given that both fields are required.
            self.__message['text'] = f"Name and Price are requerid"
        
        #Dashboard is updated.
        self.__tree.get_products()


    def delete_product(self):
        """
            It is the function that is executed when pressing the delete button, it makes the query
            to delete a selected record on the board.

            self: It is to access any attribute or method of the class.
        """

        self.__message['text'] = ""

        try:
            #Check if there is a record selected.
            self.__tree.item(self.__tree.selection())['values'][0]
        except IndexError as e:
            #The message is given that it is required to select a record.
            self.__message['text'] = "Please Select a Record"
            return
        
        self.__message['text'] = ""
        
        #Get the ID of the product, for the selected record.
        id = self.__tree.item(self.__tree.selection())['values'][0]
        #Get the name of the product, for the selected record.
        name_product = self.__tree.item(self.__tree.selection())['values'][1]
        #Run the query.
        query = "DELETE FROM product WHERE id= ?"
        run_query(query = query, parameters=(id,))
        #The message that the query was successful is given.
        self.__message['text'] = f"Record {name_product} deleted successfully"
        #Dashboard is updated.
        self.__tree.get_products()
        
    def edit_record(self, update_parameters=()):
        """
            Makes the query to update a record in the product table.

            self: It is to access any attribute or method of the class.
            update_parameters: Receive a tuple with the parameters to update
            (new_name, new_price, id).
        """

        #Run the query.
        query = "UPDATE product set name = ?, price = ? WHERE id= ?"
        run_query(query = query, parameters = update_parameters)
        #The message that the query was successful is given.
        self.__message['text'] = "Update successfully"
        #Dashboard is updated.
        self.__tree.get_products()

    def edit_product(self):
        """
            It is the function that is executed when pressing the edit
            button, it opens a small window where the new values ​​will be entered.

            self: It is to access any attribute or method of the class.
        """
        self.__message['text'] = ""

        try:
            #Check if there is a record selected.
            self.__tree.item(self.__tree.selection())['values'][0]
        except IndexError as e:
            #The message is given that it is required to select a record.
            self.__message['text'] = "Please Select a Record"
            return
        self.__message['text'] = ""
        
        #Get the product ID of the selected record.
        id = self.__tree.item(self.__tree.selection())['values'][0]

        #Get the product name of the selected record.
        name_product = self.__tree.item(self.__tree.selection())['values'][1]
        #Get the price of the product of the selected record.
        price_product = self.__tree.item(self.__tree.selection())['values'][2]
       # The pop-up window opens, to enter the new values
        EditWindow(
            id = id,
            old_name = name_product,
            old_price= price_product,
            edit_command = self.edit_record
        )
        
    
#This is where the app runs
if __name__ == "__main__":
    window = Root()
    app = App(window)
    window.mainloop()