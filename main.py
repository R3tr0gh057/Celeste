import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
# import webbrowser
import os
import smtplib
import requests

# from functions.browser.searchTools import imgsearch,gogsearch,ytsearch
# from functions.browser.tabNavigation import closeTab,switchTab
# from functions.exploits.passwordCracking import brutes
# from functions.ai_res.gpt import gpt_res
from functions.system.musicPlayer import player, listsongs
from functions.ai_res.local_ollama import get_ai_response

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Toad!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Toad!")   

    else:
        speak("Good Evening Toad!")  

    speak("I am Celeste. How may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[+] Listening...\n")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=None, timeout=None)

    try:
        print("[+] Recognizing...\n")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("[!] Say that again please...\n")  
        return "None"
    return query

#Needs improvement
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def main():
        # Logic for executing tasks based on query
        while True:
            query = takeCommand().lower()
            if '' in query: #add your own hotword for the AI in the quotes 
                speak('How may I help you?')
                query = takeCommand().lower()
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("search wikipedia for ", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open stack' in query:
                    webbrowser.open("stackoverflow.com")   

                elif 'play the song' in query:
                    try:
                        song = query.replace("play music", "")
                        player(song)

                    except Exception as e:
                        print(e)
                        speak("Apologies toad, I could not find the music in your music directory")

                elif 'songs in my playlist' in query:
                    try:
                        listsongs()
                    except:
                        print("Could not find your music directory")

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in query:
                    try:
                        codePath = "PATH"
                        os.startfile(codePath)
                    except Exception as e:
                        print(e)
                        speak("Apologies toad, I could not find the code directory")

                elif 'email to someone' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        speak("Whom should I send it to?")
                        receiver = takeCommand()    
                        sendEmail(receiver, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Apologies Toad, I could not send the mail")

                elif 'search images for' in query:
                    searchterm = query.replace("search images for", "")
                    try:
                        speak(f"Searching images for {searchterm}")
                        imgsearch(searchterm)
                    except Exception as e:
                        print(e)
                        speak("Apologies toad, an exception error has been raised")  

                elif 'search google for' in query:
                    searchterm = query.replace("search google for", "")
                    try:
                        speak(f"Searching google for {searchterm}")
                        gogsearch(searchterm)
                    except Exception as e:
                        print(e)
                        speak("Apologies toad, an exception error has been raised")

                elif 'search youtube for' in query:
                    searchterm = query.replace("search youtube for", "")
                    try:
                        speak(f"Searching youtube for {searchterm}")
                        ytsearch(searchterm)
                    except Exception as e:
                        print(e)
                        speak("Apologies toad, an exception error has been raised")

                elif 'close all tabs' in query:
                    try:
                        closeTab()
                    except Exception as e:
                        print(e)
                        speak("Exception was raised")
                
                elif 'switch tabs' in query:
                    try:
                        switchTab()
                    except Exception as e:
                        print(e)
                        speak("Apologies toad, an exception error has been raised")

                elif 'run brute force' in query:
                    try:
                        query = query.replace("run brute force on", "")
                        if 'instagram' in query:
                            website = 'https://www.instagram.com/accounts/login/'
                            user_selector = '#loginForm > div > div:nth-child(1) > div > label > input'
                            pass_selector = '#loginForm > div > div:nth-child(2) > div > label > input'
                            enter = '#loginForm > div > div:nth-child(3) > button'
                        elif 'github' in query:
                            website = 'https://github.com/login'
                            user_selector = '#login_field'
                            pass_selector = '#password'
                            enter = '#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button'
                        elif 'reddit' in query:
                            website = 'https://www.reddit.com/login/'
                            user_selector = '#loginUsername'
                            pass_selector = '#loginPassword'
                            enter = 'body > div > main > div.OnboardingStep.Onboarding__step.mode-auth > div > div.Step__content > form > fieldset:nth-child(8) > button'
                        elif 'facebook' in query:
                            website = 'https://www.facebook.com/login/'
                            user_selector = '#email'
                            pass_selector = '#pass'
                            enter = '#u_0_5_Cb'

                        speak('What is the username of the target?')
                        username = takeCommand().lower()
                        passlist = '' #add the path to the passlist file
                        brutes(username, user_selector, pass_selector,enter,passlist,website)
                    
                    except Exception as e:
                        print(e)
                        speak("The password has been found or you have been locked out, bruteforcing complete")
                
                else:
                    try:
                        answer = get_ai_response(query)
                        print(f"To answer your question, {answer}")
                        speak(answer)
                    except Exception as e:
                        print(e)
                        speak('That didnt work')

if __name__ == "__main__":
    main()