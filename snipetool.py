#!/usr/bin/env python3
import tkinter as tk

from widgets.bar import Bar
from widgets.mainscreen import MainScreen
from widgets.settingsmenu import SettingsScreen
from widgets.infoscreen import InfoScreen
from widgets.sidebar import SideBar
# from widgets.sidebar_settings import SettingsButton
# from widgets.sidebar_github import Ghub
from settings import Settings

class SnipeTool:
    def __init__(self):
        self.settings = Settings()
        self.settings.load_settings("settings/snipetool_config.yaml")

        self.window = tk.Tk()
        self.window.bind("<Configure>", self.on_resize)

        # Some variables which can be changed by the widgets. Which is why we
        # need to pass these variables by reference instead of by value. Thus
        # we use a mutable variable type
        self.snipe_time = []
        self.clock = []

        self.currentscreen = [None]

        self.bar = Bar(self.window, 40, Settings(self.settings.get_settings(['bar'], {})))
        self.sidebar = SideBar(self, 30)

        self.mainscreen = MainScreen(self, self.currentscreen)
        self.standard_size = "330x190"
        self.settingsscreen = SettingsScreen(self, self.settings, self.currentscreen)
        self.infoscreen = InfoScreen(self, self.settings)

    def setup_window(self):
        self.window.attributes('-topmost', True)
        self.window.geometry(self.standard_size)
        self.window.title("Bottenkraker Snipetool")
        self.window.wm_iconbitmap('images/icon.ico')

        # Bar
        bar_canvas = self.bar.setup_window()
        bar_canvas.pack(side="bottom")

        # Main screen
        # Info
        self.info_frame = self.infoscreen.setup_window()
        self.info_frame.place(x=0, y=0)
        # Settings
        self.settings_frame = self.settingsscreen.setup_window()
        self.settings_frame.place(x=0, y=0)
        # Input and information
        self.mainscreen_frame = self.mainscreen.setup_window()
        self.mainscreen_frame.place(x=0, y=0)
        self.mainscreen_frame.tkraise()
        self.currentscreen[0] = "main"

        # Sidebar
        sidebar = self.sidebar.setup_window(self.settingsscreen, self.infoscreen, self.mainscreen)
        sidebar.pack(side="right", pady=(5, 0))

        # Apply theme
        self.settingsscreen.theme.apply_colors(self.window)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run(self):
        self.mainscreen.start()
        # self.time_selector.start()
        self.bar.start(self.snipe_time, self.clock)

    def on_closing(self):
        self.mainscreen.stop()
        self.bar.stop()
        self.window.destroy()
        self.settings.save_settings("settings/snipetool_config.yaml")

    def on_resize(self, event):
        if (event.widget == self.window):
            self.bar.on_resize(event)
            self.sidebar.on_resize(event)
            self.settingsscreen.on_resize(event)
            self.mainscreen.on_resize(event)
            self.infoscreen.on_resize(event)

    def setup(self):
        self.setup_window()
        self.run()
        self.window.mainloop()

tool = SnipeTool()
tool.setup()
