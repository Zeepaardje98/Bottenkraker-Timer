import tkinter as tk

from help_funcs.helper import open_image

class SettingsButton:
    def __init__(self, parent, settings):
        self.parent = parent
        self.settings = settings

        self.new = None
        self.old = None

        self.opened = False
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
        if not self.opened:
            self.opened = True
            self.new.tkraise()
        else:
            self.opened = False
            self.old.tkraise()
