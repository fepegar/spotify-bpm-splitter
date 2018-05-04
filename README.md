# Spotify BPM splitter

This is a toy app to split a Spotify playlist in multiple playlists sorted by tempo / BPM using [`spotipy`](http://spotipy.readthedocs.io/en/latest/).

## Requirements
1. `pip install spotipy`
2. [Spotify credentials](https://developer.spotify.com/my-applications). More info in [`spotipy` docs](http://spotipy.readthedocs.io/en/latest/#authorization-code-flow)

## Usage
Get the playlist URI by right-clicking on it, go to `Share` and `Copy Spotify URI`. Pass it as an argument to the Python script:
```shell
JAZZ_URI="spotify:user:spotify:playlist:37i9dQZF1DWTR4ZOXTfd9K"
./splitter $JAZZ_URI
```

## Caveats
1. You need to create a dummy Spotify app to get your authentication credentials
2. Spotify API doesn't seem to return more than 100 songs from a playlist

## Contributing
Contributions are welcome!
