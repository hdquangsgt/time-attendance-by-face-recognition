from tkinter import *
from tkinter import ttk, filedialog
from numpy import NaN
from tkcalendar import *
from .detail_timekeeping import DetailTimekeepingGUI
import os
import pandas as pd
from .datepicker import CustomDateEntry
from datetime import date
import numpy as np

class TimekeepingGUI(object):
    def __init__(self, root):
        self.root = root
        self.root.title('Chấm công')
        self.root.geometry('1350x700+0+0')
        self.root.resizable(False, False)

        bg_color = '#990099'
        
        #   Title monitor
        title = Label(self.root, text='Danh sách chấm công', font=('time new roman',25,'bold'),relief = RIDGE,bd=12,bg=bg_color,fg='white')
        title.pack(fill = X)

        # Layouts menu
        Layout_Frame = Frame(self.root, bd = 14, relief = RIDGE, bg = bg_color)
        Layout_Frame.place(x = 20, y = 100, width = 400, height = 560)

        layout_title = Label(Layout_Frame, 
                            text='Bảng điều khiển',
                            bg = bg_color,
                            fg = 'white',
                            compound = CENTER,
                            font = ('time new roman', 24, 'bold'))
        layout_title.grid(row = 0, columnspan = 2, pady = 50)
        
        def onClickEmployeeManage():
            from .employee import EmployeeGUI
            self.root.destroy()
            employee = Tk()
            frm_employee = EmployeeGUI(employee)

        def logout():
            from .login import LoginGUI
            self.root.destroy()
            logout = Tk()
            frm_login = LoginGUI(logout)

        btn_employee = Button(Layout_Frame,
                        text = 'Quản lý nhân viên',
                        width = 23,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        relief = RIDGE,
                        bd = 5,
                        command = onClickEmployeeManage,
                        font = ('time new roman', 18, 'bold'))
        btn_employee.grid(row = 1, column = 0, padx = 5, pady = 10)

        btn_keeptime = Button(Layout_Frame,
                        text = 'Chấm công',
                        width = 23,
                        bg = 'red',
                        fg = 'white',
                        relief = RIDGE,
                        bd = 5,
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'))
        btn_keeptime.grid(row = 2, column = 0, padx = 5, pady = 5)

        btn_logout = Button(Layout_Frame,
                        text = 'Đăng xuất',
                        width = 23,
                        bg = 'gray',
                        fg = 'white',
                        relief = RIDGE,
                        bd = 5,
                        compound = CENTER,
                        command = logout,
                        font = ('time new roman', 18, 'bold'))
        btn_logout.grid(row = 3, column = 0, padx = 5, pady = 180)
        
        #   Panel right Screen
        Panel_right = Frame(self.root, bg = bg_color, bd = 10, relief = RIDGE)
        Panel_right.place(x = 500, y = 100, width = 840, height = 560)

        Timekeeping_Frame = Frame(Panel_right, bg = bg_color)
        Timekeeping_Frame.place(x = 0, y = 80, width = 820, height = 450)

        #   Table data timekeeping
        table_frame = Frame(Timekeeping_Frame, bd = 5, relief = RIDGE, bg = bg_color)
        table_frame.place(x = 5, y = 100, width = 810, height = 350)

        scroll_x = Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient = VERTICAL)

        self.table_timekeeping = ttk.Treeview(
            table_frame, 
            columns = ('id','date_logtime', 'user_id', 'checkin_time','checkout_time'),
            xscrollcommand = scroll_x.set,
            yscrollcommand = scroll_y.set
        )
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.table_timekeeping.xview)
        scroll_y.config(command = self.table_timekeeping.yview)

        self.table_timekeeping.heading('id', text = 'Số thứ tự')
        self.table_timekeeping.heading('date_logtime', text = 'Ngày chấm công')
        self.table_timekeeping.heading('user_id', text = 'Mã nhân viên')
        self.table_timekeeping.heading('checkin_time', text = 'Giờ checkin')
        self.table_timekeeping.heading('checkout_time', text = 'Giờ checkout')

        self.table_timekeeping['show'] = 'headings'

        self.table_timekeeping.column('id', width = 50, anchor=CENTER)
        self.table_timekeeping.column('date_logtime', width = 100, anchor=CENTER)
        self.table_timekeeping.column('user_id', width = 150, anchor=CENTER)
        self.table_timekeeping.column('checkin_time', width = 150, anchor=CENTER)
        self.table_timekeeping.column('checkout_time', width = 100, anchor=CENTER)

        self.loadData(self.table_timekeeping)
        self.table_timekeeping.pack(fill = BOTH, expand = 1)

        #   Select datetime picker
        lbl_timepicker = Label(Panel_right, text = 'Ngày chấm công', bg = bg_color, fg= 'white', font=('time new roman',14,'bold'))
        lbl_timepicker.grid(row = 0, column = 0, padx = 10, pady = 25)

        def callback(date):
            self.loadData(self.table_timekeeping, date.get())

        self.selectedDate = StringVar()
        self.selectedDate.trace("w", lambda name, index, mode, selectedDate=self.selectedDate: callback(self.selectedDate))

        self.timepicker = CustomDateEntry(Panel_right, date_pattern='dd/MM/yyyy', textvariable = self.selectedDate)
        self.timepicker._set_text(self.timepicker._date.strftime('%d/%m/%Y'))
        self.timepicker.config(width = 30)
        self.timepicker.grid(row = 0, column = 1,padx = 20, pady = 25, ipady = 4, ipadx = 20)

        #   Button checkin employee
        btn_checkin = Button(Panel_right,
            bd = 0,
            relief = "groove",
            compound = CENTER,
            bg = "yellow",
            fg = "black",
            text = 'Check-in',
            activeforeground = "pink",
            activebackground = "white",
            font = ('time new roman', 13, 'bold'),
            pady = 10)
        btn_checkin.grid(row = 1, column = 0, padx = 25, pady = 15)

        #   Button checkout employee
        btn_checkout = Button(Panel_right,
            bd = 0,
            relief = "groove",
            compound = CENTER,
            bg = "yellow",
            fg = "black",
            text = 'Check-out',
            activeforeground = "pink",
            activebackground = "white",
            font = ('time new roman', 13, 'bold'),
            pady = 10)
        btn_checkout.grid(row = 1, column = 1, padx = 25, pady = 15)

        #   Get data record
        def getData():
            selected = self.table_timekeeping.focus()
            return self.table_timekeeping.item(selected, 'values')

        #   Create binding click function
        def selectTimekeepingDetail(e):
            timekeeping = getData()
            if timekeeping:
                self.root.destroy()
                frame = Tk()
                frame = DetailTimekeepingGUI(frame,timekeeping)
            else:
                pass

        self.timekeepingData = {}
        def selectTimekeepingData(e):
            self.timekeepingData = getData()

        #   Bindings
        self.table_timekeeping.bind('<Double-1>', selectTimekeepingDetail)
        self.table_timekeeping.bind('<ButtonRelease-1>', selectTimekeepingData)

    def loadData(self, timekeeping_tree, dateTimekeeping = None):
        self.clearTree(timekeeping_tree)
        iid = 0
        filename = os.path.abspath('data/Models/Timekeeping.xlsx')
        filename_employee = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        df1 = pd.read_excel(filename_employee)

        if(dateTimekeeping):
            df = df[df['date_logtime'] == dateTimekeeping]
        else:
            today = date.today()
            df = df[df['date_logtime'] == today.strftime("%d/%m/%Y")]

        #   Put data in treeview
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            row[0] = row[0].strftime('%d/%m/%Y')
            row[3] = str(row[3])
            if(row[3] != 'nan'):
                row[3] = ' '
            employee = df1[df1.user_id == row[1]].iloc[0]
            data = [iid + 1, row[0] , row[1], row[2], row[3], row[4], row[5]]

            if(str(employee.avatar) != 'nan'):
                timekeeping_tree.insert('',index = 'end', iid = iid, value = data)
                iid = iid + 1

    def clearTree(self,my_tree):
        my_tree.delete(*my_tree.get_children())
    
    def selectDate(self,e):
        print('hello')
        self.loadData(self.table_timekeeping,self.timepicker.get_date())

    def checkin():
        pass

    def checkout():
        pass
