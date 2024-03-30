from Name import Name
from GUIBuilder import GuiApp
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Names Database")
    app = GuiApp(root)
    app.run()



if __name__ == "__main__":
    main()
