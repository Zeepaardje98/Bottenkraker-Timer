import tkinter as tk

from settings import Settings

class InfoScreen:
    def __init__(self, root, settings):
        self.root = root
        self.frame = tk.Frame(self.root.window, width=self.root.window.winfo_width() - self.root.sidebar.width,
                                                height=self.root.window.winfo_height() - self.root.bar.bar_height - 4, background="green")
        self.frame.grid_propagate(False)
        self.settings = settings

    def on_resize(self, event):
        self.frame.config(width=self.root.window.winfo_width() - self.root.sidebar.width,
                          height=self.root.window.winfo_height() - self.root.bar.bar_height - 4)

    def setup_window(self):
        string = ("Bottenkraker-Timer v1.1.2\n" +
                  "This tool is made by Bottenkraker/Ricardo\n\n" +
                  "Icons by  https://icons8.com")
        text = tk.Label(self.frame, text=string)
        text.grid(row=0, column=0, padx=(10,0), pady=(5,0), sticky='W')
        return self.frame
