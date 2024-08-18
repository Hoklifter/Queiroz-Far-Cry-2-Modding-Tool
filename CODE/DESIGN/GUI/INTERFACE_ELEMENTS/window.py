import tkinter as tk
import os


class Window(tk.Tk):
    def __init__(self, gui_instance):
        tk.Tk.__init__(self)
        if os.name == 'posix':
            iconpng = "..icons/icon256x256.png"
        elif os.name == 'nt':
            iconpng = "..\\icons\\icon256x256.png"
        iconpng = os.path.realpath(iconpng)
        iconpng = tk.PhotoImage(iconpng)

        self.gui_instance = gui_instance
        self.title("Far Cry 2 Modding Tool")
        self.geometry("800x600")
        self.resizable(False, False)
        self.iconphoto(False, iconpng)