import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', 'config.ini'))

def get_music_directory():
    return config.get('PATHS', 'music_directory')

def get_email_credentials():
    email = config.get('EMAIL', 'address')
    password = config.get('EMAIL', 'password')
    return email, password
