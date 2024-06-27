"""To run the script as CLI, run this file as follows:
Usage: python3 file.fat or file.dat"""
from .UTILS import Unpack, Pack, Edit

class FC2ModdingTool:
    # unpack = Unpack("patch.fat")
    edit = Edit("patch_unpack/generated/entitylibrarypatchoverride/22_weapons.xml")
    # pack = Pack("patch_unpack")
    