import pathlib
import tkinter as tk
import pygubu
import tkinter.ttk as ttk
import os

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = os.path.join(PROJECT_PATH, "about.ui")


class AboutApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: ttk.Frame = builder.get_object("main", master)
        builder.connect_callbacks(self)
        self.parent = master
        self.top_frame = tk.Frame(self.parent)

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.mainwindow

    def run(self):
        self.mainwindow.mainloop()



