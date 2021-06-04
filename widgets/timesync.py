import tkinter as tk

from help_funcs.helper import open_image
from clock import Clock


class Timesync:
    def __init__(self, window, clock_ref, settings):
        self.settings = settings
        self.servers = self.settings.get_settings(['servers'])
        self.selected = self.settings.get_settings(['selected'])

        self.clock = clock_ref
        self.clock += [Clock(self.servers['standard']['delay'], self.selected, self.servers[self.selected]['delay'], 10)]
        self.clock[0].start()

        self.window = window
        self.is_running = False
        self.update_thread = None

        # Displayed image corresponding to the server.
        # NOTE: file needs to be saved because tkinter needs a reference.
        # Otherwise the file/image is drawn on the canvas and when the function
        # ends, tkinter loses its reference as file is deleted by pythons
        # garbage collector
        self.image_canvas = None
        self.image = None
        self.file = None

        # Displayed image + text of last server synchronisation
        self.sync_symbol = None
        self.current_symbol = None
        self.sync_text = None

    # Update the canvas by drawing the image contained in self.file
    def update_image(self):
        try:
            if self.servers[self.selected]['image'] == '':
                self.file = open_image("images/default.jpg", (self.image_canvas.winfo_height(), self.image_canvas.winfo_width()))
            else:
                self.file = open_image(self.servers[self.selected]['image'], (self.image_canvas.winfo_height(), self.image_canvas.winfo_width()))
        except Exception:
            self.file = open_image(self, "images/default.jpg", (self.image_canvas.winfo_height(), self.image_canvas.winfo_width()))
        self.image_canvas.itemconfig(self.image, image=self.file)

    def select_server(self, sv_server):
        # Stop the old clock and create+start a new clock with the desired server
        if self.clock[0]:
            self.clock[0].stop()
        self.clock[0] = Clock(self.servers['standard']['delay'], sv_server.get(), self.servers[sv_server.get()]['delay'], 10)
        self.clock[0].start()
        self.selected = sv_server.get()

        # Update the settings with the selected server
        self.settings.update_settings(['selected'], self.selected)

        self.update_image()

    # Returns A string with the amount of seconds or minutes between now and
    # the last synchronisation with the server.
    def time_sync(self, time):
        diff = time - self.clock[0].last_synced

        if diff < 60:
            return str(round(diff)) + " s"
        if diff >= 60:
            return str(math.floor(diff / 60)) + " m"

    def update_sync_symbol(self, time):
        if self.clock[0].server_sync:
            self.sync_symbol.itemconfig(self.current_symbol, fill="green")
            self.sync_symbol.itemconfig(self.sync_text, text=self.time_sync(time))
        else:
            self.sync_symbol.itemconfig(self.current_symbol, fill="red")
            self.sync_symbol.itemconfig(self.sync_text, text="")


    def setup_window(self):
        # Frame of our sync interface
        server_frame = tk.Frame(self.window, width=100 + 40, height=100)

        # Stringvar with selected server
        sv_server = tk.StringVar(name="SERVER")
        sv_server.set(self.selected)


        # Canvas with server image
        self.image_canvas = tk.Canvas(server_frame, width=60, height=60, background="grey")
        self.image_canvas.place(x=80, y=0)
        self.file = open_image("images/default.jpg", (self.image_canvas.winfo_height(), self.image_canvas.winfo_width()))
        self.image = self.image_canvas.create_image(0, 0, image=self.file, anchor='nw')
        # TODO: fix this actually placing an image(there is currently a bug
        #       where no image will show until a new server is synced)


        # Canvas with the synchronisation symbol + text
        self.sync_symbol = tk.Canvas(self.window, width=30, height=20)
        self.sync_symbol.place(in_=server_frame, relx=1.0, rely=0.7, x=5)
        self.current_symbol = self.sync_symbol.create_oval(2, 2, 11, 11, fill="grey")
        self.sync_text = self.sync_symbol.create_text((2, 10), font="calibri 8", width=50, text="test", anchor='nw')

         # width: 140, height: 30. (0, 80)
        selector = tk.OptionMenu(server_frame, sv_server, *self.servers)
        selector.place(x=0, y=70, width=100, height=30)
        submit_btn = tk.Button(server_frame, text='Sync', command=lambda: self.select_server(sv_server))
        submit_btn.place(x=(100 + 5), y=70, width=35, height=28)

        return server_frame

    # Execute update and do the same update a second later
    def run(self):
        time = self.clock[0].time_ms()
        # List of Updates
        self.update_sync_symbol(time)

        if self.is_running:
            time = self.clock[0].time_ms()
            self.update_thread = self.window.after(1000 - (round(time * 1000) % 1000), self.run)

    # Start running
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.run()

    # Stop running
    def stop(self):
        if self.is_running:
            self.window.after_cancel(self.update_thread)
            self.clock[0].stop()
            self.update_thread = None
            self.is_running = False
