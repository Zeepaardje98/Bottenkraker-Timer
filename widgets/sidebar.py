import tkinter as tk

from widgets.sidebar_settings import SettingsButton
from widgets.sidebar_github import Ghub
from widgets.sidebar_upload import Upload
from widgets.sidebar_info import Info

from settings import Settings

class SideBar:
    def __init__(self, root, width):
        self.width = width
        self.root = root
        self.frame = tk.Frame(root.window, height=root.window.winfo_height(), width=self.width)#, background="yellow")
        self.frame.pack_propagate(False)

        self.ghublink = Ghub(self.frame, Settings({"ghub": root.settings.get_settings(["ghub"]),
                                                   "themes": root.settings.get_settings(["themes"]),
                                                   "selected_theme": root.settings.get_settings(["selected_theme"])}))
        self.settingsbutton = SettingsButton(self.frame, Settings({"themes": root.settings.get_settings(["themes"]),
                                                                   "selected_theme": root.settings.get_settings(["selected_theme"])}))
        self.upload = Upload(self.root, self.frame, Settings({"themes": root.settings.get_settings(["themes"]),
                                                              "selected_theme": root.settings.get_settings(["selected_theme"])}))
        self.info = Info(self.root, self.frame, Settings({"themes": root.settings.get_settings(["themes"]),
                                                          "selected_theme": root.settings.get_settings(["selected_theme"])}))


    def on_resize(self, event):
        self.frame.config(height=self.root.window.winfo_height())

    def setup_window(self, settingsscreen, mainscreen):
        settings_btn = self.settingsbutton.setup_window(settingsscreen.frame, mainscreen.frame)
        settings_btn.pack(side="top", pady=(5, 0))

        ghub_btn = self.ghublink.setup_window()
        ghub_btn.pack(side="top", pady=(5, 0))

        upload_btn = self.upload.setup_window()
        upload_btn.pack(side="top", pady=(5, 0))

        info_btn = self.info.setup_window()
        info_btn.pack(side="top", pady=(5, 0))

        return self.frame
