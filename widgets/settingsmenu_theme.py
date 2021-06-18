import tkinter as tk

from settings import Settings

class Theme:
    def __init__(self, root, parent, settings):
        self.root = root
        self.parent = parent
        self.settings = settings

    def setup_window(self):
        theme_frame = tk.Frame(self.parent)

        label = tk.Label(theme_frame, text="Theme:", anchor='w')
        label.grid(row=0, column=0)
        sv = tk.StringVar(theme_frame, self.settings.get_settings(['selected_theme']))
        entry = tk.Entry(theme_frame, textvariable=sv, width=10)
        entry.grid(row=0, column=1)

        btn_frame = tk.Frame(theme_frame, width=100, height=28)
        submit_btn = tk.Button(btn_frame, text='Save', command=lambda: self.submit_theme(sv))
        submit_btn.place(x=0, y=0, width=50, height=28)
        empty_btn = tk.Button(btn_frame, text='Empty', command=lambda: self.empty_theme(sv))
        empty_btn.place(x=50, y=0, width=50, height=28)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=(3,0))

        return theme_frame

    def valid_theme(self, string):
        if string in self.settings.get_settings(['themes']).keys():
            return True
        return False

    def apply_theme(self, widget):
        theme = self.settings.get_settings(['selected_theme'])
        if theme == 'default':
            return
        if parent:
            widget.config(background = self.settings.get_settings(['themes', theme, 'background']))

        if len(widget.children.values()) < 0:
            return
        for child in widget.children.values():
            self.apply_theme(child, False)
            child.config(background = self.settings.get_settings(['themes', theme, 'background']))
        return

    def submit_theme(self, sv):
        if self.valid_theme(sv.get()):
            print(True)
        else:
            print(False)
