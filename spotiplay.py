import sys
import vlc
import spotipy
import pafy
import time
import math
import os
import win32gui
from spotipy.oauth2 import SpotifyOAuth
from youtube_search import YoutubeSearch
import spotipy.util as util
# We need some Authentication.
# The Client_ID Client_Secret And Username needs to be set by yourself, for now.
username = "-"
scope = "user-read-currently-playing"
token = util.prompt_for_user_token(
                           username,
                           scope,
                           client_id='-',
                           client_secret='-',
                           redirect_uri='http://example.com/callback/')

class spotiplay(object):
    def EeverythingActually(self):
        # GETTING THE SONG
        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_playing_track()
            songName = results["item"]["name"]
            artistName = results['item']['album']['artists'][0]['name']

            search = songName + " - " + artistName
            searchResult = YoutubeSearch(search, max_results=1).to_dict()
            print("Song Author " + artistName)
            print(searchResult[0]['id'])
            songTimeStamp = results['progress_ms'] / 1000
            SpotifySongDuration = results['item']['duration_ms'] /1000
            roundedSongTimeStamp = math.trunc(songTimeStamp)
            # GETTING THE ACTUAL VIDEO
            url = 'https://youtube.com/watch?v=' + searchResult[0]['id'] + "&t=" + str(roundedSongTimeStamp) + "s"  # This is for selecting the right video, and time. But doesnt work that way sadly, but was a good try...
            video = pafy.new(url)
            best = video.getbestvideo()
            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(best.url)
            # I want to check again where the song is, because of the loading time of the script.
            results = sp.current_user_playing_track()
            SpotifySongDuration = results['item']['duration_ms'] / 1000
            songTimeStamp = results['progress_ms'] / 1000
            roundedSongTimeStamp = math.trunc(songTimeStamp)
            # The actuaL player
            print("You are currently at: " + str(roundedSongTimeStamp) + "S" + " of the " + str(SpotifySongDuration) + "S")
            Media.add_option('start-time=' + str(songTimeStamp)) # You could add a runtime diffrence, but in my situtation it looks quite alright
            Media.get_mrl()
            player.set_media(Media)
            player.play()
            videoLength = (video.length)
            # I want to check again where the song is, because of the loading time of the script.

            time.sleep(SpotifySongDuration - roundedSongTimeStamp)
            player.stop()
            os.system("reloader.py")
            # Restarting the script ones the video ends
            # We will need another script for this one



spotiplay.EeverythingActually(1)

while True:
     pass
