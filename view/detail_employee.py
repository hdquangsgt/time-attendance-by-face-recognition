from tkinter import *

class DetailEmployeeGUI(object):
    def __init__(self, root, id):
        self.root = root
        self.root.title('Quản lý nhân viên')
        self.root.geometry('1350x700+0+0')

        #   Panel left
        panel_left = Frame(self.root, bd = 4, relief = RIDGE, bg = 'gray')
        panel_left.place(x = 20, y = 100, width = 400, height = 560)

        layout_title = Label(panel_left,
                            text='Chi tiết nhân viên',
                            bg = 'gray',
                            fg = 'black',
                            compound = CENTER,
                            font = ('time new roman', 24, 'bold'))
        layout_title.grid(row = 0, columnspan = 2, pady = 50)
        
        #   Load Avatar

        #   Button back

        #   Panel right
        
        #   Load Employee Detail Information

        #   Button update
