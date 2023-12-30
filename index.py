from pytube import YouTube, Playlist
import sys

playlist_URL = sys.argv[1]

playlist = Playlist(playlist_URL)

for video_URL in playlist: 
  yt = YouTube(video_URL)
  yt.streams.filter(only_audio=True).first().download("downloads")