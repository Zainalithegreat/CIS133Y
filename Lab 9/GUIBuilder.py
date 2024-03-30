import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from Database import Database
from Name import Name

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "GUI.ui"


class GuiApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: ttk.Frame = builder.get_object("Main", master)
        builder.connect_callbacks(self)
        self.Search = builder.get_object('Entry', master)
        self.treeview = builder.get_object('treeView', master)
        self.checked = builder.get_variable("CheckBox")
        self.setup_tree()

    def setup_tree(self):
        tree = self.treeview

        tree.configure(columns=(0, 1, 2, 3, 4), displaycolumns=(0, 1, 2, 3, 4))

    def Toggle(self):
        if self.checked.get() == "1":
            gender = "M"
        else:
            gender = "F"
        return gender

    def displayContents(self):
        name = self.Search.get()
        gender = self.Toggle()

        for i in self.treeview.get_children():
            self.treeview.delete(i)
        rows = Name.read_name(name, gender)
        count = 1
        for row in rows:
            self.treeview.insert("", "end", values=(count, row.get_name(), row.get_year(), row.get_gender(), row.get_count()))
            count += 1
    def run(self):
        self.mainwindow.mainloop()


