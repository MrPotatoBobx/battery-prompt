import os
import time

os.system("acpi -V > output.txt")
battery = open("output.txt", "r")
percent = battery.readline()
percentnum = percent.split()
percent4real = percentnum[3]
percentage = int(percent4real[:-1])
charge = percentnum[2]

while charge != "Discharging,":
    battery = open("output.txt", "r")
    percent = battery.readline()
    percentnum = percent.split()
    percent4real = percentnum[3]
    percentage = int(percent4real[:-1])
    charge = percentnum[2]  
    os.system("acpi -V > output.txt")
    time.sleep(20)



while percentage >= 10:
    
    battery = open("output.txt", "r")
   
    os.system("acpi -V > output.txt")
    percent = battery.readline()
    percentnum = percent.split()
    percent4real = percentnum[3]
    percentage = int(percent4real[:-1])
    time.sleep(30)
os.system("python3 gui.py")
