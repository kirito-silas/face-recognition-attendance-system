import cv2                  
import numpy as np          
import NameFind

WHITE = [255, 255, 255]


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
ID=NameFind.AddName()
Count = 0
while Count < 100:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                                    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                                         
    for (x, y, w, h) in faces:                                                                  
        FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]     
        Img = (NameFind.DetectEyes(FaceImage))
        cv2.putText(gray, "FACE DETECTED", (x+(w//2), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
        if Img is not None:
            frame = Img                                                                         
        else:
            frame = gray[y: y+h, x: x+w]
        cv2.imwrite("dataset/User." + str(ID) + "." + str(Count) + ".jpg",frame)
        cv2.waitKey(300)   
        cv2.imshow("CAPTURED PHOTO", frame)
        Count = Count + 1
        
    cv2.imshow('Face Recognition System Capture Faces', gray)                                       
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
