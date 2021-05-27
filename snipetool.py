#!/usr/bin/env python3
import tkinter as tk
import datetime
from timesync import Clock

def test():
    print("test")
#
# class GUI:
#     window = tk.Tk()
#     window.attributes('-topmost',True)

class SnipeTool:
    window = tk.Tk()
    window.attributes('-topmost',True)

    clock = Clock(server='pool.ntp.org', interval=5)

    snipe_time = 0

    bar_canvas = None
    bar_text = None
    bar = None

    def update_vars(self, stringvar):
        if str(stringvar) == "SNIPETIME":
            time = int(datetime.datetime.strptime(stringvar.get(),'%Y-%m-%d %H:%M:%S:%f').timestamp() * 1000)
            print(time)
        elif str(stringvar) == "SNIPEMS":
            print("ms")
        self.snipe_time = time

    def update_timestamp(self):
        time = self.clock.time_ms()

        # Make a timestamp from the current server time and place it onto the
        # bar
        string = datetime.datetime.fromtimestamp(time/1000.0).strftime("%Y-%m-%d %H:%M:%S")
        self.bar_canvas.itemconfig(self.bar_text, text=string)

        # MilliSecond after which the new seconds start, and we should update
        # the timestamp again
        self.window.after(1000 - (time % 1000), self.update_timestamp)

    def update_bar(self):
        time = self.clock.time_ms()

        if (self.snipe_time > time - 1000) and (self.snipe_time > time):
            self.bar_canvas.itemconfig(self.bar, fill='green')

        fill = 1 + ((time - self.snipe_time) % 1000) / 2.5
        self.bar_canvas.coords(self.bar, 1, 1, fill, 41)
        self.window.after(20, self.update_bar)

    def setup_window(self):
        # Create Stringvars corresponding to the entrie fields
        snipe_time = tk.StringVar(name="SNIPETIME")
        snipe_ms = tk.StringVar(name="SNIPEMS")
        snipe_time.trace("w", lambda name, index, mode, snipe_time=snipe_time: self.update_vars(snipe_time))
        snipe_ms.trace("w", lambda name, index, mode, snipe_ms=snipe_ms: self.update_vars(snipe_ms))

        entry_frame = tk.Frame(self.window, width=80+10+150, height=25+5+25)
        entry_frame.pack(side = tk.TOP, padx=20, pady=10)
        # Snipe Time label
        st_label = tk.Label(entry_frame, text="Snipe Time:", anchor='w')
        st_label.place(x=0, y=0, width=80, height=25)
        # Snipe Ms label
        sm_label = tk.Label(entry_frame, text="Snipe Ms:", anchor='w')
        sm_label.place(x=0, y=25 + 5, width=80, height=25)
        # Snipe Time entry
        st_entry = tk.Entry(entry_frame, textvariable=snipe_time, validatecommand=test, width=150)
        st_entry.place(in_=st_label, relx=1.0, x=10)
        # Snipe Ms entry
        sm_entry = tk.Entry(entry_frame, textvariable=snipe_ms, validatecommand=test, width=150)
        sm_entry.place(in_=sm_label, relx=1.0, x=10)



        self.bar_canvas = tk.Canvas(self.window, width=400, height=40, background="grey")
        self.bar_canvas.pack()
        # Colored loading bar
        self.bar = self.bar_canvas.create_rectangle(1, 1, 201, 41, fill="orange", width=0)
        self.bar_text = self.bar_canvas.create_text((200, 20), font="calibri 20 bold", width=300)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.clock.stop()
        self.window.destroy()



    def setup(self):
        self.setup_window()
        self.update_bar()
        self.update_timestamp()
        self.window.mainloop()


tool = SnipeTool()
tool.setup()
# clock = Clock(interval=30)
