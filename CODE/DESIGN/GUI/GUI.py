from .INTERFACE_ELEMENTS import (
    Window,
    MenuBar,
    
)


class GUI:
    def __init__(self, app) -> None:
        self.app = app
        self.window = Window(self)
        self.menubar = MenuBar(self.window)
        self.window.mainloop()