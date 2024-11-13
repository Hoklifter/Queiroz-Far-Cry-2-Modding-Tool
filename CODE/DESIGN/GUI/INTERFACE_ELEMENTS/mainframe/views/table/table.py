
from ..common.frames import (
    OperationFrameWithButtons,
)

from ..common.elements import (
    ActionButton,
    FileLabel
)

from .frames import (
    FileRelatedFrame,
    DOMRelatedFrame,
)
from .elements import (
    ParentDropdown,
    NavStack,
    MyTableCanva,
)

from .......OBJECTS import (
    FC2Xml,
    FC2XmlParent,
    FC2XmlElement,
)

from .....utils import try_to_destroy_widget
from .......UTILS.methods_for_builtins import get_nth_value

import tkinter as tk


"""Pseudo code

stack = [[ak47, ak47-gold, ak47-multiplayer]]
generate table based on ak47(index stack[0][0])

select option 5 in table:
go to stack[0][0][option=5]
this will get the 5th child of the element ak = ak[5]
remember that et.Element objects are indexable

generate table stack[0][0][5]

stack=[[ak47, ak47-gold, ak47-multiplayer], 5]


binding to update element:
    iterate through stack[0] and make a change to the element stack[1:]

so if stack = [[ak47, ak47-gold, ak47-multiplayer], 5, 3, 4, 3, 1, 2]

update the elements ak47[5][3][4][3][1][2], ak47-gold[5][3][4][3][1][2] and ak47-multiplayer[5][3][4][3][1][2]
"""




class TableView(tk.Frame):
    def __init__(self, master, xmlobj=None):
        tk.Frame.__init__(self, master)
        self.index_stack: list[int, ...] = [] #type:ignore
        self.parent_group = None #List of fc2xmlparent [ak, ak2, ak3]
        if xmlobj:
            self.create_table(xmlobj)
        self.pack()

    def recreate_dom_things(self):
        try_to_destroy_widget(self, "dom_related_frame")
        master = DOMRelatedFrame(self)
        self.table_canva = MyTableCanva(master.table_frame)
        self.go_back_button = ActionButton(master.button_frame, "Go Back", self.go_back)

        stack = []
        current_elem = None
        for index in self.index_stack:
            index = [index]
            if not current_elem:
                current_elem = self.parent_group[0]

            current_elem = current_elem[index]
            stack.append(current_elem)

        self.nav_stack = NavStack(master.nav_stack_frame, stack, index_stack=self.index_stack)
        self.operation_frame = OperationFrameWithButtons(master)
        self.dom_related_frame = master

    def recreate_file_things(self):
        try_to_destroy_widget(self, "file_related_frame")
        from .......fc2moddingtool import FC2ModdingTool
        master = FileRelatedFrame(self)

        self.filelabel = FileLabel(master.file_label_frame, FC2ModdingTool.xml.basename)

        dropdown_values = []
        for elem_class, elem_names in FC2ModdingTool.xml.unified_parents.items():
            for elem_name in elem_names:
                dropdown_values.append(f"{elem_class}.{elem_name}")
        self.parent_dropdown = ParentDropdown(master.parent_dropdown_frame, dropdown_values)

        self.file_related_frame = master

    def go_back(self):
        if len(self.index_stack):
            self.index_stack.pop()
            self.render()

    def create_table(self, element_reference:FC2Xml|list[FC2XmlParent, ...]|FC2XmlElement, index=None): #type:ignore
        if isinstance(element_reference, FC2Xml):
            self.recreate_file_things()
            parent_class = get_nth_value(element_reference.unified_parents)
            parent_group = get_nth_value(parent_class)
            self.create_table(parent_group)
            return

        elif isinstance(element_reference, list): #type:ignore List of fc2xmlparent [ak, ak2, ak3]
            self.parent_group = element_reference

        elif isinstance(element_reference, FC2XmlElement) and isinstance(index, int):
            self.index_stack.append(index)

        else:
            raise TypeError(
                f"The type in this function needs to be FC2XmlElement, list[FC2XmlElement, ...] or FC2Xml, not {type(element_reference)}"
            )
        self.render()

    def render(self):
        try:
            self.recreate_dom_things()
        except IndexError:
            self.index_stack.clear()
            self.render()
            return

        current_element = self.parent_group[0][self.index_stack]

        # print()
        for index, child in enumerate(current_element):

            if len(child) > 0:
                # print(child.name, child)
                link_button = ActionButton(
                    master=self.dom_related_frame.button_frame,
                    text=f"{index}. {child.name}",
                    command=lambda c=child, i=index: self.create_table(element_reference=c, index=i)
                )
                """Thanks CHATGPT:
                The issue is a common pitfall when using lambda functions in loops in Python.
                Specifically, when you create a lambda function inside a loop,
                the lambda captures the variable by reference, not by value.
                This means that all the lambda functions will reference the same child variable,
                which will be the last child in the loop after the loop completes.

                lambda : self.create_table(child) will not work.

                lambda c=child: self.create_table(c) creates a lambda function with a default
                argument c that captures the current value of child at each iteration.
                This ensures that each button's command is bound to the specific child from that iteration,
                rather than all buttons being bound to the last child in the loop.

                Key Takeaway:
                When using lambda functions in a loop, be aware of variable capture and use default arguments
                to ensure that each lambda captures the correct value from the loop iteration."""

            else:
                row = table_length = self.table_canva.model.getRowCount()

                self.table_canva.addRow(index)
                self.table_canva.model.setValueAt(child.name, row, 0)
                self.table_canva.model.setValueAt(child.text, row, 1)
                self.table_canva.updateModel(self.table_canva.model)
