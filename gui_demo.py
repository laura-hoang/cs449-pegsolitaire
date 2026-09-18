import tkinter as tk


root = tk.Tk()
root.geometry("250x200")

tk.Label(root, text="Hello World").pack()

tk.Checkbutton(root, text="Check me").pack()

tk.Radiobutton(root, text="Option 1", value=1).pack()

tk.Radiobutton(root, text="Option 2", value=2).pack()

canvas = tk.Canvas(root, width=200, height=50)
canvas.pack()

canvas.create_line(10, 10, 190, 10)
canvas.create_line(10, 30, 190, 30)

root.mainloop()


