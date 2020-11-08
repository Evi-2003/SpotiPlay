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
import configparser

# We need some Authentication.
# The Client_ID Client_Secret And Username needs to be set by yourself, for now.
config = configparser.ConfigParser()
config.read('config.ini')
config.get('DEFAULT', 'username')
config.get('DEFAULT', 'client_id')
config.get('DEFAULT', 'client_secret')

# Getting the username
if config['DEFAULT']['username'] == "username":
    print("Input username. ( It is not the same as your e-mail.  It's a weird username which you can find on spotify.com at your account")
    inputUsername = input()
    config.set('DEFAULT', 'username', inputUsername)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    print("Username set as: " + config['DEFAULT']['username'])

# Getting te client_id
if config['DEFAULT']['client_id'] == "id":
    print("Input Client-ID... You can get it from the spotify developer dashboard")
    inputClientID = input()
    config.set('DEFAULT', 'client_id', inputClientID)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    print("client_id set as: " + config['DEFAULT']['client_id'])

# Getting the client_secret
if config['DEFAULT']['knowsOfUri'] == "false":
    print("Add to your spotify dashboard the redirection url: 'http://example.com/callback/' This will only be shown one time. ")
    inputClientSecret = input()
    true = 'true'
    config.set('DEFAULT', 'knowsOfUri', true)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    print("Have a nice day!")
# Making user aware of the redirection url
if config['DEFAULT']['client_secret'] == "secret":
    print("Input Client-secret... You can get it from the spotify developer dashboard")
    inputClientSecret = input()
    config.set('DEFAULT', 'client_secret', inputClientSecret)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    print("client_secret set as: " + config['DEFAULT']['client_secret'])
# staring script
scope = "user-read-currently-playing"
token = util.prompt_for_user_token(
                           config['DEFAULT']['username'],
                           scope,
                           config['DEFAULT']['client_id'],
                           config['DEFAULT']['client_secret'],
                           config['DEFAULT']['redirect_uri'])

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
            Media.add_option('start-time=' + str(songTimeStamp)) #1s run time diffrence
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
