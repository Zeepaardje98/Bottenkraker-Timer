#!/usr/bin/env python3
import datetime
import math
import tkinter as tk

from bar import Bar
from entries import Entries
from timesync import Timesync


class SnipeTool:
    window = tk.Tk()
    entries = Entries(window)
    bar = Bar(window)
    time_selector = Timesync(window)

    def string_sync(self):
        clock = self.time_selector.clock
        last_synced = clock.last_synced
        time = clock.time_ms()
        diff = time - last_synced

        if diff < 60:
            return str(round(diff)) + " s"
        if diff >= 60:
            return str(math.floor(diff / 60)) + " m"

    def update_second(self):
        time = self.time_selector.clock.time_ms()

        # Make a timestamp from the current server time and place it onto the
        # bar
        string = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")
        self.bar.bar_canvas.itemconfig(self.bar.bar_text, text=string)

        # Update the symbol and text of last server sync
        if self.time_selector.clock.server_sync:
            self.time_selector.sync_symbol.delete(self.time_selector.current_symbol)
            self.time_selector.current_symbol = self.time_selector.sync_symbol.create_oval(2, 2, 11, 11, fill="green")
            self.time_selector.sync_symbol.itemconfig(self.time_selector.sync_text, text=self.string_sync())
        else:
            self.time_selector.sync_symbol.delete(self.time_selector.current_symbol)
            self.time_selector.current_symbol = self.time_selector.sync_symbol.create_oval(2, 2, 11, 11, fill="red")
            self.time_selector.sync_symbol.itemconfig(self.time_selector.sync_text, text="")

        # MilliSecond after which the new seconds start, and we should update
        # the timestamp again
        self.window.after(1000 - (round(time * 1000) % 1000), self.update_second)

    def update_bar(self):
        time = self.time_selector.clock.time_ms()
        self.bar.update_bar(time, self.entries.snipe_time)
        self.window.after(10, self.update_bar)

    def setup_window(self):
        self.window.attributes('-topmost', True)
        self.window.geometry("404x152")
        self.window.title("Bottenkraker Snipetool")
        self.window.wm_iconbitmap('images/icon.ico')

        selector = self.time_selector.setup_window()
        selector.place(x=225, y=10)
        # self.time_selector.canvas.create_image(0, 0, image=self.time_selector.file, anchor='nw')

        entry_frame = self.entries.setup_window()
        entry_frame.place(x=55, y=10)

        bar_canvas = self.bar.setup_window()
        bar_canvas.place(x=0, y=110)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.time_selector.clock.stop()
        self.window.destroy()

    def setup(self):
        self.setup_window()
        self.update_bar()
        self.update_second()
        self.window.mainloop()


tool = SnipeTool()
tool.setup()
