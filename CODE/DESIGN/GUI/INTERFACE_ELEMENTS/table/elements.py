import tkinter as tk
from tkinter import ttk
import tkintertable as tt
from customtkinter import CTkTextbox
from .....OBJECTS import FC2XmlElement, FC2XmlParent
from ...utils import _save_xml, _open_xml, _pack, _unpack

class ParentDropdown(ttk.Combobox):
    def __init__(self, master, values) -> None:
        ttk.Combobox.__init__(self, master, state='readonly',width=300, values=values, justify="center", )
        self.pack()
        self.current(0)
        self.bind("<<ComboboxSelected>>", self.parent_changed)

    def parent_changed(self, event):
        from .....fc2moddingtool import FC2ModdingTool
        parents = FC2ModdingTool.xml.parents
        table = FC2ModdingTool.gui.mainframe.table
        selected_parent = parents[self.current()]
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
        from .....fc2moddingtool import FC2ModdingTool

        table_stack = FC2ModdingTool.gui.mainframe.table.stack
        index = self.get_currentRecordName()
        name, value = self.model.data[index].values()
        element:FC2XmlElement = table_stack[-1]
        element.set_child_value(index, value)
        """Testar e depois dar uma olhada em fc2moddingtool"""
        # print(f"""Modificando o filho de '{element.name}' no index {index} com nome de '{name}'. Valor antigo : {element.element_instance[index].text}, valor novo : {value} """)


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