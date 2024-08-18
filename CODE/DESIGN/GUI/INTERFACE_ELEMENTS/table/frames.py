import tkinter as tk
from customtkinter import CTkScrollableFrame, set_appearance_mode
set_appearance_mode('light')

class ButtonFrame(CTkScrollableFrame):
    def __init__(self, master):
        CTkScrollableFrame.__init__(self, master, height='11c', border_width=1)
        self.grid(row=0, column=0, sticky="NW",)


class TableFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height="10.7c", width=200)
        self.grid(row=0,column=1, sticky="NW")


class NavStackFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height='1.5cm', highlightcolor='green', highlightthickness=0, width=767) # xmlframe, mainframe, window
        self.grid(sticky='NW', row=1, column=0, columnspan=3)
        self.propagate(False)


class OperationButtonsFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height='0.7cm', width=767)
        self.grid(row=2, column=0, columnspan=3)
        self.propagate(False)


class ParentDropdownFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height='0.6cm', width=498)
        self.grid(row=0, column=1, sticky='W', padx=(47, 0))
        self.propagate(False)

class FileLabelFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height='0.6cm',width=220,)
        self.grid(sticky="NW", row=0, column=0,)
        self.propagate(False)

class FileRelatedFrame(tk.Frame):
    def __init__(self, master, ):
        tk.Frame.__init__(self, master,  highlightcolor='blue', highlightthickness=0, height='0.7cm', width=767)
        self.grid(sticky="W", row=0, column=0,)
        self.propagate(False)
        self.file_label_frame = FileLabelFrame(self)
        self.parent_dropdown_frame = ParentDropdownFrame(self)


class XMLRelatedFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid(row=1, column=0,)
        self.table_frame = TableFrame(self)
        self.button_frame = ButtonFrame(self)
        self.nav_stack_frame = NavStackFrame(self)
        self.operations_frame = OperationButtonsFrame(self)
