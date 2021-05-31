#!/usr/bin/env python3
import datetime
import math
import tkinter as tk

from widgets.bar import Bar
from widgets.entries import Entries
from widgets.timesync import Timesync
from settings import Settings

class SnipeTool:
    settings = Settings()
    settings.load_settings("settings/snipetool_config.yaml")

    window = tk.Tk()

    entries = Entries(window)
    time_selector = Timesync(window, Settings(settings.get_settings(['timesync'])))
    bar = Bar(window, Settings(settings.get_settings(['bar'])))

    def setup_window(self):
        self.window.attributes('-topmost', True)
        self.window.geometry("404x152")
        self.window.title("Bottenkraker Snipetool")
        self.window.wm_iconbitmap('images/icon.ico')

        selector = self.time_selector.setup_window()
        selector.place(x=225, y=10)

        entry_frame = self.entries.setup_window()
        entry_frame.place(x=55, y=10)

        bar_canvas = self.bar.setup_window()
        bar_canvas.place(x=0, y=110)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run(self):
        self.time_selector.start()
        self.bar.start(self.time_selector, self.entries)

    def on_closing(self):
        self.time_selector.stop()
        self.bar.stop()
        self.window.destroy()

    def setup(self):
        self.setup_window()
        self.run()
        self.window.mainloop()

tool = SnipeTool()
tool.setup()
