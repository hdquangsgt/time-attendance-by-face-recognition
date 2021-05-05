from tkinter import *
from tkcalendar import *
from datetime import date
from tkinter import messagebox

root = Tk()

ent = DateEntry(root, width = 15, background = 'blue', foregroundcolor = 'red', borderWidth = 3)
ent.pack(padx = 10, pady = 10)

mainloop()
