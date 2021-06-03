#!/usr/bin/env python3
import tkinter as tk

from widgets.bar import Bar
from widgets.entries import Entries
from widgets.timesync import Timesync
from widgets.settingsmenu import SettingsMenu
from settings import Settings

class SnipeTool:
    def __init__(self):
        self.settings = Settings()
        self.settings.load_settings("settings/snipetool_config.yaml")
        self.window = tk.Tk()

        # Some variables which can be changed by the widgets. Which is why we
        # need to pass these variables by reference instead of by value. Thus
        # we use a mutable variable type
        self.snipe_time = []
        self.clock = []

        self.entries = Entries(self.window, self.snipe_time, Settings(self.settings.get_settings(['entries'])))
        self.time_selector = Timesync(self.window, self.clock, Settings(self.settings.get_settings(['timesync'])))
        self.bar = Bar(self.window, Settings(self.settings.get_settings(['bar'])))
        self.settingsmenu = SettingsMenu(self, self.window, self.settings)


    def setup_window(self):
        self.window.attributes('-topmost', True)
        self.window.geometry("404x152")
        self.window.title("Bottenkraker Snipetool")
        self.window.wm_iconbitmap('images/icon.ico')

        # x 225 - 365
        selector = self.time_selector.setup_window()
        selector.place(x=225, y=10)

        entry_frame = self.entries.setup_window()
        entry_frame.place(x=55, y=10)

        bar_canvas = self.bar.setup_window()
        bar_canvas.place(x=0, y=110)

        settings_btn = self.settingsmenu.setup_window()
        settings_btn.place(x=375, y=10)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run(self):
        self.time_selector.start()
        self.bar.start(self.snipe_time, self.clock)

    def on_closing(self):
        self.time_selector.stop()
        self.bar.stop()
        self.window.destroy()
        self.settings.save_settings("settings/snipetool_config.yaml")

    def setup(self):
        self.setup_window()
        self.run()
        self.window.mainloop()

tool = SnipeTool()
tool.setup()
