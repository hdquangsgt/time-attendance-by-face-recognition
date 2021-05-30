import os
import cv2
from keras_facenet import FaceNet
import numpy as np
import pickle

# Lay data trong face_train

path = 'data/face_train'
data = {}

model = FaceNet()


for folder in os.listdir(path):
    data[folder] = []
    for item in os.listdir(os.path.join(path, folder)):
        img = cv2.imread(os.path.join(path, folder, item))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img = np.expand_dims(img, axis = 0)
        # Face extract embedding
        encoding = model.embeddings(img)
        # Add embedding to data face name
        data[folder].append(encoding)
        # Release memories
        del img
        del encoding

with open("Models/data_embeddings.p", "wb") as f:
    pickle.dump(data, f)





# Test lay data trong dictionary
# data = {
#     "Trung": [
#             [1, 2, 3],
#             [4, 5, 6]
#     ],
#     "Quang": [
#             [1,1,1],
#             [2,2,2]
#     ]
# }

# for i in data:
#     for j in data[i]:
#         print(i, '->', j)

