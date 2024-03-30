import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import os
import pathlib

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = os.path.join(PROJECT_PATH, "sample.ui")
ANSWER_UI = os.path.join(PROJECT_PATH, "answer.ui")

class NewprojectApp:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.main_window: ttk.Frame = builder.get_object("topLevel", master)
        builder.connect_callbacks(self)
        self.bitcoin_input = builder.get_object('Input', master)
        self.builders = []

    def calculate(self):
        try:
            bitcoin_input = float(self.bitcoin_input.get())
            total = 72126 * bitcoin_input
            answer_window = tk.Toplevel(self.main_window)
            self.show_answer(answer_window, f"Total bitcoin in USD: {total}$\n\n")
        except ValueError:
            answer_window = tk.Toplevel(self.main_window)
            self.show_answer(answer_window, "There was an error outputting, please input a number\n\n")

    def clear(self):
        self.bitcoin_input.delete(0, tk.END)

    def show_answer(self, master, text):
        builder = pygubu.Builder()
        self.builders.append(builder)
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(ANSWER_UI)
        self.answer_window: ttk.Frame = builder.get_object("main", master)
        message = builder.get_variable('text')
        message.set(text)

    def get_top_frame(self):
        return self.main_window

    def run(self):
        self.main_window.mainloop()
