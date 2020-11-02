

# using the spotipy api
import sys
import vlc
import spotipy
import pafy
import win32gui
from spotipy.oauth2 import SpotifyOAuth
from youtube_search import YoutubeSearch
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
    songName = results["item"]["name"]
    artistName = results['item']['album']['artists'][0]['name']
    search = songName + " - " + artistName
    searchResult = YoutubeSearch(search, max_results=1).to_dict()
   # print(songName)
    print(artistName)
    print(search)
    print(searchResult[0]['id'])

# Youtube part
url = 'https://youtube.com/watch?v=' + searchResult[0]['id']
video = pafy.new(url)
best = video.getbestvideo()
media = vlc.MediaPlayer(best.url)
media.play()
media.set_fullscreen(True)
media.audio_set_mute(True)
while True:
     pass
