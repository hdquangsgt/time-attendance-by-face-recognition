from tkinter import *
import os
from .employee import EmployeeGUI
from .timekeeping import TimekeepingGUI

class Dashboard(object):
    def __init__(self, root):
        self.root = root
        self.root.geometry('550x445+0+0')

        Layout_Frame = Frame(self.root, bd=4, relief = RIDGE, bg = 'blue')
        Layout_Frame.place(x = 0, y = 5, width = 550, height = 570)

        layout_title = Label(Layout_Frame, 
                            text='Bảng điều khiển',
                            bg = 'yellow',
                            fg = 'blue',
                            font = ('time new roman', 18, 'bold'),
                            bd = 5,
                            relief = GROOVE)
        layout_title.place(x = 0, y = 0, relwidth = 1)

        def onClickEmployeeManage():
            employee = Tk()
            frm_employee = EmployeeGUI(employee)
            self.root.destroy()

        def onClickKeeptimeManage():
            timekeeping = Tk()
            frm_timekeeping = TimekeepingGUI(timekeeping)
            self.root.destroy()

        Dashboard_Frame = Frame(Layout_Frame, bd=4, relief = RIDGE, bg = 'blue')
        Dashboard_Frame.place(x = 0, y = 45, relwidth = 1)
        btn_employee = Button(Dashboard_Frame, 
                        text = 'Quản lý nhân viên',
                        width = 15,
                        height = 5,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'),
                        command = onClickEmployeeManage)
        btn_employee.grid(row = 0, column = 0, padx = 0, pady = 10)

        btn_keeptime = Button(Dashboard_Frame,
                        text = 'Quản lý chấm công',
                        width = 15,
                        height = 5,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'),
                        command = onClickKeeptimeManage)
        btn_keeptime.grid(row = 2, column = 0, padx = 0, pady = 15)

        

