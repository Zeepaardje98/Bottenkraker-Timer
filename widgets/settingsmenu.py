import tkinter as tk

from widgets.settingsmenu_barcolor import BarColor
from widgets.settingsmenu_theme import Theme

from settings import Settings

class SettingsScreen:
    def __init__(self, root, settings):
        self.root = root
        self.frame = tk.Frame(self.root.window, width=self.root.window.winfo_width() - self.root.sidebar.width,
                                                height=self.root.window.winfo_height() - self.root.bar.bar_height - 4)#, background="green")
        self.frame.grid_propagate(False)
        self.settings = settings

        self.barcolors = BarColor(self.root, self.frame, Settings(self.settings.get_settings(['bar', 'colors'], {})))
        self.theme = Theme(self.root, self.frame, self.settings)

    def on_resize(self, event):
        self.frame.config(width=self.root.window.winfo_width() - self.root.sidebar.width,
                          height=self.root.window.winfo_height() - self.root.bar.bar_height - 4)

    def setup_window(self):
        color_frame = self.barcolors.setup_window()
        color_frame.grid(row=0, column=0, padx=(10,0), pady=(5,0), sticky='W')
        theme_frame = self.theme.setup_window()
        theme_frame.grid(row=1, column=0, padx=(10,0), pady=(5,0), sticky='W')
        return self.frame
