from tkinter import *
from view.datepicker import CustomDateEntry

def callback(asdv):
    print(asdv.get())


root = Tk()
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = CustomDateEntry(root, date_pattern='dd/MM/yyyy', textvariable = sv)
e._set_text(e._date.strftime('%d/%m/%Y'))
e.config(width = 30)
e.pack()

root.mainloop()