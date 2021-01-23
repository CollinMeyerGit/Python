import time
import os
import subprocess
import wikipedia
def openChrome():
    global os
    os.chdir(r"C:\Program Files (x86)\Google\Chrome\Application")
    os.system('chrome.exe')
def openFileExplorer():
    global subprocess
    subprocess.Popen(r'explorer "This PC"')
def showDate():
    months = ["","January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"]
    days = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
    "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth",
    "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "twenty first",
    "twenty second", "twenty third", "twenty fourth", "twenty fifth", "twenty sixth",
    "twenty seventh", "twenty eighth", "twenty ninth", "thirdieth", "thirdy first"]
    global time
    t = time.localtime()
    month = months[t[1]]
    day = days[t[2]]
    year = t[0]
    date = "The date is " + month + "," + str(day) + str(year)
    return date
def wiki(wikiPhrase):
    wikiSummary = wikipedia.summary(wikiPhrase)
    return wikiSummary
def showTime():
    global time
    t = time.localtime()
    hour = t[3]
    minute = t[4]
    if hour > 12:
        hour = hour - 12
        dayNight = "pm"
    else:
        dayNight = "am"
    time = "The time is " + str(hour) + str(minute) + dayNight
    return time