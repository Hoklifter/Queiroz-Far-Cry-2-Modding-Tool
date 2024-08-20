import tkinter as tk
import os


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        os_name = os.name
        if os_name == 'posix':
            iconpng = "CODE/DESIGN/GUI/icons/icon256x256.png"
        elif os_name == 'nt':
            iconpng = "CODE\\DESIGN\\GUI\\icons\\icon256x256.png"
        iconpng = os.path.realpath(iconpng)
        iconpng = tk.PhotoImage(file=iconpng)

        self.title("Far Cry 2 Modding Tool")
        self.geometry("800x600")
        self.resizable(False, False)
        self.iconphoto(False, iconpng)