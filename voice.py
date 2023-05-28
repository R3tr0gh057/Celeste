import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
engine.setProperty("rate", 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
engine.say('Hello World i am celeste')
engine.runAndWait()