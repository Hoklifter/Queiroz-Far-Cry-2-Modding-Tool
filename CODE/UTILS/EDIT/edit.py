        # editables = {
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
        #     "weapons.xml" : self.edit_weapons,


import os
import sys
import xml.etree.ElementTree as ET

from .UTILS.get_shit import (
    get_parents
)

from .UTILS.main_funcs import (
    ask_for_input,
    logic_based_on_user_input,
    show_options
)

class Edit:
    def __init__(self, xml_path) -> None:
        """Parse XML files;
           Separate elements by their label/value
        """

        # core
        self.cwd = os.getcwd()
        self.xml_path = xml_path = os.path.realpath(xml_path)
        self.filename = os.path.basename(xml_path)
        self.domtree = ET.parse(xml_path)
        self.root = self.domtree.getroot()
        self.parents, self.parents_names = get_parents(self.root)
        self.stack = [self.parents]

        self.user_input = None
        self.current = self.stack[-1]
        self.current_info = 'ROOT'
        self.options = None
        self.main()
    
    def main(self):
        while self.stack:
            "preparar GUI e testar em outros arquivos"
            show_options(self)
            ask_for_input(self)
            logic_based_on_user_input(self)

if __name__ == "__main__":
    file_path = ''
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    edit = Edit(file_path)