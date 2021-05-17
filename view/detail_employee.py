from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter
from .datepicker import CustomDateEntry
from pathlib import Path

class DetailEmployeeGUI(object):
    def __init__(self, root, employee):
        self.root = root
        self.root.title('Quản lý nhân viên')
        self.root.geometry('1350x700+0+0')
        self.root.resizable(False, False)

        bg_color = '#990099'
        self.employee = employee

        #   Title monitor
        title = Label(self.root, text='Chi tiết nhân viên', font=('time new roman',24,'bold'),relief = RIDGE,bd=12,bg=bg_color,fg='white')
        title.pack(fill = X)

        #   Panel left
        self.panel_left = Frame(self.root, bd = 4, relief = RIDGE, bg = bg_color)
        self.panel_left.place(x = 20, y = 100, width = 400, height = 560)
        
        #   Title
        self.lbl_title_avt = Label(self.panel_left, text = 'Ảnh gốc', bg = bg_color, fg = 'white', font = ('time new roman', 20))
        self.lbl_title_avt.pack(fill = X)

        #   Load Avatar
        if(self.employee[5] != 'nan' and os.path.exists(self.employee[5])):
            imageBG = Image.open(os.path.abspath(self.employee[5]))
            resizeBG = imageBG.resize((180,180), Image.ANTIALIAS)
        else:
            imageBG = Image.open(os.path.abspath('view/images/avatar-default.png'))
            resizeBG = imageBG.resize((180,180), Image.ANTIALIAS)

        self.avatar = ImageTk.PhotoImage(resizeBG)

        self.lbl_avatar = Label(self.panel_left, image = self.avatar)
        self.lbl_avatar.place(x = 100, y = 50)
        self.lbl_avatar.bind('<Double-1>',self.uploadAvatar)

        #   Button back
        btn_back = Button(self.panel_left,
                        text = 'Trở về',
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        width = 27,
                        font = ('tim new roman', 18),
                        command = self.goToBack)
        btn_back.place(x = 2, y = 505)

        #   Panel right
        panel_right = Frame(self.root, bg = bg_color)
        panel_right.place(x = 450, y = 100, width = 840, height = 560)

        #   Load Employee Detail Information
        lbl_title = Label(panel_right, text = 'Thông tin nhân viên', font=("time new roman", 20))
        lbl_title.grid(row = 0, columnspan = 2)

        #   Field id
        id_lbl = Label(panel_right, text = 'Số thứ tự', width = 20, compound = LEFT, font=("bold", 10))
        id_lbl.grid(row = 1, column = 0, padx = 110, pady = 20)

        self.id_value_lbl = Entry(panel_right, width = 40, font=("bold", 10))
        self.id_value_lbl.insert(0,self.employee[0])
        self.id_value_lbl.config(state='disabled')
        self.id_value_lbl.grid(row = 1, column = 1, padx = 10, pady = 20, ipady = 1, ipadx = 20)

        #   Field user id
        userId_lbl = Label(panel_right, text = 'Mã nhân viên', width = 20, compound = LEFT, font=("bold", 10))
        userId_lbl.grid(row = 2, column = 0, padx = 110, pady = 20)

        self.userId_value_lbl = Entry(panel_right, width = 40, font=("bold", 10))
        self.userId_value_lbl.insert(0,self.employee[4])
        self.userId_value_lbl.config(state='disabled')
        self.userId_value_lbl.grid(row = 2, column = 1, padx = 5, pady = 20, ipady = 1, ipadx = 20)

        #   Field name
        name_lbl = Label(panel_right, text="Họ và tên", width = 20, compound = LEFT, font=("bold", 10))
        name_lbl.grid(row = 3, column = 0, padx = 110, pady = 20)

        self.name_entry = Entry(panel_right, width = 40, font=("bold", 10))
        self.name_entry.insert(0,self.employee[1])
        self.name_entry.grid(row = 3, column = 1, padx = 5, pady = 20, ipady = 1, ipadx = 20)

        #   Field birth
        birth_lbl = Label(panel_right, text="Ngày sinh", width = 20, compound = LEFT, font=("bold", 10))
        birth_lbl.grid(row = 4, column = 0, padx = 110, pady = 20)

        self.birth_entry = CustomDateEntry(panel_right, date_pattern='dd/MM/yyyy')
        self.birth_entry._set_text(self.employee[2])
        self.birth_entry.config(width = 44)
        self.birth_entry.grid(row = 4, column = 1, padx = 5, pady = 10, ipady = 2, ipadx = 20)
        
        #   Field email
        email_lbl = Label(panel_right, text="Email", width = 20, compound = LEFT, font=("bold", 10))
        email_lbl.grid(row = 5, column = 0, padx = 110, pady = 20)

        self.email_entry = Entry(panel_right, width = 40, font=("bold", 10))
        self.email_entry.insert(0,self.employee[3])
        self.email_entry.grid(row = 5, column = 1, padx = 5, pady = 20, ipady = 2, ipadx = 20)

        #   Button update
        update_btn = Button(panel_right, text='Cập nhật')
        update_btn.place(x = 400, y = 600)

    def uploadAvatar(self,event):
        pathFileFaces = os.path.abspath('data/face_train/' + str(self.employee[4]))
        Path(pathFileFaces).mkdir(parents=True, exist_ok=True)
        filename = filedialog.askopenfilename(initialdir=pathFileFaces,title="Select A File",filetypes=(('Image File','.jpg'),('All File',"*.*")))
        im = Image.open(filename)

        #   Update path avatar
        self.updatePathAvatar('data/face_train/' + filename.split('data/face_train/')[1])
        tkimage = ImageTk.PhotoImage(im)
        self.lbl_avatar = Label(self.panel_left, image = tkimage)
        self.lbl_avatar.place(x = 100, y = 50)
        self.lbl_avatar.bind('<Double-1>',self.uploadAvatar)
        self.root.mainloop()

    def updatePathAvatar(self,pathImage):
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        df.loc[df['user_id'] == self.employee[4], 'avatar'] = pathImage

        writer = pd.ExcelWriter(filename, engine='xlsxwriter', datetime_format='dd/mm/yyyy')
        df.to_excel(writer,index=False)
        writer.save()

    def goToBack(self):
        from .employee import EmployeeGUI
        self.root.destroy()
        frame = Tk()
        employee = EmployeeGUI(frame)
            