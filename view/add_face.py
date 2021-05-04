import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import *
import os
import time

class AddFaceGUI(object):
    def __init__(self, root, employee = None):
        width, height = 800, 600
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.root = root
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.lmain = Label(self.root)
        self.lmain.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot=Button(self.root, text="Chụp", width = 50, command = self.snapshot)
        self.btn_snapshot.pack(anchor = CENTER, expand=True)

        self.btn_back = Button(self.root, text='Trở về',width=20,bg='brown',fg='white',command=self.goToBack)
        self.btn_back.pack(anchor = CENTER, expand=True)

        self.employee = employee
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


    def snapshot(self):
        user_id = self.employee[4]
        folder = os.path.abspath('data/face_train/'+user_id)
        # Get a frame from the video source
        ret, frame = self.get_frame()
        name = "/frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
        if ret:
            cv2.imwrite(folder + name, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def get_frame(self):
        if self.cap.isOpened():
            isTrue, frame = self.cap.read()
            if isTrue:
                # Return a boolean success flag and the current frame converted to BGR
                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (isTrue, None)
        else:
            return (isTrue, None)

    def goToBack(self):
        from .employee import EmployeeGUI
        frame = Tk()
        self.root.destroy()
        employee = EmployeeGUI(frame)

