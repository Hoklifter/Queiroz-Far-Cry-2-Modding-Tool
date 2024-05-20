import os
import shutil
import sys
import subprocess

class Pack:
    def __init__(self, unpacked_folder_path) -> None:
        """Convert XML to binary .fcb file and pack folder into .fat & .dat"""

        # core
        self.cwd = os.getcwd()

        # unpacked_folder
        self.unpacked_folder_path = os.path.realpath(unpacked_folder_path)
        self.unpacked_folder_name = os.path.basename(self.unpacked_folder_path)

        # packing tools
        self.tools_dir = os.path.join(self.cwd, "CODE/BOGGALOG_TOOLS/Packing-Unpacking")
        self.pack_folder_tool = os.path.join(self.tools_dir, "Gibbed.Dunia.pack.exe")
        self.binary_convert_tool = os.path.join(self.tools_dir, "Gibbed.Dunia.ConvertBinary.exe")
        self.packed_files = os.path.join(self.cwd, ".dat"), os.path.join(self.cwd, ".fat")
        
        self.main()
        
    def main(self):
        # convert binaries
        generated_folder = os.path.join(self.unpacked_folder_path, "generated")
        patch_override_files_table = os.path.join(generated_folder, "entitylibrarypatchoverride.xml")
        patch_override_game_files = os.path.join(generated_folder, "entitylibrarypatchoverride")
        subprocess.run(["wine", self.binary_convert_tool, patch_override_files_table])
        if os.path.exists(patch_override_game_files):
            shutil.rmtree(patch_override_game_files)
        if os.path.exists(patch_override_files_table):
            os.remove(patch_override_files_table)

        # pack folder
        subprocess.run(["wine", self.pack_folder_tool, self.unpacked_folder_path])

if __name__ == "__main__":
    file_path = ''
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    pack = Pack(file_path)