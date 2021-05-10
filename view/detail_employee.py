from tkinter import *
from PIL import ImageTk, Image
import os
import pandas as pd
from openpyxl import load_workbook
from .datepicker import CustomDateEntry

class DetailEmployeeGUI(object):
    def __init__(self, root, employee):
        self.root = root
        self.root.title('Quản lý nhân viên')
        self.root.geometry('1350x700+0+0')
        self.root.resizable(False, False)

        bg_color = '#990099'
        print(employee)

        #   Title monitor
        title = Label(self.root, text='Chi tiết nhân viên', font=('time new roman',24,'bold'),relief = RIDGE,bd=12,bg=bg_color,fg='white')
        title.pack(fill = X)

        #   Panel left
        panel_left = Frame(self.root, bd = 4, relief = RIDGE, bg = bg_color)
        panel_left.place(x = 20, y = 100, width = 400, height = 560)
        
        #   Load Avatar
        imageBG = Image.open(os.path.abspath('view/images/avatar-default.png'))
        resizeBG = imageBG.resize((200,200), Image.ANTIALIAS)
        self.avatar = ImageTk.PhotoImage(resizeBG)

        lbl_avatar = Label(panel_left, image = self.avatar)
        lbl_avatar.place(x = 120, y = 0)

        #   Button back
        btn_back = Button(panel_left,
                        text = 'Trở về',
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        width = 50,
                        font = ('tim new roman', 20),
                        command = self.goToBack)
        btn_back.place(x = 0, y = 300)

        #   Panel right
        panel_right = Frame(self.root, bg = bg_color)
        panel_right.place(x = 450, y = 100, width = 840, height = 560)

        #   Load Employee Detail Information

        #   Field id
        id_lbl = Label(panel_right, text = 'Số thứ tự', width = 20, compound = LEFT, font=("bold", 10))
        id_lbl.grid(row = 0, column = 0, padx = 110, pady = 10)

        self.id_value_lbl = Entry(panel_right, width = 40, font=("bold", 10))
        self.id_value_lbl.insert(0,employee[0])
        self.id_value_lbl.config(state='disabled')
        self.id_value_lbl.grid(row = 0, column = 1, padx = 10, pady = 10, ipady = 1, ipadx = 20)

        #   Field user id
        userId_lbl = Label(panel_right, text = 'Mã nhân viên', width = 20, compound = LEFT, font=("bold", 10))
        userId_lbl.grid(row = 1, column = 0, padx = 100, pady = 10)

        self.userId_value_lbl = Entry(panel_right, width = 40, font=("bold", 10))
        self.userId_value_lbl.insert(0,employee[4])
        self.userId_value_lbl.config(state='disabled')
        self.userId_value_lbl.grid(row = 1, column = 1, padx = 5, pady = 10, ipady = 1, ipadx = 20)

        #   Field name
        name_lbl = Label(panel_right, text="Họ và tên", width = 20, compound = LEFT, font=("bold", 10))
        name_lbl.grid(row = 2, column = 0, padx = 100, pady = 10)

        self.name_entry = Entry(panel_right, width = 40, font=("bold", 10))
        self.name_entry.insert(0,employee[1])
        self.name_entry.grid(row = 2, column = 1, padx = 5, pady = 20, ipady = 1, ipadx = 20)

        #   Field birth
        birth_lbl = Label(panel_right, text="Ngày sinh", width = 20, compound = LEFT, font=("bold", 10))
        birth_lbl.grid(row = 3, column = 0, padx = 110, pady = 10)

        self.birth_entry = CustomDateEntry(panel_right)
        self.birth_entry._set_text(employee[2])
        self.birth_entry.config(width = 44)
        self.birth_entry.grid(row = 3, column = 1, padx = 5, pady = 10, ipady = 1, ipadx = 20)
        
        #   Field email
        email_lbl = Label(panel_right, text="Email", width = 20, compound = LEFT, font=("bold", 10))
        email_lbl.grid(row = 4, column = 0, padx = 110, pady = 10)

        self.email_entry = Entry(panel_right, width = 40, font=("bold", 10))
        self.email_entry.insert(0,employee[3])
        self.email_entry.grid(row = 4, column = 1, padx = 5, pady = 10, ipady = 1, ipadx = 20)

        #   Button update

    def goToBack(self):
            from .employee import EmployeeGUI
            frame = Tk()
            employee = EmployeeGUI(frame)
            self.root.destroy()