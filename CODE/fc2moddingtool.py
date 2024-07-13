"""To run the script as CLI, run this file as follows:
Usage: python3 file.fat or file.dat"""
from tkinter import (
    filedialog,
    ttk
)


import os 


from .UTILS import (
    unpack,
    Edit,
    pack,
)

from .DESIGN import (
    GUI
)

print()
class FC2ModdingTool:
    def __init__(self,):
        self.current_fat = None
        self.current_edit_xml_path = None
        self.main()

    def gui_unpack(self):
        filepath = filedialog.askopenfilename(filetypes=[("*", ".dat"), ("*", ".fat")])
        if filepath:
            unpacked_fat = unpack(filepath)
            filepath = unpacked_fat or self.current_fat
            self.current_fat = filepath

    def gui_pack_current(self):
        pack(self.current_fat)

    def gui_pack(self):
        dirpath = filedialog.askdirectory(mustexist=True)
        if dirpath:
            pack(dirpath)

    def main(self):
        gui = GUI(self)  


        # unpack = Unpack("patch.fat")
        # edit = Edit("patch_unpack/generated/entitylibrarypatchoverride/22_weapons.xml")
        # pack = Pack("patch_unpack")
    

    """To do today:
    Transform classes in utils to functions"""