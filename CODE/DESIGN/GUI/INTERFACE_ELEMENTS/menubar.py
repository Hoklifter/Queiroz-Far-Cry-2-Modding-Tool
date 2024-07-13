import tkinter as tk


class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, bd=0 )
        self.file = tk.Menu(self, tearoff=False)
        self.file.add_command(label="Unpack File...", command=master.gui_instance.app.gui_unpack)
        self.file.add_command(label="Pack Folder...", command=master.gui_instance.app.gui_pack)
        self.file.add_command(label="Edit Unpacked Folder...", command=None)
        self.file.add_command(label="Exit", command=quit)
        self.add_cascade(label="File", menu=self.file)

        self.add_command(label="Help", command=None)
        self.add_command(label="About", command=None)

        self.master.config(menu=self)
