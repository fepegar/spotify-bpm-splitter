import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

credentials = SpotifyClientCredentials()
# token = credentials.get_access_token()
token = util.prompt_for_user_token(
    username=username,
    scope='playlist-modify-private')
spotify = spotipy.Spotify(auth=token)
sp = spotify

uri = 'spotify:user:ferniss:playlist:54OuamNpPqUoYzJJPgt1Nb'
username = 'ferniss'
playlist = sp.user_playlist(username, uri)

tempos_dict = {}
for track_dict in playlist['tracks']['items']:
    track = track_dict['track']
    features = sp.audio_features(track['uri'])[0]
    print(track['name'], features['tempo'])
    tempos_dict[track['uri']] = features['tempo']
