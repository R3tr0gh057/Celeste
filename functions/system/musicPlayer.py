import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', '..', 'config.ini'))

music_directory = config.get('PATHS', 'music_directory')

def player(songName):
    for filename in os.listdir(music_directory):
        f = os.path.join(music_directory, filename)
        if songName in f.lower():
            print(f"Playing {f}")
            os.startfile(f)

def listsongs():
    for filename in os.listdir(music_directory):
        print(filename)