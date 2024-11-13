import tkinter as tk
from tkinter import ttk
import tkintertable as tt
from customtkinter import CTkTextbox
from .......OBJECTS import FC2XmlElement, FC2XmlParent
from .......UTILS.methods_for_builtins import get_nth_value

class ParentDropdown(ttk.Combobox):
    def __init__(self, master, values) -> None:
        ttk.Combobox.__init__(self, master, state='readonly',width=300, values=values, justify="center", )
        self.values = values
        self.pack()
        self.current(0)
        self.bind("<<ComboboxSelected>>", self.parent_changed)

    def parent_changed(self, event):
        from .......fc2moddingtool import FC2ModdingTool
        unified_parents = FC2ModdingTool.xml.unified_parents
        table = FC2ModdingTool.gui.mainframe.content
        selected_parent_class, selected_parent = self.values[self.current()].split('.')
        table.create_table(unified_parents[selected_parent_class][selected_parent])



class NavStack(CTkTextbox):
    def __init__(self, master, stack:list[FC2XmlElement, ...], index_stack=[]): #type:ignore
        CTkTextbox.__init__(self, master, 767)
        stack_repr = "/".join([element.name for element in stack])
        self.insert('0.0', stack_repr)
        self.insert('end', f"\n{index_stack}")
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
            thefont = ('Arial',9)

        )

        self.model.addColumn("Name")
        self.model.addColumn("Value")
        self.show()
        self.bind_all('<KeyRelease>', self.set_element_in_parents_of_group)

    def set_element_in_parents_of_group(self, event):
        from .......fc2moddingtool import FC2ModdingTool

        table_index_stack                      = FC2ModdingTool.gui.mainframe.content.index_stack
        parent_group:list[FC2XmlElement, ...] = FC2ModdingTool.gui.mainframe.content.parent_group #type:ignore

        index = self.get_currentRecordName()
        name, value = self.model.data[index].values()

        for parent in parent_group:
            element = parent[table_index_stack][index]
            element.element_instance.text = value
            # element[3, 5, 4, 4] = element[3][5][4][4]

        # Pegar pelo index e aplicar a todos os filhos, procurar uma função nativa para indexar
        # print(f"""Modificando o filho de '{element.name}' no index {index} com nome de '{name}'. Valor antigo : {element.element_instance[index].text}, valor novo : {value} """)
