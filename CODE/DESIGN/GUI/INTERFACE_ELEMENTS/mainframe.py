import tkinter as tk

from .table import (
    Table,
)

from .table.frames import (
    OperationButtonsFrame
)

from .table.elements import (
    OpenXmlButton, PackButton, UnpackButton
)

class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=767, height=596, highlightcolor='red', highlightthickness=0)
        self.place(relx=0.5, rely=0.5, anchor='center')

        self.start_menu = OperationButtonsFrame(self)
        self.start_menu.pack()

        unpackbutton = UnpackButton(self.start_menu)
        packbutton = PackButton(self.start_menu)
        openxmlbutton = OpenXmlButton(self.start_menu)


    def show(self):
        self.start_menu.destroy()
        self.table = Table(self)