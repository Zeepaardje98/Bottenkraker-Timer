import tkinter as tk
import webbrowser

from help_funcs.helper import open_image

class Ghub:
    def __init__(self, window, settings):
        self.window = window
        self.settings = settings

        self.logo = None
        self.btn = None

    def github(self):
        webbrowser.open(self.settings.get_settings(['link']))

    def setup_window(self):
        self.logo = open_image(self.settings.get_settings(['image']), (20,20))
        self.btn = tk.Button(self.window, image=self.logo, width=20, height=20, relief='flat', bd=0, command=self.github)

        return self.btn

    def change_logo(self, path):
        self.logo = open_image(path, (20,20))
        self.btn.config(image=self.logo)
