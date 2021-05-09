from tkinter import *
from tkcalendar import *
import os
import pandas as pd
from .datepicker import CustomDateEntry

class TimekeepingGUI(object):
    def __init__(self, root):
        self.root = root
        self.root.title('Chấm công')
        self.root.geometry('1350x700+0+0')
        self.root.resizable(False, False)

        bg_color = '#990099'
        
        #   Title monitor
        title = Label(self.root, text='Chấm công', font=('time new roman',25,'bold'),relief = RIDGE,bd=12,bg=bg_color,fg='white')
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
        btn_logout.grid(row = 4, column = 0, padx = 5, pady = 150)
        
        #   Table data timekeeping
        Timekeeping_Frame = Frame(self.root, bd = 4, relief = RIDGE)
        Timekeeping_Frame.place(x = 550, y = 100, width = 840, height = 560)

        #   Select datetime picker
        lbl_timepicker = Label(Timekeeping_Frame, text = 'Ngày chấm công', font=('time new roman',14,'bold'))
        lbl_timepicker.grid(row = 0, column = 0, pady = 25)
        
        timepicker = CustomDateEntry(Timekeeping_Frame)
        timepicker._set_text(timepicker._date.strftime('%d/%m/%Y'))
        timepicker.grid(row = 0, column = 1, pady = 25)

        #   Button checkin employee
        btn_checkin = Button(Timekeeping_Frame,
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
        btn_checkout = Button(Timekeeping_Frame,
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

        #   Table data timekeeping
        table_frame = Frame(Timekeeping_Frame, bd = 4, relief = RIDGE, bg = 'crimson')
        table_frame.place(x = 0, y = 150, width = 830, height = 400)

        scroll_x = Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient = VERTICAL)

        table_timekeeping = ttk.Treeview(
            table_frame, 
            columns = ('date_logtime', 'user_id', 'checkin_time','checkout_time'),
            xscrollcommand = scroll_x.set,
            yscrollcommand = scroll_y.set
        )
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = table_timekeeping.xview)
        scroll_y.config(command = table_timekeeping.yview)

        table_timekeeping.heading('date_logtime', text = 'Ngày chấm công')
        table_timekeeping.heading('user_id', text = 'Mã nhân viên')
        table_timekeeping.heading('checkin_time', text = 'Giờ checkin')
        table_timekeeping.heading('checkout_time', text = 'Giờ checkout')

        table_timekeeping['show'] = 'headings'

        table_timekeeping.column('date_logtime', width = 100)
        table_timekeeping.column('user_id', width = 150)
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
            employee_tree.insert('',index = 'end',value = row)
            iid = iid + 1
