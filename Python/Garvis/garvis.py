from pynput import keyboard
import pyttsx3
import speech_recognition as sr
import garvisCalls
engine = pyttsx3.init()
r = sr.Recognizer()
r.dynamic_energy_threshold = False
r.energy_threshold = 400
mic = sr.Microphone()
def getAudio():
    idx = 1    
    while(idx <= 3):
        with mic as source:
            engine.say("What can I help you with?")
            engine.runAndWait()
            try:
                audio = r.listen(mic, timeout = 3.0)
            except sr.WaitTimeoutError:
                print('fail')
        try:
            line = r.recognize_google(audio)
        except:
            engine.say("I didn't quite get that, please try again")
            engine.runAndWait()
            idx = idx + 1
        else:
            idx = 0
            return line
def run():
    line = getAudio()
    lineList = line.split()
    for i in lineList:
        if i == "time":
            time = garvisCalls.showTime()
            engine.say(time)
            engine.runAndWait()
        elif i.lower() == "chrome":
            garvisCalls.openChrome()
        elif i.lower() == "explorer":
            garvisCalls.openFileExplorer()
        elif i.lower() == "date":
            date = garvisCalls.showDate()
            engine.say(date)
            engine.runAndWait()
        elif i.lower() == "wikipedia":
            wikiPhrase = line[11:(len(line) - 1)]
            wikiSummary = garvisCalls.wiki(wikiPhrase)
            engine.say(wikiSummary)
            engine.runAndWait()
loop = 1
while(loop == 1):
    goo = input()
    if goo == "exit":
        loop = 2
    else:
        run()
