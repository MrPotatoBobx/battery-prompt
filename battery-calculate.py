import os
import time
os.system("acpi -V > output.txt")
battery = open("output.txt", "r")
percent = battery.readline()
percentnum = percent.split()
percent4real = percentnum[3]
promptnum = "10%"
while percent4real != promptnum:
    battery = open("output.txt", "r")
    percent = battery.readline()
    percentnum = percent.split()
    percent4real = percentnum[3]
    promptnum = "10%"

    os.system("acpi -V > output.txt")
    time.sleep(30)
os.system("python3 gui.py")
