import tkinter as tk

from help_funcs.helper import open_image

class SettingsButton:
    def __init__(self, parent, settings, cur):
        self.parent = parent
        self.settings = settings
        self.currentscreen = cur

        self.new = None
        self.old = None

        self.logo = None
        self.settings_btn = None

    def setup_window(self, screen1, screen2):
        theme = self.settings.get_settings(["selected_theme"])
        self.logo = open_image(self.settings.get_settings(["themes", theme, "settings_im"]), (25,25))
        self.settings_btn = tk.Button(self.parent, image=self.logo, width=20, height=20, relief='flat', bd=0, command=self.show_popup)
        self.new = screen1
        self.old = screen2

        return self.settings_btn

    def change_logo(self, path):
        self.logo = open_image(path, (25,25))
        self.settings_btn.config(image=self.logo)

    def show_popup(self):
        if self.currentscreen[0] != "settings":
            self.currentscreen[0] = "settings"
            self.new.tkraise()
        else:
            self.old.tkraise()
            self.currentscreen[0] = "main"
