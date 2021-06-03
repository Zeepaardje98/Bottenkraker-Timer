import datetime
import re
import tkinter as tk


def test():
    print("test")


class Entries:
    def __init__(self, window, entries_ref, settings):
        self.window = window
        self.settings = settings

        self.st_entry = None
        self.sm_entry = None
        self.st_entry_white = True
        self.sm_entry_white = True

        self.snipe_time = entries_ref
        self.snipe_time += [0]

        self.sv_formats = [re.compile('^\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}$'),
                           re.compile('^\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}:\d{1,3}$'),
                           re.compile('^\d{13,}\.\d{1,3}$'),
                           re.compile('^\d{1,3}$')]

    def update_vars(self, stringvar):
        if str(stringvar) == "SNIPETIME":
            entry_white = True
            string = stringvar.get()
            if self.sv_formats[0].match(string):
                self.snipe_time[0] = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S").timestamp()
            elif self.sv_formats[1].match(string):
                self.snipe_time[0] = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S:%f").timestamp()
            # TODO: We should be able to paste a timestamp, this has not yet been tested
            elif self.sv_formats[2].match(string):
                self.snipe_time[0] = float(string)
            elif string == '':
                entry_white = True
            else:
                entry_white = False

            # Change entry color based on right/wrong input
            if not entry_white and self.st_entry_white:
                self.st_entry.config({"background": self.settings.get_settings(['wrong_color'])})
                self.st_entry_white = False
            elif entry_white and not self.st_entry_white:
                self.st_entry.config({"background": self.settings.get_settings(['right_color'])})
                self.st_entry_white = True

        elif str(stringvar) == "SNIPEMS":
            entry_white = True
            string = stringvar.get()
            if self.sv_formats[3].match(string):
                self.snipe_time[0] = int(self.snipe_time[0]) + (int(string) % 1000) / 1000
            elif string == '':
                entry_white = True
            else:
                entry_white = False

            # Change entry color based on right/wrong input
            if not entry_white and self.sm_entry_white:
                self.sm_entry.config({"background": self.settings.get_settings(['wrong_color'])})
                self.sm_entry_white = False
            elif entry_white and not self.sm_entry_white:
                self.sm_entry.config({"background": self.settings.get_settings(['right_color'])})
                self.sm_entry_white = True

    def setup_window(self):
        sv_time = tk.StringVar(name="SNIPETIME")
        sv_ms = tk.StringVar(name="SNIPEMS")
        sv_time.trace("w", lambda name, index, mode, sv_time=sv_time: self.update_vars(sv_time))
        sv_ms.trace("w", lambda name, index, mode, sv_ms=sv_ms: self.update_vars(sv_ms))

        entry_frame = tk.Frame(self.window, width=80 + 10 + 150, height=25 + 5 + 25)
        # Snipe Time label
        st_label = tk.Label(entry_frame, text="Snipe Time:", anchor='w')
        st_label.place(x=0, y=0, width=80, height=25)
        # Snipe Ms label
        sm_label = tk.Label(entry_frame, text="Snipe Ms:", anchor='w')
        sm_label.place(x=0, y=25 + 5, width=80, height=25)
        # Snipe Time entry
        self.st_entry = tk.Entry(entry_frame, textvariable=sv_time, width=150)
        self.st_entry.place(in_=st_label, relx=1.0, x=10, y=-1)
        # Snipe Ms entry
        self.sm_entry = tk.Entry(entry_frame, textvariable=sv_ms, width=150)
        self.sm_entry.place(in_=sm_label, relx=1.0, x=10, y=-1)

        return entry_frame
