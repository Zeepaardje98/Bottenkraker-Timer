import tkinter as tk
import webbrowser

from help_funcs.helper import open_image


class Ghub:
    def __init__(self, window, settings):
        self.window = window
        self.settings = settings

        self.logo = None

    def github(self):
        webbrowser.open(self.settings.get_settings(['link']))

    def setup_window(self):
        self.logo = open_image(self.settings.get_settings(['image']), (20,20))
        settings_btn = tk.Button(self.window, image=self.logo, width=20, height=20, relief='flat', command=self.github)

        return settings_btn
