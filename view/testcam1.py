import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import *

class TestCam(object):
    def __init__(self, root):
        width, height = 800, 600
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.root = root
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.lmain = Label(self.root)
        self.lmain.pack()

        self.show_frame()
        self.root.mainloop()

    def show_frame(self):
        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.show_frame)

