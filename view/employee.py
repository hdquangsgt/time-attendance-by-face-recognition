from tkinter import *
from tkinter import ttk, filedialog
from .registry import RegistryForm
from .timekeeping import TimekeepingGUI
from .detail_employee import DetailEmployeeGUI
from .add_face import AddFaceGUI
import os
from os import path
import pandas as pd
from datetime import datetime
from pathlib import Path

class EmployeeGUI(object):
    def __init__(self, root):
        self.root = root
        self.root.title('Quản lý nhân viên')
        self.root.geometry('1350x700+0+0')

        # Layouts menu
        Layout_Frame = Frame(self.root, bd=4, relief = RIDGE, bg = 'blue')
        Layout_Frame.place(x = 20, y = 100, width = 400, height = 560)

        layout_title = Label(Layout_Frame, 
                            text='Bảng điều khiển',
                            bg = 'blue',
                            fg = 'white',
                            compound = CENTER,
                            font = ('time new roman', 24, 'bold'))
        layout_title.grid(row = 0, columnspan = 2, pady = 50)

        def onClickKeeptimeManage():
            self.root.destroy()
            timekeeping = Tk()
            frm_timekeeping = TimekeepingGUI(timekeeping)

        def logout():
            from .login import LoginGUI
            self.root.destroy()
            logout = Tk()
            frm_login = LoginGUI(logout)

        btn_employee = Button(Layout_Frame,
                        text = 'Quản lý nhân viên',
                        width = 25,
                        bg = 'red',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'))
        btn_employee.grid(row = 1, column = 0, padx = 0, pady = 10)

        btn_keeptime = Button(Layout_Frame,
                        text = 'Chấm công',
                        width = 25,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        command = onClickKeeptimeManage,
                        font = ('time new roman', 18, 'bold'))
        btn_keeptime.grid(row = 2, column = 0, padx = 0, pady = 5)

        btn_logout = Button(Layout_Frame,
                        text = 'Đăng xuất',
                        width = 25,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        command = logout,
                        font = ('time new roman', 18, 'bold'))
        btn_logout.grid(row = 4, column = 0, padx = 0, pady = 150)

        #   Title monitor
        title = Label(self.root, text='Quản lý nhân viên', font=('time new roman',20,'bold'),bg='blue',fg='white')
        title.pack(side=TOP, fill=X)

        #   Panel right Screen
        Panel_right = Frame(self.root, bd = 4,bg = 'crimson', relief = RIDGE)
        Panel_right.place(x = 500, y = 100, width = 840, height = 560)

        #   Employee Screen
        Employee_Frame = Frame(Panel_right,bd = 4,bg = 'crimson')
        Employee_Frame.place(x = 0, y = 80, width = 839, height = 450)

        #   Table data employee
        table_frame = Frame(Employee_Frame, bd = 4, relief = RIDGE, bg = 'crimson')
        table_frame.place(x = 0, y = 100, width = 830, height = 350)

        scroll_x = Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient = VERTICAL)

        table_employee = ttk.Treeview(
            table_frame, 
            columns = ('id', 'name', 'birth', 'email'),
            xscrollcommand = scroll_x.set,
            yscrollcommand = scroll_y.set
        )
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = table_employee.xview)
        scroll_y.config(command = table_employee.yview)

        table_employee.heading('id', text = 'STT')
        table_employee.heading('name', text = 'Họ và tên')
        table_employee.heading('birth', text = 'Ngày sinh')
        table_employee.heading('email', text = 'Email')

        table_employee['show'] = 'headings'

        table_employee.column('id', width = 100)
        table_employee.column('name', width = 150)
        table_employee.column('birth', width = 100)
        table_employee.column('email', width = 150)

        self.loadData(table_employee)
        table_employee.pack(fill = BOTH, expand = 1)

        #   Search Screen
        Search_Frame = Frame(Panel_right, bg = 'crimson')
        Search_Frame.place(x = 0, y = 20, width = 840, height = 80)

        #   Search
        lbl_search = Label(Search_Frame, text = 'Tìm kiếm nhân viên', bg = 'crimson', fg= 'white', font = ('time new roman', 14, 'bold'))
        lbl_search.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')

        def callback(event):
            self.loadData(table_employee,event.get())

        keyword = StringVar()
        keyword.trace("w", lambda name, index, mode, keyword = keyword: callback(keyword))
        txt_search = Entry(Search_Frame, width = 20, font = ('time new roman', 12), bd = 5, relief = GROOVE, textvariable = keyword)
        txt_search.grid(row = 0, column = 1, padx = 20, pady = 10)

        btn_search = Button(Search_Frame, text = 'Tìm kiếm', width = 10, font = ('time new roman', 12), pady = 5)
        btn_search.grid(row = 0, column = 2, padx = 20, pady = 10)

        #   Button registry employee
        btn_registry = Button(Employee_Frame,
            text = 'Thêm nhân viên',
            bg = 'blue',
            font = ('time new roman', 13, 'bold'),
            command = self.registry)
        btn_registry.grid(row = 0, column = 0, padx = 25, pady = 25)

        #   Button add face employee
        btn_addFace = Button(Employee_Frame,
            text = 'Thêm khuôn mặt',
            bg = 'green',
            font = ('time new roman', 13, 'bold'),
            command = self.addFace)
        btn_addFace.grid(row = 0, column = 1, padx = 20, pady = 25)

        #   Button show data face employee
        btn_showFace = Button(Employee_Frame,
            text = 'Xem dữ liệu khuôn mặt',
            bg = 'yellow',
            font = ('time new roman', 13, 'bold'),
            command = self.showFace)
        btn_showFace.grid(row = 0, column = 2, padx = 20)

        #   Button show data face employee
        btn_trainFace = Button(Employee_Frame,
            text = 'Training khuôn mặt',
            bg = 'yellow',
            font = ('time new roman', 13, 'bold'))
        btn_trainFace.grid(row = 0, column = 3, padx = 20, pady = 25)

        #   Get data record
        def getData():
            selected = table_employee.focus()
            return table_employee.item(selected, 'values')

        #   Create binding click function
        def selectEmployeeDetail(e):
            employee = getData()
            if employee:
                frame = Tk()
                frame = DetailEmployeeGUI(frame,employee)
                self.root.destroy()
            else:
                pass

        self.employeeData = {}
        def selectEmployeeData(e):
            self.employeeData = getData()
        
        #   Bindings
        table_employee.bind('<Double-1>', selectEmployeeDetail)
        table_employee.bind('<ButtonRelease-1>',selectEmployeeData)
        
    def loadData(self,employee_tree, keyword = None):
        self.clearTree(employee_tree)
        iid = 0
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        
        if (keyword):
            df = df[df['name'].str.lower().str.contains(keyword)]

        #   Put data in treeview
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            row[3] = row[3].strftime('%m/%d/%Y')
            data = [row[0],row[2],row[3],row[4],row[1]]
            employee_tree.insert('',index = 'end', iid = row[0],value=data)
            iid = iid + 1

    def clearTree(self,my_tree):
        my_tree.delete(*my_tree.get_children())

    def registry(self):
        self.root.destroy()
        registry = Tk()
        registryForm = RegistryForm(registry)

    def addFace(self):
        import cv2
        if(self.employeeData):
            Path(os.path.abspath('data/face_train/' + self.employeeData[4])).mkdir(parents=True, exist_ok=True)
            addFaceFrame = AddFaceGUI(employee = self.employeeData)
        return

    def showFace(self):
        if(self.employeeData):
            Path(os.path.abspath('data/face_train/' + self.employeeData[4])).mkdir(parents=True, exist_ok=True)
            os.startfile(os.path.abspath('data/face_train/' + self.employeeData[4]))

    def deleteEmployee(self):
        pass

    def searchEmployee(self):
        keyword = StringVar()
        
        
        