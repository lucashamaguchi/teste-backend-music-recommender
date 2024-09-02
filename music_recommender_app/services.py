from teste_backend_music_recommender.settings import OPEN_WEATHER_APP_ID, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from base64 import b64encode
import requests

DEFAULT_GENRES = {
    'high': 'pop',
    'medium': 'rock',
    'low': 'classical'
}

class MusicRecommender(object):
    def __init__(self):
        pass

    def get_song_indications_by_location(self, lat, long, *args, **kwargs) -> dict:
        temperature = self._get_temperature_by_location(lat, long)
        genre = self._get_song_genre_by_temperature(temperature)
        songs = self._get_song_recommendations_by_genre(genre)
        return {
            'temperature': temperature,
            'genre': genre,
            'songs': songs
        }

    def _get_temperature_by_location(self, lat, long, *args, **kwargs) -> int:
        # TODO: implement integration with openweather here
        url = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={appid}&exclude=minutely,hourly,daily,weekly&units=metric'.format_map({
            'lat': lat,
            'long': long,
            'appid': OPEN_WEATHER_APP_ID
        })

        req = requests.get(url)

        response = req.json()

        return response.get('current', {}).get('temp', 0)

    def _get_song_genre_by_temperature(self, temperature, *args, **kwargs) -> str:
        # in case we need to customize the logic for genre by temperature, for exemple if we need to get from a database
        # the current recommendation genre or if we start customizing from a specific user or session
        temperature_level = 'low'
        if temperature > 25:
            temperature_level = 'high'
        elif temperature >= 10:
            temperature_level = 'medium'
        return DEFAULT_GENRES[temperature_level]

    def _get_song_recommendations_by_genre(self, genre) -> list:
        # TODO: implement integration with music recommendations here
        token = self.__get_spotify_token()
        
        url = 'https://api.spotify.com/v1/recommendations'
        req = requests.get(url,
            params={
                'seed_genres': genre
            },
            headers={
                'authorization': f'Bearer {token}'
            }
        )
        
        response = req.json()
        
        tracks = response.get('tracks', list())
        return [
            {
                'name': track.get('name'),
                'url': track.get('external_urls', dict()).get('spotify', ''),
                'images': track.get('album', dict()).get('images', list()),
            } for track in tracks
        ]


    def __get_spotify_token(self):
        url = 'https://accounts.spotify.com/api/token'
        req = requests.post(url, {'grant_type': 'client_credentials'}, headers={
            'authorization': 'Basic {}'.format(b64encode(f'{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}'.encode()).decode())
        })
        
        response = req.json()
                
        return response.get('access_token', '')
