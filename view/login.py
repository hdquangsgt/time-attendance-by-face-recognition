from tkinter import *
from PIL import ImageTk, Image
from .dashboard import Dashboard
import os

class LoginGUI(object):
    def __init__(self, root):
        self.root = root;
        self.root.title('Đăng nhập');
        self.root.geometry('490x380+0+0');

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
                            command=self.submit).grid(row=3,column=1,pady=10)
    def checkLogin(usename, password):
        if(usename == 'username' and password == 'password'):
            return;

    def submit(self):
        self.root.destroy()
        window = Tk()
        dashboard = Dashboard(window)
