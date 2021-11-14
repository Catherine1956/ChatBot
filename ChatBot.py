import sys
import time
from gtts import gTTS
import pyttsx3
import os

Q = [
    "what is your name?",
    "what did you do?",
    "what is your favourite color?",
    "who is your favourite hero?",
]
A = [
    "Artificial Intelligence",
    "I do my best to help you",
    " I like every color",
    "You are my favourite hero",
]
uname = "sir"
pcname = "PC"
file = open(os.path.dirname(os.path.abspath(__file__)) + "\dataset.txt", "r")
data = file.read()
file.close()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty("rate", rate - 25)
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def separate(data):
    split_data = data.split("\n")
    questiona = [
        split_data[i].replace("- - ", "")
        for i in range(0, len(split_data))
        if i % 2 == 0
    ]
    answera = [
        split_data[i].replace("  - ", "")
        for i in range(0, len(split_data))
        if i % 2 != 0
    ]
    global Q1, A1
    Q1 = Q + questiona
    A1 = A + answera


def Input():
    I = input(uname + ":")
    I = str.lower(I)
    find(I)


def find(I):
    for j in range(0, 3):
        b = "Typing" + "." * j
        print(b, end="\r")
        time.sleep(0.4)
    for i in range(0, len(Q1)):
        if I.lower() == str.lower(Q1[i]):
            print(pcname + ":" + A1[i])
            speak(A1[i])
            Input()
    else:
        print(pcname + ":" + "I'm unable to answer your query.")
        speak("I'm unable to answer your query.")
        Input()


separate(data)

Input()
