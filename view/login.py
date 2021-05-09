from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from .dashboard import Dashboard
import os
import hashlib, secrets
import pandas as pd

class LoginGUI(object):
    def __init__(self, root):
        self.root = root;
        self.root.title('Đăng nhập');
        self.root.geometry('490x380+0+0');
        self.root.resizable(False, False)

        #========= All images =========#
        imageBG = Image.open(os.path.abspath('view/images/bg-login.png'))
        resizeBG = imageBG.resize((490,50), Image.ANTIALIAS)
        imageIconUser = Image.open(os.path.abspath('view/images/icon-user.png'))
        resizeUser = imageIconUser.resize((25,25), Image.ANTIALIAS)
        imageIconPassword = Image.open(os.path.abspath('view/images/icon-password.png'))
        resizePassword = imageIconPassword.resize((25,25), Image.ANTIALIAS)
        imageIconLogo = Image.open(os.path.abspath('view/images/logo.png'))
        resizeLogo = imageIconLogo.resize((100,100), Image.ANTIALIAS)

        self.bg_login = ImageTk.PhotoImage(resizeBG)
        self.user_icon = ImageTk.PhotoImage(resizeUser)
        self.password_icon = ImageTk.PhotoImage(resizePassword)
        self.logo = ImageTk.PhotoImage(resizeLogo)

        self.txtuser = ''
        self.txtpass = ''

        title = Label(self.root, text = 'Đăng nhập', font = ('time new roman',25,'bold'), fg = 'white', image = self.bg_login, compound='center')
        title.pack()

        resizeFormBG = imageBG.resize((500,500), Image.ANTIALIAS)
        self.bg_form = ImageTk.PhotoImage(resizeFormBG)
        bg_lbl = Label(self.root, image = self.bg_form)
        bg_lbl.pack()

        Login_Frame = Frame(self.root, bg = 'white');
        Login_Frame.place(x = 10, y = 60);
        
        logolbl = Label(Login_Frame, image = self.logo).grid(row = 0, column = 0, pady = 10)

        lbluser = Label(Login_Frame,
                        text = 'Tài khoản',
                        image = self.user_icon,
                        compound = LEFT,
                        font = ('time new roman',20,'bold'),
                        bg = 'white').grid(row = 1, column = 0, padx = 20, pady = 10)
        self.user_entry = Entry(Login_Frame, bd=5, relief=GROOVE, font=('time new roman',15))
        self.user_entry.grid(row=1,column=1,padx=20)

        lblpass = Label(Login_Frame,
                        text = 'Mật khẩu',
                        image = self.password_icon,
                        compound = LEFT,
                        font = ('time new roman',20,'bold'),
                        bg = 'white').grid(row = 2, column = 0, padx = 20, pady = 10)
        self.pass_entry = Entry(Login_Frame, bd=5, relief=GROOVE, font=('time new roman',15), show = '*')
        self.pass_entry.grid(row=2,column=1,padx=20)

        btnSubmit = Button(Login_Frame,
                            bd=0,
                            relief="groove",
                            compound=CENTER,
                            bg='darkorange3',
                            fg='black',
                            text='Đăng nhập',
                            activeforeground="pink",
                            activebackground="white",
                            font=('time new roman',14,'bold'),
                            pady=10,
                            command=self.submit)
        btnSubmit.grid(row=3,column=1,pady=10)

        self.user_entry.bind('<Return>',self.submit)
        self.pass_entry.bind('<Return>',self.submit)

    def checkLogin(self, username, password):
        filename = 'data/Models/User.xlsx'
        df = pd.read_excel(filename)

        user_list = df['user'].tolist()
        password_list = df['password'].tolist()

        flagLogin = 0

        for u, p in zip(user_list, password_list):
            if username.strip() == u and hashlib.sha256(password.strip().encode('utf-8')).hexdigest() == p:
                flagLogin = 1

        return flagLogin

    def submit(self, event):
        flagLogin = self.checkLogin(username=self.user_entry.get(), password=self.pass_entry.get())

        if flagLogin == 1:
            self.root.destroy()
            window = Tk()
            dashboard = Dashboard(window)
        else:
            messagebox.showerror(title="Lỗi Đăng Nhập", message="Tài khoản hoặc mật khẩu của bạn bị sai. Vui lòng nhập lại!")
        
