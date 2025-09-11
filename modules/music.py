import os
from core.config import get_music_directory

def play_song(song_name):
    music_directory = get_music_directory()
    for filename in os.listdir(music_directory):
        f = os.path.join(music_directory, filename)
        if song_name.lower() in f.lower():
            print(f"Playing {f}")
            os.startfile(f)
            return f"Playing {filename}"
    return "Song not found."

def list_songs():
    music_directory = get_music_directory()
    songs = os.listdir(music_directory)
    for filename in songs:
        print(filename)
    return songs
