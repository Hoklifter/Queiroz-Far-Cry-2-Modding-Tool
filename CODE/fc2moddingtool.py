"""     #    editables = {
        #     "buddies.xml" : self.edit_buddies,
        #     "cameras.xml" :self.edit_cameras,
        #     "curves.xml" :self.edit_curves,
        #     "enemy_archetypes.xml" : self.edit_enemy_archetypes,
        #     "gadgets.xml" : self.edit_gadgets,
        #     "ghostpatrols.xml" : self.edit_ghostpatrols,
        #     "oa_missionpickups.xml" : self.edit_missionpickups,
        #     "oa_streetsigns.xml" : self.edit_streetsigns,
        #     "pickups.xml" : self.edit_pickups,
        #     "player.xml" : self.edit_player,
        #     "vehicle.xml" : self.edit_vehicle,
        #     "weaponproperties.xml" : self.edit_weaponproperties,
        #     "weapons.xml" : self.edit_weapons,"""


import tkinter as tk

from tkinter import (
    filedialog
)

from xml.etree.ElementTree import (
    Element
)
import os 

from .OBJECTS import (
    FC2Xml
)

from .UTILS import (
    unpack,
    pack,

)

from .DESIGN import (
    GUI
)

class FC2ModdingTool:
    """!!! Mudar pra class var inves de instance var, e save_document"""
    def __init__(self,):

        self.unpacked:str = None
        self.xml:FC2Xml = None
        self.gui = GUI(self)
        self.gui.menubar._select_xml("21_WeaponProperties.xml")
        self.gui.window.mainloop()
