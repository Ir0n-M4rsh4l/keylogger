kill -9 $(ps aux | grep python3 | grep keylogger.py | cut -d " " -f6)
 