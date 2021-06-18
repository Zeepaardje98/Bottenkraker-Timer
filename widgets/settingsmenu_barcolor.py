import tkinter as tk
import re

def valid_color(string):
    regex = re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
    colors = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta", "orange", "grey"]
    if string in colors or re.search(regex, string):
        return True
    return False

class BarColor:
    def __init__(self, root, parent, settings):
        self.root = root
        self.parent = parent
        self.settings = settings

    def submit_barcolors(self, stringvars):
        for stringvar in stringvars:
            if valid_color(stringvar.get()):
                self.settings.update_settings([str(stringvar)], stringvar.get())
                # The background color of the bar won't get updated
                # automatically. So do this manually
                if str(stringvar) == "background":
                    self.root.bar.bar_canvas.configure(bg=stringvar.get())

    def setup_window(self):
        color_frame = tk.Frame(self.parent)
        ec_label = tk.Label(color_frame, text="Empty Color:", anchor='w')
        ec_label.grid(row=0, column=0, sticky='W')
        ec_sv = tk.StringVar(self.parent, self.settings.get_settings(['background']), name="background")
        ec_entry = tk.Entry(color_frame, textvariable=ec_sv, width=10)
        ec_entry.grid(row=0, column=1)
        fc_label = tk.Label(color_frame, text="Fill Color:", anchor='w')
        fc_label.grid(row=1, column=0, sticky='W')
        fc_sv = tk.StringVar(self.parent, self.settings.get_settings(['fill']), name="fill")
        fc_entry = tk.Entry(color_frame, textvariable=fc_sv, width=10)
        fc_entry.grid(row=1, column=1)
        dc_label = tk.Label(color_frame, text="Done Color:", anchor='w')
        dc_label.grid(row=2, column=0, sticky='W')
        dc_sv = tk.StringVar(self.parent, self.settings.get_settings(['fill_done']), name="fill_done")
        dc_entry = tk.Entry(color_frame, textvariable=dc_sv, width=10)
        dc_entry.grid(row=2, column=1)

        stringvars = [ec_sv, fc_sv, dc_sv]

        btn_frame = tk.Frame(color_frame, width=100, height=28)
        submit_btn = tk.Button(btn_frame, text='Save', command=lambda: self.submit_barcolors(stringvars))
        submit_btn.place(x=0, y=0, width=50, height=28)
        empty_btn = tk.Button(btn_frame, text='Empty', command=lambda: self.empty_barcolors(stringvars))
        empty_btn.place(x=50, y=0, width=50, height=28)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=(3,0))


        return color_frame
