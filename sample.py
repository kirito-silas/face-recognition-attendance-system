import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
up_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')
low_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lowerbody.xml')
while True:
    ret, frame = cap.read()
    frame=imutils.resize(frame, width=min(1000, frame.shape[1]))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    human = human_cascade.detectMultiScale(gray, 1.0485258, 6)
    up = up_cascade.detectMultiScale(gray, 1.0485258, 6)
    low = low_cascade.detectMultiScale(gray, 1.0485258, 6)
    face = face_cascade.detectMultiScale(gray, 1.0485258, 6)
    for (x,y,w,h) in human:
        #gray_face = gray[y: y+h, x: x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(225,225,0),2)
    for (a,b,c,d) in up:
        cv2.rectangle(frame,(a,b),(a+c,b+d),(225,225,0),2)
        print(human)
    for (e,f,g,z) in low:
        cv2.rectangle(frame,(e,f),(e+g,f+z),(225,225,0),2)
        print(human)
    for (i,j,k,l) in face:
        cv2.rectangle(frame,(i,j),(i+k,j+l),(225,225,0),2)
        print(human)

        print(human)

    cv2.imshow('Human Detection System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
