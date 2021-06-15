#!/usr/bin/env python3
import tkinter as tk

from widgets.bar import Bar
from widgets.mainscreen import MainScreen
from widgets.settingsmenu import SettingsScreen
from widgets.sidebar_settings import SettingsButton
from widgets.sidebar_github import Ghub
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

        self.bar = Bar(self.window, Settings(self.settings.get_settings(['bar'], {})))
        self.sidebar = tk.Frame(self.window)#, background="red")

        self.mainscreen = MainScreen(self)
        self.settingsscreen = SettingsScreen(self)

        self.ghublink = Ghub(self.sidebar, Settings(self.settings.get_settings(['ghub'], {})))
        self.settingsbutton = SettingsButton(self.sidebar, self.settingsscreen.frame, self.mainscreen.frame)


    def setup_window(self):
        self.window.attributes('-topmost', True)
        self.window.geometry("350x193")
        self.window.title("Bottenkraker Snipetool")
        self.window.wm_iconbitmap('images/icon.ico')


        # Bar
        bar_canvas = self.bar.setup_window()
        bar_canvas.pack(side="bottom")

        # Settings
        self.settings_frame = self.settingsscreen.setup_window()
        self.settings_frame.place(x=0, y=0)
        # Input and information
        self.mainscreen_frame = self.mainscreen.setup_window()
        self.mainscreen_frame.place(x=0, y=0)
        self.mainscreen_frame.tkraise()

        # self.settingsmenu.change_theme(self.window, True)

        # Sidebar
        settings_btn = self.settingsbutton.setup_window()
        settings_btn.grid(row=0, column=0, pady=(2, 2))

        ghub_btn = self.ghublink.setup_window()
        ghub_btn.grid(row=1, column=0, pady=(2, 2))

        self.sidebar.pack(side="right")

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
            self.settingsscreen.on_resize(event)
            self.mainscreen.on_resize(event)

    def setup(self):
        self.setup_window()
        self.run()
        self.window.mainloop()

tool = SnipeTool()
tool.setup()
