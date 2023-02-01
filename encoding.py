import os
import base64
previousatt="encodedface.txt"
if os.path.isfile(previousatt):
    os.remove(previousatt)
else:
    print("Creating new attendance sheet")
fob=open('encodedface.txt','a')
f=open('detect.txt','r')
lines = f.read().split("\n")
print (lines)


names=[]
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        
        z=str(z)
        
        file=open("encodedface.txt","a")
        file.write(z)
        #file.write("\t")
        file.write("\n")
        file.close()
        

        
    return names
for i in range(0,len(lines)):
    data=lines[i].encode('utf-8')
    name=str(base64.b64encode(data).decode())
    print(name)
    enterData(name)
f.close()
os.remove('detect.txt')
