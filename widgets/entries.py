import datetime
import re
import tkinter as tk


def test():
    print("test")


class Entries:
    def __init__(self, window, entries_ref, settings):
        self.window = window
        self.settings = settings
        self.defaults = settings.get_settings(['defaults'], {'arrival': 'vandaag 04:20:00', 'ms': 0, 'walktime': '00:00:00'})

        self.st_entry = None
        self.sm_entry = None
        self.wt_entry = None

        self.st_entry_white = True
        self.sm_entry_white = True
        self.wt_entry_white = True

        self.snipe_time = entries_ref
        self.snipe_time += [0]

        self.arrival_time = 0
        self.send_time = None
        self.ms = 0
        self.walk_time = 0

        self.sv_formats = [re.compile('^\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}$'),          # yyyy-mm-dd hh:mm:ss
                           re.compile('^\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}:\d{1,3}$'),  # yyyy-mm-dd hh:mm:ss:xxx
                           re.compile('^\d{13,}\.\d{1,3}$'),                                        # timestamp
                           re.compile('^\d{1,3}$'),                                                 # xxx
                           re.compile('^\d{1,2}:\d{1,2}:\d{1,2}$'),                                 # hh:mm:ss
                           re.compile('^(vandaag)\s\d{1,2}:\d{1,2}:\d{1,2}$'),                      # vandaag hh:mm:ss
                           re.compile('^(morgen)\s\d{1,2}:\d{1,2}:\d{1,2}$')]                       # morgen hh:mm:ss

    def update_vars(self, stringvar):
        if str(stringvar) == "SNIPETIME":
            entry_white = True
            string = stringvar.get()
            if self.sv_formats[0].match(string):
                self.arrival_time = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S").timestamp()
                self.snipe_time[0] = (int(self.arrival_time) - int(self.walk_time)) + self.ms
                self.send_time = datetime.datetime.fromtimestamp(self.snipe_time[0]).strftime("%H:%M:%S.%f")[:-3]
                self.send_label.config(text=f'Send: {self.send_time}')


            elif self.sv_formats[1].match(string):
                self.arrival_time = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S:%f").timestamp()
                self.snipe_time[0] = (int(self.arrival_time) - int(self.walk_time)) + self.ms
                self.send_time = datetime.datetime.fromtimestamp(self.snipe_time[0]).strftime("%H:%M:%S.%f")[:-3]
                self.send_label.config(text=f'Send: {self.send_time}')


            # TODO: We should be able to paste a timestamp, this has not yet been tested
            elif self.sv_formats[2].match(string):
                self.arrival_time = float(string)
                self.snipe_time[0] = (int(self.arrival_time) - int(self.walk_time)) + self.ms
                self.send_time = datetime.datetime.fromtimestamp(self.snipe_time[0]).strftime("%H:%M:%S.%f")[:-3]
                self.send_label.config(text=f'Send: {self.send_time}')

            # vandaag + time implementation
            elif self.sv_formats[5].match(string):
                string = f'{datetime.datetime.now().strftime("%Y-%m-%d")} {string[8:]}'
                self.arrival_time = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S").timestamp()
                self.snipe_time[0] = (int(self.arrival_time) - int(self.walk_time)) + self.ms
                self.send_time = datetime.datetime.fromtimestamp(self.snipe_time[0]).strftime("%H:%M:%S.%f")[:-3]
                self.send_label.config(text=f'Send: {self.send_time}')

            # morgen + time implementation
            elif self.sv_formats[6].match(string):
                tmr = datetime.datetime.now() + datetime.timedelta(days=1)
                string = f'{tmr.strftime("%Y-%m-%d")} {string[7:]}'
                self.arrival_time = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S").timestamp()
                self.snipe_time[0] = (int(self.arrival_time) - int(self.walk_time)) + self.ms
                self.send_time = datetime.datetime.fromtimestamp(self.snipe_time[0]).strftime("%H:%M:%S.%f")[:-3]
                self.send_label.config(text=f'Send: {self.send_time}')
            elif string != '':
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
                self.ms = (int(string) % 1000) / 1000
                self.snipe_time[0] = (int(self.arrival_time) - int(self.walk_time)) + self.ms
                self.send_time = datetime.datetime.fromtimestamp(self.snipe_time[0]).strftime("%H:%M:%S.%f")[:-3]
                self.send_label.config(text=f'Send: {self.send_time}')
            elif string != '':
                entry_white = False


            # Change entry color based on right/wrong input
            if not entry_white and self.sm_entry_white:
                self.sm_entry.config({"background": self.settings.get_settings(['wrong_color'])})
                self.sm_entry_white = False
            elif entry_white and not self.sm_entry_white:
                self.sm_entry.config({"background": self.settings.get_settings(['right_color'])})
                self.sm_entry_white = True

        elif str(stringvar) == "WALKTIME":
            entry_white = True
            string = stringvar.get()

            if self.sv_formats[4].match(string):
                at_hms    = string.split(":")
                self.walk_time = ((((int(at_hms[0]) * 60) + int(at_hms[1])) * 60 + int(at_hms[2])))
                self.snipe_time[0] = (int(self.arrival_time) - int(self.walk_time)) + self.ms
                self.send_time = datetime.datetime.fromtimestamp(self.snipe_time[0]).strftime("%H:%M:%S.%f")[:-3]
                self.send_label.config(text=f'Send: {self.send_time}')
            elif string != '':
                entry_white = False

            if not entry_white and self.wt_entry_white:
                self.wt_entry.config({"background": self.settings.get_settings(['wrong_color'])})
                self.wt_entry_white = False
            elif entry_white and not self.wt_entry_white:
                self.wt_entry.config({"background": self.settings.get_settings(['right_color'])})
                self.wt_entry_white = True

    def setup_window(self):
        sv_time = tk.StringVar(name="SNIPETIME")
        sv_walk = tk.StringVar(name="WALKTIME")
        sv_ms = tk.StringVar(name="SNIPEMS")

        sv_time.trace("w", lambda name, index, mode, sv_time=sv_time: self.update_vars(sv_time))
        sv_walk.trace("w", lambda name, index, mode, sv_time=sv_time: self.update_vars(sv_walk))
        sv_ms.trace("w", lambda name, index, mode, sv_ms=sv_ms: self.update_vars(sv_ms))

        entry_frame = tk.Frame(self.window, width=80 + 10 + 150, height=85)
        # Sending time
        # Needs to be first because of update order
        self.send_label = tk.Label(entry_frame, text="Send: 00:00:00:000", anchor='w')
        self.send_label.place(x=0, y=75 + 5, width=200, height=25)
        self.send_label.config(font=("calibri 12 bold"))

        # Snipe Time label
        st_label = tk.Label(entry_frame, text="Snipe Time:", anchor='w')
        st_label.place(x=0, y=0, width=80, height=25)
        # Walk Time label
        wt_label = tk.Label(entry_frame, text="Walk Time:", anchor='w')
        wt_label.place(x=0, y=25 + 5, width=80, height=25)
        # Snipe Ms label
        sm_label = tk.Label(entry_frame, text="Snipe Ms:", anchor='w')
        sm_label.place(x=0, y=55 + 5, width=80, height=25)

        # Snipe Time entry
        self.st_entry = tk.Entry(entry_frame, textvariable=sv_time, width=150)
        self.st_entry.place(in_=st_label, relx=1.0, x=10, y=-1)
        self.st_entry.insert(-1, self.defaults['arrival'])
        # Walk Time entry
        self.wt_entry = tk.Entry(entry_frame, textvariable=sv_walk, width=150)
        self.wt_entry.place(in_=wt_label, relx=1.0, x=10)
        self.wt_entry.insert(-1, self.defaults['walktime'])
        # Snipe Ms entry
        self.sm_entry = tk.Entry(entry_frame, textvariable=sv_ms, width=150)
        self.sm_entry.place(in_=sm_label, relx=1.0, x=10, y=-1)
        self.sm_entry.insert(-1, self.defaults['ms'])

        return entry_frame
