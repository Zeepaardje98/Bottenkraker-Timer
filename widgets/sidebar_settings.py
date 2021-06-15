import tkinter as tk

from help_funcs.helper import open_image

class SettingsButton:
    def __init__(self, parent, new, old):
        self.parent = parent
        self.new = new
        self.old = old

        self.opened = False
        self.logo = None


    def setup_window(self):
        self.logo = open_image("images/settings_dark.png", (20,20))
        settings_btn = tk.Button(self.parent, image=self.logo, width=20, height=20, relief='flat', command=self.show_popup)

        return settings_btn

    def show_popup(self):
        if not self.opened:
            print("open popup")
            self.opened = True
            self.new.tkraise()
        else:
            self.opened = False
            self.old.tkraise()
