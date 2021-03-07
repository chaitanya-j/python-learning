import tkinter as tk

    

root = tk.Tk()

ent = tk.Entry(root)
def button_command():
    text = ent.get()
    print(text)
    return None

label = tk.Label(text="Username")
btn_ok = tk.Button(text="OK", command=button_command)

label.pack()
ent.pack()
btn_ok.pack()

btn_ok.bind("<Button-1>",lambda e: root.destroy())

root.mainloop()