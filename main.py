import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import time

import selenium
from sys import stdout
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[+] Listening...\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("[+] Recognizing...\n")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
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

#Automated google search using selenium
def googlesearch(content):
    keyword = content
    search_selector = '#APjFqb' #search abr css selector
    button_selector = 'gNO89b' #search button class name
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--disable-extentions")
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(chrome_options=opt)
    wait = WebDriverWait(browser, 10)
    try:
        browser.get(content)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, button_selector)))
        sel_search = browser.find_element(By.CSS_SELECTOR, search_selector)
        enter = browser.find_element(By.CLASS_NAME, button_selector)
        
        speak('What should I search for you?') #search using voice
        search_string = takeCommand().lower()
        sel_search.send_keys(search_string)
        time.sleep(2)
        enter.click()
        
    except selenium.common.exceptions.NoSuchElementException:
        print('Missing element')
        speak('A selector element cannot be found or has been replaced')
    
    except selenium.common.exceptions.ElementNotInteractableException:
        print('Element not interactable')
        speak('The website has crashed due to the element being non interactable')
    
    #Block to navigate thu search tabs
    query = takeCommand().lower()
    if 'go to images' in query:
        speak('going to images')
        images = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div/div[1]/div/div[1]/div/div[3]/a')
        images.click()

    elif 'go to maps' in query:
        speak('checking maps')
        maps = browser.find_element(By.CSS_SELECTOR, '#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a')
        maps.click()

    elif 'go to videos' in query:
        speak('searching youtube for your query')
        youtubeSearch()

#Function to search youtube and play the first video
def youtubeSearch():
    search_selector = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input' #search bar xpath
    button_selector = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button' #search button xpath
    video_selector = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string' #video selector xpath
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--disable-extentions")
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(chrome_options=opt)
    wait = WebDriverWait(browser, 10)
    try:
        browser.get('https://www.youtube.com/')
        wait.until(EC.presence_of_element_located((By.XPATH, button_selector)))
        sel_search = browser.find_element(By.XPATH, search_selector)
        enter = browser.find_element(By.XPATH, button_selector)
        
        speak('What should I search for you?') #search using voice
        search_string = takeCommand().lower()
        sel_search.send_keys(search_string)
        time.sleep(2)
        enter.click()

        wait.until(EC.presence_of_element_located((By.XPATH, video_selector)))
        vid_click = browser.find_element(By.XPATH, video_selector)
        vid_click.click()
        
    except selenium.common.exceptions.NoSuchElementException:
        print('Missing element')
        speak('A selector element cannot be found or has been replaced')
    
    except selenium.common.exceptions.ElementNotInteractableException:
        print('Element not interactable')
        speak('The website has crashed due to the element being non interactable')

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            youtubeSearch()

        elif 'open google' in query:
            #webbrowser.open("google.com")
            googlesearch('https://www.google.com/')

        elif 'open stack' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            try:
                music_dir = 'D:\\--LIBRARY--\\MUSIC\\_shisha_'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                print(e)
                speak("Apologies toad, I could not find your music directory")

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