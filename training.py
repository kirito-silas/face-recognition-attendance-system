import os
import cv2
import numpy as np
from PIL import Image

    
LBPHFace = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 15)

path = 'dataset'
def getImageWithID (path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')
        faceImage = faceImage.resize((110,110))
        faceNP = np.array(faceImage, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        FaceList.append(faceNP)
        IDs.append(ID)
        cv2.imshow('Training Set', faceNP)
        cv2.waitKey(1)
    return np.array(IDs), FaceList 
IDs, FaceList = getImageWithID(path)
LBPHFace.train(FaceList, IDs)
print('LBPH FACE RECOGNISER COMPLETE...')
LBPHFace.write('trainer/train.xml')
#LBPHFace.write('trainer/trainer.yml')
print ('ALL XML FILES SAVED...')

cv2.destroyAllWindows()
