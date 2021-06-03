import tkinter as tk
from PIL import ImageTk, Image
import re

def open_image(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

class SettingsMenu:
    def __init__(self, parent, window, settings):
        self.window = window
        self.settings = settings
        self.parent = parent

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

    def submit_barcolors(self, stringvars):
        regex = re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
        colors = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta", "orange", "grey"]
        for stringvar in stringvars:
            if stringvar.get() in colors or re.search(regex, stringvar.get()):
                self.settings.update_settings(['bar', 'colors', str(stringvar)], stringvar.get())
                # The background color of the bar won't get updated
                # automatically. So do this manually
                if str(stringvar) == "background":
                    self.parent.bar.bar_canvas.configure(bg=stringvar.get())

    def submit_entries(self, stringvars):
        self.submit_barcolors(stringvars[0:3])


    def empty_entries(self, stringvars):
        print(stringvars.get())

    def setup_window(self):
        self.setup_settings()

        self.logo = open_image("images/settings_dark.png", (20,20))
        settings_btn = tk.Button(self.window, image=self.logo, width=20, height=20, relief='flat', command=self.show_popup)
        return settings_btn

    def setup_settings(self):
        self.frame = tk.Frame(self.window, width=self.window.winfo_width(), height=self.window.winfo_height())

        # bar color settings
        color_frame = tk.Frame(self.frame, width=80 + 10 + 80, height=90)
        ec_label = tk.Label(color_frame, text="Empty Color:", anchor='w')
        ec_label.place(x=0, y=0, width=80, height=25)
        ec_sv = tk.StringVar(self.window, self.settings.get_settings(['bar', 'colors', 'background']), name="background")
        ec_entry = tk.Entry(color_frame, textvariable=ec_sv)
        ec_entry.place(in_=ec_label, relx=1.0, x=10, y=-1, height=25, width=80)
        fc_label = tk.Label(color_frame, text="Fill Color:", anchor='w')
        fc_label.place(x=0, y=30, width=80, height=25)
        fc_sv = tk.StringVar(self.window, self.settings.get_settings(['bar', 'colors', 'fill']), name="fill")
        fc_entry = tk.Entry(color_frame, textvariable=fc_sv)
        fc_entry.place(in_=fc_label, relx=1.0, x=10, y=-1, height=25, width=80)
        dc_label = tk.Label(color_frame, text="Done Color:", anchor='w')
        dc_label.place(x=0, y=60, width=80, height=25)
        dc_sv = tk.StringVar(self.window, self.settings.get_settings(['bar', 'colors', 'fill_done']), name="fill_done")
        dc_entry = tk.Entry(color_frame, textvariable=dc_sv)
        dc_entry.place(in_=dc_label, relx=1.0, x=10, y=-1, height=25, width=80)
        color_frame.place(x=10, y=10)

        # StringVars of all the settings
        stringvars = [ec_sv, fc_sv, dc_sv]

        btn_frame = tk.Frame(self.frame, width=100, height=30)
        submit_btn = tk.Button(btn_frame, text='Save', command=lambda: self.submit_entries(stringvars))
        submit_btn.place(x=0, y=0, width=50, height=28)
        empty_btn = tk.Button(btn_frame, text='Empty', command=lambda: self.empty_entries(stringvars))
        empty_btn.place(x=50, y=0, width=50, height=28)

        btn_frame.place(x=290, y=110)
