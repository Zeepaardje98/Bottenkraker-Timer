import tkinter as tk

from help_funcs.helper import open_image

class SettingsButton:
    def __init__(self, parent):
        self.parent = parent
        self.new = None
        self.old = None

        self.opened = False
        self.logo = None

    def set_screens(self, new, old):
        self.new = new
        self.old = old

    def setup_window(self, screen1, screen2):
        self.logo = open_image("images/settings_dark.png", (20,20))
        settings_btn = tk.Button(self.parent, image=self.logo, width=20, height=20, relief='flat', command=self.show_popup)
        self.set_screens(screen1, screen2)

        return settings_btn

    def show_popup(self):
        if not self.opened:
            print("open popup")
            self.opened = True
            self.new.tkraise()
        else:
            self.opened = False
            self.old.tkraise()
