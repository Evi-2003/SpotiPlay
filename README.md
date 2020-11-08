# SpotiPlay
A program to automatically find the right music video for the Spotify song, and play it in line with the song. 
So you can watch the official music video's while using Spotify. Hope you like it! 
# Usage
Change the values of: Client_ID, Client_Secret and the username. You get those from the Spotify Developer dashboard. The username is not the same as you're email. You can find your username at spotify.com and then under account. 
At your spotify dashboard you need to add the redirection url: 'http://example.com/callback/' to be accepted. 
After you have installed the requirements.
Now go play a song, and start run.py. It will immediately start the youtube video at 0:00 and not at the point where the song is in Spotify. So ones the video starts, reset your spotify song, by sliding the progress bar to the left. 

You may notice at some video's the song and the video does not go aline of eachother. Which is a irritating issue which for now i can't resolve. It is simply because of official music video's are often a bit longer then the actual song on Spotify. Which i can't detect. If the song writer is singing it can look weird if they go along. [Patch 0.91 should help! ... or a later version](https://github.com/Remco17/SpotiPlay/releases/tag/0.91)
## You can fix this by muting your Spotify and change the script line at line 49 to false. This unmutes the videos.  ---- I may make this the default, not sure yet.
# Language
I'm going to build this using Python
# API
For this to work we need to detect the song that is currently playing. Spotify has an API for this. 
For now, you need to set your own variables from the Spotify Developer website. 
# Requirements 
- Install VLC Media Player
- Python - I made it at Python 3.9
You can install those using PIP
 - python-vlc
 - spotipy
 - pafy
 - youtube_search
 - youtube-dl
 - pywin32
# Music Player
Just keep using Spotify, i only made it for spotify
# TO-DO 
- [X] Detecting the songs name + Artist
- [x] Getting the song name out of the results variable
- [x] Using the songs name to find the right music video for it using Youtube. 
- [x] Displaying the right video
- [x] When the song ends, the scripts need to be reloaded automatically
- [X] Implement a easy authorization for the user, so they don't have to edit the script --- For now impossible, from a security stand point. I can't hide the secret key. So you need to set your own. I could only do this on a server side, which i won't do. (Maybe in the future)
- [X] Finding a way to start the video at a specified point
- [X] Make the video follow the timestamp of the song - This is a hard one for now -- Need to figure out how to make the VLC video start from another time than 0:00. I found out that i could change the youtube url with the seconds played in Spotify. But sadly that's not the fix. VLC downloads the video from 0;00 so that won't work for now. 
- [ ] Asking for the client_id, client_secret, and the username. So the user doesn't have to change the script...
- [ ] Chaning the video in the VLC player without restarting the rescript. 
- [ ] Cleaning up the code




