
from .frames import (
    FileRelatedFrame,
    XMLRelatedFrame,
)
from .elements import (
    ParentDropdown,
    ActionButton,
    NavStack,
    MyTableCanva,
    FileLabel,
    SaveButton,
)

from .....OBJECTS import (
    FC2Xml,
    FC2XmlParent,
    FC2XmlElement,
)

class Table:
    def __init__(self, master):
        self.fc2moddingtool = master.master.gui_instance.app
        self.master = master
        self.stack = []

    def try_to_destroy_widget(self, widget:str):
        if hasattr(self, widget):
            widget = getattr(self, widget)
            widget.destroy()
       
    def recreate_xml_things(self):
        self.try_to_destroy_widget("xml_related_frame")
        master = XMLRelatedFrame(self.master)

        self.table_canva = MyTableCanva(master.table_frame)
        self.go_back_button = ActionButton(master.button_frame, "Go Back", self.go_back)
        self.nav_stack = NavStack(master.nav_stack_frame, self.stack)
        self.save_button = SaveButton(master.operations_frame)

        self.xml_related_frame = master

    def recreate_file_things(self):
        self.try_to_destroy_widget("file_related_frame")
        master = FileRelatedFrame(self.master)
        parents_names = [parent.name for parent in self.fc2moddingtool.xml.parents]

        self.filelabel = FileLabel(master.file_label_frame, self.fc2moddingtool.xml.basename)
        self.parent_dropdown = ParentDropdown(master.parent_dropdown_frame, parents_names)

        self.file_related_frame = master

    def go_back(self):
        if len(self.stack) > 1:
            self.stack.pop()
            self.render()
    
    def create_table(self, element_reference:FC2Xml|FC2XmlParent|FC2XmlElement):
        def wrapper():
            if isinstance(element_reference, FC2Xml):
                self.recreate_file_things()
                parent_zero:FC2XmlParent = element_reference.parents[self.parent_dropdown.current()]
                self.create_table(parent_zero)()
                return
                
            if isinstance(element_reference, FC2XmlElement):
                self.stack.append(element_reference)
                
            elif isinstance(element_reference, FC2XmlParent):
                self.stack = [element_reference.entity]

            self.render()
        return wrapper

    def render(self):
        self.recreate_xml_things()
        current:FC2XmlElement = self.stack[-1]

        for index, child in enumerate(current.element_instance):
            child = FC2XmlElement(child)

            if len(child) > 0:
                link_button = ActionButton(
                    master=self.xml_related_frame.button_frame,
                    text=f"{index}. {child.name}",
                    command=self.create_table(child)
                )
            else:
                row = table_length = self.table_canva.model.getRowCount()
                
                self.table_canva.addRow(index)
                self.table_canva.model.setValueAt(child.name, row, 0)
                self.table_canva.model.setValueAt(child.text, row, 1)


    



