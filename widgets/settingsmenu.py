import tkinter as tk
from PIL import ImageTk, Image

def open_image(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

class SettingsMenu:
    def __init__(self, window, settings):
        self.window = window
        self.settings = settings

        self.opened = False
        self.frame = None

        self.logo = None

    def show_popup(self):
        if not self.opened:
            self.opened = True
            self.frame.place(x=0, y=0)
        else:
            self.opened = False
            self.frame.place_forget()


    def setup_window(self):
        self.setup_settings()

        self.logo = open_image("images/settings_dark.png", (20,20))
        settings_btn = tk.Button(self.window, image=self.logo, width=20, height=20, relief='flat', command=self.show_popup)
        return settings_btn

    def setup_settings(self):
        self.frame = tk.Frame(self.window, width=self.window.winfo_width(), height=self.window.winfo_height())

        color_frame = tk.Frame(self.window, width=80 + 10 + 150, height=25)

        sv_ec_entry = tk.StringVar(name="EC_ENTRY")
        ec_label = tk.Label(color_frame, text="Empty color:", anchor='w')
        ec_label.place(x=0, y=25 + 5, width=80, height=25)
        # Snipe Time entry
        ec_entry = tk.Entry(color_frame, textvariable=sv_ec_entry, width=150)
        ec_entry.place(in_=ec_label, relx=1.0, x=10)

        # return settings_frame
