import os
import time
battery = open("output.txt", "r")
percent = battery.readline()
percentnum = percent.split()
percent4real = percentnum[3]
promptnum = "10%"
while percent4real != promptnum:
    os.system("acpi -V > ~/battery-prompt/output.txt")
    time.sleep(30)
os.system("python3 ~/battery-prompt/gui.py")
