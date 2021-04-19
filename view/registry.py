from tkinter import *
from PIL import ImageTk, Image
import os

class RegistryForm(object):
    def __init__(self, root):
        self.root = root
        self.root.title('Quản lý nhân viên')
        self.root.geometry('1350x700+0+0')

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
        registry_frm.place(x = 480, y = 100, width = 700, height = 500)

        name_lbl = Label(registry_frm, text="Họ và tên", width=20, compound = LEFT, font=("bold", 10))
        name_lbl.grid(row = 1, column = 1, padx = 10, pady = 10)

        name_entry = Entry(registry_frm)
        name_entry.grid(row = 1, column = 2, padx = 10, pady = 10)

        label_2 = Label(registry_frm, text="Email", width=20, compound = LEFT, font=("bold", 10))
        label_2.grid(row = 2, column = 1, padx = 10, pady = 10)

        entry_2 = Entry(registry_frm)
        entry_2.grid(row = 2, column = 2, padx = 10, pady = 10)

        Button(registry_frm, text='Trở về',width=20,bg='brown',fg='white',command=self.goToBack).place(x=150,y=380)
        Button(registry_frm, text='Đăng ký',width=20,bg='brown',fg='white').place(x=400,y=380)
        
    def goToBack(self):
        from .employee import EmployeeGUI
        frame = Tk()
        employee = EmployeeGUI(frame)
        self.root.destroy()
