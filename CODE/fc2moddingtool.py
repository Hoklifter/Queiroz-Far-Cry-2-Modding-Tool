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


from .OBJECTS import (
    FC2Xml
)

from .UTILS import (
    pack,
    unpack,
)


from .DESIGN import (
    GUI
)

from .DESIGN.GUI.utils import (
    _open_xml
)

class FC2ModdingTool:
    unpacked:str = None
    xml:FC2Xml = None
    gui = GUI()

FC2ModdingTool.gui.window.mainloop()
