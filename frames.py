from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)

frame.pack()

frame.config(height=200, width= 400)
frame.config(relief= RIDGE)

ttk.Button(frame, text='click me').grid()
frame.config(padding = (30, 50))
ttk.LabelFrame(root, height = 100, width=200, text='MyFrame').pack()

if __name__ == '__main__':
    mainloop()