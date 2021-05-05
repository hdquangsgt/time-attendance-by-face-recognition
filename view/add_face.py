import cv2
import os
import time
import mediapipe as mp 

class AddFaceGUI(object):
    def __init__(self, employee = None):
        self.employee = employee
        if (self.employee):
            user_id = self.employee[4]
            folder = os.path.abspath('data/face_train/'+user_id)

        video_capture = cv2.VideoCapture(0)
        mpFaceDetect = mp.solutions.face_detection
        mpDraw = mp.solutions.drawing_utils

        faceDetection = mpFaceDetect.FaceDetection(0.7)

        while True:
            _, img = video_capture.read()

            # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = faceDetection.process(img)

            if results.detections:
                for id, detection in enumerate(results.detections):
                    # mpDraw.draw_detection(img, detection)
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, ic = img.shape
                    bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

                    if cv2.waitKey(1) & 0xFF == ord('b'):
                        timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
                        x, y, w, h = bbox
                        roi_color = img[y:y+h, x:x+w]
                        roi_color = cv2.resize(roi_color, (180, 180))
                        cv2.imwrite(folder + '/' + str(timestr) + ".jpg", roi_color)

                    self.fancyBox(img, bbox)
                    # cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2
                    #         , (255, 0, 255), 2)
            cv2.imshow('Video', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        video_capture.release()
        cv2.destroyAllWindows()
    
    def fancyBox(self,img, bbox, l=30, t=2, rt=1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
        # cv2.rectangle(img, bbox, (255, 0, 255), rt)
        # Top left x, y
        cv2.line(img, (x, y), (x + l, y), (255, 0, 255), t)
        cv2.line(img, (x, y), (x, y + l), (255, 0, 255), t)
        # Top right x, y
        cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y + l), (255, 0, 255), t)
        # Bottom left x, y
        cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)
        # Bottom right x, y
        cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)

