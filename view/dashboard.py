from tkinter import *
import os
from .employee import EmployeeGUI
from .timekeeping import TimekeepingGUI

class Dashboard(object):
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')

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
            employee = Tk()
            frm_employee = EmployeeGUI(employee)
            self.root.destroy()

        def onClickKeeptimeManage():
            timekeeping = Tk()
            frm_timekeeping = TimekeepingGUI(timekeeping)
            self.root.destroy()

        btn_employee = Button(Layout_Frame, 
                        text = 'Quản lý nhân viên',
                        width = 25,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'),
                        command = onClickEmployeeManage)
        btn_employee.grid(row = 20, column = 0, padx = 0, pady = 10)

        btn_keeptime = Button(Layout_Frame,
                        text = 'Quản lý chấm công',
                        width = 25,
                        bg = 'gray',
                        fg = 'white',
                        compound = CENTER,
                        font = ('time new roman', 18, 'bold'),
                        command = onClickKeeptimeManage)
        btn_keeptime.grid(row = 21, column = 0, padx = 0, pady = 5)

        

