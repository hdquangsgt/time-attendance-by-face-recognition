from tkinter import *
from PIL import Image, ImageTk
import time
import cv2
import os

class AddFaceGUI(object):
    def __init__(self, root, video_source = 0, employee = None):
        self.appName = 'Thêm khuôn mặt nhân viên'
        self.root = root
        self.root.title(self.appName)
        self.root.resizable(0,0)
        self.root['bg'] = 'black'
        self.video_source = video_source

        self.vid = MyVideoCapture(self.video_source)
        self.label = Label(self.root, text = self.appName, font = 15, bg = 'blue', fg = 'white').pack(side = TOP, fill = BOTH)

        self.canvas = Canvas(self.root, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot=Button(self.root, text="Chụp", width = 50, command = self.snapshot)
        self.btn_snapshot.pack(anchor = CENTER, expand=True)

        self.btn_back = Button(self.root, text='Trở về',width=20,bg='brown',fg='white',command=self.goToBack)
        self.btn_back.pack(anchor = CENTER, expand=True)

        self.root.mainloop()

    def snapshot(self):
        folder = os.path.abspath('data/images/')
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

        self.root.after(self.delay, self.update)

    def goToBack(self):
        from .employee import EmployeeGUI
        frame = Tk()
        self.root.destroy()
        employee = EmployeeGUI(frame)

class MyVideoCapture:
    def __init__(self, video_source = 0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    def get_frame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                # Return a boolean success flag and the current frame converted to BGR
                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (isTrue, None)
            cv2.imshow(frame)
        else:
            return (isTrue, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
    
