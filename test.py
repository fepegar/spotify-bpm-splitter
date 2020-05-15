import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

credentials = SpotifyClientCredentials()
token = util.prompt_for_user_token(
    username='ferniss',
    scope='playlist-modify-private')
spotify = spotipy.Spotify(auth=token)
sp = spotify

uri = 'spotify:playlist:0kNHFNoDBVu9u8SpwgWTos'
username = 'ferniss'
playlist = sp.user_playlist(username, uri)

for idx, track_dict in enumerate(playlist['tracks']['items']):
    print(idx + 1, track_dict['track']['name'])
