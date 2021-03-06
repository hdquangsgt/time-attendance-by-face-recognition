from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
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
        
        #   Title
        self.lbl_title_avt = Label(self.panel_left, text = 'Ảnh gốc', bg = bg_color, fg = 'white', font = ('time new roman', 20))
        self.lbl_title_avt.pack(fill = X)

        #   Load Avatar
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        fileImage = df[df['user_id'] == self.timekeeping[2]].iloc[0]['avatar']
        if(fileImage != 'nan' and os.path.exists(fileImage)):
            im = Image.open(os.path.abspath(fileImage))
            resizeBG = im.resize((180,180), Image.ANTIALIAS)
        else:
            imageBG = Image.open(os.path.abspath('view/images/avatar-default.png'))
            resizeBG = imageBG.resize((180,180), Image.ANTIALIAS)

        self.avatar = ImageTk.PhotoImage(resizeBG)
        self.lbl_avatar = Label(self.panel_left, image = self.avatar)
        self.lbl_avatar.place(x = 100, y = 50)

        #   Button update
        btn_update = Button(self.panel_left,
                        text = 'Cập nhật',
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        width = 27,
                        font = ('tim new roman', 18),
                        command = self.showDialogQuestion)
        btn_update.place(x = 2, y = 450)

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
        self.panel_right = Frame(self.root, bg = bg_color)
        self.panel_right.place(x = 450, y = 100, width = 840, height = 560)

        #   Load Timekeepipng Detail Information

        #   Field date logtime
        id_lbl = Label(self.panel_right, text = 'Ngày chấm công', width = 20, compound = LEFT, font=("bold", 10))
        id_lbl.grid(row = 0, column = 0, padx = 110, pady = 20)

        self.id_value_lbl = Entry(self.panel_right, width = 40, font=("bold", 10))
        self.id_value_lbl.insert(0,self.timekeeping[1])
        self.id_value_lbl.config(state='disabled')
        self.id_value_lbl.grid(row = 0, column = 1, padx = 10, pady = 20, ipady = 1, ipadx = 20)

        #   Field user id
        userId_lbl = Label(self.panel_right, text = 'Mã nhân viên', width = 20, compound = LEFT, font=("bold", 10))
        userId_lbl.grid(row = 1, column = 0, padx = 110, pady = 20)

        listUserId = df['user_id'].tolist()
        self.userId_value_lbl = ttk.Combobox(self.panel_right, value = listUserId, width = 38, font=("bold", 10))
        self.userId_value_lbl.current(listUserId.index(self.timekeeping[2]))
        self.userId_value_lbl.grid(row = 1, column = 1, padx = 5, pady = 20, ipady = 1, ipadx = 20)

        #   Field checkin time
        checkin_time_lbl = Label(self.panel_right, text="Giờ checkin", width = 20, compound = LEFT, font=("bold", 10))
        checkin_time_lbl.grid(row = 2, column = 0, padx = 110, pady = 20)

        self.checkin_entry = Entry(self.panel_right, width = 40, font=("bold", 10))
        self.checkin_entry.insert(0,self.timekeeping[3])
        self.checkin_entry.grid(row = 2, column = 1, padx = 5, pady = 20, ipady = 1, ipadx = 20)

        #   Field checkout time
        checkout_time_lbl = Label(self.panel_right, text="Giờ checkout", width = 20, compound = LEFT, font=("bold", 10))
        checkout_time_lbl.grid(row = 3, column = 0, padx = 110, pady = 20)

        self.checkout_entry = Entry(self.panel_right, width = 40, font=("bold", 10))
        self.checkout_entry.insert(0,self.timekeeping[4])
        self.checkout_entry.grid(row = 3, column = 1, padx = 5, pady = 10, ipady = 2, ipadx = 20)
        
        #   Field face checkin
        face_checkin_lbl = Label(self.panel_right, text="Ảnh checkin", width = 20, compound = LEFT, font=("bold", 10))
        face_checkin_lbl.grid(row = 4, column = 0, padx = 110, pady = 20)

        if(os.path.exists(self.timekeeping[5]) & os.path.isfile(self.timekeeping[5])):
            imCheckin = Image.open(os.path.abspath(self.timekeeping[5]))
            resizeImCheckin = imCheckin.resize((180,180), Image.ANTIALIAS)
            imgFaceCheckin = ImageTk.PhotoImage(resizeImCheckin)
        else:
            imCheckin = Image.open(os.path.abspath('view/images/image-default-checkout.png'))
            resizeImCheckout = imCheckin.resize((180,180), Image.ANTIALIAS)
        self.faceCheckin = Label(self.panel_right, image = imgFaceCheckin)
        self.faceCheckin.grid(row = 5, column = 0, padx = 10, pady = 20)
        
        #   Field face checkout
        face_checkout_lbl = Label(self.panel_right, text="Ảnh checkout", width = 20, compound = LEFT, font=("bold", 10))
        face_checkout_lbl.grid(row = 4, column = 1, padx = 110, pady = 20)

        if(os.path.exists(self.timekeeping[6]) & os.path.isfile(self.timekeeping[6])):
            imCheckout = Image.open(os.path.abspath(self.timekeeping[6]))
            resizeImCheckout = imCheckout.resize((180,180), Image.ANTIALIAS)
        else:
            imCheckout = Image.open(os.path.abspath('view/images/image-default-checkout.png'))
            resizeImCheckout = imCheckout.resize((180,180), Image.ANTIALIAS)
        imgFaceCheckout = ImageTk.PhotoImage(resizeImCheckout)
        self.faceCheckout = Label(self.panel_right, image = imgFaceCheckout)
        self.faceCheckout.grid(row = 5, column = 1, padx = 10, pady = 20)

        self.root.mainloop()

    def showDialogQuestion(self):
        global question_frame
        question_frame = Tk()
        question_frame.geometry('380x90')
        question_frame.resizable(False, False)
        question_frame.title('Cập nhật logtime')

        lbl_question = Label(question_frame, text = 'Bạn có chắc chắn muốn chỉnh sửa logtime này!', font = ('time new roman', 13))
        lbl_question.place(x = 15, y = 15)

        btn_ok = Button(question_frame, width = 10, text = 'OK', bg = 'yellow', fg = 'black', font = ('time new roman',11), command = self.updateLogtime)
        btn_ok.place(x = 55, y = 50)

        btn_cancel = Button(question_frame, width = 10, text = 'Hủy', bg = 'red', fg = 'black', font = ('time new roman',11), command = self.destroyDialog)
        btn_cancel.place(x = 230, y = 50)

    def updateLogtime(self):
        filename = os.path.abspath('data/Models/Timekeeping.xlsx')
        df = pd.read_excel(filename)
        
        timeCheckin = self.checkin_entry.get()
        timeCheckout = self.checkout_entry.get()
        if(timeCheckin == ''):
            messagebox.showerror(title="Lỗi chỉnh sửa", message="Thông tin không được để rỗng!")
            return
        if(not (self.isValidateTime(timeCheckin) or self.isValidateTime(timeCheckout))):
            messagebox.showerror(title="Lỗi chỉnh sửa", message="Định dạng giờ checkin hoặc checkout không đúng!")
            return

        df.loc[(df['date_logtime'] == self.timekeeping[1]) & (df['user_id'] == self.timekeeping[2]), 'checkin_time'] = timeCheckin
        df.loc[(df['date_logtime'] == self.timekeeping[1]) & (df['user_id'] == self.timekeeping[2]), 'checkout_time'] = timeCheckout

        if(self.timekeeping[2] != self.userId_value_lbl.get()):
            if(self.userId_value_lbl.get() not in df['user_id'].tolist()):
                df.loc[(df['date_logtime'] == self.timekeeping[1]) & (df['user_id'] == self.timekeeping[2]), 'user_id'] = self.userId_value_lbl.get()
            else:
                messagebox.showerror(title="Lỗi chỉnh sửa", message="User ID này đã tồn tại trong danh sách chấm công!")
        writer = pd.ExcelWriter(filename, engine='xlsxwriter', datetime_format='dd/mm/yyyy')
        df.to_excel(writer,index=False)
        writer.save()
        question_frame.destroy()

    def isValidateTime(self,time):
        import re
        regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
        p = re.compile(regex)
        if (time == ""):
            return False
        m = re.search(p, time)
        if(m is None):
            return False
        else:
            return True

    def destroyDialog(self):
        question_frame.destroy()
    
    def goToBack(self):
        from .timekeeping import TimekeepingGUI
        self.root.destroy()
        frame = Tk()
        TimekeepingGUI(frame)
        
