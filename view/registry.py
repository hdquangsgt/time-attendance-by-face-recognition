from tkinter import *
from PIL import ImageTk, Image
import os
import pandas as pd
from openpyxl import load_workbook
# import xlwt
# import xlrd

class RegistryForm(object):
    def __init__(self, root):
        self.root = root
        self.root.title('Quản lý nhân viên')
        self.root.geometry('700x450+0+0')
        self.name_entry = ''
        self.birth_entry = ''
        self.email_entry = ''

        #========= All images =========#
        # imageBG = os.path.abspath('view/images/background-login.png')
        # self.bg_icon = PhotoImage(file = imageBG)
        # bg_lbl = Label(self.root, image = self.bg_icon).place(x = 250, y = 0, relwidth = 1, relheight = 1)

        # icon_registry = os.path.abspath('view/images/registry.png')
        # self.icon_registry = PhotoImage(file=icon_registry)
        # registry_lbl = Label(self.root, image = self.icon_registry).place(x = 80, y = 80)

        registry_title = Label(self.root, 
                            text='Đăng ký nhân viên',
                            bg = 'blue',
                            fg = 'white',
                            compound = CENTER, 
                            bd = 10, 
                            relief = GROOVE,
                            font = ('time new roman', 24, 'bold'))
        registry_title.place(x = 0, y = 0, relwidth = 1)

        registry_frm = Frame(self.root, bg = 'white')
        registry_frm.place(x = 100, y = 100, width = 500, height = 300)

        #   Field name
        name_lbl = Label(registry_frm, text="Họ và tên", width = 20, compound = LEFT, font=("bold", 10))
        name_lbl.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.name_entry = Entry(registry_frm, width = 40)
        self.name_entry.grid(row = 1, column = 2, padx = 10, pady = 10)

        #   Field birth
        birth_lbl = Label(registry_frm, text="Ngày sinh", width = 20, compound = LEFT, font=("bold", 10))
        birth_lbl.grid(row = 2, column = 1, padx = 10, pady = 10)

        self.birth_entry = Entry(registry_frm, width = 40)
        self.birth_entry.grid(row = 2, column = 2, padx = 10, pady = 10)

        #   Field email
        email_lbl = Label(registry_frm, text="Email", width = 20, compound = LEFT, font=("bold", 10))
        email_lbl.grid(row = 3, column = 1, padx = 10, pady = 10)

        self.email_entry = Entry(registry_frm, width = 40)
        self.email_entry.grid(row = 3, column = 2, padx = 10, pady = 10)

        Button(registry_frm, text='Trở về',width=20,bg='brown',fg='white',command=self.goToBack).place(x=50,y=250)
        Button(registry_frm, text='Đăng ký',width=20,bg='brown',fg='white',command=self.submit).place(x=300,y=250)
        
    def addDataExcel(self, data, filename):
        df = pd.DataFrame(data)
        print(df)
        writer = pd.ExcelWriter(filename, engine='openpyxl')
        writer.book = load_workbook(filename)
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        reader = pd.read_excel(filename)
        df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)
        writer.save()

    def submit(self):
        from .employee import EmployeeGUI
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        id = len(df.index) + 1
        name = self.name_entry.get()
        user_id = self.generateUserId(name)
        data = {
            'id': [id],
            'user_id': [user_id],
            'name': [name],
            'birth': [self.birth_entry.get()],
            'email': [self.email_entry.get()]
        }
        # self.addDataExcel(data, filename)
        self.createFolder(user_id)
        
        #   Exit
        employeeFrame = Tk()
        EmployeeGUI(employeeFrame)
        self.root.destroy()

    def createFolder(self,userId):
        parent_dir = os.path.abspath('data/face_train')
        path = os.path.join(parent_dir, userId)
        os.makedirs(path) 


    def generateUserId(self,name):
        arrName = name.split()
        user_id = arrName[len(arrName) - 1]

        for i in range(len(arrName)):
            if (i < len(arrName) - 1):
                user_id = user_id + arrName[i][0]

        count = 1
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            if user_id in row[1]:
                user_id = user_id + str(count)
                count = count + 1

        return user_id

    def goToBack(self):
        from .employee import EmployeeGUI
        frame = Tk()
        employee = EmployeeGUI(frame)
        self.root.destroy()
