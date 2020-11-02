# using the spotipy api
import sys
import spotipy
import win32gui
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

# we need some autothentication, because who the fuck are you.
#The Client_ID Client_Secret And redrect url needs to be set by yourself, for now.
username = "-"
    
scope = "user-read-currently-playing"
token = util.prompt_for_user_token(
                           username,
                           scope,
                           client_id='-',
                           client_secret='-',
                           redirect_uri='http://example.com/callback/')
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_playing_track()
    songs = results["item"]["name"]
    print(songs)
