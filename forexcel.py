import xlwt
import xlrd
from datetime import datetime
import time
import datetime
import os
#-------------------------------------
dt_date = datetime.datetime.now()
 
#print ("The Current date is:" ,dt_date)
 
#print("In specified format:", dt_date.strftime("%A, %d %b %Y,\t %T"))
print("time",dt_date.strftime("%T"))

#----------------------------------------
date = xlwt.easyxf(num_format_str='D-MMM-YY')
time = xlwt.easyxf(num_format_str='H:M')
#td = time.strftime("%d-%m-%Y")
a = input ("enter the file name with .txt")
name=input("Enter the name of the class and semester")

book = xlwt.Workbook()
ws = book.add_sheet('First Sheet')
f = open('text/'+a, 'r+')
data = f.readlines()
#ws.write(0, 0, datetime.now(), date)
check = dt_date

#---------------------------------------------
if check.hour == 9 and check.minute <= 30:
    h = ('First hour')
elif check.hour == 10 and check.minute >= 20:
    h = ('Second hour')
elif check.hour == 11 and check.minute >= 20:
    h = ('Third hour')
elif check.hour == 12 and check.minute >= 10:
    h = ('Fourth hour')
elif check.hour == 14 and check.minute >= 00:
    h = ('Fifth hour')
elif check.hour  == 15 and check.minute <= 40:
    h = ('Sixth hour')
else:
    print("Error in timings")
    h = ('wrong time')
print(h)
#-------------------------------------

for i in range(len(data)):
    row = data[i].split()
    ws.write(i,3,"Present")
    ws.write(i,4,dt_date,date)
    #ws.write(i,4,dt_date)
    ws.write(i,5,dt_date,time)
    ws.write(i,6,h)
    for j in range(len(row)):
        ws.write(i, j, row[j])
        #ws.write(i,j+1,datetime.now(),date)

book.save(os.path.join('attendence',(name+" "+dt_date.strftime("%A, %d %b %Y")+" "+h+'.xls')))
#book.save(name+" "+check+'.xls')
print("File "+name+" has been saved")
f.close()
