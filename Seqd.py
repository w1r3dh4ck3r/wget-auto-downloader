import os

baseRepeat = 0

repeat = int(input("Repet how many times: "))
startNumber = int(input("Starting number: "))
url = str(input("Enter download URL: "))
saveDir = str(input("Save directory: "))

while (baseRepeat < repeat):
    os.system("wget -P " + saveDir + " " + url .format(startNumber))
    baseRepeat = baseRepeat + 1
    startNumber = startNumber + 1
