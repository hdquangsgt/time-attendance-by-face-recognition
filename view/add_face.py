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

        def fancyBox(img, bbox, l=30, t=2, rt=1):
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

                    fancyBox(img, bbox)
                    # cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2
                    #         , (255, 0, 255), 2)
            cv2.imshow('Video', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        video_capture.release()
        cv2.destroyAllWindows()

    def detect_face(self, frame):
        mpFaceDetect = mp.solutions.face_detection
        mpDraw = mp.solutions.drawing_utils

        faceDetection = mpFaceDetect.FaceDetection(0.7)

        results = faceDetection.process(frame)
        boxx = []
        if results.detections:
            for id, detection in enumerate(results.detections):
                # mpDraw.draw_detection(img, detection)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = frame.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                boxx.append(bbox)
        return boxx

    def fancyBox(self, img, bbox, l=30, t=2, rt=1):
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

    def show_frame(self):
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
                        cv2.imwrite("dataset/" +  str(face_id) + '/' +
                            str(timestr) + ".jpg", roi_color)
                            
                    fancyBox(img, bbox)
                    cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2
                            , (255, 0, 255), 2)
                cv2.imshow('Video', img)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break

    def snapshot(self):
        user_id = self.employee[4]
        folder = os.path.abspath('data/face_train/'+user_id)
        # Get a frame from the video source
        ret, frame = self.get_frame()
        boxx = self.detect_face(frame)
        for i in boxx:
            x, y, w, h = i
            roi_face = frame[y:y+h, x:x+w]   
            roi_face = cv2.resize(roi_face, (180, 180))

            name = "/frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
            if ret:
                cv2.imwrite(folder + name, cv2.cvtColor(roi_face, cv2.COLOR_BGR2RGB))

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
        self.root.destroy()
        cv2.destroyAllWindows()
        frame = Tk()
        employee = EmployeeGUI(frame)

