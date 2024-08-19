import tkinter as tk
from tkinter import filedialog

from ..utils import (
    _unpack, _pack, _pack_current, _open_xml, _save_xml
)

class FileCascade(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, tearoff=False)
        self.add_command(label="Unpack .FAT/.DAT...", command=_unpack)
        self.add_separator()
        self.add_command(label="Pack...", command=_pack)
        self.add_command(label="Pack Current", command=_pack_current)
        self.add_separator()
        self.add_command(label="Open XML...", command=_open_xml)
        self.add_command(label="Save XML...", command=_save_xml)
        self.add_separator()
        self.add_command(label="Exit", command=quit)
        self.master.add_cascade(label="File", menu=self)



class Menubar(tk.Menu): 
    def __init__(self, master):
        tk.Menu.__init__(self, master, bd=0)
        self.file = FileCascade(self)

        self.add_command(label="Help", command=None)
        self.add_command(label="About", command=None)

        self.master.config(menu=self)
