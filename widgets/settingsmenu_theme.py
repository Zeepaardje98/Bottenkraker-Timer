import tkinter as tk

from settings import Settings

from help_funcs.helper import open_image

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
        selector = tk.OptionMenu(theme_frame, sv, *self.settings.get_settings(['themes']), command=lambda x: self.submit_theme(sv))
        selector.config(width=10)
        selector.grid(row=0, column=1)

        return theme_frame

    def valid_theme(self, string):
        if string in self.settings.get_settings(["themes"]).keys():
            return True
        return False

    def apply_colors(self, widget):
        theme = self.settings.get_settings(["selected_theme"])
        if (theme != "default"):
            if widget.winfo_class() in ["Tk", "Frame"]:
                widget.config(bg = self.settings.get_settings(['themes', theme, 'background']))

            elif widget.winfo_class() == "Label":
                widget.config(bg = self.settings.get_settings(['themes', theme, 'background']),
                              fg = self.settings.get_settings(['themes', theme, 'text']))

            elif widget.winfo_class() == "Canvas":
                widget.config(highlightbackground = self.settings.get_settings(['themes', theme, 'entry']))
                if (widget != self.root.bar.bar_canvas):
                    widget.config(bg = self.settings.get_settings(['themes', theme, 'background']))
                if (widget == self.root.mainscreen.time_selector.sync_symbol):
                    self.root.mainscreen.time_selector.sync_symbol.itemconfig(self.root.mainscreen.time_selector.sync_text, fill=self.settings.get_settings(['themes', theme, 'text']))

            elif widget.winfo_class() == "Entry":
                widget.config(relief="flat")
                widget.config(bg = self.settings.get_settings(['themes', theme, 'entry']),
                              fg = self.settings.get_settings(['themes', theme, 'text']))

            elif widget.winfo_class() == "Button":
                widget.config(relief="flat")
                if widget not in self.root.sidebar.frame.children.values():
                    widget.config(bg = self.settings.get_settings(['themes', theme, 'button']),
                                  fg = self.settings.get_settings(['themes', theme, 'text']),
                                  activebackground = self.settings.get_settings(['themes', theme, 'primary']))
                else:
                    widget.config(bg = self.settings.get_settings(['themes', theme, 'background']),
                                  activebackground = self.settings.get_settings(['themes', theme, 'background']))

            elif widget.winfo_class() == "Menubutton":
                widget.config(relief="flat")
                widget.config(bg = self.settings.get_settings(['themes', theme, 'button']),
                              fg = self.settings.get_settings(['themes', theme, 'text']),
                              activebackground = self.settings.get_settings(['themes', theme, 'primary']),
                              highlightcolor = self.settings.get_settings(['themes', theme, 'background']),
                              highlightbackground = self.settings.get_settings(['themes', theme, 'background']))

            elif widget.winfo_class() == "Menu":
                widget.config(relief="flat")
                widget.config(bg = self.settings.get_settings(['themes', theme, 'button']),
                              fg = self.settings.get_settings(['themes', theme, 'text']),
                              activebackground = self.settings.get_settings(['themes', theme, 'primary']),
                              relief="flat")

        if len(widget.children.values()) < 0:
            return
        for child in widget.children.values():
            self.apply_colors(child)
        return

    def change_images(self):
        theme = self.settings.get_settings(["selected_theme"])
        self.root.sidebar.settingsbutton.change_logo(self.settings.get_settings(['themes', theme, 'settings_im']))
        self.root.sidebar.ghublink.change_logo(self.settings.get_settings(['themes', theme, 'ghub_im']))
        self.root.sidebar.upload.change_logo(self.settings.get_settings(['themes', theme, 'upload_im']))
        self.root.sidebar.info.change_logo(self.settings.get_settings(['themes', theme, 'info_im']))

    def apply_theme(self):
        self.apply_colors(self.root.window)
        self.change_images()

    def submit_theme(self, sv):
        if self.valid_theme(sv.get()):
            self.settings.update_settings(['selected_theme'], sv.get())
            self.settings.update_settings(['entries', 'right_color'], self.settings.get_settings(['themes', sv.get(), 'entry']))
            self.apply_theme()

            # theme = self.settings.get_settings(["selected_theme"])
            # self.root.sidebar.ghublink.logo = open_image(self.settings.get_settings(['themes', theme, 'ghub_im']), (20,20))
