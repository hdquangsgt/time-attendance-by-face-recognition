import cv2
import os
from datetime import datetime
import mediapipe as mp
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter

class AddFaceGUI(object):
    def __init__(self, employee = None, tmp = None):
        self.employee = employee
        self.tmp = tmp
        
        countImage = 0
        if (self.employee):
            user_id = self.employee[4]
            folder = os.path.abspath('data/face_train/' + user_id)
            countImage = len([name for name in os.listdir(os.path.abspath('data/face_train/'+self.employee[4]))])

        if(self.tmp):
            folder = os.path.abspath('data/tmp/' + self.tmp)

        video_capture = cv2.VideoCapture(0)
        mpFaceDetect = mp.solutions.face_detection
        mpDraw = mp.solutions.drawing_utils

        faceDetection = mpFaceDetect.FaceDetection(0.7)
        count = 0

        while True:
            _, img = video_capture.read()

            # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = faceDetection.process(img)

            if results.detections:
                for id, detection in enumerate(results.detections):
                    # mpDraw.draw_detection(img, detection)
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, ic = img.shape
                    bbox = int(bboxC.xmin * iw) - 20, int(bboxC.ymin * ih) - 45, int(bboxC.width * iw) + 40, int(bboxC.height * ih) + 50

                    if(countImage > 14 or count > 14):
                        pass
                    else:
                        if cv2.waitKey(1) & 0xFF == ord('b'):
                            timestr = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')
                            x, y, w, h = bbox
                            roi_color = img[y:y+h, x:x+w]
                            roi_color = cv2.resize(roi_color, (180, 180))
                            pathImage = folder + '/' + str(timestr) + ".jpg"
                            cv2.imwrite(pathImage, roi_color)
                            if(self.employee != None):
                                if(self.employee[5] == 'nan'):
                                    self.updatePathAvatar('data/face_train/' + user_id + '/' + str(timestr) + ".jpg")
                            count += 1

                    self.fancyBox(img, bbox)
            cv2.putText(img, f'Total Face: {int(count)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2
                        , (192, 0, 215), 2)
            cv2.imshow('Video', img)

            if (cv2.waitKey(1) & 0xFF == ord('q')):
                if(countImage > 5 or count > 5):
                    break
        video_capture.release()
        cv2.destroyAllWindows()
    
    def fancyBox(self,img, bbox, l=30, t=2, rt=1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
        # cv2.rectangle(img, bbox, (192, 0, 215), rt)
        # Top left x, y
        cv2.line(img, (x, y), (x + l, y), (192, 0, 215), t)
        cv2.line(img, (x, y), (x, y + l), (192, 0, 215), t)
        # Top right x, y
        cv2.line(img, (x1, y), (x1 - l, y), (192, 0, 215), t)
        cv2.line(img, (x1, y), (x1, y + l), (192, 0, 215), t)
        # Bottom left x, y
        cv2.line(img, (x, y1), (x + l, y1), (192, 0, 215), t)
        cv2.line(img, (x, y1), (x, y1 - l), (192, 0, 215), t)
        # Bottom right x, y
        cv2.line(img, (x1, y1), (x1 - l, y1), (192, 0, 215), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (192, 0, 215), t)

    def updatePathAvatar(self,pathImage):
        filename = os.path.abspath('data/Models/Employee.xlsx')
        df = pd.read_excel(filename)
        df.loc[df['user_id'] == self.employee[4], 'avatar'] = pathImage

        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        df.to_excel(writer,index=False)
        writer.save()