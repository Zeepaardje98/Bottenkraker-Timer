import tkinter as tk
import webbrowser

from help_funcs.helper import open_image

class Donate:
    def __init__(self, window, settings):
        self.window = window
        self.settings = settings

        self.logo = None
        self.btn = None

    def link(self):
        webbrowser.open("https://www.paypal.com/donate?business=ricardo.van.aken%40hotmail.nl&no_recurring=0&currency_code=EUR")

    def setup_window(self):
        theme = self.settings.get_settings(["selected_theme"])
        self.logo = open_image(self.settings.get_settings(["themes", theme, "donate_im"]), (25,25))
        self.btn = tk.Button(self.window, image=self.logo, width=20, height=20, relief='flat', bd=0, command=self.link)

        return self.btn

    def change_logo(self, path):
        self.logo = open_image(path, (25,25))
        self.btn.config(image=self.logo)
