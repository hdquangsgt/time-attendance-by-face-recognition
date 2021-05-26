from tkinter import *
from tkinter import ttk
import pandas as pd
import os

question_frame = Tk()
question_frame.geometry('380x90')
question_frame.resizable(False, False)
question_frame.title('Cập nhật logtime')

filename = os.path.abspath('data/Models/Employee.xlsx')
df = pd.read_excel(filename)
arr = df['user_id'].tolist()

def pick_color(e):
    print(my_combo.get())

my_combo = ttk.Combobox(question_frame, value = arr)
my_combo.current(arr.index('QuangTrung'))
my_combo.pack(pady = 20)
my_combo.bind('<<ComboboxSelected>>', pick_color)

question_frame.mainloop()