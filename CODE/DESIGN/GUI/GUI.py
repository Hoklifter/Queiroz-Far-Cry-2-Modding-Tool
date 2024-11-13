from .INTERFACE_ELEMENTS import (
    Window,
    Menubar,
    MainFrame
)


class GUI:
    def __init__(self) -> None:
        self.mode = 'table'
        self.window = Window()
        self.menubar = Menubar(self.window)
        self.mainframe = MainFrame(self.window)
