import tkinter as tk
from .....utils import _save_xml, _open_xml, _pack, _unpack

class ActionButton(tk.Button):
    def __init__(self, master, text, command):
        tk.Button.__init__(self, master, text=text, command=command)
        self.pack()

class SaveButton(ActionButton):
    def __init__(self, master):
        ActionButton.__init__(self, master, text="Save", command=_save_xml)
        self.pack(side='left')

class OpenXmlButton(ActionButton):
    def __init__(self, master):
        ActionButton.__init__(self, master, text="Open Xml...", command=_open_xml)
        self.pack(side='left')

class UnpackButton(ActionButton):
    def __init__(self, master):
        ActionButton.__init__(self, master, text="Unpack...", command=_unpack)
        self.pack(side='left')

class PackButton(ActionButton):
    def __init__(self, master):
        ActionButton.__init__(self, master, text="Pack...", command=_pack)
        self.pack(side='left')

class FileLabel(tk.Text):
    def __init__(self, master, text):
        tk.Text.__init__(self, master, width=220)
        self.pack(side="left")
        self.insert(0.0, text)
        self.configure(state='disabled')
