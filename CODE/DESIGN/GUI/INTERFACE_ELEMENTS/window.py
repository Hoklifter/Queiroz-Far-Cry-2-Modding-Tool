import tkinter as tk
import os


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        iconpng_path = os.path.normpath("CODE/DESIGN/GUI/icons/icon256x256.png")
        iconpng = tk.PhotoImage(file=iconpng_path)

        self.title("Queiroz's Far Cry 2 Modding Tool")
        self.geometry("800x600")
        self.resizable(False, False)
        self.iconphoto(False, iconpng)

    def update_geometry(self):
        from ....fc2moddingtool import FC2ModdingTool
        GUI = FC2ModdingTool.gui
        if GUI.mode == 'table':
            self.geometry("800x600")
        elif GUI.mode == 'sheet':
            self.geometry("1200x600")