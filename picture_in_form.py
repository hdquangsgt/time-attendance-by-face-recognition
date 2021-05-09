from tkinter import *
from PIL import ImageTk, Image

root = Tk()
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("2021-05-05_21-44-19.jpg"))  
canvas.create_image(50, 50, anchor=NW, image=img) 
root.mainloop() 


