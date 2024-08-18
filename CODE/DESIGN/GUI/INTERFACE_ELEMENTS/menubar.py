import tkinter as tk
from tkinter import filedialog

from ....OBJECTS import (
    FC2Xml,
    FC2XmlElement,
    FC2XmlParent
)

from ....UTILS import (
    unpack,
    pack
)

def ask_for_path_then_execute(filetypes=None, askfordir=False, title=None, initialdir=None):
        def decorator(func):
            def wrapper(self, overwrite_path=None):
                if overwrite_path:
                    func(self, overwrite_path)
                else:
                    if askfordir:
                        path = filedialog.askdirectory(
                            mustexist=True,
                            title=title,
                            initialdir=initialdir
                        )
                    else:
                        path = filedialog.askopenfilename(
                            filetypes=filetypes,
                            title=title,
                            initialdir=initialdir
                        )
                    if path:
                        func(self, path)
            return wrapper
        return decorator

class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, bd=0)
        self.fc2moddingtool = master.gui_instance.app

        self.file = tk.Menu(self, tearoff=False)
        self.file.add_command(label="Unpack File...", command=self._unpack)
        self.file.add_command(label="Pack Folder...", command=self._pack)
        self.file.add_command(label="Edit Xml...", command=self._select_xml)
        self.file.add_command(label="Exit", command=quit)
        self.add_cascade(label="File", menu=self.file)

        self.add_command(label="Help", command=None)
        self.add_command(label="About", command=None)

        self.master.config(menu=self)

    @ask_for_path_then_execute(filetypes=[("*", ".dat"), ("*", ".fat")],title="Select .fat/.dat file...")
    def _unpack(self, fatpath):
        self.fc2moddingtool.unpacked_path = unpacked_path = unpack(fatpath)
        self._select_xml(unpacked_path)

    def _pack_current(self):
        pack(self.fc2moddingtool.unpacked_path)

    @ask_for_path_then_execute(askfordir=True)
    def _pack(self, dirpath):
        pack(dirpath)

    @ask_for_path_then_execute(filetypes=[("*", ".xml")], title="Select .xml file...",)
    def _select_xml(self, xml_path):
        self.fc2moddingtool.xml = FC2Xml(xml_path)
        self.fc2moddingtool.gui.mainframe.show()
        self.fc2moddingtool.gui.mainframe.table.create_table(self.fc2moddingtool.xml)()
    
        """Settar, Salvar"""