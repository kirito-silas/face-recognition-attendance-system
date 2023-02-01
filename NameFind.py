import os
import cv2
import math
import  time

now_time = time.clock()

#face = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#glass_cas = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
glass_cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

WHITE = [255, 255, 255]

def FileRead():
    Info = open("Names.txt", "r")                       
    NAME = []                                           
    while (True):                                       
        Line = Info.readline()
        if Line == '':
            break
        NAME.append (Line.split(",")[1].rstrip())
       
    return NAME                                     
        
Names = FileRead()                                 


previousatt="detect.txt"
if os.path.isfile(previousatt):
    os.remove(previousatt)
else:
    print("Creating new attendance sheet")
fob=open('detect.txt','a')
#f=open('detect.txt','r')
#lines = f.read().split("\n")
#print (lines)

names=[]
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z=str(z)
        file=open("detect.txt","a")
        file.write(z)
        file.write("\t")
        file.write("\n")
        file.close()
        print(z)
    return names
def ID2Name(ID, conf):
    if ID > 0:
        NameString = "Name: " + Names[ID-1]
        print(Names)
        #z = Names
        enterData(Names)
    else:
        NameString = " Face Not Recognised "  
   

    return NameString





def AddName():
    Name = input('Enter Your Name ')
    Info = open("Names.txt", "r+")
    ID = ((sum(1 for line in Info))+1)
    Info.write(str(ID) + "," + Name + "\n")
    print ("Name Stored in " + str(ID))
    Info.close()
    return ID



def DispID(x, y, w, h, NAME, Image):
#def DispID(x, y, w, h):

    #  

    Name_y_pos = y - 10
    Name_X_pos = x + w//2 - (len(NAME)*7//2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ---------------------------
    
    draw_box(Image, x, y, w, h)
    
                  
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), (0,0,0), -2)           # Draw a Black Rectangle over the face frame
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, NAME, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         # Print the name of the ID


def draw_box(Image, x, y, w, h):
    cv2.line(Image, (x, y), (x + (w//5) ,y), WHITE, 2)
    cv2.line(Image, (x+((w//5)*4), y), (x+w, y), WHITE, 2)
    cv2.line(Image, (x, y), (x, y+(h//5)), WHITE, 2)
    cv2.line(Image, (x+w, y), (x+w, y+(h//5)), WHITE, 2)
    cv2.line(Image, (x, (y+(h//5*4))), (x, y+h), WHITE, 2)
    cv2.line(Image, (x, (y+h)), (x + (w//5) ,y+h), WHITE, 2)
    cv2.line(Image, (x+((w//5)*4), y+h), (x + w, y + h), WHITE, 2)
    cv2.line(Image, (x+w, (y+(h//5*4))), (x+w, y+h), WHITE, 2)


# -
def DispID2(x, y, w, h, NAME, Image):


    Name_y_pos = y - 40
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), (0,0,0), -2)           # Draw a Black Rectangle over the face frame
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, NAME, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         # Print the name of the ID


def DispID3(x, y, w, h, NAME, Image):


    Name_y_pos = y - 70
    Name_X_pos = x + w//2 - (len(NAME)*7//2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), (0,0,0), -2)           
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, NAME, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)             


def DrawBox(Image, x, y, w, h):
    cv2.rectangle(Image, (x, y), (x + w, y + h), (255, 255, 255), 1)     



def DetectEyes(Image):
    Theta = 0
    rows, cols = Image.shape
    glass = glass_cas.detectMultiScale(Image)                                              
    for (sx, sy, sw, sh) in glass:
        if glass.shape[0] == 2:                                                             
            if glass[1][0] > glass[0][0]:
                DY = ((glass[1][1] + glass[1][3] / 2) - (glass[0][1] + glass[0][3] / 2))   
                DX = ((glass[1][0] + glass[1][2] / 2) - glass[0][0] + (glass[0][2] / 2))    
            else:
                DY = (-(glass[1][1] + glass[1][3] / 2) + (glass[0][1] + glass[0][3] / 2)) 
                DX = (-(glass[1][0] + glass[1][2] / 2) + glass[0][0] + (glass[0][2] / 2))   

            if (DX != 0.0) and (DY != 0.0):                                               
                Theta = math.degrees(math.atan(round(float(DY) / float(DX), 2)))            
                print ("Scanning..  " + str(Theta))

                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), Theta, 1)                
                Image = cv2.warpAffine(Image, M, (cols, rows))
                # cv2.imshow('ROTATED', Image)                                             

                Face2 = face.detectMultiScale(Image, 1.3, 5)                                
                for (FaceX, FaceY, FaceWidth, FaceHeight) in Face2:
                    CroppedFace = Image[FaceY: FaceY + FaceHeight, FaceX: FaceX + FaceWidth]
                    return CroppedFace


def tell_time_passed():
    print ('TIME PASSED ' + str(round(((time.clock() - now_time)/60), 2)) + ' MINS')

