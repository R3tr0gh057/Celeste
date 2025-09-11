from modules.music import play_song, list_songs
from modules.ai import get_ai_response
from modules.search import search_google, search_youtube, search_images
from modules.email import send_email
from modules.bruteforce import run_bruteforce

class CommandDispatcher:
    def __init__(self):
        self.command_map = {
            'play the song': self.handle_play_song,
            'songs in my playlist': self.handle_list_songs,
            'search google for': self.handle_search_google,
            'search youtube for': self.handle_search_youtube,
            'search images for': self.handle_search_images,
            'email to someone': self.handle_send_email,
            'run brute force': self.handle_bruteforce,
            'ai': self.handle_ai_response,
        }

    def dispatch(self, query):
        for key, handler in self.command_map.items():
            if key in query:
                return handler(query)
        return self.handle_ai_response(query)

    def handle_play_song(self, query):
        # Extract song name from query
        song = query.replace('play the song', '').strip()
        return play_song(song)

    def handle_list_songs(self, query):
        return list_songs()

    def handle_search_google(self, query):
        searchterm = query.replace('search google for', '').strip()
        return search_google(searchterm)

    def handle_search_youtube(self, query):
        searchterm = query.replace('search youtube for', '').strip()
        return search_youtube(searchterm)

    def handle_search_images(self, query):
        searchterm = query.replace('search images for', '').strip()
        return search_images(searchterm)

    def handle_send_email(self, query):
        # In practice, would prompt for content/receiver
        return send_email('receiver@example.com', 'content')

    def handle_bruteforce(self, query):
        # Extract target from query
        return run_bruteforce(query)

    def handle_ai_response(self, query):
        return get_ai_response(query)
