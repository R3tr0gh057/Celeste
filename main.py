import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import requests
from core.voice import speak, take_command
from core.dispatcher import CommandDispatcher

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def wish_me():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Toad!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Toad!")
    else:
        speak("Good Evening Toad!")
    speak("I am Celeste. How may I help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def main():
    dispatcher = CommandDispatcher()
    wish_me()
    while True:
        query = take_command().lower()
        if query == "none":
            continue
        response = dispatcher.dispatch(query)
        if response:
            speak(str(response))

if __name__ == "__main__":
    main()