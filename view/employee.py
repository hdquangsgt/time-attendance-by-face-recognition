from tkinter import *
from .registry import RegistryForm
import os

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
                        font = ('time new roman', 18, 'bold'))
        btn_keeptime.grid(row = 21, column = 0, padx = 0, pady = 5)

        #   Title monitor
        title = Label(self.root, text='Quản lý nhân viên', font=('time new roman',20,'bold'),bg='blue',fg='white')
        title.pack(side=TOP, fill=X)

        #   Button registry employee
        btn_registry = Button(self.root,
            text = 'Thêm nhân viên',
            width = 250,
            bg = 'blue',
            compound = CENTER,
            font = ('time new roman', 14, 'bold'),
            command = self.registry)
        btn_registry.place(x = 1050, y = 150, width = 250, height = 40)
        
        #   Table data employee
        Employee_Frame = Frame(self.root, bd=4, relief = RIDGE)
        Employee_Frame.place(x = 550, y = 253, width = 750, height = 400)

        header = ['STT', 'Họ và tên', 'Số ngày đi trễ', 'Số ngày nghỉ','Thao tác']
        self.table(5,len(header),Employee_Frame,header)

    def table(self,rows,columns,frame,header):
        for row in range(rows):
            for column in range(columns):
                if (row == 0):
                    lbl = Label(frame, text = header[column], bg = 'white', fg = 'black', padx = 3, pady = 3)
                    lbl.config(font = ('time new roman',14))
                    lbl.grid(row = row, column = column, sticky = 'nsew', padx = 1, pady = 1)
                    frame.grid_columnconfigure(column, weight = 1)
                else:
                    lbl = Label(frame, text = 'row: ' + str(row) + ' column: ' + str(column), bg = 'black', fg = 'white', padx = 3, pady = 3)
                    lbl.grid(row = row, column = column, sticky = 'nsew', padx = 1, pady = 1)
                    frame.grid_columnconfigure(column, weight = 1)

    def destroy(self):
            print('hello boy')
            self.root.destroy()

    def registry(self):
        registry = Tk()
        registryForm = RegistryForm(registry)
        self.root.destroy()


        



        
        