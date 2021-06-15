import tkinter as tk
from widgets.mainscreen_entries import Entries
from widgets.mainscreen_timesync import Timesync
from settings import Settings

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root.window, width=self.root.window.winfo_width() - self.root.sidebar.width,
                                                height=self.root.window.winfo_height() - self.root.bar.bar_height - 4)#, background="red")
        self.frame.grid_propagate(False)

        self.entries = Entries(self.frame, self.root.snipe_time, Settings(self.root.settings.get_settings(['entries'], {})))
        self.time_selector = Timesync(self.frame, self.root.clock, Settings(self.root.settings.get_settings(['timesync'], {})))

    def on_resize(self, event):
        self.frame.config(width=self.root.window.winfo_width() - self.root.sidebar.width,
                          height=self.root.window.winfo_height() - self.root.bar.bar_height - 4)
        # print(self.frame.winfo_width(), self.frame.winfo_height())

    def setup_window(self):
        entry_frame = self.entries.setup_window()
        entry_frame.grid(row=0, column=0, columnspan=3, padx=(10, 0), pady=(5, 0))

        selector, canvas = self.time_selector.setup_window()
        canvas.grid(row=0, column=3)
        selector.grid(row=1, column=2, columnspan=2)

        return self.frame

    def start(self):
        self.time_selector.start()

    def stop(self):
        self.time_selector.stop()
