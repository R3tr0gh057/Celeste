import os

def player(songName):
    directory = '' #add your music directory here
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if songName in f.lower():
            print(f"Playing {f}")
            os.startfile(f)

def listsongs():
    directory = '' #add your music directory here
    for filename in os.listdir(directory):
        print(filename)