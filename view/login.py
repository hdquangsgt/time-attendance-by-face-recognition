from tkinter import *
from PIL import ImageTk, Image
from .master import Layouts
import os

class LoginGUI(object):
    def __init__(self, root):
        self.root = root;
        self.root.title('Login');
        self.root.geometry('920x650+0+0');

        #========= All images =========#
        imageBG = os.path.abspath('view/images/background-login.png')
        imageIconUser = Image.open(os.path.abspath('view/images/icon-user.png'))
        resizeUser = imageIconUser.resize((50,50), Image.ANTIALIAS)
        imageIconPassword = Image.open(os.path.abspath('view/images/icon-password.png'))
        resizePassword = imageIconPassword.resize((50,50), Image.ANTIALIAS)
        imageIconLogo = Image.open(os.path.abspath('view/images/logo.png'))
        resizeLogo = imageIconLogo.resize((200,200), Image.ANTIALIAS)

        self.bg_icon = PhotoImage(file=imageBG)
        self.user_icon = ImageTk.PhotoImage(resizeUser)
        self.password_icon = ImageTk.PhotoImage(resizePassword)
        self.logo = ImageTk.PhotoImage(resizeLogo)

        bg_lbl = Label(self.root, image = self.bg_icon).pack()

        title = Label(self.root, text = 'Đăng nhập', font=('time new roman',40,'bold'), bg = 'blue', fg = 'white', bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        Login_Frame = Frame(self.root, bg = 'white');
        Login_Frame.place(x = 225, y = 150);
        
        logolbl = Label(Login_Frame, image = self.logo).grid(row = 0, column = 0, pady = 10)

        lbluser = Label(Login_Frame,
                        text = 'Họ và tên',
                        image = self.user_icon,
                        compound = LEFT,
                        font = ('time new roman',20,'bold'),
                        bg = 'white').grid(row = 1, column = 0, padx = 20, pady = 10)
        txtuser = Entry(Login_Frame,bd=5,relief=GROOVE,font=('',15)).grid(row=1,column=1,padx=20)
        lblpass = Label(Login_Frame,
                        text = 'Mật khẩu',
                        image = self.password_icon,
                        compound = LEFT,
                        font = ('time new roman',20,'bold'),
                        bg = 'white').grid(row = 2, column = 0, padx = 20, pady = 10)
        txtpass = Entry(Login_Frame,bd=5,relief=GROOVE,font=('',15)).grid(row=2,column=1,padx=20)

        btnSubmit = Button(Login_Frame,
                            text='Đăng nhập',
                            width=15,
                            font=('time new roman',14,'bold'),
                            bg='green',
                            fg='black',
                            command=self.submit).grid(row=3,column=1,pady=10)

    def checkLogin(usename, password):
        if(usename == 'username' and password == 'password'):
            return;

    def submit(self):
        window = Tk()
        layouts = Layouts(window)
        self.root.destroy()
