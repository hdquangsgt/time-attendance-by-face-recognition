from tkinter import *
import os
import pandas as pd

class TimekeepingGUI(object):
    def __init__(self, root):
        self.root = root
        self.root.title('Quản lý chấm công')
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

        def onClickEmployeeManage():
            from .employee import EmployeeGUI
            employee = Tk()
            frm_employee = EmployeeGUI(employee)
            self.root.destroy()

        def logout():
            from .login import LoginGUI
            logout = Tk()
            frm_login = LoginGUI(logout)
            self.root.destroy()

        btn_employee = Button(Layout_Frame,
                        text = 'Quản lý nhân viên',
                        width = 25,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'),
                        command = onClickEmployeeManage)
        btn_employee.grid(row = 1, column = 0, padx = 0, pady = 10)

        btn_keeptime = Button(Layout_Frame,
                        text = 'Chấm công',
                        width = 25,
                        bg = 'red',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'))
        btn_keeptime.grid(row = 2, column = 0, padx = 0, pady = 5)

        btn_logout = Button(Layout_Frame,
                        text = 'Đăng xuất',
                        width = 25,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'),
                        command = logout)
        btn_logout.grid(row = 4, column = 0, padx = 0, pady = 150)

        #   Title monitor
        title = Label(self.root, text='Chấm công', font=('time new roman',20,'bold'),bg='blue',fg='white')
        title.pack(side=TOP, fill=X)
        
        #   Table data timekeeping
        Timekeeping_Frame = Frame(self.root, bd = 4, relief = RIDGE)
        Timekeeping_Frame.place(x = 550, y = 100, width = 840, height = 560)

        #   Button registry employee
        btn_registry = Button(Timekeeping_Frame,
            text = 'Checkin',
            bg = 'blue',
            font = ('time new roman', 13, 'bold'))
        btn_registry.grid(row = 1, column = 0, pady = 25)

        #   Button add face employee
        btn_addFace = Button(Timekeeping_Frame,
            text = 'Check out',
            bg = 'green',
            font = ('time new roman', 13, 'bold'))
        btn_addFace.grid(row = 1, column = 1, pady = 25)

        #   Table data timekeeping
        table_frame = Frame(Timekeeping_Frame, bd = 4, relief = RIDGE, bg = 'crimson')
        table_frame.place(x = 0, y = 150, width = 830, height = 400)

        scroll_x = Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient = VERTICAL)

        table_timekeeping = ttk.Treeview(
            table_frame, 
            columns = ('id', 'name', 'user_id', 'date_logtime', 'checkin_time','checkout_time'),
            xscrollcommand = scroll_x.set,
            yscrollcommand = scroll_y.set
        )
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = table_timekeeping.xview)
        scroll_y.config(command = table_timekeeping.yview)

        table_timekeeping.heading('id', text = 'STT')
        table_timekeeping.heading('user_id', text = 'Mã nhân viên')
        table_timekeeping.heading('name', text = 'Họ và tên')
        table_timekeeping.heading('date_logtime', text = 'Ngày chấm công')
        table_timekeeping.heading('checkin_time', text = 'Giờ checkin')
        table_timekeeping.heading('checkout_time', text = 'Giờ checkout')

        table_timekeeping['show'] = 'headings'

        table_timekeeping.column('id', width = 100)
        table_timekeeping.column('user_id', width = 150)
        table_timekeeping.column('name', width = 150)
        table_timekeeping.column('date_logtime', width = 100)
        table_timekeeping.column('checkin_time', width = 150)
        table_timekeeping.column('checkout_time', width = 100)

        self.loadData(table_timekeeping)
        table_timekeeping.pack(fill = BOTH, expand = 1)

    def loadData(self,employee_tree):
        iid = 0
        filename = os.path.abspath('data/Models/Timekeeping.xlsx')
        df = pd.read_excel(filename)

        #   Put data in treeview
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            employee_tree.insert('',index = 'end', iid = row[0],value = row)
            iid = iid + 1
