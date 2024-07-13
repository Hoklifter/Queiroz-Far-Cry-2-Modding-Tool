"""Some notes:
    - Unpacked means the folder you get when you use the unpack function or run the Gibbed.Dunia.Unpack.exe"""

import os
import subprocess
import shutil

# core paths
CWD = os.getcwd()
TEMP = os.path.join(CWD, "TEMP")


# unpacking tools
TOOLS_DIR = os.path.join(CWD, "CODE/BOGGALOG_TOOLS/Packing-Unpacking")
FAT_TOOL_UNPACK = os.path.join(TOOLS_DIR, "Gibbed.Dunia.Unpack.exe")
FAT_TOOL_PACK = os.path.join(TOOLS_DIR, "Gibbed.Dunia.pack.exe")
FCB_TOOL_CONVERT = os.path.join(TOOLS_DIR, "Gibbed.Dunia.ConvertBinary.exe")

# xml decoding tools
XML_TOOLS_DIR = os.path.join(CWD, "CODE/BOGGALOG_TOOLS/XML-Decoder")
XML_TOOL_DECODER = os.path.join(XML_TOOLS_DIR, r"Start XML Decoder.bat")
XML_PUT_TO_DECODE_HERE_DIR = os.path.join(XML_TOOLS_DIR, r"Put xml files to decode in here")

# unpacked paths
ENTITY_LIBRARIES_DIRS = ["downloadcontent/dlc1/generated", "generated"]


def _move_element(element_path : str, destination : str, filters=()):
    for func in filters:
        if not func(element_path):
            return
        
    element_name = os.path.basename(element_path)
    destination = os.path.join(destination, element_name)

    shutil.move(element_path, destination)


def _move_elements(origin : str, destination : str, filters=()):
    """Moves all elements from one dir to another"""
    for element in os.listdir(origin):
        element_path = os.path.join(origin, element)
        _move_element(element_path, destination, filters)


def convert_entity_library(library_path : str) -> dict:
    """Convert .fcb to a directory with xml files or
    a directory with xml files to a .fcb.

    You must pass the entity library or the entity library info
    
    passing entitylibrarypatchoverride.fcb will create entitylibrarypatchoverride and entitylibrarypatchoverride.xml
    passing entitylibrarypatchoverride.xml will create entitylibrarypatchoverride.fcb

    Returns the new library info"""

    entity_library_path_no_ext, entity_library_extension = os.path.splitext(library_path)
    subprocess.run(["wine", FCB_TOOL_CONVERT, library_path])
    
    if entity_library_extension == ".xml":
        converted_entity_library = {
            "file" : entity_library_path_no_ext + ".fcb",
            "folder" : None
        }
    elif entity_library_extension == ".fcb":
        converted_entity_library = {
            "file" : entity_library_path_no_ext + ".xml",
            "folder" : entity_library_path_no_ext
        }

    return converted_entity_library


def _convert_libraries_in_unpacked(unpacked_path : str, mode : str):
    """
mode   : description

to_xml : Convert to folder with configuration files and a file with 
to_fcb : Convert to a .fcb

"""
    converted_libs = []
    if mode not in ("to_xml", "to_fcb"):
        raise ValueError(f"invalid mode: {mode!r}")

    for directory in ENTITY_LIBRARIES_DIRS:
        entity_library_dir = os.path.join(unpacked_path, directory)
        for element in os.listdir(entity_library_dir):

            element_path = os.path.join(entity_library_dir, element)
            element_is_fcb = element_path.endswith(".fcb")
            element_is_xml = element_path.endswith(".xml")
            element_is_file = os.path.isfile(element_path)

            if element_is_file:
                if (mode == "to_xml" and element_is_fcb) \
                or (mode == "to_fcb" and element_is_xml):
                    converted_lib = convert_entity_library(element_path)
                    converted_libs.append(converted_lib)

    return converted_libs


def _move_old_entity_library(unpacked_path : str, move_back:bool = False):
    """Move old entity library and entity library override to temp
    for packing or moves it back."""

    for directory in ENTITY_LIBRARIES_DIRS:
        entity_library_dir = os.path.join(unpacked_path, directory)
        temp_library_dir = os.path.join(TEMP, directory)
        os.makedirs(temp_library_dir, exist_ok=True)

        if not move_back:
            _move_elements(entity_library_dir, temp_library_dir, (lambda x : not x.endswith(".fcb"),))
        else:
            _move_elements(temp_library_dir, entity_library_dir, (lambda x : not x.endswith("blank"),))


def decode_xmls(directory : str):
    """Decode all xmls in given directory."""
    # Move xml files to decoding tool dir
    _move_elements(directory, XML_PUT_TO_DECODE_HERE_DIR)
    # Decode
    subprocess.run(["wine", XML_TOOL_DECODER])
    # Move xml files back to original dir
    _move_elements(XML_PUT_TO_DECODE_HERE_DIR, directory)


def unpack(fat_path : str) -> str:
    """Unpack .fat & .dat files and decode .xml files.
    Returns unpacked directory path"""
    
    # .fat or .dat file
    fat_path = os.path.realpath(fat_path)

    def unpack_fat(file_path : str) -> str:
        """Unpack .fat & .dat files
        Returns unpacked directory path"""

        file_basename = os.path.basename(file_path)
        file_path_no_ext = os.path.splitext(file_path)[0]
        file_unpacked_dir = f"{file_path_no_ext}_unpack"
        file_validate = subprocess.run(["wine", FAT_TOOL_UNPACK, file_path], capture_output=True).stderr # unpacks the .fat file and get stderr

        if b'Unhandled Exception:' in file_validate:
            for x in file_validate:
                print(x)
            raise Exception(f"Error when unpacking {file_basename}")

        return file_unpacked_dir




    unpacked_fat_dir = unpack_fat(fat_path)
    converted_libraries = _convert_libraries_in_unpacked(unpacked_fat_dir, mode="to_xml")
    for library in converted_libraries:
        decode_xmls(library["folder"])

    return unpacked_fat_dir


def pack(unpacked_path : str) -> dict:
    """Convert .xml to binary .fcb file and pack folder into .fat & .dat
    
    Return packed files info
    """
    
    unpacked_path = os.path.realpath(unpacked_path)
    unpacked_name = os.path.basename(unpacked_path)

    # move old converted library
    _move_old_entity_library(unpacked_path)

    # convert libraries
    _convert_libraries_in_unpacked(unpacked_path, mode="to_fcb")

    # pack folder
    subprocess.run(["wine", FAT_TOOL_PACK, unpacked_path])

    # move old library back
    _move_old_entity_library(unpacked_path, move_back=True)

    packed_files = {
        "dat" : os.path.join(CWD, f"{unpacked_name}.dat"),
        "fat" : os.path.join(CWD, f"{unpacked_name}.fat")
    }

    return packed_files