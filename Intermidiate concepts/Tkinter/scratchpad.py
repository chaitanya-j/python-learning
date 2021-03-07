import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()

image = Image.open('alert.png')
# The (450, 350) is (height, width)
image = image.resize((450, 350), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = tk.Label(image = my_img)
my_img.pack()

root.mainloop()