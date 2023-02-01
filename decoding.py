import base64
import os

f=open('text/encodedface.txt','r')
lines = f.read().split("\n")
maindata=[]
for i in range(0,len(lines)):
    maindata.append(base64.b64decode(lines[i]))
print(maindata)

fob=open('text/DecodedResults.txt','w+')

for i in range(0,len(maindata)):
    fob.write(str(maindata[i]) + '\n')
fob.close()
os.system('comparingclasses.py')
