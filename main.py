import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import requests
import time
from core.voice import speak, take_command
from core.dispatcher import CommandDispatcher



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
        # Efficient listening with timeout and phrase_time_limit
        query = take_command(timeout=5, phrase_time_limit=10)
        if not query or query.lower() == "none":
            continue
        # Prompt engineering for AI queries
        if 'ai' in query.lower() or query.strip():
            conversational_prompt = (
                f"You are Celeste, a friendly and helpful AI assistant. Respond in a natural, conversational way, avoid bullet points or numbered lists, and keep the tone engaging and human-like. Here is the user's message: {query}"
            )
            response = dispatcher.dispatch(conversational_prompt)
        else:
            response = dispatcher.dispatch(query)
        if response:
            print(f"Celeste: {response}")
            speak(str(response))
            time.sleep(10)

if __name__ == "__main__":
    main()