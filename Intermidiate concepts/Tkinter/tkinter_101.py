import tkinter as tk


window = tk.Tk()
#greeting = tk.Label(text="Hello, welcomt to ShockWave Developers ltd.")


button = tk.Button(
    text="NEXT"
    )

label = tk.Label(text="Name")
entry = tk.Entry()

#label.pack()
#entry.pack()
button.pack()
window.mainloop()
def handle_click(event):
    print("The button was clicked!")

button.bind("<Button-1>", handle_click)

