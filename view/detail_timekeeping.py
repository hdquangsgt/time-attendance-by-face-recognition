from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter
from .datepicker import CustomDateEntry
from pathlib import Path

class DetailTimekeepingGUI(object):
    def __init__(self, root, timekeeping):
        self.root = root
        self.root.title('Chấm công')
        self.root.geometry('1350x700+0+0')
        self.root.resizable(False, False)

        bg_color = '#990099'
        self.timekeeping = timekeeping

        #   Title monitor
        title = Label(self.root, text='Chi tiết chấm công', font=('time new roman',24,'bold'),relief = RIDGE,bd=12,bg=bg_color,fg='white')
        title.pack(fill = X)

        #   Panel left
        self.panel_left = Frame(self.root, bd = 4, relief = RIDGE, bg = bg_color)
        self.panel_left.place(x = 20, y = 100, width = 400, height = 560)
        
        #   Load Avatar
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        fileImage = df[df['user_id'] == self.timekeeping[1]].iloc[0]['avatar']

        im = Image.open(os.path.abspath(fileImage))
        resizeBG = im.resize((180,180), Image.ANTIALIAS)

        self.avatar = ImageTk.PhotoImage(resizeBG)
        self.lbl_avatar = Label(self.panel_left, image = self.avatar)
        self.lbl_avatar.place(x = 120, y = 0)

        #   Button back
        btn_back = Button(self.panel_left,
                        text = 'Trở về',
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        width = 25,
                        font = ('tim new roman', 20),
                        command = self.goToBack)
        btn_back.place(x = 0, y = 300)

        #   Panel right
        panel_right = Frame(self.root, bg = bg_color)
        panel_right.place(x = 450, y = 100, width = 840, height = 560)

        #   Load Timekeepipng Detail Information

        #   Field date logtime
        id_lbl = Label(panel_right, text = 'Ngày chấm công', width = 20, compound = LEFT, font=("bold", 10))
        id_lbl.grid(row = 0, column = 0, padx = 110, pady = 20)

        self.id_value_lbl = Entry(panel_right, width = 40, font=("bold", 10))
        self.id_value_lbl.insert(0,self.timekeeping[0])
        self.id_value_lbl.config(state='disabled')
        self.id_value_lbl.grid(row = 0, column = 1, padx = 10, pady = 20, ipady = 1, ipadx = 20)

        #   Field user id
        userId_lbl = Label(panel_right, text = 'Mã nhân viên', width = 20, compound = LEFT, font=("bold", 10))
        userId_lbl.grid(row = 1, column = 0, padx = 110, pady = 20)

        self.userId_value_lbl = Entry(panel_right, width = 40, font=("bold", 10))
        self.userId_value_lbl.insert(0,self.timekeeping[1])
        self.userId_value_lbl.config(state='disabled')
        self.userId_value_lbl.grid(row = 1, column = 1, padx = 5, pady = 20, ipady = 1, ipadx = 20)

        #   Field checkin time
        checkin_time_lbl = Label(panel_right, text="Giờ checkin", width = 20, compound = LEFT, font=("bold", 10))
        checkin_time_lbl.grid(row = 2, column = 0, padx = 110, pady = 20)

        self.checkin_entry = Entry(panel_right, width = 40, font=("bold", 10))
        self.checkin_entry.insert(0,self.timekeeping[2])
        self.checkin_entry.grid(row = 2, column = 1, padx = 5, pady = 20, ipady = 1, ipadx = 20)

        #   Field checkout time
        checkout_time_lbl = Label(panel_right, text="Giờ checkout", width = 20, compound = LEFT, font=("bold", 10))
        checkout_time_lbl.grid(row = 3, column = 0, padx = 110, pady = 20)

        self.checkout_entry = Entry(panel_right, width = 40, font=("bold", 10))
        self.checkout_entry.insert(0,self.timekeeping[3])
        self.checkout_entry.grid(row = 3, column = 1, padx = 5, pady = 10, ipady = 2, ipadx = 20)
        
        # #   Field face checkin
        # email_lbl = Label(panel_right, text="Ảnh checkin", width = 20, compound = LEFT, font=("bold", 10))
        # email_lbl.grid(row = 4, column = 0, padx = 110, pady = 20)

        
        # self.email_entry.grid(row = 4, column = 1, padx = 5, pady = 20, ipady = 2, ipadx = 20)

        # #   Field face checkout
        # email_lbl = Label(panel_right, text="Ảnh checkout", width = 20, compound = LEFT, font=("bold", 10))
        # email_lbl.grid(row = 4, column = 0, padx = 110, pady = 20)

        # self.email_entry = Entry(panel_right, width = 40, font=("bold", 10))
        # self.email_entry.insert(0,self.timekeeping[5])
        # self.email_entry.grid(row = 4, column = 2, padx = 5, pady = 20, ipady = 2, ipadx = 20)

        #   Button update
        update_btn = Button(panel_right)

    def goToBack(self):
        from .timekeeping import TimekeepingGUI
        self.root.destroy()
        frame = Tk()
        timekeeping = TimekeepingGUI(frame)
