import tkinter as tk
from tkinter import filedialog

from ..utils import (
    _unpack, _pack, _open_xml, _save_xml, set_viewmode, about, help
)

class FileCascade(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, tearoff=False)
        self.add_command(label="Unpack .FAT/.DAT...", command=_unpack)
        self.add_separator()
        self.add_command(label="Pack...", command=_pack)
        self.add_separator()
        self.add_command(label="Open XML...", command=_open_xml)
        self.add_command(label="Save XML", command=_save_xml)
        self.add_separator()
        self.add_command(label="Exit", command=quit)
        self.master.add_cascade(label="File", menu=self)


class AppearanceCascade(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, tearoff=False)
        self.add_command(label="Table mode", command= lambda : set_viewmode('table'))
        # self.add_command(label="Sheet mode", command= lambda : set_viewmode('sheet'))
        # self.add_command(label="Simple mode", command=lambda : set_viewmode('simple'))
        self.master.add_cascade(label="Appearance", menu=self)


class ViewCascade(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, tearoff=False)
        self.appearance = AppearanceCascade(self)
        self.master.add_cascade(label="View", menu=self)


class Menubar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, bd=0)
        self.file = FileCascade(self)
        self.view = ViewCascade(self)

        self.add_command(label="Help", command=help)
        self.add_command(label="About", command=about)

        self.master.config(menu=self)
