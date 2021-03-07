import tkinter as tk
from PIL import ImageTk, Image

path = '/home/chaitanya/Work/learning/python-learning/battery-tracking/disconnecting-plug.jpg'

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()