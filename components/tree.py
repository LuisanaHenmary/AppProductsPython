from tkinter import ttk
import tkinter as tkr
import sys
sys.path.insert(1,"..")
from utils.funtions import run_query


class Tree(ttk.Treeview):
    #This class is for creating an object that serves as a component for the application.
    """
        It is a dashboard where it shows the current records of the product table.
    """

    def __init__(self, i, j):
        """
            Initializes the object and places it in the grid.

            self: It is to access any attribute or method of the class.
            i: Receives an integer that is the row in which it is located in the grid.
            j: Receives an integer that is the column in which it is located in the grid.
        """

        #Overload the parent constructor, determining the height and the number of columns
        #three in this case.
        super().__init__(height=15,columns = [f"#{n}" for n in range(1, 4)])

        #It is configured to show the headers.
        self.config(show='headings')
        #Location in the grid.
        self.grid(row = i, column = j, columnspan=2)

        #The heads are printed.
        self.heading('#1', text='ID', anchor = tkr.CENTER)
        self.heading('#2', text='Name', anchor = tkr.CENTER)
        self.heading('#3', text='Price',anchor = tkr.CENTER)

    def get_products(self):
        """
            Update the table according to the current records of
            the product table in the database.

            self: It is to access any attribute or method of the class.
        """

        #Get the old records.
        records = self.get_children() 

        #Removes them
        for element in records:
            self.delete(element)

        #Run the query.
        query = "SELECT * FROM product ORDER BY name DESC"
        db_rows = run_query(query = query)

        #Insert the current records into the board.
        for row in db_rows:
            self.insert('', tkr.END, values=row)


