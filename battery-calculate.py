import os
import time

os.system("acpi -V > output.txt")
battery = open("output.txt", "r")
percent = battery.readline()
percentnum = percent.split()
percent4real = percentnum[3]
percentage = int(percent4real[:-1])
while percentage <= 10:
    
    battery = open("output.txt", "r")
   
    
    percent = battery.readline()
    percentnum = percent.split()
    percent4real = percentnum[3]
    percentage = int(percent4real[:-1])
    print ("test")
    os.system("acpi -V > output.txt")
    time.sleep(10)
os.system("python3 gui.py")

