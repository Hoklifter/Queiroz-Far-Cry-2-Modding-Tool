import tkinter as tk
from .table import (
    Table
)

class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=767, height=596, highlightcolor='red', highlightthickness=0)
        self.place(relx=0.5, rely=0.5, anchor='center')

    def show(self):
        self.table = Table(self)