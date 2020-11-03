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
# we need some Authentication, because who the fuck are you.
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
            print(songName)
            print(artistName)
            print(search)
            print(searchResult[0]['id'])
            songTimeStamp = results['progress_ms'] / 1000
            SpotifySongDuration = results['item']['duration_ms'] /1000
            roundedSongTimeStamp = math.trunc(songTimeStamp)
            # GETTING THE ACTUAL VIDEO
            url = 'https://youtube.com/watch?v=' + searchResult[0]['id'] + "&t=" + str(
                roundedSongTimeStamp) + "s"  # This is for selecting the right video, and time. But doesnt work that way sadly, but was a good try...
            print(url)
            video = pafy.new(url)
            best = video.getbestvideo()
            media = vlc.MediaPlayer(best.url)
            media.play()
            media.audio_set_mute(True)
            videoLength = (video.length)
            print(videoLength)
            time.sleep(SpotifySongDuration -10)
            media.stop()
            os.system("reloader.py")
            # Restarting the script ones the video ends
            # We will need another script for this one



spotiplay.EeverythingActually(1)

while True:
     pass
