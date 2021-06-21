import tkinter as tk

from help_funcs.helper import open_image

class Info:
    def __init__(self, root, window, settings, cur):
        self.root = root
        self.window = window
        self.settings = settings
        self.currentscreen = cur

        self.new = None
        self.old = None

        self.logo = None
        self.btn = None

    def info(self):
        print("open info screen")

    def change_logo(self, path):
        self.logo = open_image(path, (25,25))
        self.btn.config(image=self.logo)

    def setup_window(self, screen1, screen2):
        theme = self.settings.get_settings(["selected_theme"])
        self.logo = open_image(self.settings.get_settings(["themes", theme, "info_im"]), (25,25))
        self.btn = tk.Button(self.window, image=self.logo, width=20, height=20, relief='flat', bd=0, command=self.show_popup)
        self.new = screen1
        self.old = screen2

        return self.btn

    def show_popup(self):
        if self.currentscreen[0] != "info":
            self.currentscreen[0] = "info"
            self.new.tkraise()
        else:
            self.old.tkraise()
            self.currentscreen[0] = "main"
