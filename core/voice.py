import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
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
