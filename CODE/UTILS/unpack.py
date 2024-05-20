import os
import sys
import subprocess

class Unpack:
    def __init__(self, file_path) -> None:
        """Unpack .fat & .dat files and decode .xml files."""

        # core
        self.cwd = os.getcwd()

        # .fat | .dat
        self.file_path = os.path.realpath(file_path)
        self.file_extension = os.path.splitext(self.file_path) # split-extension not split-text
        self.file_dir = os.path.dirname(self.file_path)
        self.file_basename = os.path.basename(self.file_path)
        self.file_name = os.path.splitext(self.file_basename)[0]

        # unpacking tools
        self.tools_dir = os.path.join(self.cwd, "CODE/BOGGALOG_TOOLS/Packing-Unpacking")
        self.unpack_fat_tool = os.path.join(self.tools_dir, "Gibbed.Dunia.Unpack.exe")
        self.binary_convert_tool = os.path.join(self.tools_dir, "Gibbed.Dunia.ConvertBinary.exe")

        # xml decoding tools
        self.xml_decoder_tool_dir = os.path.join(self.cwd, "CODE/BOGGALOG_TOOLS/XML-Decoder")
        self.xml_decoder_tool = os.path.join(self.xml_decoder_tool_dir, r"Start XML Decoder.bat")
        self.xml_to_decode_dir = os.path.join(self.xml_decoder_tool_dir, r"Put xml files to decode in here")
        
        self.main()
        
    def main(self):

        # unpack fat & dat
        file_validate = subprocess.run(["wine", self.unpack_fat_tool, self.file_path], capture_output=True).stderr # unpacks the .fat file and get stderr
        if b'Unhandled Exception:' in file_validate:
                for x in file_validate: print(x)
                exit()
        unpacked_file_dir = f"{self.file_extension[0]}_unpack"

        # convert binaries
        patch_override_dir = os.path.join(unpacked_file_dir, "generated")
        patch_override = os.path.join(patch_override_dir, "entitylibrarypatchoverride.fcb")
        subprocess.run(["wine", self.binary_convert_tool, patch_override])
        converted_patch_override_dir = os.path.join(patch_override_dir, "entitylibrarypatchoverride")
        

        # decode xml
        for xml_file in os.listdir(converted_patch_override_dir): # Move xml files
            xml_file_path = os.path.join(converted_patch_override_dir, xml_file)
            new_xml_file_path = os.path.join(self.xml_to_decode_dir, xml_file)
            os.replace(xml_file_path, new_xml_file_path)
        subprocess.run(["wine", self.xml_decoder_tool])

        for xml_file in os.listdir(self.xml_to_decode_dir): # Move xml files back
            xml_file_path = os.path.join(self.xml_to_decode_dir, xml_file)
            new_xml_file_path = os.path.join(converted_patch_override_dir, xml_file)
            os.replace(xml_file_path, new_xml_file_path)

        

if __name__ == "__main__":
    file_path = ''
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    unpack = Unpack(file_path)