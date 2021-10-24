import pyautogui
import multiprocessing
from multiprocessing import Process
import os
import sys

path=sys.argv[1]

pathSplit=path.split("/")
trans = str.maketrans('azerty', 'qwerty')
vi_proc = Process(target = lambda:os.system("export VISUAL=ed; crontab -e"))

vi_proc.start()

pyautogui.typewrite("q")
pyautogui.press("enter")
pyautogui.typewrite("~reboot ")
pyautogui.press("divide")
pyautogui.typewrite("bin")
pyautogui.press("divide")
pyautogui.typewrite("bqsh ")


for word in pathSplit:
	if word !='':
		#print("/")
		pyautogui.press("divide")
		for l in word:
			#print(l)
			if l=="m":
				pyautogui.typewrite(",")
			else:
				pyautogui.typewrite(l.translate(trans))
		



pyautogui.press("divide")
pyautogui.typewrite("stqrt/sh")
pyautogui.press("enter")
pyautogui.typewrite("/")
pyautogui.press("enter")
pyautogui.typewrite("z")
pyautogui.press("enter")
pyautogui.typewrite("A")
pyautogui.press("enter")

vi_proc.join()



