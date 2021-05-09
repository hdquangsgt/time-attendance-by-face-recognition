from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog


def UploadAction(event=None):
    filename = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
    pic = Toplevel()

    im = Image.open(filename)
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(pic,image = tkimage)
    myvar.image = tkimage
    myvar.pack()

    pic.mainloop()

root = Tk()
button = Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()

