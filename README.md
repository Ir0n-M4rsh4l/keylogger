# The project
This project is a simple linux keylogger. When activated, it registers all the actions made with the keyboard. The log files are registered in the computer, ready to be analysed by the logAnalyser code. The singularity of this project is that the keylogger program is launched at every boot of the computer. Moreover the installation of the keylogger doesn't request a root access to the machine.

# Installation
Download the codes and place them in a folder. Execute automatic.py with the path to start.sh as argument to launched the keylogger at every boot. Don't forget to change the directories in start.sh. To stop the keylogger, use stop.sh
