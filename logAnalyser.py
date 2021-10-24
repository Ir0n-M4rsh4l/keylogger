import os
import sys
import datetime

date=datetime.datetime.now()
day=datetime.datetime.today()
f=open("logAnalyse"+str(day)+".txt","w")

log=sys.argv[1]
logf=open(log,"r")

class event:
    def __init__(self,date,process,window,key):
        self.date=date
        self.process=process
        self.window=window
        self.key=key

lines=logf.readlines()
i=2
current_window = str(lines[4])
f.write("#####################################\n")
f.write("New " + str(current_window) )
f.write(str(lines[2]) )
f.write("#####################################\n")
string=""

while i < len(lines):

    e=event(str(lines[i]),str(lines[i+1]),str(lines[i+2]),str(lines[i+3]))
    string+=(str(e.key))
    
    if current_window == e.window :
        pass
       
    else :
        f.write(string + "\n")
        string=""
       # f.write("-----------------------------------\n")
        f.write("#####################################\n")
        f.write("New " + str(e.window) )
        f.write(str(e.date))
        f.write("#####################################\n")
        current_window = e.window
    i+=5


f.write(string)

f.close()
logf.close
