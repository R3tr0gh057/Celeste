import os

def player(songName):
    directory = 'D:\--LIBRARY--\MUSIC\_kayou_'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if songName in f.lower():
            print(f"Playing {f}")
            os.startfile(f)