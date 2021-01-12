import sys
import tkinter as tk
import pafy
import vlc
import time
from timeloop import Timeloop
from datetime import timedelta
import math
import os
import win32gui
import spotipy
from spotipy.oauth2 import SpotifyOAuth # Will be needed for the Spotify Authentication and to see which song is being played
from youtube_search import YoutubeSearch # Will be needed for downloading the associated song video
import spotipy.util as util
import configparser
import threading

print ('For this script to work you need to configure some things at the spotify developer dashboard')
print ('At the repo you must read the instructions to configure the spotify dashboard')

print ('----') 

print ('Now we will need some stuff')

# Reading the hidden config file to save the settings
config = configparser.ConfigParser()
config.read('.config.ini')
config.get('DEFAULT', 'username')
config.get('DEFAULT', 'client_id')
config.get('DEFAULT', 'client_secret')

# The script will check here if the config file already had been configured
# If the script sees that the config file is the same as the one deliverd with the standard settings it will ask for new ones
# --------
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
if config['DEFAULT']['client_secret'] == "secret":
    print("Input Client-secret... You can get it from the spotify developer dashboard")
    inputClientSecret = input()
    config.set('DEFAULT', 'client_secret', inputClientSecret)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    print("client_secret set as: " + config['DEFAULT']['client_secret'])

# We will now set the token with the information from the config file:
scope = "user-read-currently-playing"
token = util.prompt_for_user_token(
                           config['DEFAULT']['username'],
                           scope,
                           config['DEFAULT']['client_id'],
                           config['DEFAULT']['client_secret'],
                           config['DEFAULT']['redirect_uri'])

# We will be using global variables so i will be able to use variables in other functions
nameOfSong = 'none'
nameOfAuthor= 'none'
songTimeStamp = 0
songDuration = 0
spotifyResults = ''
youtubeSearchTerms = 'none'
def collectSong():
    global songDuration
    global songTimeStamp
    global nameOfSong
    global nameOfAuthor
    global spotifyResultss
    global foundVideo
    player = ''
    sp = spotipy.Spotify(auth=token)
    spotifyResults = sp.current_user_playing_track()
    nameOfAuthor = spotifyResults['item']['album']['artists'][0]['name']
    nameOfSong = spotifyResults["item"]["name"]
    songTimeStamp = spotifyResults['progress_ms'] / 1000
    songDuration = spotifyResults['item']['duration_ms'] /1000
collectSong()
oldNameOfSong = nameOfSong # Note which song currently is assigned to nameOfSong
print ("The song you are currently playing:" + " " + nameOfSong + " - Author: " + nameOfAuthor)

# The following fuction will find the correct youtube video for the song
def findMusicVideo():
    global youtubeSearchTerms
    global foundVideo
    youtubeSearchTerms = nameOfSong + " - " + nameOfAuthor
    foundVideo = YoutubeSearch(youtubeSearchTerms, max_results=1).to_dict()
    foundVideo = ('https://youtube.com/watch?v=' + foundVideo[0]['id'])
    print(foundVideo)
findMusicVideo()

# Downloading video
def downloadVideo():
    global best
    video = pafy.new(foundVideo)
    best = video.getbestvideo()
downloadVideo()

def startPlayer():
    global videoPlayer
    global musicVideo
    global Instance
    Instance = vlc.Instance()
    videoPlayer = Instance.media_player_new()
    musicVideo = Instance.media_new(best.url)

    musicVideo.add_option('start-time=' + str(songTimeStamp))
    musicVideo.get_mrl()
    # Here we will check if the song has changed
    videoPlayer.set_media(musicVideo)
    videoPlayer.play()
    videoPlayer.set_fullscreen(True)
    timeNeedtoSleep = songDuration - songTimeStamp
    timeNeedtoSleep = math.trunc(timeNeedtoSleep)
    print("The song will end in " + str(timeNeedtoSleep) + " seconds")
    time.sleep(timeNeedtoSleep)
    videoPlayer.stop()
startPlayer() # start player for first time

# Checking which song is playing when the song ends
collectSong()
print('new song collected')
findMusicVideo()
print("found music video")
downloadVideo()
print('downloaded video')
startPlayer()
print('has started player')



# This is currently not working, i'm working on this. If someone can help me with this would be awesome! ;)
#def hasSongChanged():
 #       collectSong()
 #       if nameOfSong != oldNameOfSong:
 #           findMusicVideo()
 #           downloadVideo()
 #           time.sleep(3)
 #          musicVideo = Instance.media_new(best.url)
 #           musicVideo.add_option('start-time=' + str(songTimeStamp))
 #          musicVideo.get_mrl()
 #          videoPlayer.set_media(musicVideo)

