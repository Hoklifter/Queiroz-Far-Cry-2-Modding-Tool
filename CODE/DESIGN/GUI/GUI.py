from .INTERFACE_ELEMENTS import (
    Window,
    MenuBar,
    Table,
    MainFrame
)

from tkinter import Frame


class GUI:
    def __init__(self, app) -> None:
        """
        -GUI Constructors
        -Decorators done
        -maybe reuse some aspects of the edit function
        -More commands on windowbar
        -Get element_info
        """
        self.app = app
        self.window = Window(self)
        self.menubar = MenuBar(self.window)
        self.mainframe = MainFrame(self.window)

    