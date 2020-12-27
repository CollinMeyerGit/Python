import pyttsx3
import os
import speech_recognition as sr
import time
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
                audio = r.listen(source, timeout = 3.0)
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
line = getAudio()
print(line.lower())

if line.lower() == "run chrome":
    os.chdir(r"C:\Program Files (x86)\Google\Chrome\Application")
    os.system('chrome.exe')
elif line.lower() == "what time is it":
    t = time.localtime()
    time = "The time is " + str(t[3]) + " " + str(t[4])
    print(time)
    engine.say(time)
    engine.runAndWait()
quit