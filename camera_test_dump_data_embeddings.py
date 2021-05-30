import pickle
import numpy as np
import cv2
from keras_facenet import FaceNet
import mediapipe as mp 
from scipy.spatial.distance import cosine

video_capture = cv2.VideoCapture(0)

mpFaceDetect = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils

faceDetection = mpFaceDetect.FaceDetection(0.6)
model = FaceNet()

with open("Models/data_embeddings.p", "rb") as f:
    data = pickle.load(f)

        

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
            bbox = int(bboxC.xmin * iw) - 20, int(bboxC.ymin * ih) - 45, int(bboxC.width * iw) + 40, int(bboxC.height * ih) + 50
            
            x, y, w, h = bbox
            roi_color = img[y:y+h, x:x+w]
            if roi_color.shape[0] != 0 and roi_color.shape[1] != 0:
                roi_color = cv2.resize(roi_color,(160,160))
                face_preprocess = cv2.cvtColor(roi_color, cv2.COLOR_BGR2RGB)
                face_preprocess = np.expand_dims(roi_color, axis = 0)

                face_feature = model.embeddings(face_preprocess)
                
                distance = 99999
                name = 'Unknow'
                for db_name in data:
                    for encoding in data[db_name]:
                        dist = cosine(encoding, face_feature)
                        if dist < 0.25 and dist < distance:
                            name = db_name
                            distance = dist
                cv2.putText(img, name, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(distance, '->', name)
                fancyBox(img, bbox)
                # cv2.putText(img, str(result[0]), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                # print(proba, ' -> ', result[0])
                
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()






