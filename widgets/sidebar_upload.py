import tkinter as tk
import re
import json

from help_funcs.helper import open_image

class Upload:
    def __init__(self, root, window, settings):
        self.root = root
        self.window = window
        self.settings = settings

        self.logo = None
        self.btn = None

    def upload(self):
        dict = {}
        entries = self.root.mainscreen.entries
        try:
            dict = json.loads(self.root.window.clipboard_get())
        except:
            print("no valid input has been selected for uploading")

        if dict:
            if "snipe_time" in dict.keys():
                entries.sv_time.set(dict["snipe_time"])
            if "snipe_ms" in dict.keys():
                entries.sv_ms.set(dict["snipe_ms"])
            if "walk_time" in dict.keys():
                entries.sv_walk.set(dict["walk_time"])
# {"walk_time": "00:05:00", "snipe_ms": "500", "snipe_time": "vandaag 17:00:00"}


    def change_logo(self, path):
        self.logo = open_image(path, (25,25))
        self.btn.config(image=self.logo)

    def setup_window(self):
        theme = self.settings.get_settings(["selected_theme"])
        self.logo = open_image(self.settings.get_settings(["themes", theme, "upload_im"]), (25,25))
        self.btn = tk.Button(self.window, image=self.logo, width=20, height=20, relief='flat', bd=0, command=self.upload)

        return self.btn
