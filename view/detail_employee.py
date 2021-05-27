from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter
from .datepicker import CustomDateEntry
from pathlib import Path
import re

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
        lbl_title = Label(panel_right, text = 'Thông tin nhân viên', width = 55, bg = bg_color, fg = 'white', font=("time new roman", 20))
        lbl_title.grid(row = 0, columnspan = 5)

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

        self.txtUserId = StringVar()
        self.txtUserId.set(self.employee[4])
        self.userId_value_lbl = Entry(panel_right, width = 40, font=("bold", 10), textvariable = self.txtUserId)
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
        update_btn = Button(panel_right,
                            text='Cập nhật',
                            width = 15,
                            font=("time new roman", 18),
                            command = self.updateEmployee)
        update_btn.place(x = 300, y = 500)

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

    def updateEmployee(self):
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        
        name = self.name_entry.get()
        validated = self.validate(name,self.email_entry.get())

        if (validated == ['','']):
            df.loc[df['user_id'] == self.employee[4], 'birth'] = self.birth_entry.get_date()
            df.loc[df['user_id'] == self.employee[4], 'email'] = self.email_entry.get()

            
            if(not df.loc[(df['user_id'] == self.employee[4]) & (df['name'] != name), 'name'].empty):
                user_id = self.generateUserId(self.no_accent_vietnamese(name))
                avatar = df.loc[df['user_id'] == self.employee[4], 'avatar']

                df.iloc[(df['user_id'] == self.employee[4]) & (df['name'] != self.name_entry.get()), 'name'] = name
                df.iloc[(df['user_id'] == self.employee[4]) & (df['name'] != self.name_entry.get()), 'user_id'] = user_id

                df.iloc[(df['user_id'] == user_id) & (df['name'] != self.name_entry.get()), 'avatar'] = avatar.replace(self.employee[4], user_id)
                self.renameDir(self.employee[4], user_id)
                self.txtUserId.set(user_id)

            writer = pd.ExcelWriter(filename, engine='xlsxwriter', datetime_format='dd/mm/yyyy')
            df.to_excel(writer,index=False)
            writer.save()
            messagebox.showinfo(title="Thông báo chỉnh sửa", message="Thông tin nhân viên được chỉnh sửa thành công!")
        else:
            global errorFrame
            errorFrame = Tk()
            errorFrame.geometry('240x80')
            errorFrame.resizable(False, False)
            errorFrame.title('Kiểm tra dữ liệu nhập')

            if(validated[0]):
                Label(errorFrame, text = validated[0], fg = 'red').grid(row = 0, column = 0, padx = 50, pady = 5)
            elif(validated[1]):
                Label(errorFrame, text = validated[1], fg = 'red').grid(row = 1, column = 0, padx = 50, pady = 5)

            Button(errorFrame, text = 'Đã hiểu', command = self.deleteErrorFrame).grid(row = 3, column = 0, padx = 20, pady = 15)
            return

    def deleteErrorFrame(self):
        errorFrame.destroy()

    def renameDir(self,user_id, new_user_id):
        if(os.path.exists(os.path.abspath("data/face_train/" + user_id))):
            os.rename(os.path.abspath("data/face_train/" + user_id), os.path.abspath("data/face_train/" + new_user_id))
        else:
            print('khong ton tai thu muc!')
            return

    def no_accent_vietnamese(self,s):
        s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
        s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
        s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
        s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
        s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
        s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
        s = re.sub('[íìỉĩị]', 'i', s)
        s = re.sub('[ÍÌỈĨỊ]', 'I', s)
        s = re.sub('[úùủũụưứừửữự]', 'u', s)
        s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
        s = re.sub('[ýỳỷỹỵ]', 'y', s)
        s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
        s = re.sub('đ', 'd', s)
        s = re.sub('Đ', 'D', s)
        return s
    
    def generateUserId(self,name):
        arrName = name.split()
        user_id = arrName[len(arrName) - 1]

        for i in range(len(arrName)):
            if (i < len(arrName) - 1):
                user_id = user_id + arrName[i][0]
        root_name = user_id
        count = 1
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            if root_name in row[1]:
                user_id = root_name + str(count)
                count = count + 1

        return user_id

    def validate(self,name,email):
        name_message = ''
        email_message = ''
        input = {
            'name' : name,
            'email': email
        }
        if(self.checkEmpty(input)):
            return self.checkEmpty(input)
        
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(not re.search(regex,email)):   
            email_message = 'Định dạng email không hợp lệ'
        return [name_message,email_message]

    def checkEmpty(self,input):
        result = []
        if(len(input['name']) == 0):
            result.append('Tên không được để trống')

        if(len(input['email']) == 0):
            result.append('Email không được để trống')

        return result

    def goToBack(self):
        from .employee import EmployeeGUI
        self.root.destroy()
        frame = Tk()
        EmployeeGUI(frame)
            