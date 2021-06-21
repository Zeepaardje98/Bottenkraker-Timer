import tkinter as tk

from help_funcs.helper import open_image

class Info:
    def __init__(self, root, window, settings):
        self.root = root
        self.window = window
        self.settings = settings

        self.logo = None
        self.btn = None

    def info(self):
        print("open info screen")

    def change_logo(self, path):
        self.logo = open_image(path, (25,25))
        self.btn.config(image=self.logo)

    def setup_window(self):
        theme = self.settings.get_settings(["selected_theme"])
        self.logo = open_image(self.settings.get_settings(["themes", theme, "info_im"]), (25,25))
        self.btn = tk.Button(self.window, image=self.logo, width=20, height=20, relief='flat', bd=0, command=self.info)

        return self.btn
