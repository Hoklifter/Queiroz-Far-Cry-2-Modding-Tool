from .INTERFACE_ELEMENTS import (
    Window,
    Menubar,
    MainFrame
)


class GUI:
    def __init__(self) -> None:
        """
        -GUI Constructors
        -Decorators done
        -maybe reuse some aspects of the edit function
        -More commands on windowbar
        -Get element_info
        """
        self.window = Window()
        self.menubar = Menubar(self.window)
        self.mainframe = MainFrame(self.window)

    