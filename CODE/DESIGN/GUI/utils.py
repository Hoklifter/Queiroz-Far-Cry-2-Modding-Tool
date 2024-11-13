from tkinter import filedialog
from ...UTILS import pack, unpack
from ...OBJECTS import FC2Xml
import webbrowser


def set_viewmode(mode):
    from ...fc2moddingtool import FC2ModdingTool
    FC2ModdingTool.gui.mode = mode
    FC2ModdingTool.gui.window.update_geometry()
    FC2ModdingTool.gui.mainframe.show()

def try_to_destroy_widget(obj, widget=None):
        try:
            if widget:
                widget = getattr(obj, widget)
                widget.destroy()
            else:
                obj.destroy()
        except:
            pass

def ask_for_path_then_execute(filetypes=None, askfordir=False, title=None):
        "Creates the decorator with the passed arguments."
        def decorator(func):
            "Receives the decorated function and create the wrapper"
            def wrapper(overwrite_path=None):
                "Final modified function"
                if overwrite_path:
                    "Do not call filedialog if argument is passed to function."
                    func(overwrite_path)
                else:
                    from ...fc2moddingtool import FC2ModdingTool
                    initialdir=FC2ModdingTool.unpacked

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
                        func(path)
            return wrapper
        return decorator


@ask_for_path_then_execute(filetypes=[("*", ".dat"), ("*", ".fat")],title="Select .fat/.dat file...")
def _unpack(fatpath):
    from ...fc2moddingtool import FC2ModdingTool

    FC2ModdingTool.unpacked = unpack(fatpath)
    _open_xml()

@ask_for_path_then_execute(askfordir=True)
def _pack(dirpath):
    pack(dirpath)
    print(f'SUCCESS: {dirpath!r} PACKED SUCCESFULLY.')

@ask_for_path_then_execute(filetypes=[("*", ".xml")], title="Select .xml file...",)
def _open_xml(xml_path):
    from ...fc2moddingtool import FC2ModdingTool
    FC2ModdingTool.xml = FC2Xml(xml_path)
    FC2ModdingTool.gui.mainframe.show()

def _save_xml():
    from ...fc2moddingtool import FC2ModdingTool

    FC2ModdingTool.xml.save_document()

def about():
    webbrowser.open('https://github.com/Hoklifter')
def help():
    webbrowser.open('https://github.com/Hoklifter/Queiroz-Far-Cry-2-Modding-Tool')