import sys
import tkinter as tk

print("Python:", sys.version)
print("Interpreter:", sys.executable)

root = tk.Tk()
root.title("Tk rendering test")

print("Tk version:", root.tk.call("package", "provide", "Tk"))

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()
canvas.create_rectangle(50, 50, 350, 250, fill="red")
canvas.create_text(200, 150, text="Can you see this?", fill="white")

root.mainloop()