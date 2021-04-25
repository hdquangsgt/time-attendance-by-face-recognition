from tkinter import *
from tkinter import ttk, filedialog
from .registry import RegistryForm
from .timekeeping import TimekeepingGUI
from .detail_employee import DetailEmployeeGUI
import os
import pandas as pd
from datetime import datetime
import cv2

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
            timekeeping = Tk()
            frm_timekeeping = TimekeepingGUI(timekeeping)
            self.root.destroy()

        btn_employee = Button(Layout_Frame,
                        text = 'Quản lý nhân viên',
                        width = 25,
                        bg = 'red',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'))
        btn_employee.grid(row = 20, column = 0, padx = 0, pady = 10)

        btn_keeptime = Button(Layout_Frame,
                        text = 'Quản lý chấm công',
                        width = 25,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        command = onClickKeeptimeManage,
                        font = ('time new roman', 18, 'bold'))
        btn_keeptime.grid(row = 21, column = 0, padx = 0, pady = 5)

        #   Title monitor
        title = Label(self.root, text='Quản lý nhân viên', font=('time new roman',20,'bold'),bg='blue',fg='white')
        title.pack(side=TOP, fill=X)

        #   Employee Screen
        Employee_Frame = Frame(self.root, bd=4,bg = 'crimson', relief = RIDGE)
        Employee_Frame.place(x = 500, y = 100, width = 840, height = 550)

        #   Search
        lbl_search = Label(Employee_Frame, text = 'Tìm kiếm nhân viên', bg = 'crimson', fg= 'white', font = ('time new roman', 14, 'bold'))
        lbl_search.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')

        txt_search = Entry(Employee_Frame, width = 20, font = ('time new roman', 12), bd = 5, relief = GROOVE)
        txt_search.grid(row = 0, column = 1, padx = 20, pady = 10)

        btn_search = Button(Employee_Frame, text = 'Tìm kiếm', width = 10, pady = 5)
        btn_search.grid(row = 0, column = 2, padx = 20, pady = 10)

        #   Button registry employee
        btn_registry = Button(Employee_Frame,
            text = 'Thêm nhân viên',
            width = 250,
            bg = 'blue',
            compound = CENTER,
            font = ('time new roman', 14, 'bold'),
            command = self.registry)
        btn_registry.place(x = 600, y = 100, width = 200, height = 30)

        #   Table data employee
        table_frame = Frame(Employee_Frame, bd = 4, relief = RIDGE, bg = 'crimson')
        table_frame.place(x = -2, y = 150, width = 830, height = 400)

        scroll_x = Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient = VERTICAL)

        table_employee = ttk.Treeview(
            table_frame, 
            columns = ('id', 'name', 'birth', 'email', 'late_date', 'off_date','action'),
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
        table_employee.heading('late_date', text = 'Số ngày đi trễ')
        table_employee.heading('off_date', text = 'Số ngày nghỉ')

        table_employee['show'] = 'headings'

        table_employee.column('id', width = 100)
        table_employee.column('name', width = 150)
        table_employee.column('birth', width = 100)
        table_employee.column('email', width = 150)
        table_employee.column('late_date', width = 100)
        table_employee.column('off_date', width = 100)

        self.loadData(table_employee)
        table_employee.pack(fill = BOTH, expand = 1)

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

        #   Action employee
        def subMenu(e):
            iid = table_employee.identify_row(e.y)
            if iid:
                data = table_employee.selection_set(iid)
            else:
                pass

            selecteEmployee = table_employee.focus()
            value = table_employee.item(selecteEmployee, 'values')
            employeeSelected = value
            action.tk_popup(e.x_root,e.y_root)
        
        #   Bindings
        table_employee.bind('<Double-1>', selectEmployeeDetail)
    
    def loadData(self,employee_tree):
        iid = 0
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        #   Clear old record
        # clearTree(employee_tree)

        #   Put data in treeview
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            # print(row[1])
            row[2] = row[2].strftime('%m/%d/%Y')
            employee_tree.insert('',index = 'end', iid = row[0],value=row)
            iid = iid + 1

    def clearTree(my_tree):
        my_tree.delete(*my_tree.get_children())

    def registry(self):
        registry = Tk()
        registryForm = RegistryForm(registry)
        self.root.destroy()

    def showFace(self):
        pass

    def deleteEmployee(self):
        pass

class Employee(object):
    def __init__(self, id, name, birth, email, late_date, off_date):
        self.id = id
        self.name = name
        self.birth = birth
        self.email = email
        self.late_date = late_date
        self.off_date = off_date
        
        