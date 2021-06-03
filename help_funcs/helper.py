from PIL import ImageTk, Image

def open_image(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))
