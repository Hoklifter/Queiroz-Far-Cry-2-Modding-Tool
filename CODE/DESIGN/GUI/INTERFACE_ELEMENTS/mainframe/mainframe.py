import tkinter as tk

from .views import (
    # SheetView,
    TableView,
    # SimpleView,
)

from .views.common import (
     OperationFrameWithButtons
)

from...utils import try_to_destroy_widget

from tkinter.dialog import Dialog

class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=767, height=596, highlightcolor='red', highlightthickness=0)
        self.place(relx=0.5, rely=0.5, anchor='center')
        self.content = OperationFrameWithButtons(self)
        self.content.place(x=225, y=225)


    def show(self):
        from .....fc2moddingtool import FC2ModdingTool
        if not FC2ModdingTool.xml:
                raise ValueError(f"xml not loaded")
        try_to_destroy_widget(self, 'content')


        def table():
            self.content = TableView(self, xmlobj=FC2ModdingTool.xml)
        # def sheet():
        #     self.content = SheetView(self, xmlobj=FC2ModdingTool.xml)

        # def simple():
        #     self.content = SimpleView(self, xmlobj=FC2ModdingTool.xml)

        mode = FC2ModdingTool.gui.mode
        match mode:
            case 'table':
                table()
            # case 'sheet':
            #     sheet()
            # case 'simple':
            #     simple()
            case _:
                raise ValueError(f"invalid mode: {mode!r}")
