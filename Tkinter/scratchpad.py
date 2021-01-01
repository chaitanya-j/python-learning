import tkinter as tk

perc = 20
sts = "Charging"

root = tk.Tk()

def handle_click(event):
    global root
    print("The button was clicked!")
    root.destroy()

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)

button.pack()
root.mainloop()