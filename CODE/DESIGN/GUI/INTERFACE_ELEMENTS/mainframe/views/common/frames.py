import tkinter as tk
from .elements import (
    PackButton,
    SaveButton,
    UnpackButton,
    OpenXmlButton,
)

class FileLabelFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height='0.6cm',width=220,)
        self.grid(sticky="NW", row=0, column=0,)
        self.propagate(False)

class OperationFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height='0.7cm', width=767)
        self.grid(row=2, column=0, columnspan=3)
        self.propagate(False)

class OperationFrameWithButtons(OperationFrame):
    def __init__(self,master):
        OperationFrame.__init__(self, master)
        self.pack_button = PackButton(self)
        self.save_button = SaveButton(self)
        self.unpack_button = UnpackButton(self)
        self.open_xml_button = OpenXmlButton(self)