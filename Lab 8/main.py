#******************************************************************************
# Author:           Zain Ali, Ben duChalard
# Lab:              Lab 8
# Date:             3/16/2024
# Description:      This program is a GUI program, it takes in the users bitcoin and converts them into dollars
#
# Input:            bitcoin_input
# Output:           total
# Sources:
#
#
#******************************************************************************


import tkinter as tk
import tkinter.ttk as ttk
from bitcoin import NewprojectApp
from about import AboutApp

class MainApp:
    def __init__(self, master):
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column=0, row=0, sticky='nsew')

        about_app = AboutApp(self.__main_notebook)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        bitcoin_input = NewprojectApp(self.__main_notebook)
        self.__main_notebook.add(bitcoin_input.get_top_frame(), text="Bitcoin Calculator")

    def run(self):
        self.__main_notebook.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bitcoin Calculator")
    app = MainApp(root)
    app.run()

