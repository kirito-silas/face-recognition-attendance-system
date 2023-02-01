import os
import cv2
import numpy as np
import NameFind


#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

recognise = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 15)
recognise.read('trainer/train.xml')


cap = cv2.VideoCapture(0)                                                       
# cap = cv2.VideoCapture('TestVid.wmv')   # Video object

while True:
    ret, img = cap.read()                                                       
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        
        # Eyes should be inside the face.
        gray_face = gray[y: y+h, x: x+w]
        eyes = eye_cascade.detectMultiScale(gray_face)
        for (ex, ey, ew, eh) in eyes:
            ID, conf = recognise.predict(gray_face)
            NAME = NameFind.ID2Name(ID, conf)
            NameFind.DispID(x, y, w, h, NAME, gray)
            #NameFind.DispID(x, y, w, h)
                  
    cv2.imshow('Face Recognition System', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        os.system('encoding.py')
        break

cap.release()
cv2.destroyAllWindows()
