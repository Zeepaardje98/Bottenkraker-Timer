#!/usr/bin/env python3
import tkinter as tk

from widgets.bar import Bar
from widgets.entries import Entries
from widgets.timesync import Timesync
from widgets.settingsmenu import SettingsMenu
from widgets.githublink import Ghub
from settings import Settings

class SnipeTool:
    def __init__(self):
        self.settings = Settings()
        self.settings.load_settings("settings/snipetool_config.yaml")

        self.window = tk.Tk()
        self.window.bind("<Configure>", self.on_resize)

        self.widgetframe = tk.Frame(self.window)#, background="green")
        self.sidebar = tk.Frame(self.window)#, background="red")

        # Some variables which can be changed by the widgets. Which is why we
        # need to pass these variables by reference instead of by value. Thus
        # we use a mutable variable type
        self.snipe_time = []
        self.clock = []

        self.entries = Entries(self.widgetframe, self.snipe_time, Settings(self.settings.get_settings(['entries'], {})))
        self.time_selector = Timesync(self.widgetframe, self.clock, Settings(self.settings.get_settings(['timesync'], {})))
        self.bar = Bar(self.window, Settings(self.settings.get_settings(['bar'], {})))
        self.ghublink = Ghub(self.sidebar, Settings(self.settings.get_settings(['ghub'], {})))
        self.settingsmenu = SettingsMenu(self, self.window, self.settings)


    def setup_window(self):
        self.window.attributes('-topmost', True)
        self.window.geometry("350x193")
        self.window.title("Bottenkraker Snipetool")
        self.window.wm_iconbitmap('images/icon.ico')

        # Bar
        bar_canvas = self.bar.setup_window()
        bar_canvas.pack(side="bottom")#, expand=True, fill="x")

        # Input and information
        entry_frame = self.entries.setup_window()
        entry_frame.grid(row=0, column=0, columnspan=3, pady=(10, 0))

        selector, canvas = self.time_selector.setup_window()
        canvas.grid(row=0, column=3)
        selector.grid(row=1, column=2, columnspan=2)

        self.widgetframe.pack(side="left", padx=(40, 0))

        # Sidebar
        settings_btn = self.settingsmenu.setup_window()
        settings_btn.grid(row=0, column=0, pady=(2, 2))

        ghub_btn = self.ghublink.setup_window()
        ghub_btn.grid(row=1, column=0, pady=(2, 2))

        self.sidebar.pack(side="right", padx=(0, 10))

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run(self):
        self.time_selector.start()
        self.bar.start(self.snipe_time, self.clock)

    def on_closing(self):
        self.time_selector.stop()
        self.bar.stop()
        self.window.destroy()
        self.settings.save_settings("settings/snipetool_config.yaml")

    def on_resize(self, event):
        if (event.widget == self.window):
            self.bar.on_resize(event)
            self.settingsmenu.on_resize(event)

    def setup(self):
        self.setup_window()
        self.run()
        self.window.mainloop()

tool = SnipeTool()
tool.setup()
