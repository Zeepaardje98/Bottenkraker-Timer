import tkinter as tk

class SettingsScreen:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root.window, width=self.root.window.winfo_width() - self.root.sidebar.width,
                                                height=self.root.window.winfo_height() - self.root.bar.bar_height - 4)#, background="green")
        self.frame.pack_propagate(False)

    def on_resize(self, event):
        self.frame.config(width=self.root.window.winfo_width() - self.root.sidebar.width,
                          height=self.root.window.winfo_height() - self.root.bar.bar_height - 4)

    def setup_window(self):
        return self.frame
