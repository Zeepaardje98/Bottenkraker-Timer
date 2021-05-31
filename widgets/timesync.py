import tkinter as tk
from PIL import ImageTk, Image

from clock import Clock


class Timesync:
    def __init__(self, window, settings):
        self.window = window

        self.servers = settings.get_settings(['servers'])
        self.selected = settings.get_settings(['selected'])  # get this from settings later
        self.clock = Clock(self.servers['standard']['delay'], self.selected, self.servers[self.selected]['delay'], 30)

        self.canvas = None
        self.file = None  # Current image
        self.sync_symbol = tk.Canvas(self.window, width=30, height=20)
        self.current_symbol = self.sync_symbol.create_oval(2, 2, 11, 11, fill="red")
        self.sync_text = self.sync_symbol.create_text((2, 10), font="calibri 8", width=50, text="test", anchor='nw')

    # Resize an image given by Path, to the canvas. Set self.file as this image
    def set_file(self, path):
        img = Image.open(path)
        img = img.resize((self.canvas.winfo_height(), self.canvas.winfo_width()), Image.ANTIALIAS)
        self.file = ImageTk.PhotoImage(img)

    def update_image(self):
        try:
            if self.servers[self.selected]['image'] == '':
                self.set_file("images/default.jpg")
            else:
                self.set_file(self.servers[self.selected]['image'])
        except Exception:
            self.set_file("images/default.jpg")
        self.canvas.create_image(0, 0, image=self.file, anchor='nw')

    def select_server(self, sv_server):
        self.clock.stop()
        self.selected = sv_server.get()
        self.clock = Clock(self.servers['standard']['delay'], sv_server.get(), self.servers[sv_server.get()]['delay'], 30)

        self.update_image()

    def setup_window(self):
        # Frame of our sync interface
        server_frame = tk.Frame(self.window, width=100 + 40, height=30 + 80)

        # Stringvar with selected server
        sv_server = tk.StringVar(name="SERVER")
        sv_server.set(self.selected)

        self.canvas = tk.Canvas(server_frame, width=60, height=60, background="grey")
        self.canvas.place(x=80, y=0)

        # width: 140, height: 30. (0, 80)
        selector = tk.OptionMenu(server_frame, sv_server, *self.servers)
        selector.place(x=0, y=65, width=100, height=30)
        submit_btn = tk.Button(server_frame, text='Sync', command=lambda: self.select_server(sv_server))
        submit_btn.place(x=(100 + 5), y=65, width=35, height=28)

        self.sync_symbol.place(in_=server_frame, relx=1.0, rely=0.7, x=5)

        return server_frame
