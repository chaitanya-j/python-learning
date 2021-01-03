import tkinter as tk
from PIL import ImageTk, Image 

root = tk.Tk()
canvas = tk.Canvas(width=500,height=500)

canvas.pack()

photo = ImageTk.PhotoImage(Image.open('disconnecting-plug.jpg'))

#photo = tk.PhotoImage(file="//home//chaitanya//Work//learning//python-learning//Battery tracking//disconnecting-plug.jpg")
canvas.create_image(250,-90, image=photo, anchor=tk.N)

root.mainloop()