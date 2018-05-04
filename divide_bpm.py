import sys
import math
from collections import OrderedDict

import spotipy
import spotipy.util as util


class Divider:

    def __init__(self, username):
        self.username = username
        self.spotify = self.get_spotify()

    @staticmethod
    def get_id_from_uri(uri):
        return uri.split(':')[-1]

    @staticmethod
    def sort_dict(dict_random):
        dict_sorted = OrderedDict(
            sorted(dict_random.items(), key=lambda x: x[1], reverse=True))
        return dict_sorted

    def get_spotify(self):
        token = util.prompt_for_user_token(
            username=self.username,
            scope='playlist-modify-private')
        spotify = spotipy.Spotify(auth=token)
        return spotify

    def get_tempos_dict(self, playlist_uri):
        # Seems to get only 100 tracks
        playlist = self.spotify.user_playlist(self.username, playlist_uri)
        tempos_dict = {}
        for i, track_dict in enumerate(playlist['tracks']['items'], 1):
            track = track_dict['track']
            features = self.spotify.audio_features(track['uri'])[0]
            print(f"{i:3} {track['name']:40} {features['tempo']}")
            tempos_dict[track['uri']] = features['tempo']
        tempos_dict = self.sort_dict(tempos_dict)
        return tempos_dict

    def create_playlist(self, name):
        playlist_dict = self.spotify.user_playlist_create(
            self.username, name, public=False)
        return playlist_dict['uri']

    def add_to_playlist(self, playlist_uri, track_uri):
        playlist_id = self.get_id_from_uri(playlist_uri)
        self.spotify.user_playlist_add_tracks(
            self.username, playlist_id, [track_uri])

    def divide(self, playlist_uri):
        playlists_dict = {}
        tempos_dict = self.get_tempos_dict(playlist_uri)
        for track_uri, tempo in tempos_dict.items():
            tempo_floor_10 = 10 * math.floor(tempo / 10)
            playlist_name = f'{tempo_floor_10}-{tempo_floor_10 + 10} bpm'
            if playlist_name in playlists_dict:
                playlist_uri = playlists_dict[playlist_name]
            else:
                playlist_uri = self.create_playlist(playlist_name)
                playlists_dict[playlist_name] = playlist_uri
            self.add_to_playlist(playlist_uri, track_uri)



def main():
    try:
        uri = sys.argv[1]
    except IndexError:
        uri = 'spotify:user:ferniss:playlist:3DsmWF9iyzA3m4Y9E1db6i'  # 2018
        print('No URI was provided. Using', uri)

    divider = Divider('ferniss')
    divider.divide(uri)


if __name__ == '__main__':
    main()
