from tkinter import *

tk = Tk()
tk.title("Hello World!")
frame = LabelFrame(tk, text="hehe")
frame.pack()
b = Button(frame, text="hi")
b.pack()

tk.mainloop()
