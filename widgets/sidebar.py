import tkinter as tk

from widgets.sidebar_settings import SettingsButton
from widgets.sidebar_github import Ghub
from settings import Settings

class SideBar:
    def __init__(self, root, width):
        self.width = width
        self.root = root
        self.frame = tk.Frame(root.window, height=root.window.winfo_height(), width=self.width)#, background="yellow")
        self.frame.pack_propagate(False)

        self.ghublink = Ghub(self.frame, Settings(root.settings.get_settings(['ghub'], {})))
        self.settingsbutton = SettingsButton(self.frame)

    def on_resize(self, event):
        self.frame.config(height=self.root.window.winfo_height())

    def setup_window(self, settingsscreen, mainscreen):
        settings_btn = self.settingsbutton.setup_window(settingsscreen.frame, mainscreen.frame)
        settings_btn.pack(side="top")

        ghub_btn = self.ghublink.setup_window()
        ghub_btn.pack(side="top")
        return self.frame
