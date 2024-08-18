import tkinter as tk
from tkinter import ttk
import tkintertable as tt
from customtkinter import CTkTextbox
from .....OBJECTS import FC2XmlElement, FC2XmlParent

class ParentDropdown(ttk.Combobox):
    def __init__(self, master, values) -> None:
        ttk.Combobox.__init__(self, master, state='readonly',width=300, values=values, justify="center", )
        self.pack()
        self.current(0)
        self.bind("<<ComboboxSelected>>", self.parent_changed)

    def parent_changed(self, event):
        table = self.master.master.master.table #ParentDropdownFrame, FileRelatedFrame, MainFrame, Table
        fc2moddingtool = self.master.master.master.master.gui_instance.app ##ParentDropdownFrame, FileRelatedFrame, MainFrame, Window, gui_instance, app
        selected_parent = fc2moddingtool.xml.parents[self.current()]
        table.create_table(selected_parent)()

class FileLabel(tk.Text):
    def __init__(self, master, text):
        tk.Text.__init__(self, master, width=220)
        self.pack(side="left")
        self.insert(0.0, text)
        self.configure(state='disabled')


class NavStack(CTkTextbox):
    def __init__(self, master, stack:list[FC2XmlElement, ...]): #type:ignore
        CTkTextbox.__init__(self, master, 767)
        stack_repr = "/".join([element.name for element in stack])
        self.insert(0.0, stack_repr)
        self.configure(state='disabled')
        self.pack(side='left')

class MyTableCanva(tt.TableCanvas):
    def __init__(self, master):
        tt.TableCanvas.__init__(
            self,
            master,
            rows=0,
            cols=0,
            showkeynamesinheader=True,
            height='10.7c',
            cellwidth=250,
        )

        self.model.addColumn("Name")
        self.model.addColumn("Value")
        self.show()
        self.bind_all('<KeyRelease>', self.set_element)

    def set_element(self, event):
        fc2moddingtool = self.master.master.master.master.gui_instance.app #self, tableframe, xmlrelated, mainframe, window, gui_instance, app
        index = self.get_currentRecordName()
        name, value = self.model.data[index].values()
        element = fc2moddingtool.gui.mainframe.table.stack[-1]
        element.set_child_value(index, value)
        """Testar e depois dar uma olhada em fc2moddingtool"""
        # print(f"""Modificando o filho de '{element.name}' no index {index} com nome de '{name}'. Valor antigo : {element.element_instance[index].text}, valor novo : {value} """)
        

class ActionButton(tk.Button):
    def __init__(self, master, text, command):
        tk.Button.__init__(self, master, text=text, command=command)
        self.pack()

class SaveButton(ActionButton):
    def __init__(self, master):
        ActionButton.__init__(self, master, text="Save", command=self.save_file)
        self.pack(side='left')

    def save_file(self):
        print("saving...")