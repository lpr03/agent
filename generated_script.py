import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("Hello, World!")
    root.geometry("400x300")

    label1 = tk.Label(root, text="Hello, World!")
    label1.pack(padx=20, pady=20)

    button1 = tk.Button(root, text="Click Me", command=root.quit)
    button1.pack(padx=20, pady=20)

    button2 = tk.Button(root, text="Exit", command=root.destroy)
    button2.pack(padx=20, pady=20)

    root.mainloop()

create_gui()